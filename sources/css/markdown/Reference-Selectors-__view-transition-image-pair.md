*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#mdn-search)
    

`::view-transition-image-pair()` CSS pseudo-element
===================================================

Baseline 2025

Newly available

Since October 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::view-transition-image-pair()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents a container for a [view transition's](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
 "old" and "new" view states — before and after the transition.

During a view transition, `::view-transition-image-pair()` is included in the associated pseudo-element tree as explained in [The view transition pseudo-element tree](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#the_view_transition_pseudo-element_tree)
. It is only ever a child of a [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
. In terms of children, it can have a [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
 or a [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
, or both.

`::view-transition-image-pair()` is given the following default styling in the UA stylesheet:

css

    :root::view-transition-image-pair(*) {
      position: absolute;
      inset: 0;
    
      animation-duration: inherit;
      animation-fill-mode: inherit;
      animation-delay: inherit;
    }
    

During a view transition, `::view-transition-image-pair()` has [`isolation: isolate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation)
 set on it in the view transition style sheet so that its children can be blended with non-normal blend modes without affecting other visual outputs.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#syntax)

-------------------------------------------------------------------------------------------------------------------

css

    ::view-transition-image-pair([ <pt-name-selector> <pt-class-selector>? ] | <pt-class-selector>) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#parameters)

[`*`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#sect)

The [universal selector (`*`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
; selects all view transition groups on a page.

[`root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#root)

Causes the pseudo-element to match the default `root` view transition snapshot group created by the user agent to contain the view transition for the overall page. This group includes any element not assigned to its own specific view transition snapshot group via the [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 property.

[`<pt-name-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#pt-name-selector)

The [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 set as the value of the [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 property.

[`<pt-class-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#pt-class-selector)

The [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 set as the value of the [`view-transition-class`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class)
 property preceded by a period (`.`).

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#examples)

-----------------------------------------------------------------------------------------------------------------------

css

    ::view-transition-image-pair(root) {
      isolation: auto;
    }
    
    ::view-transition-image-pair(.card) {
      isolation: isolate;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 1  <br>\# ::view-transition-image-pair](https://drafts.csswg.org/css-view-transitions/#::view-transition-image-pair) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_view-transition-image-pair/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_view-transition-image-pair (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aview-transition-image-pair&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_view-transition-image-pair%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aview-transition-image-pair%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_view-transition-image-pair%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")