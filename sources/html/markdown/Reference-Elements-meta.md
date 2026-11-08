*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#mdn-search)
    

`<meta>` HTML metadata element
==============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<meta>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata)
 that cannot be represented by other meta-related elements, such as [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base)
, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
, [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
, or [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)
.

The type of metadata provided by the `<meta>` element can be one of the following:

*   If the [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
     attribute is set, the `<meta>` element provides _document-level metadata_ that applies to the whole page.
*   If the [`http-equiv`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv)
     attribute is set, the `<meta>` element acts as a _pragma directive_ to simulate directives that could otherwise be given by an HTTP header.
*   If the [`charset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#charset)
     attribute is set, the `<meta>` element is a _charset declaration_, giving the character encoding in which the document is encoded.
*   If the [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
     attribute is set, the `<meta>` element provides _user-defined metadata_.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#attributes)

---------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

**Note:** The [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
 attribute has a specific meaning for the `<meta>` element. The [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
 attribute must not be set on a `<meta>` element that includes a [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
, [`http-equiv`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv)
, or [`charset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#charset)
 attribute.

[`charset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#charset)

This attribute declares the document's character encoding. If the attribute is present, its value must be an ASCII case-insensitive match for the string `"utf-8"`, because UTF-8 is the only valid encoding for HTML5 documents. `<meta>` elements which declare a character encoding must be located entirely within the first 1024 bytes of the document.

[`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/content)

This attribute contains the value for the [`http-equiv`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv)
 or [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
 attribute, depending on which is used.

[`http-equiv`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv)

Defines a pragma directive, which are instructions for the browser for processing the document. The attribute's name is short for `http-equivalent` because the allowed values are names of equivalent HTTP headers.

[`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#media)

The `media` attribute defines which media the theme color defined in the `content` attribute should be applied to. Its value is a [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
, which defaults to `all` if the attribute is missing. This attribute is only relevant when the element's [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
 attribute is set to [`theme-color`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color)
. Otherwise, it has no effect, and should not be included.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)

The `name` and `content` attributes can be used together to provide document metadata in terms of name-value pairs, with the `name` attribute giving the metadata name, and the `content` attribute giving the value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#examples)

-----------------------------------------------------------------------------------------------

### [Setting a meta description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#setting_a_meta_description)

The following `<meta>` tag provides a `description` as metadata for the web page:

### [Setting a page redirect](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#setting_a_page_redirect)

The following example uses `http-equiv="refresh"` to direct the browser to perform a redirect. The `content="3;url=https://www.mozilla.org"` attribute will redirect page to `https://www.mozilla.org` after 3 seconds:

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)<br>. If the [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)<br> attribute is present: [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | *   `<meta charset>`, `<meta http-equiv>`: a [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)<br>     element. If the [`http-equiv`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv)<br>     is not an encoding declaration, it can also be inside a [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)<br>     element, itself inside a `<head>` element.<br>*   `<meta name>`: any element that accepts [metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)<br>    .<br>*   `<meta itemprop>`: any element that accepts [metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)<br>     or [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>    . |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLMetaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMetaElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-meta-element](https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#see_also)

-----------------------------------------------------------------------------------------------

*   [Standard metadata names](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
    
*   [Learn: `<meta>`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Webpage_metadata#metadata_the_meta_element)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meta/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meta (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")