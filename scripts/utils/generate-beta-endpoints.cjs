// scripts/utils/generate-beta-endpoints.cjs
//
// Scans generated resource files for [BETA] docstrings and extracts URL paths
// from self._post / _get / _put / _patch / _delete calls. Produces
// src/hiddenlayer/lib/_beta_endpoints.py with a list of (path pattern, qualified
// method name) entries used for runtime warnings.
//
// Paths are stored as segment patterns rather than literal strings so that
// endpoints with path parameters (e.g. /evaluations/v1/red-team/{workflow_id}/status)
// are matched even though the runtime URL has the parameter value substituted in.
// A segment of None is a wildcard matching any single path segment.

const fs = require("fs");
const path = require("path");

const RESOURCES_DIR = path.resolve(__dirname, "../../src/hiddenlayer/resources");
const OUTPUT_FILE = path.resolve(
  __dirname,
  "../../src/hiddenlayer/lib/_beta_endpoints.py"
);

// ---------------------------------------------------------------------------
// File discovery
// ---------------------------------------------------------------------------

function walkPythonFiles(dir) {
  const results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...walkPythonFiles(full));
    } else if (entry.name.endsWith(".py") && entry.name !== "__init__.py") {
      results.push(full);
    }
  }
  return results;
}

// ---------------------------------------------------------------------------
// Parsing
// ---------------------------------------------------------------------------

/**
 * Convert a captured URL path into a segment pattern. Literal segments stay as
 * strings; any segment containing a `{...}` path parameter becomes `null`, a
 * wildcard matching any single segment at request time.
 *
 * @param {string} rawPath
 * @returns {Array<string | null>}
 */
function toSegments(rawPath) {
  return rawPath
    .replace(/^\//, "")
    .split("/")
    .filter((s) => s.length > 0)
    .map((s) => (s.includes("{") ? null : s));
}

/**
 * Collect, in document order, the sync resource methods in a file along with
 * the line range of each method body. Only classes inheriting SyncAPIResource
 * are considered (async classes resolve to the same paths, so one entry per
 * path is enough).
 *
 * @param {string[]} lines
 * @returns {Array<{ className: string, methodName: string, start: number, end: number }>}
 */
function collectSyncMethods(lines) {
  const methods = [];
  let currentSyncClass = null;
  let classIndent = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    const classMatch = line.match(/^(\s*)class\s+(\w+)\(([^)]*)\)/);
    if (classMatch) {
      const indent = classMatch[1].length;
      const className = classMatch[2];
      const bases = classMatch[3];
      if (/\bSyncAPIResource\b/.test(bases)) {
        currentSyncClass = className;
        classIndent = indent;
      } else {
        // Any other class (async resource, response wrappers, etc.) ends the
        // current sync class context.
        currentSyncClass = null;
      }
      continue;
    }

    if (!currentSyncClass) continue;

    const defMatch = line.match(/^(\s+)(?:async\s+)?def\s+(\w+)\s*\(/);
    if (!defMatch) continue;
    if (defMatch[1].length <= classIndent) continue; // not a method of this class
    const methodName = defMatch[2];
    if (methodName.startsWith("_")) continue;

    methods.push({ className: currentSyncClass, methodName, start: i, end: lines.length });
  }

  // Bound each method body by the start of the next method/class.
  for (let m = 0; m < methods.length; m++) {
    methods[m].end = m + 1 < methods.length ? methods[m + 1].start : lines.length;
  }
  return methods;
}

/** @param {string[]} bodyLines */
function bodyHasBeta(bodyLines) {
  return bodyLines.some((l) => l.includes("[BETA]"));
}

/**
 * Find the request URL path in a method body. Handles both a plain string path
 * (`self._post("/path", ...)`) and the path_template form used for endpoints
 * with parameters (`self._get(path_template("/path/{id}", id=id), ...)`).
 *
 * @param {string[]} bodyLines
 * @returns {string | null}
 */
function findUrlPath(bodyLines) {
  const text = bodyLines.join("\n");
  const verb = text.match(/self\._(?:post|get|put|patch|delete)\s*\(/);
  if (!verb) return null;
  const after = text.slice(verb.index);
  // First double-quoted string after the verb call, optionally wrapped in
  // path_template(...). Both forms start the path with a leading slash.
  const pathMatch = after.match(/(?:path_template\s*\(\s*)?"(\/[^"]*)"/);
  return pathMatch ? pathMatch[1] : null;
}

/**
 * @param {string} source
 * @returns {Array<{ segments: Array<string | null>, method: string }>}
 */
function extractBetaEndpoints(source) {
  const lines = source.split("\n");
  const results = [];

  for (const { className, methodName, start, end } of collectSyncMethods(lines)) {
    const body = lines.slice(start, end);
    if (!bodyHasBeta(body)) continue;
    const urlPath = findUrlPath(body);
    if (!urlPath) continue;
    results.push({ segments: toSegments(urlPath), method: `${className}.${methodName}` });
  }

  return results;
}

// ---------------------------------------------------------------------------
// Output
// ---------------------------------------------------------------------------

/** @param {Array<string | null>} segments */
function segmentsKey(segments) {
  return segments.map((s) => (s === null ? "*" : s)).join("/");
}

function buildOutput(entries) {
  entries.sort((a, b) => segmentsKey(a.segments).localeCompare(segmentsKey(b.segments)));

  const rows = entries
    .map((e) => {
      const items = e.segments.map((s) => (s === null ? "None" : `"${s}"`));
      // A single-element tuple needs a trailing comma; multi-element tuples omit
      // it to avoid ruff's magic-trailing-comma line explosion.
      const tuple = items.length === 1 ? `(${items[0]},)` : `(${items.join(", ")})`;
      return `    (${tuple}, "${e.method}"),`;
    })
    .join("\n");

  return `"""Auto-generated registry of beta endpoints.

DO NOT EDIT -- regenerated by scripts/utils/generate-beta-endpoints.cjs

Each entry is a (path pattern, qualified method name) pair. A path pattern is a
tuple of segments where a string is a literal match and None is a wildcard that
matches any single path-parameter segment. Used for runtime beta warnings.
"""

from __future__ import annotations

BETA_ENDPOINTS: list[tuple[tuple[str | None, ...], str]] = [
${rows}
]
`;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main() {
  const files = walkPythonFiles(RESOURCES_DIR);
  const all = [];

  for (const file of files) {
    all.push(...extractBetaEndpoints(fs.readFileSync(file, "utf-8")));
  }

  // Deduplicate by rendered pattern (sync + async classes share paths; we only
  // scanned sync, but guard anyway).
  const seen = new Set();
  const unique = [];
  for (const e of all) {
    const key = segmentsKey(e.segments);
    if (seen.has(key)) continue;
    seen.add(key);
    unique.push(e);
  }

  fs.writeFileSync(OUTPUT_FILE, buildOutput(unique), "utf-8");
  console.log(`Wrote ${unique.length} beta endpoint(s) to ${OUTPUT_FILE}`);
  for (const e of unique) {
    console.log(`  /${segmentsKey(e.segments)} -> ${e.method}`);
  }
}

main();
