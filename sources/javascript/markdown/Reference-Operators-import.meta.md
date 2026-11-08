*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#mdn-search)
    

import.meta
===========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`import.meta`** meta-property exposes context-specific metadata to a JavaScript module. It contains information about the module, such as the module's URL.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#syntax)

---------------------------------------------------------------------------------------------------------

### [Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#value)

The `import.meta` object is created by the host environment, as an extensible [`null`\-prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#null-prototype_objects)
 object where all properties are writable, configurable, and enumerable. The spec doesn't specify any properties to be defined on it, but hosts usually implement the following properties:

[`url`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#url)

The full URL to the module, includes query parameters and/or hash (following the `?` or `#`). In browsers, this is either the URL from which the script was obtained (for external scripts), or the document's base URL when the module script was created (for inline scripts). In Node.js, file-based modules use a `file:` URL, while modules loaded from other supported URL schemes use their corresponding URLs.

[`resolve`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/resolve)

Resolves a module specifier to a URL using the current module's URL as base.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#description)

-------------------------------------------------------------------------------------------------------------------

The `import.meta` syntax consists of the keyword `import`, a dot, and the identifier `meta`. Because `import` is a [reserved word](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words)
, not an identifier, this is not a [property accessor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
, but a special expression syntax.

The `import.meta` meta-property is available in JavaScript modules; using `import.meta` outside of a module (including [direct `eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#direct_and_indirect_eval)
 within a module) is a syntax error.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#examples)

-------------------------------------------------------------------------------------------------------------

### [Passing query parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#passing_query_parameters)

Using query parameters in the `import` specifier allows module-specific argument passing, which may be complementary to reading parameters from the application-wide [`window.location`](https://developer.mozilla.org/en-US/docs/Web/API/Window/location)
 (or on Node.js, through `process.argv`). For example, with the following HTML:

The `index.mjs` module is able to retrieve the `someURLInfo` parameter through `import.meta`:

The same applies when a module imports another:

The ES module implementation in Node.js supports resolving module specifiers containing query parameters (or the hash), as in the latter example. However, you cannot use queries or hashes when the module is specified through the CLI command (like `node index.mjs?someURLInfo=5`), because the CLI entrypoint uses a more CommonJS-like resolution mode, treating the path as a file path rather than a URL. To pass parameters to the entrypoint module, use CLI arguments and read them through `process.argv` instead (like `node index.mjs --someURLInfo=5`).

### [Resolving a file relative to the current one](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#resolving_a_file_relative_to_the_current_one)

In Node.js CommonJS modules, there's a `__dirname` variable that contains the absolute path to the folder containing current module, which is useful for resolving relative paths. However, Node.js does not provide this variable in ES modules. To resolve a relative file you can use `import.meta.url`. Note that this uses URLs rather than filesystem paths.

Before (CommonJS):

After (ES modules):

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-ImportMeta](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-ImportMeta) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    
*   [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/import.meta/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/import.meta (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fimport.meta&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fimport.meta%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fimport.meta%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fimport.meta%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")