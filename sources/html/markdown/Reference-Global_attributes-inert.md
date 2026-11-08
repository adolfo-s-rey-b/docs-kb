*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert#mdn-search)
    

`inert` HTML global attribute
=============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`inert`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is a Boolean attribute indicating that the element and all of its flat tree descendants become _inert_. The `inert` attribute can be added to sections of content that should not be interactive. When an element is inert, it along with all of the element's descendants, including normally interactive elements such as links, buttons, and form controls are disabled because they cannot receive focus or be clicked. The `inert` attribute can also be added to elements that should be offscreen or hidden. An inert element, along with its descendants, gets removed from the tab order and accessibility tree.

Modal [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
s generated with [`showModal()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal)
 escape inertness, meaning that they don't inherit inertness from their ancestors, but can be made inert by having the `inert` attribute explicitly set on themselves. No other element can escape inertness.

**Note:** While `inert` is a global attribute and can be applied to any element, it is generally used for sections of content. To make individual controls "inert", consider using the [`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)
 attribute, along with CSS [`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
 styles, instead.

Inert HTML elements and their flat tree descendants:

*   Do not have [`click`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event "click")
     events fired when clicked on.
*   Cannot be focused and [`focus`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focus_event "focus")
     events cannot be fired on them.
*   Are not searchable via browser find-in-page features (none of their content is found/matched).
*   Disallow users from selecting text contained within their content — akin to using the CSS property [`user-select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select)
     to disable text selection.
*   Cannot have otherwise-editable content edited. This includes, for example, the contents of textual [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     fields, and text elements with [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     set on them.
*   Are hidden from assistive technologies as they are excluded from the accessibility tree.

The following other features can be used to set an element and its descendants to an inert state:

*   The CSS [`interactivity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity)
     property.
*   The [`HTMLElement.inert`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/inert)
     DOM property.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert#accessibility_concerns)

-------------------------------------------------------------------------------------------------------------------------------------

Use careful consideration for accessibility when applying the `inert` attribute. By default, there is no visual way to tell whether or not an element or its subtree is inert. As a web developer, it is your responsibility to clearly indicate the content parts that are active and those that are inert.

While providing visual and non-visual cues about content inertness, also remember that the visual viewport may contain only sections of content. Users may be zoomed in to a small section of content, or users may not be able to view the content at all. Inert sections not being obviously inert can lead to frustration and bad user experience.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert#examples)

---------------------------------------------------------------------------------------------------------

In this example, the second [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 and all of its descendants are made inert via the `inert` attribute:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-inert-attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert#see_also)

---------------------------------------------------------------------------------------------------------

*   HTML [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
     element
*   [`HTMLElement.inert`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/inert)
     DOM property
*   CSS [`interactivity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity)
     property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/inert/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/inert (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Finert&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Finert%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Finert%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Finert%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")