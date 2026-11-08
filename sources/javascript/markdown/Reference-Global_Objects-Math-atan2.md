*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#mdn-search)
    

Math.atan2()
============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Math.atan2()`** static method returns the angle in the plane (in radians) between the positive x-axis and the ray from (0, 0) to the point (x, y), for `Math.atan2(y, x)`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#try_it)

-------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#syntax)

-------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#parameters)

[`y`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#y)

The y coordinate of the point.

[`x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#x)

The x coordinate of the point.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#return_value)

The angle in radians (between -π and π, inclusive) between the positive x-axis and the ray from (0, 0) to the point (x, y).

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#description)

-----------------------------------------------------------------------------------------------------------------------

The `Math.atan2()` method measures the counterclockwise angle θ, in radians, between the positive x-axis and the point `(x, y)`. Note that the arguments to this function pass the y-coordinate first and the x-coordinate second.

![A diagram showing the angle returned by atan2(y, x)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2/atan2.png)

`Math.atan2()` is passed separate `x` and `y` arguments, while [`Math.atan()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan)
 is passed the ratio of those two arguments. `Math.atan2(y, x)` differs from `Math.atan(y / x)` in the following cases:

| `x` | `y` | `Math.atan2(y, x)` | `Math.atan(y / x)` |
| --- | --- | --- | --- |
| `Infinity` | `Infinity` | π / 4 | `NaN` |
| `Infinity` | `-Infinity` | \-π / 4 | `NaN` |
| `-Infinity` | `Infinity` | 3π / 4 | `NaN` |
| `-Infinity` | `-Infinity` | \-3π / 4 | `NaN` |
| 0   | 0   | 0   | `NaN` |
| 0   | \-0 | \-0 | `NaN` |
| < 0 (including `-0`) | 0   | π   | 0   |
| < 0 (including `-0`) | \-0 | \-π | 0   |
| `-Infinity` | \> 0 | π   | \-0 |
| \-0 | \> 0 | π / 2 | \-π / 2 |
| `-Infinity` | < 0 | \-π | 0   |
| \-0 | < 0 | \-π / 2 | π / 2 |

In addition, for points in the second and third quadrants (`x < 0`), `Math.atan2()` would output an angle less than \-π2\-\\frac{\\pi}{2} or greater than π2\\frac{\\pi}{2}.

Because `atan2()` is a static method of `Math`, you always use it as `Math.atan2()`, rather than as a method of a `Math` object you created (`Math` is not a constructor).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using Math.atan2()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#using_math.atan2)

### [Difference between Math.atan2(y, x) and Math.atan(y / x)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#difference_between_math.atan2y_x_and_math.atany_x)

The following script prints all inputs that produce a difference between `Math.atan2(y, x)` and `Math.atan(y / x)`.

The output is:

| x     | y     | atan2 | atan  |
|-------|-------|-------|-------|
| -∞    | -∞    | -3π/4 | NaN   |
| -∞    | -1    | -π    | 0     |
| -∞    | -0    | -π    | 0     |
| -∞    | 0     | π     | -0    |
| -∞    | 1     | π     | -0    |
| -∞    | ∞     | 3π/4  | NaN   |
| -1    | -∞    | -π/2  | π/2   |
| -1    | -1    | -3π/4 | π/4   |
| -1    | -0    | -π    | 0     |
| -1    | 0     | π     | -0    |
| -1    | 1     | 3π/4  | -π/4  |
| -1    | ∞     | π/2   | -π/2  |
| -0    | -∞    | -π/2  | π/2   |
| -0    | -1    | -π/2  | π/2   |
| -0    | -0    | -π    | NaN   |
| -0    | 0     | π     | NaN   |
| -0    | 1     | π/2   | -π/2  |
| -0    | ∞     | π/2   | -π/2  |
| 0     | -0    | -0    | NaN   |
| 0     | 0     | 0     | NaN   |
| ∞     | -∞    | -π/4  | NaN   |
| ∞     | ∞     | π/4   | NaN   |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-math.atan2](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-math.atan2) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`Math.acos()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/acos)
    
*   [`Math.asin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/asin)
    
*   [`Math.atan()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan)
    
*   [`Math.cos()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cos)
    
*   [`Math.sin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sin)
    
*   [`Math.tan()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/tan)
    
*   CSS [`atan2()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2)
     function

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 29, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/math/atan2/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/math/atan2 (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMath%2Fatan2&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmath%2Fatan2%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMath%2Fatan2%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmath%2Fatan2%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0fb5a7e4cc045ba0b1dc453624f196309d9bea10%0A*+Document+last+modified%3A+2025-12-29T17%3A25%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")