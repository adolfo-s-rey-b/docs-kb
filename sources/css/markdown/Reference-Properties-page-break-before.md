*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#mdn-search)
    

`page-break-before` CSS property
================================

Deprecated

Avoid using this feature in new projects. The `page-break-` alias properties exist only for backwards compatibility with pages that predate the `break-` properties. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [Page breaks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation "In printed page layouts, the break-after, break-before, break-inside CSS properties control where printed pages start and end. Also known as pagination or page breaking.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Warning:** This property has been replaced by the [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
 property.

The **`page-break-before`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property adjusts page breaks _before_ the current element.

This property applies to block elements that generate a box. It won't apply on an empty [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 that won't generate a box.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#try_it)

---------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#syntax)

---------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#auto)

Initial value. Automatic page breaks (neither forced nor forbidden).

[`always`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#always)

Always force page breaks before the element.

[`avoid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#avoid)

Avoid page breaks before the element.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#left)

Force page breaks before the element so that the next page is formatted as a left page. It's the page placed on the left side of the spine of the book or the back side of the page in duplex printing.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#right)

Force page breaks before the element so that the next page is formatted as a right page. It's the page placed on the right side of the spine of the book or the front side of the page in duplex printing.

[`recto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#recto)

If pages progress left-to-right, then this acts like `right`. If pages progress right-to-left, then this acts like `left`.

[`verso`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#verso)

If pages progress left-to-right, then this acts like `left`. If pages progress right-to-left, then this acts like `right`.

[Page break aliases](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#page_break_aliases)

---------------------------------------------------------------------------------------------------------------------------------

The `page-break-before` property is now a legacy property, replaced by [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
.

For compatibility reasons, `page-break-before` should be treated by browsers as an alias of `break-before`. This ensures that sites using `page-break-before` continue to work as designed. A subset of values should be aliased as follows:

| page-break-before | break-before |
| --- | --- |
| `auto` | `auto` |
| `left` | `left` |
| `right` | `right` |
| `avoid` | `avoid` |
| `always` | `page` |

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | block-level elements in the normal flow of the root element. User agents may also apply it to other elements like `table-row` elements. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

page-break-before =   
  auto     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  always   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inherit    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#examples)

-------------------------------------------------------------------------------------------------------------

### [Avoid a page break before an element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#avoid_a_page_break_before_an_element)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Logical Properties and Values Module Level 1  <br>\# page](https://drafts.csswg.org/css-logical/#page) |
| [CSS Fragmentation Module Level 3  <br>\# page-break-properties](https://drafts.csswg.org/css-break/#page-break-properties) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
    , [`break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after)
    , [`break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
    
*   [`page-break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-after)
    , [`page-break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside)
    
*   [`orphans`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
    , [`widows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/page-break-before/index.md?plain=1 "Folder: en-us/web/css/reference/properties/page-break-before (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpage-break-before&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpage-break-before%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpage-break-before%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpage-break-before%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")