*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#mdn-search)
    

`form` HTML attribute
=====================

The `form` HTML attribute associates a form-associated element with a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element within the same document. This attribute applies to the [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
, [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements.

[Values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#values)

---------------------------------------------------------------------------------------------

The `id` of the `<form>` element that the element should be associated with.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#usage_notes)

-------------------------------------------------------------------------------------------------------

By default, form controls are associated with their nearest ancestor [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element, while form controls that are not nested within a `<form>` are not associated with any form. The `form` attribute enables overriding these default behaviors.

The `form` attribute of the [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
, [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements allows you to specify an explicit form owner, enabling you to associate form controls located anywhere within a document with any `<form>` element located in the same document.

When a form is submitted, the names and values of the `<form>` element's associated controls are submitted, whether or not they are physically nested within that `<form>`, and even if they are nested in a different `<form>`.

A control's `form` attribute takes as its value the `id` of the `<form>` element you want to associate the control with. All other values set for the `form` attribute are ignored.

While setting the attribute value to the `id` of the nearest ancestor `<form>` isn't necessary, explicitly defining the association between a form control and its nearest ancestor form ensures the form control will not be disassociated from its form if scripts or malformed HTML result in that specific `<form>` not being the nearest form ancestor of the control.

### [Associating with a non-ancestor form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#associating_with_a_non-ancestor_form)

The `form` attribute can be used to associate a form control nested in one `<form>` with another `<form>`.

In this code example, the username `<input>` is nested within the `internalForm`, but the `form` attribute disassociates the control from its ancestor form in which it is nested, and associates it with the `externalForm` instead:

In this case, the username will be submitted when the `externalForm` is submitted, while the `internalForm` has no associated form controls.

### [Non-inheritance of the `form` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#non-inheritance_of_the_form_attribute)

The `form` attribute only associates the element on which it is set. The attribute behavior is not inherited. For example, when the `form` attribute is set on a `<fieldset>` element, it only associates the `<fieldset>`; it does **not** automatically associate the form controls nested within that `<fieldset>`.

In this example, the `<fieldset>` and `username` `<input>` are associated with the `exampleForm`, and included in the [`HTMLFormControlsCollection`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormControlsCollection)
 of the [`HTMLFormElement.elements`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements)
 property, but the `password` is not. Only the `username` will be included when the `exampleForm` is submitted:

Each nested element needs its own `form` attribute or must be nested inside the form. You can check which elements are associated with a form via JavaScript, using [HTMLFormElement.elements](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements)
.

### [Form submission](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#form_submission)

Including the `form` attribute does not mean the element will be submitted with the form. Only submittable elements, including `<button>`, `<input>`, `<select>`, and `<textarea>`, have their name and values submitted when their associated `<form>` is submitted.

In this case, even though the `<output>` is implicitly then explicitly associated with the `calcForm`, the `result` is not submitted along with `a` and `b` when `calcForm` is submitted. It is, however, part of the form's `HTMLFormControlsCollection`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#examples)

-------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#basic_example)

This example demonstrates how form-associated elements can be associated with a `<form>` element using the `form` attribute, even if they are not explicitly nested inside it. All of the form-associated elements shown in this example are associated with the `loginForm` either implicitly (by being directly nested inside the form), or explicitly via the `form` attribute. When the login form is submitted, the names and values of each submittable element will be included.

### [Element associated with a different form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#element_associated_with_a_different_form)

In this example, we have two `<form>` elements: `parentForm` and `targetForm`. The `<button>` inside `parentForm` has its `form` attribute set to `targetForm`, disassociating it from its nearest ancestor `parentForm`, while associating it with the `targetForm`. When the submit button is activated, it submits the `targetForm`, not its `parentForm` ancestor.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-fae-form](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

### [html.elements.button.form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#html.elements.button.form)

### [html.elements.fieldset.form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#html.elements.fieldset.form)

### [html.elements.input.form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#html.elements.input.form)

### [html.elements.object.form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#html.elements.object.form)

### [html.elements.output.form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#html.elements.output.form)

### [html.elements.select.form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#html.elements.select.form)

### [html.elements.textarea.form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#html.elements.textarea.form)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form#see_also)

-------------------------------------------------------------------------------------------------

*   [Overriding default form behaviors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#overriding_default_form_behaviors)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/form/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/form (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fform&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fform%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fform%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fform%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8d9cda4e9080e9c324a521f40c7e0704ef94ce07%0A*+Document+last+modified%3A+2026-07-03T08%3A23%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")