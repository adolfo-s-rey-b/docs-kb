*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#mdn-search)
    

`color-gamut` CSS media feature
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since February 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`color-gamut`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 is used to apply CSS styles based on the approximate range of color [gamut](https://developer.mozilla.org/en-US/docs/Glossary/Gamut)
 supported by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 and the output device.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#syntax)

--------------------------------------------------------------------------------------------------------

The `color-gamut` feature is specified as one of the following [color spaces](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 as keyword values:

[`srgb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#srgb)

The user agent and the output device can support approximately the [sRGB](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#srgb)
 gamut or more. This includes the vast majority of color displays.

[`p3`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#p3)

The user agent and the output device can support approximately the gamut specified by the [Display P3](https://registry.color.org/rgb-registry/displayp3 "External link (opens in new tab)")
 color space or more. The P3 gamut is larger than and includes the sRGB gamut.

[`rec2020`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#rec2020)

The user agent and the output device can support approximately the gamut specified by the [ITU-R Recommendation BT.2020](https://en.wikipedia.org/wiki/Rec._2020 "External link (opens in new tab)")
 color space or more. The REC. 2020 gamut is larger than and includes the P3 gamut.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#examples)

------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#html)

html

    <p>This is a test.</p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#css)

css

    p {
      padding: 10px;
      border: solid;
    }
    
    @media (color-gamut: srgb) {
      p {
        background: #f4ae8a;
      }
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# color-gamut](https://drafts.csswg.org/mediaqueries/#color-gamut) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut#see_also)

------------------------------------------------------------------------------------------------------------

*   [`color()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color)
     function to specify colors in a defined colorspace.
*   [CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module
*   [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     at-rule that is used to specify the color-gamut expression.
*   [Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
     to understand when and how to use a media query.
*   [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
     module
*   [sRGB](https://en.wikipedia.org/wiki/SRGB "External link (opens in new tab)")
     on Wikipedia

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/color-gamut/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/color-gamut (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fcolor-gamut&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fcolor-gamut%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fcolor-gamut%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fcolor-gamut%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")