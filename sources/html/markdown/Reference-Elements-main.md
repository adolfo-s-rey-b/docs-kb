*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#mdn-search)
    

`<main>` HTML main element
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<main>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents the dominant content of the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#try_it)

-------------------------------------------------------------------------------------------

    <header>Gecko facts</header>
    
    <main>
      <p>
        Geckos are a group of usually small, usually nocturnal lizards. They are
        found on every continent except Antarctica.
      </p>
    
      <p>
        Many species of gecko have adhesive toe pads which enable them to climb
        walls and even windows.
      </p>
    </main>
    

    header {
      font:
        bold 7vw "Arial",
        sans-serif;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#attributes)

---------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#usage_notes)

-----------------------------------------------------------------------------------------------------

A document mustn't have more than one `<main>` element that doesn't have the [`hidden`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden)
 attribute specified.

The content of a `<main>` element should be unique to the document. Content that is repeated across a set of documents or document sections such as sidebars, navigation links, copyright information, site logos, and search forms shouldn't be included unless the search form is the main function of the page.

`<main>` doesn't contribute to the document's outline; that is, unlike elements such as [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
, headings such as [h2](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
, and such, `<main>` doesn't affect the [DOM's](https://developer.mozilla.org/en-US/docs/Glossary/DOM)
 concept of the structure of the page. It's strictly informative.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#accessibility)

---------------------------------------------------------------------------------------------------------

### [Landmark](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#landmark)

The `<main>` element behaves like a [`main` landmark](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/main_role)
 role. [Landmarks](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Techniques#landmark_roles)
 can be used by assistive technology to quickly identify and navigate to large sections of the document. Prefer using the `<main>` element over declaring `role="main"`, unless there are [legacy browser support concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#browser_compatibility)
.

### [Skip navigation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#skip_navigation)

Skip navigation, also known as "skipnav", is a technique that allows an assistive technology user to quickly bypass large sections of repeated content (main navigation, info banners, etc.). This lets the user access the main content of the page faster.

Adding an [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attribute to the `<main>` element lets it be a target of a skip navigation link.

html

    <body>
      <a href="#main-content">Skip to main content</a>
    
      <!-- navigation and header content -->
    
      <main id="main-content">
        <!-- main page content -->
      </main>
    </body>
    

*   [WebAIM: "Skip Navigation" Links](https://webaim.org/techniques/skipnav/ "External link (opens in new tab)")
    

### [Reader mode](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#reader_mode)

Browser reader mode functionality looks for the presence of the `<main>` element, as well as [heading](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 and [content sectioning elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#content_sectioning)
 when converting content into a specialized reader view.

*   [Building websites for Safari Reader Mode and other reading apps.](https://medium.com/@mandy.michael/building-websites-for-safari-reader-mode-and-other-reading-apps-1562913c86c9 "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#examples)

-----------------------------------------------------------------------------------------------

html

    <!-- other content -->
    
    <main>
      <h1>Apples</h1>
      <p>The apple is the pomaceous fruit of the apple tree.</p>
    
      <article>
        <h2>Red Delicious</h2>
        <p>
          These bright red apples are the most common found in many supermarkets.
        </p>
        <p>…</p>
        <p>…</p>
      </article>
    
      <article>
        <h2>Granny Smith</h2>
        <p>These juicy, green apples make a great filling for apple pies.</p>
        <p>…</p>
        <p>…</p>
      </article>
    </main>
    
    <!-- other content -->
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, palpable content. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Tag omission | None; both the starting and ending tags are mandatory. |
| Permitted parents | Where [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br> is expected, but only if it is a [hierarchically correct `main` element](https://html.spec.whatwg.org/multipage/grouping-content.html#hierarchically-correct-main-element "External link (opens in new tab)")<br>. |
| Implicit ARIA role | `[main](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/main_role) ` |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-main-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main#see_also)

-----------------------------------------------------------------------------------------------

*   Basic structural elements: [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
    , [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
    , [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
    
*   Section-related elements: [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
    , [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
    , [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    , [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
    , or [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
    
*   [ARIA: Main role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/main_role)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/main/index.md?plain=1 "Folder: en-us/web/html/reference/elements/main (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmain&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmain%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmain%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmain%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F100cf25d92d3953f3c70ecaa2af637d5e42179d8%0A*+Document+last+modified%3A+2026-09-10T17%3A31%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")