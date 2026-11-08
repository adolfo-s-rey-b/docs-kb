*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#mdn-search)
    

`:autofill` CSS pseudo-class
============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/500)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:autofill`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches when an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element has its value autofilled by the browser. The class stops matching if the user edits the field.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#try_it)

------------------------------------------------------------------------------------------------

    input {
      border: 3px solid black;
    }
    input:autofill {
      outline: 5px solid magenta;
      border: 3px dashed yellow;
    }
    

    <form>
      <p>Click on the text box and choose any option suggested by your browser.</p>
      <p>
        <label for="name">Name</label>
        <input id="name" name="name" type="text" autocomplete="given-name" />
      </p>
      <p>
        <label for="email">Email Address</label>
        <input id="email" name="email" type="email" autocomplete="email" />
      </p>
      <p>
        <label for="country">Country</label>
        <input
          id="country"
          name="country"
          type="text"
          autocomplete="country-name" />
      </p>
    </form>
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#description)

----------------------------------------------------------------------------------------------------------

The `:autofill` pseudo-class selects [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements containing un-edited content that was auto-filled by the user-agent. Autocompletion may occur when browser settings are set to enable autocompletion or the [`autocomplete` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)
 is set on the element itself.

When the user uses the browser's autocompletion feature to autofill a form control, all the form controls that can be autofilled based on the selection get populated. These will all match the `:autofill` UI state. If the user edits a control, that control will no longer match `:autofill`, even if the value is the same as the autofilled value.

The specification includes the vendor-prefixed `:-webkit-autofill` pseudo-class as an alias. This also matches input elements autofilled by the user agent, and no longer matches if the user edits the autofilled field.

Note that the user agent style sheets of many browsers use `!important` in their style declarations, making some styles non-overridable. For example, Chrome has the following in its internal stylesheet:

css

    input:-internal-autofill-selected {
      appearance: menulist-button;
      background-image: none !important;
      background-color:
        light-dark(rgb(232 240 254), rgb(70 90 126 / 0.4)) !important;
      color: fieldtext !important;
    }
    

This means that you cannot override the default [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
, or [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 values on selected autofilled input elements in your own rules, but you can override the [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
, and you can override these properties for the autofilled elements that aren't currently focused.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#syntax)

------------------------------------------------------------------------------------------------

css

    :autofill {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#examples)

----------------------------------------------------------------------------------------------------

The following example demonstrates the use of the `:autofill` pseudo-class to change the border of a text field that has been autocompleted by the browser.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#html)

We include three HTML `<input>` elements, each with an associated [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
. The `name` and `email` will likely autocomplete and match `:autofill`, while the `pet` value is unlikely to.

html

    <form method="post" action="">
      <p>
        <label for="name">Name: </label>
        <input name="n" id="name" autocomplete="given-name" />
      </p>
      <p>
        <label for="email">Email: </label>
        <input type="email" name="email" id="email" autocomplete="email" />
      </p>
      <p>
        <label for="pet">Your pet's name: </label>
        <input name="pet" id="pet" />
      </p>
    </form>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#css)

We apply a [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
, [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
, and [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
 to the `<input>` elements when they match the `:autofill` state.

css

    input {
      border-radius: 0px;
    }
    
    input:autofill {
      border-radius: 0.5lh;
      outline: 5px dashed magenta;
      border-color: yellow;
    }
    

    @supports not selector(:autofill) {
      body::before {
        content: "Your browser doesn't support the :autofill selector.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

### [Results](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#results)

If you allow the `name` to autocomplete, the `name` and `email` will both have a rounded border and a magenta outline, though likely the border will not change due to the `!important` flag set in the user agent style sheet. Try editing one of the fields: note how once you edit the value, even if you reset it to it's autocompletion value, the `:autofill` styles are no longer applied.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-autofill](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-autofill) |
| [Selectors Level 4  <br>\# selectordef-autofill](https://drafts.csswg.org/selectors/#selectordef-autofill) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill#see_also)

----------------------------------------------------------------------------------------------------

*   [`<input>` pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#input_pseudo-classes)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_autofill/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_autofill (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aautofill&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_autofill%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aautofill%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_autofill%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb6de98eb9cd52ce7e37f22a340352f0af4c9d597%0A*+Document+last+modified%3A+2026-08-14T17%3A15%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")