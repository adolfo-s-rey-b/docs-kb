*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#mdn-search)
    

`<input type="tel">` HTML attribute value
=========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`tel`** are used to let the user enter and edit a telephone number. Unlike [`<input type="email">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
 and [`<input type="url">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
, the input value is not automatically validated to a particular format before the form can be submitted, because formats for telephone numbers vary so much around the world.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#try_it)

------------------------------------------------------------------------------------------------

    <label for="phone">
      Enter your phone number:<br />
      <small>Format: 123-456-7890</small>
    </label>
    
    <input
      type="tel"
      id="phone"
      name="phone"
      pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
      required />
    

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
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#value)

----------------------------------------------------------------------------------------------

The [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute contains a string that either represents a telephone number or is an empty string (`""`).

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#additional_attributes)

------------------------------------------------------------------------------------------------------------------------------

In addition to the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 and the attributes that operate on all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements regardless of their type, telephone number inputs support the following attributes.

### [list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#list)

The values of the list attribute is the [`id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id "id")
 of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element located in the same document. The [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 provides a list of predefined values to suggest to the user for this input. Any values in the list that are not compatible with the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 are not included in the suggested options. The values provided are suggestions, not requirements: users can select from this predefined list or provide a different value.

### [maxlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#maxlength)

The maximum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the telephone number field. This must be an integer value of 0 or higher. If no `maxlength` is specified, or an invalid value is specified, the telephone number field has no maximum length. This value must also be greater than or equal to the value of `minlength`.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is greater than `maxlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [minlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#minlength)

The minimum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the telephone number field. This must be a non-negative integer value smaller than or equal to the value specified by `maxlength`. If no `minlength` is specified, or an invalid value is specified, the telephone number input has no minimum length.

The telephone number field will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is fewer than `minlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#pattern)

The `pattern` attribute, when specified, is a regular expression that the input's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 must match for the value to pass [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. It must be a valid JavaScript regular expression, as used by the [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 type, and as documented in our [guide on regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
; the `'u'` flag is specified when compiling the regular expression so that the pattern is treated as a sequence of Unicode code points, instead of as [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
. No forward slashes should be specified around the pattern text.

If the specified pattern is not specified or is invalid, no regular expression is applied and this attribute is ignored completely.

**Note:** Use the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#title)
 attribute to specify text that most browsers will display as a tooltip to explain what the requirements are to match the pattern. You should also include other explanatory text nearby.

See [Pattern validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#pattern_validation)
 below for details and an example.

### [placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#placeholder)

The `placeholder` attribute is a string that provides a brief hint to the user as to what kind of information is expected in the field. It should be a word or short phrase that demonstrates the expected type of data, rather than an explanatory message. The text _must not_ include carriage returns or line feeds.

If the control's content has one directionality ([LTR](https://developer.mozilla.org/en-US/docs/Glossary/LTR)
 or [RTL](https://developer.mozilla.org/en-US/docs/Glossary/RTL)
) but needs to present the placeholder in the opposite directionality, you can use Unicode bidirectional algorithm formatting characters to override directionality within the placeholder; see [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls "External link (opens in new tab)")
 for more information.

**Note:** Avoid using the `placeholder` attribute if you can. It is not as semantically useful as other ways to explain your form, and can cause unexpected technical issues with your content. See [`<input>` labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
 for more information.

### [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#readonly)

A Boolean attribute which, if present, means this field cannot be edited by the user. Its `value` can, however, still be changed by JavaScript code directly setting the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 `value` property.

**Note:** Because a read-only field cannot have a value, `required` does not have any effect on inputs with the `readonly` attribute also specified.

### [size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#size)

The `size` attribute is a numeric value indicating how many characters wide the input field should be. The value must be a number greater than zero, and the default value is 20. Since character widths vary, this may or may not be exact and should not be relied upon to be so; the resulting input may be narrower or wider than the specified number of characters, depending on the characters and the font ([`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 settings in use).

This does _not_ set a limit on how many characters the user can enter into the field. It only specifies approximately how many can be seen at a time. To set an upper limit on the length of the input data, use the [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#maxlength)
 attribute.

[Using tel inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#using_tel_inputs)

--------------------------------------------------------------------------------------------------------------------

Despite the fact that inputs of type `tel` are functionally identical to standard `text` inputs, they do serve useful purposes; the most quickly apparent of these is that mobile browsers — especially on mobile phones — may opt to present a custom keypad optimized for entering phone numbers. Using a specific input type for telephone numbers also makes adding custom validation and handling of phone numbers more convenient.

**Note:** Browsers that don't support type `tel` fall back to being a standard [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
 input.

Telephone numbers are a very commonly collected type of data on the web. When creating any kind of registration or e-commerce site, for example, you will likely need to ask the user for a telephone number, whether for business purposes or for emergency contact purposes. Given how commonly-entered phone numbers are, it's unfortunate that a "one size fits all" solution for validating phone numbers is not practical.

Fortunately, you can consider the requirements of your own site and implement an appropriate level of validation yourself. See [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#validation)
, below, for details.

### [Custom keyboards](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#custom_keyboards)

One of the main advantages of `<input type="tel">` is that it causes mobile browsers to display a special keyboard for entering phone numbers. For example, here's what the keypads look like on a couple of devices.

| Firefox for Android | WebKit iOS (Safari/Chrome/Firefox) |
| --- | --- |
| ![Firefox for Android screen shot](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel/fx-android-tel.png) | ![Firefox for iOS screenshot](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel/iphone-tel-keyboard-50pct.png) |

### [A basic tel input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#a_basic_tel_input)

In its most basic form, a tel input can be implemented like this:

html

    <label for="telNo">Phone number:</label>
    <input id="telNo" name="telNo" type="tel" />
    

There is nothing magical going on here. When submitted to the server, the above input's data would be represented as, for example, `telNo=+12125553151`.

### [Placeholders](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#placeholders)

Sometimes it's helpful to offer an in-context hint as to what form the input data should take. This can be especially important if the page design doesn't offer descriptive labels for each [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
. This is where **placeholders** come in. A placeholder is a value that demonstrates the form the `value` should take by presenting an example of a valid value, which is displayed inside the edit box when the element's `value` is `""`. Once data is entered into the box, the placeholder disappears; if the box is emptied, the placeholder reappears.

Here, we have a `tel` input with the placeholder `123-4567-8901`. Note how the placeholder disappears and reappears as you manipulate the contents of the edit field.

html

    <input id="telNo" name="telNo" type="tel" placeholder="123-4567-8901" />
    

### [Controlling the input size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#controlling_the_input_size)

You can control not only the physical length of the input box, but also the minimum and maximum lengths allowed for the input text itself.

#### Physical input element size

The physical size of the input box can be controlled using the [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
 attribute. With it, you can specify the number of characters the input box can display at a time. In this example, for instance, the `tel` edit box is 20 characters wide:

html

    <input id="telNo" name="telNo" type="tel" size="20" />
    

#### Element value length

The `size` is separate from the length limitation on the entered telephone number. You can specify a minimum length, in characters, for the entered telephone number using the [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)
 attribute; similarly, use [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
 to set the maximum length of the entered telephone number.

The example below creates a 20-character wide telephone number entry box, requiring that the contents be no shorter than 9 characters and no longer than 14 characters.

html

    <input
      id="telNo"
      name="telNo"
      type="tel"
      size="20"
      minlength="9"
      maxlength="14" />
    

**Note:** The above attributes do affect [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#validation)
 — the above example's inputs will count as invalid if the length of the value is less than 9 characters, or more than 14. Most browser won't even let you enter a value over the max length.

### [Providing default options](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#providing_default_options)

#### Providing a single default using the value attribute

As always, you can provide a default value for a `tel` input box by setting its [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute:

html

    <input id="telNo" name="telNo" type="tel" value="333-4444-4444" />
    

#### Offering suggested values

Taking it a step further, you can provide a list of default phone number values from which the user can select. To do this, use the [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)
 attribute. This doesn't limit the user to those options, but does allow them to select commonly-used telephone numbers more quickly. This also offers hints to [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)
. The `list` attribute specifies the ID of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element, which in turn contains one [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 element per suggested value; each `option`'s `value` is the corresponding suggested value for the telephone number entry box.

html

    <label for="telNo">Phone number: </label>
    <input id="telNo" name="telNo" type="tel" list="defaultTels" />
    
    <datalist id="defaultTels">
      <option value="111-1111-1111"></option>
      <option value="122-2222-2222"></option>
      <option value="333-3333-3333"></option>
      <option value="344-4444-4444"></option>
    </datalist>
    

With the [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element and its [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
s in place, the browser will offer the specified values as potential values for the phone number; this is typically presented as a popup or drop-down menu containing the suggestions. While the specific user experience may vary from one browser to another, typically clicking in the edit box presents a drop-down of the suggested phone numbers. Then, as the user types, the list is adjusted to show only filtered matching values. Each typed character narrows down the list until the user makes a selection or types a custom value.

Here's a screenshot of what that might look like:

![An input box has focus with a blue focus ring. The input has a drop-down menu showing four phone numbers the user can select.](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel/phone-number-with-options.png)

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#validation)

--------------------------------------------------------------------------------------------------------

As we've touched on before, it's quite difficult to provide a one-size-fits-all client-side validation solution for phone numbers. So what can we do? Let's consider some options.

**Warning:** HTML form validation is _not_ a substitute for server-side scripts that ensure the entered data is in the proper format before it is allowed into the database. It's far too easy for someone to make adjustments to the HTML that allow them to bypass the validation, or to remove it entirely. It's also possible for someone to bypass your HTML entirely and submit the data directly to your server. If your server-side code fails to validate the data it receives, disaster could strike when improperly-formatted data (or data which is too large, is of the wrong type, and so forth) is entered into your database.

### [Making telephone numbers required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#making_telephone_numbers_required)

You can make it so that an empty input is invalid and won't be submitted to the server using the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute. For example, let's use this HTML:

html

    <form>
      <div>
        <label for="telNo">Enter a telephone number (required): </label>
        <input id="telNo" name="telNo" type="tel" required />
        <span class="validity"></span>
      </div>
      <div>
        <button>Submit</button>
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

And let's include the following CSS to highlight valid entries with a checkmark and invalid entries with a cross:

css

    div {
      margin-bottom: 10px;
      position: relative;
    }
    
    input[type="number"] {
      width: 100px;
    }
    
    input + span {
      padding-right: 30px;
    }
    
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
      color: darkred;
    }
    
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
      color: #009000;
    }
    

The output looks like this:

### [Pattern validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#pattern_validation)

If you want to further restrict entered numbers so they also have to conform to a specific pattern, you can use the [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attribute, which takes as its value a [regular expression](https://developer.mozilla.org/en-US/docs/Glossary/Regular_expression)
 that entered values have to match.

In this example we'll use the same CSS as before, but our HTML is changed to look like this:

html

    <form>
      <div>
        <label for="telNo">
          Enter a telephone number (in the form xxx-xxx-xxxx):
        </label>
        <input
          id="telNo"
          name="telNo"
          type="tel"
          required
          pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" />
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
    
    input[type="number"] {
      width: 100px;
    }
    
    input + span {
      padding-right: 30px;
    }
    
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
      color: darkred;
    }
    
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
      color: #009000;
    }
    

Notice how the entered value is reported as invalid unless the pattern xxx-xxx-xxxx is matched; for instance, 41-323-421 won't be accepted. Neither will 800-MDN-ROCKS. However, 865-555-6502 will be accepted. This particular pattern is obviously only useful for certain locales — in a real application you'd probably have to vary the pattern used depending on the locale of the user.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#examples)

----------------------------------------------------------------------------------------------------

In this example, we present a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element that lets the user choose which country they're in, and a set of `<input type="tel">` elements to let them enter each part of their phone number; there is no reason why you can't have multiple `tel` inputs.

Each input has a [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
 attribute to show a hint to sighted users about what to enter into it, a [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 to enforce a specific number of characters for the desired section, and an [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
 attribute to contain a hint to be read out to screen reader users about what to enter into it.

html

    <div>
      <label for="country">Choose your country:</label>
      <select id="country" name="country">
        <option>UK</option>
        <option selected>US</option>
        <option>Germany</option>
      </select>
    </div>
    <div>
      <p>Enter your telephone number:</p>
      <span class="areaDiv">
        <input
          id="areaNo"
          name="areaNo"
          type="tel"
          required
          placeholder="Area code"
          pattern="[0-9]{3}"
          aria-label="Area code" />
        <span class="validity"></span>
      </span>
      <span class="number1Div">
        <input
          id="number1"
          name="number1"
          type="tel"
          required
          placeholder="First part"
          pattern="[0-9]{3}"
          aria-label="First part of number" />
        <span class="validity"></span>
      </span>
      <span class="number2Div">
        <input
          id="number2"
          name="number2"
          type="tel"
          required
          placeholder="Second part"
          pattern="[0-9]{4}"
          aria-label="Second part of number" />
        <span class="validity"></span>
      </span>
    </div>
    

The JavaScript contains an [`onchange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "onchange")
 event handler that, when the `<select>` value is changed, updates the `<input>` element's `pattern`, `placeholder`, and `aria-label` to suit the format of telephone numbers in that country/territory.

js

    const selectElem = document.querySelector("select");
    const inputElems = document.querySelectorAll("input");
    
    selectElem.onchange = () => {
      for (const e of inputElems) {
        e.value = "";
      }
    
      if (selectElem.value === "US") {
        inputElems[2].parentNode.style.display = "inline";
    
        inputElems[0].placeholder = "Area code";
        inputElems[0].pattern = "[0-9]{3}";
    
        inputElems[1].placeholder = "First part";
        inputElems[1].pattern = "[0-9]{3}";
        inputElems[1].setAttribute("aria-label", "First part of number");
    
        inputElems[2].placeholder = "Second part";
        inputElems[2].pattern = "[0-9]{4}";
        inputElems[2].setAttribute("aria-label", "Second part of number");
      } else if (selectElem.value === "UK") {
        inputElems[2].parentNode.style.display = "none";
    
        inputElems[0].placeholder = "Area code";
        inputElems[0].pattern = "[0-9]{3,6}";
    
        inputElems[1].placeholder = "Local number";
        inputElems[1].pattern = "[0-9]{4,8}";
        inputElems[1].setAttribute("aria-label", "Local number");
      } else if (selectElem.value === "Germany") {
        inputElems[2].parentNode.style.display = "inline";
    
        inputElems[0].placeholder = "Area code";
        inputElems[0].pattern = "[0-9]{3,5}";
    
        inputElems[1].placeholder = "First part";
        inputElems[1].pattern = "[0-9]{2,4}";
        inputElems[1].setAttribute("aria-label", "First part of number");
    
        inputElems[2].placeholder = "Second part";
        inputElems[2].pattern = "[0-9]{4}";
        inputElems[2].setAttribute("aria-label", "Second part of number");
      }
    };
    

The example looks like this:

This is an interesting idea, which goes to show a potential solution to the problem of dealing with international phone numbers. You would have to extend the example of course to provide the correct pattern for potentially every country, which would be a lot of work, and there would still be no foolproof guarantee that the users would enter their numbers correctly.

It makes you wonder if it is worth going to all this trouble on the client-side, when you could just let the user enter their number in whatever format they wanted on the client-side and then validate and sanitize it on the server. But this choice is yours to make.

    div {
      margin-bottom: 10px;
      position: relative;
    }
    
    input[type="number"] {
      width: 100px;
    }
    
    input + span {
      padding-right: 30px;
    }
    
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
      color: darkred;
    }
    
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
      color: #009000;
    }
    

[Technical Summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#technical_summary)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#value)<br>** | A string representing a telephone number, or empty |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported common attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)<br>, [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)<br>, [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)<br>, [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)<br>, [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly)<br>, and [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size) |
| **IDL attributes** | `list`, `selectionStart`, `selectionEnd`, `selectionDirection`, and `value` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | with no `list` attribute: `[textbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role) `  <br>with `list` attribute: `[combobox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role) ` |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# telephone-state-(type=tel)](https://html.spec.whatwg.org/multipage/input.html#telephone-state-(type=tel)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel#see_also)

----------------------------------------------------------------------------------------------------

*   [HTML forms guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    *   [`<input type="text">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
        
    *   [`<input type="email">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/tel/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/tel (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Ftel&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Ftel%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Ftel%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Ftel%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")