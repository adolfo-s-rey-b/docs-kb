*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#mdn-search)
    

Math.log1p()
============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Math.log1p()`** static method returns the natural logarithm (base [e](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/E)
) of `1 + x`, where `x` is the argument. That is:

∀x\>−1,𝙼𝚊𝚝𝚑.𝚕𝚘𝚐𝟷𝚙(𝚡)\=ln(1+x)\\forall x > -1,\\;\\mathtt{\\operatorname{Math.log1p}(x)} = \\ln(1 + x)

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#try_it)

-------------------------------------------------------------------------------------------------------------

    console.log(Math.log1p(1));
    // Expected output: 0.6931471805599453
    
    console.log(Math.log1p(0));
    // Expected output: 0
    
    console.log(Math.log1p(-1));
    // Expected output: -Infinity
    
    console.log(Math.log1p(-2));
    // Expected output: NaN
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#syntax)

-------------------------------------------------------------------------------------------------------------

js

    Math.log1p(x)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#parameters)

[`x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#x)

A number greater than or equal to -1.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#return_value)

The natural logarithm (base [e](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/E)
) of `x + 1`. If `x` is -1, returns [`-Infinity`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/NEGATIVE_INFINITY)
. If `x < -1`, returns [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#description)

-----------------------------------------------------------------------------------------------------------------------

For very small values of _x_, adding 1 can reduce or eliminate precision. The double floats used in JS give you about 15 digits of precision. 1 + 1e-15 = 1.000000000000001, but 1 + 1e-16 = 1.000000000000000 and therefore exactly 1.0 in that arithmetic, because digits past 15 are rounded off.

When you calculate log(1 + _x_), where _x_ is a small positive number, you should get an answer very close to _x_ because: limx→0log⁡(1+x)x\=1\\lim\_{x \\to 0} \\frac{\\log(1+x)}{x} = 1. If you calculate `Math.log(1 + 1.1111111111e-15)`, you should get an answer close to `1.1111111111e-15`. Instead, you will end up taking the logarithm of `1.00000000000000111022` (the roundoff is in binary, so sometimes it gets ugly), and get the answer 1.11022…e-15, with only 3 correct digits. If you calculate `Math.log1p(1.1111111111e-15)` instead, you will get a much more accurate answer, `1.1111111110999995e-15`, with 15 correct digits of precision (actually 16 in this case).

If the value of `x` is less than -1, the return value is always [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
.

Because `log1p()` is a static method of `Math`, you always use it as `Math.log1p()`, rather than as a method of a `Math` object you created (`Math` is not a constructor).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using Math.log1p()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#using_math.log1p)

js

    Math.log1p(-2); // NaN
    Math.log1p(-1); // -Infinity
    Math.log1p(-0); // -0
    Math.log1p(0); // 0
    Math.log1p(1); // 0.6931471805599453
    Math.log1p(Infinity); // Infinity
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-math.log1p](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-math.log1p) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Math.log1p` in `core-js`](https://core-js.io/docs/features/ecmascript/math "External link (opens in new tab)")
    
*   [es-shims polyfill of `Math.log1p`](https://www.npmjs.com/package/math.log1p "External link (opens in new tab)")
    
*   [`Math.exp()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/exp)
    
*   [`Math.log()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log)
    
*   [`Math.expm1()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/expm1)
    
*   [`Math.log10()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log10)
    
*   [`Math.log2()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log2)
    
*   [`Math.pow()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/pow)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/math/log1p/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/math/log1p (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMath%2Flog1p&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmath%2Flog1p%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMath%2Flog1p%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmath%2Flog1p%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")