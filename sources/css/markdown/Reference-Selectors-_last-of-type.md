*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#mdn-search)
    

`:last-of-type` CSS pseudo-class
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:last-of-type`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents the last element of its type (tag name) among a group of sibling elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#try_it)

----------------------------------------------------------------------------------------------------

    dt {
      font-weight: bold;
    }
    
    dd {
      margin: 3px;
    }
    
    dd:last-of-type {
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#syntax)

----------------------------------------------------------------------------------------------------

css

    :last-of-type {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#examples)

--------------------------------------------------------------------------------------------------------

### [Styling the last paragraph](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#styling_the_last_paragraph)

#### HTML

html

    <h2>Heading</h2>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
    

#### CSS

css

    p:last-of-type {
      color: red;
      font-style: italic;
    }
    

#### Result

### [Nested elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#nested_elements)

This example shows how nested elements can also be targeted. Note that the [universal selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
 (`*`) is implied when no simple selector is written.

#### HTML

html

    <article>
      <div>This `div` is first.</div>
      <div>This <span>nested `span` is last</span>!</div>
      <div>
        This <em>nested `em` is first</em>, but this <em>nested `em` is last</em>!
      </div>
      <p>This `p` qualifies!</p>
      <div>This is the final `div`!</div>
    </article>
    

#### CSS

css

    article :last-of-type {
      background-color: pink;
    }
    

#### Result

### [Multiple selectors elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#multiple_selectors_elements)

This HTML example contains nested elements of different types. The CSS contains both type selectors and class selectors.

#### HTML

html

    <p>This `p` is not selected.</p>
    <p>This `p` is not selected either.</p>
    <p>
      This `p` is last `p` element of its parent e.g. `body` selected by `p` type
      selector.
    </p>
    <div class="container">
      <div class="item">This `div` is not selected.</div>
      <div class="item">This `div` is not selected either.</div>
      <div class="item">
        This `div` is last `div` element of its parent `div` selected by `.container
        .item` class selector.
      </div>
      <p class="item">
        This `p` is last `p` element of its parent `div` selected by `.container
        .item` class selector.
      </p>
    </div>
    

#### CSS

css

    p:last-of-type {
      background: skyblue;
    }
    
    .container .item:last-of-type {
      color: red;
      font-weight: bold;
    }
    

#### Result

The last `<div>` and the last `<p>` are both red and bold as the `.item:last-of-type` selects the last of every type if that last element also has the `item` class.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# last-of-type-pseudo](https://drafts.csswg.org/selectors/#last-of-type-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type#see_also)

--------------------------------------------------------------------------------------------------------

*   [`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
    , [`:nth-last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_last-of-type/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_last-of-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Alast-of-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_last-of-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Alast-of-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_last-of-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")