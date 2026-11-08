*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#mdn-search)
    

Strict equality (===)
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **strict equality (`===`)** operator checks whether its two operands are equal, returning a Boolean result. Unlike the [equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
 operator, the strict equality operator always considers operands of different types to be different.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#try_it)

-------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#syntax)

-------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#description)

-----------------------------------------------------------------------------------------------------------------------

The strict equality operators (`===` and `!==`) provide the [IsStrictlyEqual](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness#strict_equality_using)
 semantic.

*   If the operands are of different types, return `false`.
*   If both operands are objects, return `true` only if they refer to the same object.
*   If both operands are `null` or both operands are `undefined`, return `true`.
*   If either operand is `NaN`, return `false`.
*   Otherwise, compare the two operand's values:
    *   Numbers must have the same numeric values. `+0` and `-0` are considered to be the same value.
    *   Strings must have the same characters in the same order.
    *   Booleans must be both `true` or both `false`.

The most notable difference between this operator and the [equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
 (`==`) operator is that if the operands are of different types, the `==` operator attempts to convert them to the same type before comparing.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#examples)

-----------------------------------------------------------------------------------------------------------------

### [Comparing operands of the same type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#comparing_operands_of_the_same_type)

### [Comparing operands of different types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#comparing_operands_of_different_types)

### [Comparing objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#comparing_objects)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-equality-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-equality-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Equality (`==`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
    
*   [Inequality (`!=`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality)
    
*   [Strict inequality (`!==`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/strict_equality/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/strict_equality (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FStrict_equality&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fstrict_equality%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FStrict_equality%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fstrict_equality%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")