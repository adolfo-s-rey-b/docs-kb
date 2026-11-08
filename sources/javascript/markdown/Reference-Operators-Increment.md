*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#mdn-search)
    

Increment (++)
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **increment (`++`)** operator increments (adds one to) its operand and returns the value before or after the increment, depending on where the operator is placed.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#syntax)

-------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#description)

-----------------------------------------------------------------------------------------------------------------

The `++` operator is overloaded for two types of operands: number and [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
. It first [coerces the operand to a numeric value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#numeric_coercion)
 and tests the type of it. It performs BigInt increment if the operand becomes a BigInt; otherwise, it performs number increment.

If used postfix, with operator after operand (for example, `x++`), the increment operator increments and returns the value before incrementing.

If used prefix, with operator before operand (for example, `++x`), the increment operator increments and returns the value after incrementing.

The increment operator can only be applied on operands that are references (variables and object properties; i.e., valid [assignment targets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
). `++x` itself evaluates to a value, not a reference, so you cannot chain multiple increment operators together.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#examples)

-----------------------------------------------------------------------------------------------------------

### [Postfix increment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#postfix_increment)

### [Prefix increment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#prefix_increment)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-postfix-increment-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-postfix-increment-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Addition (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
    
*   [Subtraction (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction)
    
*   [Division (`/`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division)
    
*   [Multiplication (`*`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)
    
*   [Remainder (`%`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)
    
*   [Exponentiation (`**`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
    
*   [Decrement (`--`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)
    
*   [Unary negation (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)
    
*   [Unary plus (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/increment/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/increment (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FIncrement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fincrement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FIncrement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fincrement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")