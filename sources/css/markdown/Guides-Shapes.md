*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#mdn-search)
    

CSS shapes
==========

The **CSS shapes** module describes geometric shapes. It also defines CSS properties that can use the shapes to control the geometry of an element's float area; this area can then be applied to exclusions, or specify an element's content area.

The specification defines several ways to create shapes. Content can be wrapped around or within a shape rather than following the default rectangle shape of the element's box.

Shapes define geometries that can be used as CSS values. This module provides functions for creating ellipses, polygons, and arbitrary geometries. Other CSS modules can make use of shapes defined in this specification, including [CSS motion path](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Motion_path)
 and [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
.

[CSS shapes in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#css_shapes_in_action)

------------------------------------------------------------------------------------------------------------

The example below shows an image that has been floated left, and the `shape-outside` property applied with a value of `circle(50%)`. This creates a circle shape, and the content wrapping the float now wraps around that shape. This changes the length of the wrapping text's line boxes. You can click "Play" to edit the code in the MDN Playground.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#reference)

--------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#properties)

*   [`shape-image-threshold`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold)
    
*   [`shape-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin)
    
*   [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
    

The CSS shapes module also introduces the `shape-inside` and `shape-padding` properties. Currently, no browsers support these features.

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#data_types)

*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
    

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#functions)

*   [`circle()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/circle)
    
*   [`ellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/ellipse)
    
*   [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
    
*   [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
    
*   [`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
    
*   [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
    
*   [`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)
    
*   [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
    

### [Terms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#terms)

*   [Reference box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#the_reference_box)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#guides)

--------------------------------------------------------------------------------

[Overview of shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Overview)

Defining basic shapes with the `shape-margin` and `clip-path` properties, and debugging basic shapes with Developer Tools.

[Shapes from box values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_box_values)

Using `border-radius` curvatures and CSS box model values to create shapes.

[Basic shapes with `shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside)

Creating rectangles, circles, ellipses, and polygons with CSS shapes, the reference box, and the `shape-outside` property.

[Shapes from images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_images)

Creating shapes from semi-transparent image files and CSS Gradients.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#related_concepts)

----------------------------------------------------------------------------------------------------

[CSS motion path](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Motion_path)
 module

*   [`offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset)
    
*   [`offset-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-anchor)
    
*   [`offset-distance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance)
    
*   [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
    
*   [`offset-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position)
    
*   [`offset-rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate)
    
*   [`ray()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ray)
     function

[CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
 module

*   [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/clip-rule)
    
*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
    
*   [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
    
*   [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
    

[CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
 module

*   [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
     shorthand

[CSS borders and box decorations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations)
 module

*   [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
    

[CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
 module

*   [`<box-edge>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge)
     data type

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#specifications)

------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 1](https://drafts.csswg.org/css-shapes-1/) |
| [CSS Shapes Module Level 2](https://drafts.csswg.org/css-shapes-2/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes#see_also)

------------------------------------------------------------------------------------

*   [Shape generator](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Shape_generator)
    
*   [CSS Shapes resources](https://codepen.io/KristopherVanSant/post/css-shapes-resources "External link (opens in new tab)")
    
*   [CSS Shapes 101](https://alistapart.com/article/css-shapes-101/ "External link (opens in new tab)")
     via alistapart.com (2014)
*   [Creating non-rectangular layouts with CSS Shapes](https://www.sarasoueidan.com/blog/css-shapes/ "External link (opens in new tab)")
     via sarasoueidan.com (2013)
*   [How to use CSS Shapes in your web design](https://webdesign.tutsplus.com/how-to-use-css-shapes-in-your-web-design--cms-27498t "External link (opens in new tab)")
     via tutsplus.com (2016)
*   [Edit CSS shapes with the shape path editor](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/edit_css_shapes/index.html "External link (opens in new tab)")
     via mozilla.org (2018) ([Video](https://www.youtube.com/watch?v=u9bDe3Bw0sA "External link (opens in new tab)")
    )

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/shapes/index.md?plain=1 "Folder: en-us/web/css/guides/shapes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FShapes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fshapes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FShapes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fshapes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd0970bc03cf30a9a8089954cc542a17dbe9eba3%0A*+Document+last+modified%3A+2026-07-16T09%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")