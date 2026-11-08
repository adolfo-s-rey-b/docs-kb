*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#mdn-search)
    

`<footer>` HTML footer element
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<footer>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#sectioning_content)
 or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#labeling_section_content)
 element. A `<footer>` typically contains information about the author of the section, copyright data or links to related documents.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#try_it)

---------------------------------------------------------------------------------------------

    <article>
      <h1>How to be a wizard</h1>
      <ol>
        <li>Grow a long, majestic beard.</li>
        <li>Wear a tall, pointed hat.</li>
        <li>Have I mentioned the beard?</li>
      </ol>
      <footer>
        <p>© 2018 Gandalf</p>
      </footer>
    </article>
    

    article {
      min-height: 100%;
      display: grid;
      grid-template-rows: auto 1fr auto;
    }
    
    footer {
      display: flex;
      justify-content: center;
      padding: 5px;
      background-color: #45a1ff;
      color: white;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#attributes)

-----------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#usage_notes)

-------------------------------------------------------------------------------------------------------

*   Enclose information about the author in an [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
     element that can be included into the `<footer>` element.
*   When the nearest ancestor sectioning content or sectioning root element is the body element the footer applies to the whole page.
*   The `<footer>` element is not sectioning content and therefore doesn't introduce a new section in the [outline](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    .

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#accessibility)

-----------------------------------------------------------------------------------------------------------

Prior to the release of Safari 13, the `contentinfo` [landmark role](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/WAI-ARIA_basics#signpostslandmarks)
 was not properly exposed by [VoiceOver](https://help.apple.com/voiceover/info/guide/ "External link (opens in new tab)")
. If needing to support legacy Safari browsers, add `role="contentinfo"` to the `footer` element to ensure the landmark will be properly exposed.

*   Related: [WebKit Bugzilla: 146930 – AX: HTML native elements (header, footer, main, aside, nav) should work the same as ARIA landmarks, sometimes they don't](https://webkit.org/b/146930 "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#examples)

-------------------------------------------------------------------------------------------------

html

    <body>
      <h3>FIFA World Cup top goalscorers</h3>
      <ol>
        <li>Miroslav Klose, 16</li>
        <li>Ronaldo Nazário, 15</li>
        <li>Gerd Müller, 14</li>
      </ol>
    
      <footer>
        <small>
          Copyright © 2023 Football History Archives. All Rights Reserved.
        </small>
      </footer>
    </body>
    

css

    footer {
      text-align: center;
      padding: 5px;
      background-color: #abbaba;
      color: black;
    }
    

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, palpable content. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, but with no `<footer>` or [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)<br> descendants. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. Note that a `<footer>` element must not be a descendant of an [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)<br>, [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)<br> or another `<footer>` element. |
| Implicit ARIA role | [contentinfo](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/contentinfo_role)<br>, or [generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role)<br> if a descendant of an [article](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)<br>, [aside](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)<br>, [main](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)<br>, [nav](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)<br> or [section](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)<br> element, or an element with `[article](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/article_role) `, `[complementary](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/complementary_role) `, `[main](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/main_role) `, `[navigation](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/navigation_role) ` or `[region](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/region_role) ` role |
| Permitted ARIA roles | [`group`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br> or [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role) |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-footer-element](https://html.spec.whatwg.org/multipage/sections.html#the-footer-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer#see_also)

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
    , [`<hgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup)
    , [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
    , [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    , [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
    ;
*   [Using HTML sections and outlines](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    
*   [ARIA: Contentinfo role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/contentinfo_role)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/footer/index.md?plain=1 "Folder: en-us/web/html/reference/elements/footer (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ffooter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ffooter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ffooter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ffooter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")