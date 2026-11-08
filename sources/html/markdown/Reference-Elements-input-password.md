*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#mdn-search)
    

`<input type="password">` HTML attribute value
==============================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

`<input>` elements of type **`password`** provide a way for the user to securely enter a password.

The element is presented as a one-line plain text editor control in which the text is obscured so that it cannot be read, usually by replacing each character with a symbol such as the asterisk ("\*") or a dot ("•"). This character will vary depending on the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 and operating system.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#try_it)

-----------------------------------------------------------------------------------------------------

    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" />
    </div>
    
    <div>
      <label for="pass">Password (8 characters minimum):</label>
      <input type="password" id="pass" name="password" minlength="8" required />
    </div>
    
    <input type="submit" value="Sign in" />
    

    label {
      display: block;
    }
    
    input[type="submit"],
    label {
      margin-top: 1rem;
    }
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#value)

---------------------------------------------------------------------------------------------------

The [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute contains a string whose value is the current contents of the text editing control being used to enter the password. If the user hasn't entered anything yet, this value is an empty string (`""`). If the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 property is specified, then the password edit box must contain a value other than an empty string to be valid.

If the [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attribute is specified, the content of a `password` control is only considered valid if the value passes validation; see [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#validation)
 for more information.

**Note:** The line feed (U+000A) and carriage return (U+000D) characters are not permitted in a `password` value. When setting the value of a password control, line feed and carriage return characters are stripped out of the value.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#additional_attributes)

-----------------------------------------------------------------------------------------------------------------------------------

In addition to the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
, and the attributes that operate on all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements regardless of their type, password field inputs support the following attributes.

**Note:** The [`autocorrect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect)
 global attribute can be added to password inputs, but the stored state is always `off`.

### [maxlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#maxlength)

The maximum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the password field. This must be an integer value of 0 or higher. If no `maxlength` is specified, or an invalid value is specified, the password field has no maximum length. This value must also be greater than or equal to the value of `minlength`.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is greater than `maxlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [minlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#minlength)

The minimum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the password entry field. This must be a non-negative integer value smaller than or equal to the value specified by `maxlength`. If no `minlength` is specified, or an invalid value is specified, the password input has no minimum length.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is fewer than `minlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#pattern)

The `pattern` attribute, when specified, is a regular expression that the input's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 must match for the value to pass [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. It must be a valid JavaScript regular expression, as used by the [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 type, and as documented in our [guide on regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
; the `'u'` flag is specified when compiling the regular expression, so that the pattern is treated as a sequence of Unicode code points, instead of as [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
. No forward slashes should be specified around the pattern text.

If the specified pattern is not specified or is invalid, no regular expression is applied and this attribute is ignored completely.

**Note:** Use the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#title)
 attribute to specify text that most browsers will display as a tooltip to explain what the requirements are to match the pattern. You should also include other explanatory text nearby.

Use of a pattern is strongly recommended for password inputs, in order to help ensure that valid passwords using a wide assortment of character classes are selected and used by your users. With a pattern, you can mandate case rules, require the use of some number of digits and/or punctuation characters, and so forth. See the section [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#validation)
 for details and an example.

### [placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#placeholder)

The `placeholder` attribute is a string that provides a brief hint to the user as to what kind of information is expected in the field. It should be a word or short phrase that demonstrates the expected type of data, rather than an explanatory message. The text _must not_ include carriage returns or line feeds.

If the control's content has one directionality ([LTR](https://developer.mozilla.org/en-US/docs/Glossary/LTR)
 or [RTL](https://developer.mozilla.org/en-US/docs/Glossary/RTL)
) but needs to present the placeholder in the opposite directionality, you can use Unicode bidirectional algorithm formatting characters to override directionality within the placeholder; see [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls "External link (opens in new tab)")
 for more information.

**Note:** Avoid using the `placeholder` attribute if you can. It is not as semantically useful as other ways to explain your form, and can cause unexpected technical issues with your content. See [`<input>` labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
 for more information.

### [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#readonly)

A Boolean attribute which, if present, means this field cannot be edited by the user. Its `value` can, however, still be changed from JavaScript code that directly sets the value of the [`HTMLInputElement.value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement "HTMLInputElement.value")
 property.

**Note:** Because a read-only field cannot have a value, `required` does not have any effect on inputs with the `readonly` attribute also specified.

### [size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#size)

The `size` attribute is a numeric value indicating how many characters wide the input field should be. The value must be a number greater than zero, and the default value is 20. Since character widths vary, this may or may not be exact and should not be relied upon to be so; the resulting input may be narrower or wider than the specified number of characters, depending on the characters and the font ([`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 settings in use).

This does _not_ set a limit on how many characters the user can enter into the field. It only specifies approximately how many can be seen at a time. To set an upper limit on the length of the input data, use the [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#maxlength)
 attribute.

[Using password inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#using_password_inputs)

-----------------------------------------------------------------------------------------------------------------------------------

Password input boxes generally work just like other textual input boxes; the main difference is the obscuring of the content to prevent people near the user from reading the password.

The precise behavior of the entry process may vary from browser to browser. Some browsers display the typed character for a moment before obscuring it, while others allow the user to toggle the display of plain-text on and off. Both approaches help a user check that they entered the intended password, which can be particularly difficult on mobile devices.

**Note:** Any forms involving sensitive information like passwords (such as login forms) should be served over HTTPS. Many browsers now implement mechanisms to warn against insecure login forms.

### [A basic password input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#a_basic_password_input)

Here we see the most basic password input, with a label established using the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element.

html

    <label for="userPassword">Password: </label>
    <input id="userPassword" type="password" />
    

### [Allowing autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#allowing_autocomplete)

To allow the user's password manager to automatically enter the password, specify the [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)
 attribute. For passwords, this should typically be one of the following:

[`on`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#on)

Allow the browser or a password manager to automatically fill out the password field. This isn't as informative as using either `current-password` or `new-password`.

[`off`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#off)

Don't allow the browser or password manager to automatically fill out the password field. Note that some software ignores this value, since it's typically harmful to users' ability to maintain safe password practices.

[`current-password`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#current-password)

Allow the browser or password manager to enter the current password for the site. This provides more information than `on` does, since it lets the browser or password manager automatically enter currently-known password for the site in the field, but not to suggest a new one.

[`new-password`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#new-password)

Allow the browser or password manager to automatically enter a new password for the site; this is used on "change your password" and "new user" forms, on the field asking the user for a new password. The new password may be generated in a variety of ways, depending on the password manager in use. It may fill in a new suggested password, or it might show the user an interface for creating one.

html

    <label for="userPassword">Password:</label>
    <input id="userPassword" type="password" autocomplete="current-password" />
    

### [Making the password mandatory](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#making_the_password_mandatory)

To tell the user's browser that the password field must have a valid value before the form can be submitted, specify the Boolean [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute.

html

    <label for="userPassword">Password: </label>
    <input id="userPassword" type="password" required />
    <input type="submit" value="Submit" />
    

### [Specifying an input mode](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#specifying_an_input_mode)

If your recommended (or required) password syntax rules would benefit from an alternate text entry interface than the standard keyboard, you can use the [`inputmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#inputmode)
 attribute to request a specific one. The most obvious use case for this is if the password is required to be numeric (such as a PIN). Mobile devices with virtual keyboards, for example, may opt to switch to a numeric keypad layout instead of a full keyboard, to make entering the password easier. If the PIN is for one-time use, set the [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)
 attribute to either `off` or `one-time-code` to suggest that it's not saved.

html

    <label for="pin">PIN: </label>
    <input id="pin" type="password" inputmode="numeric" />
    

### [Setting length requirements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#setting_length_requirements)

As usual, you can use the [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)
 and [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
 attributes to establish minimum and maximum acceptable lengths for the password. This example expands on the previous one by specifying that the user's PIN must be at least four and no more than eight digits. The [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
 attribute is used to ensure that the password entry control is eight characters wide.

html

    <label for="pin">PIN:</label>
    <input
      id="pin"
      type="password"
      inputmode="numeric"
      minlength="4"
      maxlength="8"
      size="8" />
    

### [Selecting text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#selecting_text)

As with other textual entry controls, you can use the [`select()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/select "select()")
 method to select all the text in the password field.

#### HTML

html

    <label for="userPassword">Password: </label>
    <input id="userPassword" type="password" size="12" />
    <button id="selectAll">Select All</button>
    

#### JavaScript

js

    document.getElementById("selectAll").onclick = () => {
      document.getElementById("userPassword").select();
    };
    

#### Result

You can also use [`selectionStart`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/selectionStart "selectionStart")
 and [`selectionEnd`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/selectionEnd "selectionEnd")
 to get (or set) what range of characters in the control are currently selected, and [`selectionDirection`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/selectionDirection "selectionDirection")
 to know which direction selection occurred in (or will be extended in, depending on your platform; see its documentation for an explanation). However, given that the text is obscured, the usefulness of these is somewhat limited.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#validation)

-------------------------------------------------------------------------------------------------------------

If your application has character set restrictions or any other requirement for the actual content of the entered password, you can use the [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attribute to establish a regular expression to be used to automatically ensure that your passwords meet those requirements.

In this example, only values consisting of at least four and no more than eight hexadecimal digits are valid.

html

    <label for="hexId">Hex ID: </label>
    <input
      id="hexId"
      type="password"
      pattern="[0-9a-fA-F]{4,8}"
      title="Enter an ID consisting of 4-8 hexadecimal digits"
      autocomplete="new-password" />
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#examples)

---------------------------------------------------------------------------------------------------------

### [Requesting a Social Security number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#requesting_a_social_security_number)

This example only accepts input which matches the format for a [valid United States Social Security Number](https://en.wikipedia.org/wiki/Social_Security_number#Structure "External link (opens in new tab)")
. These numbers, used for tax and identification purposes in the US, are in the form "123-45-6789". Assorted rules for what values are permitted in each group exist as well.

#### HTML

html

    <label for="ssn">SSN:</label>
    <input
      type="password"
      id="ssn"
      inputmode="numeric"
      minlength="9"
      maxlength="12"
      pattern="(?!000)([0-6]\d{2}|7([0-6]\d|7[012]))([ -])?(?!00)\d\d\3(?!0000)\d{4}"
      required
      autocomplete="off" />
    <br />
    <label for="ssn">Value:</label>
    <span id="current"></span>
    

This uses a [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 which limits the entered value to strings representing legal Social Security numbers. Obviously, this regexp doesn't guarantee a valid SSN (since we don't have access to the Social Security Administration's database), but it does ensure the number could be one; it generally avoids values that cannot be valid. In addition, it allows the three groups of digits to be separated by a space, a dash ("-"), or nothing.

The [`inputmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#inputmode)
 is set to `numeric` to encourage devices with virtual keyboards to switch to a numeric keypad layout for easier entry. The [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)
 and [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
 attributes are set to 9 and 12, respectively, to require that the value be at least nine and no more than 12 characters (the former without separating characters between the groups of digits and the latter with them). The [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute is used to indicate that this control must have a value. Finally, [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)
 is set to `off` to avoid password managers and session restore features trying to set its value, since this isn't a password at all.

#### JavaScript

The JavaScript displays the entered SSN onscreen so you can see it. This defeats the purpose of a password field, but it helps experiment with the `pattern`.

js

    const ssn = document.getElementById("ssn");
    const current = document.getElementById("current");
    
    ssn.oninput = (event) => {
      current.textContent = ssn.value;
    };
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#technical_summary)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#value)<br>** | A string representing a password, or empty |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported Common Attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`inputmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#inputmode)<br>, [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)<br>, [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)<br>, [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)<br>, [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)<br>, [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly)<br>, [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)<br>, and [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size) |
| **IDL attributes** | `selectionStart`, `selectionEnd`, `selectionDirection`, and `value` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [no corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# password-state-(type=password)](https://html.spec.whatwg.org/multipage/input.html#password-state-(type=password)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/password/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/password (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fpassword&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fpassword%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fpassword%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fpassword%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcb7d4dde9f0a43664c64587d9d70b8835286eb7%0A*+Document+last+modified%3A+2026-10-01T19%3A41%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")