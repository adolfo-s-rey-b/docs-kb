*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#mdn-search)
    

`y` CSS property
================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`y`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the y-axis coordinate of the top left corner of the SVG [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 shape, [`<image>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/image)
 image, [`<foreignObject>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/foreignObject)
 viewport and nested [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
 viewport relative to the nearest `<svg>` ancestor's user [coordinate system](https://developer.mozilla.org/en-US/docs/Web/API/CSSOM_view_API/Coordinate_systems)
. If present, it overrides the element's [`y`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/y)
 attribute.

**Note:** The `y` property only applies to [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
, [`<image>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/image)
, [`<foreignObject>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/foreignObject)
, and [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
 elements nested in an `<svg>`. It has no effect on outermost `<svg>` elements and does not apply to other SVG elements nor to HTML elements or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#syntax)

-----------------------------------------------------------------------------------------

css

    /* length and percentage values */
    y: 10px;
    y: 10%;
    
    /* Global values */
    y: inherit;
    y: initial;
    y: revert;
    y: revert-layer;
    y: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#values)

The [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 and [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values denote the y-axis coordinate position of the top left corner of the SVG element.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

As an absolute or relative length, it can be expressed in any unit allowed by the CSS [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 data type.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Percentages refer to the height of the SVG [`viewBox`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)
, if declared, otherwise, the percentage refers to the height of the current SVG viewport.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#formal_definition)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)<br>, [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)<br>, [`<image>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/image)<br>, and [`<foreignObject>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/foreignObject)<br> elements in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the height of the current SVG viewport |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#formal_syntax)

-------------------------------------------------------------------------------------------------------

y =   
  <length-percentage>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#examples)

---------------------------------------------------------------------------------------------

### [Defining the y-axis coordinates of SVG shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#defining_the_y-axis_coordinates_of_svg_shapes)

This example demonstrates the basic use case of `y`, and how the CSS `y` property takes precedence over the `y` attribute.

#### HTML

We include four identical SVG `<rect>` elements; their [`x`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/x)
 and `y` attributes values are all `10`, meaning the four rectangles are all in the same location, `10px` from the top and left corner of the SVG viewport.

html

    <svg>
      <rect width="40" height="40" x="10" y="10" />
      <rect width="40" height="40" x="10" y="10" />
      <rect width="40" height="40" x="10" y="10" />
      <rect width="40" height="40" x="10" y="10" />
    </svg>
    

#### CSS

We style all the rectangles to have a black border and be slightly transparent, so overlapping rectangles are visible. We provide the rectangle with different [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
 and `y` values.

css

    svg {
      border: 1px solid;
    }
    
    rect {
      fill: none;
      stroke: black;
      opacity: 0.8;
    }
    
    rect:nth-of-type(2) {
      y: -20px;
      fill: red;
    }
    
    rect:nth-of-type(3) {
      y: 4em;
      fill: yellow;
    }
    
    rect:nth-of-type(4) {
      y: 60%;
      fill: orange;
    }
    

#### Results

The top edges of the rectangles are at `10` (from the attribute), `-20px`, `4em`, and `60%`, respectively. The rectangle is `40px` tall, so the `-20px` places half the red rectangle outside the viewport. The SVG is `150px` tall, so the orange rectangle's top side is `90px` from the top of the SVG viewport.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# Y](https://w3c.github.io/svgwg/svg2-draft/geometry.html#Y) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y#see_also)

---------------------------------------------------------------------------------------------

*   SVG [`y`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/y)
     attribute
*   Geometry properties: `y`, [`cx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cx)
    , [`cy`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy)
    , [`r`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r)
    , [`rx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx)
    , [`ry`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ry)
    , [`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/x)
    , [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    , [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    
*   [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    
*   [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    
*   [`paint-order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order)
    
*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
     data type

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/y/index.md?plain=1 "Folder: en-us/web/css/reference/properties/y (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fy&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fy%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fy%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fy%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")