*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#mdn-search)
    

`<noscript>` HTML noscript element
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<noscript>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#attributes)

-------------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#examples)

---------------------------------------------------------------------------------------------------

### [Result with scripting enabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#result_with_scripting_enabled)

Rocks!

### [Result with scripting disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#result_with_scripting_disabled)

[External Link](https://www.mozilla.org/ "External link (opens in new tab)")

Rocks!

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#usage_notes)

---------------------------------------------------------------------------------------------------------

The `<noscript>` element represents its children differently depending on if scripting is enabled:

*   If scripting is disabled the `<noscript>` element represents its children as [HTML content](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
    .
*   If scripting is enabled, the `<noscript>` element represents its children as [text](https://developer.mozilla.org/en-US/docs/Web/API/Text)
    .

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#technical_summary)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)<br>, [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Permitted content | When scripting is disabled and when it is a descendant of the [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)<br> element: in any order, zero or more [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)<br> elements, zero or more [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)<br> elements, and zero or more [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)<br> elements.  <br>When scripting is disabled and when it isn't a descendant of the [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)<br> element: any [transparent content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#transparent_content_model)<br>, but no `<noscript>` element must be among its descendants.  <br>Otherwise: flow content or phrasing content. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, if there are no ancestor `<noscript>` element, or in a [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)<br> element (but only for an HTML document), here again if there are no ancestor `<noscript>` element. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-noscript-element](https://html.spec.whatwg.org/multipage/scripting.html#the-noscript-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/noscript/index.md?plain=1 "Folder: en-us/web/html/reference/elements/noscript (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fnoscript&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fnoscript%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fnoscript%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fnoscript%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")