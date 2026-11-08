*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid#mdn-search)
    

`:user-valid` CSS pseudo-class
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:user-valid`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents any validated form element whose value validates correctly based on its [validation constraints](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. However, unlike [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 it only matches once the user has interacted with it.

This pseudo-class is applied if the form control is valid and any of the following has occurred:

*   The user made a change to the form control and committed the change such as by moving focus elsewhere.
*   The user has attempted to submit the form, even if no change was made to the control.
*   The value was invalid when it gained focus, and the user made a change making it valid, even if focus is still in the control.

Once this pseudo-class has been applied, the user-agent re-validates whether the control is valid at every keystroke when the control has focus.

*   If the control has focus, and the value was invalid when it gained focus, re-validate on every keystroke.

The result is that if the control was valid when the user started interacting with it, the validity styling is changed only when the user shifts focus to another control. However, if the user is trying to correct a previously-flagged value, the control shows immediately when the value becomes valid. Required items are flagged as invalid only if the user changes them or attempts to submit an unchanged invalid value.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid#syntax)

--------------------------------------------------------------------------------------------------

css

    :user-valid {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid#examples)

------------------------------------------------------------------------------------------------------

### [Setting a color and symbol on :user-valid](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid#setting_a_color_and_symbol_on_user-valid)

In the following example, the green border and ✅ only display once the user has interacted with the field. Try changing the email address to another valid email to see it in action.

html

    <label for="email">Email *: </label>
    <input id="email" name="email" type="email" value="test@example.com" required />
    <span></span>
    

css

    input:user-valid {
      border: 2px solid green;
    }
    
    input:user-valid + span::before {
      content: "✓";
      color: green;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-user-valid](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-user-valid) |
| [Selectors Level 4  <br>\# user-valid-pseudo](https://drafts.csswg.org/selectors/#user-valid-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid#see_also)

------------------------------------------------------------------------------------------------------

*   [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
    
*   [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
    
*   [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
    
*   [`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)
    
*   [`:user-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_user-valid/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_user-valid (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Auser-valid&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_user-valid%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Auser-valid%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_user-valid%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")