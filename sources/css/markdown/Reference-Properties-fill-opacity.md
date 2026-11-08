*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#mdn-search)
    

`fill-opacity` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`fill-opacity`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the opacity of the painting operation (color, gradient, pattern, etc.) applied to SVG shapes or text content elements to fill the element. The property defines the opacity of the element's `fill` only; it does not affect the stroke. If present, it overrides the element's [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-opacity)
 attribute.

**Note:** The `fill-opacity` property only applies to [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
, [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)
, [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)
, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)
, [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
, [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
, [`<textPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/textPath)
, and [`<tspan>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/tspan)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG, HTML, or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#syntax)

----------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#values)

The [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 and [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values denote the opacity of the `fill` of the element.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

A numeric value between `0` and `1`, inclusive.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A percentage value between `0%` and `100%`, inclusive.

With `0` or `0%`, the element is fully transparent. With `1` or `100%`, the element is fully opaque. With values in between, the element is semi-transparent, with content behind the element being visible.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `1` |
| Applies to | SVG shapes and text content elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| Percentages | map to the range `[0,1]` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | The same as the specified value after clipping the [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)<br> to the range \[0.0, 1.0\]. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#formal_syntax)

------------------------------------------------------------------------------------------------------------------

fill-opacity =   
  [<'opacity'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    
  
[<opacity>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 =   
  <opacity-value>    
  
<opacity-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#examples)

--------------------------------------------------------------------------------------------------------

### [Defining the fill opacity of SVG elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#defining_the_fill_opacity_of_svg_elements)

This example demonstrates the basic use case of `fill-opacity`, and how the CSS `fill-opacity` property takes precedence over the `fill-opacity` attribute and has no effect on any `stroke` applied to a shape.

#### HTML

We include several different SVG graphic elements and set the `fill-opacity` attribute of each one to `1` (except `line`), meaning the fill of each element is opaque. The `fill-opacity` SVG attribute does not apply to [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)
.

#### CSS

With CSS, we use the `fill-opacity` property to override the value of the SVG [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-opacity)
 attribute, giving each SVG element a different value.

We add a [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
 to the circle and ellipse, to demonstrate that the opacity of the stroke is not impacted by the `fill-opacity` property.

Other SVG styles are set, including a background image to allow the opacity of each element to be more easily seen. These are not shown for the sake of brevity.

#### Results

Only two elements are fully opaque: the first rectangle and the line. The first rectangle is not matched by any of the selectors, therefore no CSS is applied and the `fill` is fully opaque. The `line` is matched, with `fill-opacity: 10%` set. However, the line has no `fill` paint operation — only the `stroke` is visible — therefore the declaration has no effect.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fill and Stroke Module Level 3  <br>\# fill-opacity](https://drafts.csswg.org/fill-stroke-3/#fill-opacity) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity#see_also)

--------------------------------------------------------------------------------------------------------

*   SVG [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-opacity)
     attribute
*   Presentation properties: `fill-opacity`, [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
    , [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters)
    , [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
    , [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    , [`marker-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-end)
    , [`marker-mid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-mid)
    , [`marker-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start)
    , [`shape-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering)
    , [`stop-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color)
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

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/fill-opacity/index.md?plain=1 "Folder: en-us/web/css/reference/properties/fill-opacity (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffill-opacity&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffill-opacity%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffill-opacity%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffill-opacity%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")