*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#mdn-search)
    

`<hex-color>` CSS type
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<hex-color>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 is a notation for describing the _hexadecimal color syntax_ of an [sRGB](https://developer.mozilla.org/en-US/docs/Glossary/RGB)
 color using its primary color components (red, green, blue) written as hexadecimal numbers, as well as its transparency.

A `<hex-color>` value can be used everywhere where a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 can be used.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#syntax)

---------------------------------------------------------------------------------------------

#RGB        // The three-value syntax
#RGBA       // The four-value syntax
#RRGGBB     // The six-value syntax
#RRGGBBAA   // The eight-value syntax

### [Value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#value)

[`R` or `RR`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#r)

The _red_ component of the color, as a case-insensitive hexadecimal number between `0` and `ff` (255). If there is only one number, it is duplicated: `1` means `11`.

[`G` or `GG`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#g)

The _green_ component of the color, as a case-insensitive hexadecimal number between `0` and `ff` (255). If there is only one number, it is duplicated: `c` means `cc`.

[`B` or `BB`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#b)

The _blue_ component of the color, as a case-insensitive hexadecimal number between `0` and `ff` (255). If there is only one number, it is duplicated: `9` means `99`.

[`A` or `AA` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#a)

The _alpha_ component of the color, indicating its transparency, as a case-insensitive hexadecimal number between `0` and `ff` (255). If there is only one number, it is duplicated: `e` means `ee`. `0`, or `00`, represents a fully transparent color, and `f`, or `ff`, a fully opaque one.

**Note:** The syntax is case-insensitive: `#00ff00` is the same as `#00FF00`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#examples)

-------------------------------------------------------------------------------------------------

### [Hexadecimal hot pink](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#hexadecimal_hot_pink)

This example includes four hot pink squares, with fully opaque or semi-transparent backgrounds created using four different-length case-insensitive hex-color syntaxes.

#### HTML

#### CSS

The hot pink background colors are created using the three-, four-, six-, and eight-value hex notations, using both uppercase and lowercase letters.

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 4  <br>\# hex-notation](https://drafts.csswg.org/css-color/#hex-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color#see_also)

-------------------------------------------------------------------------------------------------

*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     data type
*   [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
     data-type
*   [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
     color function
*   [CSS color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/hex-color/index.md?plain=1 "Folder: en-us/web/css/reference/values/hex-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fhex-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fhex-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fhex-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fhex-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")