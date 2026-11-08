*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#mdn-search)
    

`<hgroup>` HTML heading group element
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<hgroup>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a heading and related content. It groups a single [`<h1>–<h6>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 element with one or more [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#try_it)

---------------------------------------------------------------------------------------------

    <hgroup>
      <h1>Frankenstein</h1>
      <p>Or: The Modern Prometheus</p>
    </hgroup>
    <p>
      Victor Frankenstein, a Swiss scientist, has a great ambition: to create
      intelligent life. But when his creature first stirs, he realizes he has made a
      monster. A monster which, abandoned by his master and shunned by everyone who
      sees it, follows Dr Frankenstein to the very ends of the earth.
    </p>
    

    hgroup {
      text-align: right;
      padding-right: 16px;
      border-right: 10px solid #00c8d7;
    }
    
    hgroup h1 {
      margin-bottom: 0;
    }
    
    hgroup p {
      margin: 0;
      font-weight: bold;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#attributes)

-----------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#usage_notes)

-------------------------------------------------------------------------------------------------------

The `<hgroup>` element allows the grouping of a heading with any secondary content, such as subheadings, an alternative title, or tagline. Each of these types of content represented as a `<p>` element within the `<hgroup>`.

The `<hgroup>` itself has no impact on the document outline of a web page. Rather, the single allowed heading within the `<hgroup>` contributes to the document outline.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#examples)

-------------------------------------------------------------------------------------------------

html

    <!doctype html>
    <title>HTML Standard</title>
    <body>
      <hgroup id="document-title">
        <h1>HTML: Living Standard</h1>
        <p>Last Updated 12 July 2022</p>
      </hgroup>
      <p>Some intro to the document.</p>
      <h2>Table of contents</h2>
      <ol id="toc">
        …
      </ol>
      <h2>First section</h2>
      <p>Some intro to the first section.</p>
    </body>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, heading content, palpable content. |
| Permitted content | Zero or more [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)<br> elements, followed by one [h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h2](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h3](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h4](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h5](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, or [h6](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br> element, followed by zero or more [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)<br> elements. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | `[group](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-hgroup-element](https://html.spec.whatwg.org/multipage/sections.html#the-hgroup-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup#see_also)

-------------------------------------------------------------------------------------------------

*   Others section-related elements: [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
    , [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
    , [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    , [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
    , [h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h2](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h3](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h4](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h5](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h6](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
    , [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
    , [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    , [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
    ;
*   [Sections and outlines of an HTML document](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/hgroup/index.md?plain=1 "Folder: en-us/web/html/reference/elements/hgroup (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fhgroup&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fhgroup%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fhgroup%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fhgroup%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")