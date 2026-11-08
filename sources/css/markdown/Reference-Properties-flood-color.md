*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#mdn-search)
    

`flood-color` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`flood-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the color of the current filter primitive subregion in [`<feFlood>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFlood)
 and [`<feDropShadow>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDropShadow)
 elements within a [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
. If present, it overrides the element's [`flood-color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/flood-color)
 attribute.

**Note:** The `flood-color` property only applies to [`<feFlood>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFlood)
 and [`<feDropShadow>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDropShadow)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG, HTML, or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#syntax)

---------------------------------------------------------------------------------------------------

css

    /* <color> values */
    flood-color: red;
    flood-color: hsl(120deg 75% 25% / 60%);
    flood-color: currentColor;
    
    /* Global values */
    flood-color: inherit;
    flood-color: initial;
    flood-color: revert;
    flood-color: revert-layer;
    flood-color: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#values)

This property is specified as one `<color>` value:

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The flood's color. This can be any valid CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `black` |
| Applies to | [`<feFlood>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFlood)<br> and [`<feDropShadow>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDropShadow)<br> elements in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

flood-color =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#examples)

-------------------------------------------------------------------------------------------------------

### [Defining the color of a filters flood](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#defining_the_color_of_a_filters_flood)

This example demonstrates the basic use case of `flood-color`, and how the CSS `flood-color` property takes precedence over the `flood-color` attribute.

#### HTML

We have an SVG with two [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
 elements, each with a [`<feFlood>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFlood)
 child. Each `<feFlood>` element includes the SVG `flood-color` attribute defining the flood color as `seagreen`. We included two [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 elements with a filter attribute; this is where the filters will be displayed.

html

    <svg viewBox="0 0 420 120" xmlns="http://www.w3.org/2000/svg">
      <filter id="flood1">
        <feFlood flood-color="seagreen" />
      </filter>
      <filter id="flood2">
        <feFlood flood-color="seagreen" />
      </filter>
    
      <rect id="r1" filter="url(#flood1)" />
      <rect id="r2" filter="url(#flood2)" />
    </svg>
    

#### CSS

We define the size and position of our `<rect>` using the CSS [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/x)
, and [`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y)
 properties:

css

    rect {
      width: 100px;
      height: 100px;
      x: 10px;
      y: 10px;
    }
    #r2 {
      x: 150px;
    }
    

We then apply different flood color values to the `<feFlood>` elements using the CSS `flood-color` property. We use a named color and a 3-digit hexadecimal color, but we can use any valid CSS color syntax:

css

    #flood1 feFlood {
      flood-color: rebeccapurple;
    }
    #flood2 feFlood {
      flood-color: #ff3366;
    }
    

#### Results

The attributes defined the squares as seagreen, but these values were overridden by the CSS `flood-color` values.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# FloodColorProperty](https://drafts.csswg.org/filter-effects/#FloodColorProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color#see_also)

-------------------------------------------------------------------------------------------------------

*   [`flood-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity)
    
*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    
*   [`lighting-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color)
    
*   [`stop-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color)
    
*   [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    
*   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
    
*   SVG [`flood-color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/flood-color)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flood-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flood-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflood-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflood-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflood-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflood-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")