*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#mdn-search)
    

Math.clz32()
============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Math.clz32()`** static method returns the number of leading zero bits in the 32-bit binary representation of a number.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#try_it)

-------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#syntax)

-------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#parameters)

[`x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#x)

A number.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#return_value)

The number of leading zero bits in the 32-bit binary representation of `x`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#description)

-----------------------------------------------------------------------------------------------------------------------

`clz32` is short for **C**ount**L**eading**Z**eros**32**.

If `x` is not a number, it will be converted to a number first, then converted to a 32-bit unsigned integer.

If the converted 32-bit unsigned integer is `0`, `32` is returned, because all bits are `0`. If the most significant bit is `1` (i.e., the number is greater than or equal to 231), `0` is returned.

This function is particularly useful for systems that compile to JS, like [Emscripten](https://emscripten.org/ "External link (opens in new tab)")
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using Math.clz32()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#using_math.clz32)

### [Implementing Count Leading Ones and beyond](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#implementing_count_leading_ones_and_beyond)

At present, there is no `Math.clon` for "Count Leading Ones" (named "clon", not "clo", because "clo" and "clz" are too similar especially for non-English-speaking people). However, a `clon` function can easily be created by inverting the bits of a number and passing the result to `Math.clz32`. Doing this will work because the inverse of 1 is 0 and vice versa. Thus, inverting the bits will inverse the measured quantity of 0's (from `Math.clz32`), thereby making `Math.clz32` count the number of ones instead of counting the number of zeros.

Consider the following 32-bit word:

Using this logic, a `clon` function can be created as follows:

Further, this technique could be extended to create a jumpless "Count Trailing Zeros" function, as seen below. The `ctrz` function takes a bitwise AND of the integer with its two's complement. By how two's complement works, all trailing zeros will be converted to ones, and then when adding 1, it would be carried over until the first `0` (which was originally a `1`) is reached. All bits higher than this one stay the same and are inverses of the original integer's bits. Therefore, when doing bitwise AND with the original integer, all higher bits become `0`, which can be counted with `clz`. The number of trailing zeros, plus the first `1` bit, plus the leading bits that were counted by `clz`, total to 32.

Then we can define a "Count Trailing Ones" function like so:

These helper functions can be made into an [asm.js](https://developer.mozilla.org/en-US/docs/Games/Tools/asm.js)
 module for a potential performance improvement.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-math.clz32](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-math.clz32) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Math.clz32` in `core-js`](https://core-js.io/docs/features/ecmascript/math "External link (opens in new tab)")
    
*   [es-shims polyfill of `Math.clz32`](https://www.npmjs.com/package/math.clz32 "External link (opens in new tab)")
    
*   [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
    
*   [`Math.imul`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/imul)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/math/clz32/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/math/clz32 (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMath%2Fclz32&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmath%2Fclz32%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMath%2Fclz32%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmath%2Fclz32%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")