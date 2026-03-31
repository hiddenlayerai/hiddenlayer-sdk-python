// @ts-check
const fs = require('fs');
const path = require('path');

const resourcesDir = path.resolve(__dirname, '..', '..', 'src', 'hiddenlayer', 'resources');

/**
 * Recursively walk a directory yielding file paths.
 */
async function* walk(dir) {
  for await (const d of await fs.promises.opendir(dir)) {
    const entry = path.join(dir, d.name);
    if (d.isDirectory()) yield* walk(entry);
    else if (d.isFile()) yield entry;
  }
}

/**
 * Compute the relative import path from a resource file to the lib._beta module.
 * e.g. resources/scans/jobs.py (depth 2) → "...lib._beta"
 */
function computeImportPrefix(filePath) {
  const rel = path.relative(resourcesDir, filePath);
  // Count directory separators to determine depth
  const depth = rel.split(path.sep).length; // file itself counts as 1
  // From resources/foo.py we need "..lib._beta" (2 dots = up to package root)
  // From resources/scans/jobs.py we need "...lib._beta" (3 dots)
  return '.'.repeat(depth + 1);
}

/**
 * Extract class names that extend SyncAPIResource or AsyncAPIResource.
 */
function extractClassNames(content) {
  const classes = [];
  const pattern = /class\s+(\w+)\((Sync|Async)APIResource\)/g;
  let match;
  while ((match = pattern.exec(content)) !== null) {
    classes.push(match[1]);
  }
  return classes;
}

/**
 * Patch a single resource file: insert or remove warn_beta calls
 * based on whether methods have [BETA] in their docstrings.
 *
 * Returns the (possibly modified) content, or null if no changes needed.
 */
function patchFile(content, filePath) {
  const classNames = extractClassNames(content);
  if (classNames.length === 0) return null;

  // Build a map of class name → line range so we can attribute methods to classes
  const classRanges = [];
  for (const className of classNames) {
    const classPattern = new RegExp(`class\\s+${className}\\(`);
    const match = classPattern.exec(content);
    if (match) {
      classRanges.push({ name: className, start: match.index });
    }
  }
  classRanges.sort((a, b) => a.start - b.start);

  // Find all method definitions with their docstrings.
  // Pattern: optional "async" then "def methodname(" followed eventually by a docstring.
  // The leading capture group grabs only the whitespace indentation, not the "async" keyword.
  const methodPattern =
    /( +)(?:async\s+)?def\s+(\w+)\s*\([^)]*\)[^:]*:\s*\n\s+"""([\s\S]*?)"""/g;

  const edits = [];
  let match;

  while ((match = methodPattern.exec(content)) !== null) {
    const indent = match[1];
    const methodName = match[2];
    const docstring = match[3];
    const fullMatch = match[0];
    const matchEnd = match.index + fullMatch.length;

    // Skip private/dunder methods and property accessors
    if (methodName.startsWith('_')) continue;
    if (methodName === 'with_raw_response' || methodName === 'with_streaming_response')
      continue;

    // Determine which class this method belongs to
    let className = null;
    for (let i = classRanges.length - 1; i >= 0; i--) {
      if (match.index > classRanges[i].start) {
        className = classRanges[i].name;
        break;
      }
    }
    if (!className) continue;

    const qualifiedName = `${className}.${methodName}`;
    const warnCall = `warn_beta("${qualifiedName}")`;
    const isBeta = docstring.includes('[BETA]');

    if (isBeta && !content.includes(warnCall)) {
      // Insert warn_beta call after the closing """
      const bodyIndent = indent + '    ';
      edits.push({
        type: 'insert',
        index: matchEnd,
        text: '\n' + bodyIndent + warnCall,
      });
    } else if (!isBeta) {
      // Remove any existing warn_beta call for this method
      const warnPattern = new RegExp(
        `\\n\\s*warn_beta\\("${escapeRegExp(qualifiedName)}"\\)`,
      );
      const warnMatch = content.match(warnPattern);
      if (warnMatch && warnMatch.index !== undefined) {
        edits.push({
          type: 'remove',
          index: warnMatch.index,
          length: warnMatch[0].length,
        });
      }
    }
  }

  if (edits.length === 0) {
    return manageImport(content, filePath);
  }

  // Apply edits bottom-up
  edits.sort((a, b) => (b.index || 0) - (a.index || 0));
  let modified = content;
  for (const edit of edits) {
    if (edit.type === 'insert') {
      modified =
        modified.slice(0, edit.index) + edit.text + modified.slice(edit.index);
    } else if (edit.type === 'remove') {
      modified =
        modified.slice(0, edit.index) +
        modified.slice(edit.index + edit.length);
    }
  }

  // Manage import
  const result = manageImport(modified, filePath);
  return result !== null ? result : modified !== content ? modified : null;
}

/**
 * Add or remove the warn_beta import as needed.
 */
function manageImport(content, filePath) {
  const hasAnyCalls = /warn_beta\(/.test(content);
  const importPrefix = computeImportPrefix(filePath);
  const importStatement = `from ${importPrefix}lib._beta import warn_beta`;
  const hasImport = content.includes('warn_beta') && content.includes('from') && /from\s+\.+lib\._beta\s+import\s+warn_beta/.test(content);

  let modified = content;

  if (hasAnyCalls && !hasImport) {
    // Add import after the last existing import line
    const importPattern = /^from\s.+import\s.+$/gm;
    let lastIndex = -1;
    let m;
    while ((m = importPattern.exec(modified)) !== null) {
      lastIndex = m.index + m[0].length;
    }
    if (lastIndex !== -1) {
      modified =
        modified.slice(0, lastIndex) +
        '\n' +
        importStatement +
        modified.slice(lastIndex);
    }
  } else if (!hasAnyCalls && hasImport) {
    modified = modified.replace(
      new RegExp(`\\nfrom\\s+\\.+lib\\._beta\\s+import\\s+warn_beta`),
      '',
    );
  }

  return modified !== content ? modified : null;
}

function escapeRegExp(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

async function main() {
  let patchedCount = 0;

  for await (const filePath of walk(resourcesDir)) {
    if (!filePath.endsWith('.py')) continue;
    if (path.basename(filePath) === '__init__.py') continue;

    const content = await fs.promises.readFile(filePath, 'utf8');

    // Skip files without resource classes
    if (
      !content.includes('SyncAPIResource') &&
      !content.includes('AsyncAPIResource')
    )
      continue;

    const patched = patchFile(content, filePath);
    if (patched !== null) {
      await fs.promises.writeFile(filePath, patched, 'utf8');
      const rel = path.relative(process.cwd(), filePath);
      console.log(`patched ${rel}`);
      patchedCount++;
    }
  }

  console.log(`\n${patchedCount} file(s) patched.`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
