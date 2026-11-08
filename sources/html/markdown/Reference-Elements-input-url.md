*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#mdn-search)
    

`<input type="url">` HTML attribute value
=========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`url`** are used to let the user enter and edit a URL.

The input value is automatically validated to ensure that it's either empty or a properly-formatted URL before the form can be submitted. The [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 CSS pseudo-classes are automatically applied as appropriate to visually denote whether the current value of the field is a valid URL or not.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#try_it)

------------------------------------------------------------------------------------------------

    <label for="url">Enter an https:// URL:</label>
    <input
      type="url"
      name="url"
      id="url"
      placeholder="https://example.com"
      pattern="https://.*"
      size="30"
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
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#value)

----------------------------------------------------------------------------------------------

The [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute contains a string that is automatically validated as conforming to URL syntax. More specifically, there are two possible value formats that will pass validation:

1.  An empty string ("") indicates the user did not enter a value or that the value was removed.
2.  A single properly-formed absolute URL. This doesn't necessarily mean the URL address exists, but it is at least formatted correctly. An entry matching `urlscheme://rest-of-url` can be valid, even if the `urlscheme` entered doesn't exist.

See [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#validation)
 for details on how URLs are validated to ensure that they're formatted properly.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#additional_attributes)

------------------------------------------------------------------------------------------------------------------------------

In addition to the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
, and the attributes that operate on all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements regardless of their type, `url` inputs support the following attributes.

**Note:** The [`autocorrect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect)
 global attribute can be added to url inputs, but the stored state is always `off`.

### [list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#list)

The values of the list attribute is the [`id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id "id")
 of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element located in the same document. The [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 provides a list of predefined values to suggest to the user for this input. Any values in the list that are not compatible with the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 are not included in the suggested options. The values provided are suggestions, not requirements: users can select from this predefined list or provide a different value.

### [maxlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#maxlength)

The maximum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the `url` input. This must be an integer value of `0` or higher. If no `maxlength` is specified, or an invalid value is specified, the `url` input has no maximum length. This value must also be greater than or equal to the value of `minlength`.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text value of the field is greater than `maxlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [minlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#minlength)

The minimum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the `url` input. This must be a non-negative integer value smaller than or equal to the value specified by `maxlength`. If no `minlength` is specified, or an invalid value is specified, the `url` input has no minimum length.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is fewer than `minlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#pattern)

The `pattern` attribute, when specified, is a regular expression that the input's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 must match for the value to pass [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. It must be a valid JavaScript regular expression, as used by the [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 type, and as documented in our [guide on regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
; the `'u'` flag is specified when compiling the regular expression so that the pattern is treated as a sequence of Unicode code points, instead of as [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
. No forward slashes should be specified around the pattern text.

If the specified pattern is not specified or is invalid, no regular expression is applied and this attribute is ignored completely.

**Note:** Use the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#title)
 attribute to specify text that most browsers will display as a tooltip to explain what the requirements are to match the pattern. You should also include other explanatory text nearby.

See the section [Pattern validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#pattern_validation)
 for details and an example.

### [placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#placeholder)

The `placeholder` attribute is a string that provides a brief hint to the user as to what kind of information is expected in the field. It should be a word or short phrase that demonstrates the expected type of data, rather than an explanatory message. The text _must not_ include carriage returns or line feeds.

If the control's content has one directionality ([LTR](https://developer.mozilla.org/en-US/docs/Glossary/LTR)
 or [RTL](https://developer.mozilla.org/en-US/docs/Glossary/RTL)
) but needs to present the placeholder in the opposite directionality, you can use Unicode bidirectional algorithm formatting characters to override directionality within the placeholder; see [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls "External link (opens in new tab)")
 for more information.

**Note:** Avoid using the `placeholder` attribute if you can. It is not as semantically useful as other ways to explain your form, and can cause unexpected technical issues with your content. See [`<input>` labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
 for more information.

### [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#readonly)

The [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)
 Boolean attribute, if present, means this field cannot be edited by the user. Its `value` can, however, still be changed by JavaScript code directly setting the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 `value` property.

**Note:** Because a read-only field cannot have a value, [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)
 does not have any effect on inputs with the `readonly` attribute also specified.

### [size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#size)

The `size` attribute is a numeric value indicating how many characters wide the input field should be. The value must be a number greater than zero, and the default value is 20. Since character widths vary, this may or may not be exact and should not be relied upon to be so; the resulting input may be narrower or wider than the specified number of characters, depending on the characters and the font ([`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 settings in use).

This does _not_ set a limit on how many characters the user can enter into the field. It only specifies approximately how many can be seen at a time. To set an upper limit on the length of the input data, use the [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#maxlength)
 attribute.

### [spellcheck](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#spellcheck)

The [`spellcheck`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck)
 global attribute is used to indicate whether to enable spell-checking for an element. It can be used on any editable content, but here we consider specifics related to the use of `spellcheck` on [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements. The permitted values for `spellcheck` are:

[`false`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#false)

Disable spell-checking for this element.

[`true`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#true)

Enable spell-checking for this element.

["" (empty string) or no value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#empty_string_or_no_value)

Follow the element's default behavior for spell-checking. This may be based upon a parent's `spellcheck` setting or other factors.

An input field can have spell-checking enabled if it doesn't have the [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#readonly)
 attribute set and is not disabled.

The value returned by reading `spellcheck` may not reflect the actual state of spell-checking within a control if the [user agent's](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 preferences override the setting.

[Using URL inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#using_url_inputs)

--------------------------------------------------------------------------------------------------------------------

When you create a URL input with the proper `type` value, `url`, you get automatic validation that the entered text is at least in the correct form to potentially be a legitimate URL. This can help avoid cases in which the user mistypes their website's address, or provides an invalid one.

It's important, however, to note that this is not enough to ensure that the specified text is a URL which actually exists, corresponds to the user of the site, or is acceptable in any other way. It ensures that the value of the field is properly formatted to be a URL.

**Note:** A user can tinker with your HTML behind the scenes, so your site _must not_ use this validation for any security purposes. You _must_ verify the URL on the server-side of any transaction in which the provided text may have any security implications of any kind.

### [A basic URL input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#a_basic_url_input)

This element is implemented as a standard text input field with basic validation features. In its most basic form, a URL input can be implemented like this:

html

    <input id="myURL" name="myURL" type="url" />
    

Notice that it's considered valid when empty and when a single validly-formatted URL address is entered, but is otherwise not considered valid. By adding the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute, only properly-formed URLs are allowed; the input is no longer considered valid when empty.

There is nothing magical going on here. Submitting this form would cause the following data to be sent to the server: `myURL=http%3A%2F%2Fwww.example.com`. Note how characters are escaped as necessary.

### [Placeholders](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#placeholders)

Sometimes it's helpful to offer an in-context hint as to what form the input data should take. This can be especially important if the page design doesn't offer descriptive labels for each [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
. This is where **placeholders** come in. A placeholder is a value that demonstrates the form the `value` should take by presenting an example of a valid value, which is displayed inside the edit box when the element's `value` is "". Once data is entered into the box, the placeholder disappears; if the box is emptied, the placeholder reappears.

Here, we have a `url` input with the placeholder `http://www.example.com`. Note how the placeholder disappears and reappears as you manipulate the contents of the edit field.

html

    <input
      id="myURL"
      name="myURL"
      type="url"
      placeholder="http://www.example.com" />
    

### [Controlling the input size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#controlling_the_input_size)

You can control both the physical length of the input box and the minimum and maximum lengths allowed for the input text.

#### Physical input element size

The physical size of the input box can be controlled using the [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
 attribute. With it, you can specify the number of characters the input box can display at a time. In this example, for instance, the `url` edit box is 30 characters wide:

html

    <input id="myURL" name="myURL" type="url" size="30" />
    

#### Element value length

The `size` is separate from the length limitation on the entered URL itself. You can specify a minimum length, in characters, for the entered URL using the [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)
 attribute; similarly, use [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
 to set the maximum length of the entered URL. If `maxLength` exceeds `size`, the input box's contents will scroll as needed to show the current selection or insertion point as the content is manipulated.

The example below creates a 30-character wide URL address entry box, requiring that the contents be no shorter than 10 characters and no longer than 80 characters.

html

    <input
      id="myURL"
      name="myURL"
      type="url"
      size="30"
      minlength="10"
      maxlength="80" />
    

**Note:** These attributes also affect validation; a value shorter or longer than the specified minimum/maximum lengths will be classified as invalid; in addition most browsers will refuse to let the user enter a value longer than the specified maximum length.

### [Providing default options](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#providing_default_options)

#### Providing a single default using the value attribute

As always, you can provide a default value for a `url` input box by setting its [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute:

html

    <input id="myURL" name="myURL" type="url" value="http://www.example.com" />
    

#### Offering suggested values

Taking it a step further, you can provide a list of default options from which the user can select by specifying the [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)
 attribute. This doesn't limit the user to those options, but does allow them to select commonly-used URLs more quickly. This also offers hints to [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)
. The `list` attribute specifies the ID of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
, which in turn contains one [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 element per suggested value; each `option`'s `value` is the corresponding suggested value for the URL entry box.

html

    <input id="myURL" name="myURL" type="url" list="defaultURLs" />
    
    <datalist id="defaultURLs">
      <option value="https://developer.mozilla.org/"></option>
      <option value="http://www.google.com/"></option>
      <option value="http://www.microsoft.com/"></option>
      <option value="https://www.mozilla.org/"></option>
      <option value="http://w3.org/"></option>
    </datalist>
    

With the [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element and its [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
s in place, the browser will offer the specified values as potential values for the URL; this is typically presented as a popup or drop-down menu containing the suggestions. While the specific user experience may vary from one browser to another, typically clicking in the edit box presents a drop-down of the suggested URLs. Then, as the user types, the list is adjusted to show only matching values. Each typed character narrows down the list until the user makes a selection or types a custom value.

#### Using labels for suggested values

You can opt to include the [`label`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#label)
 attribute on one or all of your `<option>` elements to provide textual labels. Some browsers may display only the labels, while others may display both the label and the URL.

html

    <input id="myURL" name="myURL" type="url" list="defaultURLs" />
    
    <datalist id="defaultURLs">
      <option value="https://developer.mozilla.org/" label="MDN Web Docs"></option>
      <option value="http://www.google.com/" label="Google"></option>
      <option value="http://www.microsoft.com/" label="Microsoft"></option>
      <option value="https://www.mozilla.org/" label="Mozilla"></option>
      <option value="http://w3.org/" label="W3C"></option>
    </datalist>
    

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#validation)

--------------------------------------------------------------------------------------------------------

There are two levels of content validation available for `url` inputs. First, there's the standard level of validation offered to all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
s, which automatically ensures that the contents meet the requirements to be a valid URL. But there's also the option to add additional filtering to ensure that your own specialized needs are met, if you have any.

**Warning:** HTML form validation is _not_ a substitute for scripts that ensure that the entered data is in the proper format. It's far too easy for someone to make adjustments to the HTML that allow them to bypass the validation, or to remove it entirely. It's also possible for someone to bypass your HTML entirely and submit the data directly to your server. If your server-side code fails to validate the data it receives, disaster could strike when improperly-formatted data (or data which is too large, is of the wrong type, and so forth) is entered into your database.

### [Basic validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#basic_validation)

Browsers that support the `url` input type automatically provide validation to ensure that only text that matches the standard format for URLs is entered into the input box.

The syntax of a URL is fairly intricate. It's defined by WHATWG's [URL Living Standard](https://url.spec.whatwg.org/ "External link (opens in new tab)")
 and is described for newcomers in our article [What is a URL?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)

### [Making a URL required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#making_a_url_required)

As mentioned earlier, to make a URL entry required before the form can be submitted (you can't leave the field blank), you just need to include the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute on the input.

### [Pattern validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#pattern_validation)

If you need the entered URL to be restricted further than just "any string that looks like a URL," you can use the [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attribute to specify a [regular expression](https://developer.mozilla.org/en-US/docs/Glossary/Regular_expression)
 the value must match for the value to be valid.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#examples)

----------------------------------------------------------------------------------------------------

### [URL validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#url_validation)

In this example, we make sure that a URL is filled in using the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute and that the URL is something on `mozilla.org` using the [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attribute for illustration.

#### HTML

In the `url` input, we set `pattern` to `".*\.mozilla\.org.*"`. This regular expression validates a string that has any number of characters, followed by ".mozilla.org", followed by any number of characters. Because the browser runs both the standard URL filter _and_ our custom pattern against the specified text, we wind up with a validation that says "make sure this is a valid URL, and also contains `.mozilla.org`."

Note that a strict pattern like `https://developer\.mozilla\.org.*` would be more robust, but that would make the `type="url"` attribute redundant in this case.

The [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attribute also describes the `pattern` for users with assistive technologies.

html

    <form>
      <label for="myURL">
        Enter a url from this site:
        <input
          id="myURL"
          name="myURL"
          type="url"
          required
          pattern=".*\.mozilla\.org.*"
          title="URL should include mozilla.org" />
        <span class="validity"></span>
      </label>
      <button>Submit</button>
    </form>
    

    document.querySelectorAll("form").forEach((form) => {
      form.addEventListener("submit", (event) => {
        event.preventDefault();
      });
    });
    

#### CSS

The CSS gives visual clues to show the user if the content is [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 or [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 by adding an appropriate [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property and includes [alternative text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#alternative_text_string_counter_attr)
 for users with assistive technologies.

css

    input:focus:invalid {
      outline: 2px solid red;
    }
    
    input:focus:valid {
      outline: 2px solid green;
    }
    
    input + span {
      padding: 0 0.3rem;
    }
    
    input:invalid + span::after {
      content: "✖" / "Content is not valid";
      color: red;
    }
    
    input:valid + span::after {
      content: "✓" / "Content is valid";
      color: green;
    }
    

#### Result

Copy this page's url and paste it in the input field and you will see a green outline and green tick. Enter any other URL that doesn't contain **mozilla.org** or an invalid URL and you will see a red outline and red cross.

Check the [Pattern validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#pattern_validation)
 and [Using URL inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#using_url_inputs)
 sections for other examples.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#technical_summary)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#value)<br>** | A string representing a URL, or empty |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported Common Attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)<br>, [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)<br>, [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)<br>, [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)<br>, [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly)<br>, [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)<br> and [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size) |
| **IDL attributes** | `list`, `value`, `selectionEnd`, `selectionDirection` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | with no `list` attribute: `[textbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role) `  <br>with `list` attribute: `[combobox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role) ` |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# url-state-(type=url)](https://html.spec.whatwg.org/multipage/input.html#url-state-(type=url)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url#see_also)

----------------------------------------------------------------------------------------------------

*   [HTML forms guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<input type="tel">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel)
    
*   [`<input type="email">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/url/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/url (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Furl&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Furl%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Furl%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Furl%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")