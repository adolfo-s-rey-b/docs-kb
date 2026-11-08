*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#mdn-search)
    

`flood-opacity` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`flood-opacity`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the opacity of the current filter primitive subregion in [`<feFlood>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFlood)
 and [`<feDropShadow>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDropShadow)
 elements within a [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
. If present, it overrides the element's [`flood-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/flood-opacity)
 attribute.

The property value impacts the [`flood-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color)
's alpha channel; it can increase the transparency of a `flood-color` but cannot make the color defined by the `flood-color` property more opaque.

**Note:** The `flood-opacity` property only applies to [`<feFlood>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFlood)
 and [`<feDropShadow>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDropShadow)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG, HTML, or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#syntax)

-----------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#values)

The `<opacity-value>` is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 denoting the opacity of the SVG gradient `<flood>` element.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

A numeric value between `0` and `1`, inclusive.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A percentage value between `0%` and `100%`, inclusive.

With `0` or `0%` set, the flood is fully transparent. With `1` or `100%` set, the element is the full opacity of the `flood-color` value, which may or may not be partially opaque.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `black` |
| Applies to | [`<feFlood>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFlood)<br> and [`<feDropShadow>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDropShadow)<br> elements in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified value, clipped in the range `[0,1]` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

flood-opacity =   
  [<'opacity'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    
  
[<opacity>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 =   
  <opacity-value>    
  
<opacity-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#examples)

---------------------------------------------------------------------------------------------------------

### [Defining the flood opacity of a filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#defining_the_flood_opacity_of_a_filter)

This example demonstrates the basic use case of `flood-opacity`, and how the CSS `flood-opacity` property takes precedence over the `flood-opacity` attribute.

#### HTML

We have an SVG with a few [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
 elements, each with a [`<feFlood>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFlood)
 child. The `<feFlood>` define the filters as `seagreen`, with the first being declared by its `flood-opacity` attribute as fully opaque and the second being fully transparent. We included two [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 elements, each with a filter attribute.

#### CSS

We define the [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/x)
, and [`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y)
,positioning of our rectangles with CSS, and include a repeating linear gradient as a [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 on the SVG so the opacity of the flood-color is more apparent:

We then apply different flood opacity values to the `<feFlood>` elements using the CSS `flood-opacity`: property:

#### Results

The attributes defined the first square as fully opaque and the second as fully transparent, but these values were overridden by the CSS `flood-opacity` values. The seagreen filters are 50% and 90% opaque, respectively.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# FloodOpacityProperty](https://drafts.csswg.org/filter-effects/#FloodOpacityProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity#see_also)

---------------------------------------------------------------------------------------------------------

*   [`flood-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color)
    
*   [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    
*   [`stop-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity)
    
*   [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)
    
*   [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    
*   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    
*   [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
    , including [`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
    
*   SVG [`flood-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/flood-opacity)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flood-opacity/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flood-opacity (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflood-opacity&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflood-opacity%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflood-opacity%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflood-opacity%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc9f3d85f24d7839c9fe36a68d8042d088d906147%0A*+Document+last+modified%3A+2026-09-05T08%3A25%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")