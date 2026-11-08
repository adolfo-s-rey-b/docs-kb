*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Pagination#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Pagination#mdn-search)
    

Pagination
==========

This cookbook pattern demonstrates the navigation pattern used to display pagination, where the user can move between pages of content such as search results.

![Links to sets of pages in a paged listing](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Pagination/pagination.png)

[Requirements](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Pagination#requirements)

----------------------------------------------------------------------------------------------------------------

The pagination pattern typically displays items in a row. To ensure that the pagination is understandable by people using a screen reader, we mark the items up as a list inside a [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
 element, and then use CSS to display the layout visually as a row.

Typically, the pagination component will be centered horizontally underneath the content.

[Recipe](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Pagination#recipe)

----------------------------------------------------------------------------------------------------

Click "Play" in the code blocks below to edit the example in the MDN Playground:

[Choices made](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Pagination#choices_made)

----------------------------------------------------------------------------------------------------------------

This pattern is laid out using [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 — one flex container nested inside another. The [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
 element is designated a flex container in order that we can center the list inside using the [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 property.

The list itself also becomes a flex container to lay the items out as a row. To space the items out we can either use a [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 on the flex items or add a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 on the flex container.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Pagination#accessibility_concerns)

------------------------------------------------------------------------------------------------------------------------------------

We want to ensure that a person using a screen reader understands what this navigation does, and where they will go when clicking a link. To help with this we have added [`aria-label="pagination"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
 on the `<nav>` element.

We have also added some additional content that would be read by a screen reader but is hidden visually, and set the [`aria-hidden`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-hidden)
 attribute on the paging arrows.

The "See Also" section at the end of this document has links to related accessibility topics.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Pagination#see_also)

--------------------------------------------------------------------------------------------------------

*   [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    , [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
    
*   [Know your ARIA: 'hidden' vs 'none'](https://www.scottohara.me/blog/2018/05/05/hidden-vs-none.html "External link (opens in new tab)")
     (2018)
*   [Invisible content just for screen reader users](https://webaim.org/techniques/css/invisiblecontent/#techniques "External link (opens in new tab)")
     via WebAIM.org (2020)
*   [Writing CSS with accessibility in mind](https://medium.com/@matuzo/writing-css-with-accessibility-in-mind-8514a0007939 "External link (opens in new tab)")
     (2017)
*   [a11y style guide: pagination](https://a11y-style-guide.com/style-guide/section-navigation.html#kssref-navigation-pagination "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Pagination/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/how_to/layout_cookbook/pagination/index.md?plain=1 "Folder: en-us/web/css/how_to/layout_cookbook/pagination (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FPagination&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fpagination%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FPagination%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fpagination%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")