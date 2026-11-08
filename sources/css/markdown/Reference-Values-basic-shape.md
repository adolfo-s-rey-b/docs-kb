*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#mdn-search)
    

`<basic-shape>` CSS type
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<basic-shape>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a shape used in the [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
, [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
, [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
, and [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
 properties.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#try_it)

-----------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax)

-----------------------------------------------------------------------------------------------

The `<basic-shape>` data type is used to create basic shapes including rectangles by [container inset](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_rectangles_by_container_insets)
, by [coordinate distance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_rectangles_by_distance)
, or by [set dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_rectangles_with_dimensions)
, [circles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_circles)
, [ellipses](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_ellipses)
, [polygons](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_polygons)
, [paths](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_paths)
, and [author created shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_shapes)
. These basic shapes are defined using one `<basic_shape>` CSS functions, with each value requiring a parameter that follows the shape's function-specific syntax.

### [Common parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#common_parameters)

The parameters common across the syntax of some basic shape functions include:

[`round <'border-radius'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#round_border-radius)

Defines rounded corners for [rectangles by container insets](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_rectangles_by_container_insets)
, [rectangles by distance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_rectangles_by_distance)
, and [rectangles with dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_rectangles_with_dimensions)
 using the same syntax as the CSS [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 shorthand property.

[`<shape-radius>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#shape-radius)

Defines the radius for a [circle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_circles)
 or an [ellipse](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_ellipses)
. Valid values include [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, `closest-side` (the default), `farthest-side`, `closest-corner`, and `farthest-corner`. Negative values are invalid.

The `closest-side` keyword value uses the length from the center of the shape to the closest side of the reference box to create the radius length. The `farthest-side` keyword value uses the length from the center of the shape to the farthest side of the reference box. Similarly, the `closest-corner` and `farthest-corner` use the length from the center of the shape to the closest and farthest corners, respectively.

[`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#position)

Defines the center [`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
 of a [circle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_circles)
 or an [ellipse](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_ellipses)
. It defaults to `center` if omitted.

[`<fill-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#fill-rule)

Sets the [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
 that is used to determine how the interior of the shape defined by the basic shapes [polygon](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_polygons)
, [path](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_paths)
, and [shape](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_shapes)
 is to be filled. Possible values are `nonzero` (the default) and `evenodd`.

**Note:** `<fill-rule>` is not supported in [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 and using it invalidates the property.

### [Syntax for rectangles: `<basic-shape-rect>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_rectangles_basic-shape-rect)

The `<basic-shape-rect>` type, a subset of the `<basic-shape>` type, represents the basic-shape functions limited to creating rectangles, including [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
, [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
, and [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
.

The [`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
, [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
, and [`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)
 functions can also be used to create rectangles, but are not limited to only four-sided, right-angled shapes.

#### Syntax for rectangles by container insets

The [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
 function creates an inset rectangle, with its size defined by the offset distance of each of the four sides of its container and, optionally, rounded corners.

inset( <length-percentage>{1,4} \[ round <'border-radius'> \]? )

When all of the first four arguments are supplied, they represent the top, right, bottom, and left offsets from the reference box inward that define the position of the edges of the inset rectangle. These arguments follow the syntax of the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 shorthand, which lets you set all four insets with one, two, three, or four values.

If a pair of insets for a dimension adds up to more than 100% of that dimension, both values are proportionally reduced so their sum equals 100%. For example, the value `inset(90% 10% 60% 10%)` has a top inset of `90%` and a bottom inset of `60%`. These values are reduced proportionally to `inset(60% 10% 40% 10%)`. Shapes such as this, that enclose no area and have no [`shape-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin)
, do not affect wrapping.

#### Syntax for rectangles by distance

The [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
 function defines a rectangle using the specified distances from the top and left edges of the reference box, with optional rounded corners.

rect( \[ <length-percentage> | auto \]{4} \[ round <'border-radius'> \]? )

When using the `rect()` function, you do not define the width and height of the rectangle. Instead, you specify four values to create the rectangle, with its dimensions determined by the size of the reference box and the four offset values. Each value can be either a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or the keyword `auto`. The `auto` keyword is interpreted as `0%` for the top and left values and as `100%` for the bottom and right values.

#### Syntax for rectangles with dimensions

The [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
 function defines a rectangle located at the specified distances from the left (`x`) and top (`y`) edges of the reference box and sized by the specified width (`w`) and height (`h`) of the rectangle, in that order, with optional rounded corners.

xywh( <length-percentage>{2} <length-percentage \[0,∞\]>{2} \[ round <'border-radius'> \]? )

### [Syntax for circles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_circles)

The [`circle()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/circle)
 function defines a circle using a radius and a position.

circle( <shape-radius>? \[ at <position> \]? )

The `<shape-radius>` argument represents the radius of the circle defined as either a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
. A percentage value here is resolved from the used width and height of the reference box as `sqrt(width^2+height^2)/sqrt(2)`. If omitted, the radius is defined by `closest-side`.

### [Syntax for ellipses](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_ellipses)

The [`ellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/ellipse)
 function defines an ellipse using two radii and a position.

ellipse( \[ <shape-radius>{2} \]? \[ at <position> \]? )

The `<shape-radius>` arguments represent _rx_ and _ry_, the x-axis and y-axis radii of the ellipse, in that order. These values are specified as either a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
. Percentage values here are resolved against the used width (for the rx value) and the used height (for the ry value) of the reference box. If only one radius value is provided, the `ellipse()` shape function is invalid. If no value is provided, `50% 50%` is used.

### [Syntax for polygons](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_polygons)

The [`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
 function defines a polygon using a set of comma-separated coordinate pairs, optionally preceded by an SVG [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
, a corner-rounding parameter, or both.

polygon( <'fill-rule'>? \[ round <length> \]? , \[ <length-percentage> <length-percentage> \]# )

The optional first parameter can contain one or both of the following, separated by a space:

*   An SVG [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
     value, either `nonzero` or `evenodd`, specifying the algorithm used to fill the polygon shape.
*   The keyword [`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#round_length)
     followed by a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     value, separated by a space. This specifies that the polygon should have rounded corners, with the `<length>` specifying the corner radius.

Each coordinate pair consists of two space-separated `<length-percentage>` values. These values represent the x- and y-axis coordinates of a polygon vertex.

### [Syntax for paths](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_paths)

The [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
 function defines a shape using an SVG [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
 and an SVG [path definition](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d)
.

path( <'fill-rule'>? , <string> )

The required `<string>` is an [SVG path](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d)
 as a quoted string. The `path()` function is not a valid [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
 property value.

### [Syntax for shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_shapes)

The [`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)
 function defines a shape using an initial starting point and a series of shape commands.

shape( <'fill-rule'>? from <coordinate-pair> , <shape-command># )

The `from <coordinate-pair>` parameter represents the starting point for the first shape command, and `<shape-command>` defines one or more shape commands, which are similar to the [SVG path commands](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#path_commands)
. The `shape()` function is not a valid [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
 property value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#description)

---------------------------------------------------------------------------------------------------------

When creating a shape, the reference box is defined by the property that uses `<basic-shape>` values. The coordinate system for the shape has its origin at the top-left corner of the element's margin box by default, with the x-axis running to the right and the y-axis running downwards. All the lengths expressed in percentages are resolved from the dimensions of the reference box.

The default reference box is the [`margin-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#margin-box)
, as demonstrated in the image below. The image shows a circle created using `shape-outside: circle(50%)`, highlighting the different parts of the box model as seen in a browser's Developer Tools. The shape here is defined with reference to the margin-box.

![An image showing a circle inspected with the Firefox DevTools Shape Inspector. The different parts of the box model are highlighted.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shapes-reference-box.png)

### [Computed values of basic shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#computed_values_of_basic_shapes)

The values in a `<basic-shape>` function are computed as specified, with the following additional considerations:

*   For any omitted values, their defaults are used.
*   A [`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
     value in `circle()` or `ellipse()` is computed as a pair of offsets from the top left corner of the reference box: the first offset is horizontal, and the second is vertical. Each offset is specified as a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
     value.
*   A [`<border-radius>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
     value in `inset()` is expanded into a list of eight values, each either a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    .
*   [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
    , [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
    , and [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
     functions compute to the equivalent `inset()` function.

### [Interpolation of basic shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#interpolation_of_basic_shapes)

When animating between two `<basic-shape>` functions, the [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 rules listed below are followed. The parameter values of each `<basic-shape>` function form a list. For interpolation to occur between two shapes, both shapes must use the same reference box and the number and type of values in both `<basic-shape>` lists must match.

Each value in the lists of the two `<basic-shape>` functions is interpolated based on its computed value as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, or [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 where possible. Interpolation can still occur if the values are not one of those data types but are identical between the two interpolating basic shape functions, such as `nonzero`.

*   **Both shapes are of type `ellipse()` or type `circle()`**: Interpolation is applied between each corresponding value if their radii are specified as either a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
     (rather than keywords such as `closest-side` or `farthest-side`).
    
*   **Both shapes are of type `inset()`**: Interpolation is applied between each corresponding value.
    
*   **Both shapes are of type `polygon()`**: Interpolation is applied between each corresponding value if they use the same `<fill-rule>` and have the same number of comma-separated coordinate pairs.
    
*   **Both shapes are of type `path()`**: Interpolation is applied to each parameter as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
     if the path strings in both the shapes match the number, type, and sequence of [path data commands](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#path_commands)
    .
    
*   **Both shapes are of type `shape()`**: Interpolation is applied between each corresponding value if they have the identical command keyword and use the same `<by-to>` keyword. If `shape()` is used in the [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
     property, the two shapes interpolate if they also have the same `<fill-rule>`.
    
    *   If they use the `<curve-command>` or the `<smooth-command>`, the number of control points must match for interpolation.
        
    *   If they use the `<arc-command>` with different `<arc-sweep>` directions, the interpolated result goes clockwise (`cw`). If they use different `<arc-size>` keywords, the size is interpolated using the `large` value.
        
*   **One shape is of type `path()` and the other is of type `shape()`**: Interpolation is applied between each corresponding value if the list of path data commands is identical in number as well as sequence. The interpolated shape is a `shape()` function, maintaining the same list of path data commands.
    

In all other cases, no interpolation occurs and the animation is discrete.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#examples)

---------------------------------------------------------------------------------------------------

### [Animated polygon](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#animated_polygon)

In this example, we use the [@keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 at-rule to animate a clip path between two polygons. Note that both polygons have the same number of vertices, which is necessary for this type of animation to work.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 1  <br>\# basic-shape-functions](https://drafts.csswg.org/css-shapes/#basic-shape-functions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#see_also)

---------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
    , [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    , [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
    , [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
    
*   SVG shape elements: [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
    , [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)
    , [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)
    , [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)
    , [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)
    , [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
    
*   [Overview of CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Overview)
    
*   [CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
     module
*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module
*   [Edit shape paths in Firefox developer tools](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/edit_css_shapes/index.html "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/basic-shape/index.md?plain=1 "Folder: en-us/web/css/reference/values/basic-shape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2e0b9415ed31484a4830e214eff9e06e408c7261%0A*+Document+last+modified%3A+2026-09-22T00%3A07%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")