*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#mdn-search)
    

`:visited` CSS pseudo-class
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:visited`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 applies once the link has been visited by the user. For privacy reasons, the styles that can be modified using this selector are very limited. The `:visited` pseudo-class applies only to [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 elements that have an `href` attribute.

Styles defined by the `:visited` and unvisited [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
 pseudo-classes can be overridden by any subsequent user-action pseudo-classes ([`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
 or [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
) that have at least equal specificity. To style links appropriately, put the `:visited` rule after the `:link` rule but before the `:hover` and `:active` rules, as defined by the _LVHA-order_: `:link` — `:visited` — `:hover` — `:active`. The `:visited` pseudo-class and `:link` pseudo-class are mutually exclusive.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#try_it)

-----------------------------------------------------------------------------------------------

    p {
      font-weight: bold;
    }
    
    a:visited {
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
        <a href="https://developer.mozilla.org/missing-1">Random MDN page</a>
      </li>
      <li>
        <a href="https://example.com/missing-1">Random Example page</a>
      </li>
    </ul>
    

[Privacy restrictions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#privacy_restrictions)

---------------------------------------------------------------------------------------------------------------------------

For privacy reasons, browsers strictly limit which styles you can apply using this pseudo-class, and how they can be used:

*   Allowable CSS properties are [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    , [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    , [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
    , [`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color)
    , [`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color)
    , [`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
    , [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    , [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    , [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    , and [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    .
*   Allowable SVG attributes are [`fill`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill)
     and [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
    .
*   The alpha component of the allowed styles will be ignored. The alpha component of the element's non-`:visited` state will be used instead. In Firefox when the alpha component is `0`, the style set in `:visited` will be ignored entirely.
*   Although these styles can change the appearance of colors to the end user, the [`window.getComputedStyle`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle)
     method will lie and always return the value of the non-`:visited` color.
*   The [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
     element is never matched by `:visited`.
*   DOM methods that match elements via CSS selectors — such as [`querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
     and [`querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)
     — will always return an "empty" result even if there are visited links in a document. For the aforementioned methods, this will be `null` or an empty [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)
    , respectively.

**Note:** For more information on these limitations and the reasons behind them, see [Privacy and the :visited selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#syntax)

-----------------------------------------------------------------------------------------------

css

    :visited {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#examples)

---------------------------------------------------------------------------------------------------

Properties that would otherwise have no color or be transparent cannot be modified with `:visited`. Of the properties that can be set with this pseudo-class, your browser probably has a default value for `color` and `column-rule-color` only. Thus, if you want to modify the other properties, you'll need to give them a base value outside the `:visited` selector.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#html)

html

    <a href="#test-visited-link">Have you visited this link yet?</a><br />
    <a href="">You've already visited this link.</a>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#css)

css

    a {
      /* Specify non-transparent defaults to certain properties,
         allowing them to be styled with the :visited state */
      background-color: white;
      border: 1px solid white;
    }
    
    a:visited {
      background-color: yellow;
      border-color: hotpink;
      color: hotpink;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-visited](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-visited) |
| [Selectors Level 4  <br>\# visited-pseudo](https://drafts.csswg.org/selectors/#visited-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited#see_also)

---------------------------------------------------------------------------------------------------

*   [Privacy and the :visited selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited)
    
*   Link-related pseudo-classes: [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
    , [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
    , [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_visited/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_visited (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Avisited&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_visited%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Avisited%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_visited%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")