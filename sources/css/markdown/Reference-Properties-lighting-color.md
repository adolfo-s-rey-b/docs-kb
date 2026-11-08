*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#mdn-search)
    

`lighting-color` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`lighting-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the color of the light source for the [`<feDiffuseLighting>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDiffuseLighting)
 and [`<feSpecularLighting>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feSpecularLighting)
 SVG lighting filter primitives within an SVG [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
. If present, it overrides the element's [`lighting-color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/lighting-color)
 attribute.

**Note:** The `lighting-color` property only applies to [`<feDiffuseLighting>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDiffuseLighting)
 and [`<feSpecularLighting>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feSpecularLighting)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG, HTML, or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#syntax)

------------------------------------------------------------------------------------------------------

css

    /* <color> values */
    lighting-color: red;
    lighting-color: hsl(120deg 75% 25% / 60%);
    lighting-color: currentColor;
    
    /* Global values */
    lighting-color: inherit;
    lighting-color: initial;
    lighting-color: revert;
    lighting-color: revert-layer;
    lighting-color: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#values)

This property is specified as one `<color>` value:

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The lighting's color. This can be any valid CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `white` |
| Applies to | [`<feDiffuseLighting>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDiffuseLighting)<br> and [`<feSpecularLighting>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feSpecularLighting)<br> elements in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

lighting-color =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#examples)

----------------------------------------------------------------------------------------------------------

### [Defining the color of filter lighting](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#defining_the_color_of_filter_lighting)

This example demonstrates the basic use case of `lighting-color`, and how the CSS `lighting-color` property takes precedence over the `lighting-color` attribute.

#### HTML

We have an SVG with two [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
 elements, one with a `<feDiffuseLighting>` and one with a `<feSpecularLighting>` child. Each includes the SVG `lighting-color` attribute defining the lighting color as `red`. Both of these children have a [`<fePointLight>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/fePointLight)
, the required child that sets the light source. We included two [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 elements with a filter attribute; this is where the filters will be displayed.

html

    <svg viewBox="0 0 420 120" xmlns="http://www.w3.org/2000/svg">
      <filter id="flood1">
        <feDiffuseLighting lighting-color="red">
          <fePointLight x="75" y="30" z="10" />
        </feDiffuseLighting>
      </filter>
      <filter id="flood2">
        <feSpecularLighting specularExponent="5" lighting-color="red">
          <fePointLight x="225" y="75" z="5" />
        </feSpecularLighting>
      </filter>
    
      <rect id="r1" filter="url(#flood1)" />
      <rect id="r2" filter="url(#flood2)" />
    </svg>
    

#### CSS

We define the size and position of our `<rect>` using the CSS [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/x)
, and [`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y)
 properties. We also add a background image to the SVG to make any color alpha transparency more apparent:

css

    svg {
      background-image: repeating-linear-gradient(
        45deg,
        transparent 0 9px,
        #cccccc 0px 10px
      );
    }
    
    rect {
      width: 100px;
      height: 100px;
      x: 10px;
      y: 10px;
    }
    
    #r2 {
      x: 150px;
    }
    

We then apply different lighting color values to the filter's child elements using the CSS `lighting-color` property. We use a named color and a 3-digit hexadecimal color, but we can use any valid CSS color syntax:

css

    feDiffuseLighting {
      lighting-color: blue;
    }
    
    feSpecularLighting {
      lighting-color: #ff0099;
    }
    

#### Results

The attributes defined the color of both light filters as `red`, but these values were overridden by the CSS `lighting-color` values.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# LightingColorProperty](https://drafts.csswg.org/filter-effects/#LightingColorProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color#see_also)

----------------------------------------------------------------------------------------------------------

*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    
*   [`flood-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color)
    
*   [`stop-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color)
    
*   [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    
*   [`flood-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
    
*   SVG [`lighting-color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/lighting-color)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/lighting-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/lighting-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flighting-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flighting-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flighting-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flighting-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")