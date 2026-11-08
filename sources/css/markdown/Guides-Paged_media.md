*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#mdn-search)
    

CSS paged media
===============

The **CSS paged media** module defines the properties that control the presentation of content for print or any other media that splits content into discrete pages. It allows you to set page breaks, control printable areas, and style left and right pages differently.

The CSS paged media module specifies how pages are generated and laid out to hold fragmented content in a paged presentation, including content that is printed or represented as a print preview. The module defines functionality for controlling page margins, size, orientation, and headers and footers. It extends [generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
 to provide functionality for generating page numbers and running headers and footers.

The process of paginating content into generated pages and controlling breaks inside elements is covered in the [CSS fragmentation module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation)
.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#reference)

-------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#properties)

*   [`page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page)
    

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#at-rules_and_descriptors)

*   [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
    *   [`page-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation)
         descriptor
    *   [`size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size)
         descriptor
    *   [Margin descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
        
*   [Margin at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#margin_at-rules)
    

The CSS paged media module also introduces the `bleeds` and `marks` descriptors of the `@page` at-rule. Currently, no browsers support these features.

### [Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#selectors)

*   [`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)
    
*   [`:first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first)
    
*   [`:left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left)
    
*   [`:right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#guides)

-------------------------------------------------------------------------------------

[Printing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing)

Tips and techniques for helping improve web content printer output.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#related_concepts)

---------------------------------------------------------------------------------------------------------

*   [CSS fragmentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation)
     module
    *   [`break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after)
         property
    *   [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
         property
    *   [`break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
         property
    *   [`orphans`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
         property
    *   [`widows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows)
         property

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#specifications)

-----------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Paged Media Module Level 3](https://drafts.csswg.org/css-page/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media#see_also)

-----------------------------------------------------------------------------------------

*   [CSS fragmentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation)
     module
*   [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/paged_media/index.md?plain=1 "Folder: en-us/web/css/guides/paged_media (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPaged_media&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fpaged_media%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPaged_media%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fpaged_media%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F74d9a1227d110a152bf4d68f5d5f753e723ea01b%0A*+Document+last+modified%3A+2026-05-26T15%3A07%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")