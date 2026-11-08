*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping#mdn-search)
    

CSS scoping
===========

The **CSS scoping** module defines the CSS scoping and encapsulation mechanisms, focusing on the [Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
 [scoping](https://css.oddbird.net/scope/ "External link (opens in new tab)")
 mechanism.

CSS styles are either global in scope or scoped to a [shadow tree](https://developer.mozilla.org/en-US/docs/Glossary/Shadow_tree)
. Globally scoped styles apply to all the elements in the node tree that match the selector, including custom elements in that tree, but not to the shadow trees composing each custom element. Selectors and their associated style definitions don't bleed between scopes.

Within the CSS of a shadow tree, selectors don't select elements outside the tree, either in the global scope or in other shadow trees. Each custom element has its own shadow tree, which contains all the components that make up the custom element (but not the custom element, or "host", itself).

Sometimes it's useful to be able to style a host from inside the shadow tree context. The CSS scoping module makes this possible by defining selectors that:

*   Enable a shadow tree to style its host.
*   Enable external CSS to style elements within a shadow DOM (but only if the associated custom element is set up to accept external styles).

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping#reference)

---------------------------------------------------------------------------------------

### [Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping#selectors)

*   [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
    
*   [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
    
*   [`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
    
*   [`::slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping#guides)

---------------------------------------------------------------------------------

[Web components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)

An introduction to the different technologies used to create reusable web components — custom elements whose functionality is encapsulated away from the rest of your code.

[Using shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)

Shadow DOM fundamentals, including attaching a shadow DOM to an element, adding to the shadow DOM tree, and styling.

[Using templates and slots](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_templates_and_slots)

Defining reusable HTML structure using [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
 and [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
 elements, and using that structure inside web components.

[Using custom elements](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements)

Introduction to the Custom Elements API, the JavaScript API used to create custom elements that encapsulate functionality.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping#related_concepts)

-----------------------------------------------------------------------------------------------------

*   CSS [`:defined`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined)
     pseudo-class
    
*   CSS [`::part`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
     pseudo-element
    
*   HTML [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
     element
    
*   HTML [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
     element
    
*   HTML [`slot`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/slot)
     attribute
    
*   [Shadow tree](https://developer.mozilla.org/en-US/docs/Glossary/Shadow_tree)
     glossary term
    
*   [DOM](https://developer.mozilla.org/en-US/docs/Glossary/DOM)
     glossary term
    
*   [Compound selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#compound_selector)
     term
    
*   [Selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list)
     term
    
*   [Web components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)
     interfaces, properties, and methods
    
    *   [`CustomElementRegistry`](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry)
         interface
    *   [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element)
         API
        *   [`Element.slot`](https://developer.mozilla.org/en-US/docs/Web/API/Element/slot)
             property
        *   [`Element.assignedSlot`](https://developer.mozilla.org/en-US/docs/Web/API/Element/assignedSlot)
             property
        *   [`Element.attachShadow()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow)
             method
    *   [`HTMLSlotElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSlotElement)
         interface
    *   [`HTMLTemplateElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement)
         interface
    *   [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
         interface

**Note:** Despite the name, the [`:scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope)
 pseudo-class, which represents elements that are a reference point (or scope) for selectors to match against, is defined in the [Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
 module. It is otherwise unrelated to the CSS scoping module, which is focused on scoping as it pertains to the Shadow DOM scoping mechanism.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping#specifications)

-------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scope](https://drafts.csswg.org/css-scoping/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping#see_also)

-------------------------------------------------------------------------------------

*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module
*   [CSS pseudo elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
     module
*   [CSS namespaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Namespaces)
     module
*   [CSS shadow-parts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts)
     module
*   [Template, slot, and shadow](https://web.dev/learn/html/template/ "External link (opens in new tab)")
     on web.dev (2023)
*   [Custom element best practices](https://web.dev/articles/custom-elements-best-practices "External link (opens in new tab)")
     on web.dev (2019)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/scoping/index.md?plain=1 "Folder: en-us/web/css/guides/scoping (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScoping&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fscoping%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScoping%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fscoping%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")