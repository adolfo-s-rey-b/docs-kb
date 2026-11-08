*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#mdn-search)
    

`::view-transition-group()` CSS pseudo-element
==============================================

Baseline 2025

Newly available

Since October 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::view-transition-group()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents a single view transition snapshot group.

During a view transition, `::view-transition-group()` is included in the associated pseudo-element tree as explained in [The view transition pseudo-element tree](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#the_view_transition_pseudo-element_tree)
. It is only ever a child of [`::view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition)
, and has a [`::view-transition-image-pair()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair)
 as a child.

`::view-transition-group()` is given the following default styling in the UA stylesheet:

By default, selected elements initially mirror the size and position of the [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
 pseudo-element representing the "old" view state, or the [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
 pseudo-element representing the "new" view state if there isn't an "old" view state.

If there's both an "old" and "new" view state, styles in the view transition style sheet animate this pseudo-element's [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 from the size of the "old" view state's border box to that of the "new" view state's border box.

**Note:** View transition styles are dynamically generated during the view transition; see the specification [setup transition pseudo-elements](https://drafts.csswg.org/css-view-transitions-1/#setup-transition-pseudo-elements "External link (opens in new tab)")
 and [update pseudo-element styles](https://drafts.csswg.org/css-view-transitions-1/#update-pseudo-element-styles "External link (opens in new tab)")
 sections for more details.

In addition, the element's transform is animated from the "old" view state's screen space transform to the new view state's screen space transform. This style is generated dynamically since the values of animated properties are determined at the time that the transition begins.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#syntax)

--------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#parameters)

[`*`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#sect)

The [universal selector (`*`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
; selects all view transition groups on a page.

[`root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#root)

The [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 applied to [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
 causes the pseudo-element to match the default `root` view transition group. This is the snapshot group created by the user agent to contain the view transition for the overall page. This group includes any element not assigned to its own specific view transition snapshot group via the `view-transition-name` property.

[`<pt-name-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#pt-name-selector)

The [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 set as the value of the [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 property.

[`<pt-class-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#pt-class-selector)

The [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 set as the value of the [`view-transition-class`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class)
 property, preceded by a period (`.`).

The [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
 of the named view transition pseudo-element is equal to the [specificity of the type selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity#type_column)
, unless the parameter used is the universal selector is used, in which case the specificity is zero.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#examples)

------------------------------------------------------------------------------------------------------------------

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 1  <br>\# ::view-transition-group](https://drafts.csswg.org/css-view-transitions/#::view-transition-group) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group#see_also)

------------------------------------------------------------------------------------------------------------------

*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_view-transition-group/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_view-transition-group (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aview-transition-group&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_view-transition-group%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aview-transition-group%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_view-transition-group%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fddf85bfec1b6e43cdacb404de0c38a801c561640%0A*+Document+last+modified%3A+2026-05-12T10%3A30%3A13.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")