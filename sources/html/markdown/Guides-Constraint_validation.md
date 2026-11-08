*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#mdn-search)
    

Using HTML form validation and the Constraint Validation API
============================================================

The creation of web forms has always been a complex task. While marking up the form itself is easy, checking whether each field has a valid and coherent value is more difficult, and informing the user about the problem may become a headache. [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
 introduced new mechanisms for forms: it added new semantic types for the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element and _constraint validation_ to ease the work of checking the form content on the client side. Basic, usual constraints can be checked, without the need for JavaScript, by setting new attributes; more complex constraints can be tested using the Constraint Validation API.

For a basic introduction to these concepts, with examples, see the [Form validation tutorial](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
.

**Note:** HTML Constraint validation doesn't remove the need for validation on the _server side_. Even though far fewer invalid form requests are to be expected, invalid ones can still be sent in many ways:

*   By modifying HTML via the browser's developer tools.
*   By hand-crafting an HTTP request without using the form.
*   By programmatically writing content into the form (certain constraint validations are _only run_ for user input, and not if you set the value of a form field using JavaScript).

Therefore, you should always validate form data on the server side, consistent with what is done on the client side.

[Intrinsic and basic constraints](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#intrinsic_and_basic_constraints)

--------------------------------------------------------------------------------------------------------------------------------------------------

In HTML, basic constraints are declared in two ways:

*   By choosing the most semantically appropriate value for the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
     attribute of the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element, e.g., choosing the `email` type automatically creates a constraint that checks whether the value is a valid email address.
*   By setting values on validation-related attributes, allowing basic constraints to be described without the need for JavaScript.

### [Semantic input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#semantic_input_types)

The intrinsic constraints for the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 attribute are:

| Input type | Constraint description | Associated violation |
| --- | --- | --- |
| [`<input type="URL">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url) | The value must be an absolute [URL](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)<br>, as defined in the [URL Living Standard](https://url.spec.whatwg.org/ "External link (opens in new tab)")<br>. | **[TypeMismatch](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/typeMismatch)<br>** constraint violation |
| [`<input type="email">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email) | The value must be a syntactically valid email address, which generally has the format `username@hostname.tld` but can also be local such as `username@hostname`. | **[TypeMismatch](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/typeMismatch)<br>** constraint violation |

For the `email` input type, if the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#multiple)
 attribute is set, several values can be set as a comma-separated list. If any of the values in the list do not satisfy the condition described here, the **Type mismatch** constraint violation is triggered.

Note that most input types don't have intrinsic constraints, as some are barred from constraint validation or have a sanitization algorithm transforming incorrect values to a correct default.

### [Validation-related attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#validation-related_attributes)

In addition to the `type` attribute described above, the following attributes are used to describe basic constraints:

| Attribute | Input types supporting the attribute | Possible values | Constraint description | Associated violation |
| --- | --- | --- | --- | --- |
| `[pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern) ` | `text`, `search`, `url`, `tel`, `email`, `password` | A [JavaScript regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)<br> (compiled with the [`global`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/global)<br>, [`ignoreCase`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/ignoreCase)<br>, and [`multiline`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/multiline)<br> flags _disabled_) | The value must match the pattern. | [**`patternMismatch`**](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/patternMismatch)<br> constraint violation |
| `[min](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min) ` | `range`, `number` | A valid number | The value must be greater than or equal to the value. | **`[rangeUnderflow](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeUnderflow) `** constraint violation |
| `date`, `month`, `week` | A valid date |
| `datetime-local`, `time` | A valid date and time |
| `[max](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max) ` | `range`, `number` | A valid number | The value must be less than or equal to the value | **`[rangeOverflow](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeOverflow) `** constraint violation |
| `date`, `month`, `week` | A valid date |
| `datetime-local`, `time` | A valid date and time |
| `[required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required) ` | `text`, `search`, `url`, `tel`, `email`, `password`, `date`, `datetime-local`, `month`, `week`, `time`, `number`, `checkbox`, `radio`, `file`; also on the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br> and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)<br> elements | _none_ as it is a Boolean attribute: its presence means _true_, its absence means _false_ | There must be a value (if set). | **`[valueMissing](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/valueMissing) `** constraint violation |
| `[step](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step) ` | `date` | An integer number of days | Unless the step is set to the `any` literal, the value must be **min** + an integral multiple of the step. | **`[stepMismatch](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/stepMismatch) `** constraint violation |
| `month` | An integer number of months |
| `week` | An integer number of weeks |
| `datetime-local`, `time` | An integer number of seconds |
| `range`, `number` | An integer |
| `[minlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength) ` | `text`, `search`, `url`, `tel`, `email`, `password`; also on the [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)<br> element | An integer length | The number of characters (code points) must not be less than the value of the attribute, if non-empty. All newlines are normalized to a single character (as opposed to CRLF pairs) for [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)<br>. | **`[tooShort](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooShort) `** constraint violation |
| `[maxlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength) ` | `text`, `search`, `url`, `tel`, `email`, `password`; also on the [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)<br> element | An integer length | The number of characters (code points) must not exceed the value of the attribute. | **`[tooLong](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooLong) `** constraint violation |

[Constraint validation process](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#constraint_validation_process)

----------------------------------------------------------------------------------------------------------------------------------------------

Constraint validation is done through the Constraint Validation API either on a single form element or at the form level, on the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element itself. The constraint validation is done in the following ways:

*   By a call to the `checkValidity()` or `reportValidity()` method of a form-associated DOM interface, ([`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
    , [`HTMLSelectElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement)
    , [`HTMLButtonElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLButtonElement)
    , [`HTMLOutputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOutputElement)
     or [`HTMLTextAreaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTextAreaElement)
    ), which evaluates the constraints only on this element, allowing a script to get this information. The `checkValidity()` method returns a Boolean indicating whether the element's value passes its constraints. (This is typically done by the user-agent when determining which of the CSS pseudo-classes, [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
     or [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
    , applies.) In contrast, the `reportValidity()` method reports any constraint failures to the user.
*   By a call to the `checkValidity()` or `reportValidity()` method on the [`HTMLFormElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement)
     interface.
*   By submitting the form itself.

Calling `checkValidity()` is called _statically_ validating the constraints, while calling `reportValidity()` or submitting the form is called _interactively_ validating the constraints.

**Note:**

*   If the [`novalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#novalidate)
     attribute is set on the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
     element, interactive validation of the constraints doesn't happen.
*   Calling the `submit()` method on the [`HTMLFormElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement)
     interface doesn't trigger a constraint validation. In other words, this method sends the form data to the server even if it doesn't satisfy the constraints. Call the `click()` method on a submit button instead.
*   The `minlength` and `maxlength` constraints are only checked on user-provided input. They are not checked if a value is set programmatically, even when explicitly calling `checkValidity()` or `reportValidity()`.

[Complex constraints using the Constraint Validation API](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#complex_constraints_using_the_constraint_validation_api)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Using JavaScript and the Constraint API, it is possible to implement more complex constraints, for example, constraints combining several fields, or constraints involving complex calculations.

Basically, the idea is to trigger JavaScript on some form field event (like **onchange**) to calculate whether the constraint is violated, and then to use the method `field.setCustomValidity()` to set the result of the validation: an empty string means the constraint is satisfied, and any other string means there is an error and this string is the error message to display to the user.

### [Constraint combining several fields: Postal code validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#constraint_combining_several_fields_postal_code_validation)

The postal code format varies from one country to another. Many countries allow an optional prefix with the country code (like `D-` in Germany, `F-` in France, and `CH-` in Switzerland). Some countries use only a fixed number of digits in postal codes, while others, like the UK, have more complex formats that allow letters at some specific positions.

**Note:** This is not a comprehensive postal code validation library, but rather a demonstration of the key concepts.

As an example, we will add a script checking the constraint validation for a form:

This displays the following form:

First, we write a function checking the constraint itself:

Then we link it to the `change` event for the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 and the `input` event for the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
:

### [Limiting the size of a file before its upload](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#limiting_the_size_of_a_file_before_its_upload)

Another common constraint is to limit the size of a file to be uploaded. Checking this on the client side before the file is transmitted to the server requires combining the Constraint Validation API, and especially the `field.setCustomValidity()` method, with another JavaScript API, here the File API.

Here is the HTML part:

html

    <label for="fs">Select a file smaller than 75 kB: </label>
    <input type="file" id="fs" />
    

This displays:

The JavaScript reads the file selected, uses the `File.size()` method to get its size, compares it to the (hard coded) limit, and calls the Constraint API to inform the browser if there is a violation:

js

    const fs = document.getElementById("fs");
    
    function checkFileSize() {
      const files = fs.files;
    
      // If there is (at least) one file selected
      if (files.length > 0) {
        if (files[0].size > 75 * 1000) {
          // Check the constraint
          fs.setCustomValidity("The selected file must not be larger than 75 kB");
          fs.reportValidity();
          return;
        }
      }
      // No custom constraint violation
      fs.setCustomValidity("");
    }
    

Finally, we hook the method with the correct event:

js

    fs.addEventListener("change", checkFileSize);
    

[Visual styling of constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#visual_styling_of_constraint_validation)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Apart from setting constraints, web developers want to control what messages are displayed to the users and how they are styled.

### [Controlling the look of elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#controlling_the_look_of_elements)

The look of elements can be controlled via CSS pseudo-classes.

#### :required and :optional CSS pseudo-classes

The [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
 and [`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)
 [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 allow writing selectors that match form elements that have the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute, or that don't have it.

#### :placeholder-shown CSS pseudo-class

See [`:placeholder-shown`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)
.

#### :valid :invalid CSS pseudo-classes

The [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 are used to represent <input> elements whose content validates and fails to validate respectively according to the input's type setting. These classes allow the user to style valid or invalid form elements to make it easier to identify elements that are either formatted correctly or incorrectly.

### [Controlling the text of constraint violation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation#controlling_the_text_of_constraint_violation)

The following items can help with controlling the text of a constraint violation:

*   The `setCustomValidity(message)` method on the following elements:
    
    *   [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
        . Note: Setting a custom validity message on fieldset elements will not prevent form submission in most browsers.
    *   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
        
    *   [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
        
    *   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
        
    *   Submit buttons (created with either a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
         element with the `submit` type, or an `input` element with the [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
         type). Other types of buttons do not participate in constraint validation.
    *   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
        
*   The [`ValidityState`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)
     interface describes the object returned by the `validity` property of the element types listed above. It represents various ways that an entered value can be invalid. Together, they help explain why an element's value fails to validate, if it's not valid.
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/guides/constraint_validation/index.md?plain=1 "Folder: en-us/web/html/guides/constraint_validation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FConstraint_validation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fguides%2Fconstraint_validation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FConstraint_validation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fguides%2Fconstraint_validation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")