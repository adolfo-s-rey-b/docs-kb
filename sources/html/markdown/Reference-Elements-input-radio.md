*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#mdn-search)
    

`<input type="radio">` HTML attribute value
===========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`radio`** are generally used in **radio groups**—collections of radio buttons describing a set of related options.

Only one radio button in a given group can be selected at the same time. Radio buttons are typically rendered as small circles, which are filled or highlighted when selected.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#try_it)

--------------------------------------------------------------------------------------------------

    <fieldset>
      <legend>Select a maintenance drone:</legend>
    
      <div>
        <input type="radio" id="huey" name="drone" value="huey" checked />
        <label for="huey">Huey</label>
      </div>
    
      <div>
        <input type="radio" id="dewey" name="drone" value="dewey" />
        <label for="dewey">Dewey</label>
      </div>
    
      <div>
        <input type="radio" id="louie" name="drone" value="louie" />
        <label for="louie">Louie</label>
      </div>
    </fieldset>
    

    p,
    label {
      font:
        1rem "Fira Sans",
        sans-serif;
    }
    
    input {
      margin: 0.4rem;
    }
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#value)

------------------------------------------------------------------------------------------------

The `value` attribute is a string containing the radio button's value. The value is never shown to the user by their [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
. Instead, it's used to identify which radio button in a group is selected.

### [Defining a radio group](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#defining_a_radio_group)

A radio group is defined by giving each of radio buttons in the group the same [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name)
. Once a radio group is established, selecting any radio button in that group automatically deselects any currently-selected radio button in the same group.

You can have as many radio groups on a page as you like, as long as each has its own unique `name`.

For example, if your form needs to ask the user for their preferred contact method, you might create three radio buttons, each with the `name` property set to `contact` but one with the value `email`, one with the value `phone`, and one with the value `mail`. The user never sees the `value` or the `name` (unless you expressly add code to display it).

The resulting HTML looks like this:

html

    <fieldset>
      <legend>Please select your preferred contact method:</legend>
      <div>
        <input type="radio" id="contactChoice1" name="contact" value="email" />
        <label for="contactChoice1">Email</label>
    
        <input type="radio" id="contactChoice2" name="contact" value="phone" />
        <label for="contactChoice2">Phone</label>
    
        <input type="radio" id="contactChoice3" name="contact" value="mail" />
        <label for="contactChoice3">Mail</label>
      </div>
    </fieldset>
    

