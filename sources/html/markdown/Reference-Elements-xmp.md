*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp#mdn-search)
    

`<xmp>` HTML plain text rendering element
=========================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[Summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp#summary)

--------------------------------------------------------------------------------------------

The **`<xmp>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element renders text between the start and end tags without interpreting the HTML in between and using a monospaced font. The HTML2 specification recommended that it should be rendered wide enough to allow 80 characters per line.

**Note:** Do not use this element.

*   It has been deprecated since HTML3.2 and was not implemented in a consistent way. It was completely removed from current HTML.
*   Use the [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
     element or, if semantically adequate, the [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
     element instead. Note that you will need to escape the `<` character as `&lt;` and the `&` character as `&amp;` to make sure they are not interpreted as markup.
*   A monospaced font can also be obtained on any element, by applying an adequate [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
     style using `monospace` as the generic-font value for the [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
     property.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp#attributes)

--------------------------------------------------------------------------------------------------

This element has no other attributes than the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
, common to all elements.

[DOM interface](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp#dom_interface)

--------------------------------------------------------------------------------------------------------

This element implements the [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
 interface.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# xmp](https://html.spec.whatwg.org/multipage/obsolete.html#xmp) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp#see_also)

----------------------------------------------------------------------------------------------

*   The [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
     and [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
     elements to be used instead.
*   The [`<plaintext>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext)
     element, similar to `<xmp>` but also obsolete.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/xmp/index.md?plain=1 "Folder: en-us/web/html/reference/elements/xmp (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fxmp&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fxmp%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fxmp%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fxmp%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")