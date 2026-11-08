*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#mdn-search)
    

`<input type="checkbox">` HTML attribute value
==============================================

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`checkbox`** are rendered by default as boxes that are checked (ticked) when activated, like you might see in an official government paper form. The exact appearance depends upon the operating system configuration under which the browser is running. Generally this is a square but it may have rounded corners. A checkbox allows you to select single values for submission in a form (or not).

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#try_it)

-----------------------------------------------------------------------------------------------------

    <fieldset>
      <legend>Choose your monster's features:</legend>
    
      <div>
        <input type="checkbox" id="scales" name="scales" checked />
        <label for="scales">Scales</label>
      </div>
    
      <div>
        <input type="checkbox" id="horns" name="horns" />
        <label for="horns">Horns</label>
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
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#value)

---------------------------------------------------------------------------------------------------

A string representing the value of the checkbox. This is not displayed on the client-side, but on the server this is the `value` given to the data submitted with the checkbox's `name`. Take the following example:

html

    <form>
      <div>
        <input
          type="checkbox"
          id="subscribeNews"
          name="subscribe"
          value="newsletter" />
        <label for="subscribeNews">Subscribe to newsletter?</label>
      </div>
      <div>
        <button type="submit">Subscribe</button>
      </div>
    </form>
    

In this example, we've got a name of `subscribe`, and a value of `newsletter`. When the form is submitted, the data name/value pair will be `subscribe=newsletter`.

If the `value` attribute was omitted, the default value for the checkbox is `on`, so the submitted data in that case would be `subscribe=on`.

**Note:** If a checkbox is unchecked when its form is submitted, neither the name nor the value is submitted to the server. There is no HTML-only method of representing a checkbox's unchecked state (e.g., `value=unchecked`). If you wanted to submit a default value for the checkbox when it is unchecked, you could include JavaScript to create an [<input type="hidden">](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden)
 within the form with a value indicating an unchecked state.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#additional_attributes)

-----------------------------------------------------------------------------------------------------------------------------------

