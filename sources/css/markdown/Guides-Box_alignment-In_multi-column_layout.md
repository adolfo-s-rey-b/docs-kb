*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout#mdn-search)
    

Box alignment in multi-column layout
====================================

The [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
 module details how alignment works in various layout methods; in this guide, we explore how box alignment works in the context of [multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
. As this guide aims to detail things that are specific to both modules, it should be read in conjunction with the [box alignment overview](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview)
 guide, which details the common features of box alignment across layout methods.

In [multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts)
, the [alignment container](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Container)
 is the content box of the multicol container. The [alignment subject](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Subject)
 is the column box. The properties which apply to multi-column layouts are detailed below.

[align-content and justify-content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout#align-content_and_justify-content)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 property applies to the block axis and [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 to the inline axis. Any spacing added to the columns due to use of space distribution will be added to the gap between the columns, therefore making the gap larger than might be specified by the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 (or [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 shorthand) property.

Using a value of `justify-content` other than `normal` or `stretch` will cause column boxes to display at the [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 specified on the multicol container, and the remaining space distributed according to the value of `justify-content`.

[column-gap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout#column-gap)

----------------------------------------------------------------------------------------------------------------------

The [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 property was originally specified in the multiple-column layout specification and then later unified with the gap properties for other layout methods in box alignment. While other layout methods treat the initial value of `column-gap` as `0`, multi-column layout treats it as `1em` — you generally want a gap between columns.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout#see_also)

------------------------------------------------------------------------------------------------------------------

*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module
*   [Box alignment overview](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview)
    
*   [Box alignment in flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [Box alignment for block, absolutely positioned, and table layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 20, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/box_alignment/in_multi-column_layout/index.md?plain=1 "Folder: en-us/web/css/guides/box_alignment/in_multi-column_layout (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_alignment%2FIn_multi-column_layout&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbox_alignment%2Fin_multi-column_layout%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_alignment%2FIn_multi-column_layout%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbox_alignment%2Fin_multi-column_layout%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca5d9f9e63b460fc0c9e15ac57d9739e10e4ea0d%0A*+Document+last+modified%3A+2025-11-20T07%3A05%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")