*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#mdn-search)
    

CSS shadow parts
================

The **CSS shadow parts** module defines the [`::part()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
 pseudo-element that can be set on a [shadow host](https://developer.mozilla.org/en-US/docs/Glossary/Shadow_tree)
. Using this pseudo-element, you can enable shadow hosts to expose the selected element in the shadow tree to the outside page for styling purposes.

By default, elements in a shadow tree can be styled only within their respective shadow roots. The CSS shadow parts module enables including a [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
 attribute on [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
 descendants that make up the custom element, exposing the shadow tree node to external styling via the `::part()` pseudo-element.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#reference)

--------------------------------------------------------------------------------------------

### [Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#selectors)

*   [`::part()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
    

### [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#html_attributes)

*   [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
    
*   [`exportparts`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts)
    

### [Definitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#definitions)

*   [Shadow tree](https://developer.mozilla.org/en-US/docs/Glossary/Shadow_tree)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#guides)

--------------------------------------------------------------------------------------

[CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)

Alphabetical list of pseudo-elements defined by all the CSS specifications and WebVTT

[Web components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)

Overview of the different APIs that enable creating reusable custom elements or web components.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#related_concepts)

----------------------------------------------------------------------------------------------------------

*   HTML [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
     element
*   HTML [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
     element
*   [`Element.part`](https://developer.mozilla.org/en-US/docs/Web/API/Element/part)
     property
*   [`Element.shadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/Element/shadowRoot)
     property
*   [`Element.attachShadow()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow)
     method
*   [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
     interface
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
     module
    *   [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
        
    *   [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
        
    *   [`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
        
    *   [`::slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
        

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#specifications)

------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Unknown specification](https://drafts.csswg.org/css-shadow-parts/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts#see_also)

------------------------------------------------------------------------------------------

*   [CSS pseudo elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
     module
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module
*   [Using shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
    
*   [Templates: Styling outside of the current scope](https://web.dev/learn/html/template/#styling_outside_of_the_current_scope "External link (opens in new tab)")
     on web.dev (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/shadow_parts/index.md?plain=1 "Folder: en-us/web/css/guides/shadow_parts (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FShadow_parts&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fshadow_parts%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FShadow_parts%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fshadow_parts%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")