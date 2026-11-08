*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#mdn-search)
    

`rx` CSS property
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2024.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`rx`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the x-axis, or horizontal, radius of an SVG [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)
 and the horizontal curve of the corners of an SVG [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 rectangle. If present, it overrides the shape's [`rx`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/rx)
 attribute.

**Note:** The `rx` property only applies to [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)
 and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG elements or HTML elements or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#syntax)

------------------------------------------------------------------------------------------

css

    /* Initial value */
    rx: auto;
    
    /* Length and percentage values */
    rx: 20px;
    rx: 20%;
    
    /* Global values */
    rx: inherit;
    rx: initial;
    rx: revert;
    rx: revert-layer;
    rx: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#values)

The [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or `auto` keyword value denotes the horizontal radius of ellipses and the horizontal border-radius of rectangles.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Absolute or relative lengths can be expressed in any unit allowed by the CSS [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 data type. Negative values are invalid.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Percentages refer to the width of the current SVG viewport. The used value for a `<rect>` is never more than 50% of the width of the rectangle.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#auto)

When set or defaulting to `auto`, the `rx` value equals the absolute length value used for [`ry`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ry)
. If both `rx` and `ry` have a computed value of `auto`, the used value is `0`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#formal_definition)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)<br> and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)<br> elements in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the width of the current SVG viewport |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#formal_syntax)

--------------------------------------------------------------------------------------------------------

rx =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto                   
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#examples)

----------------------------------------------------------------------------------------------

### [Creating rounded corners](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#creating_rounded_corners)

This example demonstrates creating rectangles with rounded corners by applying the `rx` property to SVG `<rect>` elements.

#### HTML

We include an SVG image with five `<rect>` elements; all the rectangles are the same except for their [`x`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/x)
 attribute value, which positions them along the x-axis.

html

    <svg xmlns="http://www.w3.org/2000/svg">
      <rect width="50" height="120" y="5" x="5" />
      <rect width="50" height="120" y="5" x="60" />
      <rect width="50" height="120" y="5" x="115" />
      <rect width="50" height="120" y="5" x="170" />
      <rect width="50" height="120" y="5" x="225" />
    </svg>
    

#### CSS

With CSS, we set an `rx` value on four of the rectangles:

css

    svg {
      border: 1px solid;
    }
    
    rect:nth-of-type(2) {
      rx: 10px;
      fill: red;
    }
    
    rect:nth-of-type(3) {
      rx: 2em;
      fill: blue;
    }
    
    rect:nth-of-type(4) {
      rx: 5%;
      fill: orange;
    }
    
    rect:nth-of-type(5) {
      rx: 80%;
      fill: green;
    }
    

#### Results

The first rectangle defaults to `auto`; as all the `ry` values in this example also default to `auto`, the used value of `rx` is `0`. The red and blue rectangles have `10px` and `2em` rounded corners, respectively. As the SVG viewport defaults to 300px by 150px, the orange rectangle's `5%` value creates a `15px` radius. The green rectangle has `rx: 80%` set. However, as the value of `rx` is never more than `50%` of the width of the rectangle, the effect is as if `rx: 50%; ry: 50%` was set.

### [Defining the horizontal radius of an ellipse](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#defining_the_horizontal_radius_of_an_ellipse)

This basic `<ellipse>` example demonstrates the CSS `rx` property taking precedence over an SVG `rx` attribute to define the shape's horizontal radius.

#### HTML

We include two identical `<ellipse>` elements in an SVG; each with the `rx` attribute set to `20`.

html

    <svg xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="80" cy="50" rx="20" ry="40" />
      <ellipse cx="80" cy="50" rx="20" ry="40" />
    </svg>
    

#### CSS

We only style the first ellipse, letting its twin use default user agent styles (with [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
 defaulting to black). The geometric `rx` property overrides the value of the SVG [`rx`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/rx)
 attribute. We also set the `fill` and [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
 properties to differentiate the styled shape from its twin.

css

    svg {
      border: 1px solid;
    }
    
    ellipse:first-of-type {
      rx: 80px;
      fill: magenta;
      stroke: rebeccapurple;
    }
    

#### Results

The styled ellipse's horizontal radius is `80px`, as defined in the CSS `rx` property value. The unstyled ellipse's horizontal radius is `20px`, which was defined by the `rx` attribute.

### [Ellipse horizontal radius percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#ellipse_horizontal_radius_percentage_values)

This example demonstrates using percentage values for `rx`.

#### HTML

We use the same markup as the previous example.

html

    <svg xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="80" cy="50" rx="20" ry="40" />
      <ellipse cx="80" cy="50" rx="20" ry="40" />
    </svg>
    

#### CSS

The CSS is similar to the previous example, with the only difference being the `rx` property value; in this case, we use a percentage value.

css

    svg {
      border: 1px solid;
    }
    
    ellipse:first-of-type {
      rx: 30%;
      fill: magenta;
      stroke: rebeccapurple;
    }
    

#### Results

When using percentage values for `rx`, the values are relative to the width of the SVG viewport. Here, the size of the styled ellipse horizontal radius is `30%` of the width of the current SVG viewport. As the width defaulted to `300px`, the `rx` value is `90px`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# RX](https://w3c.github.io/svgwg/svg2-draft/geometry.html#RX) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx#see_also)

----------------------------------------------------------------------------------------------

*   Geometry properties: `rx`, [`cx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cx)
    , [`cy`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy)
    , [`r`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r)
    , [`ry`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ry)
    , [`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/x)
    , [`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y)
    , [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    , [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    
*   [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    
*   [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    
*   [`paint-order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order)
    
*   [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
     shorthand property
*   [`radial-gradient`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
    
*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
     data type
*   SVG [`rx`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/rx)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 25, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/rx/index.md?plain=1 "Folder: en-us/web/css/reference/properties/rx (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frx&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frx%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frx%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frx%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb94f607de0017642074f3466e20cbd9017a1b150%0A*+Document+last+modified%3A+2026-10-25T21%3A29%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")