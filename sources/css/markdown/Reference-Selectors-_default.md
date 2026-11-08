*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#mdn-search)
    

`:default` CSS pseudo-class
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:default`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selects form elements that are the default in a group of related elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#try_it)

-----------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 0.5em;
    }
    
    fieldset {
      margin-top: 0.5em;
    }
    
    input:default {
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
    

What this selector matches is defined in [HTML Standard §4.16.3 Pseudo-classes](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-default "External link (opens in new tab)")
 — it may match the [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
, [`<input type="radio">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
, and [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 elements:

*   A default option element is the first one with the `selected` attribute, or the first enabled option in DOM order. `multiple` [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    s can have more than one `selected` option, so all will match `:default`.
*   `<input type="checkbox">` and `<input type="radio">` match if they have the `checked` attribute.
*   [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
     matches if it is a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
    's [default submission button](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#implicit-submission "External link (opens in new tab)")
    : the first `<button>` in DOM order that belongs to the form. This also applies to [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     types that submit forms, like `image` or `submit`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#syntax)

-----------------------------------------------------------------------------------------------

css

    :default {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#examples)

---------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#html)

html

    <fieldset>
      <legend>Favorite season</legend>
    
      <input type="radio" name="season" id="spring" value="spring" />
      <label for="spring">Spring</label>
    
      <input type="radio" name="season" id="summer" value="summer" checked />
      <label for="summer">Summer</label>
    
      <input type="radio" name="season" id="fall" value="fall" />
      <label for="fall">Fall</label>
    
      <input type="radio" name="season" id="winter" value="winter" />
      <label for="winter">Winter</label>
    </fieldset>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#css)

css

    input:default {
      box-shadow: 0 0 2px 1px coral;
    }
    
    input:default + label {
      color: coral;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-default](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-default) |
| [Selectors Level 4  <br>\# default-pseudo](https://drafts.csswg.org/selectors/#default-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default#see_also)

---------------------------------------------------------------------------------------------------

*   [Web forms — Working with user data](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   [Styling web forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms)
    
*   Related HTML elements: [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    , [`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
    , [`<input type="radio">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
    , and [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_default/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_default (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Adefault&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_default%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Adefault%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_default%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")