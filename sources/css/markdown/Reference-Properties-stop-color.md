*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#mdn-search)
    

`stop-color` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`stop-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the color to use for an SVG [`<stop>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/stop)
 element within a gradient. If present, it overrides the element's [`stop-color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stop-color)
 attribute.

**Note:** The `stop-color` property only applies to [`<stop>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/stop)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG, HTML, or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#syntax)

--------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#values)

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The color of the fill. This can be any valid CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `black` |
| Applies to | [`<stop>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/stop)<br> elements in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#formal_syntax)

----------------------------------------------------------------------------------------------------------------

stop-color =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#examples)

------------------------------------------------------------------------------------------------------

### [Defining the color stops of SVG gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#defining_the_color_stops_of_svg_gradients)

This example demonstrates the basic use case of `stop-color`, and how the CSS `stop-color` property takes precedence over the `stop-color` attribute.

#### HTML

We have an SVG with three [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 squares and three [`<linearGradient>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/linearGradient)
 elements. Each gradient has four [`<stop>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/stop)
 elements creating gradients that go from black to white and then white to gray; the only difference between them is the `id` value.

#### CSS

We include a [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
 and [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
 outlining the rectangle. We define the colors of the first and last stops in each gradient, overriding their `stop-color` attribute values, using the `stop-color` property. Various CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 syntaxes are shown.

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# StopColorProperty](https://w3c.github.io/svgwg/svg2-draft/pservers.html#StopColorProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color#see_also)

------------------------------------------------------------------------------------------------------

*   SVG [`stop-color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stop-color)
     attribute
*   Presentation properties: `stop-color`, [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
    , [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters)
    , [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
    , [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
    , [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    , [`marker-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-end)
    , [`marker-mid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-mid)
    , [`marker-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start)
    , [`shape-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering)
    , [`stop-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity)
    , [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    , [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray)
    , [`stroke-dashoffset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)
    , [`stroke-linecap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)
    , [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin)
    , [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
    , [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)
    , [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
    , [`text-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor)
    , and [`vector-effect`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect)
    
*   [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
     data type

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/stop-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/stop-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstop-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstop-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstop-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstop-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F28f5f3b9b463fa842fa686ccc73c9e1d9b06282b%0A*+Document+last+modified%3A+2026-08-27T09%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")