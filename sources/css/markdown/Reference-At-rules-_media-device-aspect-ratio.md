*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio#mdn-search)
    

`device-aspect-ratio` CSS media feature
=======================================

Deprecated

Avoid using this feature in new projects. Device media queries do not reflect available layout, only the physical size of the device. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media "The @media CSS rule conditionally applies styles based on the output device type, its capabilities, and the user's preferences. Media queries are composed of an optional media type such as screen or print, and one or more mandatory media features, such as prefers-reduced-animations.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** To query for the [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 of the viewport, developers should use the [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio)
 media feature instead.

The **`device-aspect-ratio`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test the width-to-height [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 of an output device.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio#syntax)

----------------------------------------------------------------------------------------------------------------

The `device-aspect-ratio` feature is specified as a [`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
. It is a range feature, meaning that you can also use the prefixed **`min-device-aspect-ratio`** and **`max-device-aspect-ratio`** variants to query minimum and maximum values, respectively.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio#examples)

--------------------------------------------------------------------------------------------------------------------

### [Using min-device-aspect-ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio#using_min-device-aspect-ratio)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# device-aspect-ratio](https://drafts.csswg.org/mediaqueries/#device-aspect-ratio) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/device-aspect-ratio/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/device-aspect-ratio (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdevice-aspect-ratio&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdevice-aspect-ratio%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdevice-aspect-ratio%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdevice-aspect-ratio%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")