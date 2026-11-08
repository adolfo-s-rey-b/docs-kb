*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#mdn-search)
    

`:nth-last-of-type()` CSS pseudo-class
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:nth-last-of-type()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches elements based on their position among siblings of the same type (tag name), counting from the end.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#try_it)

--------------------------------------------------------------------------------------------------------

    dt {
      font-weight: bold;
    }
    
    dd {
      margin: 3px;
    }
    
    dd:nth-last-of-type(3n) {
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#syntax)

--------------------------------------------------------------------------------------------------------

css

    :nth-last-of-type(<An+B> | even | odd) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#parameters)

The `:nth-last-of-type()` pseudo-class is specified with a single argument, which represents the pattern for matching elements, counting from the end.

See [`:nth-last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child)
 for a more detailed explanation of its syntax.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#examples)

------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#html)

html

    <div>
      <span>This is a span.</span>
      <span>This is another span.</span>
      <em>This is emphasized.</em>
      <span>Wow, this span gets limed!!!</span>
      <del>This is struck through.</del>
      <span>Here is one last span.</span>
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#css)

css

    span:nth-last-of-type(2) {
      background-color: lime;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# nth-last-of-type-pseudo](https://drafts.csswg.org/selectors/#nth-last-of-type-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type#see_also)

------------------------------------------------------------------------------------------------------------

*   [`:nth-last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child)
    , [`:nth-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_nth-last-of-type/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_nth-last-of-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Anth-last-of-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_nth-last-of-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Anth-last-of-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_nth-last-of-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")