*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#mdn-search)
    

`<title>` HTML document title element
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<title>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element defines the document's title that is shown in a [browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)
's title bar or a page's tab. It only contains text; HTML tags within the element, if any, are also treated as plain text.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#attributes)

----------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#usage_notes)

------------------------------------------------------------------------------------------------------

The `<title>` element is always used within a page's [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
 block.

### [Page titles and SEO](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#page_titles_and_seo)

The contents of a page title can have significant implications for search engine optimization ([SEO](https://developer.mozilla.org/en-US/docs/Glossary/SEO)
). In general, a longer, descriptive title performs better than short or generic titles. The content of the title is one of the components used by search engine algorithms to decide the order in which to list pages in search results. Also, the title is the initial "hook" by which you grab the attention of readers glancing at the search results page.

A few guidelines and tips for composing good titles:

*   Avoid one- or two-word titles. Use a descriptive phrase, or a term-definition pairing for glossary or reference-style pages.
*   Search engines typically display about the first 55–60 characters of a page title. Text beyond that may be lost, so try not to have titles longer than that. If you must use a longer title, make sure the important parts come earlier and that nothing critical is in the part of the title that is likely to be dropped.
*   Don't use "keyword blobs." If your title is just a list of words, algorithms often reduce your page's position in the search results.
*   Try to make sure your titles are as unique as possible within your own site. Duplicate—or near-duplicate—titles can contribute to inaccurate search results.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#accessibility)

----------------------------------------------------------------------------------------------------------

It is important to provide an accurate and concise title to describe the page's purpose.

A common navigation technique for users of assistive technology is to read the page title and infer the content the page contains. This is because navigating into a page to determine its content can be a time-consuming and potentially confusing process. Titles should be unique to every page of a website, ideally surfacing the primary purpose of the page first, followed by the name of the website. Following this pattern will help ensure that the primary purpose of the page is announced by a screen reader first. This provides a far better experience than having to listen to the name of a website before the unique page title, for every page a user navigates to in the same website.

### [Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#examples)

If a form submission contains errors and the submission re-renders the current page, the title can be used to help make users aware of any errors with their submission. For instance, update the page `title` value to reflect significant page state changes (such as form validation problems).

**Note:** Presently, dynamically updating a page's title will not be automatically announced by screen readers. If you are going to update the page title to reflect significant changes to a page's state, then the use of [ARIA Live Regions](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)
 may be necessary, as well.

*   [MDN Understanding WCAG, Guideline 2.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.4_%E2%80%94_navigable_provide_ways_to_help_users_navigate_find_content_and_determine_where_they_are)
    
*   [Understanding Success Criterion 2.4.2 | W3C Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/page-titled.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#examples_2)

--------------------------------------------------------------------------------------------------

This example establishes a page whose title (as displayed at the top of the window or in the window's tab) as "Awesome interesting stuff".

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)<br>. |
| Permitted content | Text that is not inter-element [whitespace](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)<br>. |
| Tag omission | Both opening and closing tags are required. Note that leaving off `</title>` should cause the browser to ignore the rest of the page. |
| Permitted parents | A [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)<br> element that contains no other `<title>` element. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted. |
| DOM interface | [`HTMLTitleElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTitleElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-title-element](https://html.spec.whatwg.org/multipage/semantics.html#the-title-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title#see_also)

------------------------------------------------------------------------------------------------

*   SVG [`<title>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/title)
     element

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/title/index.md?plain=1 "Folder: en-us/web/html/reference/elements/title (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftitle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftitle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftitle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftitle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")