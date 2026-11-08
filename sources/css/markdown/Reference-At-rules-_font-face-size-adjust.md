*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#mdn-search)
    

`size-adjust` CSS at-rule descriptor
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`size-adjust`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 descriptor for the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule defines a multiplier for glyph outlines and metrics associated with this font. This makes it easier to harmonize the designs of various fonts when rendered at the same font size.

The `size-adjust` descriptor behaves in a similar fashion to the [`font-size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust)
 property. It calculates an adjustment per font by matching ex heights.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#syntax)

------------------------------------------------------------------------------------------------------------

css

    size-adjust: 90%;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#values)

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#percentage)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value with an initial value of 100%.

All metrics associated with this font are scaled by the given percentage. This includes glyph advances, baseline tables, and overrides provided by [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 descriptors.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `100%` |
| Percentages | as specified |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

size-adjust =   
  [<percentage \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#examples)

----------------------------------------------------------------------------------------------------------------

### [Overriding metrics of a fallback font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#overriding_metrics_of_a_fallback_font)

The `size-adjust` property can help when overriding the metrics of a fallback font to better match those of a primary web font.

css

    @font-face {
      font-family: "web-font";
      src: url("https://example.com/font.woff");
    }
    
    @font-face {
      font-family: "local-font";
      src: local("Local Font");
      size-adjust: 90%;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 5  <br>\# size-adjust-desc](https://drafts.csswg.org/css-fonts-5/#size-adjust-desc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
     descriptor
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
     descriptor
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
     descriptor
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
     descriptor
*   [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)
     descriptor
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    
*   [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
     descriptor
*   [`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
     descriptor
*   [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
     descriptor
*   [`font-size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust)
     property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-face/size-adjust/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-face/size-adjust (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Fsize-adjust&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Fsize-adjust%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Fsize-adjust%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Fsize-adjust%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")