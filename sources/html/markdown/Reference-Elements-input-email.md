*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#mdn-search)
    

`<input type="email">` HTML attribute value
===========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`email`** are used to let the user enter and edit an email address, or, if the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
 attribute is specified, a list of email addresses.

The input value is automatically validated to ensure that it's either empty or a properly-formatted email address (or list of addresses) before the form can be submitted. The [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 CSS pseudo-classes are automatically applied as appropriate to visually denote whether the current value of the field is a valid email address or not.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#try_it)

--------------------------------------------------------------------------------------------------

    <label for="email">Enter your example.com email:</label>
    
    <input type="email" id="email" pattern=".+@example\.com" size="30" required />
    

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
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#value)

------------------------------------------------------------------------------------------------

The [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute contains a string which is automatically validated as conforming to email syntax. More specifically, there are three possible value formats that will pass validation:

1.  An empty string ("") indicating that the user did not enter a value or that the value was removed.
2.  A single properly-formed email address. This doesn't necessarily mean the email address exists, but it is at least formatted correctly. This means `username@domain` or `username@domain.tld`. There's more to it than that, of course; see [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#validation)
     for a [regular expression](https://developer.mozilla.org/en-US/docs/Glossary/Regular_expression)
     that matches the email address validation algorithm.
3.  If and only if the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#multiple)
     attribute is specified, the value can be a list of properly-formed comma-separated email addresses. Any trailing and leading whitespace is removed from each address in the list.

See [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#validation)
 for details on how email addresses are validated to ensure that they're formatted properly.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#additional_attributes)

--------------------------------------------------------------------------------------------------------------------------------

In addition to the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
, and the attributes that operate on all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements regardless of their type, `email` inputs support the following attributes.

**Note:** The [`autocorrect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect)
 global attribute can be added to email inputs, but the stored state is always `off`.

### [list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#list)

The values of the list attribute is the [`id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id "id")
 of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element located in the same document. The [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 provides a list of predefined values to suggest to the user for this input. Any values in the list that are not compatible with the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 are not included in the suggested options. The values provided are suggestions, not requirements: users can select from this predefined list or provide a different value.

### [maxlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#maxlength)

The maximum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the `email` input. This must be an integer value of 0 or higher. If no `maxlength` is specified, or an invalid value is specified, the `email` input has no maximum length. This value must also be greater than or equal to the value of `minlength`.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text value of the field is greater than `maxlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [minlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#minlength)

The minimum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the `email` input. This must be a non-negative integer value smaller than or equal to the value specified by `maxlength`. If no `minlength` is specified, or an invalid value is specified, the `email` input has no minimum length.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is fewer than `minlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [multiple](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#multiple)

A Boolean attribute which, if present, indicates that the user can enter a list of multiple email addresses, separated by commas and, optionally, whitespace characters. See [Allowing multiple email addresses](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#allowing_multiple_email_addresses)
 for an example, or [HTML attribute: multiple](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
 for more details.

**Note:** Normally, if you specify the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute, the user must enter a valid email address for the field to be considered valid. However, if you add the `multiple` attribute, a list of zero email addresses (an empty string, or one which is entirely whitespace) is a valid value. In other words, the user does not have to enter even one email address when `multiple` is specified, regardless of the value of `required`.

### [pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#pattern)

The `pattern` attribute, when specified, is a regular expression that the input's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 must match for the value to pass [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. It must be a valid JavaScript regular expression, as used by the [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 type, and as documented in our [guide on regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
; the `'u'` flag is specified when compiling the regular expression so that the pattern is treated as a sequence of Unicode code points, instead of as [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
. No forward slashes should be specified around the pattern text.

If the specified pattern is not specified or is invalid, no regular expression is applied and this attribute is ignored completely.

**Note:** Use the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#title)
 attribute to specify text that most browsers will display as a tooltip to explain what the requirements are to match the pattern. You should also include other explanatory text nearby.

See the section [Pattern validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#pattern_validation)
 for details and an example.

### [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#placeholder)

The `placeholder` attribute is a string that provides a brief hint to the user as to what kind of information is expected in the field. It should be a word or short phrase that demonstrates the expected type of data, rather than an explanatory message. The text _must not_ include carriage returns or line feeds.

If the control's content has one directionality ([LTR](https://developer.mozilla.org/en-US/docs/Glossary/LTR)
 or [RTL](https://developer.mozilla.org/en-US/docs/Glossary/RTL)
) but needs to present the placeholder in the opposite directionality, you can use Unicode bidirectional algorithm formatting characters to override directionality within the placeholder; see [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls "External link (opens in new tab)")
 for more information.

**Note:** Avoid using the `placeholder` attribute if you can. It is not as semantically useful as other ways to explain your form, and can cause unexpected technical issues with your content. See [`<input>` labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
 for more information.

### [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#readonly)

A Boolean attribute which, if present, means this field cannot be edited by the user. Its `value` can, however, still be changed by JavaScript code directly setting the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 `value` property.

**Note:** Because a read-only field cannot have a value, `required` does not have any effect on inputs with the `readonly` attribute also specified.

### [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#size)

The `size` attribute is a numeric value indicating how many characters wide the input field should be. The value must be a number greater than zero, and the default value is 20. Since character widths vary, this may or may not be exact and should not be relied upon to be so; the resulting input may be narrower or wider than the specified number of characters, depending on the characters and the font ([`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 settings in use).

This does _not_ set a limit on how many characters the user can enter into the field. It only specifies approximately how many can be seen at a time. To set an upper limit on the length of the input data, use the [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#maxlength)
 attribute.

[Using email inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#using_email_inputs)

--------------------------------------------------------------------------------------------------------------------------

Email addresses are among the most frequently-inputted textual data forms on the web; they're used when logging into websites, when requesting information, to allow order confirmation, for webmail, and so forth. As such, the `email` input type can make your job as a web developer much easier since it can help simplify your work when building the user interface and logic for email addresses. When you create an email input with the proper `type` value, `email`, you get automatic validation that the entered text is at least in the correct form to potentially be a legitimate email address. This can help avoid cases in which the user mistypes their address, or provides an invalid address.

It's important, however, to note that this is not enough to ensure that the specified text is an email address which actually exists, corresponds to the user of the site, or is acceptable in any other way. It ensures that the value of the field is properly formatted to be an email address.

**Note:** It's also crucial to remember that a user can tinker with your HTML behind the scenes, so your site _must not_ use this validation for any security purposes. You _must_ verify the email address on the server side of any transaction in which the provided text may have any security implications of any kind.

### [A basic email input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#a_basic_email_input)

Currently, all browsers which implement this element implement it as a standard text input field with basic validation features. The specification does, however, allow browsers latitude on this. For example, the element could be integrated with the user's device's built-in address book to allow picking email addresses from that list. In its most basic form, an `email` input can be implemented like this:

html

    <input id="emailAddress" type="email" />
    

Notice that it's considered valid when empty and when a single validly-formatted email address is entered, but is otherwise not considered valid. By adding the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute, only validly-formed email addresses are allowed; the input is no longer considered valid when empty.

### [Allowing multiple email addresses](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#allowing_multiple_email_addresses)

By adding the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
 Boolean attribute, the input can be configured to accept multiple email addresses.

html

    <input id="emailAddress" type="email" multiple />
    

The input is now considered valid when a single email address is entered, or when any number of email addresses separated by commas and, optionally, some number of whitespace characters are present.

**Note:** When `multiple` is used, the value _is_ allowed to be empty.

Some examples of valid strings when `multiple` is specified:

*   `""`
*   `"me@example"`
*   `"me@example.org"`
*   `"me@example.org,you@example.org"`
*   `"me@example.org, you@example.org"`
*   `"me@example.org,you@example.org, us@example.org"`

Some examples of invalid strings:

*   `","`
*   `"me"`
*   `"me@example.org you@example.org"`

### [Placeholders](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#placeholders)

Sometimes it's helpful to offer an in-context hint as to what form the input data should take. This can be especially important if the page design doesn't offer descriptive labels for each [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
. This is where **placeholders** come in. A placeholder is a value that demonstrates the form the `value` should take by presenting an example of a valid value, which is displayed inside the edit box when the element's `value` is "". Once data is entered into the box, the placeholder disappears; if the box is emptied, the placeholder reappears.

Here, we have an `email` input with the placeholder `sophie@example.com`. Note how the placeholder disappears and reappears as you manipulate the contents of the edit field.

html

    <input type="email" placeholder="sophie@example.com" />
    

### [Controlling the input size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#controlling_the_input_size)

You can control not only the physical length of the input box, but also the minimum and maximum lengths allowed for the input text itself.

#### Physical input element size

The physical size of the input box can be controlled using the [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
 attribute. With it, you can specify the number of characters the input box can display at a time. In this example the `email` edit box is 15 characters wide:

html

    <input type="email" size="15" />
    

#### Element value length

The `size` is separate from the length limitation on the entered email address itself so that you can have fields fit in a small space while still allowing longer email address strings to be entered. You can specify a minimum length, in characters, for the entered email address using the [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)
 attribute; similarly, use [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
 to set the maximum length of the entered email address.

The example below creates a 32 character-wide email address entry box, requiring that the contents be no shorter than 3 characters and no longer than 64 characters.

html

    <input type="email" size="32" minlength="3" maxlength="64" />
    

### [Providing default options](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#providing_default_options)

#### Providing a single default using the value attribute

As always, you can provide a default value for an `email` input box by setting its [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute:

html

    <input type="email" value="default@example.com" />
    

#### Offering suggested values

Taking it a step further, you can provide a list of default options from which the user can select by specifying the [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)
 attribute. This doesn't limit the user to those options, but does allow them to select commonly-used email addresses more quickly. This also offers hints to [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)
. The `list` attribute specifies the ID of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
, which in turn contains one [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 element per suggested value; each `option`'s `value` is the corresponding suggested value for the email entry box.

html

    <input type="email" size="40" list="defaultEmails" />
    
    <datalist id="defaultEmails">
      <option value="jbond007@mi6.defence.gov.uk"></option>
      <option value="jbourne@unknown.net"></option>
      <option value="nfury@shield.org"></option>
      <option value="tony@starkindustries.com"></option>
      <option value="hulk@grrrrrrrr.arg"></option>
    </datalist>
    

With the [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element and its [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
s in place, the browser will offer the specified values as potential values for the email address; this is typically presented as a popup or drop-down menu containing the suggestions. While the specific user experience may vary from one browser to another, typically clicking in the edit box presents a drop-down of the suggested email addresses. Then, as the user types, the list is filtered to show only matching values. Each typed character narrows down the list until the user makes a selection or types a custom value.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#validation)

----------------------------------------------------------------------------------------------------------

There are two levels of content validation available for `email` inputs. First, there's the standard level of validation offered to all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
s, which automatically ensures that the contents meet the requirements to be a valid email address. But there's also the option to add additional filtering to ensure that your own specialized needs are met, if you have any.

**Warning:** HTML form validation is _not_ a substitute for scripts that ensure that the entered data is in the proper format. It's far too easy for someone to make adjustments to the HTML that allow them to bypass the validation, or to remove it completely. It's also possible for someone to bypass your HTML entirely and submit the data directly to your server. If your server-side code fails to validate the data it receives, disaster could strike when improperly-formatted data (or data which is too large, is of the wrong type, and so forth) is entered into your database.

### [Basic validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#basic_validation)

Browsers automatically provide validation to ensure that only text that matches the standard format for Internet email addresses is entered into the input box. Browsers use an algorithm equivalent to the following regular expression:

js

    /^[\w.!#$%&'*+/=?^`{|}~-]+@[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)*$/i;
    

To learn more about how form validation works and how to take advantage of the [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 CSS properties to style the input based on whether the current value is valid, see [Form data validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
.

**Note:** There are known specification issues related to international domain names and the validation of email addresses in HTML. See [W3C bug 15489](https://www.w3.org/Bugs/Public/show_bug.cgi?id=15489 "External link (opens in new tab)")
 and [whatwg/html#4562](https://github.com/whatwg/html/issues/4562 "External link (opens in new tab)")
 for details.

### [Pattern validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#pattern_validation)

If you need the entered email address to be restricted further than just "any string that looks like an email address," you can use the [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attribute to specify a [regular expression](https://developer.mozilla.org/en-US/docs/Glossary/Regular_expression)
 the value must match for it to be valid. If the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#multiple)
 attribute is specified, each individual item in the comma-delineated list of values must match the [regular expression](https://developer.mozilla.org/en-US/docs/Glossary/Regular_expression)
.

For example, let's say you're building a page for employees of Best Startup Ever, Inc. which will let them contact their IT department for help. In our simplified form, the user needs to enter their email address and a message describing the problem they need help with. We want to ensure that not only does the user provide a valid email address, but for security purposes, we require that the address be an internal corporate email address.

Since inputs of type `email` validate against both the standard email address validation _and_ the specified [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
, you can implement this easily. Let's see how:

    body {
      font: 16px sans-serif;
    }
    
    .emailBox {
      padding-bottom: 20px;
    }
    
    .messageBox {
      padding-bottom: 20px;
    }
    
    label {
      line-height: 22px;
    }
    
    label::after {
      content: ":";
    }
    

html

    <form>
      <div class="emailBox">
        <label for="emailAddress">Your email address</label><br />
        <input
          id="emailAddress"
          type="email"
          size="64"
          maxlength="64"
          required
          placeholder="username@beststartupever.com"
          pattern=".+@beststartupever\.com"
          title="Please provide only a Best Startup Ever corporate email address" />
      </div>
    
      <div class="messageBox">
        <label for="message">Request</label><br />
        <textarea
          id="message"
          cols="80"
          rows="8"
          required
          placeholder="My shoes are too tight, and I have forgotten how to dance."></textarea>
      </div>
      <input type="submit" value="Send Request" />
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

Our [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 contains one [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 of type `email` for the user's email address, a [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 to enter their message for IT into, and an `<input>` of type [`"submit"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
, which creates a button to submit the form. Each text entry box has a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 associated with it to let the user know what's expected of them.

Let's take a closer look at the email address entry box. Its [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
 and [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
 attributes are both set to 64 in order to show room for 64 characters worth of email address, and to limit the number of characters actually entered to a maximum of 64. The [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute is specified, making it mandatory that a valid email address be provided.

An appropriate [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
 is provided—`username@beststartupever.com`—to demonstrate what constitutes a valid entry. This string demonstrates both that an email address should be entered, and suggests that it should be a corporate beststartupever.com account. This is in addition to the fact that using type `email` will validate the text to ensure that it's formatted like an email address. If the text in the input box isn't an email address, you'll get an error message that looks something like this:

![Invalid email address in error state with a popout from the input reading 'please enter an email address'.](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email/enter-valid-email-address.png)

If we left things at that, we would at least be validating on legitimate email addresses. But we want to go one step farther: we want to make sure that the email address is in fact in the form `[username]@beststartupever.com`. This is where we'll use [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
. We set `pattern` to `.+@beststartupever.com`. This regular expression requests a string that consists of at least one character of any kind, then an "@" followed by the domain name "beststartupever.com".

Note that this is not even close to an adequate filter for valid email addresses; it would allow things such as " @beststartupever.com" (note the leading space) or "@@beststartupever.com", neither of which is valid. However, the browser runs both the standard email address filter _and_ our custom pattern against the specified text. As a result, we wind up with a validation which says "make sure this resembles a valid email address, and if it is, make sure it's also a beststartupever.com address."

It's advisable to use the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attribute along with `pattern`. If you do, the `title` _must_ describe the pattern. That is, it should explain what format the data should take on, rather than any other information. That's because the `title` may be displayed or spoken as part of a validation error message. For example, the browser might present the message "The entered text doesn't match the required pattern." followed by your specified `title`. If your `title` is something like "Email address", the result would be the message "The entered text doesn't match the required pattern. Email address", which isn't very good.

That's why, instead, we specify the string "Please provide only a Best Startup Ever corporate email address" By doing that, the resulting full error message might be something like "The entered text doesn't match the required pattern. Please provide only a Best Startup Ever corporate email address."

![A valid email address, but the input is in error state with a popout from the input reading 'The entered text doesn't match the required pattern. Please provide only a Best Startup Ever corporate email address.'](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email/email-pattern-match-bad.png)

**Note:** If you run into trouble while writing your validation regular expressions and they're not working properly, check your browser's console; there may be helpful error messages there to aid you in solving the problem.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#examples)

------------------------------------------------------------------------------------------------------

Here we have an email input with the ID `emailAddress` which is allowed to be up to a maximum of 256 characters long. The input box itself is physically 64 characters wide, and displays the text `user@example.gov` as a placeholder anytime the field is empty. In addition, by using the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
 attribute, the box is configured to allow the user to enter zero or more email addresses, separated by commas, as described in [Allowing multiple email addresses](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#allowing_multiple_email_addresses)
. As a final touch, the [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)
 attribute contains the ID of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 whose [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
s specify a set of suggested values the user can choose from.

As an added touch, the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element is used to establish a label for the email entry box, with its [`for`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#for)
 attribute referencing the `emailAddress` ID of the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element. By associating the two elements in this way, clicking on the label will focus the input element.

html

    <label for="emailAddress">Email</label><br />
    <input
      id="emailAddress"
      type="email"
      placeholder="user@example.gov"
      list="defaultEmails"
      size="64"
      maxlength="256"
      multiple />
    
    <datalist id="defaultEmails">
      <option value="jbond007@mi6.defence.gov.uk"></option>
      <option value="jbourne@unknown.net"></option>
      <option value="nfury@shield.org"></option>
      <option value="tony@starkindustries.com"></option>
      <option value="hulk@grrrrrrrr.arg"></option>
    </datalist>
    

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#technical_summary)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#value)<br>** | A string representing an email address, or empty |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported Common Attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)<br>, [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)<br>, [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#multiple)<br>, [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name)<br>, [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)<br>, [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)<br>, [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly)<br>, [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)<br>, [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)<br>, and [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type) |
| **IDL attributes** | `list` and `value` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | with no `list` attribute: `[textbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role) `  <br>with `list` attribute: `[combobox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role) ` |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# email-state-(type=email)](https://html.spec.whatwg.org/multipage/input.html#email-state-(type=email)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email#see_also)

------------------------------------------------------------------------------------------------------

*   [HTML forms guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<input type="tel">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel)
    
*   [`<input type="url">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
    
*   Attributes:
    *   [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)
        
    *   [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength)
        
    *   [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength)
        
    *   [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
        
    *   [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern)
        
    *   [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
        
    *   [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)
        
    *   [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/size)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/email/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/email (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Femail&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Femail%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Femail%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Femail%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")