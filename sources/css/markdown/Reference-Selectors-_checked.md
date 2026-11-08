*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#mdn-search)
    

`:checked` CSS pseudo-class
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:checked`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selector represents any **radio** ([`<input type="radio">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
), **checkbox** ([`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
), or **option** ([`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 in a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element) that is checked or toggled to an `on` state.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#try_it)

-----------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 0.5em;
    }
    
    fieldset {
      margin-top: 0.5em;
    }
    
    input:checked {
      border: none;
      outline: 2px solid deeppink;
    }
    

    <label for="name">Name (required):</label>
    <input id="name" name="name" type="text" required />
    
    <label for="birth">Date of birth:</label>
    <input id="birth" name="birth" type="date" />
    
    <label for="origin">How did you find out about us? (required)</label>
    <select id="origin" name="origin" required>
      <option value="">Choose an option</option>
      <option value="google">Google</option>
      <option value="facebook">Facebook</option>
      <option value="advertisement">Advertisement</option>
    </select>
    
    <fieldset>
      <legend>Preferred contact method:</legend>
      <label>
        <input name="contact" type="radio" value="email" checked /> Email
      </label>
      <label><input name="contact" type="radio" value="phone" /> Phone</label>
    </fieldset>
    
    <label>
      <input name="newsletter" type="checkbox" checked /> I want to subscribe to a
      personalized newsletter.
    </label>
    <label>
      <input name="privacy" type="checkbox" required /> I have read and I agree to
      the Privacy Policy (required).
    </label>
    

The user can engage this state by checking/selecting an element, or disengage it by unchecking/deselecting the element.

**Note:** Because browsers often treat `<option>`s as [replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
, the extent to which they can be styled with the `:checked` pseudo-class varies from browser to browser. [Customizable select element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
 functionality can be used to enable full customization of `<option>` elements just like any regular DOM element, in supporting browsers.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#syntax)

-----------------------------------------------------------------------------------------------

css

    :checked {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#examples)

---------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#basic_example)

#### HTML

html

    <div>
      <input type="radio" name="my-input" id="yes" value="yes" />
      <label for="yes">Yes</label>
    
      <input type="radio" name="my-input" id="no" value="no" />
      <label for="no">No</label>
    </div>
    
    <div>
      <input type="checkbox" name="my-checkbox" id="opt-in" />
      <label for="opt-in">Check me!</label>
    </div>
    
    <select name="my-select" id="fruit">
      <option value="opt1">Apples</option>
      <option value="opt2">Grapes</option>
      <option value="opt3">Pears</option>
    </select>
    

#### CSS

css

    div,
    select {
      margin: 8px;
    }
    
    /* Labels for checked inputs */
    input:checked + label {
      color: red;
    }
    
    /* Radio element, when checked */
    input[type="radio"]:checked {
      box-shadow: 0 0 0 3px orange;
    }
    
    /* Checkbox element, when checked */
    input[type="checkbox"]:checked {
      box-shadow: 0 0 0 3px hotpink;
    }
    
    /* Option elements, when selected */
    option:checked {
      box-shadow: 0 0 0 3px lime;
      color: red;
    }
    

#### Result

### [Toggling elements with a hidden checkbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#toggling_elements_with_a_hidden_checkbox)

This example utilizes the `:checked` pseudo-class to let the user toggle content based on the state of a checkbox, all without using [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
.

#### HTML

html

    <input type="checkbox" id="expand-toggle" />
    
    <table>
      <thead>
        <tr>
          <th>Column #1</th>
          <th>Column #2</th>
          <th>Column #3</th>
        </tr>
      </thead>
      <tbody>
        <tr class="expandable">
          <td>[more text]</td>
          <td>[more text]</td>
          <td>[more text]</td>
        </tr>
        <tr>
          <td>[cell text]</td>
          <td>[cell text]</td>
          <td>[cell text]</td>
        </tr>
        <tr>
          <td>[cell text]</td>
          <td>[cell text]</td>
          <td>[cell text]</td>
        </tr>
        <tr class="expandable">
          <td>[more text]</td>
          <td>[more text]</td>
          <td>[more text]</td>
        </tr>
        <tr class="expandable">
          <td>[more text]</td>
          <td>[more text]</td>
          <td>[more text]</td>
        </tr>
      </tbody>
    </table>
    
    <label for="expand-toggle" id="expand-btn">Toggle hidden rows</label>
    

#### CSS

css

    /* Hide the toggle checkbox */
    #expand-toggle {
      display: none;
    }
    
    /* Hide expandable content by default */
    .expandable {
      visibility: collapse;
      background: #dddddd;
    }
    
    /* Style the button */
    #expand-btn {
      display: inline-block;
      margin-top: 12px;
      padding: 5px 11px;
      background-color: #ffff77;
      border: 1px solid;
      border-radius: 3px;
    }
    
    /* Show hidden content when the checkbox is checked */
    #expand-toggle:checked ~ * .expandable {
      visibility: visible;
    }
    
    /* Style the button when the checkbox is checked */
    #expand-toggle:checked ~ #expand-btn {
      background-color: #cccccc;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-checked](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-checked) |
| [Selectors Level 4  <br>\# checked-pseudo](https://drafts.csswg.org/selectors/#checked-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked#see_also)

---------------------------------------------------------------------------------------------------

*   [Web forms — working with user data](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   [Styling web forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms)
    
*   Related HTML elements: [`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
    , [`<input type="radio">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
    , [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    , and [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
    
*   [Replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_checked/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_checked (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Achecked&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_checked%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Achecked%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_checked%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")