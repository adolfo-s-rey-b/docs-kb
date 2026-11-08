*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#mdn-search)
    

`::file-selector-button` CSS pseudo-element
===========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::file-selector-button`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents the button of an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 of [`type="file"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#try_it)

-------------------------------------------------------------------------------------------------------------

    input {
      margin-top: 1rem;
    }
    
    input::file-selector-button {
      font-weight: bold;
      color: dodgerblue;
      padding: 0.5em;
      border: thin solid grey;
      border-radius: 3px;
    }
    

    <label for="avatar">Choose a profile picture:</label><br />
    
    <input id="avatar" type="file" name="avatar" accept="image/png, image/jpeg" />
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#syntax)

-------------------------------------------------------------------------------------------------------------

css

    ::file-selector-button {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#examples)

-----------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#basic_example)

#### HTML

html

    <form>
      <label for="fileUpload">Upload file</label>
      <input type="file" id="fileUpload" />
    </form>
    

#### CSS

    form {
      display: flex;
      gap: 1em;
      align-items: center;
    }
    

css

    input[type="file"]::file-selector-button {
      border: 2px solid #6c5ce7;
      padding: 0.2em 0.4em;
      border-radius: 0.2em;
      background-color: #a29bfe;
      transition: 1s;
    }
    
    input[type="file"]::file-selector-button:hover {
      background-color: #81ecec;
      border: 2px solid #00cec9;
    }
    

#### Result

Note that `::file-selector-button` is a whole element, and as such matches the rules from the UA stylesheet. In particular, fonts and colors won't necessarily inherit from the `input` element.

### [Fallback example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#fallback_example)

#### HTML

html

    <form>
      <label for="fileUpload">Upload file</label>
      <input type="file" id="fileUpload" />
    </form>
    

#### CSS

    form {
      display: flex;
      gap: 1em;
      align-items: center;
    }
    

css

    input[type="file"]::file-selector-button {
      border: 2px solid #6c5ce7;
      padding: 0.2em 0.4em;
      border-radius: 0.2em;
      background-color: #a29bfe;
      transition: 1s;
    }
    
    input[type="file"]::-ms-browse:hover {
      background-color: #81ecec;
      border: 2px solid #00cec9;
    }
    
    input[type="file"]::-webkit-file-upload-button:hover {
      background-color: #81ecec;
      border: 2px solid #00cec9;
    }
    
    input[type="file"]::file-selector-button:hover {
      background-color: #81ecec;
      border: 2px solid #00cec9;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4  <br>\# file-selector-button-pseudo](https://drafts.csswg.org/css-pseudo/#file-selector-button-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [WebKit CSS extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions)
    
*   [File and Directory Entries API](https://developer.mozilla.org/en-US/docs/Web/API/File_and_Directory_Entries_API)
    
*   [`<input type="file">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_file-selector-button/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_file-selector-button (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Afile-selector-button&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_file-selector-button%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Afile-selector-button%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_file-selector-button%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")