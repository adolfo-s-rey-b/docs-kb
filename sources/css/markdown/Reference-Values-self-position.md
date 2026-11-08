*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#mdn-search)
    

`<self-position>` CSS type
==========================

The **`<self-position>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 value data type is used by the [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 and [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 properties, and the [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
 shorthand, to align the box within its alignment container. It is also used by the [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
 and [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 properties, and the [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
 shorthand, to specify default values for `justify-self` and `align-self`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#syntax)

-------------------------------------------------------------------------------------------------

<self-position> = center | start | end | self-start | self-end | flex-start | flex-end

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#values)

-------------------------------------------------------------------------------------------------

The following keyword values are represented by the `<self-position>` grammar term:

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#center)

Centers the [alignment subject](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Subject)
 within its [alignment container](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Container)
.

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#start)

Aligns the alignment subject flush with the alignment container's start edge.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#end)

Aligns the alignment subject flush with the alignment container's end edge.

[`self-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#self-start)

Aligns the alignment subject flush with the edge of the alignment container corresponding to the alignment subject's start side.

[`self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#self-end)

Aligns the alignment subject flush with the edge of the alignment container corresponding to the alignment subject's end side.

[`flex-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#flex-start)

In flex layout, aligns the alignment subject flush with the edge of the alignment container corresponding to the flex container's main-start or cross-start side, as appropriate. It is identical to `start` for layout modes other than flex layout.

[`flex-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#flex-end)

In flex layout, aligns the alignment subject flush with the edge of the alignment container corresponding to the flex container's main-end or cross-end side, as appropriate. Identical to `end` for layout modes other than flex layout.

**Note:** The `left` and `right` keywords are excluded from `<self-position>`, despite being valid positional alignment values for the `justify-*` properties ([`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
, [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
, and [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
), because they are not allowed in the `align-*` properties ([`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
, [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
, and [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
). They are instead explicitly included in the `justify-*` properties' grammars.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# typedef-self-position](https://drafts.csswg.org/css-align/#typedef-self-position) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position#see_also)

-----------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    , [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    , [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
    , [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    , [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    , [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
    
*   Other box alignment data types: [`<baseline-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
    , [`<content-distribution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution)
    , [`<overflow-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position)
    , and [`<content-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-position)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/self-position/index.md?plain=1 "Folder: en-us/web/css/reference/values/self-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fself-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fself-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fself-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fself-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")