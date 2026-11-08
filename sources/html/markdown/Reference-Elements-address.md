*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#mdn-search)
    

`<address>` HTML contact address element
========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<address>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#try_it)

----------------------------------------------------------------------------------------------

    <p>Contact the author of this page:</p>
    
    <address>
      <a href="mailto:jim@example.com">jim@example.com</a><br />
      <a href="tel:+14155550132">+1 (415) 555‑0132</a>
    </address>
    

    a[href^="mailto"]::before {
      content: "📧 ";
    }
    
    a[href^="tel"]::before {
      content: "📞 ";
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#attributes)

------------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#usage_notes)

--------------------------------------------------------------------------------------------------------

The contact information provided by an `<address>` element's contents can take whatever form is appropriate for the context, and may include any type of contact information that is needed, such as a physical address, URL, email address, phone number, social media handle, geographic coordinates, and so forth. The `<address>` element should include the name of the person, people, or organization to which the contact information refers. However, this element should not contain more information than the contact information, like a publication date (which belongs in a [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time)
 element).

`<address>` can be used in a variety of contexts, such as providing a business's contact information in the page header, or indicating the author of an article by including an `<address>` element within the [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
. The `<address>` element can only be used to represent the contact information for its nearest [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 or [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element ancestor. Typically an `<address>` element can be placed inside the [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
 element of the current section, if any.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#examples)

--------------------------------------------------------------------------------------------------

This example demonstrates the use of `<address>` to demarcate the contact information for an article's author.

html

    <address>
      You can contact author at
      <a href="http://www.example.com/contact">www.example.com</a>.<br />
      If you see any bugs, please
      <a href="mailto:webmaster@example.com">contact webmaster</a>.<br />
      You may also want to visit us:<br />
      Mozilla Foundation<br />
      331 E Evelyn Ave<br />
      Mountain View, CA 94041<br />
      USA
    </address>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#result)

Although it renders text with the same default styling as the [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
 or [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
 elements, it is more appropriate to use `<address>` when dealing with contact information, as it conveys additional semantic information.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#technical_summary)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, palpable content. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, but with no nested `<address>` element, no heading content ([`<hgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup)<br>, [h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h2](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h3](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h4](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h5](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h6](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>), no sectioning content ([`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)<br>, [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)<br>, [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)<br>, [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)<br>), and no [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)<br> or [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)<br> element. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, but always excluding `<address>` elements (according to the logical principle of symmetry, if `<address>` tag, as a parent, cannot have nested `<address>` element, then the same `<address>` content cannot have `<address>` tag as its parent). |
| Implicit ARIA role | `[group](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)<br> Prior to Gecko 2.0 (Firefox 4), Gecko implemented this element using the [`HTMLSpanElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSpanElement)<br> interface |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-address-element](https://html.spec.whatwg.org/multipage/sections.html#the-address-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address#see_also)

--------------------------------------------------------------------------------------------------

*   Others section-related elements: [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
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
    , [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    , [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    , [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
    ;
*   [Sections and outlines of an HTML document](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/address/index.md?plain=1 "Folder: en-us/web/html/reference/elements/address (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Faddress&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Faddress%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Faddress%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Faddress%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcb7d4dde9f0a43664c64587d9d70b8835286eb7%0A*+Document+last+modified%3A+2026-10-01T19%3A41%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")