*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#mdn-search)
    

`::view-transition-old()` CSS pseudo-element
============================================

Baseline 2025

Newly available

Since October 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::view-transition-old()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents the "old" view state of a view transition — a static snapshot of the old view, before the transition.

During a view transition, `::view-transition-old()` is included in the associated pseudo-element tree as explained in [The view transition pseudo-element tree](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#the_view_transition_pseudo-element_tree)
, provided there's an "old" view state to represent. It is only ever a child of a [`::view-transition-image-pair()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair)
, and never has any children.

It is a replaced element and therefore can be manipulated with properties such as [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 and [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
. It has natural dimensions equal to the content's size.

The following default styling is included in the UA stylesheet:

**Note:** Additional view transition styles are also setup to animate `::view-transition-old()`. These are dynamically generated during the view transition; see the specification [setup transition pseudo-elements](https://drafts.csswg.org/css-view-transitions-1/#setup-transition-pseudo-elements "External link (opens in new tab)")
 and [update pseudo-element styles](https://drafts.csswg.org/css-view-transitions-1/#update-pseudo-element-styles "External link (opens in new tab)")
 sections for more details.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#syntax)

------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#parameters)

[`*`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#sect)

The universal selector (`*`) selects all view transition groups on a page.

[`root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#root)

Causes the pseudo-element to match the default `root` view transition snapshot group created by the user agent to contain the view transition for the overall page. This group includes any element not assigned to its own specific view transition snapshot group via the [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 property.

[`<pt-name-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#pt-name-selector)

The [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 set as the value of the [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 property.

[`<pt-class-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#pt-class-selector)

The [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 set as the value of the [`view-transition-class`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class)
 property preceded by a period (`.`).

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#examples)

----------------------------------------------------------------------------------------------------------------

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 1  <br>\# ::view-transition-old](https://drafts.csswg.org/css-view-transitions/#::view-transition-old) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old#see_also)

----------------------------------------------------------------------------------------------------------------

*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_view-transition-old/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_view-transition-old (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aview-transition-old&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_view-transition-old%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aview-transition-old%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_view-transition-old%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")