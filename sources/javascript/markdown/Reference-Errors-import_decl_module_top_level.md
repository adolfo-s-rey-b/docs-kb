*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level#mdn-search)
    

SyntaxError: import declarations may only appear at top level of a module
=========================================================================

The JavaScript exception "import declarations may only appear at top level of a module" occurs when an import declaration is not at the top level of a module. This might be because the import declaration is nested in other constructs (functions, blocks, etc.), or more often because the current file is not treated as a module.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level#message)

-------------------------------------------------------------------------------------------------------------------------

SyntaxError: Cannot use import statement outside a module (V8-based)
SyntaxError: import declarations may only appear at top level of a module (Firefox)
SyntaxError: Unexpected identifier 'x'. import call expects one or two arguments. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level#error_type)

-------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------------------

You may have an `import` declaration that's nested in another construct, such as a function or a block. The `import` declaration must be at the top level of the module. If you want to conditionally import a module, or lazily import it on demand, use [dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
 instead.

If the `import` is already at the top level of the code, it may be because the file is not interpreted as a module. Runtimes require external hints to determine whether a file is a module or not, and here are several ways to provide such hints:

*   If the file is directly loaded from HTML, make sure the [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
     tag has the `type="module"` attribute.
*   If the file is run in Node, make sure either the file has the `.mjs` extension, or the closest `package.json` file has the `"type": "module"` field.
*   If the file is run as a [worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
    , make sure you call the `Worker()` constructor with the `type: "module"` option.
*   Import this file from another module.

One other cause might be when you are writing `import` with a compiler (such as TypeScript) and you accidentally ran the source file. Since `import` declarations usually appear at the very start of the program, they are the first thing the parser sees and then complains about. Make sure to compile the source file and execute the compiled file instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Conditional imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level#conditional_imports)

You cannot use `import` inside other constructs, like you might do in Python.

Either move the `import` to the top level, or use dynamic import.

### [Importing in a non-module script](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level#importing_in_a_non-module_script)

If you are loading the script from HTML, make sure to add the `type="module"` attribute to the `<script>` tag.

If for some reason you cannot migrate the script to a module, you can use dynamic import.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [Using modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    
*   [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    
*   [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/import_decl_module_top_level/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/import_decl_module_top_level/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/import_decl_module_top_level (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2Fimport_decl_module_top_level&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fimport_decl_module_top_level%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2Fimport_decl_module_top_level%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fimport_decl_module_top_level%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")