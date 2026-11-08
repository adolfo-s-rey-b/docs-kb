*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#mdn-search)
    

`r` CSS property
================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`r`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the radius of a circle. It can only be used with the SVG [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
 element. If present, it overrides the circle's [`r`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/r)
 attribute.

**Note:** The `r` property only applies to [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG elements or HTML elements or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#syntax)

-----------------------------------------------------------------------------------------

css

    /* Length and percentage values */
    r: 3px;
    r: 20%;
    
    /* Global values */
    r: inherit;
    r: initial;
    r: revert;
    r: revert-layer;
    r: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#values)

The [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 and [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values define the radius of the circle.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Absolute or relative lengths can be expressed in any unit allowed by the CSS [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 data type. Negative values are invalid.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Percentages refer to the normalized diagonal of the current SVG viewport, which is calculated as <width>2+<height>22.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#formal_definition)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)<br> element in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the normalized diagonal of the current SVG viewport |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#formal_syntax)

-------------------------------------------------------------------------------------------------------

r =   
  <length-percentage>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#examples)

---------------------------------------------------------------------------------------------

### [Defining the radius of a circle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#defining_the_radius_of_a_circle)

In this example, we have two identical `<circle>` elements in an SVG, each with a `10` radius and the same x- and y-axis coordinates for their center points.

html

    <svg xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="10" />
      <circle cx="50" cy="50" r="10" />
    </svg>
    

With CSS, we style only the first circle, allowing the second circle to use default styles (with [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
 defaulting to black). We use the `r` property to override the value of the SVG [`r`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/r)
 attribute, giving it a `fill` and [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
. The default size of an SVG is `300px` wide and `150px` tall.

css

    svg {
      border: 1px solid black;
    }
    
    circle:first-of-type {
      r: 30px;
      fill: lightgreen;
      stroke: black;
    }
    

### [ViewBox versus viewport pixels](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#viewbox_versus_viewport_pixels)

This example contains two SVGs, each with two `<circle>` elements. The second SVG includes a `viewBox` attribute to demonstrate the difference between SVG viewBox and SVG viewports.

html

    <svg xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="10" />
      <circle cx="50" cy="50" r="10" />
    </svg>
    <svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="10" />
      <circle cx="50" cy="50" r="10" />
    </svg>
    

The CSS is similar to the previous example, with `r: 30px` set, but we set a [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 to ensure the images are both `300px` wide:

css

    svg {
      border: 1px solid black;
      width: 300px;
    }
    
    circle:first-of-type {
      r: 30px;
      fill: lightgreen;
      stroke: black;
    }
    

Because the `viewBox` attribute defines the SVG as 200 SVG coordinate system pixels wide, and the image is scaled up to `300px`, the `30` SVG coordinate pixels are scaled to be rendered as `45` CSS pixels.

### [Defining the radius of a circle using percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#defining_the_radius_of_a_circle_using_percentages)

In this example, we use the same markup as the previous example. The only difference is the `r` value; in this case, we use a percentage value.

    <svg xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="10" />
      <circle cx="50" cy="50" r="10" />
    </svg>
    <svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="10" />
      <circle cx="50" cy="50" r="10" />
    </svg>
    

css

    svg {
      border: 1px solid black;
      width: 300px;
    }
    
    circle:first-of-type {
      r: 30%;
      fill: lightgreen;
      stroke: black;
    }
    

In both cases, the circle radius is `30%` of the normalized diagonal of the SVG viewport. The radius `r` is equal to 0.3×<width>2+<height>22. While the first image is using `300` and `150` CSS pixels and the second is using `200` and `100` SVG view box units, 30% is a proportional value. As a result, the `r` value is the same: `47.43` viewBox units, which resolves to `71.15` CSS pixels.

While the `r` is the same, the center points differ because the second SVG is scaled up by 50%, pushing its center down and to the right by 50%.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# R](https://w3c.github.io/svgwg/svg2-draft/geometry.html#R) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r#see_also)

---------------------------------------------------------------------------------------------

*   Geometry properties: `r`, [`cx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cx)
    , [`cy`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy)
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
*   SVG [`r`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/r)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/r/index.md?plain=1 "Folder: en-us/web/css/reference/properties/r (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fr&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fr%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fr%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fr%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")