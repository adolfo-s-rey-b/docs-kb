*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#mdn-search)
    

`:read-write` CSS pseudo-class
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:read-write`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents an element (such as `input` or `textarea`) that is editable by the user.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#try_it)

--------------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 1em;
    }
    
    *:read-write {
      background-color: ivory;
      border: 2px solid darkorange;
      border-radius: 5px;
    }
    

    <p>Please fill in your details:</p>
    
    <label for="email">Email Address:</label>
    <input id="email" name="email" type="email" value="test@example.com" />
    
    <label for="note">Short note about yourself:</label>
    <textarea id="note" name="note">Don't be shy</textarea>
    
    <label for="pic">Your picture:</label>
    <input id="pic" name="pic" type="file" />
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#syntax)

--------------------------------------------------------------------------------------------------

css

    :read-write {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#examples)

------------------------------------------------------------------------------------------------------

### [Confirming form details using read-only controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#confirming_form_details_using_read-only_controls)

You can use [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)
 form controls when you want a user to verify information they entered earlier, which you want to submit with new data in read-write controls. In the example below, the [`:read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only)
 pseudo-class is used to make the [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 (a user's address) look like a regular paragraph. The `:read-write` pseudo-class provides a way to highlight the editable `<textarea>` (the delivery instructions):

    body {
      font-family: "Josefin Sans", sans-serif;
      margin: 10px auto;
    }
    
    legend {
      color: white;
      background: black;
      padding: 5px 10px;
    }
    
    fieldset > div {
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
    }
    
    label,
    textarea {
      display: block;
      font-family: inherit;
      font-size: 100%;
      margin: 0;
      box-sizing: border-box;
      padding: 5px;
      height: 30px;
    }
    
    textarea {
      width: 50%;
    }
    
    textarea {
      height: 70px;
      resize: none;
    }
    
    label {
      width: 40%;
    }
    

css

    textarea:read-only {
      border: 0;
    }
    
    textarea:read-write {
      box-shadow: inset 1px 1px 3px #cccccc;
      border-radius: 5px;
    }
    

html

    <fieldset>
      <legend>Confirm details</legend>
      <div>
        <label for="address">Address:</label>
        <textarea id="address" name="address" readonly>
    123 Choco Mountain,
    Awesome Ridge,
    CA</textarea>
      </div>
      <div>
        <label for="instructions">Delivery instructions</label>
        <textarea id="instructions" name="instructions"></textarea>
      </div>
    </fieldset>
    

### [Styling read-write non-form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#styling_read-write_non-form_controls)

This selector doesn't just select [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
/[`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements — it will select _any_ element that can be edited by the user, such as a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element with [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 set on it.

html

    <p contenteditable>This paragraph is editable; it is read-write.</p>
    
    <p>This paragraph is not editable; it is read-only.</p>
    

css

    body {
      font-family: sans-serif;
    }
    
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
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-read-write](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-read-write) |
| [Selectors Level 4  <br>\# read-write-pseudo](https://drafts.csswg.org/selectors/#read-write-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write#see_also)

------------------------------------------------------------------------------------------------------

*   [`:read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only)
    
*   HTML [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_read-write/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_read-write (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aread-write&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_read-write%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aread-write%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_read-write%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")