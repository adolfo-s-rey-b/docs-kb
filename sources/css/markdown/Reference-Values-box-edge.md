*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#mdn-search)
    

`<box-edge>` CSS type
=====================

The **`<box-edge>`** value types represent a [box edge](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
 keyword, such as [`content-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#content-box)
 and [`border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#border-box)
. The box-edge keywords are used to define different aspects of an element's box model and how elements are positioned and rendered on screen.

The box-edge keywords are the components of, but not limited to, the data types `<visual-box>`, `<layout-box>`, `<paint-box>`, `<coord-box>`, and `<geometry-box>`. These types are applied to properties such as [`transform-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box)
 and [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#syntax)

--------------------------------------------------------------------------------------------

<visual-box> = content-box | padding-box | border-box /\* the three <box> values \*/
<layout-box> or <shape-box> = <visual-box> | margin-box
<paint-box> = <visual-box> | fill-box | stroke-box
<coord-box> = <paint-box> | fill-box | stroke-box | view-box
<geometry-box> = <shape-box> | fill-box | stroke-box | view-box

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#values)

A `<box-edge>` can be of the type `<visual-box>`, `<layout-box>`, `<paint-box>`, `<coord-box>`, or `<geometry-box>`.

[`<visual-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#visual-box)

Refers to the rectangular box generated for an element as seen by a user on a web page. It includes the element's content, padding, and border. Also referred to as `<box>`, this value excludes the margin area. This value type is used for the [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
 and [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
 properties.

[`<layout-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#layout-box)

Refers to the space occupied by an element, including its content, padding, border, and margin. This value type is used for layout and positioning purposes. Also referred to as `<shape-box>`, this value type is used for the [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
 property.

[`<paint-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#paint-box)

Refers to the area within the layout box that is used to visually render the content. This includes the area where the element's background and borders are painted. As an element's paintable area does not include its margins, this value excludes `margin-box`.

[`<coord-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#coord-box)

Refers to the coordinate box used for positioning and sizing an element within its parent container. It is used to control how content flows around the edges of the box. It excludes the margin area. This value type is used for the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 property.

[`<geometry-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#geometry-box)

Defines the reference box for a [basic shape](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
, or if specified by itself, causes the edges of the specified box, including any corner shaping (such as a [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
), to be the clipping path. This value type is used for the [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
, [`mask-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip)
, and [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
 properties and the SVG [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/clip-path)
 attribute; it is also used as part of the [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
 property values.

### [Keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#keywords)

The `<box-edge>` keywords are defined as follows:

[`content-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#content-box)

Refers to the outer edge of the box's content area. The content box is the innermost box. The content area contains the actual content, such as text, images, or other HTML elements. In SVG, this value is treated as `fill-box`.

[`padding-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#padding-box)

Refers to the outer edge of the padding of the box. If there is no padding on a side, then the value is the same as `content-box`. In SVG, `padding-box` is treated as `fill-box`. The padding area surrounds the content area, starting at the outer edge of the content box.

[`border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#border-box)

Refers to the outer edge of the border of the box. If there is no border on a side, then the value is the same as `padding-box`. In SVG, `border-box` is treated as `stroke-box`. The border area surrounds the padding area, starting at the outer edge of the padding box.

[`half-border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#half-border-box)

Refers to a box shape that traverses the center of the border region; the inner half of the border region is inside the shape, and the outer half of the border region is outside the shape.

[`margin-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#margin-box)

Refers to the outer edge of the margin of the box. If there is no margin on a side, then the value is the same as `border-box`. In SVG, `margin-box` is treated as `stroke-box`.

[`fill-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#fill-box)

Refers to the object bounding box in SVG. In CSS, `fill-box` is treated as `content-box`. It is used to wrap the content around the edges defined by the `coord-box` values.

[`stroke-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#stroke-box)

Refers to the stroke bounding box in SVG. In CSS, `stroke-box` is treated as `border-box`. It is used to define the shape of the element when strokes are applied.

[`view-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#view-box)

Refers to the nearest SVG viewport element's origin box. The origin box is a rectangle with the width and height of the initial SVG user coordinate system established by the [`viewBox`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)
 attribute for that element. The origin box is positioned such that its top left corner is anchored at the [coordinate system](https://developer.mozilla.org/en-US/docs/Web/API/CSSOM_view_API/Coordinate_systems)
 origin. In CSS, `view-box` is treated as `border-box`.

**Note:** When the SVG viewport is not anchored at the origin, the origin box does not correspond to the SVG viewport.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Model Module Level 4  <br>\# keywords](https://drafts.csswg.org/css-box-4/#keywords) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#see_also)

------------------------------------------------------------------------------------------------

*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/box-edge/index.md?plain=1 "Folder: en-us/web/css/reference/values/box-edge (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbox-edge&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbox-edge%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbox-edge%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbox-edge%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd0970bc03cf30a9a8089954cc542a17dbe9eba3%0A*+Document+last+modified%3A+2026-07-16T09%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")