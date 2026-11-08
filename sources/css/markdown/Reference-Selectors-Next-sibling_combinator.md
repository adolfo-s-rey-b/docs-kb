*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#mdn-search)
    

Next-sibling combinator
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **next-sibling combinator** (`+`) separates two selectors and matches the second element only if it _immediately_ follows the first element, and both are children of the same parent [`element`](https://developer.mozilla.org/en-US/docs/Web/API/Element)
.

css

    /* Paragraphs that come immediately after any image */
    img + p {
      font-weight: bold;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#syntax)

--------------------------------------------------------------------------------------------------------------

css

    /* The white space around the + combinator is optional but recommended. */
    former_element + target_element { style properties }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#examples)

------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#basic_usage)

This example demonstrates how to select the next sibling if that next sibling is of a specific type.

#### CSS

We only style the `<li>` that comes immediately after an `<li>` that is the first of its type:

css

    li:first-of-type + li {
      color: red;
      font-weight: bold;
    }
    

#### HTML

html

    <ul>
      <li>One</li>
      <li>Two!</li>
      <li>Three</li>
    </ul>
    

#### Result

### [Selecting a previous sibling](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#selecting_a_previous_sibling)

The next-sibling combinator can be included within the [`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
 functional selector to select the previous sibling.

#### CSS

We only style the `<li>` with a next sibling that is an `<li>` that is the last of its type:

css

    li:has(+ li:last-of-type) {
      color: red;
      font-weight: bold;
    }
    

#### HTML

html

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three!</li>
      <li>Four</li>
    </ul>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# adjacent-sibling-combinators](https://drafts.csswg.org/selectors/#adjacent-sibling-combinators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Subsequent-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/next-sibling_combinator/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/next-sibling_combinator (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FNext-sibling_combinator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fnext-sibling_combinator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FNext-sibling_combinator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fnext-sibling_combinator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")