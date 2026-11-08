*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#mdn-search)
    

`text-decoration-skip` CSS property
===================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-decoration-skip`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets what parts of an element's content any text decoration affecting the element must skip over. It controls all text decoration lines drawn by the element and also any text decoration lines drawn by its ancestors.

**Note:** Most other browsers are converging on supporting the simpler [`text-decoration-skip-ink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip-ink)
 property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#syntax)

------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#none)

Nothing is skipped. Thus, text decoration is drawn for all text content and across atomic inline-level boxes.

[`objects`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#objects)

The entire margin box of the element is skipped if it is an atomic inline such as an image or inline-block.

[`spaces`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#spaces)

All spacing is skipped: all [Unicode white space characters](https://www.unicode.org/reports/tr44/#White_Space "External link (opens in new tab)")
 and all word separators, plus any adjacent [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
 or [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
.

[`leading-spaces`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#leading-spaces)

The same as `spaces`, except that only leading spaces are skipped.

[`trailing-spaces`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#trailing-spaces)

The same as `spaces`, except that only trailing spaces are skipped.

[`edges`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#edges)

The start and end of the text decoration is inset slightly (e.g., by half of the line thickness) from the content edge of the decorating box. Thus, adjacent elements receive separate underlines. (This is important in Chinese, where underlining is a form of punctuation.)

![An example of "text-decoration-skip: edges;".](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip/decoration-skip-edges.png)

[`box-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#box-decoration)

The text decoration is skipped over the box's margin, border, and padding areas. This only has an effect on decorations imposed by an ancestor; a _decorating box_ never draws over its own box decoration.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `objects` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

text-decoration-skip =   
  none  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#examples)

----------------------------------------------------------------------------------------------------------------

### [Skipping edges](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#skipping_edges)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 4  <br>\# text-decoration-skipping](https://drafts.csswg.org/css-text-decor-4/#text-decoration-skipping) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`text-decoration-skip-ink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip-ink)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-decoration-skip/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-decoration-skip (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-skip&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-skip%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-skip%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-skip%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")