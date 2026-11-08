*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext#mdn-search)
    

`<plaintext>` HTML plain text element
=====================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<plaintext>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element renders everything following the start tag as raw text, ignoring any following HTML. There is no closing tag, since everything after it is considered raw text.

**Warning:** Do not use this element.

*   `<plaintext>` is deprecated since HTML 2, and not all browsers implemented it. Browsers that did implement it didn't do so consistently.
*   `<plaintext>` is obsolete; browsers that accept it may instead treat it as a [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
     element that still interprets HTML within.
*   If `<plaintext>` is the first element on the page (other than any non-displayed elements, like [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
    ), do not use HTML at all. Instead serve a text file with the `text/plain` [MIME-type](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Configuring_server_MIME_types)
    .
*   Instead of `<plaintext>`, use the [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
     element or, if semantically accurate (such as for inline text), the [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
     element. Escape any `<`, `>` and `&` characters, to prevent browsers inadvertently parsing the element content as HTML.
*   A monospaced font can be applied to any HTML element via a [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
     [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
     style with the `monospace` generic value.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext#attributes)

--------------------------------------------------------------------------------------------------------

This element has no other attributes than the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 common to all elements.

[DOM interface](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext#dom_interface)

--------------------------------------------------------------------------------------------------------------

This element implements the [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
 interface.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# plaintext](https://html.spec.whatwg.org/multipage/obsolete.html#plaintext) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext#see_also)

----------------------------------------------------------------------------------------------------

*   The [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
     and [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
     elements, which should be used instead.
*   The [`<xmp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp)
     element, also obsolete, similar to `<plaintext>`.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/plaintext/index.md?plain=1 "Folder: en-us/web/html/reference/elements/plaintext (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fplaintext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fplaintext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fplaintext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fplaintext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")