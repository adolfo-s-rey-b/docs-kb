*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#mdn-search)
    

`:first-of-type` CSS pseudo-class
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:first-of-type`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents the first element of its type (tag name) among a group of sibling elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#try_it)

-----------------------------------------------------------------------------------------------------

    dt {
      font-weight: bold;
    }
    
    dd {
      margin: 3px;
    }
    
    dd:first-of-type {
      border: 2px solid orange;
    }
    

    <dl>
      <dt>Vegetables:</dt>
      <dd>1. Tomatoes</dd>
      <dd>2. Cucumbers</dd>
      <dd>3. Mushrooms</dd>
      <dt>Fruits:</dt>
      <dd>4. Apples</dd>
      <dd>5. Mangos</dd>
      <dd>6. Pears</dd>
      <dd>7. Oranges</dd>
    </dl>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#syntax)

-----------------------------------------------------------------------------------------------------

css

    :first-of-type {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#examples)

---------------------------------------------------------------------------------------------------------

### [Styling the first paragraph](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#styling_the_first_paragraph)

#### HTML

html

    <h2>Heading</h2>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
    

#### CSS

css

    p:first-of-type {
      color: red;
      font-style: italic;
    }
    

#### Result

### [Nested elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#nested_elements)

This example shows how nested elements can also be targeted. Note that the [universal selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
 (`*`) is implied when no type selector is written.

#### HTML

html

    <article>
      <div>This `div` is first!</div>
      <div>This <span>nested `span` is first</span>!</div>
      <div>
        This <em>nested `em` is first</em>, but this <em>nested `em` is last</em>!
      </div>
      <div>This <span>nested `span` gets styled</span>!</div>
      <p>This `p` qualifies!</p>
      <div>This is the final `div`.</div>
    </article>
    

#### CSS

css

    article :first-of-type {
      background-color: pink;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# first-of-type-pseudo](https://drafts.csswg.org/selectors/#first-of-type-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type#see_also)

---------------------------------------------------------------------------------------------------------

*   [`:first-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child)
    , [`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
    , [`:nth-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_first-of-type/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_first-of-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afirst-of-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_first-of-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afirst-of-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_first-of-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")