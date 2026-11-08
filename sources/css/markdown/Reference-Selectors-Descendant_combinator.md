*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#mdn-search)
    

Descendant combinator
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **descendant combinator** — typically represented by a single space (" ") character — combines two selectors such that elements matched by the second selector are selected if they have an ancestor (parent, parent's parent, parent's parent's parent, etc.) element matching the first selector. Selectors that utilize a descendant combinator are called _descendant selectors_.

css

    /* List items that are descendants of the "my-things" list */
    ul.my-things li {
      margin: 2em;
    }
    

The descendant combinator is technically one or more [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
 white space characters — the space character and/or one of four control characters: carriage return, form feed, new line, and tab characters — between two selectors in the absence of another combinator. Additionally, the white space characters of which the combinator is comprised may contain any number of CSS comments.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#syntax)

------------------------------------------------------------------------------------------------------------

css

    selector1 selector2 {
      /* property declarations */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#examples)

----------------------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#css)

css

    li {
      list-style-type: disc;
    }
    
    li li {
      list-style-type: circle;
    }
    

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#html)

html

    <ul>
      <li>
        <div>Item 1</div>
        <ul>
          <li>Subitem A</li>
          <li>Subitem B</li>
        </ul>
      </li>
      <li>
        <div>Item 2</div>
        <ul>
          <li>Subitem A</li>
          <li>Subitem B</li>
        </ul>
      </li>
    </ul>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# descendant-combinators](https://drafts.csswg.org/selectors/#descendant-combinators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Child combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/descendant_combinator/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/descendant_combinator (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FDescendant_combinator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fdescendant_combinator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FDescendant_combinator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fdescendant_combinator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc52ed787442db9d65b21f5c2874fa6bfd08a253a%0A*+Document+last+modified%3A+2025-11-03T17%3A48%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")