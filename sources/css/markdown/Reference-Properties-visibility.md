*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#mdn-search)
    

`visibility` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`visibility`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property shows or hides an element without changing the layout of a document. The property can also hide rows or columns in a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
.

To both hide an element _and remove it from the document layout_, set the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to `none` instead of using `visibility`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#syntax)

--------------------------------------------------------------------------------------------------

The `visibility` property is specified as one of the keyword values listed below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#values)

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#visible)

The element box is visible.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#hidden)

The element box is invisible (not drawn), but still affects layout as normal. Descendants of the element will be visible if they have `visibility` set to `visible`. The element cannot receive focus (such as when navigating through [tab indexes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
).

[`collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#collapse)

The `collapse` keyword has different effects for different elements:

*   For [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
     rows, columns, column groups, and row groups, the row(s) or column(s) are hidden and the space they would have occupied is removed (as if ``[`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display) : none`` were applied to the column/row of the table). However, the size of other rows and columns is still calculated as though the cells in the collapsed row(s) or column(s) are present. This value allows for the fast removal of a row or column from a table without forcing the recalculation of widths and heights for the entire table.
*   Collapsed flex items and ruby annotations are hidden, and the space they would have occupied is removed.
*   For other elements, `collapse` is treated the same as `hidden`.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#accessibility)

----------------------------------------------------------------------------------------------------------------

Using a `visibility` value of `hidden` on an element will remove it from the [accessibility tree](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/What_is_accessibility#accessibility_apis)
. This will cause the element and all its descendant elements to no longer be announced by screen reading technology.

[Interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#interpolation)

----------------------------------------------------------------------------------------------------------------

When animated, visibility values are interpolated between _visible_ and _not-visible_. One of the start or ending values must therefore be `visible` or no [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 can happen. The value is interpolated as a discrete step, where values of the easing function between `0` and `1` map to `visible` and other values of the easing function (which occur only at the start/end of the transition or as a result of `cubic-bezier()` functions with y values outside of \[0, 1\]) map to the closer endpoint.

[Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#notes)

------------------------------------------------------------------------------------------------

*   Support for `visibility: collapse` is missing or partially incorrect in some modern browsers. It may not be correctly treated like `visibility: hidden` on elements other than table rows and columns.
*   When applied to table rows, if the table contains cells ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
     and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
     elements) that span both visible and collapsed rows, the cell may render in unexpected ways. If the spanning cell is defined in a collapsed row, browsers do not render the table cell, as if the cells in subsequent rows were present with `visibility: collapse` applied. When the cell is defined in a visible row and spans a collapsed row, the cell contents are not reflowed, but the presentation of the cell itself varies by browser. Most browsers reduce the block size of the cell by the block size of the hidden row. This means the contents may be larger than the cell in the block-size direction. Depending on the browser, the overflowing contents are either cropped, as if `overflow: hidden` were set, while the content bleeds into the subsequent row in other browsers as if `overflow: visible` were set. In other browsers, the cell is rendered as if the row were not collapsed, with all the other cells in the row hidden as if `visibility: collapse` were set on individual cells rather than the row itself.
*   `visibility: collapse` may change the layout of a table if the table has nested tables within the cells that are collapsed, unless `visibility: visible` is specified explicitly on nested tables.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `visible` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#formal_syntax)

----------------------------------------------------------------------------------------------------------------

visibility =   
  visible       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  force-hidden  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  collapse        

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#examples)

------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#basic_example)

#### HTML

#### CSS

### [Table example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#table_example)

#### HTML

#### CSS

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Display Module Level 3  <br>\# visibility](https://drafts.csswg.org/css-display/#visibility) |
| [Scalable Vector Graphics (SVG) 2  <br>\# VisibilityControl](https://w3c.github.io/svgwg/svg2-draft/render.html#VisibilityControl) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#see_also)

------------------------------------------------------------------------------------------------------

*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    
*   SVG [`visibility`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/visibility)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/visibility/index.md?plain=1 "Folder: en-us/web/css/reference/properties/visibility (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fvisibility&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fvisibility%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fvisibility%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fvisibility%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")