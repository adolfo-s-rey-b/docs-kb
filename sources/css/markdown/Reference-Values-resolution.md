*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#mdn-search)
    

`<resolution>` CSS type
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<resolution>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
, used for describing [resolutions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/resolution)
 in [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
, denotes the pixel density of an output device, i.e., its resolution.

On screens, the units are related to _CSS_ inches, centimeters, or pixels, not physical values.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#syntax)

----------------------------------------------------------------------------------------------

The `<resolution>` data type consists of a strictly positive [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 followed by one of the units listed below. As with all CSS dimensions, there is no space between the unit literal and the number.

### [Units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#units)

[`dpi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#dpi)

Represents the number of [dots per inch](https://en.wikipedia.org/wiki/Dots_per_inch "External link (opens in new tab)")
. Screens typically contains 72 or 96 dots per inch, but the dpi for printed documents is usually much greater. As 1 inch is 2.54 cm, `1dpi ≈ 0.39dpcm`.

[`dpcm`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#dpcm)

Represents the number of [dots per centimeter](https://en.wikipedia.org/wiki/Dots_per_inch "External link (opens in new tab)")
. As 1 inch is 2.54 cm, `1dpcm ≈ 2.54dpi`.

[`dppx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#dppx)

Represents the number of dots per [`px`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#px)
 unit. Due to the 1:96 fixed ratio of CSS `in` to CSS `px`, `1dppx` is equivalent to `96dpi`, which corresponds to the default resolution of images displayed in CSS as defined by [`image-resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution)
.

[`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#x)

Alias for `dppx`.

**Note:** Although the number `0` is always the same regardless of unit, the unit may not be omitted. In other words, `0` is invalid and does not represent `0dpi`, `0dpcm`, or `0dppx`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#examples)

--------------------------------------------------------------------------------------------------

### [Use in a media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#use_in_a_media_query)

### [Valid resolutions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#valid_resolutions)

96dpi
50.82dpcm
3dppx

### [Invalid resolutions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#invalid_resolutions)

72 dpi     Spaces are not allowed between the number and the unit.
ten dpi    The number must use digits only.
0          The unit is required.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# resolution](https://drafts.csswg.org/css-values/#resolution) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#see_also)

--------------------------------------------------------------------------------------------------

*   [resolution](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/resolution)
     media feature
*   The [`image-resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution)
     property
*   [Using @media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/resolution/index.md?plain=1 "Folder: en-us/web/css/reference/values/resolution (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fresolution&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fresolution%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fresolution%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fresolution%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")