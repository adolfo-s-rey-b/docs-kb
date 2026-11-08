*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#mdn-search)
    

CSS masking
===========

The **CSS masking** module defines masking and clipping, two different graphical operations that are used to partially or fully hide portions of visual elements.

**Clipping** involves defining a closed vector path, shape, or polygon as a **clipping path**. Everything inside the clipping path region remains visible while everything outside is hidden, or "clipped out". The [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 property specifies a [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 or references an SVG [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
 element to be used as a clipping path.

CSS **masking** properties are used to apply a mask to an element or its border. A graphical object is then painted onto the background or border, completely or partially masking out parts of the element or its border, depending on the opacity or luminance of the mask.

The image used as the mask is specified by the [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 or [`mask-border-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-source)
 properties. The specified mask can be an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
, a [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
, or an SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 element. The mask can be sized and positioned similarly to [background and border images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
.

Clipping and masking in CSS behaves the same way as it does with SVG: First, the element is styled without filter effects, masking, clipping, and opacity. Then, any effects are applied to the element in the following order: [filter effects](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Filter_effects)
, clipping, masking, and opacity.

While masking provides more control and options, clipping can perform better if a basic shape is all that's required — they are easier to interpolate.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#reference)

---------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#properties)

*   [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
    
*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
     shorthand
*   [`mask-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip)
    
*   [`mask-composite`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite)
    
*   [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    
*   [`mask-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
    
*   [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
    
*   [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
    
*   [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
    
*   [`mask-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
    
*   [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
    
*   [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
     shorthand
*   [`mask-border-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset)
    
*   [`mask-border-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-repeat)
    
*   [`mask-border-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-slice)
    
*   [`mask-border-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-source)
    
*   [`mask-border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-width)
    
*   [`mask-border-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-mode)
    

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#data_types)

*   [`<geometry-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#geometry-box)
    

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#functions)

*   [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
     function

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#interfaces)

*   [`SVGClipPathElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGClipPathElement)
    
*   [`SVGMaskElement`](https://developer.mozilla.org/en-US/docs/Web/API/SVGMaskElement)
    *   [`SVGMaskElement.maskContentUnits`](https://developer.mozilla.org/en-US/docs/Web/API/SVGMaskElement/maskContentUnits)
        

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#guides)

---------------------------------------------------------------------------------

[Introduction to CSS clipping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping)

Introduction to clipping in CSS, including the `clip-path` property with examples.

[Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)

Introduction to masking in CSS, the various mask image types, and the effects of luminance and alpha-transparency in masking.

[Declaring multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks)

Introduction to mask layers and how to declare multiple mask images.

[CSS mask properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)

An exploration of CSS masking and the `mask` shorthand component properties, with explanations and examples.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#related_concepts)

-----------------------------------------------------------------------------------------------------

*   [`<coord-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#values)
    
*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
    
*   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
    
    *   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
         shorthand
    *   [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
        
    *   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
        
    *   [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
        
    *   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
        
    *   [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
         shorthand
    *   [`border-image-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
        
    *   [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
        
    *   [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
        
    *   [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)
        
    *   [`<repeat-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#values)
         data type
*   [CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
     module
    
    *   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
         data type
    *   [`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
         function
    *   [`<shape-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside#shape-box)
         data type

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#specifications)

-------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1](https://drafts.csswg.org/css-masking-1/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking#see_also)

-------------------------------------------------------------------------------------

*   [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    
*   [CSS filter effects](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Filter_effects)
     module
*   [SVG tutorial: clipping and masking](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Clipping_and_masking)
    
*   [`CanvasRenderingContext2D.clip()`](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/clip)
    
*   [`WebGLRenderingContext.colorMask()`](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/colorMask)
    
*   [PWA icon masking](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Define_app_icons#support_masking)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Mar 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/masking/index.md?plain=1 "Folder: en-us/web/css/guides/masking (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMasking&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmasking%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMasking%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmasking%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd35e3fd4bc6b80049899b45d74ed71dc996adfc7%0A*+Document+last+modified%3A+2026-03-17T20%3A48%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")