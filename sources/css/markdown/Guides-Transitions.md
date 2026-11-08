*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#mdn-search)
    

CSS transitions
===============

The **CSS transitions** module specifies functionality for creating gradual transitions between different CSS property values. The behavior of these transitions can be controlled by specifying their easing function, duration, and other values.

Normally, when the value of a CSS property changes, the result of the change from the old value to the new value is immediate. The CSS transitions module enables controlling a progression from the old property state to the new state over a specified period of time. It also provides event handlers to allow code to be run in response to different stages of a transition being reached.

In certain cases, there is no originating "from" value for a transition. For example, if an element gets added to the DOM, the styles defined are for the "to" state. This module provides the [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
 at-rule, which enables defining starting styles for such cases. The module also defines how discrete property values should be transitioned, such as transitioning the discretely animated [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property from the `none` value to a displayed value.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#reference)

-------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#properties)

*   [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
    
*   [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
    
*   [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
    
*   [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
    
*   [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
    
*   [`transition-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
    

### [At rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#at_rules)

*   [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#interfaces)

*   [`CSSStartingStyleRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStartingStyleRule)
    
*   [`CSSTransition`](https://developer.mozilla.org/en-US/docs/Web/API/CSSTransition)
    *   [`transitionProperty`](https://developer.mozilla.org/en-US/docs/Web/API/CSSTransition/transitionProperty "transitionProperty")
         property
*   [`TransitionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent)
    *   [`TransitionEvent()`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent/TransitionEvent "TransitionEvent()")
         constructor
    *   [`TransitionEvent.propertyName`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent/propertyName)
         property
    *   [`TransitionEvent.elapsedTime`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent/elapsedTime)
         property
    *   [`TransitionEvent.pseudoElement`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent/pseudoElement)
         property
    *   [`transitioncancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitioncancel_event "transitioncancel")
         event
    *   [`transitionend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionend_event "transitionend")
         event
    *   [`transitionrun`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionrun_event "transitionrun")
         event
    *   [`transitionstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionstart_event "transitionstart")
         event

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#guides)

-------------------------------------------------------------------------------------

[Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)

Step-by-step tutorial explaining how to create transitions using CSS. This article describes each relevant CSS property and explains how they interact with each other.

[Animating `display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display#animating_display)

Transitioning to and from the `none` value of the discretely animated [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property.

[Transitioning a popover](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#transitioning_a_popover)
 and [transitioning a `<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog#transitioning_dialog_elements)

Examples of transitioning from [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
 to final [`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
 and [`:open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open)
 pseudo-class styles.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#related_concepts)

---------------------------------------------------------------------------------------------------------

*   [`interpolate-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size)
     property
    
*   [`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
     function
    
*   [Intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
     glossary term
    
*   [CSS easing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Easing_functions)
     module:
    
    *   [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
         data-type
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module:
    
    *   [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
         shorthand
    *   [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
        
    *   [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
        
    *   [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
        
    *   [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
        
    *   [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
        
    *   [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
        
    *   [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
        
    *   [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
        
*   [CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms)
     module:
    
    *   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
        
    *   [`transform-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box)
        
    *   [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
        
    *   [`transform-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style)
        
*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module:
    
    *   [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
        
    *   [`scroll-padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
        
    *   [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
        
    *   [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
        
    *   [`scroll-snap-stop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
        

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#specifications)

-----------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transitions Module Level 1](https://drafts.csswg.org/css-transitions-1/) |
| [CSS Transitions Module Level 2](https://drafts.csswg.org/css-transitions-2/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions#see_also)

-----------------------------------------------------------------------------------------

*   [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    
*   [`visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
    
*   [`ViewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition)
     interface
*   [`PageTransitionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/PageTransitionEvent)
     interface

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/transitions/index.md?plain=1 "Folder: en-us/web/css/guides/transitions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FTransitions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ftransitions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FTransitions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ftransitions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")