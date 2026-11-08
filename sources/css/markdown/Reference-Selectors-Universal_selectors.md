*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#mdn-search)
    

Universal selectors
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The CSS **universal selector** (`*`) matches elements of any type.

The universal selector is a special [type selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
 and can therefore be namespaced when using [`@namespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)
. This is useful when dealing with documents containing multiple namespaces such as HTML with inline SVG or MathML, or XML that mixes multiple vocabularies.

*   `ns|*` - matches all elements in namespace _ns_
*   `*|*` - matches all elements
*   `|*` - matches all elements without any declared namespace

**Note:** The universal selector (`*`) matches **elements only**. It does **not** directly match pseudo-elements by itself.

To match all [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 pseudo-elements on a page, for example, you would have to use a selector like `*::before`. This works because the `*` matches all elements, and the `::before` pseudo-element is available on all elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#syntax)

----------------------------------------------------------------------------------------------------------

The asterisk is optional with simple selectors. For instance, `*.warning` and `.warning` are equivalent.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#examples)

--------------------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#css)

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#html)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#result)

### [Namespaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#namespaces)

In this example the selector will only match elements in the example namespace.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# the-universal-selector](https://drafts.csswg.org/selectors/#the-universal-selector) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors#see_also)

--------------------------------------------------------------------------------------------------------------

*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module
*   [Learn CSS: Basic selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 17, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/universal_selectors/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/universal_selectors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FUniversal_selectors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Funiversal_selectors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FUniversal_selectors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Funiversal_selectors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca0d81a57fd36cf5da9621c44171d0f333f3f3e1%0A*+Document+last+modified%3A+2025-11-17T17%3A34%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")