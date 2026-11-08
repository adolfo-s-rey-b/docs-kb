*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#mdn-search)
    

`::column` CSS pseudo-element
=============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/294)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#browser_compatibility)
 carefully before using this in production.

The **`::column`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents the individual columns generated when a container is set to display its content in multiple columns via [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
. The `::column` pseudo-element enables applying styles that do not affect the layout to these generated fragments.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#syntax)

-----------------------------------------------------------------------------------------------

css

    ::column {
      /* ... */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#description)

---------------------------------------------------------------------------------------------------------

When CSS multi-column layout is used to lay out a container's content in multiple columns (for example, using the [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 property), `::column` pseudo-elements are generated to contain each individual column.

The `::column` pseudo-element only accepts scroll snap properties that apply to elements inside a scroll container, including [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
, [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
, and [`scroll-snap-stop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
.

The `::column` pseudo-element can have a [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 pseudo-element. Other pseudo-elements like [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
 are not generated on `::column`. Applying `::column::scroll-marker` creates a marker for every column of the originating [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
, with the `::scroll-marker` pseudo-elements inheriting from the `::column` pseudo-element's originating element rather than the `::column` itself.

This is useful for [CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
 — `::column` can be used to generate `::scroll-marker` pseudo-elements for each column, and set them as [snap targets](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snap_target)
 using [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
.

While the styling that can be applied to `::column` is very limited, it may be expanded in the future. Any properties and values supported in the future will be limited to ones that do not affect layout.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#examples)

---------------------------------------------------------------------------------------------------

### [Scrolling column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#scrolling_column_layout)

This demo creates a responsive container that snaps each "page" of content into place. It uses the [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
 property and the `::column` pseudo-element to create content columns that span the full width of their parent [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
, which can be scrolled horizontally. Each column contains one or more list items, which vary in number depending on the viewport width.

#### HTML

The HTML consists of an [unordered list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
, with each [list item](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 containing some sample content:

html

    <ul>
    ...
      <li>
        <h2>Item 1</h2>
      </li>
    ...
    </ul>
    

    <ul>
      <li>
        <h2>Item 1</h2>
      </li>
      <li>
        <h2>Item 2</h2>
      </li>
      <li>
        <h2>Item 3</h2>
      </li>
      <li>
        <h2>Item 4</h2>
      </li>
      <li>
        <h2>Item 5</h2>
      </li>
      <li>
        <h2>Item 6</h2>
      </li>
      <li>
        <h2>Item 7</h2>
      </li>
      <li>
        <h2>Item 8</h2>
      </li>
      <li>
        <h2>Item 9</h2>
      </li>
      <li>
        <h2>Item 10</h2>
      </li>
      <li>
        <h2>Item 11</h2>
      </li>
      <li>
        <h2>Item 12</h2>
      </li>
      <li>
        <h2>Item 13</h2>
      </li>
      <li>
        <h2>Item 14</h2>
      </li>
      <li>
        <h2>Item 15</h2>
      </li>
    </ul>
    

#### CSS

The list is given a fixed [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 and a [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 of `100vw` to make it span the full width of the viewport. An [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 value of `scroll` is then set so that the content will scroll horizontally, and [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
 is used to snap to each item or "page" — a [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 value of `x mandatory` is used to make the list into a [scroll snap container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#scroll_snap_container)
. Finally, a [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
 value of `1` is set to force the list contents to display as a single column. A [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 value of `center` is also applied, to align the content with the center of the list.

    * {
      box-sizing: border-box;
    }
    
    body {
      margin: 0;
      font-family: "Helvetica", "Arial", sans-serif;
    }
    

css

    ul {
      width: 100vw;
      height: 300px;
      padding: 10px;
    
      overflow-x: scroll;
      scroll-snap-type: x mandatory;
    
      columns: 1;
      text-align: center;
    }
    

The list items are then styled:

*   A [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
     value of `inline-block` is set to make the list items sit alongside one another and make the list scroll horizontally.
*   A fixed [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
     and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
     has been set on them.
*   A `text-align` value of `left` is set on them to override the `text-align: center` set on the parent container, so the item content will be left-aligned.
*   Every even-numbered list item is given a different background-color via [`:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
    , so that it is easier to see the scrolling effect.

css

    li {
      list-style-type: none;
    
      display: inline-block;
      height: 100%;
      width: 200px;
      text-align: left;
    
      background-color: #eeeeee;
      outline: 1px solid #dddddd;
      padding: 0 20px;
      margin: 0 10px;
    }
    
    li:nth-child(even) {
      background-color: cyan;
    }
    

The [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
 property is set on the `::column` pseudo-elements — which represent the content columns generated by the `columns` property — so that when scrolled, a column is snapped to be centered within the scroll container.

css

    ul::column {
      scroll-snap-align: center;
    }
    

#### Result

### [Column-based carousel with scroll markers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#column-based_carousel_with_scroll_markers)

Expanding on the previous example, we will create scroll markers to enable direct navigation to different columns by applying a [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
 to the container and a [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 to each `::column` pseudo-element. The HTML remains unchanged.

#### CSS

We create a scroll marker group with the [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
 property, placing the group after all the content:

css

    ul {
      scroll-marker-group: after;
    }
    

We then apply styles to the [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
 pseudo-element to lay out the scroll markers in the center of the row with a `0.4em` gap between each one:

css

    ::scroll-marker-group {
      display: flex;
      gap: 0.4em;
      place-content: center;
    }
    

Finally, we use the [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 pseudo-element to create a round, transparent marker for each list item with a black border, then style the marker of the currently-scrolled element differently from the others, targeting the marker with the [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
 pseudo-class:

css

    ul::column::scroll-marker {
      content: "";
      width: 16px;
      height: 16px;
      background-color: transparent;
      border: 2px solid black;
      border-radius: 10px;
    }
    
    ul::column::scroll-marker:target-current {
      background-color: black;
    }
    

#### Result

Try pressing the scroll markers to jump straight to each page. Note how the current marker is highlighted so you can see where you are in the pagination. Also try tabbing to the scroll marker group, then use the cursor keys to cycle through each page.

See [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
 for more carousel examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Multi-column Layout Module Level 2  <br>\# column-pseudo](https://drafts.csswg.org/css-multicol-2/#column-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column#see_also)

---------------------------------------------------------------------------------------------------

*   [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
    
*   [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
    
*   [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
    
*   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    
*   [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
    
*   [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
     module
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS Carousel Gallery](https://chrome.dev/carousel/ "External link (opens in new tab)")
     via chrome.dev (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_column/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_column (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Acolumn&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_column%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Acolumn%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_column%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")