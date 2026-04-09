// scripts/utils/generate-beta-endpoints.cjs
//
// Scans generated resource files for [BETA] docstrings and extracts
// URL paths from self._post / _get / _put / _patch / _delete calls.
// Produces src/hiddenlayer/lib/_beta_endpoints.py with a mapping of
// path -> ClassName.method_name.

const fs = require("fs");
const path = require("path");

const RESOURCES_DIR = path.resolve(
  __dirname,
  "../../src/hiddenlayer/resources"
);
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
 * Extract beta endpoint mappings from a single resource file.
 *
 * Strategy:
 *  1. Find sync resource classes (inherits SyncAPIResource).
 *  2. For each class, find methods whose docstring contains [BETA].
 *  3. For each beta method, find the URL path in a self._<verb>("/path", ...) call.
 */
function extractBetaEndpoints(source) {
  const lines = source.split("\n");
  const entries = {}; // path -> ClassName.method_name

  let currentSyncClass = null;
  let insideAsyncClass = false;
  let classIndent = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Detect class declarations
    const classMatch = line.match(
      /^(\s*)class\s+(\w+)\((SyncAPIResource|AsyncAPIResource)\)/
    );
    if (classMatch) {
      const indent = classMatch[1].length;
      const className = classMatch[2];
      const baseClass = classMatch[3];
      if (baseClass === "AsyncAPIResource") {
        insideAsyncClass = true;
        currentSyncClass = null;
        classIndent = indent;
      } else {
        insideAsyncClass = false;
        currentSyncClass = className;
        classIndent = indent;
      }
      continue;
    }

    // If we hit another top-level class that isn't Sync/Async resource, reset
    const otherClassMatch = line.match(/^(\s*)class\s+\w+/);
    if (otherClassMatch && otherClassMatch[1].length <= classIndent) {
      if (!line.match(/\((SyncAPIResource|AsyncAPIResource)\)/)) {
        currentSyncClass = null;
        insideAsyncClass = false;
      }
    }

    // Skip async classes entirely
    if (insideAsyncClass) continue;
    if (!currentSyncClass) continue;

    // Detect method definitions
    const defMatch = line.match(/^\s+(?:async\s+)?def\s+(\w+)\s*\(/);
    if (!defMatch) continue;

    const methodName = defMatch[1];
    // Skip dunder and private methods
    if (methodName.startsWith("_")) continue;

    // Look ahead for the docstring and check for [BETA]
    const isBeta = docstringContainsBeta(lines, i + 1);
    if (!isBeta) continue;

    // Look ahead for the URL path in self._<verb>("...")
    const urlPath = findUrlPath(lines, i + 1);
    if (!urlPath) continue;

    entries[urlPath] = `${currentSyncClass}.${methodName}`;
  }

  return entries;
}

/**
 * Starting from lineIndex, check if the next docstring contains [BETA].
 * Scans forward through the function signature and into the body looking
 * for a triple-quoted docstring. Bails if it hits another def or class.
 */
function docstringContainsBeta(lines, startIndex) {
  for (let i = startIndex; i < lines.length && i < startIndex + 40; i++) {
    const trimmed = lines[i].trim();

    // Stop if we hit another method def or a top-level class
    if (i > startIndex && /^\s{4}(async\s+)?def\s/.test(lines[i])) return false;
    if (/^class\s/.test(lines[i])) return false;

    // Look for triple-quote docstring start
    if (trimmed.startsWith('"""') || trimmed.startsWith("'''")) {
      if (trimmed.includes("[BETA]")) return true;
      const quote = trimmed.slice(0, 3);
      // Single-line docstring that opened and closed on the same line
      if (trimmed.endsWith(quote) && trimmed.length > 3) return false;
      // Multi-line: scan until closing triple-quote
      for (let j = i + 1; j < lines.length && j < i + 50; j++) {
        if (lines[j].includes("[BETA]")) return true;
        if (lines[j].trim().endsWith(quote)) return false;
      }
      return false;
    }
  }
  return false;
}

/**
 * Starting from lineIndex, find a self._<verb>("/path", ...) call.
 *
 * Stainless-generated code often splits self._post( and the URL onto
 * separate lines, so we handle both single-line and multi-line forms:
 *   self._post("/path", ...)          -- single line
 *   self._post(                       -- verb on one line
 *       "/path",                      -- URL on the next
 */
function findUrlPath(lines, startIndex) {
  const singleLinePattern =
    /self\._(?:post|get|put|patch|delete)\(\s*"(\/[^"]+)"/;
  const verbOpenPattern = /self\._(?:post|get|put|patch|delete)\(\s*$/;
  const urlPattern = /^\s*"(\/[^"]+)"/;

  for (let i = startIndex; i < lines.length && i < startIndex + 80; i++) {
    // Single-line form: self._post("/path", ...)
    const singleMatch = lines[i].match(singleLinePattern);
    if (singleMatch) return singleMatch[1];

    // Multi-line form: self._post(\n    "/path",
    const verbMatch = lines[i].match(verbOpenPattern);
    if (verbMatch && i + 1 < lines.length) {
      const urlMatch = lines[i + 1].match(urlPattern);
      if (urlMatch) return urlMatch[1];
    }

    // Stop if we hit the next def or class
    if (
      lines[i].match(/^\s{4}(?:async\s+)?def\s/) ||
      lines[i].match(/^class\s/)
    ) {
      break;
    }
  }
  return null;
}

// ---------------------------------------------------------------------------
// Output
// ---------------------------------------------------------------------------

function buildOutput(allEntries) {
  // Sort entries by path for deterministic output
  const sortedPaths = Object.keys(allEntries).sort();

  const pairs = sortedPaths
    .map((p) => `    "${p}": "${allEntries[p]}",`)
    .join("\n");

  return `"""Auto-generated registry of beta endpoints.

DO NOT EDIT -- regenerated by scripts/utils/generate-beta-endpoints.cjs

Maps URL paths to qualified method names for runtime warnings.
"""
from __future__ import annotations

BETA_ENDPOINTS: dict[str, str] = {
${pairs}
}
`;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main() {
  const files = walkPythonFiles(RESOURCES_DIR);
  const allEntries = {};

  for (const file of files) {
    const source = fs.readFileSync(file, "utf-8");
    const entries = extractBetaEndpoints(source);
    Object.assign(allEntries, entries);
  }

  const count = Object.keys(allEntries).length;
  const output = buildOutput(allEntries);

  fs.writeFileSync(OUTPUT_FILE, output, "utf-8");
  console.log(`Wrote ${count} beta endpoint(s) to ${OUTPUT_FILE}`);
}

main();
