*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#mdn-search)
    

CSS animations
==============

The **CSS animations** module lets you animate the values of CSS properties, such as background-position and transform, over time by using keyframes. Each keyframe describes how the animated element should render at a given time during the animation sequence. You can use the properties in the animations module to control the duration, number of repetitions, delayed start, and other aspects of an animation.

[Animations in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#animations_in_action)

----------------------------------------------------------------------------------------------------------------

To view the animation in the box below, click the checkbox 'Play the animation' or hover the cursor over the box. When the animation is active, the cloud at the top changes shape, snowflakes fall, and the snow level at the bottom rises. To pause the animation, uncheck the checkbox or move your cursor away from the box.

This sample animation uses [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
 to make the flakes fall repeatedly, [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
 to make the cloud move back and forth, [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
 to raise the snow level in response to the cloud movement, and [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
 to pause the animation.

Click "Play" in the example above to see or edit the code for the animation in the MDN Playground.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#reference)

------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#properties)

*   [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
     shorthand
*   [`animation-composition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    
*   [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    
*   [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    
*   [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    
*   [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    
*   [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    
*   [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    
*   [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    
*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#at-rules_and_descriptors)

*   [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
    
*   [`<keyframe-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors)
    

### [Events](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#events)

All animations, even those with 0 seconds duration, throw animation events.

*   [`animationstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationstart_event "animationstart")
    
*   [`animationend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationend_event "animationend")
    
*   [`animationcancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationcancel_event "animationcancel")
    
*   [`animationiteration`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationiteration_event "animationiteration")
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#interfaces)

*   [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
    
*   [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent)
    
*   [`CSSAnimation`](https://developer.mozilla.org/en-US/docs/Web/API/CSSAnimation)
    
*   [`CSSKeyframeRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSKeyframeRule)
    
*   [`CSSKeyframesRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSKeyframesRule)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#guides)

------------------------------------------------------------------------------------

[Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)

Step-by-step tutorial on how to create animations using CSS. This article describes the animation-related CSS properties and at-rule and how they interact with each other.

[Animatable CSS properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties)

Overview of how different CSS properties can be animated, including their animation types and interpolation methods.

[Using the Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API)

Common animation requirements that can be solved with a few lines of JavaScript.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#related_concepts)

--------------------------------------------------------------------------------------------------------

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
        
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
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
            
*   [`will-change`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)
     CSS property
*   [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
     data type
*   [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
     media query
*   [Bezier curve](https://developer.mozilla.org/en-US/docs/Glossary/Bezier_curve)
     glossary term

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#specifications)

----------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 2](https://drafts.csswg.org/css-animations-2/) |
| [CSS Animations Level 1](https://drafts.csswg.org/css-animations/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations#see_also)

----------------------------------------------------------------------------------------

*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
*   [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
     module
*   The [`interpolate-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size)
     property and [`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
     function for enabling animations to and from [intrinsic size values](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
    .
*   The [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
     HTML element along with [canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
     and [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)
     to draw graphics and animations.
*   The [`SVGAnimationElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGAnimationElement)
     interface for all the animation-related element interfaces, including [`SVGAnimateElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGAnimateElement)
    , [`SVGSetElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGSetElement)
    , [`SVGAnimateColorElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGAnimateColorElement)
    , [`SVGAnimateMotionElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGAnimateMotionElement)
    , and [`SVGAnimateTransformElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGAnimateTransformElement)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/animations/index.md?plain=1 "Folder: en-us/web/css/guides/animations (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnimations&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fanimations%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnimations%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fanimations%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4aba58b4ad2745a73054f60b6d649d8e29b7b44d%0A*+Document+last+modified%3A+2026-10-05T11%3A36%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")