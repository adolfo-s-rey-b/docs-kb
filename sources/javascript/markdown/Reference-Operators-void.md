*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#mdn-search)
    

void operator
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`void`** operator evaluates the given `expression` and then returns [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#syntax)

--------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#description)

------------------------------------------------------------------------------------------------------------

This operator allows evaluating expressions that produce a value into places where an expression that evaluates to [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 is desired.

The `void` operator is often used merely to obtain the `undefined` primitive value, usually using `void(0)` (which is equivalent to `void 0`). In these cases, the global variable [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 can be used.

It should be noted that [the precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
 of the `void` operator should be taken into account and that parentheses can help clarify the resolution of the expression following the `void` operator:

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#examples)

------------------------------------------------------------------------------------------------------

### [Immediately Invoked Function Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#immediately_invoked_function_expressions)

When using an [immediately-invoked function expression](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
, the `function` keyword cannot be at the immediate start of the [statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
, because that would be parsed as a [function declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
, and would generate a syntax error when the parentheses representing invocation is reached — if the function is unnamed, it would immediately be a syntax error if the function is parsed as a declaration.

In order for the function to be parsed as an [expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
, the `function` keyword has to appear at a position that only accepts expressions, not statements. This can be achieved by prefixing the keyword with a [unary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#unary_operators)
, which only accepts expressions as operands. Function invocation has higher [precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
 than unary operators, so it will be executed first. Its return value (which is almost always `undefined`) will be passed to the unary operator and then immediately discarded.

Of all the unary operators, `void` offers the best semantic, because it clearly signals that the return value of the function invocation should be discarded.

This is a bit longer than wrapping the function expression in parentheses, which has the same effect of forcing the `function` keyword to be parsed as the start of an expression instead of a statement.

Note that this trick only applies to IIFEs defined with the `function` keyword. Attempting to use the `void` operator to avoid parentheses for an arrow function results in a syntax error. Arrow function expressions always require parentheses around them when being called.

### [JavaScript URIs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#javascript_uris)

When a browser follows a [`javascript:` URI](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/javascript)
, it evaluates the code in the URI and then replaces the contents of the page with the returned value, unless the returned value is [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
. The `void` operator can be used to return `undefined`. For example:

**Note:** `javascript:` pseudo protocol is discouraged over other alternatives, such as unobtrusive event handlers.

### [Non-leaking Arrow Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#non-leaking_arrow_functions)

Arrow functions introduce a short-hand braceless syntax that returns an expression. This can cause unintended side effects if the expression is a function call where the returned value changes from `undefined` to some other value.

For example, if `doSomething()` returns `false` in the code below, the checkbox will no longer be marked as checked or unchecked when the checkbox is clicked (returning `false` from the handler disables the default action).

This is unlikely to be desired behavior! To be safe, when the return value of a function is not intended to be used, it can be passed to the `void` operator to ensure that (for example) changing APIs do not cause arrow functions' behaviors to change.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-void-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-void-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void#see_also)

------------------------------------------------------------------------------------------------------

*   [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/void/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/void (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fvoid&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fvoid%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fvoid%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fvoid%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")