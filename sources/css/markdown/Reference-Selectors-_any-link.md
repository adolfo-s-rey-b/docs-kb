*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#mdn-search)
    

`:any-link` CSS pseudo-class
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:any-link`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selector represents an element that acts as the source anchor of a hyperlink, independent of whether it has been visited. In other words, it matches every [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 or [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 element that has an `href` attribute. Thus, it matches all elements that match [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
 or [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#try_it)

------------------------------------------------------------------------------------------------

    p {
      font-weight: bold;
    }
    
    a:any-link {
      color: forestgreen;
      text-decoration-color: hotpink;
    }
    

    <p>Pages that you might have visited:</p>
    <ul>
      <li>
        <a href="https://developer.mozilla.org">MDN Web Docs</a>
      </li>
      <li>
        <a href="https://www.youtube.com/YouTube">Google</a>
      </li>
    </ul>
    <p>Pages unlikely to be in your history:</p>
    <ul>
      <li>
        <a href="https://developer.mozilla.org/missing-3">Random MDN page</a>
      </li>
      <li>
        <a href="https://example.com/missing-3">Random Example page</a>
      </li>
    </ul>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#syntax)

------------------------------------------------------------------------------------------------

css

    :any-link {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#examples)

----------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#html)

html

    <a href="https://example.com">External link</a><br />
    <a href="#">Internal target link</a><br />
    <a>Placeholder link (won't get styled)</a>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#css)

css

    a:any-link {
      border: 1px solid blue;
      color: orange;
    }
    
    /* WebKit browsers */
    a:-webkit-any-link {
      border: 1px solid blue;
      color: orange;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# the-any-link-pseudo](https://drafts.csswg.org/selectors/#the-any-link-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link#see_also)

----------------------------------------------------------------------------------------------------

*   [Creating links](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Creating_links)
    
*   Matches HTML elements: [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
     and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
     with an [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
     attribute
*   Related CSS selectors:
    *   [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
        
    *   [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_any-link/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_any-link (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aany-link&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_any-link%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aany-link%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_any-link%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")