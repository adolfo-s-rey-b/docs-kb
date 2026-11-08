*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#mdn-search)
    

`::slotted()` CSS pseudo-element
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::slotted()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents any element that has been placed into a slot inside an HTML template (see [Using templates and slots](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_templates_and_slots)
 for more information).

This only works when used inside CSS placed within a [shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
. Note that this selector won't select a text node placed into a slot; it only targets actual elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#try_it)

------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#syntax)

------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#examples)

----------------------------------------------------------------------------------------------------

### [Highlighting slotted elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#highlighting_slotted_elements)

In this example, we use a template with three slots:

We define the `<person-details>` custom element. In this case, we add styles with JavaScript, though we could have added them in a [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
 block within the [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
 with the same effect:

When filling the `style` element with content, you'll see that we select all slotted elements (`::slotted(*)`) and give them a different font and color. This differentiates them from the slots that haven't been filled. We styled all the slotted [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
s (`::slotted(span)`) to differentiate the `<span>`s from the [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
s.

Our markup includes three custom elements, including a custom element with an invalid slot name in a source order that differs from the `<template>`:

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shadow Module Level 1  <br>\# slotted-pseudo](https://drafts.csswg.org/css-shadow/#slotted-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted#see_also)

----------------------------------------------------------------------------------------------------

*   [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
    
*   [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
    
*   [`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
    
*   [`:has-slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted)
    
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
     module
*   HTML [`slot`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/slot)
     attribute
*   HTML [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
     element
*   HTML [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
     element
*   [Web components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_slotted/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_slotted (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aslotted&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_slotted%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aslotted%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_slotted%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")