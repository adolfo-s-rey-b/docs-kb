*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#mdn-search)
    

Child combinator
================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **child combinator** (`>`) is placed between two CSS selectors. It matches only those elements matched by the second selector that are the direct children of elements matched by the first.

css

    /* List items that are children of the "my-things" list */
    ul.my-things > li {
      margin: 2em;
    }
    

Elements matched by the second selector must be the immediate children of the elements matched by the first selector. This is stricter than the [descendant combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator)
, which matches all elements matched by the second selector for which there exists an ancestor element matched by the first selector, regardless of the number of "hops" up the DOM.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* The white space around the > combinator is optional but recommended. */
    selector1 > selector2 { /* style properties */ }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#examples)

-----------------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#css)

css

    span {
      background-color: aqua;
    }
    
    div > span {
      background-color: yellow;
    }
    

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#html)

html

    <div>
      <span>
        Span #1, in the div.
        <span>Span #2, in the span that's in the div.</span>
      </span>
    </div>
    <span>Span #3, not in the div at all.</span>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# child-combinators](https://drafts.csswg.org/selectors/#child-combinators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Descendant combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/child_combinator/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/child_combinator (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FChild_combinator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fchild_combinator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FChild_combinator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fchild_combinator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc52ed787442db9d65b21f5c2874fa6bfd08a253a%0A*+Document+last+modified%3A+2025-11-03T17%3A48%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")