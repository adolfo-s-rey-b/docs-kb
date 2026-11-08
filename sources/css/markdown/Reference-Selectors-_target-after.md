*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#mdn-search)
    

`:target-after` CSS pseudo-class
================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/476)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#browser_compatibility)
 carefully before using this in production.

The **`:target-after`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selects scroll markers that come _after_ the active scroll marker (the one that currently matches [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
) within a scroll marker group. You can use this selector to style navigation items that come after the current navigation position within a scroll marker group.

**Note:** The `:target-after` pseudo-class is only valid on [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 pseudo-elements and elements that have been designated as scroll markers via the [`scroll-target-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group)
 property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#syntax)

----------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#examples)

--------------------------------------------------------------------------------------------------------

### [Styling navigation items before and after the active scroll marker](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#styling_navigation_items_before_and_after_the_active_scroll_marker)

In this example, we use the [`:target-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-before)
 and `:target-after` pseudo-classes to highlight the scroll markers before and after the active one, indicating items the user has already viewed and those that are still to come.

#### HTML

The markup contains a table of contents created using an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
/[`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
) and [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements. This is followed by a series of [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 elements containing content.

#### CSS

We've set `scroll-target-group: auto` on the `<ol>` to turn it into a scroll marker group container and let the browser determine which `<a>` element is the active scroll marker at any given time (that is, which link's target is currently in view). We then style the `:target-current` pseudo-class with a `red` [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 so that it stands out clearly.

Finally, we use the `:target-before` pseudo-class to style all `<a>` elements before the active scroll marker with a gray color and strike-through, to make them look completed/finished, and we use the `:target-after` pseudo-class to style all `<a>` elements after the active scroll marker with a bright underline.

#### Result

Try navigating either by clicking the links or by scrolling. In both cases, you'll see that the red text color moves between the links to match the section currently in view. The links before and after the current red link also update to use the styles defined in the `a:target-before` and `a:target-after` rules.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 5  <br>\# selectordef-target-after](https://drafts.csswg.org/css-overflow-5/#selectordef-target-after) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after#see_also)

--------------------------------------------------------------------------------------------------------

*   [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
    
*   [`scroll-target-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group)
    
*   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    , [`:target-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-before)
    
*   [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
    
*   [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
    
*   [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
    
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS Carousel Gallery](https://chrome.dev/carousel/ "External link (opens in new tab)")
     via chrome.dev (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_target-after/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_target-after (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Atarget-after&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_target-after%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Atarget-after%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_target-after%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")