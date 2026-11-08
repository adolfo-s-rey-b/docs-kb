*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex#mdn-search)
    

`tabindex` HTML global attribute
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`tabindex`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 allows developers to make HTML elements focusable, allow or prevent them from being sequentially focusable (usually with the Tab key, hence the name) and determine their relative ordering for sequential focus navigation.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex#try_it)

--------------------------------------------------------------------------------------------------------

It accepts an integer as a value, with different results depending on the integer's value:

**Note:** If an HTML element renders and has `tabindex` attribute with any valid integer value, the element can be focused with JavaScript (by calling the [`focus()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus)
 method) or visually by clicking with the mouse. The particular `tabindex` value controls whether the element is `tabbable` (i.e., reachable via sequential keyboard navigation, usually with the Tab key).

*   A _negative value_ (the exact negative value doesn't actually matter, usually `tabindex="-1"`) means that the element is not reachable via sequential keyboard navigation.
    
    **Note:** `tabindex="-1"` may be useful for elements that should not be navigated to directly using the Tab key, but need to have keyboard focus set to them. Examples include an off-screen modal window that should be focused when it comes into view, or a form submission error message that should be immediately focused when an errant form is submitted.
    
*   `tabindex="0"` means that the element should be focusable in sequential keyboard navigation, after any positive `tabindex` values. The focus navigation order of these elements is defined by their order in the document source.
    
*   A _positive value_ means the element should be focusable in sequential keyboard navigation, with its order defined by the value of the number. That is, `tabindex="4"` is focused before `tabindex="5"` and `tabindex="0"`, but after `tabindex="3"`. If multiple elements share the same positive `tabindex` value, their order relative to each other follows their position in the document source. The maximum value for `tabindex` is 32767.
    
*   If the `tabindex` attribute is included with no value set, whether the element is focusable is determined by the user agent.
    
    **Warning:** You are recommended to only use `0` and `-1` as `tabindex` values. Avoid using `tabindex` values greater than `0` and CSS properties that can change the order of focusable HTML elements ([Ordering flex items](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Ordering_items)
    ). Doing so makes it difficult for people who rely on using keyboard for navigation or assistive technology to navigate and operate page content. Instead, write the document with the elements in a logical sequence.
    

Some focusable HTML elements have a default `tabindex` value of `0` set under the hood by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
. These elements are an [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 or [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 with `href` attribute, [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<frame>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame)
 , [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
, and SVG [`<a>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/a)
 element, or a [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary)
 element that provides summary for a [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 element. Developers shouldn't add the `tabindex` attribute to these elements unless it changes the default behavior (for example, including a negative value will remove the element from the focus navigation order).

**Warning:** The tabindex attribute must not be used on the [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 element.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex#accessibility_concerns)

----------------------------------------------------------------------------------------------------------------------------------------

Avoid using the `tabindex` attribute in conjunction with non-[interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)
 to make something intended to be interactive focusable by keyboard input. An example of this would be using a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element to describe a button, instead of the [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element.

Interactive components authored using non-interactive elements are not listed in the [accessibility tree](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/What_is_accessibility#accessibility_apis)
. This prevents assistive technology from being able to navigate to and manipulate those components. The content should be semantically described using interactive elements ([`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
, etc.) instead. These elements have built-in roles and states that communicate status to the accessibility that would otherwise have to be managed by [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
.

*   [Using the tabindex attribute | Vispero](https://vispero.com/resources/using-the-tabindex-attribute/ "External link (opens in new tab)")
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-tabindex](https://html.spec.whatwg.org/multipage/interaction.html#attr-tabindex) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex#see_also)

------------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    
*   [`HTMLElement.tabIndex`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/tabIndex)
     that reflects this attribute
*   Accessibility problems with `tabindex`: see [Don't Use Tabindex Greater than 0](https://adrianroselli.com/2014/11/dont-use-tabindex-greater-than-0.html "External link (opens in new tab)")
     by Adrian Roselli
*   [Reading order](https://developer.mozilla.org/en-US/docs/Glossary/Reading_order)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/tabindex/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/tabindex (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Ftabindex&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Ftabindex%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Ftabindex%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Ftabindex%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")