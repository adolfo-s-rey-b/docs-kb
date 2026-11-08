*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#mdn-search)
    

`<integer>` CSS type
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<integer>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 is a special type of [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 that represents a positive or negative whole number. Integers can be used in numerous CSS properties and descriptors, such as the [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
, [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
, [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
, [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
, and [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
 properties and the [`range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range)
 descriptor.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#syntax)

-------------------------------------------------------------------------------------------

The `<integer>` data type consists of one or several decimal digits, 0 through 9 inclusive, optionally preceded by a single `+` or `-` sign. There is no unit associated with integers.

**Note:** There is no official range of valid `<integer>` values, and the specifications do not specify a range.

[Interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#interpolation)

---------------------------------------------------------------------------------------------------------

When animated, values of the `<integer>` data type are [interpolated](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 using discrete, whole steps. The calculation is done as if they were real, floating-point numbers; the discrete value is obtained using the [floor function](https://en.wikipedia.org/wiki/Floor_function "External link (opens in new tab)")
. The speed of the interpolation is determined by the [easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 associated with the animation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#examples)

-----------------------------------------------------------------------------------------------

### [Valid integers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#valid_integers)

12          Positive integer (without a leading + sign)
+123        Positive integer (with a leading + sign)
-456        Negative integer
0           Zero
+0          Zero, with a leading +
-0          Zero, with a leading -

### [Invalid integers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#invalid_integers)

12.0        This is a <number>, not an <integer>, though it represents an integer.
12.         Decimal points are not allowed.
+---12      Only one leading +/- is allowed.
ten         Letters are not allowed.
\_5          Special characters are not allowed.
\\35         Escaped Unicode characters are not allowed, even if they are an integer (here: 5).
\\4E94       Non-arabic numerals are not allowed, even when escaped (here: the Japanese 5, 五).
3e4         Scientific notation is not allowed.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# integers](https://drafts.csswg.org/css-values/#integers) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#see_also)

-----------------------------------------------------------------------------------------------

*   [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/integer/index.md?plain=1 "Folder: en-us/web/css/reference/values/integer (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Finteger&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Finteger%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Finteger%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Finteger%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")