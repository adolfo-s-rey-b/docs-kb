*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#mdn-search)
    

Conditional (ternary) operator
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **conditional (ternary) operator** is the only JavaScript operator that takes three operands: a condition followed by a question mark (`?`), then an expression to execute if the condition is [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 followed by a colon (`:`), and finally the expression to execute if the condition is [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
. This operator is frequently used as an alternative to an [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
 statement.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#try_it)

------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#syntax)

------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#parameters)

[`condition`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#condition)

An expression whose value is used as a condition.

[`exprIfTrue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#expriftrue)

An expression which is executed if the `condition` evaluates to a [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 value (one which equals or can be converted to `true`).

[`exprIfFalse`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#expriffalse)

An expression which is executed if the `condition` is [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 (that is, has a value which can be converted to `false`).

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#description)

----------------------------------------------------------------------------------------------------------------------------

Besides `false`, possible falsy expressions are: `null`, `NaN`, `0`, the empty string (`""`), and `undefined`. If `condition` is any of these, the result of the conditional expression will be the result of executing the expression `exprIfFalse`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#examples)

----------------------------------------------------------------------------------------------------------------------

### [A basic example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#a_basic_example)

### [Handling null values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#handling_null_values)

One common usage is to handle a value that may be `null`:

### [Conditional chains](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#conditional_chains)

The ternary operator is right-associative, which means it can be "chained" in the following way, similar to an `if … else if … else if … else` chain:

This is equivalent to the following [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
 chain.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-conditional-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-conditional-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
    
*   [Nullish coalescing operator (`??`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
    
*   [Optional chaining (`?.`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
    
*   [Learn: Making decisions in your code — conditionals](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Conditionals)
    
*   [Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
     guide

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/conditional_operator/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/conditional_operator (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FConditional_operator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fconditional_operator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FConditional_operator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fconditional_operator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")