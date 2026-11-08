*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#mdn-search)
    

`<input type="text">` HTML attribute value
==========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`text`** create basic single-line text fields.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#try_it)

-------------------------------------------------------------------------------------------------

    <label for="name">Name (4 to 8 characters):</label>
    
    <input
      type="text"
      id="name"
      name="name"
      required
      minlength="4"
      maxlength="8"
      size="10" />
    

    label {
      display: block;
      font:
        1rem "Fira Sans",
        sans-serif;
    }
    
    input,
    label {
      margin: 0.4rem 0;
    }
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#value)

-----------------------------------------------------------------------------------------------

The [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute is a string that contains the current value of the text entered into the text field. You can retrieve this using the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 `value` property in JavaScript.

js

    let theText = myTextInput.value;
    

If no validation constraints are in place for the input (see [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#validation)
 for more details), the value may be an empty string (`""`).

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#additional_attributes)

-------------------------------------------------------------------------------------------------------------------------------

In addition to the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 and the attributes that operate on all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements regardless of their type, text inputs support the following attributes.

### [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#list)

The values of the list attribute is the [`id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id "id")
 of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element located in the same document. The [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 provides a list of predefined values to suggest to the user for this input. Any values in the list that are not compatible with the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 are not included in the suggested options. The values provided are suggestions, not requirements: users can select from this predefined list or provide a different value.

### [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#maxlength)

The maximum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the `text` input. This must be an integer value of 0 or higher. If no `maxlength` is specified, or an invalid value is specified, the `text` input has no maximum length. This value must also be greater than or equal to the value of `minlength`.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text value of the field is greater than `maxlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#minlength)

The minimum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the `text` input. This must be a non-negative integer value smaller than or equal to the value specified by `maxlength`. If no `minlength` is specified, or an invalid value is specified, the `text` input has no minimum length.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is fewer than `minlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#pattern)

The `pattern` attribute, when specified, is a regular expression that the input's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 must match for the value to pass [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. It must be a valid JavaScript regular expression, as used by the [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 type, and as documented in our [guide on regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
; the `'u'` flag is specified when compiling the regular expression so that the pattern is treated as a sequence of Unicode code points, instead of as [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
. No forward slashes should be specified around the pattern text.

If the specified pattern is not specified or is invalid, no regular expression is applied and this attribute is ignored completely.

**Note:** Use the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#title)
 attribute to specify text that most browsers will display as a tooltip to explain what the requirements are to match the pattern. You should also include other explanatory text nearby.

See [Specifying a pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#specifying_a_pattern)
 for further details and an example.

### [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#placeholder)

The `placeholder` attribute is a string that provides a brief hint to the user as to what kind of information is expected in the field. It should be a word or short phrase that demonstrates the expected type of data, rather than an explanatory message. The text _must not_ include carriage returns or line feeds.

If the control's content has one directionality ([LTR](https://developer.mozilla.org/en-US/docs/Glossary/LTR)
 or [RTL](https://developer.mozilla.org/en-US/docs/Glossary/RTL)
) but needs to present the placeholder in the opposite directionality, you can use Unicode bidirectional algorithm formatting characters to override directionality within the placeholder; see [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls "External link (opens in new tab)")
 for more information.

**Note:** Avoid using the `placeholder` attribute if you can. It is not as semantically useful as other ways to explain your form, and can cause unexpected technical issues with your content. See [`<input>` accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#accessibility)
 for more information.

### [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#readonly)

A Boolean attribute which, if present, means this field cannot be edited by the user. Its `value` can, however, still be changed by JavaScript code directly setting the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 `value` property.

**Note:** Because a read-only field cannot have a value, `required` does not have any effect on inputs with the `readonly` attribute also specified.

### [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#size)

The `size` attribute is a numeric value indicating how many characters wide the input field should be. The value must be a number greater than zero, and the default value is 20. Since character widths vary, this may or may not be exact and should not be relied upon to be so; the resulting input may be narrower or wider than the specified number of characters, depending on the characters and the font ([`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 settings in use).

This does _not_ set a limit on how many characters the user can enter into the field. It only specifies approximately how many can be seen at a time. To set an upper limit on the length of the input data, use the [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#maxlength)
 attribute.

### [`spellcheck`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#spellcheck)

The [`spellcheck`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck)
 global attribute is used to indicate whether to enable spell-checking for an element. It can be used on any editable content, but here we consider specifics related to the use of `spellcheck` on [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements. The permitted values for `spellcheck` are:

[`false`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#false)

Disable spell-checking for this element.

[`true`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#true)

Enable spell-checking for this element.

[`""` (empty string) or no value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#sect)

Follow the element's default behavior for spell-checking. This may be based upon a parent's `spellcheck` setting or other factors.

An input field can have spell-checking enabled if it doesn't have the [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#readonly)
 attribute set and is not disabled.

The value returned by reading `spellcheck` may not reflect the actual state of spell-checking within a control, if the [user agent's](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 preferences override the setting.

[Using text inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#using_text_inputs)

-----------------------------------------------------------------------------------------------------------------------

`<input>` elements of type `text` create basic, single-line inputs. You should use them anywhere you want the user to enter a single-line value and there isn't a more specific input type available for collecting that value (for example, if it's a [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
, [URL](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
, [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
, or [search term](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search)
, you've got better options available).

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#basic_example)

html

    <div>
      <label for="uname">Choose a username: </label>
      <input type="text" id="uname" name="name" />
    </div>
    

This renders like so:

If this input is included in a form and submitted, the data name/value pair sent to the server will be `name=Chris` (if "Chris" was entered as the input value before submission). You must remember to include [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name)
 attribute on the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element, otherwise the text field's value won't be included with the submitted data.

### [Setting placeholders](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#setting_placeholders)

You can provide a useful placeholder inside your text input that can provide a hint as to what to enter by including using the [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
 attribute. Look at the following example:

html

    <div>
      <label for="uname">Choose a username: </label>
      <input
        type="text"
        id="uname"
        name="name"
        placeholder="Lower case, all one word" />
    </div>
    

You can see how the placeholder is rendered below:

The placeholder is typically rendered in a lighter color than the element's foreground color, and automatically vanishes when the user begins to enter text into the field (or whenever the field has a value set programmatically by setting its `value` attribute).

### [Physical input element size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#physical_input_element_size)

The physical size of the input box can be controlled using the [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
 attribute. With it, you can specify the number of characters the text input can display at a time. This affects the width of the element, letting you specify the width in terms of characters rather than pixels. In this example, for instance, the input is 30 characters wide:

html

    <div>
      <label for="uname">Choose a username: </label>
      <input
        type="text"
        id="uname"
        name="name"
        placeholder="Lower case, all one word"
        size="30" />
    </div>
    

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#validation)

---------------------------------------------------------------------------------------------------------

`<input>` elements of type `text` have no automatic validation applied to them (since a basic text input needs to be capable of accepting any arbitrary string), but there are some client-side validation options available, which we'll discuss below.

**Note:** HTML form validation is _not_ a substitute for server-scripts that ensure the entered data is in the proper format. It's far too easy for someone to make adjustments to the HTML that allow them to bypass the validation, or to remove it entirely. It's also possible for someone to bypass your HTML entirely and submit the data directly to your server. If your server-side code fails to validate the data it receives, disaster could strike when improperly-formatted data (or data which is too large, is of the wrong type, and so forth) is entered into your database.

### [A note on styling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#a_note_on_styling)

There are useful pseudo-classes available for styling form elements to help the user see when their values are valid or invalid. These are [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
. In this section, we'll use the following CSS, which will place a check (tick) mark next to inputs containing valid values, and a cross (X) next to inputs containing invalid values.

css

    div {
      margin-bottom: 10px;
      position: relative;
    }
    
    input + span {
      padding-right: 30px;
    }
    
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
    }
    
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
    }
    

The technique also requires a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 element to be placed after the form element, which acts as a holder for the icons. This was necessary because some input types on some browsers don't display icons placed directly after them very well.

### [Making input required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#making_input_required)

You can use the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute as an easy way of making entering a value required before form submission is allowed:

html

    <form>
      <div>
        <label for="uname">Choose a username: </label>
        <input type="text" id="uname" name="name" required />
        <span class="validity"></span>
      </div>
      <div>
        <button>Submit</button>
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

    div {
      margin-bottom: 10px;
      position: relative;
    }
    input + span {
      padding-right: 30px;
    }
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
    }
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
    }
    

This renders like so:

If you try to submit the form with no username entered into it, the browser will show an error message.

### [Input value length](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#input_value_length)

You can specify a minimum length (in characters) for the entered value using the [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)
 attribute; similarly, use [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
 to set the maximum length of the entered value, in characters.

The example below requires that the entered value be 4–8 characters in length.

html

    <form>
      <div>
        <label for="uname">Choose a username: </label>
        <input
          type="text"
          id="uname"
          name="name"
          required
          size="10"
          placeholder="Username"
          minlength="4"
          maxlength="8" />
        <span class="validity"></span>
      </div>
      <div>
        <button>Submit</button>
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

    div {
      margin-bottom: 10px;
      position: relative;
    }
    input + span {
      padding-right: 30px;
    }
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
    }
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
    }
    

This renders like so:

If you try to submit the form with less than 4 characters, you'll be given an appropriate error message (which differs between browsers). If you try to enter more than 8 characters, the browser won't let you.

**Note:** If you specify a `minlength` but do not specify `required`, the input is considered valid, since the user is not required to specify a value.

### [Specifying a pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#specifying_a_pattern)

You can use the [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attribute to specify a regular expression that the inputted value must match in order to be considered valid (see [Validating against a regular expression](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation#validating_against_a_regular_expression)
 for a crash course on using regular expressions to validate inputs).

The example below restricts the value to 4-8 characters and requires that it contain only lower-case letters.

html

    <form>
      <div>
        <label for="uname">Choose a username: </label>
        <input
          type="text"
          id="uname"
          name="name"
          required
          size="45"
          pattern="[a-z]{4,8}" />
        <span class="validity"></span>
        <p>Usernames must be lowercase and 4-8 characters in length.</p>
      </div>
      <div>
        <button>Submit</button>
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

    div {
      margin-bottom: 10px;
      position: relative;
    }
    
    p {
      font-size: 80%;
      color: #999999;
    }
    
    input + span {
      padding-right: 30px;
    }
    
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
    }
    
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
    }
    

This renders like so:

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#examples)

-----------------------------------------------------------------------------------------------------

You can see good examples of text inputs used in context in our [Your first HTML form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form)
 and [How to structure an HTML form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/How_to_structure_a_web_form)
 articles.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#technical_summary)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#value)<br>** | A string representing the text contained in the text field. |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported Common Attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)<br>, [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)<br>, [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)<br>, [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)<br>, [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly)<br>, [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)<br> and [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size) |
| **IDL attributes** | [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, `value` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | with no `list` attribute: `[textbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role) `  <br>with `list` attribute: `[combobox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role) ` |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# text-(type=text)-state-and-search-state-(type=search)](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text#see_also)

-----------------------------------------------------------------------------------------------------

*   [HTML Forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     and the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
     interface it's based upon.
*   [`<input type="search">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search)
    
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    : Multi-line text input

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/text/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/text (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Ftext&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Ftext%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Ftext%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Ftext%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")