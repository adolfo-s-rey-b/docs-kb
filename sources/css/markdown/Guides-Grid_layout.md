*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#mdn-search)
    

CSS grid layout
===============

The **CSS grid layout** module excels at dividing a page into major regions or defining the relationship in terms of size, position, and layering between parts of a control built from HTML primitives.

Like tables, grid layout enables an author to align elements into columns and rows. However, many more layouts are either possible or easier with CSS grid than they were with tables. For example, a grid container's child elements could position themselves so they actually overlap and layer, similar to CSS positioned elements.

[Grid layout in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#grid_layout_in_action)

-------------------------------------------------------------------------------------------------------------------

The example shows a three-column track grid with new rows created at a minimum of 100 pixels and a maximum of auto. Items have been placed onto the grid using line-based placement.

This sample animation uses [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
, [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
, [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
, and [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 to create the grid, and [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
 and [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
 to position items within the grid. To view and edit the HTML and CSS used, click the 'Play' at the top right of the example.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#reference)

-------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#properties)

*   [`grid-auto-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-columns)
    
*   [`grid-auto-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow)
    
*   [`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
    
*   [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
    
*   [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
    
*   [`grid-template-areas`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas)
    
*   [`grid-template`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template)
     shorthand
*   [`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid)
     shorthand
*   [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
    
*   [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
    
*   [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
     shorthand
*   [`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
    
*   [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
    
*   [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
     shorthand
*   [`grid-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area)
     shorthand

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#functions)

*   [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
    
*   [`minmax()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)
    
*   [`fit-content()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)
    

### [Data types and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#data_types_and_values)

*   [`<flex>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)
     (`fr` unit)

### [Terms and glossary definitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#terms_and_glossary_definitions)

*   [Grid](https://developer.mozilla.org/en-US/docs/Glossary/Grid)
    
*   [Grid areas](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Areas)
    
*   [Grid axis](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Axis)
    
*   [Grid cell](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Cell)
    
*   [Grid column](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Column)
    
*   [Grid container](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Container)
    
*   [Grid lines](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Lines)
    
*   [Grid row](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Row)
    
*   [Grid tracks](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Tracks)
    
*   [Gutters](https://developer.mozilla.org/en-US/docs/Glossary/Gutters)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#guides)

-------------------------------------------------------------------------------------

[Basic concepts of grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts)

An overview of the various features provided in the CSS grid layout module.

[Relationship of grid layout with other layout methods](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods)

How grid layout fits together with other CSS features including flexbox, absolutely positioned elements, and `display: contents`.

[Grid layout using line-based placement](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement)

Grid lines and how to position items against those lines, including the `grid-area` properties, negative line numbers, spanning multiple cells, and creating grid gutters.

[Grid template areas](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_template_areas)

Placing grid items using named template areas.

[Grid layout using named grid lines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Named_grid_lines)

Combining names and track sizes; placing grid items by defining named grid lines and template areas.

[Auto-placement in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Auto-placement)

How grid positions items that don't have any placement properties declared.

[Aligning items in CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Box_alignment)

Aligning, justifying, and centering grid items along the two axes of a grid layout.

[Grids, logical values, and writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes)

A look at the interaction between CSS grid layout, box alignment and writing modes, along with CSS logical and physical properties and values.

[Grid layout and accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Accessibility)

A look at how CSS grid layout can both help and harm accessibility.

[Realizing common layouts using grids](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Common_grid_layouts)

A few different layouts demonstrating different techniques you can use when designing with CSS grid layouts, including using [`grid-template-areas`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas)
, a 12-column flexible grid system, and a product listing using auto-placement.

[Subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Subgrid)

What subgrid does with use cases and design patterns that subgrid solves.

[Grid lanes layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes)

Details what grid lanes layout is and how to use it.

[Box alignment in CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)

How box alignment works in the context of grid layout.

[Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)

Understanding and defining gaps in grid, flexbox, and multi-column layouts, including how percentage values are resolved.

[Related features](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#related_features)

---------------------------------------------------------------------------------------------------------

[CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
 module

*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    
*   [`order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order)
    

[CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
 module

*   [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    
*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    
*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    
*   [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    
*   [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    
*   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    
*   [`place-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
    
*   [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
    
*   [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
    

[CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
 module

*   [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
     shorthand
    *   [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
        
    *   [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
        
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
    *   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
        
    *   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
        
*   [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
    
*   [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
    
*   `rule-inset`
*   [`rule-overlap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap)
    
*   [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
    
*   [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
    
*   [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
    

[CSS box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
 module

*   [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
    
*   [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
    
*   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    
*   [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
    
*   [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
    
*   [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
    
*   [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
    
*   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    
*   [`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
     data type
*   [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
     value
*   [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
     value
*   [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
     value
*   [`fit-content()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)
     function

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#specifications)

-----------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2](https://drafts.csswg.org/css-grid/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout#see_also)

-----------------------------------------------------------------------------------------

*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module
*   [CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
     module
*   [Grid by example](https://gridbyexample.com/ "External link (opens in new tab)")
    
*   [CSS grid reference](https://tympanus.net/codrops/css_reference/grid/ "External link (opens in new tab)")
     via Codrops
*   [Firefox DevTools: grid inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_grid_layouts/index.html "External link (opens in new tab)")
    
*   [CSS grid playground](https://mozilladevelopers.github.io/playground/css-grid/ "External link (opens in new tab)")
    
*   [CSS grid garden](https://cssgridgarden.com/ "External link (opens in new tab)")
     - A game for learning CSS grid

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/grid_layout/index.md?plain=1 "Folder: en-us/web/css/guides/grid_layout (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGrid_layout&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fgrid_layout%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGrid_layout%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fgrid_layout%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F04dfe418f2942ae739d41592c22fafa3679fc03c%0A*+Document+last+modified%3A+2026-10-05T17%3A37%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")