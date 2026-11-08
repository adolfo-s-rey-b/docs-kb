*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#mdn-search)
    

`required` HTML attribute
=========================

The [Boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean/HTML)
 **`required`** attribute, if present, indicates that the user must specify a value for the input before the owning form can be submitted.

The `required` attribute is supported by `[text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text) `, `[search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search) `, `[url](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url) `, `[tel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel) `, `[email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email) `, `[password](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password) `, `[date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date) `, `[month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month) `, `[week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week) `, `[time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time) `, `[datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local) `, `[number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number) `, `[checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox) `, `[radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio) `, `[file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file) `, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 types along with the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 form control elements. If present on any of these input types and elements, the [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
 pseudo class will match. If the attribute is not included, the [`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)
 pseudo class will match.

The attribute is not supported on, or relevant to, [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 and [color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color)
 input types, as both have default values. Type `color` defaults to `#000000`. Type `range` defaults to the midpoint between `min` and `max` — with `min` and `max` defaulting to 0 and 100 respectively in most browsers if not declared. `required` is also not supported on the [hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden)
 input type — users cannot be expected to fill out a hidden form field. Finally, `required` is not supported on any button input types, including [image](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
.

In the case of a same named group of [radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
 buttons, if a single radio button in the group has the `required` attribute, a radio button in that group must be checked, although it doesn't have to be the one on which the attribute is applied. To improve code maintenance, it is recommended to either include the `required` attribute in every same-named radio button in the group, or else in none.

In the case of a same named group of [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
 input types, only the checkboxes with the `required` attribute are required.

**Note:** Setting [`aria-required="true"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-required)
 tells a screen reader that an element (any element) is required, but has no bearing on the optionality of the element.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#description)

-----------------------------------------------------------------------------------------------------------

### [Attribute interactions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#attribute_interactions)

Because a read-only field cannot be changed, `required` does not have any effect on inputs with the [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)
 attribute also specified.

### [Usability](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#usability)

When including the `required` attribute, provide a visible indication near the control informing the user that the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 is required. In addition, target required form controls with the [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
 pseudo-class, styling them in a way to indicate they are required. This improves usability for sighted users. Assistive technology should inform the user that the form control is mandatory based on the required attribute, but adding `aria-required="true"` doesn't hurt, in case the browser / screen reader combination does not support `required` yet.

### [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#constraint_validation)

If the element is required and the element's value is the empty string, then the element is suffering from [`valueMissing`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/valueMissing "valueMissing")
 and the element will match the [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 pseudo class.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#accessibility_concerns)

---------------------------------------------------------------------------------------------------------------------------------

Provide an indication to users informing them the form control is required. Ensure the messaging is multi-faceted, such as through text, color, markings, and attribute, so that all users understand the requirements whether they have color blindness, cognitive differences, or are using a screen reader.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#example)

---------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#html)

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-required](https://html.spec.whatwg.org/multipage/input.html#attr-input-required) |
| [HTML  <br>\# attr-select-required](https://html.spec.whatwg.org/multipage/form-elements.html#attr-select-required) |
| [HTML  <br>\# attr-textarea-required](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-required) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#html.elements.input.required)

### [html.elements.select.required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#html.elements.select.required)

### [html.elements.textarea.required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#html.elements.textarea.required)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required#see_also)

-----------------------------------------------------------------------------------------------------

*   [`validityState.valueMissing`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/valueMissing)
    
*   [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
     and [`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/required/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/required (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frequired&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frequired%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frequired%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frequired%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")