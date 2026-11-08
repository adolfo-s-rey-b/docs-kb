*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#mdn-search)
    

`<b>` HTML bring attention to element
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<b>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `<b>` for styling text or granting importance. If you wish to create boldface text, you should use the CSS [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 property. If you wish to indicate an element is of special importance, you should use the [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
 element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#try_it)

----------------------------------------------------------------------------------------

    <p>
      The two most popular science courses offered by the school are
      <b class="term">chemistry</b> (the study of chemicals and the composition of
      substances) and <b class="term">physics</b> (the study of the nature and
      properties of matter and energy).
    </p>
    

    b {
      /* Add your styles here */
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#attributes)

------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#usage_notes)

--------------------------------------------------------------------------------------------------

*   Use the `<b>` for cases like keywords in a summary, product names in a review, or other spans of text whose typical presentation would be boldfaced (but not including any special importance).
*   Do not confuse the `<b>` element with the [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
    , [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
    , or [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark)
     elements. The [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
     element represents text of certain _importance_, [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
     puts some emphasis on the text and the [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark)
     element represents text of certain _relevance_. The `<b>` element doesn't convey such special semantic information; use it only when no others fit.
*   Similarly, do not mark titles and headings using the `<b>` element. For this purpose, use the [h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
     to [h6](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
     tags. Further, stylesheets can change the default style of these elements, with the result that they are not _necessarily_ displayed in bold.
*   It is a good practice to use the [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)
     attribute on the `<b>` element in order to convey additional semantic information as needed (for example `<b class="lead">` for the first sentence in a paragraph). This makes it easier to manage multiple use cases of `<b>` if your stylistic needs change, without the need to change all of its uses in the HTML.
*   Historically, the `<b>` element was meant to make text boldface. Styling information has been deprecated since HTML4, so the meaning of the `<b>` element has been changed.
*   If there is no semantic purpose to using the `<b>` element, you should use the CSS [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
     property with the value `"bold"` instead in order to make text bold.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#examples)

--------------------------------------------------------------------------------------------

html

    <p>
      This article describes several <b class="keywords">text-level</b> elements. It
      explains their usage in an <b class="keywords">HTML</b> document.
    </p>
    Keywords are displayed with the default style of the
    <b>element, likely in bold.</b>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#technical_summary)

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-b-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-b-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b#see_also)

--------------------------------------------------------------------------------------------

*   Other elements conveying text-level semantics: [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
    , [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
    , [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
    , [`<small>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small)
    , [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
    , [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
    , [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
    , [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
    , [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time)
    , [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
    , [`<var>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var)
    , [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
    , [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd)
    , [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
    , [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
    , [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
    , [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark)
    , [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    , [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)
    , [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
    , [`<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo)
    , [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
    , [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
    , [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr)
    .
*   [Using <b> and <i> elements (W3C)](https://www.w3.org/International/questions/qa-b-and-i-tags "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/b/index.md?plain=1 "Folder: en-us/web/html/reference/elements/b (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fb&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fb%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fb%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fb%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")