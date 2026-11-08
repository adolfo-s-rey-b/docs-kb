*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#mdn-search)
    

`<baseline-position>` CSS type
==============================

The **`<baseline-position>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 value type represents the `baseline` keyword values and `first` and `last` modifiers, used for the [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
, [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
, [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
, [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
 and [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 properties as well as the [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
, [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
, and [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
 shorthand properties.

The `first` and `last` values give a box a baseline alignment preference, defaulting to `first` if the modifier is omitted.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#syntax)

-----------------------------------------------------------------------------------------------------

<baseline-position> = \[ first | last \]? && baseline

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#values)

-----------------------------------------------------------------------------------------------------

The `<baseline-position>` enumerated value type is specified using an optional `first` or `last` modifier with the `baseline` value. If a box does not belong to a shared alignment context, then the fallback alignment is used. The fallback alignment is also used to align the baseline-sharing group within its [alignment container](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Container)
.

[`baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#baseline)

Computes to `first baseline`, as defined below.

[`first baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#first_baseline)

Aligns the alignment baseline of the box's first baseline set with the corresponding baseline of its baseline-sharing group. The fallback alignment is `safe self-start` for self-alignment or `safe start` for content distribution.

[`last baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#last_baseline)

Aligns the alignment baseline of the box's last baseline set with the corresponding baseline of its baseline-sharing group. The fallback alignment is `safe self-end` for self-alignment or `safe end` for content distribution.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# typedef-baseline-position](https://drafts.csswg.org/css-align/#typedef-baseline-position) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position#see_also)

---------------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    , [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    , [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    , [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    , [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    , [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
    , [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
    , and [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
    
*   Other box alignment data types: [`<content-distribution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution)
    , [`<content-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-position)
    , [`<overflow-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position)
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

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/baseline-position/index.md?plain=1 "Folder: en-us/web/css/reference/values/baseline-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbaseline-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbaseline-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbaseline-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbaseline-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")