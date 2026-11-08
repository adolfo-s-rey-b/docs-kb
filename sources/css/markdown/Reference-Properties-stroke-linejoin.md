*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#mdn-search)
    

`stroke-linejoin` CSS property
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`stroke-linejoin`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the shape to be used at the corners of an [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 element's stroked paths. If present, it overrides the element's [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-linejoin)
 attribute.

This property applies to any SVG corner-generating shape or text-content element (see [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-linejoin)
 for a full list), but as an inherited property, it may be applied to elements such as [`<g>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/g)
 and still have the intended effect on descendant elements'

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#syntax)

-------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#values)

[`bevel`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#bevel)

Indicates that a beveled corner is to be used to join path segments. The bevel is formed by truncating the corner by a line perpendicular to a line that bisects the difference in the subpath angles where they meet the join point.

[`miter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#miter)

Indicates that a sharp corner is to be used to join path segments. The corner is formed by extending the outer edges of the stroke at the tangents of the path segments until they intersect. This is the default value.

[`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#round)

Indicates that a round corner is to be used to join path segments. This is accomplished by cropping the join as per `bevel`, and then appending a filled arc tangent in order to round the corner.

The following values are defined, but not supported in any browser:

[`arcs`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#arcs)

_(Unsupported.)_ Indicates that an _arcs corner_ is to be used to join path segments. The arc's shape is formed by extending the outer edges of the stroke at the join point with arcs that have the same curvature as the outer edges at the join point.

[`crop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#crop)

_(Unsupported.)_ Indicates the corner should extend past the join point by the minimum amount necessary to form a convex corner. This is functionally equivalent to `miter` (see above) with a [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
 value of `1`.

[`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#fallback)

_(Unsupported; at risk.)_ behaves identically to `crop bevel` when the [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
 value is exceeded.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `miter` |
| Applies to | [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)<br>, [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)<br>, [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)<br>, [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)<br>, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)<br>, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)<br>, and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)<br> elements in an `svg` |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

stroke-linejoin =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 crop [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 arcs [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 miter [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
       [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 bevel [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 round [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 fallback [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#examples)

-----------------------------------------------------------------------------------------------------------

### [Line-joining styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#line-joining_styles)

This example demonstrates the three currently supported keyword values for `stroke-linejoin`.

#### HTML

We set up four identical paths, all of which have a black stroke with a width of one and no fill.

#### CSS

To each of the four paths, a supported line-joining value is applied. The first is beveled, the second rounded, the third mitered, and the fourth also mitered but with a [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
 of `2`, which forces the corner to be beveled instead of mitered.

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fill and Stroke Module Level 3  <br>\# stroke-linejoin](https://drafts.csswg.org/fill-stroke-3/#stroke-linejoin) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray)
    
*   [`stroke-dashoffset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)
    
*   [`stroke-linecap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)
    
*   [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
    
*   [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)
    
*   [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
    
*   [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    
*   SVG [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-linejoin)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/stroke-linejoin/index.md?plain=1 "Folder: en-us/web/css/reference/properties/stroke-linejoin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstroke-linejoin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstroke-linejoin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstroke-linejoin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstroke-linejoin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd19dec85109590176f946fcceef48c787d578b1e%0A*+Document+last+modified%3A+2026-08-27T15%3A03%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")