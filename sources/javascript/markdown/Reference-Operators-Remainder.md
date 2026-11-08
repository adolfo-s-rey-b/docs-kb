*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#mdn-search)
    

Remainder (%)
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **remainder (`%`)** operator returns the remainder left over when one operand is divided by a second operand. It always takes the sign of the dividend.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#syntax)

-------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#description)

-----------------------------------------------------------------------------------------------------------------

The `%` operator is overloaded for two types of operands: number and [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
. It first [coerces both operands to numeric values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#numeric_coercion)
 and tests the types of them. It performs BigInt remainder if both operands become BigInts; otherwise, it performs number remainder. A [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 is thrown if one operand becomes a BigInt but the other becomes a number.

For the operation `n % d`, `n` is called the dividend and `d` is called the divisor. The operation returns `NaN` if one of the operands is `NaN`, `n` is ±Infinity, or if `d` is ±0. Otherwise, if `d` is ±Infinity or if `n` is ±0, the dividend `n` is returned.

When both operands are non-zero and finite, the remainder `r` is calculated as `r := n - d * q` where `q` is the integer such that `r` has the same sign as the dividend `n` while being as close to 0 as possible.

Note that while in most languages, '%' is a remainder operator, in some (e.g., [Python, Perl](https://en.wikipedia.org/wiki/Modulo_operation#In_programming_languages "External link (opens in new tab)")
) it is a modulo operator. Modulo is defined as `k := n - d * q` where `q` is the integer such that `k` has the same sign as the divisor `d` while being as close to 0 as possible. For two values of the same sign, the two are equivalent, but when the operands are of different signs, the modulo result always has the same sign as the _divisor_, while the remainder has the same sign as the _dividend_, which can make them differ by one unit of `d`. To obtain a modulo in JavaScript, in place of `n % d`, use `((n % d) + d) % d`. In JavaScript, the modulo operation (which doesn't have a dedicated operator) is used to normalize the second operand of bitwise shift operators ([`<<`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift)
, [`>>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift)
, etc.), making the offset always a positive value.

For BigInt division, a [`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
 is thrown if the divisor `y` is `0n`. This is because number remainder by zero returns `NaN`, but BigInt has no concept of `NaN`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#examples)

-----------------------------------------------------------------------------------------------------------

### [Remainder with positive dividend](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#remainder_with_positive_dividend)

### [Remainder with negative dividend](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#remainder_with_negative_dividend)

### [Remainder with NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#remainder_with_nan)

### [Remainder with Infinity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#remainder_with_infinity)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-multiplicative-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-multiplicative-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Addition (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
    
*   [Subtraction (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction)
    
*   [Division (`/`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division)
    
*   [Multiplication (`*`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)
    
*   [Exponentiation (`**`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
    
*   [Increment (`++`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
    
*   [Decrement (`--`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)
    
*   [Unary negation (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)
    
*   [Unary plus (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
    
*   [Remainder operator vs. modulo operator](https://2ality.com/2019/08/remainder-vs-modulo.html "External link (opens in new tab)")
     by Dr. Axel Rauschmayer (2019)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/remainder/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/remainder (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FRemainder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fremainder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FRemainder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fremainder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")