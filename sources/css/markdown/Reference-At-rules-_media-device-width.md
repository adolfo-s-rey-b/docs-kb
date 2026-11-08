*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width#mdn-search)
    

`device-width` CSS media feature
================================

Deprecated

Avoid using this feature in new projects. Device media queries do not reflect available layout, only the physical size of the device. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media "The @media CSS rule conditionally applies styles based on the output device type, its capabilities, and the user's preferences. Media queries are composed of an optional media type such as screen or print, and one or more mandatory media features, such as prefers-reduced-animations.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** To query for the width of the viewport, developers should use the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/width)
 media feature instead.

The **`device-width`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test the width of an output device's rendering surface.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width#syntax)

---------------------------------------------------------------------------------------------------------

The `device-width` feature is specified as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value. It is a range feature, meaning that you can also use the prefixed **`min-device-width`** and **`max-device-width`** variants to query minimum and maximum values, respectively.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width#examples)

-------------------------------------------------------------------------------------------------------------

### [Applying a special stylesheet for devices that are narrower than 800 pixels](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width#applying_a_special_stylesheet_for_devices_that_are_narrower_than_800_pixels)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# device-width](https://drafts.csswg.org/mediaqueries/#device-width) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Using Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/device-width/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/device-width (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdevice-width&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdevice-width%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdevice-width%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdevice-width%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")