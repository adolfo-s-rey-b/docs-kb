*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#mdn-search)
    

`vertical-viewport-segments` CSS media feature
==============================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/382)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#browser_compatibility)
 carefully before using this in production.

The **`vertical-viewport-segments`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 detects whether the device has a specified number of viewport segments laid out vertically (top to bottom).

Related to the [Viewport Segments API](https://developer.mozilla.org/en-US/docs/Web/API/Viewport_segments_API)
, the `vertical-viewport-segments` feature can be used to create responsive designs that work well on multi-viewport devices — devices with a display that is divided into logically separate viewport segments, such as foldable or hinged devices.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#syntax)

-----------------------------------------------------------------------------------------------------------------------

The `vertical-viewport-segments` feature is specified as an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 value of `1` or greater, representing the number of vertical viewport segments the device has.

*   The value will be `1` for:
    *   A non-foldable device (for example, a standard single-screen smartphone or tablet).
    *   A foldable device that is either unfolded or closed (in the [`continuous` device posture](https://developer.mozilla.org/en-US/docs/Web/API/Device_Posture_API#continuous)
        ).
    *   A two-screen hinged device or a foldable device that is currently folded and is oriented horizontally so the segments are side by side.
*   The value will be `2` for a two-screen hinged device or a foldable device that is currently folded (in the [`folded` device posture](https://developer.mozilla.org/en-US/docs/Web/API/Device_Posture_API#folded)
    ) and is oriented vertically so the segments are on top of one another.
*   The value may be greater than `2` for foldable devices with more than one fold.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Basic `vertical-viewport-segments` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#basic_vertical-viewport-segments_usage)

In this snippet we use a `vertical-viewport-segments` media query to handle the case of foldable devices where the segments are top-to-bottom.

We set the top container to have a height equal to the top segment height (`env(viewport-segment-height 0 0)`), and the bottom container to have a height equal to the bottom segment height (`env(viewport-segment-height 0 1)`).

To calculate how much height the fold takes up in between the two, we subtract the bottom edge offset of the top container from the top edge offset of the bottom container (`calc(env(viewport-segment-top 0 1) - env(viewport-segment-bottom 0 0));`).

See our [Viewport segment API demo](https://mdn.github.io/dom-examples/viewport-segments-api/ "External link (opens in new tab)")
 for a full working demo ([source code](https://github.com/mdn/dom-examples/tree/main/viewport-segments-api "External link (opens in new tab)")
). Also check out [Using the Viewport Segments API](https://developer.mozilla.org/en-US/docs/Web/API/Viewport_segments_API/Using)
 for a full demo explanation.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 5  <br>\# mf-vertical-viewport-segments](https://drafts.csswg.org/mediaqueries-5/#mf-vertical-viewport-segments) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [`horizontal-viewport-segments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/horizontal-viewport-segments)
     `@media` feature
*   [Viewport Segments API](https://developer.mozilla.org/en-US/docs/Web/API/Viewport_segments_API)
    
*   [Origin trial for Foldable APIs](https://developer.chrome.com/blog/foldable-apis-ot "External link (opens in new tab)")
     via developer.chrome.com (2024)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/vertical-viewport-segments/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/vertical-viewport-segments (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fvertical-viewport-segments&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fvertical-viewport-segments%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fvertical-viewport-segments%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fvertical-viewport-segments%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")