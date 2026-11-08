*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#mdn-search)
    

Left shift (<<)
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **left shift (`<<`)** operator returns a number or BigInt whose binary representation is the first operand shifted by the specified number of bits to the left. Excess bits shifted off to the left are discarded, and zero bits are shifted in from the right.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#try_it)

--------------------------------------------------------------------------------------------------------

    const a = 5; // 00000000000000000000000000000101
    const b = 2; // 00000000000000000000000000000010
    
    console.log(a << b); // 00000000000000000000000000010100
    // Expected output: 20
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#syntax)

--------------------------------------------------------------------------------------------------------

js

    x << y
    

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#description)

------------------------------------------------------------------------------------------------------------------

The `<<` operator is overloaded for two types of operands: number and [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
. For numbers, the operator returns a 32-bit integer. For BigInts, the operator returns a BigInt. It first [coerces both operands to numeric values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#numeric_coercion)
 and tests the types of them. It performs BigInt left shift if both operands become BigInts; otherwise, it converts both operands to [32-bit integers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#fixed-width_number_conversion)
 and performs number left shift. A [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 is thrown if one operand becomes a BigInt but the other becomes a number.

The operator operates on the left operand's bit representation in [two's complement](https://en.wikipedia.org/wiki/Two's_complement "External link (opens in new tab)")
. For example, `9 << 2` yields 36:

     9 (base 10): 00000000000000000000000000001001 (base 2)
                  --------------------------------
9 << 2 (base 10): 00000000000000000000000000100100 (base 2) = 36 (base 10)

Bitwise a 32-bit integer `x` to the left by `y` bits yields `x * 2 ** y`. So for example, `9 << 3` is equivalent to `9 * (2 ** 3) = 9 * (8) = 72`.

If the left operand is a number with more than 32 bits, it will get the most significant bits discarded. For example, the following integer with more than 32 bits will be converted to a 32-bit integer:

Before: 11100110111110100000000000000110000000000001
After:              10100000000000000110000000000001

The right operand will be converted to an unsigned 32-bit integer and then taken modulo 32, so the actual shift offset will always be a positive integer between 0 and 31, inclusive. For example, `100 << 32` is the same as `100 << 0` (and produces `100`) because 32 modulo 32 is 0.

**Warning:** You may see people using `<< 0` to truncate numbers to integers. Left shifting any number `x` by `0` returns `x` converted to a 32-bit integer, which additionally removes leading bits for numbers outside the range -2147483648 to 2147483647. Use [`Math.trunc()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/trunc#using_bitwise_no-ops_to_truncate_numbers)
 instead.

For BigInts, there's no truncation. Conceptually, understand positive BigInts as having an infinite number of leading `0` bits, and negative BigInts having an infinite number of leading `1` bits.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#examples)

------------------------------------------------------------------------------------------------------------

### [Using left shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#using_left_shift)

js

    9 << 3; // 72
    
    // 9 * (2 ** 3) = 9 * (8) = 72
    
    9n << 3n; // 72n
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-left-shift-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-left-shift-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift#see_also)

------------------------------------------------------------------------------------------------------------

*   [Bitwise operators in the JS guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#bitwise_operators)
    
*   [Left shift assignment (`<<=`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift_assignment)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/left_shift/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/left_shift (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLeft_shift&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fleft_shift%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLeft_shift%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fleft_shift%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")