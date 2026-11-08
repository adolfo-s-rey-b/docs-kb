*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#mdn-search)
    

CSS box sizing
==============

The **CSS box sizing** module enables you to specify how elements fit their content or fit into a particular layout context. It defines sizing, minimum sizing, and maximum sizing properties, and also extends the CSS sizing properties with keywords that represent content-based [intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
 and context-based [extrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Extrinsic_size)
.

Elements can either be extrinsically or intrinsically sized. The [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
 defines page-relative properties to explicitly, or "extrinsically" set an element's size, including `width`, `height`, `padding`, and `margin` properties (along with `border` properties defined in the [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
 module). This CSS box sizing module extends the CSS box model module to enable an element to be sized intrinsically — setting element size based on the size of its content.

The sizing values introduced in this module allow elements with [size containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#size_containment)
 to take explicit intrinsic sizes, as if their in-flow content's width and height match the specified explicit intrinsic size, rather than being sized as if they were empty.

This module also introduced the ability to define an aspect ratio for an element's box, meaning the browser can automatically adjust an element's dimensions to maintain a specified aspect ratio as long as one of the dimensions is automatically sized.

The [logical properties and values module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
 expanded the properties available in the box model and box sizing modules to include writing-mode-relative equivalents of the corresponding physical box model and intrinsic box sizing properties.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#reference)

------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#properties)

*   [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
    
*   [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
    
*   [`contain-intrinsic-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-block-size)
    
*   [`contain-intrinsic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)
    
*   [`contain-intrinsic-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size)
    
*   [`contain-intrinsic-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
    
*   [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)
    
*   [`frame-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing)
    
*   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    
*   [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
    
*   [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
    
*   [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
    
*   [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
    
*   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    

The CSS box sizing module also introduces the `min-intrinsic-sizing` property. Currently, no browsers support this feature.

### [Data types and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#data_types_and_values)

*   [`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
     data type
*   [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
     value
*   [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
     value
*   [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
     value

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#functions)

*   [`fit-content()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)
    

### [Glossary terms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#glossary_terms)

*   [Intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
    
*   [Extrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Extrinsic_size)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#guides)

------------------------------------------------------------------------------------

[Understanding aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)

Learn about the `aspect-ratio` property, discuss aspect ratios for replaced and non-replaced elements, and examine some common aspect ratio use cases.

[Introduction to the CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)

Explains one of the fundamental concepts of CSS: the box model. This model defines how CSS lays out elements, including their content, padding, border, and margin areas.

[Mastering margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)

Sometimes, two adjacent margins are collapsed into one. This article describes the rules that govern when and why this happens, and how to control it.

[Visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)

Explains the visual formatting model.

[Controlling ratios of flex items along the main axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Controlling_flex_item_ratios)

Explains intrinsic sizing as a precursor to understanding how to control the size and flexibility of flex items along the main axis using [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
, [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
, and [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#related_concepts)

--------------------------------------------------------------------------------------------------------

*   [CSS logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
     module
    *   [`min-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-inline-size)
        
    *   [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
        
    *   [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
        
    *   [`max-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-block-size)
        
    *   [`max-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-inline-size)
        
    *   [`min-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-block-size)
        
    *   [`min-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-inline-size)
        
    *   [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
        
    *   [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
        
    *   [`padding-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block)
        
    *   [`padding-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline)
        
    *   [`border-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block)
        
    *   [`border-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline)
        
    *   [`contain-intrinsic-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-block-size)
        
    *   [`contain-intrinsic-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size)
        
    *   [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
        
    *   [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
        
    *   [`overscroll-behavior-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-block)
        
    *   [`overscroll-behavior-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline)
        
*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module
    *   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
         shorthand
    *   [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
        
    *   [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
        
    *   [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
        
    *   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
        
    *   [`margin-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim)
        
    *   [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
         shorthand
    *   [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)
        
    *   [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
        
    *   [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)
        
    *   [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
        
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
    *   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
         shorthand
    *   [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
         shorthand
    *   [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)
        
    *   [`border-left-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-width)
        
    *   [`border-right-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-width)
        
    *   [`border-top-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)
        
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
    *   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
         shorthand
    *   [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
        
    *   [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
        
    *   [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
        
    *   [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
        
    *   [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
        
    *   [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
        
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module
    *   [`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid)
        
    *   [`grid-auto-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-columns)
        
    *   [`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
        
    *   [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
        
    *   [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
        
    *   [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
        
    *   [`minmax()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)
         function
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module
    *   [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
        
    *   [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
        

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#specifications)

----------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 4](https://drafts.csswg.org/css-sizing-4/) |
| [CSS Box Sizing Module Level 3](https://drafts.csswg.org/css-sizing-3/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing#see_also)

----------------------------------------------------------------------------------------

*   [CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
     module
*   [CSS flex layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module
*   [CSS fragmentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/box_sizing/index.md?plain=1 "Folder: en-us/web/css/guides/box_sizing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_sizing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbox_sizing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_sizing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbox_sizing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F04c41175b160dc00b1a1b8e4e13b2183d89fdf1a%0A*+Document+last+modified%3A+2026-07-17T07%3A28%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")