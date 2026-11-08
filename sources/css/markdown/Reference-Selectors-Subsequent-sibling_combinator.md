*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#mdn-search)
    

Subsequent-sibling combinator
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **subsequent-sibling combinator** (`~`, a tilde) separates two selectors and matches _all instances_ of the second element that follow the first element (not necessarily immediately) and share the same parent element.

In the following example, the subsequent-sibling combinator (`~`) helps to select and style paragraphs that are both siblings of an image and appear after any image.

css

    img ~ p {
      color: red;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#syntax)

--------------------------------------------------------------------------------------------------------------------

css

    /* The white space around the ~ combinator is optional but recommended. */
    former_element ~ target_element { style properties }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#examples)

------------------------------------------------------------------------------------------------------------------------

### [Using the combinator with simple selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#using_the_combinator_with_simple_selectors)

This example shows the use of the `~` combinator when both the selectors are simple selectors (`p` and `span`).

html

    <article>
      <span>This is not red because it appears before any paragraph.</span>
      <p>Here is a paragraph.</p>
      <code>Here is some code.</code>
      <span>
        This span is red because it appears after the paragraph, even though there
        are other nodes in between.
      </span>
      <p>Whatever it may be, keep smiling.</p>
      <h1>Dream big</h1>
      <span>
        Doesn't matter how many or what kind of nodes are in between, all spans from
        the same parent after a paragraph are red.
      </span>
    </article>
    <span>
      This span is not red because it doesn't share a parent with a paragraph.
    </span>
    

css

    p ~ span {
      color: red;
    }
    

### [Using the combinator with complex selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#using_the_combinator_with_complex_selectors)

This example contains two [complex selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#complex_selector)
, both using the subsequent-sibling combinator: `.foo p ~ span` and `.foo p ~ .foo span`.

*   The first complex selector, `.foo p ~ span`, matches all spans that come after a paragraph _if_ the span and paragraph share the same parent **and** that parent or an ancestor of that parent has the class `.foo`.
*   The second complex selector, `.foo p ~ .foo span`, matches all spans that are a descendant of the element with class `.foo` _if_ that element is a sibling of the previously mentioned paragraph.

The example below shows that the target element in the complex selector must share the same parent as the initial element in the complex selector.

html

    <h1>Dream big</h1>
    <span>And yet again this is a red span!</span>
    <div class="foo">
      <p>Here is another paragraph.</p>
      <span>A blue span</span>
      <div class="foo">
        <span>A green span</span>
      </div>
    </div>
    

css

    .foo p ~ span {
      color: blue;
    }
    
    .foo p ~ .foo span {
      color: green;
    }
    

In the above HTML, the two siblings of `.foo p` are `span` and `.foo`. The green `span` is a descendant of the `.foo` class, which is a sibling of `p`.

*   When the target selector is `span`, the `span` element that is a sibling of `p` is selected. The `p` element is a descendant of `.foo`, so are its `span` siblings.
*   In `.foo p ~ .foo span`, the target selector is `span` that is a descendant of `.foo`. In this case, the `span` element that's a descendant of `.foo` is selected if that `.foo` is a sibling of `p`; essentially, both are nested in an ancestor of `.foo`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#specifications)

------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# general-sibling-combinators](https://drafts.csswg.org/selectors/#general-sibling-combinators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator#see_also)

------------------------------------------------------------------------------------------------------------------------

*   [Next-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/subsequent-sibling_combinator/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/subsequent-sibling_combinator (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FSubsequent-sibling_combinator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fsubsequent-sibling_combinator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FSubsequent-sibling_combinator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fsubsequent-sibling_combinator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")