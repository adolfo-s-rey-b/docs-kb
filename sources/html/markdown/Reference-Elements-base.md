*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#mdn-search)
    

`<base>` HTML document base URL element
=======================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<base>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element specifies the base URL to use for all _relative_ URLs in a document. There can be only one `<base>` element in a document.

A document's used base URL can be accessed by scripts with [`Node.baseURI`](https://developer.mozilla.org/en-US/docs/Web/API/Node/baseURI)
. If the document has no `<base>` elements, then `baseURI` defaults to [`location.href`](https://developer.mozilla.org/en-US/docs/Web/API/Location/href)
.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#attributes)

---------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

**Warning:** A `<base>` element must have an `href` attribute, a `target` attribute, or both. If at least one of these attributes are specified, the `<base>` element **must** come before other elements with attribute values that are URLs, such as a [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
's `href` attribute.

[`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#href)

The base URL to be used throughout the document for relative URLs. Absolute and relative URLs are allowed. [`data:`](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data)
 and [`javascript:`](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/javascript)
 URLs are not allowed.

[`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#target)

A **keyword** or **author-defined name** of the default [browsing context](https://developer.mozilla.org/en-US/docs/Glossary/Browsing_context)
 to show the results of navigation from [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, or [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 elements without explicit `target` attributes. The following keywords have special meanings:

*   `_self` (default): Show the result in the current browsing context.
*   `_blank`: Show the result in a new, unnamed browsing context.
*   `_parent`: Show the result in the parent browsing context of the current one, if the current page is inside a frame. If there is no parent, acts the same as `_self`.
*   `_top`: Show the result in the topmost browsing context (the browsing context that is an ancestor of the current one and has no parent). If there is no parent, acts the same as `_self`.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#usage_notes)

-----------------------------------------------------------------------------------------------------

### [Multiple <base> elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#multiple_base_elements)

If multiple `<base>` elements are used, only the first `href` and first `target` are obeyed — all others are ignored.

### [In-page anchors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#in-page_anchors)

Links pointing to a fragment in the document — e.g., `<a href="#some-id">` — are resolved with the `<base>`, triggering an HTTP request to the base URL with the fragment attached.

For example, given `<base href="https://example.com/">` and this link: `<a href="#anchor">To anchor</a>`. The link points to `https://example.com/#anchor`.

### [target may not contain ASCII newline, tab, or <](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#target_may_not_contain_ascii_newline_tab_or)

If the [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#target)
 attribute contains an ASCII newline, tab, or the `<` character, the value is reset to `_blank`. This is to prevent dangling markup injection attacks, a script-less attack in which an unclosed `target` attribute is injected into the page so that any text that follows is captured until the browser reaches a character that closes the attribute.

### [Open Graph](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#open_graph)

[Open Graph](https://ogp.me/ "External link (opens in new tab)")
 tags do not acknowledge `<base>`, and should always have full absolute URLs. For example:

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#examples)

-----------------------------------------------------------------------------------------------

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | Metadata content. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | A [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)<br> that doesn't contain another `<base>` element. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLBaseElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLBaseElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-base-element](https://html.spec.whatwg.org/multipage/semantics.html#the-base-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/base/index.md?plain=1 "Folder: en-us/web/html/reference/elements/base (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbase&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbase%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbase%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbase%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")