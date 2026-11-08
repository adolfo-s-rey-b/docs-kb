*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#mdn-search)
    

`stop-opacity` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`stop-opacity`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the opacity of a given color gradient stop in the SVG [`<stop>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/stop)
 element within an SVG gradient. If present, it overrides the element's [`stop-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stop-opacity)
 attribute.

The property value impacts the [`stop-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color)
's alpha channel; it can increase the transparency of a `<stop>`'s color but cannot make the color defined by the `stop-color` property more opaque.

**Note:** The `stop-opacity` property only applies to [`<stop>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/stop)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG, HTML, or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#syntax)

----------------------------------------------------------------------------------------------------

css

    /* numeric and percentage values */
    stop-opacity: 0.2;
    stop-opacity: 20%;
    
    /* Global values */
    stop-opacity: inherit;
    stop-opacity: initial;
    stop-opacity: revert;
    stop-opacity: revert-layer;
    stop-opacity: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#values)

The `<opacity-value>` is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 denoting the opacity of the SVG gradient `<stop>` element.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

A numeric value between `0` and `1`, inclusive.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A percentage value between `0%` and `100%`, inclusive.

With `0` or `0%` set, the stop is fully transparent. With `1` or `100%` set, the element is the full opacity of the `stop-color` value, which may or may not be partially opaque.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `black` |
| Applies to | [`<stop>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/stop)<br> elements in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#formal_syntax)

------------------------------------------------------------------------------------------------------------------

stop-opacity =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#examples)

--------------------------------------------------------------------------------------------------------

### [Defining the opacity of an SVG gradient color stop](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#defining_the_opacity_of_an_svg_gradient_color_stop)

This example demonstrates the basic use case of `stop-opacity`, and how the CSS `stop-opacity` property takes precedence over the `stop-opacity` attribute.

#### HTML

We have an SVG with a few [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)
 stars and three [`<linearGradient>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/linearGradient)
 elements: each has three [`<stop>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/stop)
 elements defining three color-stops that create a gradient going from blue to white to pink; the only difference between them is the `id` value.

html

    <svg viewBox="0 0 250 120" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="myGradient1">
          <stop offset="5%" stop-color="#66ccff" stop-opacity="1" />
          <stop offset="50%" stop-color="#fefefe" stop-opacity="1" />
          <stop offset="95%" stop-color="#f4aab9" stop-opacity="1" />
        </linearGradient>
        <linearGradient id="myGradient2">
          <stop offset="5%" stop-color="#66ccff" stop-opacity="1" />
          <stop offset="50%" stop-color="#fefefe" stop-opacity="1" />
          <stop offset="95%" stop-color="#f4aab9" stop-opacity="1" />
        </linearGradient>
        <linearGradient id="myGradient3">
          <stop offset="5%" stop-color="#66ccff" stop-opacity="1" />
          <stop offset="50%" stop-color="#fefefe" stop-opacity="1" />
          <stop offset="95%" stop-color="#f4aab9" stop-opacity="1" />
        </linearGradient>
      </defs>
      <polygon points="40,10 10,100 80,40 0,40 70,100" />
      <polygon points="125,10 95,100 165,40 85,40 155,100" />
      <polygon points="210,10 180,100 250,40 170,40 240,100" />
    </svg>
    

#### CSS

We include a [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
 and [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
 making the polygon path line visible.

Each `polygon` has a gradient background set using the [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
 property; the gradient's `id` is the `url()` parameter. We set `magenta` as the fallback color.

We define the opacity of the stops of each gradient using the `stop-opacity` property.

The SVG has a striped background to make the transparency settings more apparent.

    svg {
      border: 1px solid;
      height: calc(100vh - 20px);
      margin-bottom: 10px;
      background: repeating-linear-gradient(
        to top left,
        white 0 9px,
        black 9px 10px
      );
    }
    

css

    polygon {
      stroke: #333333;
      stroke-width: 1px;
    }
    polygon:nth-of-type(1) {
      fill: url("#myGradient1") magenta;
    }
    polygon:nth-of-type(2) {
      fill: url("#myGradient2") magenta;
    }
    polygon:nth-of-type(3) {
      fill: url("#myGradient3") magenta;
    }
    
    #myGradient1 stop {
      stop-opacity: 1;
    }
    #myGradient2 stop {
      stop-opacity: 0.8;
    }
    #myGradient3 stop {
      stop-opacity: 25%;
    }
    

#### Results

The first star is fully opaque. The fill of the second star is 80% opaque because the color stops are slightly translucent; the `stop-opacity: 0.8;` overrode the `stop-opacity="1"` element attribute value. The fill of the last star is barely noticeable with color stops that are 25% opaque. Note the stroke is the same opaque dark gray in all cases.

**Note:** Because we used the same `stop-opacity` value for all the sibling `<stop>` elements in the linear gradient, we could have instead used a single `<linearGradient>` with fully opaque stops, and set a value for each `<polygon>`s [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
 property instead.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# StopOpacityProperty](https://w3c.github.io/svgwg/svg2-draft/pservers.html#StopOpacityProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity#see_also)

--------------------------------------------------------------------------------------------------------

*   SVG [`stop-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stop-opacity)
     attribute
*   Presentation properties: `stop-opacity`, [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
    , [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters)
    , [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
    , [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
    , [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    , [`marker-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-end)
    , [`marker-mid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-mid)
    , [`marker-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start)
    , [`shape-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering)
    , [`stop-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color)
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

This page was last modified on Sep 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/stop-opacity/index.md?plain=1 "Folder: en-us/web/css/reference/properties/stop-opacity (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstop-opacity&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstop-opacity%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstop-opacity%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstop-opacity%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc9f3d85f24d7839c9fe36a68d8042d088d906147%0A*+Document+last+modified%3A+2026-09-05T08%3A25%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")