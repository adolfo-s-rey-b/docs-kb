*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#mdn-search)
    

Math.atan()
===========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Math.atan()`** static method returns the inverse tangent (in radians) of a number, that is

𝙼𝚊𝚝𝚑.𝚊𝚝𝚊𝚗(𝚡)\=arctan(x)\=the unique y∊\[−π2,π2\] such that tan(y)\=x\\mathtt{\\operatorname{Math.atan}(x)} = \\arctan(x) = \\text{the unique } y \\in \\left\[-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right\] \\text{ such that } \\tan(y) = x

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#try_it)

------------------------------------------------------------------------------------------------------------

    // Calculates angle of a right-angle triangle in radians
    function calcAngle(opposite, adjacent) {
      return Math.atan(opposite / adjacent);
    }
    
    console.log(calcAngle(8, 10));
    // Expected output: 0.6747409422235527
    
    console.log(calcAngle(5, 3));
    // Expected output: 1.0303768265243125
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#syntax)

------------------------------------------------------------------------------------------------------------

js

    Math.atan(x)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#parameters)

[`x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#x)

A number.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#return_value)

The inverse tangent (angle in radians between \-π2\-\\frac{\\pi}{2} and π2\\frac{\\pi}{2}, inclusive) of `x`. If `x` is [`Infinity`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity)
, it returns π2\\frac{\\pi}{2}. If `x` is `-Infinity`, it returns \-π2\-\\frac{\\pi}{2}.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#description)

----------------------------------------------------------------------------------------------------------------------

Because `atan()` is a static method of `Math`, you always use it as `Math.atan()`, rather than as a method of a `Math` object you created (`Math` is not a constructor).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#examples)

----------------------------------------------------------------------------------------------------------------

### [Using Math.atan()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#using_math.atan)

js

    Math.atan(-Infinity); // -1.5707963267948966 (-π/2)
    Math.atan(-0); // -0
    Math.atan(0); // 0
    Math.atan(1); // 0.7853981633974483  (π/4)
    Math.atan(Infinity); // 1.5707963267948966  (π/2)
    
    // The angle that the line (0,0) -- (x,y) forms with the x-axis in a Cartesian coordinate system
    const theta = (x, y) => Math.atan(y / x);
    

Note that you may want to avoid the `theta` function and use [`Math.atan2()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2)
 instead, which has a wider range (between -π and π) and avoids outputting `NaN` for cases such as when `x` is `0`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-math.atan](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-math.atan) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`Math.acos()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/acos)
    
*   [`Math.asin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/asin)
    
*   [`Math.atan2()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2)
    
*   [`Math.cos()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cos)
    
*   [`Math.sin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sin)
    
*   [`Math.tan()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/tan)
    
*   CSS [`atan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan)
     function

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 29, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/math/atan/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/math/atan (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMath%2Fatan&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmath%2Fatan%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMath%2Fatan%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmath%2Fatan%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0fb5a7e4cc045ba0b1dc453624f196309d9bea10%0A*+Document+last+modified%3A+2025-12-29T17%3A25%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")