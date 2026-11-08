*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#mdn-search)
    

`:indeterminate` CSS pseudo-class
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:indeterminate`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents any form element whose state is indeterminate, such as checkboxes that have been set to an [`indeterminate`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/indeterminate)
 state with JavaScript, radio buttons which are members of a group in which all radio buttons are unchecked, and [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
 elements with no `value` attribute.

css

    /* Selects any <input> whose state is indeterminate */
    input:indeterminate {
      background: lime;
    }
    

Elements targeted by this selector are:

*   [`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
     elements with the [`indeterminate`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/indeterminate)
     property set to `true`.
*   [`<input type="radio">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
     elements with the same `name` value and none of them `checked`.
*   [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
     elements with no `value`, placing them in an indeterminate state.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#syntax)

-----------------------------------------------------------------------------------------------------

css

    :indeterminate {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#examples)

---------------------------------------------------------------------------------------------------------

### [Checkbox & radio button](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#checkbox_radio_button)

This example applies special styles to the labels associated with indeterminate form fields.

#### HTML

html

    <fieldset>
      <legend>Checkbox</legend>
      <div>
        <input type="checkbox" id="checkbox" />
        <label for="checkbox">This checkbox label starts out lime.</label>
      </div>
    </fieldset>
    
    <fieldset>
      <legend>Radio</legend>
      <div>
        <input type="radio" id="radio1" name="radioButton" value="val1" />
        <label for="radio1">First radio label starts out lime.</label>
      </div>
      <div>
        <input type="radio" id="radio2" name="radioButton" value="val2" />
        <label for="radio2">Second radio label also starts out lime.</label>
      </div>
    </fieldset>
    

#### CSS

css

    input:indeterminate + label {
      background: lime;
    }
    

    fieldset {
      padding: 1em 0.75em;
    }
    
    fieldset:first-of-type {
      margin-bottom: 1.5rem;
    }
    
    fieldset:not(:first-of-type) > div:not(:last-child) {
      margin-bottom: 0.5rem;
    }
    

#### JavaScript

js

    const inputs = document.getElementsByTagName("input");
    
    for (const input of inputs) {
      input.indeterminate = true;
    }
    

#### Result

### [Progress bar](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#progress_bar)

#### HTML

html

    <progress></progress>
    

#### CSS

css

    progress {
      margin: 4px;
    }
    
    progress:indeterminate {
      width: 80vw;
      height: 20px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-indeterminate](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-indeterminate) |
| [Selectors Level 4  <br>\# indeterminate-pseudo](https://drafts.csswg.org/selectors/#indeterminate-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate#see_also)

---------------------------------------------------------------------------------------------------------

*   [Web forms — Working with user data](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   [Styling web forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms)
    
*   The [`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
     element's [`indeterminate`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/indeterminate)
     property
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     and the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
     interface which implements it.
*   The [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)
     CSS selector lets you style checkboxes based on whether they're checked or not

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_indeterminate/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_indeterminate (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aindeterminate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_indeterminate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aindeterminate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_indeterminate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")