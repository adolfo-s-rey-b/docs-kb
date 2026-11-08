*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#mdn-search)
    

`placeholder` HTML attribute
============================

The **`placeholder`** attribute defines the text displayed in a form control when the control has no value. The placeholder text should provide a brief hint to the user as to the expected type of data that should be entered into the control.

Effective placeholder text includes a word or short phrase that hints at the expected data type, not an explanation or prompt. The placeholder must not be used instead of a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
. As the placeholder is not visible if the value of the form control is not null, using `placeholder` instead of a `<label>` for a prompt harms usability and accessibility.

The `placeholder` attribute is supported by the following input types: `[text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text) `, `[search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search) `, `[url](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url) `, `[tel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel) `, `[email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email) `, and `[password](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password) `. It is also supported by the ``[`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea) `` element. The [example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#example)
 below shows the `placeholder` attribute in use to explain the expected format of an input field.

**Note:** Except in ``[`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea) `` elements, the `placeholder` attribute can't include any line feeds (LF) or carriage returns (CR). If either is included in the value, the placeholder text will be clipped.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#accessibility_concerns)

------------------------------------------------------------------------------------------------------------------------------------

Placeholders should only be used to show an example of the type of data that should be entered into a form; never as a replacement for a `<label>` element; doing so harms accessibility and user experience.

The `<label>` text is visually and programmatically associated with its corresponding form control. Screen readers don't announce placeholder content by default, but they do announce label content; it's the label that informs assistive technology users what data should be entered in the control. Labels also improve user experience for users of pointing devices: When a user clicks, touches, or taps a `<label>`, focus is moved to the label's associated form control.

Placeholders cannot be relied upon as a replacement for a label even for those not relying on assistive technology. Placeholder text is displayed at lower color contrast than the default form control text. This is by design, as you don't want users to be confused by what is placeholder text versus what is a filled-in form field. However, this lack of contrast can cause issues for low-vision users. Additionally, placeholder text disappears from form fields when users start entering text. If the placeholder text contains instructional information or examples that disappear, it can be confusing to users with cognitive issues and can make the form inaccessible if the placeholder contained the label.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#example)

------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#html)

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-placeholder](https://html.spec.whatwg.org/multipage/input.html#attr-input-placeholder) |
| [HTML  <br>\# attr-textarea-placeholder](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-placeholder) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#html.elements.input.placeholder)

### [html.elements.textarea.placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#html.elements.textarea.placeholder)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder#see_also)

--------------------------------------------------------------------------------------------------------

*   HTML [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
    
*   CSS [`:placeholder-shown`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)
     pseudo-class selector
*   CSS [`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
     pseudo-element selector

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/placeholder/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/placeholder (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fplaceholder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fplaceholder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fplaceholder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fplaceholder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")