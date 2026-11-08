*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#mdn-search)
    

`text-anchor` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since August 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-anchor`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property aligns a box containing a string of text where the wrapping area is determined from the [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
 property, and the text is then placed relative to the anchor point of the element, which is defined using the [`x`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/x)
 and [`y`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/y)
 (or [`dx`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/dx)
 and [`dy`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/dy)
) attributes. If present, the value of the CSS property overrides any value of the element's [`text-anchor`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/text-anchor)
 attribute.

Each individual text fragment within an element is aligned independently; thus, a multi-line [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
 element will have each line of text aligned as per the value of `text-anchor`. `text-anchor` values only have an effect on the [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
, [`<textPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/textPath)
, and [`<tspan>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/tspan)
 SVG elements. `text-anchor` does not apply to automatically wrapped text; for that, see [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#syntax)

---------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#values)

This property is specified as one of the following keyword values:

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#start)

Aligns the text such that the inline start of the text string is aligned with the anchor point. This alignment is relative to the writing direction of the text; thus, for example, in right-to-left top-to-bottom writing, the text will be placed to the left of the anchor point. If the text's inline direction is vertical, as with many Asian languages, the top edge of the text is aligned with the anchor point.

[`middle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#middle)

Aligns the text such that the center (middle) of the text string's inline box is aligned with the anchor point.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#end)

Aligns the text such that the inline end of the text string is aligned with the anchor point. This alignment is relative to the writing direction of the text; thus, for example, in right-to-left top-to-bottom writing, the text will be placed to the right of the anchor point. If the text's inline direction is vertical, as with many Asian languages, the bottom edge of the text is aligned with the anchor point.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `start` |
| Applies to | [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)<br>, [`<textPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/textPath)<br>, and [`<tspan>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/tspan)<br> elements in [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

text-anchor =   
  start   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  middle  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end       

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#example)

-----------------------------------------------------------------------------------------------------

Three `<text>` elements are given the same `x` position, but different values for `text-anchor`. A dashed red line is included to mark the x-axis position of all three anchor points.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# TextAnchorProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#TextAnchorProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor#see_also)

-------------------------------------------------------------------------------------------------------

*   [`dominant-baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline)
    
*   SVG [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
     element
*   SVG [`text-anchor`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/text-anchor)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-anchor/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-anchor (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-anchor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-anchor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-anchor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-anchor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")