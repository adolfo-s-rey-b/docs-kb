*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#mdn-search)
    

`<input type="reset">` HTML attribute value
===========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`reset`** are rendered as buttons, with a default [`click`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event "click")
 event handler that resets all inputs in the form to their initial values.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#try_it)

--------------------------------------------------------------------------------------------------

    <form>
      <div class="controls">
        <label for="comments">Comments:</label>
        <textarea id="comments" name="comments"></textarea>
    
        <input type="reset" value="Reset" />
      </div>
    </form>
    

    .controls {
      padding-top: 1rem;
      display: grid;
      grid-template-rows: repeat(2, auto);
      grid-template-columns: 1fr 2fr;
      gap: 0.7rem;
    }
    
    label {
      font-size: 0.8rem;
      justify-self: end;
    }
    
    input[type="reset"] {
      width: 5rem;
      justify-self: end;
    }
    
    input[type="reset"] {
      grid-column: 2;
      grid-row: 2;
    }
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#value)

------------------------------------------------------------------------------------------------

An `<input type="reset">` element's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute contains a string that is used as the button's label providing the button with an [accessible description](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_description)
. Buttons such as `reset` don't have a value otherwise.

### [Setting the value attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#setting_the_value_attribute)

html

    <input type="reset" value="Reset the form" />
    

### [Omitting the value attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#omitting_the_value_attribute)

If you don't specify a `value`, you get a button with the default label (typically "Reset," but this will vary depending on the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
):

html

    <input type="reset" />
    

[Using reset buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#using_reset_buttons)

----------------------------------------------------------------------------------------------------------------------------

`<input type="reset">` buttons are used to reset forms. If you want to create a custom button and then customize the behavior using JavaScript, you need to use [`<input type="button">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button)
, or better still, a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element.

You should usually avoid including reset buttons in your forms. They're rarely useful, and are instead more likely to frustrate users who click them by mistake (often while trying to click the [submit button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
).

### [A basic reset button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#a_basic_reset_button)

We'll begin by creating a basic reset button:

html

    <form>
      <div>
        <label for="example">Type in some sample text</label>
        <textarea id="example"></textarea>
      </div>
      <div>
        <input type="reset" value="Reset the form" />
      </div>
    </form>
    

This renders like so:

Try entering some text into the text field, and then pressing the reset button.

### [Adding a reset keyboard shortcut](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#adding_a_reset_keyboard_shortcut)

To add a keyboard shortcut to a reset button — just as you would with any [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 for which it makes sense — you use the [`accesskey`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/accesskey)
 global attribute.

In this example, r is specified as the access key (you'll need to press r plus the particular modifier keys for your browser/OS combination; see [`accesskey`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/accesskey)
 for a useful list of those).

html

    <form>
      <div>
        <label for="example">Type in some sample text</label>
        <textarea id="example"></textarea>
      </div>
      <div>
        <input type="reset" value="Reset the form" accesskey="r" />
      </div>
    </form>
    

The problem with the above example is that there's no way for the user to know what the access key is! This is especially true since the modifiers are typically non-standard to avoid conflicts. When building a site, be sure to provide this information in a way that doesn't interfere with the site design (for example by providing an easily accessible link that points to information on what the site access keys are). Adding a tooltip to the button (using the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attribute) can also help, although it's not a complete solution for accessibility purposes.

### [Disabling and enabling a reset button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#disabling_and_enabling_a_reset_button)

To disable a reset button, specify the [`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#disabled)
 attribute on it, like so:

html

    <input type="reset" value="Disabled" disabled />
    

You can enable and disable buttons at run time by setting `disabled` to `true` or `false`; in JavaScript this looks like `btn.disabled = true` or `btn.disabled = false`.

**Note:** See the [`<input type="button">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button#disabling_and_enabling_a_button)
 page for more ideas about enabling and disabling buttons.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#validation)

----------------------------------------------------------------------------------------------------------

Buttons don't participate in constraint validation; they have no real value to be constrained.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#examples)

------------------------------------------------------------------------------------------------------

We've included basic examples above. There isn't really anything more to say about reset buttons.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#technical_summary)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#value)<br>** | A string used as the button's label |
| **Events** | [`click`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event "click") |
| **Supported common attributes** | [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)<br> and [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value) |
| **IDL attributes** | `value` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [`button`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# reset-button-state-(type=reset)](https://html.spec.whatwg.org/multipage/input.html#reset-button-state-(type=reset)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset#see_also)

------------------------------------------------------------------------------------------------------

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

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/reset/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/reset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Freset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Freset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Freset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Freset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")