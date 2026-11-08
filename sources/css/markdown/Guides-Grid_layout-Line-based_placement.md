*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#mdn-search)
    

Grid layout using line-based placement
======================================

In the [basic concepts of grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts)
 guide, we took a brief look at positioning items on a grid using line numbers. In this guide, we will fully explore how this fundamental feature of the specification works.

Starting your exploration of grid with numbered lines is the most logical place to begin because when you use grid layout, you always have numbered lines. The lines are numbered for columns and rows, and are indexed from `1`. Note that grid is indexed according to the writing mode of the document. In a left-to-right language, such as English, line 1 is on the left-hand side of the grid. If you are working in a right-to-left language, such as Arabic, then line 1 will be on the right-hand of the grid. We will learn more about the interaction between writing modes and grids in the [grids, logical values, and writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes)
 guide.

[A basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#a_basic_example)

----------------------------------------------------------------------------------------------------------------------------

As a basic example, we create a grid with 3 column tracks and 3 row tracks. This gives us 4 lines in each dimension.

Inside our grid container, we include four child elements.

If we do not place these onto the grid in any way, they will lay out according to the auto-placement rules, one item in each of the first four cells. You can inspect the grid with your browser developer tools to see how the grid defines columns and rows.

![The example grid highlighted in DevTools](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement/highlighted_grid.png)

[Positioning items by line number](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#positioning_items_by_line_number)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

We can use line-based placement to control where these items sit on the grid. We can use the [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
 and [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
 properties to make the first item start on the far left of the grid and span a single column track. With [`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
 and [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
, we make the item start on the first row line at the top of the grid, and span to the fourth row line.

css

    .box1 {
      grid-column-start: 1;
      grid-column-end: 2;
      grid-row-start: 1;
      grid-row-end: 4;
    }
    

As you position some items, other items on the grid will continue to be laid out using the auto-placement rules. This behavior is explained in the [Auto-placement in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Auto-placement)
 guide. For now, observe how the grid is laying out un-placed items into empty cells of the grid.

Addressing each item individually using the same properties but with different values, we place all four items, spanning row and column tracks.

    * {
      box-sizing: border-box;
    }
    
    .wrapper {
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
    }
    
    .wrapper > div {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      padding: 1em;
      color: #d9480f;
    }
    

html

    <div class="wrapper">
      <div class="box1">One</div>
      <div class="box2">Two</div>
      <div class="box3">Three</div>
      <div class="box4">Four</div>
    </div>
    

css

    .box1 {
      grid-column-start: 1;
      grid-column-end: 2;
      grid-row-start: 1;
      grid-row-end: 4;
    }
    .box2 {
      grid-column-start: 3;
      grid-column-end: 4;
      grid-row-start: 1;
      grid-row-end: 3;
    }
    .box3 {
      grid-column-start: 2;
      grid-column-end: 3;
      grid-row-start: 1;
      grid-row-end: 2;
    }
    .box4 {
      grid-column-start: 2;
      grid-column-end: 4;
      grid-row-start: 3;
      grid-row-end: 4;
    }
    

Note that we can leave cells empty if we wish. One of the very nice things about grid layout is the ability to have white space in our designs without any hacks.

[The `grid-column` and `grid-row` shorthands](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#the_grid-column_and_grid-row_shorthands)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The previous example had quite a lot of code to position each item. It should come as no surprise to know there is a [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
. The [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
 and [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
 properties can be combined into [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
, [`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
 and [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
 into [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
. In this example, we replicate the above example using these shorthand properties:

    * {
      box-sizing: border-box;
    }
    
    .wrapper {
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
    }
    
    .wrapper > div {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      padding: 1em;
      color: #d9480f;
    }
    

html

    <div class="wrapper">
      <div class="box1">One</div>
      <div class="box2">Two</div>
      <div class="box3">Three</div>
      <div class="box4">Four</div>
    </div>
    

css

    .box1 {
      grid-column: 1 / 2;
      grid-row: 1 / 4;
    }
    .box2 {
      grid-column: 3 / 4;
      grid-row: 1 / 3;
    }
    .box3 {
      grid-column: 2 / 3;
      grid-row: 1 / 2;
    }
    .box4 {
      grid-column: 2 / 4;
      grid-row: 3 / 4;
    }
    

[Default spans](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#default_spans)

------------------------------------------------------------------------------------------------------------------------

In the above examples, we specified every end row and column line, in order to demonstrate the properties, however in practice if an item only spans one track you can omit the `grid-column-end` or `grid-row-end` value. Grid defaults to spanning one track.

### [Default spans with longhand placement](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#default_spans_with_longhand_placement)

This means that our initial, long-hand, example would look like this:

    * {
      box-sizing: border-box;
    }
    
    .wrapper {
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
    }
    
    .wrapper > div {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      padding: 1em;
      color: #d9480f;
    }
    

html

    <div class="wrapper">
      <div class="box1">One</div>
      <div class="box2">Two</div>
      <div class="box3">Three</div>
      <div class="box4">Four</div>
    </div>
    

css

    .box1 {
      grid-column-start: 1;
      grid-row-start: 1;
      grid-row-end: 4;
    }
    .box2 {
      grid-column-start: 3;
      grid-row-start: 1;
      grid-row-end: 3;
    }
    .box3 {
      grid-column-start: 2;
      grid-row-start: 1;
    }
    .box4 {
      grid-column-start: 2;
      grid-column-end: 4;
      grid-row-start: 3;
    }
    

### [Default spans with shorthand placement](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#default_spans_with_shorthand_placement)

Our shorthand would look like the following code, with no forward slash and second value for the items spanning one track only.

    * {
      box-sizing: border-box;
    }
    
    .wrapper {
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
    }
    
    .wrapper > div {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      padding: 1em;
      color: #d9480f;
    }
    

html

    <div class="wrapper">
      <div class="box1">One</div>
      <div class="box2">Two</div>
      <div class="box3">Three</div>
      <div class="box4">Four</div>
    </div>
    

css

    .box1 {
      grid-column: 1;
      grid-row: 1 / 4;
    }
    .box2 {
      grid-column: 3;
      grid-row: 1 / 3;
    }
    .box3 {
      grid-column: 2;
      grid-row: 1;
    }
    .box4 {
      grid-column: 2 / 4;
      grid-row: 3;
    }
    

[The `grid-area` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#the_grid-area_property)

--------------------------------------------------------------------------------------------------------------------------------------------

We can take things a step further and define each area with a single property – [`grid-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area)
. The order of the values for `grid-area` is as follows.

– [`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
 – [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
 – [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
 – [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)

    * {
      box-sizing: border-box;
    }
    
    .wrapper {
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
    }
    
    .wrapper > div {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      padding: 1em;
      color: #d9480f;
    }
    

html

    <div class="wrapper">
      <div class="box1">One</div>
      <div class="box2">Two</div>
      <div class="box3">Three</div>
      <div class="box4">Four</div>
    </div>
    

css

    .box1 {
      grid-area: 1 / 1 / 4 / 2;
    }
    .box2 {
      grid-area: 1 / 3 / 3 / 4;
    }
    .box3 {
      grid-area: 1 / 2 / 2 / 3;
    }
    .box4 {
      grid-area: 3 / 2 / 4 / 4;
    }
    

This order of values for `grid-area` can seem a little strange — it is the opposite of the direction in which we specify margins and padding as a shorthand, for example. It may help to realize that this is due to CSS grid layout using the flow-relative directions defined in [CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
. We explore how grids work with writing modes in [grids, logical values, and writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes)
. For now, consider the concept of four [flow-relative](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values)
 directions:

*   `block-start`
*   `block-end`
*   `inline-start`
*   `inline-end`

We are working in English, a left-to-right language. Our `block-start` is the top row line of the grid container, `block-end` is the final row line of the container. Our `inline-start` is the left-hand column line as `inline-start` is always the point from which text would be written in the current writing mode, while `inline-end` is the final column line of our grid.

When we specify our grid area using the `grid-area` property we first define both start lines `block-start` and `inline-start`, then both end lines `block-end` and `inline-end`. This seems unusual at first as we are used to the [physical properties](https://developer.mozilla.org/en-US/docs/Glossary/Physical_properties)
 of `top`, `right`, `bottom`, and `left`, but it makes more sense if you start to think of websites as being multi-directional in different writing modes.

[Counting backwards](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#counting_backwards)

----------------------------------------------------------------------------------------------------------------------------------

We can also count backwards from the block and inline ends of the grid, for English that would be the right-hand column line and final row line. The last lines of the explicit grid can be addressed as `-1`, and you can count back from there – so the second to last line is `-2`.

Do note that negative values are relevant only to the explicit grid. The final line is the final line of the grid defined by `grid-template-columns` and `grid-template-rows`, and does not take into account any rows or columns added in the _implicit grid_ outside of that.

In this next example, we have flipped the layout we were working with by working from the right and bottom of our grid when placing the items.

    * {
      box-sizing: border-box;
    }
    
    .wrapper {
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
    }
    
    .wrapper > div {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      padding: 1em;
      color: #d9480f;
    }
    

html

    <div class="wrapper">
      <div class="box1">One</div>
      <div class="box2">Two</div>
      <div class="box3">Three</div>
      <div class="box4">Four</div>
    </div>
    

css

    .box1 {
      grid-column-start: -1;
      grid-column-end: -2;
      grid-row-start: -1;
      grid-row-end: -4;
    }
    .box2 {
      grid-column-start: -3;
      grid-column-end: -4;
      grid-row-start: -1;
      grid-row-end: -3;
    }
    .box3 {
      grid-column-start: -2;
      grid-column-end: -3;
      grid-row-start: -1;
      grid-row-end: -2;
    }
    .box4 {
      grid-column-start: -2;
      grid-column-end: -4;
      grid-row-start: -3;
      grid-row-end: -4;
    }
    

### [Stretching an item across the grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#stretching_an_item_across_the_grid)

Being able to address the start and end lines of the grid is useful as you can then stretch an item right across the grid with:

css

    .item {
      grid-column: 1 / -1;
    }
    

[Gutters or Alleys](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#gutters_or_alleys)

--------------------------------------------------------------------------------------------------------------------------------

CSS grid includes the ability to add gutters between column and row tracks with the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 and [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 properties, or [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 shorthand.

Gaps only appear between tracks of the grid, they do not add space to the top and bottom, left or right of the container. We can add gaps to our earlier example by using these properties on the grid container.

    * {
      box-sizing: border-box;
    }
    
    .wrapper {
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
    }
    
    .wrapper > div {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      padding: 1em;
      color: #d9480f;
    }
    

html

    <div class="wrapper">
      <div class="box1">One</div>
      <div class="box2">Two</div>
      <div class="box3">Three</div>
      <div class="box4">Four</div>
    </div>
    

css

    .box1 {
      grid-column: 1;
      grid-row: 1 / 4;
    }
    .box2 {
      grid-column: 3;
      grid-row: 1 / 3;
    }
    .box3 {
      grid-column: 2;
      grid-row: 1;
    }
    .box4 {
      grid-column: 2 / 4;
      grid-row: 3;
    }
    .wrapper {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
      column-gap: 20px;
      row-gap: 1em;
    }
    

### [The gap shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#the_gap_shorthand)

The two properties can also be expressed as a shorthand, [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
. If you only give one value for `gap` it will apply to both column and row gaps. If you specify two values, the first is used for `row-gap` and the second for `column-gap`.

css

    .wrapper {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
      gap: 1em 20px;
    }
    

In terms of line-based positioning of items, the gap acts as if the line has gained extra width. Anything starting at that line starts after the gap and you cannot address the gap or place anything into it. If you want gutters that act more like regular tracks you can define a track for that purpose.

[Using the `span` keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement#using_the_span_keyword)

--------------------------------------------------------------------------------------------------------------------------------------------

In addition to specifying the start and end lines by number, you can specify a start line and then the number of tracks you would like the area to span using the `span` keyword.

    * {
      box-sizing: border-box;
    }
    
    .wrapper {
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 100px);
    }
    
    .wrapper > div {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      padding: 1em;
      color: #d9480f;
    }
    

html

    <div class="wrapper">
      <div class="box1">One</div>
      <div class="box2">Two</div>
      <div class="box3">Three</div>
      <div class="box4">Four</div>
    </div>
    

css

    .box1 {
      grid-column: 1;
      grid-row: 1 / span 3;
    }
    .box2 {
      grid-column: 3;
      grid-row: 1 / span 2;
    }
    .box3 {
      grid-column: 2;
      grid-row: 1;
    }
    .box4 {
      grid-column: 2 / span 2;
      grid-row: 3;
    }
    

You can also use the `span` keyword in the value of `grid-row-start`/`grid-row-end` and `grid-column-start/grid-column-end`. The following two examples will create the same grid area. In the first we set the start row line, then the end line we specify that we want the area to cover 3 tracks. The area will start at line 1 and end 3 lines from line 1; that is, the area will end at line 4.

css

    .box1 {
      grid-column-start: 1;
      grid-row-start: 1;
      grid-row-end: span 3;
    }
    

In the second example, we specify the end row line we want the item to finish at and then set the start line as `span 3`. This means the item will need to span upwards from the specified row line. The area will start at line 4 and span 3 lines to line 1.

css

    .box1 {
      grid-column-start: 1;
      grid-row-start: span 3;
      grid-row-end: 4;
    }
    

To become familiar with line based positioning in grid, try to build a few common layouts by placing items onto grids with varying numbers of columns. Remember that if you do not place all of the items, any leftover items will be placed according to auto-placement rules. This may result in the layout you want, but if something is appearing somewhere unexpected, check that you have set a position for it.

Also, remember that items on the grid can overlap when you place them explicitly like this. Overlapping items can create some nice effects, however, you can also end up with incorrect overlapping if you specify the wrong start or end line. Inspecting grids with your browser developer tools can be very helpful for identifying such problems as you learn, especially if your grid is quite complicated.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/grid_layout/line-based_placement/index.md?plain=1 "Folder: en-us/web/css/guides/grid_layout/line-based_placement (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGrid_layout%2FLine-based_placement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fgrid_layout%2Fline-based_placement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGrid_layout%2FLine-based_placement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fgrid_layout%2Fline-based_placement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")