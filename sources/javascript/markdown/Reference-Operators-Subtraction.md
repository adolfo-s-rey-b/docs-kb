*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#mdn-search)
    

Subtraction (-)
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **subtraction (`-`)** operator subtracts the two operands, producing their difference.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#try_it)

---------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#syntax)

---------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#description)

-------------------------------------------------------------------------------------------------------------------

The `-` operator is overloaded for two types of operands: number and [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
. It first [coerces both operands to numeric values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#numeric_coercion)
 and tests the types of them. It performs BigInt subtraction if both operands become BigInts; otherwise, it performs number subtraction. A [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 is thrown if one operand becomes a BigInt but the other becomes a number.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#examples)

-------------------------------------------------------------------------------------------------------------

### [Subtraction using numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#subtraction_using_numbers)

Other non-BigInt values are coerced to numbers:

### [Subtraction using BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#subtraction_using_bigints)

You cannot mix BigInt and number operands in subtraction.

To do subtraction with a BigInt and a non-BigInt, convert either operand:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-subtraction-operator-minus](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-subtraction-operator-minus) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Addition (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
    
*   [Division (`/`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division)
    
*   [Multiplication (`*`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)
    
*   [Remainder (`%`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)
    
*   [Exponentiation (`**`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
    
*   [Increment (`++`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
    
*   [Decrement (`--`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)
    
*   [Unary negation (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)
    
*   [Unary plus (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/subtraction/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/subtraction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FSubtraction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fsubtraction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FSubtraction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fsubtraction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")