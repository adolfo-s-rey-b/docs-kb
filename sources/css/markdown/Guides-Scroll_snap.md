*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#mdn-search)
    

CSS scroll snap
===============

The **CSS scroll snap** module provides properties that let you control the panning and scrolling behavior by defining snap positions. Content can be snapped into position as the user scrolls overflowing content within a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
, providing paging and scroll positioning.

This module includes the scroll container scroll-padding properties to adjust the optimal viewing region of paging during scroll-into-view operations. It also includes scroll-margin and scroll-alignment, set on the scroll container's children, to adjust the children's visual area when that child is scrolled into view, as well as a property to force scrolling to stop on individual children.

[Scroll snap in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#scroll_snap_in_action)

-------------------------------------------------------------------------------------------------------------------

To view scroll snapping in the box below, scroll up-and-down and left-and-right through the grid of 45 numbered boxes in the scrollable viewport. Click "Play" in the example below to view or edit the source in the MDN Playground:

With scroll snap, one of the numbered boxes that you scroll to will snap into place. The initial CSS makes the numbered box snap into the center of the viewport. Use the sliders to change the block and inline snap positions.

Using snap properties, you can allow or block the scrolling past an element, a numbered box in this case. Select the "Prevent scrolling past boxes" checkbox to force all scrolling actions to be limited to scrolling to an adjacent box.

To compare scroll snapping to regular scrolling, check the "disable snapping" checkbox and try scrolling again.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#reference)

-------------------------------------------------------------------------------------------

### [Properties on containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#properties_on_containers)

*   [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
    
*   [`scroll-padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
    *   [`scroll-padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-top)
        
    *   [`scroll-padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-right)
        
    *   [`scroll-padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-bottom)
        
    *   [`scroll-padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-left)
        
    *   [`scroll-padding-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline)
        
    *   [`scroll-padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-start)
        
    *   [`scroll-padding-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-end)
        
    *   [`scroll-padding-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block)
        
    *   [`scroll-padding-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block-start)
        
    *   [`scroll-padding-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block-end)
        

### [Properties on children](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#properties_on_children)

*   [`scroll-initial-target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target)
    
*   [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
    *   [`scroll-margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-top)
        
    *   [`scroll-margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-right)
        
    *   [`scroll-margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-bottom)
        
    *   [`scroll-margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-left)
        
    *   [`scroll-margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline)
        
    *   [`scroll-margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start)
        
    *   [`scroll-margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-end)
        
    *   [`scroll-margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block)
        
    *   [`scroll-margin-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-start)
        
    *   [`scroll-margin-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end)
        
*   [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
    
*   [`scroll-snap-stop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
    

### [Events](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#events)

*   [`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchange_event "scrollsnapchange")
    
*   [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event "scrollsnapchanging")
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#interfaces)

*   [`SnapEvent`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent)
    *   [`SnapEvent.snapTargetBlock`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent/snapTargetBlock)
        
    *   [`SnapEvent.snapTargetInline`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent/snapTargetInline)
        

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#guides)

-------------------------------------------------------------------------------------

[Basic concepts of CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts)

An overview and examples of CSS scroll snap features.

[Using scroll snap events](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events)

A guide to using the [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event "scrollsnapchanging")
 and [`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchange_event "scrollsnapchange")
 scroll snap events that are fired when the browser determines a new snap target is pending or selected.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#related_concepts)

---------------------------------------------------------------------------------------------------------

*   [`:target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target)
     pseudo-class
*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
     CSS property
*   Element [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scroll "scroll()")
     method
*   Element [`scrollBy()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollBy "scrollBy()")
     method
*   Element [`scrollIntoView()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView "scrollIntoView()")
     method
*   Element [`scrollTo()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTo "scrollTo()")
     method
*   Element [`scroll`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scroll_event "scroll")
     event
*   Element [`scrollend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollend_event "scrollend")
     event
*   [`scrollbar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/scrollbar_role)
     ARIA role
*   [Scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
     glossary term

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#specifications)

-----------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 1](https://drafts.csswg.org/css-scroll-snap/) |
| [CSS Scroll Snap Module Level 2](https://drafts.csswg.org/css-scroll-snap-2/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap#see_also)

-----------------------------------------------------------------------------------------

*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS scrollbars styling](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scrollbars_styling)
     module
*   [CSS scroll anchoring](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring)
     module
*   [Keyboard-only scrolling areas](https://adrianroselli.com/2022/06/keyboard-only-scrolling-areas.html "External link (opens in new tab)")
     on adrianroselli.com (2022)
*   [Scroll snap examples](https://codepen.io/collection/KpqBGW "External link (opens in new tab)")
     on CodePen (2022)
*   [Practical CSS scroll snapping/](https://css-tricks.com/practical-css-scroll-snapping/ "External link (opens in new tab)")
     on CSS-Tricks (2020)
*   [CSS scroll snap](https://12daysofweb.dev/2022/css-scroll-snap/ "External link (opens in new tab)")
     on 12 Days of Web (2019)
*   [Well-controlled scrolling with CSS scroll snap](https://web.dev/articles/css-scroll-snap "External link (opens in new tab)")
     on web.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/scroll_snap/index.md?plain=1 "Folder: en-us/web/css/guides/scroll_snap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll_snap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fscroll_snap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll_snap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fscroll_snap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1474534461893381d54c502e655f334b5568e597%0A*+Document+last+modified%3A+2026-08-21T19%3A37%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")