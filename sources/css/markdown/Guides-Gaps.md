*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#mdn-search)
    

CSS gaps
========

The **CSS gaps** module lets you specify spacing, or "gaps", between items in [multi-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
, [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 layouts. The [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
 module originally defined gaps and rules that control the spacing between columns in multi-column containers. This module expands on these visible separators, called _gap decorations_, extending it to grid and flexbox.

While [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 and [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 specify visual spacing around individual boxes, the properties in this module enable specifying the spacing between adjacent boxes within a given layout context for layouts that have [gutters](https://developer.mozilla.org/en-US/docs/Glossary/Gutters)
 and gaps, when the spacing is different between sibling boxes as opposed to between the first box, last box, and the container's edge. You can show rules in every gap or in a subset of gaps, defining fully animatable rule widths, colors, and insets.

Gap decorations are painted within a gap as one or more gap decoration segments, with segments occurring between any two adjacent items. When all segments are drawn, column and row rules span the entire height and width of the container. The [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
 property defines whether segments are to be drawn around areas that are not occupied by items. The [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
 properties determine if lines break when they intersect a gap, while `rule-inset` defines where segments start and end when rules do break. If they don't break, the [`rule-overlap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap)
 property defines the painting order of the rules.

[Gaps in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#gaps_in_action)

----------------------------------------------------------------------------------------------

In this example, the 2021 poem from the USA inauguration, _The Hill We Climb_, by Amanda Gorman, is displayed across multiple columns, similar to the way articles are displayed in printed newspapers. If you have JavaScript enabled, controls enable changing the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
, [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
, [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
 and [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
 properties, as well as the preferred number of columns and whether the title and a quote should span all of the columns.

When the column rule is larger than the column gap, the decorative line appears behind the text; it doesn't change the size of the gap.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#reference)

------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#properties)

*   [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
    
*   [`column-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break)
    
*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   `column-rule-inset`
*   [`column-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
    
*   [`column-rule-inset-cap-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end)
    
*   [`column-rule-inset-cap-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-start)
    
*   `column-rule-inset-end`
*   [`column-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction)
    
*   [`column-rule-inset-junction-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-end)
    
*   [`column-rule-inset-junction-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start)
    
*   `column-rule-inset-start`
*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
*   [`column-rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items)
    
*   [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    
*   [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
    
*   [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
    
*   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
    
*   [`row-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
    
*   [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
    
*   `row-rule-inset`
*   [`row-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap)
    
*   [`row-rule-inset-cap-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end)
    
*   [`row-rule-inset-cap-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start)
    
*   `row-rule-inset-end`
*   [`row-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction)
    
*   [`row-rule-inset-junction-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end)
    
*   [`row-rule-inset-junction-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-start)
    
*   `row-rule-inset-start`
*   [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    
*   [`row-rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-visibility-items)
    
*   [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
    
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
    
*   [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
    
*   [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
    
*   `rule-inset`
*   [`rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap)
    
*   `rule-inset-end`
*   [`rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction)
    
*   `rule-inset-start`
*   [`rule-overlap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap)
    
*   [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
    
*   [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
    
*   [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
    

### [Terms and glossary definitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#terms_and_glossary_definitions)

*   [Grid](https://developer.mozilla.org/en-US/docs/Glossary/Grid)
    
*   [Grid cell](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Cell)
    
*   [Grid column](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Column)
    
*   [Grid lines](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Lines)
    
*   [Grid row](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Row)
    
*   [Gutters](https://developer.mozilla.org/en-US/docs/Glossary/Gutters)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#guides)

------------------------------------------------------------------------------

[Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)

Guide to understanding and defining gaps in grid, flexbox, and multi-column layouts, including how percentage values are resolved.

[Defining CSS gap rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_rules)

Guide to understanding and defining CSS gap rules, including using the `repeat()` function, to define rule colors, widths, and styles.

[Styling columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Styling_columns)

Guide to styling columns and managing spacing between columns.

[Handling content breaks in multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Handling_content_breaks)

Introduction to the fragmentation specification and how to control where column content breaks.

[Box alignment guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment#guides)

How [box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview)
 works in the context of [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox)
, [grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
, [multiple-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout)
, and for [block, absolutely positioned and table layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables)
.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#related_concepts)

--------------------------------------------------------------------------------------------------

[CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 module

*   [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
    
*   [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
    
*   [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
    
*   [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
    
*   [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
    
*   [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
    
*   [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
    

[CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 module

*   [`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid)
    
*   [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
    
*   [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
    
*   [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
    

[CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
 module

*   [`column-fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill)
    
*   [`column-span`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span)
    
*   [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
     shorthand
    *   [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
        
    *   [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
        
    *   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
        
*   [`column-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap)
    
*   [`::column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)
    

[CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)

*   [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    
*   [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    

[CSS box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
 module

*   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    
*   [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
    
*   [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
    
*   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    
*   [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
    

[CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
 module

*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    
*   [Block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
     guide

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#specifications)

----------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1](https://drafts.csswg.org/css-gaps/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#see_also)

----------------------------------------------------------------------------------

*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/gaps/index.md?plain=1 "Folder: en-us/web/css/guides/gaps (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGaps&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fgaps%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGaps%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fgaps%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff641d1e7c63d8300c9ff1c6a24158a80e1f24ab0%0A*+Document+last+modified%3A+2026-10-16T10%3A54%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")