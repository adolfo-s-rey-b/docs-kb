*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#mdn-search)
    

`<relative-size>` CSS type
==========================

The **`<relative-size>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 describes relative size keywords. The `<relative-size>` keywords define a size relative to the computed size of the parent element. This data type is used in the [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 shorthand and [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 properties.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#syntax)

-------------------------------------------------------------------------------------------------

<relative-size> = smaller | larger

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#values)

The `<relative-size>` data type is defined using a keyword value chosen from the list below.

[`smaller`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#smaller)

A relative size one size smaller than the inherited size.

[`larger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#larger)

A relative size one size larger than the inherited size.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#description)

-----------------------------------------------------------------------------------------------------------

The `<relative-size>` keywords are relative to the current size of the element. If the inherited size is defined using an [`<absolute-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/absolute-size)
 keyword, the `<relative-size>` value equates to the adjacent size in the [`<absolute-size>` table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/absolute-size#description)
. Otherwise, the relative increase or decrease in size is between 120% and 150%.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#examples)

-----------------------------------------------------------------------------------------------------

### [Comparing the keyword values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#comparing_the_keyword_values)

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# valdef-font-size-relative-size](https://drafts.csswg.org/css-fonts/#valdef-font-size-relative-size) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size#see_also)

-----------------------------------------------------------------------------------------------------

*   CSS [`<absolute-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/absolute-size)
     data type
*   CSS [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
     and [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
     properties
*   [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/relative-size/index.md?plain=1 "Folder: en-us/web/css/reference/values/relative-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frelative-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frelative-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frelative-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frelative-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")