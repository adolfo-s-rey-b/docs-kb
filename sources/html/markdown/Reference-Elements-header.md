*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#mdn-search)
    

`<header>` HTML header element
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<header>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#try_it)

---------------------------------------------------------------------------------------------

    <header>
      <a class="logo" href="#">Cute Puppies Express!</a>
    </header>
    
    <article>
      <header>
        <h1>Beagles</h1>
        <time>08.12.2014</time>
      </header>
      <p>
        I love beagles <em>so</em> much! Like, really, a lot. They're adorable and
        their ears are so, so snugly soft!
      </p>
    </article>
    

    .logo {
      background: left / cover
        url("/shared-assets/images/examples/puppy-header.jpg");
      display: flex;
      height: 120px;
      align-items: center;
      justify-content: center;
      font:
        bold calc(1em + 2 * (100vw - 120px) / 100) "Dancing Script",
        fantasy;
      color: #ff0083;
      text-shadow: black 2px 2px 0.2rem;
    }
    
    header > h1 {
      margin-bottom: 0;
    }
    
    header > time {
      font: italic 0.7rem sans-serif;
    }
    

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#usage_notes)

-------------------------------------------------------------------------------------------------------

When not nested within [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#sectioning_content)
, [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
, or an element with the same ARIA role as these elements' implicit ARIA role, then the `<header>` element has an identical meaning to the site-wide [`banner`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/banner_role)
 landmark role. It defines a global site header, which usually includes a logo, company name, search feature, and possibly the global navigation or a slogan. It is generally located at the top of the page.

Otherwise, when nested within said elements, it loses its landmark status and represents a group of introductory or navigational aids for the surrounding section. It usually contains the surrounding section's heading (an `h1` – `h6` element) and optional subheading, but this is **not** required.

### [Historical Usage](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#historical_usage)

The `<header>` element originally existed at the very beginning of HTML for headings. It is seen in [the very first website](https://info.cern.ch/ "External link (opens in new tab)")
. At some point, headings became [`<h1>` through `<h6>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
, allowing `<header>` to be free to fill a different role.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#attributes)

-----------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#accessibility)

-----------------------------------------------------------------------------------------------------------

The `<header>` element defines a [`banner`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/banner_role)
 landmark when its context is the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element.

When placed inside an [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
, [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
, [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
, [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
, [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
, or an element with the same ARIA role as these elements' implicit ARIA role, the `<header>` element has the [`generic`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role)
 role instead, and is no longer considered a landmark. In this case, it cannot be labeled with [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
 or [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#examples)

-------------------------------------------------------------------------------------------------

### [Page Header](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#page_header)

html

    <header>
      <h1>Main Page Title</h1>
      <img src="mdn-logo-sm.png" alt="MDN logo" />
    </header>
    

#### Result

### [Article Header](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#article_header)

html

    <article>
      <header>
        <h2>The Planet Earth</h2>
        <p>
          Posted on Wednesday, <time datetime="2017-10-04">4 October 2017</time> by
          Jane Smith
        </p>
      </header>
      <p>
        We live on a planet that's blue and green, with so many things still unseen.
      </p>
      <p><a href="https://example.com/the-planet-earth/">Continue reading…</a></p>
    </article>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, but with no `<header>` or [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)<br> descendant. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. Note that a `<header>` element must not be a descendant of an [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)<br>, [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)<br> or another `<header>` element. |
| Implicit ARIA role | [banner](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/banner_role)<br>, or [generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role)<br> if a descendant of an `[article](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article) `, `[aside](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside) `, `[main](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main) `, `[nav](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav) ` or `[section](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section) ` element, or an element with `[article](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/article_role) `, `[complementary](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/complementary_role) `, `[main](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/main_role) `, `[navigation](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/navigation_role) ` or `[region](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/region_role) ` role |
| Permitted ARIA roles | [`group`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br> or [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role) |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-header-element](https://html.spec.whatwg.org/multipage/sections.html#the-header-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header#see_also)

-------------------------------------------------------------------------------------------------

*   Other section-related elements: [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
    , [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
    , [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
    , [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
    , [h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h2](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h3](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h4](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h5](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h6](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    , [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    , [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/header/index.md?plain=1 "Folder: en-us/web/html/reference/elements/header (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fheader&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fheader%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fheader%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fheader%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")