*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#mdn-search)
    

`color-interpolation-filters` CSS property
==========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`color-interpolation-filters`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the color space for imaging operations performed via SVG filter effects. If explicitly declared, the value of the CSS property overrides any value given in the element's [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/color-interpolation-filters)
 attribute.

**Note:** The [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/color-interpolation-filters)
 property is only relevant to SVG filter operations. It has _no_ effect on filter primitives like [`<feOffset>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feOffset)
, [`<feImage>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feImage)
, [`<feTile>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feTile)
, and [`<feFlood>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFlood)
, but instead applies to the various filter effect elements (e.g., [`<feBlend>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feBlend)
); see the SVG [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/color-interpolation-filters)
 page for a full list.

**Note:** It is important to remember that the SVG [`color-interpolation`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/color-interpolation)
 attribute has an initial value of `sRGB`, while `color-interpolation-filters` has an initial value of `linearRGB`. This means, in the default case, filter effect interpolations occur in a different color space than all other color interpolations.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#syntax)

-------------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#values)

This property is specified as one of the following keyword values:

[`linearRGB`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#linearrgb)

Indicates that color interpolation should occur in the linearized RGB color space as described in [the sRGB specification](https://webstore.iec.ch/en/publication/6169 "External link (opens in new tab)")
. This is the default property value.

[`sRGB`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#srgb)

Indicates that color interpolation should occur in the gamma-encoded sRGB color space.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#auto)

Indicates that the user agent can choose either the `sRGB` or `linearRGB` spaces for color interpolation. This option indicates that the author doesn't require that color interpolation occur in a particular color space.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `linearRGB` |
| Applies to | The set of elements that control the output of a [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)<br> element in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------------

color-interpolation-filters =   
  auto       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sRGB       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  linearRGB    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# ColorInterpolationFiltersProperty](https://drafts.csswg.org/filter-effects/#ColorInterpolationFiltersProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [`color-interpolation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation)
    
*   SVG [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/color-interpolation-filters)
     attribute
*   [sRGB specification](https://webstore.iec.ch/en/publication/6169 "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/color-interpolation-filters/index.md?plain=1 "Folder: en-us/web/css/reference/properties/color-interpolation-filters (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolor-interpolation-filters&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolor-interpolation-filters%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolor-interpolation-filters%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolor-interpolation-filters%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")