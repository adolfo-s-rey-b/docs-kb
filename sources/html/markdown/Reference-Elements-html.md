*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#mdn-search)
    

`<html>` HTML document root element
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<html>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element. There can be only one `<html>` element in a document.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#attributes)

---------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`version`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#version)

Specifies the version of the HTML [Document Type Definition](https://developer.mozilla.org/en-US/docs/Glossary/Doctype)
 that governs the current document. This attribute is not needed, because it is redundant with the version information in the document type declaration.

[`xmlns`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#xmlns)

Specifies the [XML](https://developer.mozilla.org/en-US/docs/Glossary/XML)
 [Namespace](https://developer.mozilla.org/en-US/docs/Glossary/Namespace)
 of the document. Default value is `"http://www.w3.org/1999/xhtml"`. This is required in documents parsed with XML [parsers](https://developer.mozilla.org/en-US/docs/Glossary/Parser)
, and optional in text/html documents.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#accessibility)

---------------------------------------------------------------------------------------------------------

While HTML does not require authors to specify `<html>` element start and ending tags, it is important for authors to do so as it will allow them to specify the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 for the webpage. Providing a `lang` attribute with a valid [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
 on the `<html>` element will help screen reading technology determine the proper language to announce. The identifying language tag should describe the language used by the majority of the content of the page. Without it, screen readers will typically default to the operating system's set language, which may cause mispronunciations.

Including a valid `lang` declaration on the `<html>` element also ensures that important metadata contained in the page's [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
, such as the page's [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)
, are also announced properly.

*   [MDN Understanding WCAG, Guideline 3.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Understandable#guideline_3.1_%e2%80%94_readable_make_text_content_readable_and_understandable)
    
*   [Understanding Success Criterion 3.1.1 | W3C Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/language-of-page.html "External link (opens in new tab)")
    

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#example)

---------------------------------------------------------------------------------------------

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | One [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)<br> element, followed by one [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)<br> element. |
| Tag omission | The start tag may be omitted if the first thing inside the `<html>` element is not a comment.  <br>The end tag may be omitted if the `<html>` element is not immediately followed by a comment. |
| Permitted parents | None. This is the root element of a document. |
| Implicit ARIA role | [document](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/document_role) |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLHtmlElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLHtmlElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-html-element](https://html.spec.whatwg.org/multipage/semantics.html#the-html-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html#see_also)

-----------------------------------------------------------------------------------------------

*   MathML top-level element: [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math "<math>")
    
*   SVG top-level element: [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 9, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/html/index.md?plain=1 "Folder: en-us/web/html/reference/elements/html (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fhtml&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fhtml%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fhtml%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fhtml%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F44a5fa2aace490e0114349d9d683675b2f5cacce%0A*+Document+last+modified%3A+2026-05-09T06%3A32%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")