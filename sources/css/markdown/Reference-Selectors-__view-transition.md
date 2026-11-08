*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition#mdn-search)
    

`::view-transition` CSS pseudo-element
======================================

Baseline 2025

Newly available

Since October 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::view-transition`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents the root of the [view transitions](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
 overlay, which contains all view transition snapshot groups and sits over the top of all other page content.

During a view transition, `::view-transition` is included in the associated pseudo-element tree as explained in [The view transition pseudo-element tree](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#the_view_transition_pseudo-element_tree)
. It is the top-level node of this tree, and has one or more [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
s as children.

`::view-transition` is given the following default styling in the UA stylesheet:

All [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
 pseudo-elements are positioned relative to the view transition root.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition#syntax)

--------------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition#examples)

------------------------------------------------------------------------------------------------------------

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 1  <br>\# selectordef-view-transition](https://drafts.csswg.org/css-view-transitions/#selectordef-view-transition) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition#see_also)

------------------------------------------------------------------------------------------------------------

*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_view-transition/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_view-transition (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aview-transition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_view-transition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aview-transition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_view-transition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")