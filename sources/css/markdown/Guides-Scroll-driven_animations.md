*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#mdn-search)
    

CSS scroll-driven animations
============================

The **CSS scroll-driven animations** module provides functionality that builds on the [CSS animations module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 and [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
. It allows you to animate property values along a scroll-based timeline rather than the default time-based document timeline. This means that you can animate an element by scrolling the element, its scroll container, or its root element, rather than just by the passing of time.

[Scroll-driven animations in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#scroll-driven_animations_in_action)

----------------------------------------------------------------------------------------------------------------------------------------------------------

You can define the scroller that controls the animation either by naming the animation or with the [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 or [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
 functions.

Scroll the element in the inline direction to see its background color change. Scroll it vertically to see the generated content move, spin, and change colors.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#reference)

--------------------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#properties)

*   [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
     shorthand
    *   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
        
    *   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
        
*   [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
     shorthand
    *   [`scroll-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
        
    *   [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
        
*   [`timeline-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope)
    
*   [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
     shorthand
    *   [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
        
    *   [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
        
    *   [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
        

### [Data types and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#data_types_and_values)

*   [`<axis>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
    
*   [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
    

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#functions)

*   [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
    
*   [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#interfaces)

*   [`ScrollTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/ScrollTimeline)
    
*   [`ViewTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTimeline)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#guides)

--------------------------------------------------------------------------------------------------

[Scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)

Scroll-driven animation timelines and creating scroll-driven animations.

[Timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)

The [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
 data type: Understanding the various timeline range names.

[Using CSS scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)

Creating scroll-triggered animations.

[Insetting view progress timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_insets)

Insetting the animation attachment ranges of scroll-driven animations.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#related_concepts)

----------------------------------------------------------------------------------------------------------------------

*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
    *   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
        
    *   [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
         at-rule
    *   [`<keyframe-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors)
        
*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
    *   [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
        
    *   [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
         shorthand
    *   [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
         shorthand
        *   [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
            
        *   [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
            
    *   [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
         shorthand
        *   [`timeline-trigger-active-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-end)
            
        *   [`timeline-trigger-active-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start)
            
    *   [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
        
    *   [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
        
    *   [`trigger-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope)
        
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
    *   [Scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
        
    *   [Scrollport](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container#scrollport)
        
*   [Web Animations](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
     API
    *   [`Element.animate()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate)
        
    *   [`Animation`](https://developer.mozilla.org/en-US/docs/Web/API/Animation)
        
    *   [`AnimationTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationTimeline)
        
    *   [`DocumentTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentTimeline)
        
    *   [`KeyframeEffect`](https://developer.mozilla.org/en-US/docs/Web/API/KeyframeEffect)
        

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations](https://drafts.csswg.org/scroll-animations-1/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations#see_also)

------------------------------------------------------------------------------------------------------

*   [Animate elements on scroll with scroll-driven animations](https://developer.chrome.com/docs/css-ui/scroll-driven-animations "External link (opens in new tab)")
     via developer.chrome.com (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/scroll-driven_animations/index.md?plain=1 "Folder: en-us/web/css/guides/scroll-driven_animations (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll-driven_animations&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fscroll-driven_animations%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll-driven_animations%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fscroll-driven_animations%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4aba58b4ad2745a73054f60b6d649d8e29b7b44d%0A*+Document+last+modified%3A+2026-10-05T11%3A36%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")