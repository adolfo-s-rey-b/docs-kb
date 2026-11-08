*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#mdn-search)
    

`:valid` CSS pseudo-class
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:valid`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents any [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or other [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element whose contents [validate](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 successfully. This allows you to easily make valid fields adopt an appearance that helps the user confirm that their data is formatted properly.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#try_it)

---------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 1em;
    }
    
    input:valid {
      background-color: ivory;
      border: none;
      outline: 2px solid deepskyblue;
      border-radius: 5px;
      accent-color: gold;
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#syntax)

---------------------------------------------------------------------------------------------

css

    :valid {
      /* ... */
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#accessibility)

-----------------------------------------------------------------------------------------------------------

The color green is commonly used to indicate valid input. People who have certain types of color blindness will be unable to determine the input's state unless it is accompanied by an additional indicator that does not rely on color to convey meaning. Typically, descriptive text and/or an icon are used.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-without-color.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#examples)

-------------------------------------------------------------------------------------------------

### [Indicating valid and invalid form fields](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#indicating_valid_and_invalid_form_fields)

In this example, we include extra `<span>` elements to generate content that indicates valid or invalid data:

html

    <fieldset>
      <legend>Contact information</legend>
      <p>Required fields are labeled with "required".</p>
      <div>
        <label for="fname">First name: </label>
        <input id="fname" name="fname" type="text" required />
        <span></span>
      </div>
      <div>
        <label for="lname">Last name: </label>
        <input id="lname" name="lname" type="text" required />
        <span></span>
      </div>
      <div>
        <label for="email"> Email address (include if you want a response): </label>
        <input id="email" name="email" type="email" />
        <span></span>
      </div>
    </fieldset>
    

To provide these indicators, we use the following CSS:

    body {
      font-family: sans-serif;
      margin: 20px auto;
      max-width: 460px;
    }
    
    fieldset {
      padding: 10px 30px 0;
    }
    
    legend {
      color: white;
      background: black;
      padding: 5px 10px;
    }
    
    fieldset > div {
      margin-bottom: 20px;
      display: flex;
      flex-flow: row wrap;
    }
    
    label,
    input {
      display: block;
      font-family: inherit;
      margin: 0;
      box-sizing: border-box;
      width: 100%;
      padding: 5px;
      height: 30px;
    }
    
    input {
      box-shadow: inset 1px 1px 3px #cccccc;
      border-radius: 5px;
    }
    
    input:hover,
    input:focus {
      background-color: #eeeeee;
    }
    
    input:required + span::after {
      font-size: 0.7rem;
      position: absolute;
      content: "required";
      color: white;
      background-color: black;
      padding: 5px 10px;
      top: -26px;
      left: -70px;
    }
    

css

    input + span {
      position: relative;
    }
    
    input + span::before {
      position: absolute;
      right: -20px;
      top: 5px;
    }
    
    input:invalid {
      border: 2px solid red;
    }
    
    input:invalid + span::before {
      content: "✖";
      color: red;
    }
    
    input:valid + span::before {
      content: "✓";
      color: green;
    }
    

We set the `<span>`s to `position: relative` so that we can position the generated content relative to them. We then absolutely position different generated content depending on whether the form's data is valid or invalid — a green check or a red cross, respectively. To add a bit of extra urgency to the invalid data, we've also given the inputs a thick red border when invalid.

**Note:** We've used `::before` to add these labels, as we were already using `::after` for the "required" labels.

You can try it below:

Notice how the required text inputs are invalid when empty, but valid when they have something filled in. The email input on the other hand is valid when empty, as it is not required, but invalid when it contains something that is not a proper email address.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-valid](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-valid) |
| [Selectors Level 4  <br>\# valid-pseudo](https://drafts.csswg.org/selectors/#valid-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid#see_also)

-------------------------------------------------------------------------------------------------

*   Other validation-related pseudo-classes: [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
    , [`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)
    , [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
    
*   [Form data validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
    
*   Accessing the [validity state](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)
     from JavaScript

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_valid/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_valid (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Avalid&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_valid%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Avalid%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_valid%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")