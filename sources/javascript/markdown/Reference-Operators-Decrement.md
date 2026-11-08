*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#mdn-search)
    

Decrement (--)
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **decrement (`--`)** operator decrements (subtracts one from) its operand and returns the value before or after the decrement, depending on where the operator is placed.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#syntax)

-------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#description)

-----------------------------------------------------------------------------------------------------------------

The `--` operator is overloaded for two types of operands: number and [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
. It first [coerces the operand to a numeric value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#numeric_coercion)
 and tests the type of it. It performs BigInt decrement if the operand becomes a BigInt; otherwise, it performs number decrement.

If used postfix, with operator after operand (for example, `x--`), the decrement operator decrements and returns the value before decrementing.

If used prefix, with operator before operand (for example, `--x`), the decrement operator decrements and returns the value after decrementing.

The decrement operator can only be applied on operands that are references (variables and object properties; i.e., valid [assignment targets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
). `--x` itself evaluates to a value, not a reference, so you cannot chain multiple decrement operators together.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#examples)

-----------------------------------------------------------------------------------------------------------

### [Postfix decrement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#postfix_decrement)

### [Prefix decrement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#prefix_decrement)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-postfix-decrement-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-postfix-decrement-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Addition (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
    
*   [Subtraction (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction)
    
*   [Division (`/`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division)
    
*   [Multiplication (`*`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)
    
*   [Remainder (`%`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)
    
*   [Exponentiation (`**`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
    
*   [Increment (`++`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
    
*   [Unary negation (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)
    
*   [Unary plus (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/decrement/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/decrement (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FDecrement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fdecrement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FDecrement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fdecrement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")