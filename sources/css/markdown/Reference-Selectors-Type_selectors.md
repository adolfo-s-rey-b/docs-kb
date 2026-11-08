*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#mdn-search)
    

Type selectors
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The CSS **type selector** matches elements by node name. In other words, it selects all elements of the given type within a document.

Type selectors can be namespaced when using [`@namespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)
. This is useful when dealing with documents containing multiple namespaces such as HTML with inline SVG or MathML, or XML that mixes multiple vocabularies.

*   `ns|h1` - matches `<h1>` elements in namespace _ns_
*   `*|h1` - matches all `<h1>` elements
*   `|h1` - matches all `<h1>` elements without any declared namespace

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#syntax)

-----------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#examples)

---------------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#css)

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#html)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#result)

### [Namespaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#namespaces)

In this example the selector will only match `<h1>` elements in the example namespace.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# type-selectors](https://drafts.csswg.org/selectors/#type-selectors) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors#see_also)

---------------------------------------------------------------------------------------------------------

*   [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
    
*   [Learn CSS: Basic selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/type_selectors/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/type_selectors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FType_selectors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Ftype_selectors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FType_selectors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Ftype_selectors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")