*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring#mdn-search)
    

CSS scroll anchoring
====================

The **CSS scroll anchoring** module defines a mechanism to prevent page movement due to DOM changes above the visible region of a scrolling box while the user is consuming the visible content.

Scroll anchoring attempts to keep the user's view of the document stable across layout changes. It works by selecting a DOM node (the anchor node) whose movement is used to determine adjustments to the scroll position. The anchor node is always a descendant of the scrolling box.

For scroll containers that are [snapped](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap)
 to an element, scroll anchoring is limited to adjustments that would be allowed by re-snapping.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring#reference)

------------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring#properties)

*   [`overflow-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor)
    

[Glossary terms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring#glossary_terms)

----------------------------------------------------------------------------------------------------------

*   [Scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
    
*   [Scroll snap](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring#guides)

------------------------------------------------------------------------------------------

[Overview of scroll anchoring](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring/Overview)

What is scroll anchoring, suppression triggers, and when and how to enable and disable this browser feature.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring#related_concepts)

--------------------------------------------------------------------------------------------------------------

*   [`overscroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Anchoring Module Level 1](https://drafts.csswg.org/css-scroll-anchoring/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring#see_also)

----------------------------------------------------------------------------------------------

*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [CSS overscroll behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overscroll_behavior)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/scroll_anchoring/index.md?plain=1 "Folder: en-us/web/css/guides/scroll_anchoring (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll_anchoring&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fscroll_anchoring%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll_anchoring%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fscroll_anchoring%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")