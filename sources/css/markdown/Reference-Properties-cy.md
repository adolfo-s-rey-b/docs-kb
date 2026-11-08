*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#mdn-search)
    

`cy` CSS property
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`cy`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the y-axis center point of an SVG [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
 or [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)
 elements. If present, it overrides the element's [`cy`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/cy)
 attribute.

**Note:** While the SVG [`<radialGradient>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/radialGradient)
 element supports the [`cy`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/cy)
 attribute, the `cy` property only applies to [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
 and [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. This attribute does not apply to `<radialGradient>` or other SVG elements nor to HTML elements or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#syntax)

------------------------------------------------------------------------------------------

css

    /* length and percentage values */
    cy: 3px;
    cy: 20%;
    
    /* Global values */
    cy: inherit;
    cy: initial;
    cy: revert;
    cy: revert-layer;
    cy: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#values)

The [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 and [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values denote the vertical center of the circle or ellipse.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

As an absolute or relative length, it can be expressed in any unit allowed by the CSS [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 data type. Negative values are invalid.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Percentages refer to the height of the current SVG viewport.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#formal_definition)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)<br> and [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)<br> elements in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the height of the current SVG viewport |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#formal_syntax)

--------------------------------------------------------------------------------------------------------

cy =   
  <length-percentage>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#examples)

----------------------------------------------------------------------------------------------

### [Defining the y-axis coordinate of a circle and ellipse](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#defining_the_y-axis_coordinate_of_a_circle_and_ellipse)

In this example, we have two identical `<circle>` and two identical `<ellipse>` elements in an SVG; their `cy` attribute values ar `50` and `150`, respectively.

html

    <svg xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="30" />
      <circle cx="50" cy="50" r="30" />
      <ellipse cx="150" cy="50" rx="20" ry="40" />
      <ellipse cx="150" cy="50" rx="20" ry="40" />
    </svg>
    

With CSS, we style only the first circle and first ellipse, allowing their twin shapes to use default styles (with [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
 defaulting to black). We use the `cy` property to override the value of the SVG [`cy`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/cy)
 attribute and also give it a `fill` and [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
 to differentiate the first shapes in each pair from their twin. The browser renders SVG images as `300px` wide and `150px` tall by default.

css

    svg {
      border: 1px solid;
    }
    
    circle:first-of-type {
      cy: 30px;
      fill: lightgreen;
      stroke: black;
    }
    ellipse:first-of-type {
      cy: 100px;
      fill: pink;
      stroke: black;
    }
    

The styled circle's center is `30px` from the top edge of the SVG viewport and the styled ellipse is `100px` from that edge, as defined in the CSS `cy` property values. The unstyled shapes centers are both `50px` from the top edge of the SVG viewport, as defined in their SVG `cy` attribute values.

### [y-axis coordinates as percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#y-axis_coordinates_as_percentage_values)

In this example, we use the same markup as the previous example. The only difference is the CSS `cy` property value; in this case, we use percentage values of `30%` and `50%`.

    <svg xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="30" />
      <circle cx="50" cy="50" r="30" />
      <ellipse cx="150" cy="50" rx="20" ry="40" />
      <ellipse cx="150" cy="50" rx="20" ry="40" />
    </svg>
    

css

    svg {
      border: 1px solid;
    }
    
    circle:first-of-type {
      cy: 30%;
      fill: lightgreen;
      stroke: black;
    }
    ellipse:first-of-type {
      cy: 50%;
      fill: pink;
      stroke: black;
    }
    

In this case, the y-axis coordinates of the center of the circle and ellipse are `30%` and `50%` of the height of the current SVG viewport, respectively. As the image's height defaulted to `150px`, meaning the `cy` value is the equivalent of `45px` and `120px`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# CY](https://w3c.github.io/svgwg/svg2-draft/geometry.html#CY) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy#see_also)

----------------------------------------------------------------------------------------------

*   SVG [`cy`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/cy)
     attribute
*   Geometry properties: `cy`, [`cx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cx)
    , [`r`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r)
    , [`rx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx)
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

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/cy/index.md?plain=1 "Folder: en-us/web/css/reference/properties/cy (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcy&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcy%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcy%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcy%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")