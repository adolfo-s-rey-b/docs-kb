*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#mdn-search)
    

CSS view transitions
====================

The **CSS view transitions** module defines the behavior of the [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
, which allows developers to create animated transitions between different states within a document and across documents. This module also defines the CSS properties and pseudo-elements for styling these transitions.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#reference)

------------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#properties)

*   [`view-transition-class`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class)
    
*   [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
    
*   [`view-transition-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope)
    

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#at-rules_and_descriptors)

*   [`@view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)
    *   [`navigation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#navigation)
         descriptor

### [Selectors and pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#selectors_and_pseudo-elements)

*   [`:active-view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition)
    
*   [`:active-view-transition-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type)
    
*   [`::view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition)
    
*   [`::view-transition-image-pair()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair)
    
*   [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
    
*   [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
    
*   [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#interfaces)

*   [`CSSViewTransitionRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSViewTransitionRule)
    
*   [`ViewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition)
    *   [`ViewTransition.skipTransition()`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition/skipTransition)
         method
    *   [`ViewTransition.updateCallbackDone`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition/updateCallbackDone)
        
    *   [`ViewTransition.ready`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition/ready)
        
    *   [`ViewTransition.finished`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition/finished)
        
    *   [`ViewTransition.transitionRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition/transitionRoot)
        
*   [`Document.startViewTransition()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/startViewTransition)
     method
*   [`Document.activeViewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/Document/activeViewTransition)
    
*   [`Element.startViewTransition()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/startViewTransition)
     method
*   [`Element.activeViewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/Element/activeViewTransition)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#guides)

------------------------------------------------------------------------------------------

[Using the View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using)

Explains how to create view transitions and customize transition animations, including manipulating active view transitions.

[Using view transition types](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types)

Shows how to use types along with same-document view transitions and cross-document view transitions.

[Using element-scoped view transitions](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_element-scoped)

Covers how element-scoped view transitions work, and how to use them.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#related_concepts)

--------------------------------------------------------------------------------------------------------------

*   [`pagereveal`](https://developer.mozilla.org/en-US/docs/Web/API/PageRevealEvent "pagereveal")
     event
    
*   [`pageswap`](https://developer.mozilla.org/en-US/docs/Web/API/PageSwapEvent "pageswap")
     event
    
*   [`Document.visibilityState`](https://developer.mozilla.org/en-US/docs/Web/API/Document/visibilityState)
    
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
    
    *   [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
        
    *   [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
        
    *   [`CSSKeyframesRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSKeyframesRule)
        
    *   [`CSSStyleRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleRule)
        
    *   [Web animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
        
*   [CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms)
     module
    
    *   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
        
    *   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
        

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 1](https://drafts.csswg.org/css-view-transitions-1/) |
| [CSS View Transitions Module Level 2](https://drafts.csswg.org/css-view-transitions-2/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions#see_also)

----------------------------------------------------------------------------------------------

*   [Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
    
*   [Functional pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#functional_pseudo-classes)
    
*   [Learn: Pseudo-classes and pseudo-elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Pseudo_classes_and_elements)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 19, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/view_transitions/index.md?plain=1 "Folder: en-us/web/css/guides/view_transitions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FView_transitions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fview_transitions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FView_transitions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fview_transitions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3114d1b72a4d46d314caa7f73f775a1f6f7407dc%0A*+Document+last+modified%3A+2026-06-19T17%3A02%3A58.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")