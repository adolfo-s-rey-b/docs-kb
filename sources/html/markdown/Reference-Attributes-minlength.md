*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength#mdn-search)
    

`minlength` HTML attribute
==========================

The **`minlength`** attribute defines the minimum [string length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
 that the user can enter into an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
. The attribute must have an integer value of 0 or higher.

The length is measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
, which is often but not always equal to the number of characters. If no `minlength` is specified, or an invalid value is specified, the input has no minimum length. This value must be less than or equal to the value of [maxlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength)
, otherwise the value will never be valid, as it is impossible to meet both criteria.

The input will fail constraint validation if the length of the text value of the field is less than minlength UTF-16 code units long, with [`validityState.tooShort`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooShort)
 returning `true`. Constraint validation is only applied when the value is changed by the user. Once submission fails, some browsers will display an error message indicating the minimum length required and the current length.

`minlength` does not imply [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)
; an input only violates a `minlength` constraint if the user has input a value. If an input is not `required`, an empty string can be submitted even if `minlength` is set.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength#try_it)

--------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength#examples)

------------------------------------------------------------------------------------------------------

By adding `minlength="5"`, the value must either be empty or five characters or longer to be valid.

We can use pseudoclasses to style the element based on whether the value is valid. The value will be valid as long as it is either null (empty) or five or more characters long. _Lime_ is invalid, _lemon is valid_.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-minlength](https://html.spec.whatwg.org/multipage/input.html#attr-input-minlength) |
| [HTML  <br>\# attr-textarea-minlength](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-minlength) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.minlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength#html.elements.input.minlength)

### [html.elements.textarea.minlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength#html.elements.textarea.minlength)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength#see_also)

------------------------------------------------------------------------------------------------------

*   [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength)
    
*   [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/size)
    
*   [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern)
    
*   [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
    
*   [Form validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/minlength/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/minlength (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fminlength&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fminlength%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fminlength%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fminlength%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")