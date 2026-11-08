*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#mdn-search)
    

`<content-distribution>` CSS type
=================================

The **`<content-distribution>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 value type is used by [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 and [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 properties, and the [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
 shorthand, to distribute a container's extra space among its [alignment subjects](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Subject)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#syntax)

--------------------------------------------------------------------------------------------------------

<content-distribution> = space-between | space-around | space-evenly | stretch

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#values)

--------------------------------------------------------------------------------------------------------

The following keyword values are represented by the `<content-distribution>` grammar term:

[`space-between`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#space-between)

Evenly distributes the [alignment subject](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Subject)
 within the [alignment container](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Container)
. The first item is placed flush with the start edge of the alignment container, the last item subject is placed flush with the end edge of the alignment container, and the remaining items are evenly distributed so that the spacing between any two adjacent items is the same. The default fallback alignment for `space-between` is `safe flex-start` for flex layout, and `start` otherwise. If there is only one item, the item will be flush with the start edge.

[`space-around`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#space-around)

The items are evenly distributed in the container, with a half-size space on either end. The spacing between any two adjacent items is the same, and the spacing before the first and after the last items is half the size of the other spacing. The default fallback alignment for `space-around` is `safe center`. If the container has only one child, the item will be centered.

[`space-evenly`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#space-evenly)

The items are evenly distributed in the container, with a full-size space on either end. The spacing between any two adjacent items, before the first item, and after the last item, are all the same. The default fallback alignment for `space-evenly` is `safe center`. If the container has only one child, the item will be centered.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#stretch)

If the combined size of the items is less than the size of the container, any items that can grow will have their size increased equally (not proportionally), while still respecting the constraints imposed by [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
, [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
, or equivalent functionality, so that the combined size of the items exactly fills the container. The default fallback alignment for `stretch` is `flex-start` in flexbox, and `start` in other layout modes. If there is only one item, and that item can grow, it will grow to fill the container.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# typedef-content-distribution](https://drafts.csswg.org/css-align/#typedef-content-distribution) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution#see_also)

------------------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    , [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    , [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
    
*   Other box alignment data types: [`<baseline-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
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

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/content-distribution/index.md?plain=1 "Folder: en-us/web/css/reference/values/content-distribution (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcontent-distribution&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcontent-distribution%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcontent-distribution%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcontent-distribution%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")