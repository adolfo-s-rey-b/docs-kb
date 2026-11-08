*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#mdn-search)
    

`autocorrect` HTML global attribute
===================================

Baseline 2026

Newly available

Since September 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`autocorrect`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute that controls whether autocorrection of editable text is enabled for spelling and/or punctuation errors.

The specific autocorrection behavior, including which words are substituted, depends on the user agent and the services provided by the underlying device. For example, on macOS a user agent might rely on [registered replacement text and punctuation](https://support.apple.com/en-vn/guide/mac-help/mh35735/mac "External link (opens in new tab)")
. Other devices and browsers may use a different approach.

Autocorrection is relevant to editable text elements:

*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     elements, except for [`password`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password)
    , [`email`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
    , and [`url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
    , which do not support autocorrection.
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
     elements.
*   Any element that has the [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     attribute set.

Editable elements have auto-correction enabled by default, except for within a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element, where the default value may be inherited from the form. Explicitly setting the attribute overrides the default.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#value)

---------------------------------------------------------------------------------------------------------

Possible values are:

[`on` or `""` (the empty string)](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#on)

Enable automatic correction of spelling and punctuation errors.

[`off`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#off)

Disable automatic correction of editable text.

The [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element types that don't support auto-correction always have the `off` state: [`password`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password)
, [`email`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
 and [`url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
.

For all other editable elements, setting any other value than those listed above is always treated as `on`. The default value for elements that are not nested inside a `<form>` is `on`.

When nested in a `<form>`, the following elements inherit their default value of `autocorrect` from the form if it has been set: [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#basic_example)

This example demonstrates basic `autocorrect` attribute usage.

#### HTML

We include two text `<input>` elements with different values for their `autocorrect` attributes:

html

    <label for="vegetable">A vegetable: </label>
    <input id="vegetable" name="vegetable" type="text" autocorrect="on" />
    
    <label for="fruit">A fruit: </label>
    <input id="fruit" name="fruit" type="text" autocorrect="off" />
    

#### Results

Enter invalid text into the fruit and vegetable text entry boxes above. If auto-correction is supported on your browser, and there is an appropriate substitution provided by the underlying device, a typo in a vegetable name input should be auto-corrected. Typos should not be corrected in the fruit name field.

### [Enabling and disabling autocorrection](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#enabling_and_disabling_autocorrection)

This example shows how you can enable and disable autocorrection using the `autocorrect` attribute.

#### HTML

The HTML markup defines a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, a "name" [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element of [`type="text"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
, a "bio" [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element, and two [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 elements.

The "username" element has `autocorrect="off"` set because auto-correcting a name would be annoying! The bio does not specify a value for `autocorrect`, which means that it is enabled (we could have set any value other than `off`).

html

    <button id="reset">Reset</button>
    <label for="username">Name: </label>
    <input id="username" name="username" type="text" autocorrect="off" />
    <label for="bio">Biography: </label>
    <textarea id="bio" name="bio"></textarea>
    

    <pre id="log"></pre>
    

    #log {
      height: 75px;
      overflow: scroll;
      padding: 0.5rem;
      border: 1px solid black;
    }
    
    button,
    input,
    textarea {
      display: block;
    }
    

    const logElement = document.querySelector("#log");
    function log(text) {
      logElement.innerText = `${logElement.innerText}${text}\n`;
      logElement.scrollTop = logElement.scrollHeight;
    }
    

#### JavaScript

The code checks whether the `autocorrect` is supported by checking if it is present on the prototype. If it is not present this fact is logged. If it is present then the value of the `autocorrect` property for each of the text-entry elements is logged.

A click handler is added for the button, which allows you to reset the entered text and the log.

js

    const resetButton = document.querySelector("#reset");
    const userNameElement = document.querySelector("#username");
    const bioElement = document.querySelector("#bio");
    
    if (!("autocorrect" in HTMLElement.prototype)) {
      log("autocorrect not supported");
    } else {
      log(`userNameElement.autocorrect: ${userNameElement.autocorrect}`);
      log(`bioElement.autocorrect: ${bioElement.autocorrect}`);
    }
    
    resetButton.addEventListener("click", (e) => {
      userNameElement.value = "";
      bioElement.value = "";
    });
    

#### Results

If auto-correction is supported by your browser, the log area below the "Biography" and "Name" inputs should show that it is enabled for "Biography" inputs but not "Name" inputs.

Enter invalid text into the name and biography text entry boxes. If the device has a substitute for the entered word, this will be used to autocorrect text in the "Biography" input (only).

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-autocorrect](https://html.spec.whatwg.org/multipage/interaction.html#attr-autocorrect) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect#see_also)

---------------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   [`spellcheck`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/autocorrect/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/autocorrect (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fautocorrect&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fautocorrect%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fautocorrect%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fautocorrect%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")