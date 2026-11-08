*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#mdn-search)
    

CSS anchor positioning
======================

The **CSS anchor positioning** module defines features that allow you to tether elements together. Certain elements are defined as **anchor elements**; **anchor-positioned elements** can then have their size and position set based on the size and location of the anchor elements to which they are bound.

In addition, the specification provides CSS-only mechanisms to:

*   Specify a set of alternative positions for an anchored element; when the default rendering position causes it to overflow its containing block and/or be rendered offscreen, the browser will try rendering the anchored element in the alternative positions instead.
*   Declare conditions under which anchor-positioned elements should be hidden, in situations where it is not appropriate to tether them to anchor elements.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#reference)

--------------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#properties)

*   [`anchor-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope)
    
*   [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
    
*   [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
    
*   [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
    
*   [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
    
*   [`position-try-order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-order)
    
*   [`position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
     shorthand
*   [`position-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility)
    

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#at-rules_and_descriptors)

*   [`@position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
    

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#functions)

*   [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
    
*   [`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
    

### [Data types and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#data_types_and_values)

*   [`anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#centering_on_the_anchor_using_anchor-center)
    
*   [`<anchor-side>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor#anchor-side)
    
*   [`<anchor-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size#anchor-size)
    
*   [`<position-area>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value)
    
*   [`<try-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-order#try-size)
    
*   [`<try-tactic>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks#try-tactic)
    

### [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#html_attributes)

*   [`anchor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor)
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#interfaces)

*   [`CSSPositionTryDescriptors`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPositionTryDescriptors)
    
*   [`CSSPositionTryRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPositionTryRule)
    
*   [`HTMLElement.anchorElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/anchorElement)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#guides)

--------------------------------------------------------------------------------------------

[Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)

An introductory guide to fundamental anchor positioning concepts, including associating, positioning, and sizing elements relative to their anchor.

[Fallback options and conditional hiding for overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)

A guide to the mechanisms CSS anchor positioning provides to prevent anchor-positioned elements from overflowing their containing elements or the viewport, including position try fallback options and conditionally hiding elements.

[Using anchored container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Anchored_container_queries)

Explains how to use anchored container queries to conditionally apply styles to anchor-positioned elements depending on what position try fallback options are active on them.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#related_concepts)

----------------------------------------------------------------------------------------------------------------

*   [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
     module:
    *   [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
        
    *   [`inset-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
        
    *   [`inset-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start)
        
    *   [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
        
    *   [`inset-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block)
        
    *   [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
        
    *   [`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
         shorthand
    *   [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
        
    *   [`min-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-block-size)
        
    *   [`min-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-inline-size)
        
    *   [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
        
    *   [`max-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-block-size)
        
    *   [`max-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-inline-size)
        
    *   [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
        
    *   [`margin-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-end)
        
    *   [`margin-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start)
        
    *   [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
        
    *   [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
        
    *   [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
        
    *   [Inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
         glossary term
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module:
    *   [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
        
    *   [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
        
    *   [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
        
    *   [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
        
*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module:
    *   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
        
    *   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
        
    *   [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
        
    *   [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
        
    *   [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
        
    *   [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
        
    *   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
        
    *   [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
        
    *   [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
        
    *   [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
        
    *   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
        
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module:
    *   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
        
    *   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
        
    *   [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
        
    *   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
        
    *   [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
        
    *   [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
        

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Anchor Positioning Module Level 1](https://drafts.csswg.org/css-anchor-position-1/) |
| [CSS Anchor Positioning Module Level 2](https://drafts.csswg.org/css-anchor-position-2/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning#see_also)

------------------------------------------------------------------------------------------------

*   [CSS scroll anchoring](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring)
     module
*   [Learn: CSS positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning)
    
*   [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
     module
*   [Learn: Sizing items in CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Sizing)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Mar 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/anchor_positioning/index.md?plain=1 "Folder: en-us/web/css/guides/anchor_positioning (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnchor_positioning&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fanchor_positioning%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnchor_positioning%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fanchor_positioning%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F879a1aece3a1d4eb28c0024f0baac6aa1b96638e%0A*+Document+last+modified%3A+2026-03-24T08%3A57%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")