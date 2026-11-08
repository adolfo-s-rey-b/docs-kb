*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#mdn-search)
    

Unsigned right shift (>>>)
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **unsigned right shift (`>>>`)** operator returns a number whose binary representation is the first operand shifted by the specified number of bits to the right. Excess bits shifted off to the right are discarded, and zero bits are shifted in from the left. This operation is also called "zero-filling right shift", because the sign bit becomes `0`, so the resulting number is always positive. Unsigned right shift does not accept [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 values.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#try_it)

------------------------------------------------------------------------------------------------------------------

    const a = 5; //  00000000000000000000000000000101
    const b = 2; //  00000000000000000000000000000010
    const c = -5; //  11111111111111111111111111111011
    
    console.log(a >>> b); //  00000000000000000000000000000001
    // Expected output: 1
    
    console.log(c >>> b); //  00111111111111111111111111111110
    // Expected output: 1073741822
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#syntax)

------------------------------------------------------------------------------------------------------------------

js

    x >>> y
    

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#description)

----------------------------------------------------------------------------------------------------------------------------

Unlike other arithmetic and bitwise operators, the unsigned right shift operator does not accept [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 values. This is because it fills the leftmost bits with zeroes, but conceptually, BigInts have an infinite number of leading sign bits, so there's no "leftmost bit" to fill with zeroes.

The operator operates on the left operand's bit representation in [two's complement](https://en.wikipedia.org/wiki/Two's_complement "External link (opens in new tab)")
. Consider the 32-bit binary representations of the decimal (base 10) numbers `9` and `-9`:

     9 (base 10): 00000000000000000000000000001001 (base 2)
    -9 (base 10): 11111111111111111111111111110111 (base 2)

The binary representation under two's complement of the negative decimal (base 10) number `-9` is formed by inverting all the bits of its opposite number, which is `9` and `00000000000000000000000000001001` in binary, and adding `1`.

In both cases, the sign of the binary number is given by its leftmost bit: for the positive decimal number `9`, the leftmost bit of the binary representation is `0`, and for the negative decimal number `-9`, the leftmost bit of the binary representation is `1`.

Given those binary representations of the decimal (base 10) numbers `9`, and `-9`:

For the positive number `9`, zero-fill right shift and [sign-propagating right shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift)
 yield the same result: `9 >>> 2` yields `2`, the same as `9 >> 2`:

      9 (base 10): 00000000000000000000000000001001 (base 2)
                   --------------------------------
9 >>  2 (base 10): 00000000000000000000000000000010 (base 2) = 2 (base 10)
9 >>> 2 (base 10): 00000000000000000000000000000010 (base 2) = 2 (base 10)

Notice how two rightmost bits, `01`, have been shifted off, and two zeroes have been shifted in from the left.

However, notice what happens for `-9`: `-9 >> 2` ([sign-propagating right shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift)
) yields `-3`, but `-9 >>> 2` (zero-fill right shift) yields 1073741821:

      -9 (base 10): 11111111111111111111111111110111 (base 2)
                    --------------------------------
-9 >>  2 (base 10): 11111111111111111111111111111101 (base 2) = -3 (base 10)
-9 >>> 2 (base 10): 00111111111111111111111111111101 (base 2) = 1073741821 (base 10)

Notice how two rightmost bits, `11`, have been shifted off. For `-9 >> 2` ([sign-propagating right shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift)
), two copies of the leftmost `1` bit have been shifted in from the left, which preserves the negative sign. On the other hand, for `-9 >>> 2` (zero-fill right shift), zeroes have instead been shifted in from the left, so the negative sign of the number is not preserved, and the result is instead a (large) positive number.

If the left operand is a number with more than 32 bits, it will get the most significant bits discarded. For example, the following integer with more than 32 bits will be converted to a 32-bit integer:

Before: 11100110111110100000000000000110000000000001
After:              10100000000000000110000000000001

The right operand will be converted to an unsigned 32-bit integer and then taken modulo 32, so the actual shift offset will always be a positive integer between 0 and 31, inclusive. For example, `100 >>> 32` is the same as `100 >>> 0` (and produces `100`) because 32 modulo 32 is 0.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#examples)

----------------------------------------------------------------------------------------------------------------------

### [Using unsigned right shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#using_unsigned_right_shift)

js

    9 >>> 2; // 2
    -9 >>> 2; // 1073741821
    

Unsigned right shift doesn't work with BigInts.

js

    9n >>> 2n; // TypeError: BigInts have no unsigned right shift, use >> instead
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-unsigned-right-shift-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-unsigned-right-shift-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Bitwise operators in the JS guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#bitwise_operators)
    
*   [Unsigned right shift assignment (`>>>=`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift_assignment)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/unsigned_right_shift/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/unsigned_right_shift (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FUnsigned_right_shift&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Funsigned_right_shift%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FUnsigned_right_shift%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Funsigned_right_shift%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")