*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#mdn-search)
    

Unary negation (-)
==================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **unary negation (`-`)** operator precedes its operand and negates it.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#try_it)

------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#syntax)

------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#description)

----------------------------------------------------------------------------------------------------------------------

The `-` operator is overloaded for two types of operands: number and [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
. It first [coerces the operand to a numeric value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#numeric_coercion)
 and tests the type of it. It performs BigInt negation if the operand becomes a BigInt; otherwise, it performs number negation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#examples)

----------------------------------------------------------------------------------------------------------------

### [Negating numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#negating_numbers)

### [Negating non-numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#negating_non-numbers)

The unary negation operator can convert a non-number into a number.

BigInts can be negated using the unary negation operator.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-unary-minus-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-unary-minus-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Addition (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
    
*   [Subtraction (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction)
    
*   [Division (`/`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division)
    
*   [Multiplication (`*`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)
    
*   [Remainder (`%`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)
    
*   [Exponentiation (`**`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
    
*   [Increment (`++`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
    
*   [Decrement (`--`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)
    
*   [Unary plus (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/unary_negation/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/unary_negation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FUnary_negation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Funary_negation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FUnary_negation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Funary_negation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")