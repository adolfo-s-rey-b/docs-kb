*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#mdn-search)
    

SyntaxError: function statement requires a name
===============================================

The JavaScript exception "function statement requires a name" occurs when there is a [function statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
 in the code that requires a name.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#message)

-----------------------------------------------------------------------------------------------------------------------

SyntaxError: Function statements require a function name (V8-based)
SyntaxError: function statement requires a name (Firefox)
SyntaxError: Function statements must have a name. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#error_type)

-----------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#what_went_wrong)

----------------------------------------------------------------------------------------------------------------------------------------

There is a [function statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
 in the code that requires a name. You'll need to check how functions are defined and if you need to provide a name for it, or if the function in question needs to be a function expression, an [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
, or if the function code is placed correctly in this context at all.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#examples)

-------------------------------------------------------------------------------------------------------------------------

### [Statements vs. expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#statements_vs._expressions)

A _[function statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
_ (or _function declaration_) requires a name. This won't work:

You can use a [function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
 (assignment) instead:

If your function is intended to be an [IIFE](https://en.wikipedia.org/wiki/Immediately-invoked_function_expression "External link (opens in new tab)")
 (Immediately Invoked Function Expression, which is a function that runs as soon as it is defined) you will need to add a few more braces:

### [Labeled functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#labeled_functions)

[Labels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
 are an entirely different feature from function names. You can't use a label as a function name.

In addition, labeled function declarations themselves are a deprecated feature. Use regular function declarations instead.

### [Object methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#object_methods)

If you intended to create a method of an object, you will need to create an object. The following syntax without a name after the `function` keyword is valid then.

You can also use the [method syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
.

### [Callback syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#callback_syntax)

Also, check your syntax when using callbacks. Braces and commas can quickly get confusing.

Correct would be:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    
*   [`function` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
    
*   [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
    
*   [Labeled statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unnamed_function_statement/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/unnamed_function_statement/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/unnamed_function_statement (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUnnamed_function_statement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Funnamed_function_statement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUnnamed_function_statement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Funnamed_function_statement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")