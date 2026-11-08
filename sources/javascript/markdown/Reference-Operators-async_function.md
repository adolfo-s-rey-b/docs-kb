*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#mdn-search)
    

async function expression
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`async function`** keywords can be used to define an async function inside an expression.

You can also define async functions using the [`async function` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
 or the [arrow syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#syntax)

------------------------------------------------------------------------------------------------------------

**Note:** An [expression statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
 cannot begin with the keywords `async function` to avoid ambiguity with an [`async function` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
. The `async function` keywords only begin an expression when they appear in a context that cannot accept statements.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#parameters)

[`name` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#name)

The function name. Can be omitted, in which case the function is _anonymous_. The name is only local to the function body.

[`paramN` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#paramn)

The name of a formal parameter for the function. For the parameters' syntax, see the [Functions reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_parameters)
.

[`statements` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#statements)

The statements which comprise the body of the function.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#description)

----------------------------------------------------------------------------------------------------------------------

An `async function` expression is very similar to, and has almost the same syntax as, an [`async function` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
. The main difference between an `async function` expression and an `async function` declaration is the _function name_, which can be omitted in `async function` expressions to create _anonymous_ functions. An `async function` expression can be used as an [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 (Immediately Invoked Function Expression) which runs as soon as it is defined, allowing you to mimic [top-level await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#top-level_await)
. See also the chapter about [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
 for more information.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#examples)

----------------------------------------------------------------------------------------------------------------

### [Using async function expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#using_async_function_expression)

### [Async IIFE](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#async_iife)

An `async` [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 allows you to use [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 and [`for...await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
 in contexts where [top-level await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#top-level_await)
 is not available. Here we use an [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 to define the IIFE, but `async function` expressions can also be used.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-async-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-async-function-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
    
*   [`AsyncFunction`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncFunction)
    
*   [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/async_function/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/async_function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fasync_function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fasync_function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fasync_function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fasync_function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")