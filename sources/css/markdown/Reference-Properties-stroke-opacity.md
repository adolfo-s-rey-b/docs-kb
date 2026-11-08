*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#mdn-search)
    

`stroke-opacity` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`stroke-opacity`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the opacity of an [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 shape's stroke. The effect is identical to that of [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
, except it is applied only to the stroke, not to the entire element. If present, it overrides the element's [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-opacity)
 attribute.

This property applies to SVG shapes and text-content elements (see [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-opacity)
 for a full list), but as an inherited property, it may be applied to elements such as [`<g>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/g)
 and still have the intended effect on descendant elements' strokes.

Note that a shape's stroke partially covers the fill of that shape, so a stroke with an opacity less than `1` will show the fill blended with the stroke where they overlap. To avoid this effect, it is possible to apply a global opacity with the [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 property or to put the stroke behind the fill with the [`paint-order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order)
 attribute.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#syntax)

------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#values)

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

Any real number from 0 to 1, inclusive. A value of `0` makes the stroke completely transparent, and a value of `1` makes it completely opaque. Values outside the range 0 – 1 are clipped to the nearest end of that range; thus, negative values are clipped to `0`.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

The same as `<number>` (see above), except the allowed range is 0% to 100% and clipping is done with regard to that range.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `1` |
| Applies to | [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)<br>, [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)<br>, [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)<br>, [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)<br>, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)<br>, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)<br>, and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)<br> elements in an `svg` |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified value, clipped in the range `[0,1]` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

stroke-opacity =   
  [<'opacity'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    
  
[<opacity>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 =   
  <opacity-value>    
  
<opacity-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#examples)

----------------------------------------------------------------------------------------------------------

### [Various stroke opacities](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#various_stroke_opacities)

This example demonstrates basic usage of the `stroke-opacity` property and how, as a shape's stroke partially covers its fill, a stroke with an opacity less than `1` blends with the fill where they overlap.

#### HTML

First, we set up five multi-segment paths, all of which use a black stroke with a width of one, and a `dodgerblue` fill for the subpaths. Each path creates a series of mountain symbols, going from left (a shallow corner angle) to right (an extreme corner angle).

#### CSS

To these paths, we apply a successively higher stroke opacity value. For the first four paths, the fill can be seen through the inner half of the stroke path, though it may be difficult to discern for the fourth path. For the fifth and last path, the stroke is fully opaque and so the fill cannot be seen through the stroke.

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fill and Stroke Module Level 3  <br>\# stroke-opacity](https://drafts.csswg.org/fill-stroke-3/#stroke-opacity) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity#see_also)

----------------------------------------------------------------------------------------------------------

*   [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    
*   [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
    
*   [`paint-order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order)
    
*   [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    
*   [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray)
    
*   [`stroke-dashoffset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)
    
*   [`stroke-linecap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)
    
*   [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin)
    
*   [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
    
*   [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
    
*   SVG [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-opacity)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/stroke-opacity/index.md?plain=1 "Folder: en-us/web/css/reference/properties/stroke-opacity (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstroke-opacity&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstroke-opacity%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstroke-opacity%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstroke-opacity%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")