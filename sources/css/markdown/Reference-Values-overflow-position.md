*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position#mdn-search)
    

`<overflow-position>` CSS type
==============================

The **`<overflow-position>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 value type defines how an alignment subject that is larger than its alignment container will overflow that container. For example, if centered items are wider than their container, the overflow may be displayed beyond the viewport's start edge, which can't be scrolled to. The `<overflow-position>` value defines whether the alignment mode should be overridden to ensure the content is visible (`safe`) or if the alignment mode must be adhered to (`unsafe`).

This data type is valid for the [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
, [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
, [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
, [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
 and [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 properties as well as the [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
, [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
, and [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
 shorthand properties. If omitted, the default overflow alignment is a blend of `safe` and `unsafe`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position#syntax)

-----------------------------------------------------------------------------------------------------

<overflow-position> = unsafe | safe

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position#values)

-----------------------------------------------------------------------------------------------------

The following keyword values are represented by the `<overflow-position>` grammar term:

[`safe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position#safe)

If the size of the [alignment subject](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Subject)
 overflows the [alignment container](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Container)
, the alignment subject is instead aligned as if the alignment mode were `start`.

[`unsafe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position#unsafe)

Regardless of the relative sizes of the alignment subject and alignment container, the given alignment value is honored.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# typedef-overflow-position](https://drafts.csswg.org/css-align/#typedef-overflow-position) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position#see_also)

---------------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    , [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    , [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    , [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
     [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    , [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    , [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
    , [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
    , and [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
    
*   Other box alignment data types: [`<content-distribution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution)
    , [`<content-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-position)
    , [`<baseline-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
    , and [`<self-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/overflow-position/index.md?plain=1 "Folder: en-us/web/css/reference/values/overflow-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Foverflow-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Foverflow-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Foverflow-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Foverflow-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")