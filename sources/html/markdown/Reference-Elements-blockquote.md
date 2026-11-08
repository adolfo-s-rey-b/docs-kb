*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#mdn-search)
    

`<blockquote>` HTML block quotation element
===========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<blockquote>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation (see [Notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#usage_notes)
 for how to change it). A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
 element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#try_it)

-------------------------------------------------------------------------------------------------

    <div>
      <blockquote cite="https://www.huxley.net/bnw/four.html">
        <p>
          Words can be like X-rays, if you use them properly—they'll go through
          anything. You read and you're pierced.
        </p>
      </blockquote>
      <p>—Aldous Huxley, <cite>Brave New World</cite></p>
    </div>
    

    div:has(> blockquote) {
      background-color: #ededed;
      margin: 10px auto;
      padding: 15px;
      border-radius: 5px;
    }
    
    blockquote p::before {
      content: "\201C";
    }
    
    blockquote p::after {
      content: "\201D";
    }
    
    blockquote + p {
      text-align: right;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#attributes)

---------------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`cite`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#cite)

A URL that designates a source document or message for the information quoted. This attribute is intended to point to information explaining the context or the reference for the quote.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#usage_notes)

-----------------------------------------------------------------------------------------------------------

According to the specification, attribution for the quotation, if any, must be placed outside the `<blockquote>` element.

To change the indentation applied to the quoted text, use the [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
 [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
 and/or [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
 properties, or the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 shorthand property.

To include shorter quotes inline rather than in a separate block, use the [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
 (Quotation) element.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#examples)

-----------------------------------------------------------------------------------------------------

This example demonstrates the use of the `<blockquote>` element to quote a passage from [RFC 1149](https://datatracker.ietf.org/doc/html/rfc1149 "External link (opens in new tab)")
, _A Standard for the Transmission of IP Datagrams on Avian Carriers_.

html

    <blockquote cite="https://datatracker.ietf.org/doc/html/rfc1149">
      <p>
        Avian carriers can provide high delay, low throughput, and low altitude
        service. The connection topology is limited to a single point-to-point path
        for each carrier, used with standard carriers, but many carriers can be used
        without significant interference with each other, outside early spring. This
        is because of the 3D ether space available to the carriers, in contrast to
        the 1D ether used by IEEE802.3. The carriers have an intrinsic collision
        avoidance system, which increases availability.
      </p>
    </blockquote>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#technical_summary)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, sectioning root, palpable content. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | `[blockquote](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles#structural_roles_with_html_equivalents) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLQuoteElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLQuoteElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-blockquote-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-blockquote-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#see_also)

-----------------------------------------------------------------------------------------------------

*   The [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
     element for inline quotations.
*   The [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
     element for source citations.
*   [The blockquote element](https://heydonworks.com/article/the-blockquote-element/ "External link (opens in new tab)")
     via heydonworks.com (2024)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/blockquote/index.md?plain=1 "Folder: en-us/web/html/reference/elements/blockquote (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fblockquote&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fblockquote%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fblockquote%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fblockquote%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")