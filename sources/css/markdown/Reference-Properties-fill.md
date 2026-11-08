*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#mdn-search)
    

`fill` CSS property
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`fill`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines how SVG text content and the interior canvas of SVG shapes are filled or painted. If present, it overrides the element's [`fill`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill)
 attribute.

The areas inside the outline of the SVG shape or text are painted. What is "inside" a shape may not always be clear. The paths defining a shape may overlap. The areas considered "inside" these complex shapes are clarified by the [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
 property or attribute.

If subpaths are open, `fill` closes the path before painting, as if a "closepath" command were included connecting the last point of the subpath with the first point of the subpath. In other words, `fill` applies to open subpaths within `path` elements (i.e., subpaths without a closepath command) and `polyline` elements.

**Note:** The `fill` property only applies to [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
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

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#syntax)

--------------------------------------------------------------------------------------------

css

    /* Keyword values */
    fill: none;
    fill: context-fill;
    fill: context-stroke;
    
    /* <color> values */
    fill: red;
    fill: hsl(120deg 75% 25% / 60%);
    
    /* <url> values */
    fill: url("#gradientElementID");
    fill: url("star.png");
    
    /* <url> with fallback */
    fill: url("#gradientElementID") blue;
    fill: url("star.png") none;
    
    /* Global values */
    fill: inherit;
    fill: initial;
    fill: revert;
    fill: revert-layer;
    fill: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#values)

This property is specified as a single value from the following list or as two values when using `<url>`:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#none)

No `fill` is painted; the areas inside the stroke, if any, are transparent.

[`context-fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#context-fill)

Uses the paint value of `fill` from a context element.

[`context-stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#context-stroke)

Uses the paint value of `stroke` from a context element.

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The color of the fill as any valid CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value.

[`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#url)

A URL reference to an SVG paint server element, such as a [`<linearGradient>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/linearGradient)
, [`<radialGradient>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/radialGradient)
, or [`<pattern>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/pattern)
. The resource reference can optionally be followed by a `<color>` or `none`, which will be used as a fallback if the referenced paint server doesn't resolve.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#formal_definition)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `black` |
| Applies to | SVG shapes and text content elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with `<color>` values computed and `<url>` values made absolute |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#formal_syntax)

----------------------------------------------------------------------------------------------------------

fill =   
  <paint>    
  
[<paint>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint)
 =   
  none         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <svg-paint>    
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-set()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cross-fade()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <element()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<gradient>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
        
  
<svg-paint> =   
  child               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  child( <integer> )    
  
[<image()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  image( <image-tags>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image-src>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 , [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
! )    
  
[<image-set()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
 =   
  image-set( <image-set-option>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<cross-fade()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
 =   
  cross-fade( <cf-image>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<element()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
 =   
  element( <id-selector> )    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
<image-tags> =   
  ltr  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rtl    
  
<image-src> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
<image-set-option> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<resolution>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 type( [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<cf-image> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<id-selector> =   
  <hash-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#examples)

------------------------------------------------------------------------------------------------

### [Defining fill values for SVG elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#defining_fill_values_for_svg_elements)

This example demonstrates how a `fill` is declared, the effect of the property, and how the CSS `fill` property takes precedence over the `fill` attribute.

#### HTML

We have an SVG with two complex shapes defined using the SVG [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)
 and [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
 elements. Both have the `fill` attribute set to the default `black`. We add a dark gray stroke of `#666666` using the SVG [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
 attribute but could have used the [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
 property.

html

    <svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M 10,5 l 90,0 -80,80 0,-60 80,80 -90,0 z"
        stroke="#666666"
        fill="black" />
      <polygon
        points="180,10 150,100 220,40 140,40 210,100"
        stroke="#666666"
        fill="black" />
    </svg>
    

#### CSS

We set `fill` values on the shapes in the SVG.

    svg {
      border: 1px solid;
      height: calc(100vh - 20px);
      margin-bottom: 10px;
    }
    

css

    path {
      fill: red;
    }
    polygon {
      fill: hsl(0deg 100% 50% / 60%);
    }
    

#### Results

The CSS `fill` property value overrides the SVG `fill` attribute value, resulting in both shapes being filled with a red color; the polygon's red is translucent.

### [Using fill keyword values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#using_fill_keyword_values)

This example demonstrates using keyword values for `fill`.

#### HTML

We include three [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
 elements and a [`<marker>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/marker)
 element that adds a [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
 to every path point. We set the circle marker to be black with a gray fill with the SVG [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
 and [`fill`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill)
 attributes.

html

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 90">
      <path d="M 10 44.64 L 30 10 L 70 10 L 90 44.64 L 70 79.28 L 30 79.28 Z" />
      <path d="M 100 44.64 L 80 10 L 120 10 L 140 44.64 L 120 79.28 L 80 79.28 Z" />
      <path
        d="M 150 44.64 L 130 10 L 170 10 L 190 44.64 L 170 79.28 L 130 79.28 Z" />
      <marker
        id="circle"
        markerWidth="12"
        markerHeight="12"
        refX="6"
        refY="6"
        markerUnits="userSpaceOnUse">
        <circle cx="6" cy="6" r="3" stroke-width="2" stroke="black" fill="grey" />
      </marker>
    </svg>
    

#### CSS

We set different `stroke` and `fill` colors on each path. The first path, the one with a red border, has its `fill` set to `none`. We set the circle marker's stroke and fill to the same color as the stroke of the element they're marking, using the `context-stroke` value.

    svg {
      border: 1px solid;
      height: calc(100vh - 20px);
      margin-bottom: 10px;
    }
    

css

    path {
      stroke-width: 2px;
      marker: url("#circle");
    }
    path:nth-of-type(1) {
      stroke: red;
      fill: none;
    }
    path:nth-of-type(2) {
      stroke: green;
      fill: lightgreen;
    }
    path:nth-of-type(3) {
      stroke: blue;
      fill: lightblue;
    }
    circle {
      stroke: context-stroke;
      fill: context-stroke;
    }
    

#### Results

Note how the first path has a transparent background because the `fill` is `none`, overriding the default `fill` of `black`. The circles are filled with the color of the stroke. If you change the value to `context-fill`, the circles will be transparent, `lightgreen` and `lightblue` instead of `red`, `green`, and `blue`.

### [Fills and fallbacks](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#fills_and_fallbacks)

This example demonstrates how to include a `url()` value with a fallback as a `fill` value.

#### HTML

We have an SVG containing two [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)
 stars and a [`<linearGradient>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/linearGradient)
 that goes from green to gold to red.

html

    <svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="myGradient">
          <stop offset="5%" stop-color="green" />
          <stop offset="50%" stop-color="gold" />
          <stop offset="95%" stop-color="red" />
        </linearGradient>
      </defs>
      <polygon points="80,10 50,100 120,40 40,40 110,100" />
      <polygon points="180,10 150,100 220,40 140,40 210,100" />
    </svg>
    

#### CSS

We set `fill` values on the polygons in the SVG, providing a `url()` value and a fallback.

    svg {
      border: 1px solid;
      height: calc(100vh - 20px);
      margin-bottom: 10px;
    }
    

css

    polygon:first-of-type {
      fill: url("#myGradient") magenta;
    }
    polygon:last-of-type {
      fill: url("#MISSINGIMAGE") magenta;
    }
    

#### Results

The first star has a gradient as a background. The second star uses the fallback value, as the element referenced in the `url()` does not exist.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# FillProperty](https://w3c.github.io/svgwg/svg2-draft/painting.html#FillProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill#see_also)

------------------------------------------------------------------------------------------------

*   SVG [`fill`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill)
     attribute
*   Presentation properties: `fill`, [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
    , [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters)
    , [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
    , [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
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

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/fill/index.md?plain=1 "Folder: en-us/web/css/reference/properties/fill (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffill&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffill%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffill%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffill%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")