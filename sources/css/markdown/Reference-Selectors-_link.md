*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#mdn-search)
    

`:link` CSS pseudo-class
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:link`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents an element that has not yet been visited. It matches every unvisited [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 or [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 element that has an `href` attribute.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#try_it)

--------------------------------------------------------------------------------------------

    p {
      font-weight: bold;
    }
    
    a:link {
      color: forestgreen;
      text-decoration-color: hotpink;
    }
    

    <p>Pages that you might have visited:</p>
    <ul>
      <li>
        <a href="https://developer.mozilla.org">MDN Web Docs</a>
      </li>
      <li>
        <a href="https://www.youtube.com/">YouTube</a>
      </li>
    </ul>
    <p>Pages unlikely to be in your history:</p>
    <ul>
      <li>
        <a href="https://developer.mozilla.org/missing-2">Random MDN page</a>
      </li>
      <li>
        <a href="https://example.com/missing-2">Random Example page</a>
      </li>
    </ul>
    

Styles defined by the `:link` and [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
 pseudo-classes can be overridden by any subsequent user-action pseudo-classes ([`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
 or [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
) that have at least equal specificity. To style links appropriately, put the `:link` rule before all other link-related rules, as defined by the _LVHA-order_: `:link` — `:visited` — `:hover` — `:active`. The `:visited` pseudo-class and `:link` pseudo-class are mutually exclusive.

**Note:** Use [`:any-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link)
 to select an element independent of whether it has been visited or not.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#syntax)

--------------------------------------------------------------------------------------------

css

    :link {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#examples)

------------------------------------------------------------------------------------------------

By default, most browsers apply a special [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 value to visited links. Thus, the links in this example will probably have special font colors only before you visit them. (After that, you'll need to clear your browser history to see them again.) However, the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 values are likely to remain, as most browsers do not set that property on visited links by default.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#html)

html

    <a href="#ordinary-target">This is an ordinary link.</a><br />
    <a href="">You've already visited this link.</a><br />
    <a>Placeholder link (won't get styled)</a>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#css)

css

    a:link {
      background-color: gold;
      color: green;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-link](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-link) |
| [Selectors Level 4  <br>\# link-pseudo](https://drafts.csswg.org/selectors/#link-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link#see_also)

------------------------------------------------------------------------------------------------

*   Link-related pseudo-classes: [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
    , [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
    , [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_link/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_link (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Alink&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_link%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Alink%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_link%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")