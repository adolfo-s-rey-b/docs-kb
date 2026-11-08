*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint#mdn-search)
    

`enterkeyhint` HTML global attribute
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`enterkeyhint`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute defining what action label (or icon) to present for the enter key on virtual keyboards.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint#try_it)

------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint#description)

----------------------------------------------------------------------------------------------------------------------

[Form controls](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
 (such as [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 or [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements) or elements using [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 can specify an [`inputmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode)
 attribute to control what kind of virtual keyboard will be used. To further improve the user's experience, the enter key can be customized specifically by providing an `enterkeyhint` attribute indicating how the enter key should be labeled (or which icon should be shown). The enter key usually represents what the user should do next; typical actions are: sending text, inserting a new line, or searching.

If no `enterkeyhint` attribute is provided, the user agent might use contextual information from the [`inputmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode)
, [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#input_types)
, or [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attributes to display a suitable enter key label (or icon).

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint#value)

----------------------------------------------------------------------------------------------------------

The `enterkeyhint` attribute is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute and only accepts the following values:

| Value | Description | Example label (depends on user agent and user language) |
| --- | --- | --- |
| `enterkeyhint="enter"` | Typically inserting a new line. | return, ↵ |
| `enterkeyhint="done"` | Typically meaning there is nothing more to input and the input method editor (IME) will be closed. | done, ✅ |
| `enterkeyhint="go"` | Typically meaning to take the user to the target of the text they typed. | go, 🡢 |
| `enterkeyhint="next"` | Typically taking the user to the next field that will accept text. | next, ⇥ |
| `enterkeyhint="previous"` | Typically taking the user to the previous field that will accept text. | return, ⇤ |
| `enterkeyhint="search"` | Typically taking the user to the results of searching for the text they have typed. | search, 🔍 |
| `enterkeyhint="send"` | Typically delivering the text to its target. | send |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-enterkeyhint](https://html.spec.whatwg.org/multipage/interaction.html#attr-enterkeyhint) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`HTMLElement.enterKeyHint`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/enterKeyHint)
     property reflecting this attribute
*   [`inputmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode)
     global attribute
*   [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     global attribute
*   [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#input_types)
     and [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
     attributes on [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     elements

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/enterkeyhint/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/enterkeyhint (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fenterkeyhint&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fenterkeyhint%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fenterkeyhint%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fenterkeyhint%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")