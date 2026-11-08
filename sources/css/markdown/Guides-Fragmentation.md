*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation#mdn-search)
    

CSS fragmentation
=================

The **CSS fragmentation** module defines how content is displayed when it is broken (fragmented) and flows across multiple [pages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
, regions, or [columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
. This module defines features for pagination, breaking variable fragment size and orientation, widows and orphans.

This module explains how content breaks across fragmentation containers and how such breaks can be controlled by the author. The generic term for breaking content across containers is _fragmentation_. Fragmentation occurs when an inline box wraps onto multiple lines. This can happen when using layout features such as [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
: For example, when a block spans more than one column inside a column layout container, or spans a page break when printed. Each piece of the rendering for the element is called a _fragment_.

When content is physically printed or displayed as a print preview, there are page breaks. In this paged media, as opposed to continuous media, document content can be split between one or more pages, or fragments. To avoid awkward breaks, such as halfway through a line of text or with a lone word on its own page, browsers can move content that would otherwise fall across the page break in a process is called _pagination_.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation#reference)

---------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation#properties)

*   [`box-decoration-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
    
*   [`break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after)
    
*   [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
    
*   [`break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
    
*   [`orphans`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
    
*   [`widows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows)
    

### [Glossary terms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation#glossary_terms)

*   [Fragmentainer](https://developer.mozilla.org/en-US/docs/Glossary/Fragmentainer)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation#guides)

---------------------------------------------------------------------------------------

[Handling content breaks in multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Handling_content_breaks)

Introduction to the fragmentation specification and how to control where column content breaks.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation#related_concepts)

-----------------------------------------------------------------------------------------------------------

*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    
*   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    , [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
    , and [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
     CSS properties
*   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    , [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
    , and [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
     CSS properties
*   [Block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
    

[CSS paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
 module

*   [`page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page)
    
*   [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
    

[CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
 module

*   [Principal box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model#the_principal_box)
     term
*   [Block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
     guide

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fragmentation Module Level 3](https://drafts.csswg.org/css-break/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation#see_also)

-------------------------------------------------------------------------------------------

*   [`horizontal-viewport-segments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/horizontal-viewport-segments)
     and [`vertical-viewport-segments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments)
     `@media` descriptors
*   [Viewport Segments API](https://developer.mozilla.org/en-US/docs/Web/API/Viewport_segments_API)
    
*   [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/fragmentation/index.md?plain=1 "Folder: en-us/web/css/guides/fragmentation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFragmentation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ffragmentation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFragmentation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ffragmentation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")