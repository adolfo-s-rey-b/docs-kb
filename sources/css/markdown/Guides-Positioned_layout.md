*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#mdn-search)
    

CSS positioned layout
=====================

The **CSS positioned layout** module defines the coordinate-based positioning and offsetting schemes available in CSS and the properties used to position and stack elements on a web page. The module is best known for defining the basic positioning methods, including relative positioning, sticky positioning, absolute positioning, and fixed positioning. It also defines how positioned elements are painted and layered, clarifying stacking behavior and visual order.

The positioned layout module defines the physical, logical, and shorthand [inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
. The logical properties enable developing with internationalization and responsiveness in mind.

Like all CSS modules, this module impacts and is impacted by other modules. This module describes how positioning interacts with other layout modules such as [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 and [CSS Grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
. Other modules, such as [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
, build upon this module to enable positioning elements relative to other elements and layers.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#reference)

-------------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#properties)

*   [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
    
*   [`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
    
*   [`inset-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block)
    
*   [`inset-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
    
*   [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
    
*   [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
    
*   [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
    
*   [`inset-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start)
    
*   [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
    
*   [`overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay)
    
*   [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
    
*   [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    
*   [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    

### [Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#selectors)

*   [`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
    

### [Glossary terms and definitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#glossary_terms_and_definitions)

*   [Block direction](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values#block_direction)
    
*   [Containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
    
*   [Flow relative values](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values)
    
*   [Inline direction](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values#inline_direction)
    
*   [Inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
    
*   [Positioning context](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#positioning_contexts)
    
*   [Relative position](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#relative_positioning)
    
*   [Stacking context](https://developer.mozilla.org/en-US/docs/Glossary/Stacking_context)
    
*   [Static positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#static_positioning)
    
*   [Top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#guides)

-------------------------------------------------------------------------------------------

[Understanding z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Understanding_z-index)

Presents the notion of stacking context and explains how z-ordering works, with several examples.

[Stacking without the `z-index` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_without_z-index)

The stacking rules that apply when `z-index` is not used.

[Stacking floating elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements)

How floating elements are handled with stacking.

[Using `z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index)

How to use `z-index` to change default stacking.

[Stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)

CSS stacking context, the CSS features that create new stacking contexts, and nested stacking contexts.

[Learn: positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning)

The different position values and how to use them.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#related_concepts)

---------------------------------------------------------------------------------------------------------------

*   [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
    
*   [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)
    
*   [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
    
*   [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
    
*   [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
    
*   [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
     element
    
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module
    
    *   [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
        
    *   [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
        
    *   [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
        
    *   [`position-try-order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-order)
        
    *   [`position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
         shorthand
    *   [`position-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility)
        
*   [CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms)
     module
    
    *   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
        
    *   [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
        
    *   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
        

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Positioned Layout Module Level 3](https://drafts.csswg.org/css-position/) |
| [CSS Positioned Layout Module Level 4](https://drafts.csswg.org/css-position-4/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout#see_also)

-----------------------------------------------------------------------------------------------

*   Other CSS `*-position` properties:
    *   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
        
    *   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
        
    *   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
        
    *   [`font-synthesis-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position)
        
    *   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
        
    *   [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
        
    *   [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
        
    *   [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
        
    *   [`offset-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position)
        
    *   [`ruby-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position)
        
    *   [`text-emphasis-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position)
        
    *   [`text-underline-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position)
        
*   Position-related [data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
    *   [`<baseline-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
        
    *   [`<content-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-position)
        
    *   [`<overflow-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position)
        
    *   [`<self-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position)
        
*   [CSS Scroll Snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
    *   [Snap positions](https://developer.mozilla.org/en-US/docs/Glossary/Snap_positions)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/positioned_layout/index.md?plain=1 "Folder: en-us/web/css/guides/positioned_layout (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")