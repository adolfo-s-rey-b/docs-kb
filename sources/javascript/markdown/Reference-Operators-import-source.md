*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#mdn-search)
    

import.source()
===============

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#browser_compatibility)
 carefully before using this in production.

The **`import.source()`** syntax behaves like regular [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
 syntax, except that it results in an object that represents the module's compiled source code. The module is [fetched and compiled](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#loading_the_graph)
, but its dependencies are not loaded and it is not [linked](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#linking_modules)
 or [evaluated](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#evaluating_modules)
. It can be imperatively evaluated later, such as by using [dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
 or [`WebAssembly.instantiate()`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/instantiate_static)
.

To use `import.source()`, the target module must be of a kind that supports source phase imports. Currently, only WebAssembly modules support source phase imports, and result in [`WebAssembly.Module`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/Module)
 objects. JavaScript module source objects will be added by the [ECMAScript Module Phase Imports](https://github.com/tc39/proposal-esm-phase-imports "External link (opens in new tab)")
 proposal.

For more information about the semantics of source phase imports, see the [`import source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source)
 declaration form.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#syntax)

-----------------------------------------------------------------------------------------------------------

`import.source()` is special syntax (a "meta property"), not a method on an `import` object.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#parameters)

See [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import#parameters)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#return_value)

Returns a promise that fulfills with an [`AbstractModuleSource`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource)
 object representing the module's compiled source after the module is loaded and compiled successfully.

Like regular [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import#return_value)
, the promise rejects if the module cannot be loaded or parsed. It also rejects with a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
 if the module type does not support source phase imports. The import does not load dependencies, link, or evaluate the module, so errors from those later steps are not reported.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#examples)

---------------------------------------------------------------------------------------------------------------

### [Using import.source()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#using_import.source)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Source Phase Imports  <br>\# sec-left-hand-side-expressions](https://tc39.es/proposal-source-phase-imports/#sec-left-hand-side-expressions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source#see_also)

---------------------------------------------------------------------------------------------------------------

*   [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
     guide
*   [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
    
*   [`import source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source)
    
*   [`AbstractModuleSource`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AbstractModuleSource)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/import/source/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/import/source (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fimport%2Fsource&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fimport%2Fsource%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fimport%2Fsource%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fimport%2Fsource%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")