In addition to the [common attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#attributes)
 shared by all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, `checkbox` inputs support the following attributes.

[`checked`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#checked)

A [boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean/HTML)
 attribute indicating whether this checkbox is checked by default (when the page loads). It does _not_ indicate whether this checkbox is currently checked: if the checkbox's state is changed, this content attribute does not reflect the change. (Only the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
's `checked` IDL attribute is updated.)

**Note:** Unlike other input controls, a checkbox's value is only included in the submitted data if the checkbox is currently `checked`. If it is, then the value of the checkbox's `value` attribute is reported as the input's value, or `on` if no `value` is set. Unlike other browsers, Firefox by default [persists the dynamic checked state](https://stackoverflow.com/questions/5985839/bug-with-firefox-disabled-attribute-of-input-not-resetting-when-refreshing "External link (opens in new tab)")
 of an `<input>` across page loads. Use the [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)
 attribute to control this feature.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#value_2)

The `value` attribute is one which all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
s share; however, it serves a special purpose for inputs of type `checkbox`: when a form is submitted, only checkboxes which are currently checked are submitted to the server, and the reported value is the value of the `value` attribute. If the `value` is not otherwise specified, it is the string `on` by default. This is demonstrated in the section [Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#value)
 above.

[`switch`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#switch)

A [boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean/HTML)
 attribute that applies only to `checkbox` inputs. When present, it indicates that the `checkbox` represents an on/off `switch` rather than a normal `checkbox`. It alters the appearance of the `checkbox` control, but the underlying behavior remains the same as that of a normal `checkbox`.

**Note:** This attribute allows user agents to expose `switch` ARIA semantics to assistive technologies — without requiring documents to explicitly specify `role="switch"`. The markup and API are similar to those of checkboxes, except that the `:indeterminate` pseudo-class never matches.

**Warning:** This attribute is still experimental and has limited browser support. The attribute is ignored on unsupported browsers.

[Using checkbox inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#using_checkbox_inputs)

-----------------------------------------------------------------------------------------------------------------------------------

Checkboxes are similar to [radio buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
, but with an important distinction — [same-named radio buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio#defining_a_radio_group)
 are grouped into a set in which only one radio button can be selected at a time, whereas checkboxes allow you to turn single values on and off. Where multiple same-named controls exist, radio buttons allow one to be selected out of them all, whereas checkboxes allow multiple values to be selected.

### [Handling multiple checkboxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#handling_multiple_checkboxes)

The example we saw above only contained one checkbox; in real-world situations you'll be likely to encounter multiple checkboxes. If they are completely unrelated, then you can just deal with them all separately, as shown above. However, if they're all related, things are not quite so simple.

For example, in the following demo we include multiple checkboxes to allow the user to select their interests (see the full version in the [Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#examples)
 section).

html

    <fieldset>
      <legend>Choose your interests</legend>
      <div>
        <input type="checkbox" id="coding" name="interest" value="coding" />
        <label for="coding">Coding</label>
      </div>
      <div>
        <input type="checkbox" id="music" name="interest" value="music" />
        <label for="music">Music</label>
      </div>
    </fieldset>
    

In this example you will see that we've given each checkbox the same `name`. If both checkboxes are checked and then the form is submitted, you'll get a string of name/value pairs submitted like this: `interest=coding&interest=music`. When this string reaches the server, you need to parse it other than as an associative array, so all values, not only the last value, of `interest` are captured. For one technique used with Python, see [Handle Multiple Checkboxes with a Single Serverside Variable](https://stackoverflow.com/questions/18745456/handle-multiple-checkboxes-with-a-single-serverside-variable "External link (opens in new tab)")
, for example.

### [Checking boxes by default](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#checking_boxes_by_default)

To make a checkbox checked by default, you give it the `checked` attribute. See the below example:

html

    <fieldset>
      <legend>Choose your interests</legend>
      <div>
        <input type="checkbox" id="coding" name="interest" value="coding" checked />
        <label for="coding">Coding</label>
      </div>
      <div>
        <input type="checkbox" id="music" name="interest" value="music" />
        <label for="music">Music</label>
      </div>
    </fieldset>
    

### [Switch as a checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#switch_as_a_checkbox)

The following example shows how to make a checkbox look and act like an on/off switch.

html

    <fieldset>
      <legend>Adjust your setting</legend>
      <div>
        <label for="theme">Dark mode</label>
        <input type="checkbox" name="theme" id="theme" switch checked />
      </div>
      <div>
        <label for="notifications">Notifications</label>
        <input type="checkbox" name="notifications" id="notifications" switch />
      </div>
    </fieldset>
    

**Note:** While only some browsers render the checkbox as a switch, the behavior is the same across all browsers.

### [Providing a bigger hit area for your checkboxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#providing_a_bigger_hit_area_for_your_checkboxes)

In the above examples, you may have noticed that you can toggle a checkbox by clicking on its associated [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element as well as on the checkbox itself. This is a really useful feature of HTML form labels that makes it easier to click the option you want, especially on small-screen devices like smartphones.

Beyond accessibility, this is another good reason to properly set up `<label>` elements on your forms.

### [Indeterminate state checkboxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#indeterminate_state_checkboxes)

A checkbox can be in an **indeterminate** state. This is set using the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 object's [`indeterminate`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/indeterminate)
 property via JavaScript (it cannot be set using an HTML attribute):

js

    inputInstance.indeterminate = true;
    

When `indeterminate` is `true`, the checkbox has a horizontal line in the box (it looks somewhat like a hyphen or minus sign) instead of a check/tick in most browsers.

**Note:** This is purely a visual change. It has no impact on whether the checkbox's `value` is used in a form submission. That is decided by the `checked` state, regardless of the `indeterminate` state.

There are not many use cases for this property. The most common is when a checkbox is available that "owns" a number of sub-options (which are also checkboxes). If all of the sub-options are checked, the owning checkbox is also checked, and if they're all unchecked, the owning checkbox is unchecked. If any one or more of the sub-options have a different state than the others, the owning checkbox is in the indeterminate state.

This can be seen in the below example (thanks to [CSS Tricks](https://css-tricks.com/indeterminate-checkboxes/ "External link (opens in new tab)")
 for the inspiration). In this example we keep track of the ingredients we are collecting for a recipe. When you check or uncheck an ingredient's checkbox, a JavaScript function checks the total number of checked ingredients:

*   If none are checked, the recipe name's checkbox is set to unchecked.
*   If one or two are checked, the recipe name's checkbox is set to `indeterminate`.
*   If all three are checked, the recipe name's checkbox is set to `checked`.

So in this case the `indeterminate` state is used to state that collecting the ingredients has started, but the recipe is not yet complete.

js

    const overall = document.querySelector("#enchantment");
    const ingredients = document.querySelectorAll("ul input");
    
    overall.addEventListener("click", (e) => {
      e.preventDefault();
    });
    
    for (const ingredient of ingredients) {
      ingredient.addEventListener("click", updateDisplay);
    }
    
    function updateDisplay() {
      let checkedCount = 0;
      for (const ingredient of ingredients) {
        if (ingredient.checked) {
          checkedCount++;
        }
      }
    
      if (checkedCount === 0) {
        overall.checked = false;
        overall.indeterminate = false;
      } else if (checkedCount === ingredients.length) {
        overall.checked = true;
        overall.indeterminate = false;
      } else {
        overall.checked = false;
        overall.indeterminate = true;
      }
    }
    

html

    <fieldset>
      <legend>Complete the recipe</legend>
      <div>
        <input type="checkbox" id="enchantment" name="enchantment" />
        <label for="enchantment">Enchantment table</label>
        <ul>
          <li>
            <input type="checkbox" id="book" name="ingredient" value="book" />
            <label for="book">Book</label>
          </li>
          <li>
            <input
              type="checkbox"
              id="diamonds"
              name="ingredient"
              value="diamonds" />
            <label for="diamonds">Diamonds (x2)</label>
          </li>
          <li>
            <input
              type="checkbox"
              id="obsidian"
              name="ingredient"
              value="obsidian" />
            <label for="obsidian">Obsidian (x4)</label>
          </li>
        </ul>
      </div>
    </fieldset>
    

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#validation)

-------------------------------------------------------------------------------------------------------------

Checkboxes do support [validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 (offered to all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
s). However, most of the [`ValidityState`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)
s will always be `false`. If the checkbox has the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute, but is not checked, then [`ValidityState.valueMissing`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/valueMissing)
 will be `true`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#examples)

---------------------------------------------------------------------------------------------------------

The following example is an extended version of the "multiple checkboxes" example we saw above — it has more standard options, plus an "other" checkbox that when checked causes a text field to appear to enter a value for the "other" option. This is achieved with a short block of JavaScript. The example includes implicit labels, with the `<input>` directly inside the `<label>`. The text input, without a visible label, includes the [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
 attribute which provides its accessible name. This example also includes some CSS to improve the styling.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#html)

html

    <fieldset>
      <legend>Choose your interests</legend>
      <div>
        <label>
          <input type="checkbox" id="coding" name="interest" value="coding" />
          Coding
        </label>
      </div>
      <div>
        <label>
          <input type="checkbox" id="music" name="interest" value="music" />
          Music
        </label>
      </div>
      <div>
        <label>
          <input type="checkbox" id="art" name="interest" value="art" />
          Art
        </label>
      </div>
      <div>
        <label>
          <input type="checkbox" id="sports" name="interest" value="sports" />
          Sports
        </label>
      </div>
      <div>
        <label>
          <input type="checkbox" id="cooking" name="interest" value="cooking" />
          Cooking
        </label>
      </div>
      <div>
        <label>
          <input type="checkbox" id="other" name="interest" value="other" />
          Other
        </label>
        <input
          type="text"
          id="otherValue"
          name="other"
          aria-label="Other interest" />
      </div>
    </fieldset>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#css)

css

    html {
      font-family: sans-serif;
    }
    
    div {
      margin-bottom: 10px;
    }
    
    fieldset {
      width: 600px;
      margin: 0 auto;
      background: cyan;
      border: 5px solid blue;
    }
    
    legend {
      padding: 10px;
      background: blue;
      color: cyan;
    }
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#javascript)

js

    const otherCheckbox = document.querySelector("#other");
    const otherText = document.querySelector("#otherValue");
    otherText.style.visibility = "hidden";
    
    otherCheckbox.addEventListener("change", () => {
      if (otherCheckbox.checked) {
        otherText.style.visibility = "visible";
        otherText.value = "";
      } else {
        otherText.style.visibility = "hidden";
      }
    });
    

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#technical_summary)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#value)<br>** | A string representing the value of the checkbox. |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported common attributes** | `[checked](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#checked) ` and `[switch](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#switch) ` |
| **IDL attributes** | `[checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked) `, `[indeterminate](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/indeterminate) ` and `[value](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value) ` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [`checkbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/checkbox_role) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# checkbox-state-(type=checkbox)](https://html.spec.whatwg.org/multipage/input.html#checkbox-state-(type=checkbox)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.type\_checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#html.elements.input.type_checkbox)

### [html.elements.input.switch](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#html.elements.input.switch)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#see_also)

---------------------------------------------------------------------------------------------------------

*   [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)
    , [`:indeterminate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate)
    : CSS selectors that let you style checkboxes based on their current state
*   [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
    : HTML DOM API that implements the `<input>` element

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/checkbox/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/checkbox (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fcheckbox&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fcheckbox%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fcheckbox%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fcheckbox%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")