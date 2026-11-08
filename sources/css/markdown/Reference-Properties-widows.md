*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#mdn-search)
    

`widows` CSS property
=====================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/11)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`widows`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the minimum number of lines in a block container that must be shown at the _top_ of a [page](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
, region, or [column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
.

In typography, a _widow_ is the last line of a paragraph that appears alone at the top of a page. (The paragraph is continued from a prior page.)

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#syntax)

----------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#values)

This property is specified as one `<integer>`:

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

The minimum number of lines that can stay by themselves at the top of a new fragment after a fragmentation break. The value must be positive.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#formal_definition)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `2` |
| Applies to | block container elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#formal_syntax)

------------------------------------------------------------------------------------------------------------

widows =   
  <integer \[1,∞\]>    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#examples)

--------------------------------------------------------------------------------------------------

### [Controlling column widows](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#controlling_column_widows)

This example uses a checkbox to switch `widows` between `2` and `1`. With `widows: 2`, at least two lines of a paragraph must appear at the top of a column. With `widows: 1`, the paragraph can be broken anywhere.

#### HTML

#### CSS

#### Result

In Firefox, which does not support `widows`, the behavior in this example is essentially equivalent to `widows: 1`, regardless of the checkbox state. The following screenshot shows the result with `widows: 2` in a supporting browser:

![Three paragraphs in three columns. The second paragraph spans the first and second columns. The third paragraph has two lines at the bottom of the second column and two lines at the top of the third column.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows/with-widows.png)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fragmentation Module Level 3  <br>\# widows-orphans](https://drafts.csswg.org/css-break/#widows-orphans) |
| [CSS Multi-column Layout Module Level 1  <br>\# filling-columns](https://drafts.csswg.org/css-multicol/#filling-columns) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows#see_also)

--------------------------------------------------------------------------------------------------

*   [`orphans`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
    
*   [Paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/widows/index.md?plain=1 "Folder: en-us/web/css/reference/properties/widows (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwidows&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwidows%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwidows%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwidows%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe4ed2e4bfb88dab98ae65c44c134e3359b623d9b%0A*+Document+last+modified%3A+2026-09-11T09%3A37%3A43.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")