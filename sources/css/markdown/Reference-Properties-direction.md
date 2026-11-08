*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#mdn-search)
    

`direction` CSS property
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Warning:** Where possible, authors are encouraged to avoid using the `direction` CSS property and use the HTML [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
 global attribute instead.

The **`direction`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the direction of text, table and grid columns, and horizontal overflow. Use `rtl` for languages written from right to left (like Hebrew or Arabic), and `ltr` for those written from left to right (like English and most other languages).

Note that text direction is usually defined within a document (e.g., with [HTML's `dir` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
) rather than through direct use of the `direction` property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#try_it)

-------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#syntax)

-------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#values)

This property is specified as one of the following keyword values:

[`ltr`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#ltr)

Text and other elements go from left to right. This is the default value.

[`rtl`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#rtl)

Text and other elements go from right to left.

For the `direction` property to have any effect on inline-level elements, the [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
 property's value must be `embed` or `override`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#description)

-----------------------------------------------------------------------------------------------------------

The property sets the base text direction of block-level elements and the direction of embeddings created by the [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
 property. It also sets the default alignment of text, block-level elements, and the direction that cells flow within a table or grid row.

Unlike the `dir` attribute in HTML, the `direction` property is not inherited from table columns into table cells, since CSS inheritance follows the document tree, and table cells are inside of rows but not inside of columns.

The `direction` and [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
 properties are the only two properties which are not affected by the [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
 shorthand property.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `ltr` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#formal_syntax)

---------------------------------------------------------------------------------------------------------------

direction =   
  ltr  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rtl    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#examples)

-----------------------------------------------------------------------------------------------------

### [Setting right-to-left direction](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#setting_right-to-left_direction)

In the example below are two strings of text, both which are displaying using `direction: rtl`. While the Arabic text is displayed correctly with this setting, the English text now has a full stop in an unusual location.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Writing Modes Level 4  <br>\# direction](https://drafts.csswg.org/css-writing-modes/#direction) |
| [Scalable Vector Graphics (SVG) 2  <br>\# DirectionProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#DirectionProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction#see_also)

-----------------------------------------------------------------------------------------------------

*   [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
    
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    
*   SVG [`direction`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/direction)
     attribute
*   The HTML [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
     global attribute
*   [Creating vertical form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls)
    
*   [Handling different text directions](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_different_text_directions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/direction/index.md?plain=1 "Folder: en-us/web/css/reference/properties/direction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fdirection&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fdirection%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fdirection%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fdirection%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8c21ceeff860d7b9f64b177115e3897543e7fcab%0A*+Document+last+modified%3A+2026-10-11T22%3A31%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")