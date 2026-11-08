*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#mdn-search)
    

`<dt>` HTML description term element
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<dt>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element specifies a term in a description or definition list, and as such must be used inside a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)
 element. It is usually followed by a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
 element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
 element.

The subsequent [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
 (**Description Details**) element provides the definition or other related text associated with the term specified using `<dt>`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#try_it)

-----------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#attributes)

-------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#examples)

---------------------------------------------------------------------------------------------

For examples, see the [examples provided for the `<dl>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#examples)
.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, but with no [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)<br>, [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)<br>, sectioning content or heading content descendants. |
| Tag omission | The start tag is required. The end tag may be omitted if this element is immediately followed by another `<dt>` element or a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)<br> element, or if there is no more content in the parent element. |
| Permitted parents | A [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)<br> or (in [WHATWG](https://developer.mozilla.org/en-US/docs/Glossary/WHATWG)<br> HTML, [W3C](https://developer.mozilla.org/en-US/docs/Glossary/W3C)<br> HTML 5.2 and later) a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)<br> that is a child of a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)<br>.  <br>This element can be used before a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)<br> or another `<dt>` element. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | `[listitem](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listitem_role) ` |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)<br> Up to Gecko 1.9.2 (Firefox 4) inclusive, Firefox implements the [`HTMLSpanElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSpanElement)<br> interface for this element. |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-dt-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dt-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt#see_also)

---------------------------------------------------------------------------------------------

*   [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)
    
*   [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/dt/index.md?plain=1 "Folder: en-us/web/html/reference/elements/dt (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdt&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdt%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdt%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdt%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")