Here you see the three radio buttons, each with the `name` set to `contact` and each with a unique `value` that uniquely identifies that individual radio button within the group. They each also have a unique [`id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id "id")
, which is used by the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element's [`for`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#for)
 attribute to associate the labels with the radio buttons.

You can try out this example here:

### [Data representation of a radio group](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#data_representation_of_a_radio_group)

When a form containing the above controls is submitted with a radio button selected, the form's data includes an entry in the form `contact=value`. For example, if the user clicks on the "Phone" radio button then submits the form, `contact=phone` will be included in the the form's submitted data.

If you omit the `value` attribute in the HTML, the submitted form data assigns the value `on` to the group. In this scenario, if the user clicked on the "Phone" option and submitted the form, the resulting form data would be `contact=on`, which isn't helpful. So don't forget to set your `value` attributes!

**Note:** If no radio button is selected when the form is submitted, the radio group is not included in the submitted form data at all, since there is no value to report.

It's fairly uncommon to actually want to allow the form to be submitted without any of the radio buttons in a group selected, so it is usually wise to have one default to the `checked` state. See [Selecting a radio button by default](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#selecting_a_radio_button_by_default)
 below.

Let's add a bit of code to our example so we can examine the data generated by these controls. The HTML is revised to wrap the controls in a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, add a submit button, and add a [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
 block to output the form data into:

html

    <form>
      <fieldset>
        <legend>Please select your preferred contact method:</legend>
        <div>
          <input type="radio" id="contactChoice1" name="contact" value="email" />
          <label for="contactChoice1">Email</label>
          <input type="radio" id="contactChoice2" name="contact" value="phone" />
          <label for="contactChoice2">Phone</label>
          <input type="radio" id="contactChoice3" name="contact" value="mail" />
          <label for="contactChoice3">Mail</label>
        </div>
        <div>
          <button type="submit">Submit</button>
        </div>
      </fieldset>
    </form>
    <pre id="log"></pre>
    

Then we add some [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
 to set up an event listener on the [`submit`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit_event "submit")
 event, which is sent when the user clicks the "Submit" button:

js

    const form = document.querySelector("form");
    const log = document.querySelector("#log");
    
    form.addEventListener("submit", (event) => {
      const data = new FormData(form);
      let output = "";
      for (const entry of data) {
        output = `${output}${entry[0]}=${entry[1]}\r`;
      }
      log.innerText = output;
      event.preventDefault();
    });
    

Try this example out and see how there's never more than one result for the `contact` group.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#additional_attributes)

--------------------------------------------------------------------------------------------------------------------------------

In addition to the common attributes shared by all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, `radio` inputs support the following attributes.

[`checked`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#checked)

A Boolean attribute which, if present, indicates that this radio button is the default selected one in the group.

Unlike other browsers, Firefox by default [persists the dynamic checked state](https://stackoverflow.com/questions/5985839/bug-with-firefox-disabled-attribute-of-input-not-resetting-when-refreshing "External link (opens in new tab)")
 of an `<input>` across page loads. Use the [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)
 attribute to control this feature.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#value_2)

The `value` attribute is one which all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
s share; however, it serves a special purpose for inputs of type `radio`: when a form is submitted, only radio buttons which are currently checked are submitted to the server, and the reported value is the value of the `value` attribute. If the `value` is not otherwise specified, it is the string `on` by default. This is demonstrated in the section [Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#value)
 above.

[`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)

