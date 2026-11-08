*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#mdn-search)
    

Box alignment for block, absolutely positioned, and table layouts
=================================================================

The [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
 module details how alignment works in various layout methods. In this guide, we explore how box alignment works in the context of block layout, including floated, positioned, and table elements. As this guide aims to detail things which are specific to block layout and box alignment, it should be read in conjunction with the [box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview)
 guide, which details the common features of box alignment across layout methods.

[align-content and justify-content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#align-content_and_justify-content)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 property does not apply to block containers or table cells.

The [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 property applies to the block axis in order to align the contents of the box within its container. If a content distribution method such as `space-between`, `space-around` or `space-evenly` is requested then the fallback alignment will be used, as the content is treated as a single [alignment subject](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Subject)
.

[justify-self](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#justify-self)

--------------------------------------------------------------------------------------------------------------------------

The [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 property is used to align an item inside its containing block on the inline axis.

This property does not apply to floated elements or table cells.

[align-self](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#align-self)

----------------------------------------------------------------------------------------------------------------------

The [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 property does not apply to block-level boxes (including floats), because there is more than one item in the block axis. It also does not apply to table cells.

### [Absolutely positioned elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#absolutely_positioned_elements)

The alignment container is the positioned block, accounting for the offset values of top, left, bottom, and right. The normal keyword resolves to `stretch`, unless the positioned item is a replaced element, in which case it resolves to `start`.

[Aligning in these layout methods today](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#aligning_in_these_layout_methods_today)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As we do not currently have browser support for box alignment in block layout, your options for alignment are either to use one of the existing alignment methods or, to make even a single item inside a container a flex item in order to use the alignment properties as specified in flexbox.

Alignment of blocks horizontally prior to flexbox was typically achieved by way of setting auto margins on the block. A [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 of `auto` will absorb all available space in that dimension, therefore setting a left and right margin of auto, you can push a block into the center:

In table layout, you have access to the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 property to align the contents of a cell inside that cell.

For many use cases, turning the block container into a flex item will give you the alignment capability that you are looking for. In the example below, a container with a single item inside has been turned into a flex container for the purpose of being able to use the alignment properties.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#see_also)

------------------------------------------------------------------------------------------------------------------

*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module
*   [Box alignment overview](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview)
    
*   [Box alignment in flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox)
    
*   [Box alignment in CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [Box alignment in multiple-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 20, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/box_alignment/in_block_abspos_tables/index.md?plain=1 "Folder: en-us/web/css/guides/box_alignment/in_block_abspos_tables (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_alignment%2FIn_block_abspos_tables&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbox_alignment%2Fin_block_abspos_tables%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_alignment%2FIn_block_abspos_tables%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbox_alignment%2Fin_block_abspos_tables%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca5d9f9e63b460fc0c9e15ac57d9739e10e4ea0d%0A*+Document+last+modified%3A+2025-11-20T07%3A05%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")