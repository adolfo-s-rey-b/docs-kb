*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#mdn-search)
    

`inputmode` HTML global attribute
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`inputmode`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute that hints at the type of data that might be entered by the user while editing the element or its contents. This allows a browser to display an appropriate virtual keyboard.

It is used primarily on [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, but is usable on any element in [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 mode.

It's important to understand that the `inputmode` attribute doesn't cause any validity requirements to be enforced on input. To require that input conforms to a particular data type, choose an appropriate [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#input_types)
 element type. For specific guidance on choosing [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 types, see the [Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#value)
 section.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#value)

-------------------------------------------------------------------------------------------------------

The attribute can have any of the following values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#none)

No virtual keyboard. For when the page implements its own keyboard input control.

[`text` (default value)](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#text)

Standard input keyboard for the user's current locale.

[`decimal`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#decimal)

Fractional numeric input keyboard containing the digits and decimal separator for the user's locale (typically . or ,). Devices may or may not show a minus key (\-).

[`numeric`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#numeric)

Numeric input keyboard, but only requires the digits 0–9. Devices may or may not show a minus key.

[`tel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#tel)

A telephone keypad input, including the digits 0–9, the asterisk (\*), and the pound (#) key. Inputs that _require_ a telephone number should typically use `[<input type="tel">](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel) ` instead.

[`search`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#search)

A virtual keyboard optimized for search input. For instance, the [return/submit key](https://html.spec.whatwg.org/multipage/interaction.html#input-modalities:-the-enterkeyhint-attribute "External link (opens in new tab)")
 may be labeled "Search", along with possible other optimizations. Inputs that _require_ a search query should typically use `[<input type="search">](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search) ` instead.

[`email`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#email)

A virtual keyboard optimized for entering email addresses. Typically includes the @character as well as other optimizations. Inputs that _require_ email addresses should typically use `[<input type="email">](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email) ` instead.

[`url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#url)

A keypad optimized for entering URLs. This may have the / key more prominent, for example. Enhanced features could include history access and so on. Inputs that _require_ a URL should typically use `[<input type="url">](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url) ` instead.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-inputmode](https://html.spec.whatwg.org/multipage/interaction.html#attr-inputmode) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode#see_also)

-------------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   [`enterkeyhint`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint)
     global attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/inputmode/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/inputmode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Finputmode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Finputmode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Finputmode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Finputmode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")