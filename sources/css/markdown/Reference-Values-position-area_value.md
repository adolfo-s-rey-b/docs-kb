*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#mdn-search)
    

`<position-area>` CSS type
==========================

Baseline 2026

Newly available

Since January 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/245)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<position-area>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 defines the cell or spanned cells of a **position-area grid**, a 3x3 grid whose center cell is an anchor element.

The `<position-area>` keyword values can be set as the value of the [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 property to place an anchor-positioned element in a specific location relative to its associated anchor element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#syntax)

-------------------------------------------------------------------------------------------------------

<position-area> = \[\
  \[ left | center | right | span-left | span-right | x-start | x-end | span-x-start | span-x-end | self-x-start | self-x-end | span-self-x-start | span-self-x-end | span-all \]\
||\
  \[ top | center | bottom | span-top | span-bottom | y-start | y-end | span-y-start | span-y-end | self-y-start | self-y-end | span-self-y-start | span-self-y-end | span-all \]\
|\
  \[ block-start | center | block-end | span-block-start | span-block-end | span-all \]\
||\
  \[ inline-start | center | inline-end | span-inline-start | span-inline-end | span-all \]\
|\
  \[ self-block-start | self-block-end | span-self-block-start | span-self-block-end | span-all \]\
||\
  \[ self-inline-start | self-inline-end | span-self-inline-start | span-self-inline-end | span-all \]\
|\
  \[ start | center | end | span-start | span-end | span-all \]{1,2}\
|\
  \[ self-start | center | self-end | span-self-start | span-self-end | span-all \]{1,2}\
\]

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#description)

-----------------------------------------------------------------------------------------------------------------

Position areas work on the concept of a **position-area grid**, a 3x3 grid of tiles composed of four grid lines, two on each axis, with an anchor element being the center tile:

![The position-area grid, as described below](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value/position-area.png)

When used as the value of a positioned element's `position-area` property, the dimensions of the center tile are defined by the [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 of the element's default anchor element. The dimensions of the grid's outer edge are defined by the positioned element's containing block. Logical keyterms are generally based on the writing mode and direction of the containing block, except for the `self-*` keyterms, which are calculated from the writing mode of the anchor-positioned element.

The grid tiles are broken up into rows and columns:

*   The three rows are represented by the physical values `top`, `center`, and `bottom`. They also have logical equivalents such as `block-start`, `center`, and `block-end`, and coordinate equivalents — `y-start`, `center`, and `y-end`.
*   The three columns are represented by the physical values `left`, `center`, and `right`. They also have logical equivalents such as `inline-start`, `center`, and `inline-end`, and coordinate equivalents — `x-start`, `center`, and `x-end`.

`<position-area>` values contain one or two keywords defining a specific area of the position-area grid. Setting a `position-area` value on a positioned element places its containing block in the specified grid area:

The different types of keywords that can be used include:

*   [Physical grid keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#physical_grid_keywords)
    
*   [Generic logical row and column keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#generic_logical_row_and_column_keywords)
    
*   [Explicit inline and block logical keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#explicit_inline_and_block_logical_keywords)
    
*   [Coordinate grid keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#coordinate_grid_keywords)
    

**Note:** Generally, you can't mix different types in one value, e.g., physical and logical. To do so results in invalid values. For example, `position-area: bottom inline-end` is not a valid value because it mixes physical and logical keywords.

[Physical grid keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#physical_grid_keywords)

---------------------------------------------------------------------------------------------------------------------------------------

The physical grid keywords specify a cell or section of the `position-area` grid using physical values. These values are not affected by [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 or [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 settings.

With physical row and column keywords, you can specify one keyword from each of the two lists below to select a single specific grid tile:

*   `top`, `center`, or `bottom`: The top, center, or bottom row of the grid.
*   `left`, `center`, or `right`: The left-hand, center, or right-hand column of the grid.

For example, `top left` selects the top left tile, while `center right` selects the center tile of the right-hand column.

### [Physical spanning grid keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#physical_spanning_grid_keywords)

The physical spanning keywords — when combined with a physical row or column keyword — specify a second grid tile for the position area to expand into. When such a combination is set as a `position-area` property value, a selected element is initially placed in the center of the specified row or column; it then spans in the direction specified in the spanning keyword, spanning two grid tiles:

[`span-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-left)

Span the center column and the left-hand column of the grid.

[`span-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-right)

Span the center column and the right-hand column of the grid.

[`span-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-top)

Span the center row and the top row of the grid.

[`span-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-bottom)

Span the center row and the bottom row of the grid.

[`span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-all_2)

Valid with all the keyword types, spans the cell listed as well as the adjacent cells in the same row or column. See [`span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-all_2)
 below.

For example, `top span-left` spans the top-center and top-left grid cells.

**Note:** Trying to pair a row or column keyword with an inappropriate spanning keyword will result in an invalid value. For example, `right span-right` is invalid — you can't select the center-right grid tile and then try to span further to the right.

### [Physical grid keyword defaults](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#physical_grid_keyword_defaults)

If only a single physical keyword is specified in the `position-area` value, the other value is implied as follows:

[`left`, `right`, `top`, or `bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#left)

The other value defaults to [`span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-all_2)
, causing the element to span all three tiles of the column or row it was initially placed in. For example, `left` is equivalent to `left span-all`.

[`span-left`, `span-right`, `span-top`, or `span-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-left_2)

The other value defaults to [`span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-all_2)
. For example, `span-left` is equivalent to `span-left span-all`.

[`center` or `span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#center)

The other value defaults to the same as the first value. For example, `center` is equivalent to `center center` and `span-all` is equivalent to `span-all span-all`.

[Logical grid keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#logical_grid_keywords)

-------------------------------------------------------------------------------------------------------------------------------------

The logical grid keywords specify an area of the position area grid using logical values. With these values, the position and direction are affected by [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 and [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 settings on either the element's [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 or, in the case of the `self` keywords, the positioned element itself. There are two types of logical keywords; generic and explicit.

### [Generic logical row and column keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#generic_logical_row_and_column_keywords)

The generic logical keywords use the same terms for the inline and block directions, with the direction determined by the position of the keyterm within a pair of `<position-area>` values. The first value defines the block direction position and the second value defines the inline value. You can specify one or two keyterms from the following list. Specifying two from this list defines a single specific grid tile. The keyword position or direction is:

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#start)

The start of the grid's block or inline direction, calculated from the containing block's writing mode.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#end)

The end of the grid's block or inline direction, calculated from the containing block's writing mode.

[`self-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#self-start)

The start of the grid's block or inline direction, calculated from the element's own writing mode.

[`self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#self-end)

The end of the grid's block or inline direction, calculated from the element's own writing mode.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#center_2)

The center of the grid's block direction (if this keyword is specified first) or inline direction (if this keyword is specified second).

For example, `start end` and `self-start self-end` both describe the position at the start of the block direction and the end of the inline direction. With `writing-mode: horizontal-tb` set, this is the top right of the anchor element, whereas with `writing-mode: vertical-rl` it is the bottom right of the anchor.

#### Generic logical spanning row and column keywords

The generic logical spanning keywords — when combined with a logical row or column keyword — specify a second grid tile for the position area to expand into. When such a combination is set as a `position-area` property value, a selected element is initially placed in the center of the specified row or column, and it then spans in the direction specified in the spanning keyword, spanning two grid tiles:

[`span-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-start)

Span the center tile and the start tile of the grid row/column, with the direction referring to the writing mode of the element's containing block.

[`span-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-end)

Span the center tile and the end tile of the grid row/column, with the direction referring to the writing mode of the element's containing block.

[`span-self-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-self-start)

Span the center tile and the start tile of the grid row/column for the positioned element's own writing mode.

[`span-self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-self-end)

Span the center tile and the end tile of the grid row/column, calculated from the element's own writing mode.

For example, `start span-end` and `self-start span-self-end` both specify a grid position area that starts in the center of the start block row, and spans across the tiles in that row that sit in the inline center and end columns. With `writing-mode: horizontal-tb` set, this would span over the top center and top right of the anchor, whereas with `writing-mode: vertical-rl` set it would span the element over the right center and bottom right.

### [Explicit inline and block logical keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#explicit_inline_and_block_logical_keywords)

The explicit inline and block logical row and column keywords refer explicitly to a block (row) or inline (column) position. You can specify one keyword for the block direction and one for the inline direction to select a single specific grid tile. Unlike with generic logical keyword values, the keyword order doesn't matter. However, declaring two keywords in the same axis invalidates the value.

[`block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#block-start)

The start of the grid's block direction calculated from the containing block's writing mode.

[`block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#block-end)

The end of the grid's block direction calculated from the containing block's writing mode.

[`inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#inline-start)

The start of the grid's inline direction calculated from the containing block's writing mode.

[`inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#inline-end)

The end of the grid's inline direction calculated from the containing block's writing mode.

For example, `block-start inline-end` specifies the tile at the start of the block direction and the end of the inline direction. With `writing-mode: horizontal-tb` set, this would be the tile at the top-right of the anchor, whereas with `writing-mode: vertical-rl` set this would be the tile at the bottom-right.

**Note:** The specification defines `self` equivalents of these keywords — `block-self-start`, `block-self-end`, `inline-self-start`, and `inline-self-end`. However, these are not currently supported in any browser.

#### Explicit inline and block logical spanning keywords

The explicit logical spanning keywords — when combined with a logical row or column keyword — specify a second grid tile for the position area to expand into. When such a combination is set as a `position-area` property value, a selected element is initially placed in the center of the specified row or column, based on the containing block's writing mode, and it then spans in the direction specified in the spanning keyword, spanning two grid tiles:

[`span-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-block-start)

Span the center tile and the block-start tile of the specified inline column.

[`span-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-block-end)

Span the center tile and the block-end tile of the specified inline column.

[`span-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-inline-start)

Span the center tile and the inline-start tile of the specified block row.

[`span-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-inline-end)

Span the center tile and the inline-end tile of the specified block row.

For example, `block-end span-inline-start` selects the center tile of the end block row and spans across the tiles in that row that sit in the inline center and start columns. With `writing-mode: horizontal-tb` set, this would span the bottom-center and bottom-left grid tiles, whereas with `writing-mode: vertical-rl` set it would span the left-center and top-left grid tiles.

**Note:** The specification defines `self` equivalents of these keywords, for example — `span-self-block-start`, `span-self-block-end`, `span-self-inline-start`, and `span-self-inline-end`. However, these are not currently supported in any browser.

**Note:** Trying to pair a row or column keyword with an inappropriate spanning keyword will result in an invalid property value. For example, `block-end span-block-end` is invalid — you can't select the center block-end row and then try to span one tile further past the block end direction.

### [Logical grid keyword defaults](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#logical_grid_keyword_defaults)

If only a single logical `<position-area>` keyword is specified, the other value is implied as follows:

[`start`, `end`, `self-start`, or `self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#start_2)

The other value defaults to the same as the first value, selecting the grid cell at the start row and column, or the end row and column.

[`span-start`, `span-self-start`, `span-end`, `span-self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-start_2)

The other value defaults to the same as the first value. For example, `span-start` is equivalent to `span-start span-start`.

[`block-start`, `block-end`, `inline-start`, `inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#block-start_2)

The other value defaults to [`span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-all_2)
, spanning all three tiles of the column or row set. For example, `block-start` is equivalent to `block-start span-all`.

[`span-block-start`, `span-block-end`, `span-inline-start`, `span-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-block-start_2)

The other value defaults to [`span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-all_2)
. For example, `span-inline-start` is equivalent to `span-inline-start span-all`.

[Coordinate grid keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#coordinate_grid_keywords)

-------------------------------------------------------------------------------------------------------------------------------------------

These keywords specify the cells of the `position-area` grid using x- and y-coordinate values. Its position/direction will be affected by [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 and/or [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 settings on either an element's [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 or, in the case of the `self` keywords, the element itself.

However, the grid cells are defined according to physical axes rather than block/inline directions:

*   For `writing-mode: horizontal-tb` and `vertical-lr`, the x-axis runs left-to-right and the y-axis runs top-to-bottom.
*   For `writing-mode: horizontal-tb; direction: rtl` and `writing-mode: vertical-rl`, the x-axis runs right-to-left and the y-axis runs top-to-bottom.

With coordinate row and column keywords, you can specify one keyword from the x-axis and one from the y-axis to define a single specific grid tile.

The x-axis keywords include:

[`x-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#x-start)

The start tile along the grid's x-axis, calculated from the containing block's writing mode.

[`x-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#x-end)

The end tile along the grid's x-axis, calculated from the containing block's writing mode.

[`self-x-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#self-x-start)

The start tile along the grid's x-axis, calculated from the element's own writing mode.

[`self-x-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#self-x-end)

The end tile along the grid's x-axis, calculated from the element's own writing mode.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#center_3)

The center of the grid's x-axis, calculated from the element's own writing mode.

The y-axis keywords include:

[`y-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#y-start)

The start tile along the grid's y-axis, calculated from the containing block's writing mode.

[`y-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#y-end)

The end tile along the grid's y-axis, calculated from the containing block's writing mode.

[`self-y-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#self-y-start)

The start tile along the grid's y-axis, calculated from the element's own writing mode.

[`self-y-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#self-y-end)

The end tile along the grid's y-axis, calculated from the element's own writing mode.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#center_4)

The center of the grid's y-axis, calculated from the element's own writing mode.

For example, `x-end y-start` and `self-x-end self-y-start` both select the grid cell at end of the x-axis and the start of the y-axis. With `writing-mode: horizontal-tb` set, this would be the cell to the top right of the anchor, whereas with `writing-mode: vertical-rl` is at the top left.

### [Coordinate spanning keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#coordinate_spanning_keywords)

When combined with a coordinate row or column keyword, the coordinate-spanning keywords specify a second grid tile for the position area to expand into. When such a combination is set as a `position-area` property value, a selected element is initially placed in the center of the specified row or column, and it then spans in the direction specified in the spanning keyword, spanning two grid tiles:

[`span-x-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-x-start)

Span the center tile and the x-start tile of the specified y-axis row.

[`span-x-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-x-end)

Span the center tile and the x-end tile of the specified y-axis row.

[`span-y-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-y-start)

Span the center tile and the y-start tile of the specified x-axis column.

[`span-y-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-y-end)

Span the center tile and the y-end tile of the specified x-axis column.

For example, `y-end span-x-end` selects the tile at the center of the end y-row, and spans across the tiles in that row that sit in the x-center and x-end columns. With `writing-mode: horizontal-tb` set, the position grid area would span the grid tiles at the bottom-center and bottom-right, whereas with `writing-mode: vertical-rl` set it would span the bottom-center and bottom-left tiles.

**Note:** The specification doesn't define separate coordinate `self` spanning keywords, but these are not needed — the spanning keywords can be used with both coordinate row and column keywords.

### [Coordinate grid keyword defaults](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#coordinate_grid_keyword_defaults)

If only a single coordinate grid `<position-area>` keyword is specified, the other value is implied as follows:

[`x-start`, `self-x-start`, `x-end`, `self-x-end`, `y-start`, `self-y-start`, `y-end`, or `self-y-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#x-start_2)

The other value defaults to [`span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-all_2)
, selecting the grid tiles spanning all three tiles of the column or row it was initially placed in. For example, `x-start` is equivalent to `x-start span-all`.

[`span-x-start`, `span-x-end`, `span-y-start`, `span-y-end`, `span-self-x-start`, `span-self-x-end`, `span-self-y-end`, or `span-self-y-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-x-start_2)

The other value defaults to [`span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-all_2)
. For example, `span-x-start` is equivalent to `span-x-start span-all`.

[`span-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#span-all)

-------------------------------------------------------------------------------------------------------------

`span-all` is a special keyword usable with all of the row and column keywords listed in the sections above. When you specify two values — a row/column keyword and `span-all`, the element is placed in the specified row or column, and it then spans all of the tiles in that row or column.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#examples)

-----------------------------------------------------------------------------------------------------------

See the [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 property page.

For detailed information on anchor features and usage, see the [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 module and the [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
 guide.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Anchor Positioning Module Level 1  <br>\# position-area](https://drafts.csswg.org/css-anchor-position/#position-area) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
    
*   [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
    
*   [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
    
*   [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     function
*   [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
     guide
*   [Fallback options and conditional hiding for overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
     guide
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/position-area_value/index.md?plain=1 "Folder: en-us/web/css/reference/values/position-area_value (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fposition-area_value&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fposition-area_value%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fposition-area_value%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fposition-area_value%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc9f812354ae36bbafc6f6d9b0961f3b25f350f4c%0A*+Document+last+modified%3A+2026-09-14T09%3A54%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")