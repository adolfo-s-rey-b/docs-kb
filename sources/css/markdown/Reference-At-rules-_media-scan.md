*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#mdn-search)
    

`scan` CSS media feature
========================

The **`scan`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 is used to apply CSS styles based on the scanning process of the output device.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#syntax)

-------------------------------------------------------------------------------------------------

The `scan` feature is specified as one of the following keyword values:

[`interlace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#interlace)

The output device uses "interlaced" rendering, where video frames alternate between specifying only the "even" lines on the screen and only the "odd" lines.

[`progressive`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#progressive)

The output device renders content to the screen with no special treatment.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#description)

-----------------------------------------------------------------------------------------------------------

Most modern screens (and all computer screens) use progressive rendering, displaying each screen fully with no special treatment.

Interlacing was used by CRT monitors and some plasma TVs to enable the appearance of faster frames per second (FPS) while reducing bandwidth. With interlacing, video frames alternate between rendering the even lines and the odd lines on the screen, downloading and rendering only half the screen for each frame, exploiting the human image-smoothing ability so the brain simulates a higher FPS broadcast at half the bandwidth cost.

When targeting interlaced screens, avoid very fast movement across the screen and ensure animated details are wider than 1px to reduce flickering.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#examples)

-----------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#css)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# scan](https://drafts.csswg.org/mediaqueries/#scan) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan#see_also)

-----------------------------------------------------------------------------------------------------

*   The [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     at-rule, which is used to specify the scan expression.
*   [Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
     to understand when and how to use a media query.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/scan/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/scan (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fscan&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fscan%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fscan%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fscan%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5a41c90092765ffe35958f439c2ab626714db340%0A*+Document+last+modified%3A+2026-07-18T08%3A08%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")