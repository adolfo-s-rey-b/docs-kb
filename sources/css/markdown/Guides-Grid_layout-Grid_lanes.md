*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#mdn-search)
    

Grid lanes layout
=================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/308)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#browser_compatibility)
 carefully before using this in production.

Level 3 of the [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 specification defines **grid lanes layout**, which is accessed via the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 values `grid-lanes` and `inline-grid-lanes`. This guide explains how grid lanes layout works and how to use it.

Grid lanes layout is a layout method where one axis uses a strict grid layout and the other uses a stacking algorithm. Each item is placed into the lane with the most available space, producing a tightly packed layout without strict tracks on the stacking axis.

Grid lanes layout is often referred to as _masonry layout_, because it resembles the way bricks are laid in a wall, filling gaps as efficiently as possible.

[Creating a grid lanes layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#creating_a_grid_lanes_layout)

--------------------------------------------------------------------------------------------------------------------------------------------

To create the most common grid lanes layout, where the columns are laid out in a grid and the rows are packed using the grid lanes layout algorithm, use **`display: grid-lanes`** along with [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
.

The child elements of this container will lay out item by item along the stacking axis according to the grid lanes layout algorithm: each row of items loads into the column with the most room, causing a tightly packed layout without strict row tracks.

    * {
      box-sizing: border-box;
    }
    
    body {
      font: 1.2em sans-serif;
    }
    
    .grid {
      padding: 10px;
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
    }
    
    .item {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      color: #d9480f;
    }
    

css

    .grid {
      display: grid-lanes;
      gap: 10px;
      grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    }
    

html

    <div class="grid">
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
    </div>
    

js

    // prettier-ignore
    const itemSizes = [\
      "2em", "3em", "1.6em", "4em", "3.2em",\
      "3em", "4.5em", "1em", "3.5em", "2.8em",\
    ];
    const items = document.querySelectorAll(".item");
    for (let i = 0; i < items.length; i++) {
      items[i].style.blockSize = itemSizes[i];
    }
    

It is also possible to create a grid lanes layout with items loading into rows.

js

    // prettier-ignore
    const itemSizes = [\
      "2em", "3em", "1.6em", "4em", "2.2em",\
      "3em", "4.5em", "1em", "3.5em", "2.8em",\
    ];
    const items = document.querySelectorAll(".item");
    for (let i = 0; i < items.length; i++) {
      items[i].style.inlineSize = itemSizes[i];
    }
    

css

    .grid {
      display: grid-lanes;
      gap: 10px;
      grid-template-rows: repeat(3, 100px);
    }
    

[Controlling the grid axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#controlling_the_grid_axis)

--------------------------------------------------------------------------------------------------------------------------------------

On the grid axis, things will work just as you expect them to in grid layout. You can cause items to span multiple tracks while remaining in auto-placement, using the `span` keyword. Items may also be positioned using line-based positioning.

### [Grid lanes layout with spanning items](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#grid_lanes_layout_with_spanning_items)

In this example two of the items span two tracks, and the remaining items are packed around them by the grid lanes layout algorithm.

html

    <div class="grid">
      <div class="item"></div>
      <div class="item span-2"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item span-2"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
    </div>
    

css

    .grid {
      display: grid-lanes;
      gap: 10px;
      grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    }
    
    .span-2 {
      grid-column-end: span 2;
    }
    

This example includes an item which has positioning for columns. Items with definite placement are placed before the grid lanes layout algorithm runs.

html

    <div class="grid">
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item positioned">positioned.</div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
      <div class="item"></div>
    </div>
    

css

    .grid {
      display: grid-lanes;
      gap: 10px;
      grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    }
    
    .positioned {
      padding: 1em;
      grid-column: 2 / 4;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 3  <br>\# valdef-display-grid-lanes](https://drafts.csswg.org/css-grid-3/#valdef-display-grid-lanes) |
| [CSS Grid Layout Module Level 3  <br>\# valdef-display-inline-grid-lanes](https://drafts.csswg.org/css-grid-3/#valdef-display-inline-grid-lanes) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

### [css.properties.display.grid-lanes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#css.properties.display.grid-lanes)

### [css.properties.display.inline-grid-lanes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#css.properties.display.inline-grid-lanes)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes#see_also)

----------------------------------------------------------------------------------------------------

*   [`grid-auto-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow)
     for controlling grid auto-placement

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/grid_layout/grid_lanes/index.md?plain=1 "Folder: en-us/web/css/guides/grid_layout/grid_lanes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGrid_layout%2FGrid_lanes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fgrid_layout%2Fgrid_lanes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGrid_layout%2FGrid_lanes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fgrid_layout%2Fgrid_lanes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6ddfa5bed55ec6dc6f506ea9d894c2b449617e55%0A*+Document+last+modified%3A+2026-08-27T07%3A50%3A10.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")