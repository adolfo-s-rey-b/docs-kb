*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#mdn-search)
    

`multiple` HTML attribute
=========================

The Boolean **`multiple`** attribute, if set, means the form control accepts one or more values. The attribute is valid for the [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
 and [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
 input types and the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
. The manner by which the user opts for multiple values depends on the form control.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#try_it)

-------------------------------------------------------------------------------------------------

[Overview](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#overview)

-----------------------------------------------------------------------------------------------------

Depending on the type, the form control may have a different appearance if the `multiple` attribute is set. For the file input type, the native messaging the browser provides differs. In Firefox, the file input reads "No files selected" when the attribute is present and "No file selected" when it is not. Most browsers display a scrolling list box for a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 control with the `multiple` attribute set and a single line dropdown when the attribute is omitted. The [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
 input displays the same whether or not the `multiple` attribute is included, but will match the [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 pseudo-class if more than one comma-separated email address is included if the attribute is not present.

When `multiple` is set on the [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
 input type, the user can include zero (if not also [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)
), one or more comma-separated email addresses.

If and only if the `multiple` attribute is specified, the value can be a list of properly-formed comma-separated email addresses. Any trailing and leading whitespace is removed from each address in the list.

When `multiple` is set on the [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
 input type, the user can select one or more files. The user can choose multiple files from the file picker in any way that their chosen platform allows (e.g., by holding down Shift or Control, and then clicking).

When the attribute is omitted, the user can only select a single file per `<input>`.

The `multiple` attribute on the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element represents a control for selecting zero or more options from the list of options. Otherwise, the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element represents a control for selecting a single [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 from the list of options.

When `multiple` is specified, most browsers will show a scrolling list box instead of a single line dropdown.

Multiple selected options are submitted using the [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)
 array convention, i.e., `name=value1&name=value2`.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#accessibility_concerns)

---------------------------------------------------------------------------------------------------------------------------------

Provide instructions to help users understand how to complete the form and use individual form controls. Indicate any required and optional input, data formats, and other relevant information. When using the `multiple` attribute, inform the user that multiple values are allowed and provide directions on how to provide multiple values, such as "separate email addresses with a comma."

Setting `size="1"` on a multiple select (i.e., `<select multiple size="1">`) renders a drop-down that lets users select multiple options. Some browsers don't expand the option list when the control is active, displaying multiple options in a menu list the height of a single-line box. This harms usability. When including a multiple-select, inform users they can select more than one option, even when multiple options are displayed.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#examples)

-----------------------------------------------------------------------------------------------------

### [email input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#email_input)

If and only if the `multiple` attribute is specified, the value can be a list of properly-formed comma-separated email addresses. Any trailing and leading whitespace is removed from each address in the list. If the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)
 attribute is present, at least one email address is required.

Some browsers support the appearance of the [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)
 of options from the associated [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 for subsequent email addresses when `multiple` is present. Others do not.

### [file input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#file_input)

When `multiple` is set on the [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
 input type, the user can select one or more files:

Note the difference in appearance between the example with `multiple` set and the other `file` input without.

If these inputs are included in a form submitted using [`method="get"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, each selected file's name is added to URL parameters as `?uploads=img1.jpg&uploads=img2.svg`. To submit the files as multipart form data, use `method="post"` and `enctype="multipart/form-data"`. See the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element and [sending form data](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Sending_and_retrieving_form_data#the_method_attribute)
 for more information.

### [select](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#select)

The `multiple` attribute on the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element represents a control for selecting zero or more options from the list of options. Otherwise, the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element represents a control for selecting a single [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 from the list of options. The control generally has a different appearance based on the presence of the multiple attribute, with most browsers displaying a scrolling list box instead of a single line dropdown when the attribute is present.

Note the difference in appearance between the two form controls.

There are a few ways to select multiple options in a `<select>` element with a `multiple` attribute. Depending on the operating system, mouse users can hold the Ctrl, Command, or Shift keys and then click multiple options to select/deselect them. Keyboard users can select multiple contiguous items by focusing on the `<select>` element, selecting an item at the top or bottom of the range they want to select using the Up and Down cursor keys to go up and down the options. The selection of non-contiguous is not as well-supported: items should be able to be selected and deselected by pressing Space, but support varies between browsers.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-multiple](https://html.spec.whatwg.org/multipage/input.html#attr-input-multiple) |
| [HTML  <br>\# attr-select-multiple](https://html.spec.whatwg.org/multipage/form-elements.html#attr-select-multiple) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.multiple](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#html.elements.input.multiple)

### [html.elements.select.multiple](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#html.elements.select.multiple)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple#see_also)

-----------------------------------------------------------------------------------------------------

*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    
*   [Allowing multiple email addresses](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#allowing_multiple_email_addresses)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/multiple/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/multiple (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fmultiple&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fmultiple%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fmultiple%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fmultiple%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")