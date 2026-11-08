*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#mdn-search)
    

`fill-rule` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`fill-rule`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the rule used to determine which parts of the SVG shape's canvas are included inside a shape to be filled. If present, it overrides the element's [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
 attribute.

The `fill-rule` clarifies which areas of a shape should be considered "inside" the shape. It provides two values you can set to tell the browser how the inside of a shape should be determined. For shapes that don't have intersecting paths, like a circle, the bounds of what is inside a shape to be filled are intuitively clear. With complex shapes that include intersecting paths (such as a Venn diagram) or paths enclosing other paths (such as a donut), the interpretation of which sections of the shape are "inside" the shape and should be filled by the [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
 property, may not be obvious.

**Note:** The `fill-rule` property only applies to [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)
, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)
, [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
, [`<textPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/textPath)
, and [`<tspan>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/tspan)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG, HTML, or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#syntax)

-------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    fill-rule: evenodd;
    fill-rule: nonzero;
    
    /* Global values */
    fill-rule: inherit;
    fill-rule: initial;
    fill-rule: revert;
    fill-rule: revert-layer;
    fill-rule: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#values)

This property is specified as one of the following keyword values:

[`nonzero`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#nonzero)

For every point in the shape, a ray is drawn in a random direction to beyond the shape's outer edges. Each ray is examined to determine the places where the ray crosses the shape. Starting with a count of zero, add one each time a path segment crosses the ray from left to right and subtract one each time a path segment crosses the ray from right to left. After counting the crossings, if the result is zero then the point is outside the path. Otherwise, it is inside.

[`evenodd`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#evenodd)

For every point in the fill rule's box, a ray is drawn in a random direction. The number of path segments from the given shape that the ray crosses are counted. If this number is odd, the point is inside; if even, the point is outside. Zero is taken to be even.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `nonzero` |
| Applies to | SVG shapes and text content elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#formal_syntax)

---------------------------------------------------------------------------------------------------------------

fill-rule =   
  nonzero  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  evenodd    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#examples)

-----------------------------------------------------------------------------------------------------

### [Defining the fill rules for SVG elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#defining_the_fill_rules_for_svg_elements)

This example demonstrates how a `fill-rule` is declared, the effect of the property, and how the CSS `fill-rule` property takes precedence over the `fill-rule` attribute.

#### HTML

We define an SVG with two complex shapes defined using the SVG [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)
 and [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
 elements. The polygon has the SVG `fill-rule` attribute set to `evenodd` and the star-shaped path is set to `nonzero`, which is the default. To make the lines visible, we set the outline to `red` using the SVG [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
 attribute (we could have alternatively used the [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
 property).

    <p>Original SVG</p>
    

html

    <svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
      <polygon
        points="180,10 150,100 220,40 140,40 210,100"
        stroke="red"
        fill-rule="evenodd" />
      <path
        d="M 10,5 l 90,0 -80,80 0,-60 80,80 -90,0 z"
        stroke="red"
        fill-rule="nonzero" />
    </svg>
    

    <p><code>fill-rule: nonzero;</code></p>
    <svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
      <polygon
        points="180,10 150,100 220,40 140,40 210,100"
        stroke="red"
        fill-rule="evenodd" />
      <path
        d="M 10,5 l 90,0 -80,80 0,-60 80,80 -90,0 z"
        stroke="red"
        fill-rule="nonzero" />
    </svg>
    <p><code>fill-rule: evenodd;</code></p>
    <svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
      <polygon
        points="180,10 150,100 220,40 140,40 210,100"
        stroke="red"
        fill-rule="evenodd" />
      <path
        d="M 10,5 l 90,0 -80,80 0,-60 80,80 -90,0 z"
        stroke="red"
        fill-rule="nonzero" />
    </svg>
    

The above SVG is repeated three times; we've only shown one copy for the sake of brevity.

#### CSS

The shapes nested in the first SVG have no CSS applied. We set the shapes inside the second SVG to use the `nonzero` value. The third SVG has all its nested shapes set to `evenodd`.

    svg {
      border: 1px solid;
      height: calc(33vh - 2.5em);
      margin-bottom: 10px;
    }
    p {
      margin: 0;
    }
    

css

    svg:nth-of-type(2) > * {
      fill-rule: nonzero;
    }
    svg:nth-of-type(3) > * {
      fill-rule: evenodd;
    }
    

#### Results

With the `nonzero` value for `fill-rule`, the "inside" of the shape is the entire shape. The `evenodd` value defines some space as empty. The first image renders the `fill-rule` included as an attribute. Declaring the `fill-rule` in the CSS overrides the attribute values in the second and third images.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fill and Stroke Module Level 3  <br>\# fill-rule](https://drafts.csswg.org/fill-stroke-3/#fill-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule#see_also)

-----------------------------------------------------------------------------------------------------

*   SVG [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
     attribute
*   Presentation properties: `fill-rule`, [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
    , [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters)
    , [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
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

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/fill-rule/index.md?plain=1 "Folder: en-us/web/css/reference/properties/fill-rule (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffill-rule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffill-rule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffill-rule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffill-rule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")