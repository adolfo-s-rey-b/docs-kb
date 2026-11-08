*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#mdn-search)
    

`justify-content` CSS property
==============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 **`justify-content`** property defines how the browser distributes space between and around content items along the [main axis](https://developer.mozilla.org/en-US/docs/Glossary/Main_Axis)
 of a flex container and the [inline axis](https://developer.mozilla.org/en-US/docs/Glossary/Logical_properties#inline_direction)
 of grid and multicol containers.

The interactive example below demonstrates some `justify-content` values using grid layout.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#try_it)

-------------------------------------------------------------------------------------------------------

    justify-content: start;
    

    justify-content: center;
    

    justify-content: space-between;
    

    justify-content: space-around;
    

    justify-content: space-evenly;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element">
          <div>One</div>
          <div>Two</div>
          <div>Three</div>
        </div>
      </div>
    </section>
    

    #example-element {
      border: 1px solid #c5c5c5;
      width: 220px;
      display: grid;
      grid-template-columns: 60px 60px;
      grid-auto-rows: 40px;
      row-gap: 10px;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Positional alignment */
    justify-content: center;
    justify-content: start;
    justify-content: end;
    justify-content: flex-start;
    justify-content: flex-end;
    justify-content: left;
    justify-content: right;
    
    /* Normal alignment */
    justify-content: normal;
    
    /* Distributed alignment */
    justify-content: space-between;
    justify-content: space-around;
    justify-content: space-evenly;
    justify-content: stretch;
    
    /* Overflow alignment (for positional alignment only)*/
    justify-content: safe center;
    justify-content: unsafe center;
    
    /* Global values */
    justify-content: inherit;
    justify-content: initial;
    justify-content: revert;
    justify-content: revert-layer;
    justify-content: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#values)

This property is specified as one of the following keyword values:

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#start)

The items are packed flush to each other toward the start edge of the alignment container in the main axis.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#end)

The items are packed flush to each other toward the end edge of the alignment container in the main axis.

[`flex-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#flex-start)

The items are packed flush to each other toward the start edge of the alignment container on the flex container's main-start side. This only applies to flex layout items. For items that are not children of a flex container, this value is treated like `start`.

[`flex-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#flex-end)

The items are packed flush to each other at the end edge of the alignment container on the flex container's main-end side. This only applies to flex layout items. For items that are not children of a flex container, this value is treated like `end`.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#center)

The items are packed flush to each other toward the center of the alignment container along the main axis.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#left)

The items are packed flush to each other toward the left edge of the alignment container. When the property's horizontal axis is not parallel with the inline axis, such as when [`flex-direction: column;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 is set, this value behaves like `start`.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#right)

The items are packed flush to each other toward the right edge of the alignment container in the appropriate axis. If the property's axis is not parallel with the inline axis (in a grid container) or the main-axis (in a flexbox container), this value behaves like `start`.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#normal)

Behaves as `stretch`, except in the case of multi-column containers with a non-`auto` [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
, in which case the columns take their specified `column-width` rather than stretching to fill the container. As `stretch` behaves as `start` in flex containers, `normal` also behaves as `start`.

[`space-between`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#space-between)

The items are evenly distributed within the alignment container along the main axis. The spacing between each pair of adjacent items is the same. The first item is flush with the main-start edge, and the last item is flush with the main-end edge.

[`space-around`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#space-around)

The items are evenly distributed within the alignment container along the main axis. The spacing between each pair of adjacent items is the same. The empty space before the first and after the last item equals half of the space between each pair of adjacent items. If there is only one item, it will be centered.

[`space-evenly`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#space-evenly)

The items are evenly distributed within the alignment container along the main axis. The spacing between each pair of adjacent items, the main-start edge and the first item, and the main-end edge and the last item, are all exactly the same.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#stretch)

If the combined size of the items along the main axis is less than the size of the alignment container, any `auto`\-sized items have their size increased equally (not proportionally), while still respecting the constraints imposed by [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
/[`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 (or equivalent functionality), so that the combined size exactly fills the alignment container along the main axis.

**Note:** For [flexboxes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
, the `stretch` value behaves as `flex-start` or `start`. This is because, in flexboxes, stretching is controlled using the [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
 property.

[`safe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#safe)

If the item overflows the alignment container, then the item is aligned as if the alignment mode is `start`. The desired alignment will not be implemented.

[`unsafe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#unsafe)

Even if the item overflows the alignment container, the desired alignment will be implemented. Unlike `safe`, which will ignore the desired alignment in favor of preventing overflow.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#description)

-----------------------------------------------------------------------------------------------------------------

Defined in the [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
 module, `justify-content` applies to multicol containers, flex containers, and grid containers. The property does not apply to and has no effect on block containers.

This property shares many keyword values with the [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 property, but not all! `justify-content` isn't involved in baseline alignment, and therefore does not take baseline values.

In [flex layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, the property defines how positive free space is distributed between or around flex items along the main axis. This property impacts the space between elements in a line, not the space between lines. The alignment is done after the lengths and auto margins are applied, which means that when one or more flex items in a line have a [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
 factor greater than `0`, the property has no effect as there is no space to distribute along that line. Also, as stretching along the main axis is controlled by [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
, the `stretch` value behaves as `flex-start`.

With [grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
, this property distributes available space between or around grid columns, not grid items. If the grid container is larger than the grid itself, the `justify-content` property can be used to justify the grid along the inline axis, aligning the grid columns.

Grid `auto` track sizes (and only `auto` track sizes) can be stretched by the `align-content` and `justify-content` properties. Therefore by default, an `auto` sized track will take up any remaining space in the grid container. As the grid's inline size has to be less than the grid container's inline size for there to be space to distribute, the property has no effect in this case.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | flex containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

justify-content =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <content-distribution>                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <content-position> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
[<content-distribution>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution)
 =   
  space-between  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space-around   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space-evenly   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch          
  
[<overflow-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position)
 =   
  unsafe  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  safe      
  
[<content-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-position)
 =   
  center      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  start       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flow-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flow-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flex-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flex-end      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#examples)

-----------------------------------------------------------------------------------------------------------

### [Basic grid example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#basic_grid_example)

In this example, we have a grid that is narrower than its grid container, and we use `justify-content` to distribute the available space evenly around and between the grid columns.

#### HTML

The [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 container, our grid container to-be, has 16 nested [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
s that will become grid items.

html

    <section class="container">
      <div>A</div>
      <div>B</div>
      <div>C</div>
      <div>D</div>
      <div>E</div>
      <div>F</div>
      <div>G</div>
      <div>H</div>
      <div>I</div>
      <div>J</div>
      <div>K</div>
      <div>L</div>
      <div>M</div>
      <div>N</div>
      <div>O</div>
      <div>P</div>
    </section>
    

#### CSS

    .container {
      margin: 5px;
      border: 1px solid;
      box-sizing: border-box;
    }
    
    div {
      line-height: 2em;
      border: 1px solid;
      box-sizing: border-box;
      text-align: center;
    }
    

We set the container width to `500px` and specify three columns, each `80px` wide, meaning there is `260px` of available space to distribute between or around them. We then set `justify-content: space-evenly`, which means there will be `65px` of space before, between, and after each column.

We set different widths (and background colors) to demonstrate how the justification is applied to the columns.

css

    .container {
      display: grid;
      grid: auto-flow / repeat(3, 80px);
      width: 500px;
      justify-content: space-evenly;
    }
    
    div {
      background-color: pink;
      width: 80px;
    }
    
    div:nth-of-type(n + 9) {
      width: 35px;
      background-color: lightgreen;
    }
    
    div:nth-last-of-type(3) {
      width: 250px;
      background-color: lightblue;
    }
    

#### Result

Note that `justify-contents` aligns the columns and has no effect on the items or alignment in grid areas. Grid items, even those that overflow their grid cell, do not impact column justification.

### [The safe keyterm](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#the_safe_keyterm)

This example demonstrates the `safe` keyterm. We specify four centered flex items that are not allowed to wrap, and as a result, overflow their single flex-line container. By adding `safe` to `center` in the `justify-content` property, overflowing content behaves as if the alignment mode is `start`

    <p><code>justify-content: center;</code></p>
    <section class="container safe">
      <div>A</div>
      <div>B</div>
      <div>C</div>
      <div>D</div>
    </section>
    <p><code>justify-content: safe center;</code></p>
    <section class="container safe-center">
      <div>A</div>
      <div>B</div>
      <div>C</div>
      <div>D</div>
    </section>
    <p><code>justify-content: safe center;</code> with 3 items</p>
    <section class="container safe-center">
      <div>A</div>
      <div>B</div>
      <div>C</div>
    </section>
    

    .container {
      margin: 5px auto;
      border: 1px dashed;
      box-sizing: border-box;
      background-color: lightblue;
    }
    
    div {
      line-height: 1em;
      border: 1px solid;
      box-sizing: border-box;
      text-align: center;
      background-color: pink;
    }
    

The container is set to `center`, with every container other than the first having the `safe` keyword added:

css

    .container {
      align-items: baseline;
      display: flex;
      width: 350px;
      height: 2em;
    }
    
    .safe {
      justify-content: center;
    }
    
    .safe-center {
      justify-content: safe center;
    }
    
    div {
      flex: 0 0 100px;
    }
    

#### Result

As an item overflows the alignment container, with `safe` included the alignment mode behaves as `start` and the `center` alignment is not implemented. The `safe` keyterm has no effect if the items do not overflow the container.

### [Visualizing flex item distribution](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#visualizing_flex_item_distribution)

This example includes a multi-line wrapping flex layout. The second flex item has a positive flex growth factor, consuming all the available free space in the first flex line.

#### CSS

    #container {
      margin: 5px auto;
      border: 1px dashed black;
      box-sizing: border-box;
    }
    
    div {
      line-height: 2em;
      border: 1px solid;
      box-sizing: border-box;
      text-align: center;
    }
    

css

    #container {
      display: flex;
      flex-flow: row wrap;
      justify-content: space-between; /* Can be changed in the live sample */
      width: 510px;
    }
    
    div {
      line-height: 2em;
      flex: 0 0 120px;
      background-color: pink;
    }
    
    div:nth-of-type(2) {
      flex-grow: 1;
      background-color: yellow;
    }
    
    div:nth-of-type(n + 9) {
      flex: 0 0 35px;
      background-color: lightgreen;
    }
    div:last-of-type {
      flex: 0 0 300px;
      background-color: lightblue;
    }
    

    <section id="container">
      <div>A</div>
      <div>GROW</div>
      <div>C</div>
      <div>D</div>
      <div>E</div>
      <div>F</div>
      <div>G</div>
      <div>H</div>
      <div>I</div>
      <div>J</div>
      <div>K</div>
      <div>L</div>
      <div>M</div>
      <div>N</div>
      <div>O</div>
      <div>P</div>
    </section>
    <select id="justifyContent">
      <option value="start">start</option>
      <option value="end">end</option>
      <option value="flex-start">flex-start</option>
      <option value="flex-end">flex-end</option>
      <option value="center">center</option>
      <option value="left">left</option>
      <option value="right">right</option>
      <option value="space-between" selected>space-between</option>
      <option value="space-around">space-around</option>
      <option value="space-evenly">space-evenly</option>
      <option value="stretch">stretch</option>
    </select>
    

    const justifyContent = document.getElementById("justifyContent");
    justifyContent.addEventListener("change", (evt) => {
      document.getElementById("container").style.justifyContent = evt.target.value;
    });
    

#### Result

Select different keywords from the drop-down menu to visualize the different `justify-content` keyword values. Because an item on the first line can grow, there is no available space on that line for the `justify-content` property to distribute. With the `space-between` value, the first item on each line is flush with the main-start edge, and the last item is flush with the main-end edge. As a result, if a line has only one item, it will be aligned with the main-start edge (as seen in the last line). This is not the case for other `space-*` values, such as `space-evenly` and `space-around`, which center one-item flex-lines.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# align-justify-content](https://drafts.csswg.org/css-align/#align-justify-content) |
| [CSS Flexible Box Layout Module Level 1  <br>\# justify-content-property](https://drafts.csswg.org/css-flexbox/#justify-content-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/justify-content/index.md?plain=1 "Folder: en-us/web/css/reference/properties/justify-content (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fjustify-content&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fjustify-content%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fjustify-content%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fjustify-content%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")