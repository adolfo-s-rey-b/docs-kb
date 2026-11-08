*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#mdn-search)
    

`:read-only` CSS pseudo-class
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:read-only`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selects elements (such as certain [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 types and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
) that are not editable by the user. Elements on which the HTML attribute [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)
 doesn't have an effect (such as [`<input type="radio">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
, [`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
, and all other non-form elements) are also selected by the `:read-only` pseudo-class. In fact, `:read-only` matches anything that [`:read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write)
 doesn't match, making it equivalent to `:not(:read-write)`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#try_it)

-------------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 1em;
    }
    
    *:read-only {
      font-weight: bold;
      color: indigo;
    }
    

    <p>Please enter your details:</p>
    
    <label for="email">Email Address:</label>
    <input id="email" name="email" type="email" value="test@example.com" readonly />
    
    <label for="note">Short note about yourself:</label>
    <textarea id="note" name="note">Don't be shy</textarea>
    
    <label for="pic">Your picture:</label>
    <input id="pic" name="pic" type="file" />
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#syntax)

-------------------------------------------------------------------------------------------------

css

    :read-only {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#examples)

-----------------------------------------------------------------------------------------------------

### [Confirming form information using read-only or read-write controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#confirming_form_information_using_read-only_or_read-write_controls)

One use of read-only form controls is to allow the user to check and verify information that they may have entered in an earlier form (for example, shipping details), while still being able to submit the information along with the rest of the form. This example shows how to style these controls.

The `:read-only` pseudo-class is used to remove all the styling that makes the inputs look like clickable fields, making them look more like read-only paragraphs. The `:read-write` pseudo-class on the other hand is used to provide some nicer styling to the editable `<textarea>`.

    <fieldset>
      <legend>Check shipping details</legend>
      <div>
        <label for="name">Name: </label>
        <input id="name" name="name" type="text" value="Mr Soft" readonly />
      </div>
      <div>
        <label for="address">Address: </label>
        <textarea id="address" name="address" readonly>
    23 Elastic Way,
    Viscous,
    Bright Ridge,
    CA
    </textarea>
      </div>
      <div>
        <label for="postal-code">Zip/postal code: </label>
        <input
          id="postal-code"
          name="postal-code"
          type="text"
          value="94708"
          readonly />
      </div>
    </fieldset>
    
    <fieldset>
      <legend>Final instructions</legend>
      <div>
        <label for="sms-confirm">Send confirmation by SMS?</label>
        <input id="sms-confirm" name="sms-confirm" type="checkbox" />
      </div>
      <div>
        <label for="instructions">Any special instructions?</label>
        <textarea id="instructions" name="instructions"></textarea>
      </div>
    </fieldset>
    

    body {
      font-family: "Josefin Sans", sans-serif;
      margin: 20px auto;
      max-width: 460px;
    }
    
    fieldset {
      padding: 10px 30px 0;
      margin-bottom: 20px;
    }
    
    legend {
      color: white;
      background: black;
      padding: 5px 10px;
    }
    
    fieldset > div {
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
    }
    
    label,
    input[type="text"],
    textarea {
      display: block;
      font-family: inherit;
      font-size: 100%;
      margin: 0;
      box-sizing: border-box;
      padding: 5px;
      height: 30px;
    }
    
    input[type="text"],
    textarea {
      width: 50%;
    }
    
    textarea {
      height: 110px;
      resize: none;
    }
    
    label {
      width: 40%;
    }
    
    input:hover,
    input:focus,
    textarea:hover,
    textarea:focus {
      background-color: #eeeeee;
    }
    

css

    input:read-only,
    textarea:read-only {
      border: 0;
      box-shadow: none;
      background-color: #dddddd;
    }
    
    textarea:read-write {
      outline: 1px dashed red;
      outline-offset: 2px;
      border-radius: 5px;
    }
    

### [Styling read-only non-form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#styling_read-only_non-form_controls)

This selector doesn't just select [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
/[`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements — it will select _any_ element that cannot be edited by the user.

html

    <p contenteditable>This paragraph is editable; it is read-write.</p>
    
    <p>This paragraph is not editable; it is read-only.</p>
    

css

    p {
      font-size: 150%;
      padding: 5px;
      border-radius: 5px;
    }
    
    p:read-only {
      background-color: red;
      color: white;
    }
    
    p:read-write {
      background-color: lime;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-read-only](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-read-only) |
| [Selectors Level 4  <br>\# read-only-pseudo](https://drafts.csswg.org/selectors/#read-only-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only#see_also)

-----------------------------------------------------------------------------------------------------

*   [`:read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write)
    
*   HTML [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_read-only/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_read-only (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aread-only&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_read-only%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aread-only%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_read-only%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")