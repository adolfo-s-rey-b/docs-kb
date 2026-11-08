*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#mdn-search)
    

`<input type="submit">` HTML attribute value
============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`submit`** are rendered as buttons. When the [`click`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event "click")
 event occurs (typically because the user clicked the button), the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 attempts to submit the form to the server.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#value)

-------------------------------------------------------------------------------------------------

An `<input type="submit">` element's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute contains a string which is displayed as the button's label. Buttons do not have a true value otherwise. The `value` provides the [accessible description](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_description)
 for the button.

### [Setting the value attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#setting_the_value_attribute)

html

    <input type="submit" value="Send Request" />
    

### [Omitting the value attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#omitting_the_value_attribute)

If you don't specify a `value`, the button will have a default label, chosen by the user agent. This label is likely to be something along the lines of "Submit" or "Submit Query." Here's an example of a submit button with a default label in your browser:

html

    <input type="submit" />
    

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#additional_attributes)

---------------------------------------------------------------------------------------------------------------------------------

In addition to the attributes shared by all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, `submit` button inputs support the following attributes.

### [formaction](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#formaction)

A string indicating the URL to which to submit the data. This takes precedence over the [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action)
 attribute on the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element that owns the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
.

This attribute is also available on [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

### [formenctype](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#formenctype)

A string that identifies the encoding method to use when submitting the form data to the server. There are three permitted values:

[`application/x-www-form-urlencoded`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#applicationx-www-form-urlencoded)

This, the default value, sends the form data as a string after [percent-encoding](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)
 the text using an algorithm such as [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
.

[`multipart/form-data`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#multipartform-data)

Uses the [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
 API to manage the data, allowing for files to be submitted to the server. You _must_ use this encoding type if your form includes any [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 `file` ([`<input type="file">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
).

[`text/plain`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#textplain)

Plain text; mostly useful only for debugging, so you can easily see the data that's to be submitted.

If specified, the value of the `formenctype` attribute overrides the owning form's [`enctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#enctype)
 attribute.

This attribute is also available on [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

### [formmethod](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#formmethod)

A string indicating the HTTP method to use when submitting the form's data; this value overrides any [`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#method)
 attribute given on the owning form. Permitted values are:

[`get`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#get)

A URL is constructed by starting with the URL given by the `formaction` or [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action)
 attribute, appending a question mark ("?") character, then appending the form's data, encoded as described by `formenctype` or the form's [`enctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#enctype)
 attribute. This URL is then sent to the server using an HTTP [`get`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET)
 request. This method works well for forms that contain only [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 characters and have no side effects. This is the default value.

[`post`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#post)

The form's data is included in the body of the request that is sent to the URL given by the `formaction` or [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action)
 attribute using an HTTP [`post`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST)
 method. This method supports complex data and file attachments.

[`dialog`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#dialog)

This method is used to indicate that the button closes the dialog with which the input is associated, and does not transmit the form data at all.

This attribute is also available on [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

### [formnovalidate](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#formnovalidate)

A Boolean attribute which, if present, specifies that the form should not be validated before submission to the server. This overrides the value of the [`novalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#novalidate)
 attribute on the element's owning form.

This attribute is also available on [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

### [formtarget](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#formtarget)

A string which specifies a name or keyword that indicates where to display the response received after submitting the form. The string must be the name of a **browsing context** (that is, a tab, window, or [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
). A value specified here overrides any target given by the [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#target)
 attribute on the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 that owns this input.

In addition to the actual names of tabs, windows, or inline frames, there are a few special keywords that can be used:

[`_self`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#_self)

Loads the response into the same browsing context as the one that contains the form. This will replace the current document with the received data. This is the default value used if none is specified.

[`_blank`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#_blank)

Loads the response into a new, unnamed, browsing context. This is typically a new tab in the same window as the current document, but may differ depending on the configuration of the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
.

[`_parent`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#_parent)

Loads the response into the parent browsing context of the current one. If there is no parent context, this behaves the same as `_self`.

[`_top`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#_top)

Loads the response into the top-level browsing context; this is the browsing context that is the topmost ancestor of the current context. If the current context is the topmost context, this behaves the same as `_self`.

This attribute is also available on [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

[Using submit buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#using_submit_buttons)

-------------------------------------------------------------------------------------------------------------------------------

`<input type="submit">` buttons are used to submit forms. If you want to create a custom button and then customize the behavior using JavaScript, you need to use [`<input type="button">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button)
, or better still, a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element.

If you choose to use `<button>` elements to create the buttons in your form, keep this in mind: If the `<button>` is inside a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, that button will be treated as the "submit" button. So you should be in the habit of expressly specifying which button is the submit button.

### [A basic submit button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#a_basic_submit_button)

We'll begin by creating a form with a basic submit button:

html

    <form>
      <div>
        <label for="example">Let's submit some text</label>
        <input id="example" type="text" name="text" />
      </div>
      <div>
        <input type="submit" value="Send" />
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

This renders like so:

Try entering some text into the text field, and then submitting the form.

Upon submitting, the data name/value pair gets sent to the server. In this instance, the string will be `text=user-text`, where "user-text" is the text entered by the user, encoded to preserve special characters. Where and how the data is submitted depends on the configuration of the `<form>`; see [Sending form data](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Sending_and_retrieving_form_data)
 for more details.

### [Adding a keyboard shortcut to a submit button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#adding_a_keyboard_shortcut_to_a_submit_button)

Keyboard shortcuts, also known as access keys and keyboard equivalents, let the user trigger a button using a key or combination of keys on the keyboard. To add a keyboard shortcut to a submit button — just as you would with any [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 for which it makes sense — you use the [`accesskey`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/accesskey)
 global attribute.

In this example, s is specified as the access key (you'll need to press s plus the particular modifier keys for your browser/OS combination). In order to avoid conflicts with the user agent's own keyboard shortcuts, different modifier keys are used for access keys than for other shortcuts on the host computer. See [`accesskey`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/accesskey)
 for further details.

Here's the previous example with the s access key added:

html

    <form>
      <div>
        <label for="example">Let's submit some text</label>
        <input id="example" type="text" name="text" />
      </div>
      <div>
        <input type="submit" value="Send" accesskey="s" />
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

For example, in Firefox for Mac, pressing Control\-Option\-S triggers the Send button, while Chrome on Windows uses Alt+S.

The problem with the above example is that the user will not know what the access key is! This is especially true since the modifiers are typically non-standard to avoid conflicts. When building a site, be sure to provide this information in a way that doesn't interfere with the site design (for example by providing an easily accessible link that points to information on what the site access keys are). Adding a tooltip to the button (using the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attribute) can also help, although it's not a complete solution for accessibility purposes.

### [Disabling and enabling a submit button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#disabling_and_enabling_a_submit_button)

To disable a submit button, specify the [`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)
 attribute on it, like so:

html

    <input type="submit" value="Send" disabled />
    

You can enable and disable buttons at run time by setting `disabled` to `true` or `false`; in JavaScript this looks like `btn.disabled = true` or `btn.disabled = false`.

**Note:** See the [`<input type="button">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button#disabling_and_enabling_a_button)
 page for more ideas about enabling and disabling buttons.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#validation)

-----------------------------------------------------------------------------------------------------------

Submit buttons don't participate in constraint validation; they have no real value to be constrained.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#examples)

-------------------------------------------------------------------------------------------------------

We've included basic examples above. There isn't really anything more to say about submit buttons. There's a reason this kind of control is sometimes called a "simple button."

[Technical Summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#technical_summary)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#value)<br>** | A string used as the button's label |
| **Events** | [`click`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event "click") |
| **Supported common attributes** | [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)<br> and [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value) |
| **IDL attributes** | `value` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [`button`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# submit-button-state-(type=submit)](https://html.spec.whatwg.org/multipage/input.html#submit-button-state-(type=submit)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit#see_also)

-------------------------------------------------------------------------------------------------------

*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     and the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
     interface which implements it.
*   [Forms and buttons](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Basic_native_form_controls#actual_buttons)
    
*   [HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   The [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
     element

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/submit/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/submit (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fsubmit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fsubmit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fsubmit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fsubmit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")