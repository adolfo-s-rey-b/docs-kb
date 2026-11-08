*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#mdn-search)
    

`:placeholder-shown` CSS pseudo-class
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:placeholder-shown`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents any [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element that is currently displaying [placeholder text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#try_it)

---------------------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 1em;
    }
    
    input:placeholder-shown {
      background-color: ivory;
      border: 2px solid darkorange;
      border-radius: 5px;
    }
    

    <label for="name">Full Name:</label>
    <input id="name" name="name" type="text" />
    
    <label for="email">Email Address:</label>
    <input id="email" name="email" type="email" placeholder="name@example.com" />
    
    <label for="age">Your age:</label>
    <input
      id="age"
      name="age"
      type="number"
      value="18"
      placeholder="You must be 18+" />
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#syntax)

---------------------------------------------------------------------------------------------------------

css

    :placeholder-shown {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#examples)

-------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#basic_example)

This example applies special font and border styles when the placeholder is shown.

#### HTML

html

    <input placeholder="Type something here!" />
    

#### CSS

css

    input {
      border: 1px solid black;
      padding: 3px;
    }
    
    input:placeholder-shown {
      border-color: teal;
      color: purple;
      font-style: italic;
    }
    

#### Result

### [Overflowing text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#overflowing_text)

When form fields are too small, placeholder text can get cropped in an undesirable way. You can use the [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
 property to alter the way overflowing text is displayed.

#### HTML

html

    <input id="input1" placeholder="Name, Rank, and Serial Number" /> <br /><br />
    <input id="input2" placeholder="Name, Rank, and Serial Number" />
    

#### CSS

css

    #input2:placeholder-shown {
      text-overflow: ellipsis;
    }
    

#### Result

### [Customized input field](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#customized_input_field)

The following example highlights the Student ID field with a custom style.

#### HTML

html

    <p>
      <label for="name">Student Name:</label>
      <input id="name" placeholder="Student Name" />
    </p>
    <p>
      <label for="branch">Student Branch:</label>
      <input id="branch" placeholder="Student Branch" />
    </p>
    <p>
      <label for="sid">8-Digit Student ID:</label>
      <input
        pattern="[0-9]{8}"
        id="sid"
        class="student-id"
        placeholder="8 digit id" />
    </p>
    

#### CSS

css

    input {
      background-color: #e8e8e8;
      color: black;
    }
    
    input.student-id:placeholder-shown {
      background-color: yellow;
      color: red;
      font-style: italic;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-placeholder-shown](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-placeholder-shown) |
| [Selectors Level 4  <br>\# placeholder-shown-pseudo](https://drafts.csswg.org/selectors/#placeholder-shown-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown#see_also)

-------------------------------------------------------------------------------------------------------------

*   The [`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
     pseudo-element styles the placeholder _itself_.
*   Related HTML elements: [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    , [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    
*   [HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_placeholder-shown/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_placeholder-shown (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aplaceholder-shown&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_placeholder-shown%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aplaceholder-shown%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_placeholder-shown%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")