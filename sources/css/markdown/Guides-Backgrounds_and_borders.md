*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#mdn-search)
    

CSS backgrounds and borders
===========================

The **CSS backgrounds and borders** module provides properties for adding backgrounds, borders, rounded corners, and box shadows to elements.

You can add different types of border styles, including borders made of images of any image type, from raster images to CSS gradients. Borders can be square or rounded, and a different radius can be set for each corner. Elements can be rounded whether or not they have a visible border.

Box shadows include inset and outset shadow, single or multiple shadows, and solid or allowed to fade to transparent. An outer box-shadow casts a shadow as if the border-box of the element were opaque. An inner box-shadow casts a shadow as if everything outside the padding edge were opaque. The shadow can be solid or include a spread distance with the shadow color transitioning to transparent.

The properties in this module also let you define whether cells inside a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 should have shared or separate borders.

[Backgrounds, borders, and box shadows in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#backgrounds_borders_and_box_shadows_in_action)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This sample of borders, backgrounds, and box shadows consists of centered background images made of linear and radial gradients. A series of box shadows make the border appear to "pop". The element on the left has a border image set. The element on the right has a rounded dotted border.

The background images are defined with [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
. The images are centered with [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
. Different values of the [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
 property for the multiple background images are used to make the background images stay within the content box. The background color gets clipped to the padding box preventing the background from appearing through the transparent sections for the [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
 and the [`dotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
. The rounded corners in the element on the right are created using the [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 property. A single [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 declaration is used to set all the shadows, both inset and outset.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#reference)

-------------------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#properties)

*   [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
    
*   [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    
*   [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    
*   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
    
*   [`background-repeat-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x)
    
*   [`background-repeat-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y)
    
*   [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
     shorthand
*   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
     shorthand
*   [`background-position-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x)
    
*   [`background-position-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-y)
    
*   [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
    
*   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
    
*   [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)
    
*   [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
     shorthand
*   [`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color)
    
*   [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)
    
*   [`border-left-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-width)
    
*   [`border-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left)
     shorthand
*   [`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color)
    
*   [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)
    
*   [`border-right-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-width)
    
*   [`border-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right)
     shorthand
*   [`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
    
*   [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
    
*   [`border-top-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)
    
*   [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
     shorthand
*   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
     shorthand
*   [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
     shorthand
*   [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
     shorthand
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
     shorthand
*   [`border-bottom-left-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-left-radius)
    
*   [`border-bottom-right-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-right-radius)
    
*   [`border-top-left-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-left-radius)
    
*   [`border-top-right-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius)
    
*   [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
     shorthand
*   [`border-image-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
    
*   [`border-image-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
    
*   [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
    
*   [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
    
*   [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)
    
*   [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
     shorthand
*   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    

The CSS backgrounds module level 4 also introduces the `background-position-block`, `background-position-inline`, `background-repeat-block`, `background-repeat-inline`, and `background-tbd` properties. Currently, no browsers support these features.

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#data_types)

*   [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
     enumerated type

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#guides)

-------------------------------------------------------------------------------------------------

[Using multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)

Setting one or more backgrounds on an element.

[Resizing background images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images)

Changing the size and repeating behavior of background images.

[Scaling SVG backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds)

How SVG aspect ratio, SVG dimension values, and the CSS `background-size` property impact the scaling of SVG background images.

[Using CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)

Creating CSS gradients and using them as background images.

[Learn CSS: background and borders](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Backgrounds_and_borders)

Learn how to implement decorative images using CSS background images.

[Learn CSS: the box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)

Learn how borders and other box model properties impact the CSS box model.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#related_concepts)

---------------------------------------------------------------------------------------------------------------------

*   [`border-block-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-color)
    
*   [`border-block-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-color)
    
*   [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)
    
*   [`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)
    
*   [`border-block-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style)
    
*   [`border-block-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-style)
    
*   [`border-inline-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-style)
    
*   [`border-inline-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-style)
    
*   [`border-block-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-width)
    
*   [`border-block-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-width)
    
*   [`border-inline-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width)
    
*   [`border-inline-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-width)
    
*   [`border-start-start-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius)
    
*   [`border-start-end-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-end-radius)
    
*   [`border-end-start-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-end-start-radius)
    
*   [`border-end-end-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-end-end-radius)
    
*   [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
    
*   [`box-decoration-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
    
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    
*   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     data type
*   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     data type
*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
     data type
*   [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
     data type
*   [`currentColor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#currentcolor_keyword)
     keyword

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3](https://drafts.csswg.org/css-backgrounds/) |
| [CSS Backgrounds Module Level 4](https://drafts.csswg.org/css-backgrounds-4/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders#see_also)

-----------------------------------------------------------------------------------------------------

*   [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
    
*   [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
    
*   [`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
     filter function
*   [Applying color to HTML elements using CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color)
    
*   Tools:
    *   [Border-image generator](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Border-image_generator)
        
    *   [Border-radius generator](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Border-radius_generator)
        
    *   [Box-shadow generator](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Box-shadow_generator)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/backgrounds_and_borders/index.md?plain=1 "Folder: en-us/web/css/guides/backgrounds_and_borders (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBackgrounds_and_borders&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbackgrounds_and_borders%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBackgrounds_and_borders%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbackgrounds_and_borders%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff9761309e0fe3f22822e63903439d8d6130b535f%0A*+Document+last+modified%3A+2026-02-05T14%3A00%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")