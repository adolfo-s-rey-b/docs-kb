*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#mdn-search)
    

`maxlength` HTML attribute
==========================

The **`maxlength`** attribute defines the maximum [string length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
 that the user can enter into an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
. The attribute must have an integer value of 0 or higher.

The length is measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
, which is often but not always equal to the number of characters. If no `maxlength` is specified, or an invalid value is specified, the input has no maximum length.

Any `maxlength` value must be greater than or equal to the value of [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength)
, if present and valid. The input will fail constraint validation if the length of the text value of the field is greater than maxlength UTF-16 code units long. Constraint validation is only applied when the value is changed by the user.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#try_it)

--------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#description)

------------------------------------------------------------------------------------------------------------

### [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#constraint_validation)

While the browser will generally prevent user from entering more text than the maxlength attribute allows, should the length be longer than the maxlength allows, the read-only [`tooLong`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooLong "tooLong")
 property of a [`ValidityState`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)
 object will be true.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#examples)

------------------------------------------------------------------------------------------------------

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-maxlength](https://html.spec.whatwg.org/multipage/input.html#attr-input-maxlength) |
| [HTML  <br>\# attr-textarea-maxlength](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-maxlength) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.maxlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#html.elements.input.maxlength)

### [html.elements.textarea.maxlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#html.elements.textarea.maxlength)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength#see_also)

------------------------------------------------------------------------------------------------------

*   [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength)
    
*   [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/size)
    
*   [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern)
    
*   [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
    
*   [Form validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/maxlength/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/maxlength (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fmaxlength&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fmaxlength%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fmaxlength%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fmaxlength%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")