*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#mdn-search)
    

import.defer()
==============

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/919)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#browser_compatibility)
 carefully before using this in production.

The **`import.defer()`** syntax behaves like regular [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
 syntax, except that it results in a [deferred module namespace object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer#deferred_module_namespace_object)
. The module and its dependencies are [fetched](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#loading_the_graph)
 and [linked](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#linking_modules)
 up front, but their synchronous [evaluation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#evaluating_modules)
 is deferred until the namespace's properties are accessed.

For more information about deferred evaluation, including its interaction with top-level `await`, see the [`import defer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer)
 declaration form.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#syntax)

----------------------------------------------------------------------------------------------------------

js

    import.defer(moduleName)
    import.defer(moduleName, options)
    

`import.defer()` is special syntax (a "meta property"), not a method on an `import` object.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#parameters)

See [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import#parameters)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#return_value)

Returns a promise that fulfills with a [deferred module namespace object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer#deferred_module_namespace_object)
 after the module graph is [loaded](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#loading_the_graph)
 and linked, and any eagerly evaluated [top-level `await` dependencies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer#top-level_await)
 have finished evaluating.

Like regular [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import#return_value)
, the promise rejects if the module or its dependencies cannot be loaded, parsed, or linked. It also rejects if an eagerly evaluated module throws. Errors from evaluation that remains deferred are instead thrown synchronously by the namespace operation that triggers evaluation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#examples)

--------------------------------------------------------------------------------------------------------------

### [Using import.defer()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#using_import.defer)

**Note:** It's guaranteed that awaiting the resulting promise never accidentally calls an exported `then` method—a gotcha associated with the [regular module namespace object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import#module_namespace_object)
—because the deferred module namespace object never exposes a property called `then`.

js

    const ts = await import.defer("typescript");
    
    function compilePath(path) {
      // Evaluation of the typescript module subgraph starts here
      const program = ts.createProgram([path], {});
    }
    

Never immediately destructure the returned namespace, because it triggers evaluation:

js

    const { createProgram } = await import.defer("typescript");
    // The typescript module has now been evaluated.
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Deferred Imports Evaluation  <br>\# sec-left-hand-side-expressions](https://tc39.es/proposal-defer-import-eval/#sec-left-hand-side-expressions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer#see_also)

--------------------------------------------------------------------------------------------------------------

*   [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
     guide
*   [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)
    
*   [`import defer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/import/defer/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/import/defer (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fimport%2Fdefer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fimport%2Fdefer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fimport%2Fdefer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fimport%2Fdefer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")