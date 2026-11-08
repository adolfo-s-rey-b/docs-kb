*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#mdn-search)
    

`:optional` CSS pseudo-class
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:optional`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents any [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element that does not have the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute set on it.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#try_it)

------------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 0.5em;
    }
    
    fieldset {
      margin-top: 0.5em;
    }
    
    *:optional {
      background-color: palegreen;
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
    

This pseudo-class is useful for styling fields that are not required to submit a form.

**Note:** The [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
 pseudo-class selects _required_ form fields.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#syntax)

------------------------------------------------------------------------------------------------

css

    :optional {
      /* ... */
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#accessibility)

--------------------------------------------------------------------------------------------------------------

If a [form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 contains optional [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
s, required inputs should be indicated using the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute. This will ensure that people navigating with the aid of assistive technology such as a screen reader will be able to understand which inputs need valid content to ensure a successful form submission.

Required inputs should also be indicated visually, using a treatment that does not rely solely on color to convey meaning. Typically, descriptive text and/or an icon are used.

*   [MDN Understanding WCAG, Guideline 3.3 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Understandable#guideline_3.3_%e2%80%94_input_assistance_help_users_avoid_and_correct_mistakes)
    
*   [Understanding Success Criterion 3.3.2 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/minimize-error-cues.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#examples)

----------------------------------------------------------------------------------------------------

### [The optional field has a purple border](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#the_optional_field_has_a_purple_border)

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
    
    input:optional {
      border-color: rebeccapurple;
      border-width: 3px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-optional](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-optional) |
| [Selectors Level 4  <br>\# optional-pseudo](https://drafts.csswg.org/selectors/#optional-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional#see_also)

----------------------------------------------------------------------------------------------------

*   Other validation-related pseudo-classes: [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
    , [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
    , [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
    
*   [Form data validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_optional/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_optional (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aoptional&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_optional%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aoptional%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_optional%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")