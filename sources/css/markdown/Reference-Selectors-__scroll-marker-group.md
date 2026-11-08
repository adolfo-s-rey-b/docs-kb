*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#mdn-search)
    

`::scroll-marker-group` CSS pseudo-element
==========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/289)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#browser_compatibility)
 carefully before using this in production.

The **`::scroll-marker-group`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 is generated inside a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 and contains any [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 pseudo-elements generated on descendants of the scroll container.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#syntax)

------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#description)

----------------------------------------------------------------------------------------------------------------------

A scroll container's **`::scroll-marker-group`** pseudo-element represents a **scroll marker group container**. This is a container that automatically contains any [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 pseudo-elements generated on itself or its descendants. This allows them to be positioned and styled as a group. This pseudo-element is typically used when creating a CSS carousel to provide a scroll position indicator. The individual scroll markers can be used to navigate to their associated content items.

The scroll container must have its [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
 property set to a non-`none` value for the `::scroll-marker-group` pseudo-element to be generated. The [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
 value determines where the scroll marker group container appears in the carousel's tab order and layout box order (but not DOM structure) — `before` puts it at the start, while `after` puts it at the end.

**Note:** Alternatively, a scroll marker group container can be created from an existing element containing a set of [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements using [`scroll-target-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group)
.

As an accessibility best practice, match the visual rendering position of the scroll marker group container with the tab order. When positioning the group at the start of the content, put it at the beginning of the tab order using `before`. When positioning the group at the end of the content, put it at the end of the tab order using `after`.

When a scroll marker group container is created on a scroll container using the `scroll-marker-group` property, the scroll container is rendered with [`tablist`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tablist_role)
/[`tab`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role)
 semantics. You can Tab to it with the keyboard, then move between the different "pages" using the left and right (or up and down) cursor keys, which also changes the state of the associated scroll markers and scroll buttons as expected. The scroll markers can also be tabbed between normally, as expected.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#examples)

----------------------------------------------------------------------------------------------------------------

See [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
 for other examples that use the `::scroll-marker` pseudo-element.

### [Creating carousel scroll markers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#creating_carousel_scroll_markers)

This demo is a carousel of single pages, with each item taking up the full page. We have included scroll markers to enable the user to navigate to any page with the click of a marker.

#### HTML

The HTML consists of an [unordered list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
, with each [list item](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 containing some sample content:

#### CSS

We first convert our `<ul>` into a carousel by setting the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `flex`, creating a single, non-wrapping row of `<li>` elements. The [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 property is set to `auto`, meaning if the items overflow their container on the x-axis, the content will scroll horizontally. We then convert the `<ul>` into a [scroll-snap container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#scroll_snap_container)
, ensuring that items always snap into place when the container is scrolled with a [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 value of `mandatory`.

Next, we style the `<li>` elements, using the [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 property to make them `100%` of the width of the container. The [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
 value of `start` causes the left-hand side of the left-most visible item to snap to the left edge of the container when the content is scrolled.

Next, the list's [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
 property is set to `after`, so the `::scroll-marker-group` pseudo-element is placed after the list's DOM content in the tabbing order and layout box order; this means it comes after the scroll buttons:

Next, the list's `::scroll-marker-group` pseudo-element is laid out using flexbox, with a [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 value of `center` and a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `20px` so that its children (the [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 pseudo-elements) are centered inside the `::scroll-marker-group` with a gap between each one.

Next, the scroll markers themselves are styled. The look of each one is handled by setting [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
, and [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
, but we also need to set a non-`none` value for the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
, property so they are actually generated.

**Note:** Generated content is inline by default; we can apply `width` and `height` to our scroll markers because they are being laid out as flex items.

Finally, the [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
 pseudo-class is used to select whichever scroll marker corresponds to the currently visible "page", highlighting how far the user has scrolled through the content. In this case, we set the `background-color` to `black` so it is styled as a filled-in circle.

#### Result

### [Positioning the scroll marker group container with anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#positioning_the_scroll_marker_group_container_with_anchor_positioning)

This example extends the previous one, demonstrating the use of [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 to position the scroll marker group container relative to the carousel.

#### CSS

The list's `::scroll-marker-group` pseudo-element is positioned relative to the carousel using CSS anchor positioning by giving the group a value for [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 that matches the [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 of the `<ul>`. We then position the group relative to the scroll container in the block direction by setting a [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
 value that includes an [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
 function. We also add a [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 value of `anchor-center`, which aligns the group to the center of the scroll container in the inline direction.

css

    ul {
      anchor-name: --my-carousel;
    }
    
    ul::scroll-marker-group {
      /* From the previous example */
      display: flex;
      gap: 20px;
    
      position: absolute;
      position-anchor: --my-carousel;
      top: calc(anchor(bottom) - 70px);
      justify-self: anchor-center;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 5  <br>\# scroll-marker-group-pseudo](https://drafts.csswg.org/css-overflow-5/#scroll-marker-group-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
    
*   [`scroll-target-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group)
    
*   [`::scroll-button()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button)
    
*   [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
    
*   [`::column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)
    
*   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    
*   [`:target-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-before)
    
*   [`:target-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after)
    
*   [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
    
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS Carousel Gallery](https://chrome.dev/carousel/ "External link (opens in new tab)")
     via chrome.dev (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_scroll-marker-group/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_scroll-marker-group (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Ascroll-marker-group&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_scroll-marker-group%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Ascroll-marker-group%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_scroll-marker-group%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")