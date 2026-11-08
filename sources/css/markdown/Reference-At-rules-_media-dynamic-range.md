*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#mdn-search)
    

`dynamic-range` CSS media feature
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since May 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`dynamic-range`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test the combination of brightness, contrast ratio, and color depth that are supported by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 and the output device.

**Note:** Some devices have high dynamic range capabilities that are not always 'on' and need to be activated (sometimes programmatically, sometimes by the user, sometimes based on the content). This media feature does not test whether the dynamic range capability is active; it only tests whether the device is capable of high dynamic range visuals.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#syntax)

----------------------------------------------------------------------------------------------------------

The `dynamic-range` feature is specified as a keyword value chosen from the list below.

[`standard`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#standard)

This value matches any visual device and excludes devices lacking visual capabilities. A user agent or an output device that matches `high` will also match the `standard` value.

[`high`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#high)

This value matches user agents and output devices that support high peak brightness, high contrast ratio, and color depth greater than 24 bit or 8 bit per color component of RGB. **Peak brightness** refers to how bright the brightest point a light-emitting device, such as an LCD screen, can produce. In the case of a light-reflective device, such as paper or e-ink, peak brightness refers to the point that at least absorbs light. **Contrast ratio** refers to the ratio of the luminance of the brightest color to that of the darkest color that the system is capable of producing. Currently, there is no precise way to measure peak brightness and contrast ratio, and the determination of what counts as high peak brightness and high contrast ratio depends on the user agent.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#examples)

--------------------------------------------------------------------------------------------------------------

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 5  <br>\# dynamic-range](https://drafts.csswg.org/mediaqueries-5/#dynamic-range) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Using Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/dynamic-range/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/dynamic-range (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdynamic-range&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdynamic-range%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdynamic-range%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdynamic-range%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")