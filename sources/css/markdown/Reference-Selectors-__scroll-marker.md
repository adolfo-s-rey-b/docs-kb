*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#mdn-search)
    

`::scroll-marker` CSS pseudo-element
====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/289)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#browser_compatibility)
 carefully before using this in production.

The **`::scroll-marker`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 can be generated inside any element and represents its scroll marker. All elements can have a `::scroll-marker` pseudo-element, which is placed into the [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
 of the nearest [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 ancestor. A scroll marker behaves like an anchor ([`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 element) whose scroll target is the marker's originating element — and scrolls the scroll container to that element when activated.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#syntax)

------------------------------------------------------------------------------------------------------

css

    ::scroll-marker {
      /* ... */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#description)

----------------------------------------------------------------------------------------------------------------

A `::scroll-marker` is generated on an element when the `::scroll-marker`'s [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property is set to a non-`none` value, and its has an ancestor scroll container with a non-`none` [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
 property value (meaning that it will generate a [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
 pseudo-element).

The scroll container's `::scroll-marker-group` pseudo-element automatically contains any `::scroll-marker` pseudo-elements generated on the scroll container or its descendants. This allows them to be positioned and laid out as a group and is typically used when creating a CSS carousel to create a scroll position indicator. The individual scroll markers can be used to navigate to their associated content items.

**Note:** Alternatively, a scroll marker group container can be created from an existing element container using [`scroll-target-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group)
; any contained [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements with fragment identifiers linking to sections of the page automatically behave like scroll markers.

When a scroll marker group container is created on a scroll container using the `scroll-marker-group` property, the scroll container is rendered with [`tablist`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tablist_role)
/[`tab`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role)
 semantics. You can Tab to it with the keyboard, then move between the different "pages" using the left and right (or up and down) cursor keys, which also changes the state of the associated scroll markers and scroll buttons as expected. The scroll markers can also be tabbed between normally, as expected.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#examples)

----------------------------------------------------------------------------------------------------------

See [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
 for other examples that use the `::scroll-marker` pseudo-element.

### [Creating carousel scroll markers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#creating_carousel_scroll_markers)

In this example, we demonstrate how to create scroll markers on a CSS carousel.

#### HTML

We have a basic HTML [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 list with several [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 list items.

html

    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
      <li>Item 4</li>
      <li>Item 5</li>
      <li>Item 6</li>
      <li>Item 7</li>
      <li>Item 8</li>
    </ul>
    

#### CSS

We convert our `<ul>` into a scroll snapping overflow container by setting the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `flex`, creating a single, non-wrapping row of `<li>` elements. The [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 property is set to `auto`, meaning if the items overflow their container on the x-axis, the content will scroll horizontally. We then convert the `<ul>` into a [scroll-snap container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#scroll_snap_container)
, ensuring that items always snap into place when the container is scrolled with a [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 value of `mandatory`.

We create a scroll marker group container with the `scroll-marker-group` property, placing it after all the content.

css

    ul {
      display: flex;
      gap: 4vw;
      padding-left: 0;
      overflow-x: auto;
      overscroll-behavior-x: contain;
      scroll-snap-type: x mandatory;
      scroll-marker-group: after;
    }
    

Next, we style the `<li>` elements, using the [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 property to make them `33%` of the width of the container. The [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
 value of `start` causes the left-hand side of the left-most visible item to snap to the left edge of the container when the content is scrolled.

css

    li {
      list-style-type: none;
      background-color: #eeeeee;
      flex: 0 0 33%;
      height: 100px;
      padding-top: 20px;
      scroll-snap-align: start;
      text-align: center;
    }
    

We then use the `::scroll-marker` pseudo-element to create a square marker for each list item with a red border:

css

    li::scroll-marker {
      content: "";
      border: 1px solid red;
      height: 1em;
      width: 1em;
    }
    

We also apply styles to the [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
 pseudo-element to lay out the scroll markers in the center of the row with a `0.4em` gap between each one:

css

    ::scroll-marker-group {
      display: flex;
      gap: 0.4em;
      place-content: center;
    }
    

Finally, we style the marker of the currently-scrolled element differently from the others, targeting the marker with the [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
 pseudo-class.

css

    ::scroll-marker:target-current {
      background: red;
    }
    

#### Result

### [Custom scroll marker numbering and style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#custom_scroll_marker_numbering_and_style)

This example is the same as the previous one, except that we have applied some different styling to the scroll markers, and used [CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
 to increment the number shown on each marker. The CSS differences are explained in the next section.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#css_2)

In this example, we set a name of a counter we want to increment on each `<li>` — `markers` — using the [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 property:

css

    li {
      counter-increment: markers;
    }
    

We then set the `::scroll-marker` pseudo-element's [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property to the [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 function, passing it the `markers` counter name as an argument. This has the effect of inserting a number into each marker, which increments automatically. The rest of the styling is rudimentary, but it illustrates how the markers can be fully-styled.

css

    li::scroll-marker {
      content: counter(markers);
      font-family: sans-serif;
      width: fit-content;
      height: 1em;
      padding: 5px;
      color: black;
      text-decoration: none;
      border: 2px solid rgb(0 0 0 / 0.15);
      border-radius: 0.5em;
      background-color: #eeeeee;
    }
    

For another interesting customization, we include two rules to select the marker of the first and last list items by inserting [`:first-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child)
 and [`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
 into the selector chain, respectively. We give the first marker text content of "First", and the last marker text content of "Last".

css

    li:first-child::scroll-marker {
      content: "First";
    }
    
    li:last-child::scroll-marker {
      content: "Last";
    }
    

To improve user experience, we set a different color on the markers on [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
 and use the `:target-current` pseudo-class to set a different [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 and [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 on the currently-scrolled element's marker so users know which item is currently in view:

css

    ::scroll-marker:hover {
      background-color: #ddcccc;
    }
    
    ::scroll-marker:target-current {
      background-color: purple;
      color: white;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 5  <br>\# scroll-marker-pseudo](https://drafts.csswg.org/css-overflow-5/#scroll-marker-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker#see_also)

----------------------------------------------------------------------------------------------------------

*   [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
    
*   [`scroll-target-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group)
    
*   [`::scroll-button()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button)
    
*   [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
    
*   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    
*   [`:target-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-before)
    
*   [`:target-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after)
    
*   [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
    
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS Carousel Gallery](https://chrome.dev/carousel/ "External link (opens in new tab)")
     via chrome.dev (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_scroll-marker/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_scroll-marker (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Ascroll-marker&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_scroll-marker%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Ascroll-marker%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_scroll-marker%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")