*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#mdn-search)
    

CSS box alignment
=================

The **CSS box alignment** module specifies CSS features relating to the alignment of boxes within their containers. It defines the alignment of the various CSS box layout models including block layout, table layout, flexible box layout (flexbox), and grid layout, creating a consistent alignment method across all of CSS.

The module details alignment terminology, enabling alignment properties to be used in multiple layout modules, rather than limited to a particular layout method.

Alignment is linked to writing modes in that when we align an item we do not consider whether we are aligning it to the physical dimensions of top, right, bottom, and left. Instead, we describe alignment in terms of the start and end of the particular dimension we are working with. This ensures that alignment works in the same way whichever writing mode the document has.

The alignment of text and inline-level content is defined in [CSS text module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
 and [CSS inline module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout)
, respectively.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#reference)

---------------------------------------------------------------------------------------------

### [CSS Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#css_properties)

*   [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    
*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    
*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    
*   [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    
*   [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    
*   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    
*   [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
    
*   [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
    
*   [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
    

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#data_types)

*   [`<baseline-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
    
*   [`<content-distribution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution)
    
*   [`<content-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-position)
    
*   [`<overflow-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position)
    
*   [`<self-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position)
    

### [Terms and definitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#terms_and_definitions)

*   [Alignment container](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Container)
    
*   [Alignment subject](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Subject)
    
*   [Baseline alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview#baseline_alignment)
    
*   [Distributed alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview#distributed_alignment)
    
*   [Fallback alignment](https://developer.mozilla.org/en-US/docs/Glossary/Fallback_Alignment)
    
*   [Positional alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview#positional_alignment)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#guides)

---------------------------------------------------------------------------------------

[Box alignment overview](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview)

Overview of the general concepts found in the CSS box alignment module.

[Box alignment in flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox)

How box alignment works in the context of flexbox.

[Box alignment in CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)

How box alignment works in the context of grid layout.

[Box alignment in multiple-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout)

How box alignment works in the context of multi-column layout.

[Box alignment for block, absolutely positioned and table layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables)

How box alignment works in the context of block layout, including floated, positioned, and table elements.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#related_concepts)

-----------------------------------------------------------------------------------------------------------

*   [`alignment-baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline)
    
*   [`dominant-baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline)
    
*   [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
    
*   SVG [`dominant-baseline`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/dominant-baseline)
     attribute
*   [Cross axis](https://developer.mozilla.org/en-US/docs/Glossary/Cross_Axis)
    
*   [Main axis](https://developer.mozilla.org/en-US/docs/Glossary/Main_Axis)
    

[CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
 module

*   [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
    
*   [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
    
*   [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3](https://drafts.csswg.org/css-align/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#see_also)

-------------------------------------------------------------------------------------------

*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
     module
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/box_alignment/index.md?plain=1 "Folder: en-us/web/css/guides/box_alignment (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_alignment&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbox_alignment%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_alignment%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbox_alignment%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F53745a2089268ce62bf79695d7d347bcbd0abe57%0A*+Document+last+modified%3A+2026-06-18T15%3A19%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")