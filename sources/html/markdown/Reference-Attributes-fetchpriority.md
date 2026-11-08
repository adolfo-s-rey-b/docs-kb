*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#mdn-search)
    

`fetchpriority` HTML attribute
==============================

Baseline 2024

Newly available

Since October 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`fetchpriority`** attribute allows a developer to signal that fetching a particular image early in the loading process has more or less impact on user experience than a browser can reasonably infer when assigning an internal priority. This in turn allows the browser to increase or decrease the priority, and potentially load the image earlier or later than it would otherwise.

This attribute may be applied to [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, and [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 elements. It also has an [SVG counterpart](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fetchpriority)
.

The fetch priority can be used to complement [preloading](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)
, allowing a developer to boost the priority ahead of less-impactful resources that have a higher default priority. For example, if a developer knows that a particular image significantly contributes to the website's [Largest Contentful Paint](https://developer.mozilla.org/en-US/docs/Glossary/Largest_contentful_paint)
 (LCP) they could add [`<link rel="preload">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)
 for the image and then further boost the priority using the `fetchpriority` attribute.

Note that both the internal priority of any fetch operation, and the impact of `fetchpriority` on the priority, are entirely browser dependent.

This attribute is [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 and can have one of the following values:

[`high`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#high)

Fetches the external resource at a high priority relative to other external resources.

[`low`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#low)

Fetches the external resource at a low priority relative to other external resources.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#auto)

Doesn't set a preference for the fetch priority. It is used if no value or an invalid value is set. This is the default.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#usage_notes)

----------------------------------------------------------------------------------------------------------------

The attribute should be used sparingly, as excessive or incorrect prioritization can degrade performance.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-img-fetchpriority](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-fetchpriority) |
| [HTML  <br>\# attr-link-fetchpriority](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-fetchpriority) |
| [HTML  <br>\# attr-script-fetchpriority](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-fetchpriority) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

### [html.elements.img.fetchpriority](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#html.elements.img.fetchpriority)

### [html.elements.link.fetchpriority](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#html.elements.link.fetchpriority)

### [html.elements.script.fetchpriority](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#html.elements.script.fetchpriority)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority#see_also)

----------------------------------------------------------------------------------------------------------

*   SVG [`fetchpriority`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fetchpriority)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/fetchpriority/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/fetchpriority (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Ffetchpriority&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Ffetchpriority%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Ffetchpriority%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Ffetchpriority%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")