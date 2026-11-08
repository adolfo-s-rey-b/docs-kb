*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#mdn-search)
    

`disabled` HTML attribute
=========================

The Boolean **`disabled`** attribute, when present, makes the element not mutable, focusable, or even submitted with the form. The user can neither edit nor focus on the control, nor its form control descendants.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#try_it)

-------------------------------------------------------------------------------------------------

[Overview](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#overview)

-----------------------------------------------------------------------------------------------------

If the `disabled` attribute is specified on a form control, the element and its form control descendants do not participate in constraint validation. Often browsers gray out such controls and it won't receive any browsing events, like mouse clicks or focus-related ones.

The `disabled` attribute is supported by [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
, [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
, [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 and [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
.

This Boolean disabled attribute indicates that the user cannot interact with the control or its descendant controls. If this attribute is not specified, the control inherits its setting from the containing element, for example `fieldset`; if there is no containing element with the `disabled` attribute set, and the control itself does not have the attribute, then the control is enabled. If declared on an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
, the select is still interactive (unless otherwise disabled), but none of the items in the option group are selectable.

**Note:** If a [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
 is disabled, the descendant form controls are all disabled, with the exception of form controls within the [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
.

When a supporting element has the `disabled` attribute applied, the [`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
 pseudo-class also applies to it. Conversely, elements that support the `disabled` attribute but don't have the attribute set match the [`:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled)
 pseudo-class.

This Boolean attribute prevents the user from interacting with the button. If this attribute isn't set, the button can still be disabled from a containing element, for example [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
; if there is no containing element with the `disabled` attribute set, then the button is enabled.

Firefox will, unlike other browsers, persist the dynamic disabled state of a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 across page loads. Use the [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)
 attribute to control this feature.

### [Attribute interactions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#attribute_interactions)

The difference between `disabled` and [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)
 is that read-only controls can still function and are still focusable, whereas disabled controls cannot receive focus and are not submitted with the form and generally do not function as controls until they are enabled.

Because a disabled field cannot have its value changed, [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)
 does not have any effect on inputs with the `disabled` attribute also specified. Additionally, since the elements become immutable, most other attributes, such as [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern)
, have no effect, until the control is enabled.

**Note:** The `required` attribute is not permitted on inputs with the `disabled` attribute specified.

### [Usability](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#usability)

Browsers display disabled form controls grayed as disabled form controls are immutable, won't receive focus or any browsing events, like mouse clicks or focus-related ones, and aren't submitted with the form.

If present on a supporting elements, the [`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
 pseudo class will match. If the attribute is not included, the [`:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled)
 pseudo class will match. If the element doesn't support the disabled attribute, the attribute will have no effect, including not leading to being matched by the `:disabled` and `:enabled` pseudo classes.

### [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#constraint_validation)

If the element is `disabled`, then the element's value cannot receive focus and cannot be updated by the user, and does not participate in constraint validation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#examples)

-----------------------------------------------------------------------------------------------------

When form controls are disabled, many browsers will display them in a lighter, grayed-out color by default. Here are examples of a disabled checkbox, radio button, [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 and [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
, as well as some form controls that are disabled via the disabled attribute set on the ancestor ``[`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset) `` element. The [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
s are disabled, but the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 itself is not. We could have disable the entire [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 by adding the attribute to that element rather than its descendants.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-fe-disabled](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-disabled) |
| [HTML  <br>\# attr-optgroup-disabled](https://html.spec.whatwg.org/multipage/form-elements.html#attr-optgroup-disabled) |
| [HTML  <br>\# attr-option-disabled](https://html.spec.whatwg.org/multipage/form-elements.html#attr-option-disabled) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

### [html.elements.button.disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#html.elements.button.disabled)

### [html.elements.fieldset.disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#html.elements.fieldset.disabled)

### [html.elements.input.disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#html.elements.input.disabled)

### [html.elements.optgroup.disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#html.elements.optgroup.disabled)

### [html.elements.option.disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#html.elements.option.disabled)

### [html.elements.select.disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#html.elements.select.disabled)

### [html.elements.textarea.disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#html.elements.textarea.disabled)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled#see_also)

-----------------------------------------------------------------------------------------------------

*   [`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
     and [`:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/disabled/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/disabled (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fdisabled&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fdisabled%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fdisabled%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fdisabled%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc9f3d85f24d7839c9fe36a68d8042d088d906147%0A*+Document+last+modified%3A+2026-09-05T08%3A25%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")