The `required` attribute is one which most [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
s share. If any radio button in a same-named group of radio buttons has the `required` attribute, a radio button in that group must be checked, although it doesn't have to be the one with the attribute applied.

[Using radio inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#using_radio_inputs)

--------------------------------------------------------------------------------------------------------------------------

Radio buttons look and operate in a similar manner to the push buttons on old-fashioned radios, such as the one shown below.

![Shows what radio buttons looked like in the olden days.](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio/old-radio.jpg)

Radio buttons are similar to [checkboxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
, but with an important distinction: radio buttons are designed for selecting one value out of a set, whereas checkboxes let you turn individual values on and off. Where multiple controls exist, radio buttons allow one to be selected out of them all, whereas checkboxes allow multiple values to be selected.

We already covered the fundamentals of radio buttons above. Let's now look at the other common radio-button-related features and techniques you may need to know about.

### [Selecting a radio button by default](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#selecting_a_radio_button_by_default)

To make a radio button selected by default, you include `checked` attribute, as shown in this revised version of the previous example:

html

    <fieldset>
      <legend>Please select your preferred contact method:</legend>
      <div>
        <input
          type="radio"
          id="contactChoice1"
          name="contact"
          value="email"
          checked />
        <label for="contactChoice1">Email</label>
    
        <input type="radio" id="contactChoice2" name="contact" value="phone" />
        <label for="contactChoice2">Phone</label>
    
        <input type="radio" id="contactChoice3" name="contact" value="mail" />
        <label for="contactChoice3">Mail</label>
      </div>
    </fieldset>
    

In this case, the first radio button is now selected by default.

**Note:** If you put the `checked` attribute on more than one radio button, later instances will override earlier ones; that is, the last `checked` radio button will be the one that is selected. This is because only one radio button in a group can ever be selected at once, and the user agent automatically deselects others each time a new one is marked as checked.

### [Providing a bigger hit area for your radio buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#providing_a_bigger_hit_area_for_your_radio_buttons)

In the above examples, you may have noticed that you can select a radio button by clicking on its associated [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element, as well as on the radio button itself. This is a really useful feature of HTML form labels that makes it easier for users to click the option they want, especially on small-screen devices like smartphones.

Beyond accessibility, this is another good reason to properly set up `<label>` elements on your forms.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#validation)

----------------------------------------------------------------------------------------------------------

In the case of a radio button with the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)
 attribute set, or a same-named group of radio buttons in which at least one member has `required` set, a radio button needs to be selected for the control to be considered valid. If no radio button is checked, the [`valueMissing`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/valueMissing)
 property of a [`ValidityState`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)
 object will return `true` during validation, and the browser will ask the user to select an option.

[Styling radio inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#styling_radio_inputs)

------------------------------------------------------------------------------------------------------------------------------

The following example shows a slightly more thorough version of the example we've seen throughout the article, with some additional styling, and with better semantics established through use of specialized elements. The HTML looks like this:

html

    <fieldset>
      <legend>Please select your preferred contact method:</legend>
      <div>
        <input
          type="radio"
          id="contactChoice1"
          name="contact"
          value="email"
          checked />
        <label for="contactChoice1">Email</label>
    
        <input type="radio" id="contactChoice2" name="contact" value="phone" />
        <label for="contactChoice2">Phone</label>
    
        <input type="radio" id="contactChoice3" name="contact" value="mail" />
        <label for="contactChoice3">Mail</label>
      </div>
    </fieldset>
    

The CSS involved in this example is a bit more significant:

css

    html {
      font-family: sans-serif;
    }
    
    div:first-of-type {
      display: flex;
      align-items: flex-start;
      margin-bottom: 5px;
    }
    
    label {
      margin-right: 15px;
      line-height: 32px;
    }
    
    input {
      appearance: none;
    
      border-radius: 50%;
      width: 16px;
      height: 16px;
    
      border: 2px solid #999999;
      transition: 0.2s all linear;
      margin-right: 5px;
    
      position: relative;
      top: 4px;
    }
    
    input:checked {
      border: 6px solid black;
    }
    
    legend {
      color: white;
      background-color: black;
      padding: 5px 10px;
      border-radius: 0;
      border: 0;
      font-size: 14px;
    }
    

Most notable here is the use of the [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 property (with prefixes needed to support some browsers). By default, radio buttons (and [checkboxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
) are styled with the operating system's native styles for those controls. By specifying `appearance: none`, you can remove the native styling altogether, and create your own styles for them. Here we've used a [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 along with [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 and a [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 to create a nice animating radio selection. Notice also how the [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)
 pseudo-class is used to specify the styles for the radio button's appearance when selected.

**Note:** If you wish to use the [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 property, you should test it very carefully. Although it is supported in most modern browsers, its implementation varies widely. In older browsers, even the keyword `none` does not have the same effect across different browsers, and some do not support it at all. The differences are smaller in the newest browsers.

Notice that when clicking on a radio button, there's a nice, smooth fade out/in effect as the two buttons change state. In addition, the style and coloring of the legend are customized to have strong contrast. This might not be a look you'd want in a real web application, but it definitely shows off the possibilities.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#technical_summary)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#value)<br>** | A string representing the value of the radio button. |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported common attributes** | `[checked](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#checked) `, `[value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#value) ` and `[required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required) ` |
| **IDL attributes** | `checked` and `value` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | `[radio](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radio_role) ` |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# radio-button-state-(type=radio)](https://html.spec.whatwg.org/multipage/input.html#radio-button-state-(type=radio)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#see_also)

------------------------------------------------------------------------------------------------------

*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     and the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
     interface that implements it.
*   [`RadioNodeList`](https://developer.mozilla.org/en-US/docs/Web/API/RadioNodeList)
    : the interface that describes a list of radio buttons

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/radio/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/radio (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fradio&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fradio%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fradio%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fradio%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")