*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#mdn-search)
    

`:invalid` CSS pseudo-class
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:invalid`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents any [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or other [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element whose contents fail to [validate](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
.

This pseudo-class is useful for highlighting field errors for the user.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#try_it)

-----------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 1em;
    }
    
    input:invalid {
      background-color: ivory;
      border: none;
      outline: 2px solid red;
      border-radius: 5px;
    }
    

    <label for="email">Email Address:</label>
    <input id="email" name="email" type="email" value="na@me@example.com" />
    
    <label for="secret">Secret Code: (lower case letters)</label>
    <input id="secret" name="secret" type="text" value="test" pattern="[a-z]+" />
    
    <label for="age">Your age: (18+)</label>
    <input id="age" name="age" type="number" value="5" min="18" />
    
    <label
      ><input name="tos" type="checkbox" required checked /> - Do you agree to
      ToS?</label
    >
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#syntax)

-----------------------------------------------------------------------------------------------

css

    :invalid {
      /* ... */
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#accessibility)

-------------------------------------------------------------------------------------------------------------

The color red is commonly used to indicate invalid input. People who have certain types of color blindness will be unable to determine the input's state unless it is accompanied by an additional indicator that does not rely on color to convey meaning. Typically, descriptive text and/or an icon are used.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-without-color.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#examples)

---------------------------------------------------------------------------------------------------

### [Coloring elements to show validation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#coloring_elements_to_show_validation)

#### HTML

html

    <form>
      <div class="field">
        <label for="url_input">Enter a URL:</label>
        <input type="url" id="url_input" />
      </div>
    
      <div class="field">
        <label for="email_input">Enter an email address:</label>
        <input type="email" id="email_input" required />
      </div>
    </form>
    

#### CSS

css

    label {
      display: block;
      margin: 1px;
      padding: 1px;
    }
    
    .field {
      margin: 1px;
      padding: 1px;
    }
    
    input:invalid {
      background-color: #ffdddd;
    }
    
    form:invalid {
      border: 5px solid #ffdddd;
    }
    
    input:valid {
      background-color: #ddffdd;
    }
    
    form:valid {
      border: 5px solid #ddffdd;
    }
    
    input:required {
      border-color: maroon;
      border-width: 3px;
    }
    
    input:required:invalid {
      border-color: #c00000;
    }
    

#### Result

### [Showing sections in stages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#showing_sections_in_stages)

In this example we use `:invalid` along with `~`, the [subsequent-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator)
, to make a form appear in stages, so the form initially shows the first item to complete, and when the user completes each item the form displays the next one. When the whole form is complete the user can submit it.

#### HTML

html

    <form>
      <fieldset>
        <legend>Personal Information</legend>
        <label for="form-name">Name</label><br />
        <input type="text" name="name" id="form-name" required />
      </fieldset>
    
      <fieldset>
        <legend>Contact Information</legend>
        <label for="form-email">Email Address</label><br />
        <input type="email" name="email" id="form-email" required />
      </fieldset>
    
      <fieldset>
        <legend>Message</legend>
        <label for="form-message">Message</label><br />
        <textarea name="message" id="form-message" required></textarea>
      </fieldset>
    
      <button type="submit" name="send">Submit</button>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

#### CSS

css

    /* Hide the fieldset after an invalid fieldset */
    fieldset:invalid ~ fieldset {
      display: none;
    }
    
    /* Dim and disable the button while the form is invalid */
    form:invalid button {
      opacity: 0.3;
      pointer-events: none;
    }
    
    input,
    textarea {
      box-sizing: border-box;
      width: 100%;
      font-family: monospace;
      padding: 0.25em 0.5em;
    }
    
    button {
      width: 100%;
      border: thin solid darkgrey;
      font-size: 1.25em;
      background-color: darkgrey;
      color: white;
    }
    

#### Result

[Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#notes)

---------------------------------------------------------------------------------------------

### [Radio buttons](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#radio_buttons)

If any one of the radio buttons in a group is `required`, the `:invalid` pseudo-class is applied to all of them if none of the buttons in the group is selected. (Grouped radio buttons share the same value for their `name` attribute.)

### [Gecko defaults](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#gecko_defaults)

By default, Gecko does not apply a style to the `:invalid` pseudo-class. However, it does apply a style (a red "glow" using the [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 property) to the [`:user-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid)
 pseudo-class, which applies in a subset of cases for `:invalid`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-invalid](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-invalid) |
| [Selectors Level 4  <br>\# invalid-pseudo](https://drafts.csswg.org/selectors/#invalid-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid#see_also)

---------------------------------------------------------------------------------------------------

*   Other validation-related pseudo-classes: [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
    , [`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)
    , [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
    
*   Related Mozilla pseudo-classes: [`:user-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid)
    , [`:-moz-submit-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-submit-invalid)
    
*   [Form data validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
    
*   Accessing the [validity state](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)
     from JavaScript

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_invalid/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_invalid (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ainvalid&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_invalid%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ainvalid%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_invalid%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")