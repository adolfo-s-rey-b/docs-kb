*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#mdn-search)
    

`:disabled` CSS pseudo-class
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:disabled`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents any disabled element. An element is disabled if it can't be activated (selected, clicked on, typed into, etc.) or accept focus. The element also has an enabled state, in which it can be activated or accept focus.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#try_it)

------------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 1em;
    }
    
    *:disabled {
      background-color: dimgrey;
      color: linen;
      opacity: 1;
    }
    

    <form>
      <label for="name">Name:</label>
      <input id="name" name="name" type="text" />
    
      <label for="emp">Employed:</label>
      <select id="emp" name="emp" disabled>
        <option>No</option>
        <option>Yes</option>
      </select>
    
      <label for="empDate">Employment Date:</label>
      <input id="empDate" name="empDate" type="date" disabled />
    
      <label for="resume">Resume:</label>
      <input id="resume" name="resume" type="file" />
    </form>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#syntax)

------------------------------------------------------------------------------------------------

css

    :disabled {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#examples)

----------------------------------------------------------------------------------------------------

This example shows a basic shipping form. It uses the [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
 [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")
 event to let the user enable/disable the billing fields.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#html)

html

    <form action="#">
      <fieldset id="shipping">
        <legend>Shipping address</legend>
        <input type="text" placeholder="Name" />
        <input type="text" placeholder="Address" />
        <input type="text" placeholder="Zip Code" />
      </fieldset>
      <br />
      <fieldset id="billing">
        <legend>Billing address</legend>
        <label for="billing-checkbox">Same as shipping address:</label>
        <input type="checkbox" id="billing-checkbox" checked />
        <br />
        <input type="text" placeholder="Name" disabled />
        <input type="text" placeholder="Address" disabled />
        <input type="text" placeholder="Zip Code" disabled />
      </fieldset>
    </form>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#css)

css

    input[type="text"]:disabled {
      background: #cccccc;
    }
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#javascript)

Toggle the disabled input fields when the checkbox is clicked

js

    const checkbox = document.querySelector("#billing-checkbox");
    const billingItems = document.querySelectorAll('#billing input[type="text"]');
    
    checkbox.addEventListener("change", () => {
      billingItems.forEach((item) => {
        item.disabled = !item.disabled;
      });
    });
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#result)

Check/un-check the checkbox to change the styling on the billing fields.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-disabled](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-disabled) |
| [Selectors Level 4  <br>\# disabled-pseudo](https://drafts.csswg.org/selectors/#disabled-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled#see_also)

----------------------------------------------------------------------------------------------------

*   [`:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_disabled/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_disabled (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Adisabled&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_disabled%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Adisabled%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_disabled%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")