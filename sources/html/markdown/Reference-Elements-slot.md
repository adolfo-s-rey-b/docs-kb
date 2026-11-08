*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#mdn-search)
    

`<slot>` HTML web component slot element
========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<slot>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is a placeholder inside a [Web Component](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)
 that you can fill with your own markup when the component is used. This lets you create separate DOM trees and present them together.

Slots can contain plain text, other HTML elements, or other web components. A slot can also contain default content, which is displayed if the slot is not assigned other content when the web component is used.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#attributes)

---------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#name)

The slot's name. A _named slot_ is a `<slot>` element with a `name` attribute, while an _unnamed slot_ has no `name` attribute, and the name defaults to the empty string.

When a shadow root uses [named slot assignment](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#named)
, top-level child elements of its host are rendered in slots that have a matching name in their [`slot` attribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/slot)
. Slot names should be unique per shadow root: if you have two slots with the same name, all of the elements with a matching `slot` attribute are rendered in the _first_ slot. All top-level child elements that don't have a `slot` attribute are rendered in the first unnamed `<slot>` element, which is referred to as the _default slot_. The `name` has no effect if the shadow root uses [manual slot assignment](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#manual)
.

For more information see [`shadowrootslotassignment`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootslotassignment)
 on the `<template>` element and [`Element.attachShadow()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow#slotassignment)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#examples)

-----------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#basic_usage)

This HTML shows how a number of named slots might be declared within a [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
 element. Note that these slots are only used as slots when the template is used inside a shadow root.

**Note:** You can see this complete example in action at [element-details](https://github.com/mdn/web-components-examples/tree/main/element-details "External link (opens in new tab)")
 (see it [running live](https://mdn.github.io/web-components-examples/element-details/ "External link (opens in new tab)")
). In addition, you can find an explanation at [Using templates and slots](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_templates_and_slots)
.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content) |
| Permitted content | [Transparent](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#transparent_content_model) |
| Events | [`slotchange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSlotElement/slotchange_event "slotchange") |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content) |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLSlotElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSlotElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-slot-element](https://html.spec.whatwg.org/multipage/scripting.html#the-slot-element) |
| [DOM  <br>\# shadow-tree-slots](https://dom.spec.whatwg.org/#shadow-tree-slots) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#see_also)

-----------------------------------------------------------------------------------------------

*   HTML [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
     element
*   HTML [`slot`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/slot)
     attribute
*   CSS [`::slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
     pseudo-element
*   CSS [`:has-slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted)
     pseudo-class
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
     module
*   [Using templates and slots](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_templates_and_slots)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/slot/index.md?plain=1 "Folder: en-us/web/html/reference/elements/slot (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fslot&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fslot%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fslot%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fslot%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8dd50fa9cb734907685508144376dbdd28f98be6%0A*+Document+last+modified%3A+2026-06-03T19%3A03%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")