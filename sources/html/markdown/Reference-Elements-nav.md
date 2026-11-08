*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#mdn-search)
    

`<nav>` HTML navigation section element
=======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<nav>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#try_it)

------------------------------------------------------------------------------------------

    <nav class="crumbs">
      <ol>
        <li class="crumb"><a href="#">Bikes</a></li>
        <li class="crumb"><a href="#">BMX</a></li>
        <li class="crumb">Jump Bike 3000</li>
      </ol>
    </nav>
    
    <h1>Jump Bike 3000</h1>
    <p>
      This BMX bike is a solid step into the pro world. It looks as legit as it
      rides and is built to polish your skills.
    </p>
    

    nav {
      border-bottom: 1px solid black;
    }
    
    .crumbs ol {
      list-style-type: none;
      padding-left: 0;
    }
    
    .crumb {
      display: inline-block;
    }
    
    .crumb a::after {
      display: inline-block;
      color: black;
      content: ">";
      font-size: 80%;
      font-weight: bold;
      padding: 0 3px;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#attributes)

--------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#usage_notes)

----------------------------------------------------------------------------------------------------

*   It's not necessary for all links to be contained in a `<nav>` element. `<nav>` is intended only for a major block of navigation links; typically the [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
     element often has a list of links that don't need to be in a `<nav>` element.
*   A document may have several `<nav>` elements, for example, one for site navigation and one for intra-page navigation. [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby)
     can be used in such case to promote accessibility, see [example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#labeling_section_content)
    .
*   User agents, such as screen readers targeting disabled users, can use this element to determine whether to omit the initial rendering of navigation-only content.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#examples)

----------------------------------------------------------------------------------------------

In this example, a `<nav>` block is used to contain an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) of links. With appropriate CSS, this can be presented as a sidebar, navigation bar, or drop-down menu.

html

    <nav class="menu">
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    

The semantics of the `nav` element is that of providing links. However a `nav` element doesn't have to contain a list, it can contain other kinds of content as well. In this navigation block, links are provided in prose:

html

    <nav>
      <h2>Navigation</h2>
      <p>
        You are on my home page. To the north lies <a href="/blog">my blog</a>, from
        whence the sounds of battle can be heard. To the east you can see a large
        mountain, upon which many <a href="/school">school papers</a> are littered.
        Far up this mountain you can spy a little figure who appears to be me,
        desperately scribbling a <a href="/school/thesis">thesis</a>.
      </p>
      <p>
        To the west are several exits. One fun-looking exit is labeled
        <a href="https://games.example.com/">"games"</a>. Another more
        boring-looking exit is labeled <a href="https://isp.example.net/">ISP™</a>.
      </p>
      <p>
        To the south lies a dark and dank <a href="/about">contacts page</a>.
        Cobwebs cover its disused entrance, and at one point you see a rat run
        quickly out of the page.
      </p>
    </nav>
    

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#sectioning_content)<br>, palpable content. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | `[navigation](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/navigation_role) ` |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-nav-element](https://html.spec.whatwg.org/multipage/sections.html#the-nav-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav#see_also)

----------------------------------------------------------------------------------------------

*   Other section-related elements: [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
    , [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
    , [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    , [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
    , [h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h2](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h3](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h4](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h5](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h6](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [`<hgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup)
    , [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
    , [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    , [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
    ;
*   [Sections and outlines of an HTML document](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    .
*   [ARIA: Navigation role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/navigation_role)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/nav/index.md?plain=1 "Folder: en-us/web/html/reference/elements/nav (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fnav&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fnav%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fnav%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fnav%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")