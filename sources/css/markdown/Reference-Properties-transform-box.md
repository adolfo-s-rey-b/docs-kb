*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#mdn-search)
    

`transform-box` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transform-box`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the layout box to which the [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
, individual transform properties [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
, [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
, and [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
, and [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
 properties relate.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#syntax)

-----------------------------------------------------------------------------------------------------

The `transform-box` property is specified as one of the keyword values listed below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#values)

[`content-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#content-box)

The content box is used as the reference box. The reference box of a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 is the border box of its [table wrapper box](https://developer.mozilla.org/en-US/docs/Glossary/Table_Wrapper_Box)
, not its table box.

[`border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#border-box)

The border box is used as the reference box. The reference box of a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 is the border box of its [table wrapper box](https://developer.mozilla.org/en-US/docs/Glossary/Table_Wrapper_Box)
, not its table box.

[`fill-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#fill-box)

The object bounding box is used as the reference box. For elements with associated CSS layout box, acts as `content-box`.

[`stroke-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#stroke-box)

The stroke bounding box is used as the reference box. For elements with associated CSS layout box, acts as `border-box`.

[`view-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#view-box)

The nearest [SVG](https://developer.mozilla.org/en-US/docs/Glossary/SVG)
 viewport is used as the reference box. If a [`viewBox`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)
 attribute is specified for the SVG viewport creating element, the reference box is positioned at the origin of the coordinate system established by the `viewBox` attribute, and the dimension of the reference box is set to the width and height values of the `viewBox` attribute. For elements with associated CSS layout box, acts as `border-box`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `view-box` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

transform-box =   
  content-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  border-box   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fill-box     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stroke-box   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  view-box       

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#examples)

---------------------------------------------------------------------------------------------------------

### [SVG transform-origin scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#svg_transform-origin_scoping)

In this example we have an SVG:

In the CSS we have an animation that uses a transform to rotate the rectangle infinitely. `transform-box: fill-box` is used to make the `transform-origin` the center of the bounding box, so the rectangle spins in place. Without it, the transform origin is the center of the SVG canvas, and so you get a very different effect.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 1  <br>\# transform-box](https://drafts.csswg.org/css-transforms/#transform-box) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box#see_also)

---------------------------------------------------------------------------------------------------------

*   [Using CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
    
*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    , [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
    
*   Individual transform properties:
    *   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
        
    *   [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
        
    *   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transform-box/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transform-box (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransform-box&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransform-box%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransform-box%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransform-box%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")