*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#mdn-search)
    

`autocapitalize` HTML global attribute
======================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/66)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`autocapitalize`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute that controls whether inputted text is automatically capitalized and, if so, in what manner. This is relevant to:

*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
     elements.
*   Any element with [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     set on it.

`autocapitalize` doesn't affect behavior when typing on a physical keyboard. It affects the behavior of other input mechanisms such as virtual keyboards on mobile devices and voice input. This can assist users by making data entry quicker and easier, for example by automatically capitalizing the first letter of each sentence.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#value)

------------------------------------------------------------------------------------------------------------

Possible values are:

[`none` or `off`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#none)

Do not automatically capitalize any text.

[`sentences` or `on`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#sentences)

Automatically capitalize the first character of each sentence.

[`words`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#words)

Automatically capitalize the first character of each word.

[`characters`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#characters)

Automatically capitalize every character.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#usage_notes)

------------------------------------------------------------------------------------------------------------------------

*   `autocapitalize` can be set on `<input>` and `<textarea>` elements, _and_ on their containing [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
     elements. When `autocapitalize` is set on a `<form>` element, it sets the autocapitalize behavior for all contained `<input>`s and `<textarea>`s, overriding any `autocapitalize` values set on contained elements.
*   `autocapitalize` has no effect on the `url`, `email`, or `password` `<input>` types, where autocapitalization is never enabled.
*   Where `autocapitalize` is not specified, the adopted default behavior varies between browsers. For example:
    *   Chrome and Safari default to `on`/`sentences`
    *   Firefox defaults to `off`/`none`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#examples)

------------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#html)

html

    <p>Form to test different autocapitalize settings:</p>
    
    <form>
      <div>
        <label for="default">Default: no autocapitalize set</label>
        <input type="text" id="default" name="default" />
      </div>
      <div>
        <label for="off">autocapitalize="off"</label>
        <input type="text" id="off" name="off" autocapitalize="off" />
      </div>
      <div>
        <label for="none">autocapitalize="none"</label>
        <input type="text" id="none" name="none" autocapitalize="none" />
      </div>
      <div>
        <label for="on">autocapitalize="on"</label>
        <input type="text" id="on" name="on" autocapitalize="on" />
      </div>
      <div>
        <label for="sentences">autocapitalize="sentences"</label>
        <input
          type="text"
          id="sentences"
          name="sentences"
          autocapitalize="sentences" />
      </div>
      <div>
        <label for="words">autocapitalize="words"</label>
        <input type="text" id="words" name="words" autocapitalize="words" />
      </div>
      <div>
        <label for="characters">autocapitalize="characters"</label>
        <input
          type="text"
          id="characters"
          name="characters"
          autocapitalize="characters" />
      </div>
      <div>
        <label for="characters-ta">autocapitalize="characters" on textarea</label>
        <textarea
          type="text"
          id="characters-ta"
          name="characters-ta"
          autocapitalize="characters">
        </textarea>
      </div>
    </form>
    
    <hr />
    
    <p contenteditable autocapitalize="characters">
      This content is editable and has autocapitalize="characters" set on it
    </p>
    

    div {
      margin-bottom: 20px;
    }
    

[Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#result)

--------------------------------------------------------------------------------------------------------------

Test the effect on each input using a virtual keyboard or voice entry (keyboard entry will not work).

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-autocapitalize](https://html.spec.whatwg.org/multipage/interaction.html#attr-autocapitalize) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/autocapitalize/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/autocapitalize (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fautocapitalize&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fautocapitalize%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fautocapitalize%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fautocapitalize%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")