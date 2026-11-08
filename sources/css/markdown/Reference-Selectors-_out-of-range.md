*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#mdn-search)
    

`:out-of-range` CSS pseudo-class
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:out-of-range`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element whose current value is outside the range limits specified by the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 attributes.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#try_it)

----------------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 1em;
    }
    
    input:out-of-range {
      background-color: orangered;
    }
    

    <label for="amount">How many tickets? (You can buy 2-6 tickets)</label>
    <input id="amount" name="amount" type="number" min="2" max="6" value="4" />
    
    <label for="dep">Departure Date: (Whole year 2022 is acceptable)</label>
    <input
      id="dep"
      name="dep"
      type="date"
      min="2022-01-01"
      max="2022-12-31"
      value="2025-05-05" />
    
    <label for="ret">Return Date: (Whole year 2022 is acceptable)</label>
    <input id="ret" name="ret" type="date" min="2022-01-01" max="2022-12-31" />
    

This pseudo-class is useful for giving the user a visual indication that a field's current value is outside the permitted limits.

**Note:** This pseudo-class only applies to elements that have (and can take) a range limitation. In the absence of such a limitation, the element can neither be "in-range" nor "out-of-range."

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#syntax)

----------------------------------------------------------------------------------------------------

css

    :out-of-range {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#examples)

--------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#html)

html

    <p>Values between 1 and 10 are valid.</p>
    <ul>
      <li>
        <input
          id="value1"
          name="value1"
          type="number"
          placeholder="1 to 10"
          min="1"
          max="10"
          value="12" />
        <label for="value1">Your value is </label>
      </li>
    </ul>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#css)

css

    li {
      list-style: none;
      margin-bottom: 1em;
    }
    
    input {
      border: 1px solid black;
    }
    
    input:in-range {
      background-color: rgb(0 255 0 / 25%);
    }
    
    input:out-of-range {
      background-color: rgb(255 0 0 / 25%);
      border: 2px solid red;
    }
    
    input:in-range + label::after {
      content: "okay.";
    }
    
    input:out-of-range + label::after {
      content: "out of range!";
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-out-of-range](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-out-of-range) |
| [Selectors Level 4  <br>\# out-of-range-pseudo](https://drafts.csswg.org/selectors/#out-of-range-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range#see_also)

--------------------------------------------------------------------------------------------------------

*   [`:in-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:in-range)
    
*   [Form data validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_out-of-range/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_out-of-range (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aout-of-range&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_out-of-range%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aout-of-range%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_out-of-range%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")