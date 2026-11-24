#!/usr/bin/env node
// Copies the version changesets wrote to ./package.json into the root of
// package-lock.json and every file Fern writes it into, so a release carries
// one version everywhere. Given a version, it writes package.json too: the
// publish and release jobs rebuild the version commit that way without
// running any dependency's code.
//
// Usage: node scripts/sync-version.mjs <python|python-internal|java|typescript|go> [version]
//
// From hl-sdk-gen's template/; edit it there and copy it into every SDK repo.
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";
import { pathToFileURL } from "node:url";

/**
 * @typedef {{ file: string, pattern: RegExp }} Target
 * Each pattern must match its file exactly once; its first group is the version.
 */

/** @type {Record<string, Target[]>} */
export const TARGETS = {
  python: [
    { file: "pyproject.toml", pattern: /^version = "([^"]+)"$/m },
    { file: "src/hiddenlayer/core/client_wrapper.py", pattern: /"X-Fern-SDK-Version": "([^"]+)"/ },
    // Fern writes this header only for a generator with an output block, which the internal one lacks.
    { file: "src/hiddenlayer/core/client_wrapper.py", pattern: /"User-Agent": "[^"]*\/([^"]+)"/ },
  ],
  "python-internal": [
    { file: "pyproject.toml", pattern: /^version = "([^"]+)"$/m },
    { file: "src/hiddenlayer_internal/core/client_wrapper.py", pattern: /"X-Fern-SDK-Version": "([^"]+)"/ },
  ],
  java: [
    // Fern writes no version into build.gradle without an output block, so the repo owns gradle.properties.
    { file: "gradle.properties", pattern: /^version=(.+)$/m },
    { file: "src/main/java/com/hiddenlayer/api/core/ClientOptions.java", pattern: /put\("X-Fern-SDK-Version", "([^"]+)"\)/ },
  ],
  typescript: [
    { file: "src/version.ts", pattern: /SDK_VERSION = "([^"]+)"/ },
    { file: "src/BaseClient.ts", pattern: /"X-Fern-SDK-Version": "([^"]+)"/ },
    { file: "src/BaseClient.ts", pattern: /"User-Agent": "[^"]*\/([^"]+)"/ },
  ],
  go: [
    { file: "core/request_option.go", pattern: /"X-Fern-SDK-Version", "v([^"]+)"/ },
    { file: "core/request_option.go", pattern: /"User-Agent", "[^"]*\/([^"]+)"/ },
  ],
};

/**
 * Replaces the version that `pattern` captures in `content`.
 * @param {string} content
 * @param {RegExp} pattern
 * @param {string} version
 * @returns {string}
 */
export function rewrite(content, pattern, version) {
  const matches = [...content.matchAll(new RegExp(pattern.source, `${pattern.flags}dg`))];
  if (matches.length !== 1) {
    throw new Error(`expected one match for ${pattern}, found ${matches.length}`);
  }
  const [start, end] = /** @type {[number, number]} */ (matches[0].indices?.[1]);
  return content.slice(0, start) + version + content.slice(end);
}

/** @param {unknown} error */
function errorMessage(error) {
  return typeof error === "object" && error !== null && "message" in error ? String(error.message) : String(error);
}

/**
 * Rewrites a JSON file through `update`, keeping its indentation and final newline.
 * @param {string} filePath
 * @param {(json: { version?: string, packages?: Record<string, { version?: string }> }) => void} update
 */
function updateJson(filePath, update) {
  const text = readFileSync(filePath, "utf8");
  const json = JSON.parse(text);
  update(json);
  const indent = /^([ \t]+)"/m.exec(text)?.[1] ?? 2;
  writeFileSync(filePath, JSON.stringify(json, null, indent) + (text.endsWith("\n") ? "\n" : ""));
}

/**
 * Writes `version`, or the one in `dir`/package.json, into package.json, the
 * root of package-lock.json when there is one, and every target file for `language`.
 * @param {string} dir
 * @param {string} language
 * @param {string} [version]
 * @returns {string} the version written
 */
export function syncVersion(dir, language, version) {
  const targets = TARGETS[language];
  if (!targets) {
    throw new Error(`unknown language ${language}; expected one of ${Object.keys(TARGETS).join(", ")}`);
  }
  const packageJson = path.join(dir, "package.json");
  version ??= JSON.parse(readFileSync(packageJson, "utf8")).version;
  if (typeof version !== "string" || !/^\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?$/.test(version)) {
    throw new Error(`version ${JSON.stringify(version)} is not a semver version`);
  }
  const semver = version;
  updateJson(packageJson, (json) => {
    json.version = semver;
  });
  const lockfile = path.join(dir, "package-lock.json");
  if (existsSync(lockfile)) {
    updateJson(lockfile, (json) => {
      json.version = semver;
      if (json.packages?.[""]) {
        json.packages[""].version = semver;
      }
    });
  }
  for (const { file, pattern } of targets) {
    const filePath = path.join(dir, file);
    try {
      writeFileSync(filePath, rewrite(readFileSync(filePath, "utf8"), pattern, version));
    } catch (error) {
      throw new Error(`${file}: ${errorMessage(error)}`);
    }
  }
  return version;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    const version = syncVersion(process.cwd(), process.argv[2] ?? "", process.argv[3]);
    console.log(`sync-version: wrote ${version}`);
  } catch (error) {
    console.error(`sync-version: ${errorMessage(error)}`);
    process.exit(1);
  }
}
