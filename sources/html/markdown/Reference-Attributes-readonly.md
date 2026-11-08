*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#mdn-search)
    

`readonly` HTML attribute
=========================

The Boolean **`readonly`** attribute, when present, makes the element not mutable, meaning the user cannot edit the control.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#try_it)

-------------------------------------------------------------------------------------------------

[Overview](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#overview)

-----------------------------------------------------------------------------------------------------

If the `readonly` attribute is specified on an input element, because the user cannot edit the input, the element does not participate in constraint validation.

The `readonly` attribute is supported by textual form controls, including:

*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     elements of type:
    *   `[text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text) `
    *   `[search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search) `
    *   `[tel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel) `
    *   `[url](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url) `
    *   `[email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email) `
    *   `[password](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password) `
    *   `[date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date) `
    *   `[month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month) `
    *   `[week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week) `
    *   `[time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time) `
    *   `[datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local) `
    *   `[number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number) `
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    

The attribute is not relevant to all other elements, including [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
. It also does not apply to non-textual input elements, including:

*   `[hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden) `
*   `[range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range) `
*   `[color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color) `
*   `[checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox) `
*   `[radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio) `
*   `[file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file) `
*   `[submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit) `
*   `[image](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image) `
*   `[reset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset) `
*   `[button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button) `

Inputs that support the `readonly` attribute but don't have the attribute set match the [`:read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write)
 pseudo-class. All other elements match the [`:read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only)
 pseudo-class.

### [Attribute interactions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#attribute_interactions)

The difference between [`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)
 and `readonly` is that read-only controls can still function and are still focusable, whereas disabled controls cannot receive focus and are not submitted with the form and generally do not function as controls until they are enabled.

Because a read-only field cannot have its value changed by a user interaction, [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)
 does not have any effect on inputs with the `readonly` attribute also specified.

The only way to modify dynamically the value of the readonly attribute is through a script.

**Note:** The `required` attribute is not permitted on inputs with the `readonly` attribute specified.

### [Usability](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#usability)

Browsers display the `readonly` attribute.

### [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#constraint_validation)

If the element is read-only, then the element's value cannot be updated by the user, and does not participate in constraint validation.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#example)

---------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#html)

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-readonly](https://html.spec.whatwg.org/multipage/input.html#attr-input-readonly) |
| [HTML  <br>\# attr-textarea-readonly](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-readonly) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#html.elements.input.readonly)

### [html.elements.textarea.readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#html.elements.textarea.readonly)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly#see_also)

-----------------------------------------------------------------------------------------------------

*   [`:read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only)
     and [`:read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/readonly/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/readonly (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Freadonly&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Freadonly%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Freadonly%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Freadonly%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc9f3d85f24d7839c9fe36a68d8042d088d906147%0A*+Document+last+modified%3A+2026-09-05T08%3A25%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")