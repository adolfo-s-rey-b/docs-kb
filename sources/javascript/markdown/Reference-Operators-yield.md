*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#mdn-search)
    

yield
=====

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`yield`** operator is used to pause and resume a [generator function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#try_it)

---------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#syntax)

---------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#parameters)

[`expression` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#expression)

The value to yield from the generator function via [the iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
. If omitted, `undefined` is yielded.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#return_value)

Returns the optional value passed to the generator's `next()` method to resume its execution.

**Note:** This means `next()` is asymmetric: it always sends a value to the currently suspended `yield`, but returns the operand of the next `yield`. The argument passed to the first `next()` call cannot be retrieved because there's no currently suspended `yield`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#description)

-------------------------------------------------------------------------------------------------------------

The `yield` keyword pauses generator function execution and the value of the expression following the `yield` keyword is returned to the generator's caller. It can be thought of as a generator-based version of the `return` keyword.

`yield` can only be used directly within the generator function that contains it. It cannot be used within nested functions.

Calling a generator function constructs a [`Generator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
 object. Each time the generator's [`next()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator/next)
 method is called, the generator resumes execution, and runs until it reaches one of the following:

*   A `yield` expression. In this case, the generator pauses, and the `next()` method return an [iterator result](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
     object with two properties: `value` and `done`. The `value` property is the value of the expression after the `yield` operator, and `done` is `false`, indicating that the generator function has not fully completed.
*   The end of the generator function. In this case, execution of the generator ends, and the `next()` method returns an iterator result object where the `value` is [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
     and `done` is `true`.
*   A [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
     statement. In this case, execution of the generator ends, and the `next()` method returns an iterator result object where the `value` is the specified return value and `done` is `true`.
*   A [`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
     statement. In this case, execution of the generator halts entirely, and the `next()` method throws the specified exception.

Once paused on a `yield` expression, the generator's code execution remains paused until the generator's `next()` method is called again. If an optional value is passed to the generator's `next()` method, that value becomes the value returned by the generator's current `yield` operation. The first `next()` call does not have a corresponding suspended `yield` operation, so there's no way to get the argument passed to the first `next()` call.

If the generator's [`return()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator/return)
 or [`throw()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator/throw)
 method is called, it acts as if a [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
 or [`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
 statement was executed at the paused `yield` expression. You can use [`try...catch...finally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
 within the generator function body to handle these early completions. If the `return()` or `throw()` method is called but there's no suspended `yield` expression (because `next()` has not been called yet, or because the generator has already completed), then the early completions cannot be handled and always terminate the generator.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#examples)

-------------------------------------------------------------------------------------------------------

### [Using yield](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#using_yield)

The following code is the declaration of an example generator function.

Once a generator function is defined, it can be used by constructing an iterator as shown.

You can also send a value with `next(value)` into the generator. `step` evaluates as a return value of the `yield` expression — although the value passed to the generator's `next()` method the first time `next()` is called is ignored.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-YieldExpression](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#prod-YieldExpression) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield#see_also)

-------------------------------------------------------------------------------------------------------

*   [Iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
    
*   [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    
*   [`function*` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function*)
    
*   [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/yield/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/yield (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fyield&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fyield%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fyield%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fyield%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")