*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#mdn-search)
    

Defining CSS gaps
=================

When creating [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
, [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, and [multi-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
 layouts using [CSS gap properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#properties)
, you can define and control gaps between columns and rows.

While the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 and [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 properties specify visual spacing around individual boxes, using the [properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps#properties)
 in the CSS gaps module, you can specify spacing between adjacent boxes in layouts that have [gutters](https://developer.mozilla.org/en-US/docs/Glossary/Gutters)
 and gaps.

This guide explains column and row gaps in different layout types, how to define gaps, and how to use percentages as a `gap` value.

[Understanding gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#understanding_gaps)

--------------------------------------------------------------------------------------------------------------------

While margin and padding can specify spacing around individual boxes, it's sometimes more convenient to specify spacing between adjacent boxes within a given layout. This is particularly true when the spacing between sibling boxes differs from the spacing between the first or last box and the container's edge. The [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 property, and its [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 and [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 constituent properties, provide this functionality for grid, flexbox, and multi-column layouts.

A _gap_ is either a _column gap_ or a _row gap_. Their definitions vary by layout type. For all layout types, any gap disappears when it coincides with a fragmentation break.

### [Grid container gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#grid_container_gaps)

In the context of a grid container, _row gaps_ and _column gaps_ refer to the gutters between grid rows and grid columns, respectively. The width of the gaps makes the affected grid lines behave as though they acquired thickness: the grid track between two grid lines is the space between the gutters that represent them. By default, the width of the gap is `0` in both directions.

For the purpose of track sizing, each gutter is treated as an extra, empty, fixed-size track of the specified size. A grid item that spans multiple rows or columns also spans the gutters between them.

For example, if `gap: 20px` is set on a 4x4 grid of `100px` by `100px` boxes, the grid would be `460px` by `460px`. While each box is `100px` by `100px`, a grid item that spans two horizontal rows has a height of `220px`. If it spans three, its height is `340px`. If it spans all four, its height is `460px`.

Gutter gaps set the minimum spacing between items: additional spacing may be added by [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 and [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 property values, increasing the size of the corresponding gaps.

Gutters appear only between tracks of the implicit grid. If a grid is fragmented between tracks, no gutter spacing is added between those tracks. There is no gutter before the first track or after the last track. If a track is collapsed, it has no gutter.

### [Flex container gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#flex_container_gaps)

Flex containers are created by setting [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `flex` or `inline-flex` on an element containing multiple children. By default, flex items are laid out in a single, non-wrapping row. The default gap between adjacent flex items and, if wrapping, between adjacent columns or rows, is `0`. Whether a flex container with multiple items has columns, rows, or both depends on the flow and wrapping set using the [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 shorthand.

You can add gaps between adjacent flex items along the main axis. If the [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 property is set to `row wrap` or `row-reverse wrap`, _column gap_ refers to the gutter between adjacent flex items and _row gap_ refers to the gutter between flex rows. If `flex-flow` is set to `column wrap` or `column-reverse wrap`, _row gap_ refers to the gutter between adjacent flex items and _column gap_ refers to the gutter between flex rows.

### [Multi-column gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#multi-column_gaps)

Multi-col containers are block-level elements with more than one column created by setting the [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 to a value greater than `1`. By default, columns are laid out in a single row, with a `1em` wide _column gap_ between adjacent columns. The _row gap_ is the gutter between rows of column boxes established by setting a [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
 that requires columns to wrap, creating additional rows.

[Using the `gap` shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#using_the_gap_shorthand)

--------------------------------------------------------------------------------------------------------------------------------

The [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 property sets the size of the gap ([gutter](https://developer.mozilla.org/en-US/docs/Glossary/Gutters)
) between adjacent rows within a container. The [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 property sets the size between a container's columns. Each property value can be specified as a `<length>`, a `<percentage>`, or the keyword `normal`. Percentage values are calculated against the [content box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#content_area)
 size of the container element for that dimension.

The [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 shorthand defines gaps between both rows and columns and accepts one or two values. The default value is `normal` for both sub-properties. If only one value is declared, it applies to both row and column gaps. If two values are declared, the first sets the `row-gap` value and the second sets the `column-gap`.

The effect of the definition depends on whether the container uses grid, flexbox, or multi-column layout.

You can add visible separators to gaps; these are called gap decorations. If you add decorative rules for gaps between columns, rows, or both, they appear in the middle of their gap but have no effect on the size of the gap, nor do they affect the size of the container. These gap decorations are added to the otherwise "empty space" by using the [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 shorthand or its constituent properties.

### [Gaps in grid layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#gaps_in_grid_layouts)

In grid containers, the `gap` property defines the size of the gutters between vertical and horizontal tracks. The shorthand property is specified as a value for `<'row-gap'>`, followed optionally by a value for `<'column-gap'>`. If only one value is declared, it applies to both row and column gaps.

In this example, we create a grid container with seven columns:

css

    .container {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
    }
    

Select different `gap` values to see how they change the spacing between rows and columns:

    :has([value="a"]:checked) p {
      gap: 2px 10px;
    }
    :has([value="b"]:checked) p {
      gap: 10px 2px;
    }
    :has([value="c"]:checked) p {
      gap: 10px;
    }
    :has([value="d"]:checked) p {
      gap: 2px;
    }
    

### [Gaps in flexbox layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#gaps_in_flexbox_layouts)

In flex containers, the `gap` property defines the space between both flex items and flex lines. Whether the first value sets the gap between flex items or between flex lines depends on the direction in which the flex items are laid out.

Flex items are laid out in rows or columns depending on the value of the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 property. If set to `row` or `row-reverse`, the first value defines the gap between flex lines, and the second value defines the gap between adjacent flex items within each line. If only one value is included, it applies to both gaps.

If the `flex-direction` is set to `column` or `column-reverse`, the first value defines the gap between adjacent flex items within a flex line, and the second value defines the gaps between flex lines. Again, if only one value is included, it applies to both gaps.

In this example, we create a flex container and allow the flex items to wrap:

css

    .container {
      display: flex;
      flex-wrap: wrap;
      max-width: 300px;
      height: 500px;
    }
    

Select different `gap` and `flex-direction` values to see how they change the spacing between flex items and flex lines:

    i {
      flex: 0 0 18%;
    }
    i:nth-of-type(2n) {
      flex: 0 0 12%;
    }
    i:nth-of-type(3n) {
      flex: 0 0 26%;
    }
    i:nth-of-type(5n) {
      flex: 0 0 20%;
    }
    i:nth-of-type(7n) {
      flex: 0 0 34%;
    }
    

    :has([value="a"]:checked) p {
      gap: 2px 10px;
    }
    :has([value="b"]:checked) p {
      gap: 10px 2px;
    }
    :has([value="c"]:checked) p {
      gap: 10px;
    }
    :has([value="d"]:checked) p {
      gap: 2px;
    }
    
    :has([value="row"]:checked) p {
      flex-direction: row;
    }
    :has([value="rowR"]:checked) p {
      flex-direction: row-reverse;
    }
    :has([value="col"]:checked) p {
      flex-direction: column;
    }
    :has([value="colR"]:checked) p {
      flex-direction: column-reverse;
    }
    

    <fieldset>
      <legend>Select a flex direction:</legend>
      <label
        ><input type="radio" value="row" name="dir" /> flex-direction: row;</label
      >
      <label
        ><input type="radio" value="rowR" name="dir" /> flex-direction:
        row-reverse;</label
      >
      <label
        ><input type="radio" value="col" name="dir" /> flex-direction:
        column;</label
      >
      <label
        ><input type="radio" value="colR" name="dir" /> flex-direction:
        column-reverse;</label
      >
    </fieldset>
    

    <fieldset>
      <legend>Select a layout</legend>
      <label><input type="radio" value="grid" name="dir" checked />Grid</label>
      <label><input type="radio" value="flex" name="dir" />Flexbox</label>
      <label
        ><input type="radio" value="flex2" name="dir" />Flexbox (columns)</label
      >
      <label><input type="radio" value="multicol" name="dir" />Multi-col</label>
    </fieldset>
    

### [Gaps in multi-column layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#gaps_in_multi-column_layouts)

In [CSS multi-column layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
, the `gap` property defines the gutter between columns and between rows of columns. The first value defines the gap between rows of column boxes, if multiple rows are established by the [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
 property. The second value defines the gap between adjacent column boxes.

In this example, we create a multi-col container using the `columns` shorthand property, setting a maximum of seven columns and a minimum column width of `1em`. A column height of `2.35em` enables the creation of additional rows. We also add a thin decorative rule in the middle of the gap using the [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 property:

    .container {
      columns: 7 1em / 2.35em;
      width: 450px;
      rule: 1px solid #cccccc;
    }
    @supports not (column-height: 1em) {
      body::before {
        content: "Your browser does not support the column-height property.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

By default, there is a `1em` gap between rows and columns. Change this by selecting different `gap` values:

    :has([value="a"]:checked) p {
      gap: 0.5em 3em;
    }
    :has([value="b"]:checked) p {
      gap: 3em 0.5em;
    }
    :has([value="c"]:checked) p {
      gap: 0.5em;
    }
    :has([value="d"]:checked) p {
      gap: 3em;
    }
    

The gutters may appear larger than the specified gap size because the letters don't fill the allotted space. The decorative rule appears in the middle of the gap, either `0.25em` or `1.5em` from the block and inline starts of the column and row's content depending on the setting selected. The extra whitespace is at block- and inline-end, making the gaps look larger than they are.

    <fieldset>
      <legend>Select a gap value:</legend>
      <label><input type="radio" value="a" name="gap" /> gap: 2px 10px;</label>
      <label><input type="radio" value="b" name="gap" /> gap: 10px 2px;</label>
      <label><input type="radio" value="c" name="gap" /> gap: 10px;</label>
      <label><input type="radio" value="d" name="gap" /> gap: 2px;</label>
    </fieldset>
    

    <fieldset>
      <legend>Select a gap value:</legend>
      <label><input type="radio" value="a" name="gap" /> gap: 0.5em 3em;</label>
      <label><input type="radio" value="b" name="gap" /> gap: 3em 0.5em;</label>
      <label><input type="radio" value="c" name="gap" /> gap: 0.5em;</label>
      <label><input type="radio" value="d" name="gap" /> gap: 3em;</label>
    </fieldset>
    

    <fieldset>
      <legend>Select a gap value:</legend>
      <label><input type="radio" value="a" name="gap" /> gap: 1% 5%;</label>
      <label><input type="radio" value="b" name="gap" /> gap: 5% 1%;</label>
      <label><input type="radio" value="c" name="gap" /> gap: 1%;</label>
      <label><input type="radio" value="d" name="gap" /> gap: 5%;</label>
    </fieldset>
    

    <div>
      <p class="container">
        <i>A</i>
        <i>B</i>
        <i>C</i>
        <i>D</i>
        <i>E</i>
        <i>F</i>
        <i>G</i>
        <i>H</i>
        <i>I</i>
        <i>J</i>
        <i>K</i>
        <i>L</i>
        <i>M</i>
        <i>N</i>
        <i>O</i>
        <i>P</i>
        <i>Q</i>
        <i>R</i>
        <i>S</i>
        <i>T</i>
        <i>U</i>
        <i>V</i>
        <i>W</i>
        <i>X</i>
        <i>Y</i>
        <i>Z</i>
      </p>
    </div>
    

    .container {
      font-size: 2rem;
      font-family: monospace;
      font-weight: bold;
    }
    i {
      background-color: #cccccc;
      text-align: center;
    }
    label {
      display: block;
      font-family: monospace;
      margin: 10px;
    }
    

[Specifying gap values as percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#specifying_gap_values_as_percentages)

--------------------------------------------------------------------------------------------------------------------------------------------------------

When a container has a fixed size, column and row gaps specified as percentages are calculated relative to the width and height of the container, respectively.

In this example, the size of the container is set. Select different gap sizes as percentage values, and change the layout type to see how the gaps are calculated relative to the container's size. Column gaps of `1%` and `5%` are `3px` and `15px` wide, respectively. Row gaps of `1%` and `5%` are `6px` and `30px` tall, respectively. These gap sizes apply even if the contents overflow the container.

css

    .container {
      width: 300px;
      height: 600px;
      background-color: #eeeeee;
      rule: 1px dotted #666666;
    }
    

Note that if you set the `gap` property to a single percentage value, the row gap is twice the size of the column gap because the container is twice as tall as it is wide.

    fieldset {
      width: 44%;
      float: left;
    }
    p {
      clear: both;
      font-size: 1.25rem;
    }
    
    :has([value="a"]:checked) p {
      gap: 1% 5%;
    }
    :has([value="b"]:checked) p {
      gap: 5% 1%;
    }
    :has([value="c"]:checked) p {
      gap: 1%;
    }
    :has([value="d"]:checked) p {
      gap: 5%;
    }
    
    :has([value="grid"]:checked) p {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
    }
    :has([value="flex"]:checked) p {
      display: flex;
      flex-flow: row wrap;
    }
    :has([value="flex2"]:checked) p {
      display: flex;
      flex-flow: column wrap;
    }
    :has([value="multicol"]:checked) p {
      columns: 5 2em / 2.35em;
    }
    

If we don't have a defined height or width for the container, the behavior of percentage gap values is very different. If the container has a fixed width, percentage gap values are predictable. If the container is auto‑sized, percentage gaps could create a circular dependency: the gaps depend on the container's size, but the container's size depends on the gaps. Browsers treat percentage gap values as `auto` (effectively `0`) during intrinsic sizing.

css

    .container {
      background-color: #eeeeee;
      rule: 1px dotted #666666;
      height: auto;
      width: auto;
    }
    

In the example, the width of the container is constrained by the containing block, while the height is not.

As percentage values are treated as `auto` during intrinsic sizing for gaps in grid layout, the gap is collapsed until the size of the container is determined. This means the size of the container is determined based solely on the dimensions of the content. If the example renders six rows of grid cells, there will be five row gaps, meaning the last row of grid items will overflow the background by either `5%` or `25%`, depending on whether the gap is set to `1%` or `5%`.

In flexbox layouts, the percentage gaps are treated as `0` or ignored during intrinsic sizing. The gap is applied only after sizing. As the container's block size is `auto`, the percentage row gaps resolve against `0`; so `1%` or `5%` of `0` is `0`. Percentage values are effectively ignored - the `row-gap` is `0` for both flexbox and multi-col layouts.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#see_also)

------------------------------------------------------------------------------------------------

*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/gaps/defining_gaps/index.md?plain=1 "Folder: en-us/web/css/guides/gaps/defining_gaps (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGaps%2FDefining_gaps&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fgaps%2Fdefining_gaps%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGaps%2FDefining_gaps%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fgaps%2Fdefining_gaps%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")