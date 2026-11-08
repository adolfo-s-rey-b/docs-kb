*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#mdn-search)
    

`<head>` HTML document metadata (header) element
================================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<head>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element contains machine-readable information ([metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata)
) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)
, [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
, and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
. There can be only one `<head>` element in an HTML document.

**Note:** `<head>` primarily holds information for machine processing, not human-readability. For human-visible information, like top-level headings and listed authors, see the [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
 element.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#attributes)

---------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`profile`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#profile)

The [URI](https://developer.mozilla.org/en-US/docs/Glossary/URI)
s of one or more metadata profiles, separated by [white space](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#examples)

-----------------------------------------------------------------------------------------------

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | If the document is an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)<br> [`srcdoc`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#srcdoc)<br> document, or if title information is available from a higher level protocol (like the subject line in HTML email), zero or more elements of metadata content.<br><br>Otherwise, one or more elements of metadata content where exactly one is a [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)<br> element. |
| Tag omission | The start tag may be omitted if the first thing inside the `<head>` element is an element.  <br>The end tag may be omitted if the first thing following the `<head>` element is not a space character or a comment. |
| Permitted parents | An [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)<br> element, as its first child. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLHeadElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLHeadElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-head-element](https://html.spec.whatwg.org/multipage/semantics.html#the-head-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head#see_also)

-----------------------------------------------------------------------------------------------

*   Elements that can be used inside the `<head>`:
    *   [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)
        
    *   [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base)
        
    *   [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
        
    *   [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
        
    *   [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
        
    *   [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
        
    *   [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)
        
    *   [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/head/index.md?plain=1 "Folder: en-us/web/html/reference/elements/head (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fhead&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fhead%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fhead%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fhead%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")