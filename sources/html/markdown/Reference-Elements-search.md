*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#mdn-search)
    

`<search>` HTML generic search element
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<search>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is a container representing the parts of the document or application with form controls or other content related to performing a search or filtering operation. The `<search>` element semantically identifies the purpose of the element's contents as having search or filtering capabilities. The search or filtering functionality can be for the website or application, the current web page or document, or the entire Internet or subsection thereof.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#attributes)

-----------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#usage_notes)

-------------------------------------------------------------------------------------------------------

The `<search>` element is not for presenting search results. Rather, search or filtered results should be presented as part of the main content of that web page. That said, suggestions and links that are part of "quick search" functionality within the search or filtering functionality are appropriately nested within the contents of the `<search>` element as they are search features.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#accessibility)

-----------------------------------------------------------------------------------------------------------

The `<search>` element defines a [`search`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/search_role)
 landmark. This removes the need for adding `role=search` to a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#examples)

-------------------------------------------------------------------------------------------------

### [Header search form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#header_search_form)

This example demonstrates the use of `<search>` as the container for a search within a website header to perform a site-wide search. The `<search>` is a semantic container for the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 that submits the user-entered search query to a server.

#### HTML

html

    <header>
      <h1>Movie website</h1>
      <search>
        <form action="./search/">
          <label for="movie">Find a Movie</label>
          <input type="search" id="movie" name="q" />
          <button type="submit">Search</button>
        </form>
      </search>
    </header>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

#### Result

### [Web app search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#web_app_search)

This example demonstrates potential DOM content when dynamically including JavaScript search functionality in a web application. When search functionality is implemented entirely with JavaScript, if no form is submitted, neither a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element nor a submit [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 is required. For semantics, the `<search>` element is included to contain the search and filtering capabilities.

#### HTML

html

    <search>
      <label>
        Find and filter your query
        <input type="search" id="query" />
      </label>
      <label>
        <input type="checkbox" id="exact-only" />
        Exact matches only
      </label>
    
      <section>
        <h3>Results:</h3>
        <ul id="results">
          <!-- search result content -->
        </ul>
        <output id="no-results">
          <!-- no results content -->
        </output>
      </section>
    </search>
    

#### Result

**Note:** Remember that some users don't have JavaScript, and none of your users have JavaScript running until the JavaScript is successfully downloaded, parsed, and executed. Ensure your users can access the content of your site with JavaScript disabled.

### [Multiple searches](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#multiple_searches)

This example demonstrates a page with two search features. The first is a global site search located on the header. The second is a search and filter based on the page context, in our example a car search.

#### HTML

html

    <body>
      <header>
        <h1>Car rental agency</h1>
        <search title="Website">...</search>
      </header>
      <main>
        <h2>Cars available for rent</h2>
        <search title="Cars">
          <h3>Filter results</h3>
          ...
        </search>
        <article>
          <!-- search result content -->
        </article>
      </main>
    </body>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Implicit ARIA role | `[search](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/search_role) ` |
| Permitted ARIA roles | [`form`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/form_role)<br>, [`group`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br>, [`region`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/region_role)<br>, [`search`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/search_role) |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-search-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-search-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search#see_also)

-------------------------------------------------------------------------------------------------

*   Other search-related elements: [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
    , [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    , [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
    , [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
    , [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
    
*   [ARIA: Search role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/search_role)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/search/index.md?plain=1 "Folder: en-us/web/html/reference/elements/search (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsearch&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsearch%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsearch%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsearch%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")