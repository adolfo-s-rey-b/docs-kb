*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading#mdn-search)
    

CSS font loading
================

The **CSS font loading** module describes events and interfaces used for dynamically loading font resources.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading#reference)

--------------------------------------------------------------------------------------------

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading#interfaces)

*   [`fontFace`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace)
     interface
    *   [`FontFace()`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace)
         constructor
    *   [`fontFace.family`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/family)
         property
    *   [`fontFace.style`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/style)
         property
    *   [`fontFace.weight`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/weight)
         property
    *   [`fontFace.stretch`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/stretch)
         property
    *   [`fontFace.unicodeRange`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/unicodeRange)
         property
    *   [`fontFace.variant`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/variant)
         property
    *   [`fontFace.featureSettings`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/featureSettings)
         property
    *   [`fontFace.variationSettings`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/variationSettings)
         property
    *   [`fontFace.display`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/display)
         property
    *   [`fontFace.ascentOverride`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/ascentOverride)
         property
    *   [`fontFace.descentOverride`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/descentOverride)
         property
    *   [`fontFace.lineGapOverride`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/lineGapOverride)
         property
    *   [`fontFace.sizeAdjust`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/sizeAdjust)
         property
    *   [`fontFace.load()`](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/load)
         method (returns a promise)
*   [`fontFaceSet`](https://developer.mozilla.org/en-US/docs/Web/API/FontFaceSet)
     interface
*   [`fontFaceSetLoadEvent`](https://developer.mozilla.org/en-US/docs/Web/API/FontFaceSetLoadEvent)
     event

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading#guides)

--------------------------------------------------------------------------------------

[CSS font loading API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Font_Loading_API)

Overview of the CSS Font Loading API, which provide events and interfaces for dynamically loading font resources.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading#related_concepts)

----------------------------------------------------------------------------------------------------------

*   CSS [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
     at-rule
*   CSS [`@font-feature-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)
     at-rule
*   [`CSSFontFaceRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFontFaceRule)
     interface
*   Document [`fonts`](https://developer.mozilla.org/en-US/docs/Web/API/Document/fonts "fonts")
     property (returns the [`FontFaceSet`](https://developer.mozilla.org/en-US/docs/Web/API/FontFaceSet)
     object instance)
*   WorkerGlobalScope [`fonts`](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/fonts "fonts")
     property (returns the [`FontFaceSet`](https://developer.mozilla.org/en-US/docs/Web/API/FontFaceSet)
     object instance)
*   JavaScript [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
     object

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading#specifications)

------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Font Loading Module Level 3](https://drafts.csswg.org/css-font-loading/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading#see_also)

------------------------------------------------------------------------------------------

*   [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/font_loading/index.md?plain=1 "Folder: en-us/web/css/guides/font_loading (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFont_loading&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ffont_loading%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFont_loading%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ffont_loading%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F106f215d6fb32a7ee0afe09f01a82323d39cd1f0%0A*+Document+last+modified%3A+2026-11-03T01%3A26%3A19.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")