*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#mdn-search)
    

`:host-context()` CSS pseudo-class
==================================

Deprecated

Avoid using this feature in new projects. The CSS Working Group removed `:host-context()` from the specification, due to opposition from vendors, performance considerations, and interest in alternatives. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [Container style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container_style_queries "Container style queries with the @container at-rule apply styles to an element based on the values of custom properties of its container.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:host-context()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 allows you to style elements within a [shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
 differently based on the selector of the shadow host (the element that has the shadow root) and its DOM ancestors.

Normally, elements within a shadow DOM are isolated from the DOM outside of it. The `:host-context()` allows you to "peek outside" of this Shadow DOM and check if any of the element's ancestor elements match a certain CSS selector. For example, applying a different text color to elements within a shadow root when a `.dark-theme` class is applied to `<body>`.

Think of it like this: Imagine you have a `<greenhouse>` custom element, that has a `<chameleon>` living inside. Here, the `<greenhouse>` is the Shadow DOM host and the `<chameleon>` element is within the Shadow DOM. The `:host-context()` lets the `<chameleon>` change its appearance based on the `<greenhouse>`'s environment. If the `<greenhouse>` is in a sunny location (has a "sunny-theme" class), the `<chameleon>` turns yellow. If the `<greenhouse>` is in a shady spot (a "shady-theme" class applied instead), the `<chameleon>` turns blue.

This selector pierces through all shadow boundaries. It will look for the sunny or shady theme applied directly to the `<greenhouse>` or on any of the host's ancestors and ancestor DOMs all the way up until it reaches the document root.

To limit the selector to only the `<greenhouse>` host directly or limit the selection to host's DOM, use the [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
 or [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
 pseudo-class instead.

**Note:** This has no effect when used outside a shadow DOM.

The [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
 of `:host-context()` is that of a [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
, plus the specificity of the selector passed as the function's argument.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#try_it)

----------------------------------------------------------------------------------------------------

    /* Following CSS is being applied inside the shadow DOM. */
    
    :host-context(.container) {
      border: 5px dashed green;
    }
    
    :host-context(h1) {
      color: red;
    }
    

    <!-- elements outside shadow dom -->
    <div class="container">
      <h1 id="shadow-dom-host"></h1>
    </div>
    

    const shadowDom = init();
    
    // add a <span> element in the shadow DOM
    const span = document.createElement("span");
    span.textContent = "Inside shadow DOM";
    shadowDom.appendChild(span);
    
    // attach shadow DOM to the #shadow-dom-host element
    function init() {
      const host = document.getElementById("shadow-dom-host");
      const shadowDom = host.attachShadow({ mode: "open" });
    
      const cssTab = document.querySelector("#css-output");
      const shadowStyle = document.createElement("style");
      shadowStyle.textContent = cssTab.textContent;
      shadowDom.appendChild(shadowStyle);
    
      cssTab.addEventListener("change", () => {
        shadowStyle.textContent = cssTab.textContent;
      });
      return shadowDom;
    }
    

css

    /* Selects a shadow root host, only if it is
       a descendant of the selector argument given */
    :host-context(h1) {
      font-weight: bold;
    }
    
    /* Changes paragraph text color from black to white when
       a .dark-theme class is applied to the document body */
    p {
      color: black;
    }
    
    :host-context(body.dark-theme) p {
      color: white;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#syntax)

----------------------------------------------------------------------------------------------------

css

    :host-context(<compound-selector>) {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#examples)

--------------------------------------------------------------------------------------------------------

### [Selectively styling shadow hosts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#selectively_styling_shadow_hosts)

The following snippets are taken from our [host-selectors example](https://github.com/mdn/web-components-examples/tree/main/host-selectors "External link (opens in new tab)")
 ([see it live also](https://mdn.github.io/web-components-examples/host-selectors/ "External link (opens in new tab)")
).

In this example we have a basic custom element — `<context-span>` — that you can wrap around text:

html

    <h1>
      Host selectors <a href="#"><context-span>example</context-span></a>
    </h1>
    

Inside the element's constructor, we create `style` and `span` elements, fill the `span` with the content of the custom element, and fill the `style` element with some CSS rules:

js

    const style = document.createElement("style");
    const span = document.createElement("span");
    span.textContent = this.textContent;
    
    const shadowRoot = this.attachShadow({ mode: "open" });
    shadowRoot.appendChild(style);
    shadowRoot.appendChild(span);
    
    style.textContent =
      "span:hover { text-decoration: underline; }" +
      ":host-context(h1) { font-style: italic; }" +
      ':host-context(h1)::after { content: " - no links in headers!" }' +
      ":host(.footer) { color : red; }" +
      ":host { background: rgb(0 0 0 / 10%); padding: 2px 5px; }";
    

The `:host-context(h1) { font-style: italic; }` and `:host-context(h1)::after { content: " - no links in headers!" }` rules style the instance of the `<context-span>` element (the shadow host in this instance) inside the `<h1>`. We've used it to make it clear that the custom element shouldn't appear inside the `<h1>` in our design.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shadow Module Level 1  <br>\# host-selector](https://drafts.csswg.org/css-shadow/#host-selector) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context#see_also)

--------------------------------------------------------------------------------------------------------

*   [Web components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)
    
*   CSS [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
     pseudo-class
*   CSS [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
     pseudo-class
*   CSS [`:state()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state)
     pseudo-class
*   CSS [`::slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
     pseudo-element
*   HTML [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
     element
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_host-context/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_host-context (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ahost-context&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_host-context%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ahost-context%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_host-context%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")