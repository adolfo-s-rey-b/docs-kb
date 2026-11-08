*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#mdn-search)
    

`:host()` CSS pseudo-class
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:host()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 function selects the shadow host of the [shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
 containing the CSS it is used inside (so you can select a custom element from inside its shadow DOM) — but only if the selector given as the function's parameter matches the shadow host. **`:host()`** has no effect when used outside a shadow DOM.

The most obvious use of this is to put a class name only on certain custom element instances, and then include the relevant class selector as the function argument. You can't use this with a descendant selector expression to select only instances of the custom element that are inside a particular ancestor. That's the job of [`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
.

**Note:** While other functional pseudo-classes such as [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
 and [`:not()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:not)
 accept a list of selectors as their parameters, `:host()` takes a single compound selector as its parameter. In addition, while `:is()` and `:not()` only take into account the specificity of their argument, the specificity of `:host()` is both the specificity of the pseudo-class **and** the specificity of its argument.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#try_it)

-----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#syntax)

-----------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#examples)

---------------------------------------------------------------------------------------------------------

### [Selectively styling shadow hosts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#selectively_styling_shadow_hosts)

The following snippets are taken from our [host-selectors example](https://github.com/mdn/web-components-examples/tree/main/host-selectors "External link (opens in new tab)")
 ([see it live also](https://mdn.github.io/web-components-examples/host-selectors/ "External link (opens in new tab)")
).

In this example we have a custom element — `<context-span>` — that you can wrap around text:

Inside the element's constructor, we create `style` and `span` elements, fill the `span` with the content of the custom element, and fill the `style` element with some CSS rules:

The `:host(.footer) { color : red; }` rule styles all instances of the `<context-span>` element (the shadow host in this instance) in the document that have the `footer` class set on them — we've used it to give instances of the element inside the [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
 a special color.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shadow Module Level 1  <br>\# host-selector](https://drafts.csswg.org/css-shadow/#host-selector) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function#see_also)

---------------------------------------------------------------------------------------------------------

*   [Web components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)
    
*   [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
    
*   [`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
    
*   [`:state()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_host_function/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_host_function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ahost_function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_host_function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ahost_function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_host_function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")