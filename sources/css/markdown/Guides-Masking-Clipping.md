*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#mdn-search)
    

Introduction to CSS clipping
============================

CSS clipping enables you to define visible portions of an element while hiding other parts, effectively "clipping" its content within a specific shape or area. With clipping, elements aren't limited to being rendered as rectangles and can be designed in visually engaging ways. This guide explores the [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 property along with some examples.

[CSS clipping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#css_clipping)

------------------------------------------------------------------------------------------------------

Clipping is a CSS technique used to clip (hide) sections of an element, displaying only the area of the element located within a developer-defined path. Clips areas are created by vector paths; anything in the path is visible while areas outside the path are hidden.

### [The `clip-path` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#the_clip-path_property)

The `clip-path` property applies clipping. The value it accepts is a vector path defining the area of the element that should remain visible. The path can be defined using boxes, a reference to an [SVG `<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#svg_as_source)
, or CSS [shapes and paths](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#shape_function)
. In the following example, we clip a blue square [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
, creating a diamond, using the [`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
 function as the clipping path:

With the `clip-path` property, you can make complex shapes by clipping an element to a `<basic-shape>` or to an [SVG source](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#svg_as_source)
. You can [animate and transition `clip-path` shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#animation)
 if the declared states have the same number of vector points.

### [Values of the `clip-path` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#values_of_the_clip-path_property)

To visually clip an element, the `clip-path` property is set to either a [`<geometry-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#geometry-box)
, a [`url`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 to a [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
 clip source, or a [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 created with [shape function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#shape_functions)
.

### [Geometry boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#geometry_boxes)

The `clip-path` hides everything outside of the clipped region. The most basic clipping is done via a geometry box. You can clip an element based on its margin, border, padding, or content. The effects of these visual box values can be achieved via other CSS properties, such as setting the [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
 to transparent and the [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
 to the desired visual box. We're looking at these values mostly because these values are used in conjunction with the shape functions, which we'll look at later, to define the origin of the shape clip path.

[Understanding the reference box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#the_reference_box)
 used by CSS shapes is important when using `clip-path`, especially with [basic shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#clipping_to_basic_shapes)
, as the reference box defines a shape's coordinate system.

#### Visual box values

This live example demonstrates the `clip-path` property's different visual box values on an element, while comparing it to the CSS `background-origin` property. We've applied a [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
, a [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, a [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
, and [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 to the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
. Select a radio button to update the `--value` to a different `<geometry-box>` value, which updates the [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
 and the [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 resolved values.

When a `<geometry>` box is specified in combination with a `<basic-shape>`, the value defines the reference box for the basic shape. If specified by itself, it causes the edges of the specified box, including any corner shaping (such as a `border-radius`), to be the clipping path.

#### Shape origin

The previous example may make you think that the `<geometry-box>` values are useless, as you can use `background-origin` instead. And you can. But when clipping using basic shapes, the `<geometry-box>`, when included along with a `<basic-shape>` as the `clip-path` value, defines the reference box for, or origin of, that shape. We can combine the two previous examples to demonstrate this.

For another example, see [`clip-path` shapes and geometry boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#shapes_and_geometry_boxes)
.

Even values like `clip-path: margin-box` can be useful. In addition to creative visuals made by placing the clip-path's edge at the margin-box edge, any computed value for `clip-path`, other than `none`, results in the creation of a new [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
 the same way that CSS [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 does for values other than `1`.

[Clipping to basic shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#clipping_to_basic_shapes)

------------------------------------------------------------------------------------------------------------------------------

The `clip-path` property's support of [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 values provides a powerful way to shape elements. The various shape function enable defining precise clipping regions, effectively sculpting elements into unique forms. The basic shape functions, include:

*   [`circle()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/circle)
    
*   [`ellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/ellipse)
    
*   [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
    
*   [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
    
*   [`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
    
*   [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
    
*   [`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)
    
*   [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
    

The size and position of these shapes are defined by the `<geometry-box>` value, which defaults to border-box being used as the reference box if the `clip-path` value includes a shape without the `<geometry-box>` component value.

Some of these functions appear to only provide basic predefined clipping options. They may appear to replicate effects you can create with [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
, but if you [toggled the `border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#visual_box_values)
 property in the previous example, you may have noticed the power of CSS clipping. Shapes provide even more control. For example, `inset()` enables clipping a rectangle with precise margins. The real power and control comes with `path()`, `shape()`, and even `polygon()`, which allows for custom multi-point shapes.

### [Creating polygons](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#creating_polygons)

With `polygon()`, by defining pairs of coordinates, each of which represents a vertex of the shape. you can create intricate forms like stars or abstract figures. The coordinates define vector points connected by straight lines.

Here we use the `polygon()` function to create a star:

### [Animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#animation)

Clipped shapes can be animated and transitioned by declaring the same number of vector points for the different states.

### [The `path()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#the_path_function)

The `path()` function enables drawing shapes using SVG commands. The function accepts the equivalent of the SVG [`d`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d)
 attribute as the function's parameter.

The star from the previous example can be created using `path()`:

### [Curved lines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#curved_lines)

With `path()`, we are not limited to straight lines. In this example, we use the `path()` function to create a heart:

### [SVG as source](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#svg_as_source)

Instead of passing an SVG [`d`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d)
 attribute string as the `path()` function argument, the value of the `clip-path` property can reference the SVG [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
 element directly.

The `id` of the `<clipPath>` is the parameter of the [`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_function)
 function.

### [Shape function](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#shape_function)

The SVG path syntax is not the most intuitive. For this reason, CSS also offers a `shape()` function. The `shape()` function also takes path drawing directive, but with a syntax that is more human readable. We can recreate the heart with more declarative CSS:

The `shape()` function is more robust in that it accepts CSS values and units (`path()` is limited to coordinates), including using CSS math functions like `calc()`. By using variables, we can create shapes (and boxes) of many different sizes:

### [Wrapping text around your clipped shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#wrapping_text_around_your_clipped_shapes)

Clipped elements are still rectangular boxed. Clipping means your element doesn't look like a box; but it is still a box. To wrap inline content around the non-rectangular (or rectangular) shapes you define, use the [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
 property. By default, inline content wraps around its margin box; `shape-outside` provides a way to customize this wrapping, making it possible to wrap text around the elements you've clipped, following the clip path you replicated rather than the element's rectangular box.

The content includes two elements to be clipped and the content that will be shaped around them.

In addition to applying the same shape for both the `clip-shape` and `shape-outside` properties, the clipped element has to be floated so that the clipped element is on the same line as the content.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping#see_also)

----------------------------------------------------------------------------------------------

*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
    
*   [`shape-image-threshold`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold)
    
*   [`shape-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin)
    
*   [Overview of shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Overview)
    
*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS `mask` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
    
*   [Declaring multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module
*   [CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/masking/clipping/index.md?plain=1 "Folder: en-us/web/css/guides/masking/clipping (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMasking%2FClipping&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmasking%2Fclipping%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMasking%2FClipping%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmasking%2Fclipping%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdb443a6062d0e858a62af2f9a3a7558335ffd2dd%0A*+Document+last+modified%3A+2026-08-28T20%3A15%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")