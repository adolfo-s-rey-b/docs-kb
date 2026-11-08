*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#mdn-search)
    

`:has-slotted` CSS pseudo-class
===============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/276)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:has-slotted`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches when the content of a [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
 element is not empty or not using the default value (see [Using templates and slots](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_templates_and_slots)
 for more information).

**Note:** Even a single whitespace text node is sufficient to make `:has-slotted` apply.

This only works when used inside CSS placed within a [shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
.

css

    /* Selects the content of a <slot> element that has content that is not default  */
    :has-slotted {
      color: green;
    }
    
    /* Selects the content of a <slot> element that has no content or default  */
    :not(:has-slotted) {
      color: red;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#syntax)

---------------------------------------------------------------------------------------------------

css

    :has-slotted {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#examples)

-------------------------------------------------------------------------------------------------------

This example has two `<slot>` elements, one of which has been assigned some content and the other has not.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#html)

html

    <p>
      <template shadowrootmode="open">
        <style>
          :has-slotted {
            color: rebeccapurple;
          }
        </style>
        <slot name="one">Placeholder 1</slot>
        <slot name="two">Placeholder 2</slot>
      </template>
      <span slot="one">Slotted content</span>
    </p>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#result)

The `<slot>` element that has been assigned content matched the `:has-slotted` pseudo-class and has the `color` value of `rebeccapurple` applied.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shadow Module Level 1  <br>\# the-has-slotted-pseudo](https://drafts.csswg.org/css-shadow/#the-has-slotted-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted#see_also)

-------------------------------------------------------------------------------------------------------

*   HTML [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
     element
*   HTML [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
     element
*   [`::slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_has-slotted/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_has-slotted (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ahas-slotted&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_has-slotted%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ahas-slotted%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_has-slotted%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")