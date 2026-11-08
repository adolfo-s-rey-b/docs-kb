*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#mdn-search)
    

`grid-auto-flow` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`grid-auto-flow`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls how the auto-placement algorithm works, specifying exactly how auto-placed items get flowed into the grid.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#try_it)

------------------------------------------------------------------------------------------------------

    grid-auto-flow: row;
    

    grid-auto-flow: column;
    

    grid-auto-flow: row dense;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element">
          <div>One</div>
          <div>Two</div>
          <div>Three</div>
          <div>Four</div>
          <div>Five</div>
        </div>
      </div>
    </section>
    

    #example-element {
      border: 1px solid #c5c5c5;
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      grid-template-rows: repeat(3, minmax(40px, auto));
      grid-gap: 10px;
      width: 220px;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    
    #example-element > div:nth-child(1) {
      grid-column: auto / span 2;
    }
    
    #example-element > div:nth-child(2) {
      grid-column: auto / span 2;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    grid-auto-flow: row;
    grid-auto-flow: column;
    grid-auto-flow: dense;
    grid-auto-flow: row dense;
    grid-auto-flow: column dense;
    
    /* Global values */
    grid-auto-flow: inherit;
    grid-auto-flow: initial;
    grid-auto-flow: revert;
    grid-auto-flow: revert-layer;
    grid-auto-flow: unset;
    

This property may take one of two forms:

*   a single keyword: one of `row`, `column`, or `dense`.
*   two keywords: `row dense` or `column dense`.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#values)

[`row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#row)

Items are placed by filling each row in turn, adding new rows as necessary. If neither `row` nor `column` is provided, `row` is assumed.

[`column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#column)

Items are placed by filling each column in turn, adding new columns as necessary.

[`dense`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#dense)

"dense" packing algorithm attempts to fill in holes earlier in the grid, if smaller items come up later. This may cause items to appear out-of-order, when doing so would fill in holes left by larger items.

If it is omitted, a "sparse" algorithm is used, where the placement algorithm only ever moves "forward" in the grid when placing items, never backtracking to fill holes. This ensures that all of the auto-placed items appear "in order", even if this leaves holes that could have been filled by later items.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `row` |
| Applies to | grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

grid-auto-flow =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 row [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 column [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  dense               

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#examples)

----------------------------------------------------------------------------------------------------------

### [Setting grid auto-placement](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#setting_grid_auto-placement)

#### HTML

html

    <div id="grid">
      <div id="item1"></div>
      <div id="item2"></div>
      <div id="item3"></div>
      <div id="item4"></div>
      <div id="item5"></div>
    </div>
    <select id="direction">
      <option value="column">column</option>
      <option value="row">row</option>
    </select>
    <input id="dense" type="checkbox" />
    <label for="dense">dense</label>
    

#### CSS

css

    #grid {
      height: 200px;
      width: 200px;
      display: grid;
      gap: 10px;
      grid-template: repeat(4, 1fr) / repeat(2, 1fr);
      grid-auto-flow: column; /* or 'row', 'row dense', 'column dense' */
    }
    
    #item1 {
      background-color: lime;
      grid-row-start: 3;
    }
    
    #item2 {
      background-color: yellow;
    }
    
    #item3 {
      background-color: blue;
    }
    
    #item4 {
      grid-column-start: 2;
      background-color: red;
    }
    
    #item5 {
      background-color: aqua;
    }
    

    function changeGridAutoFlow() {
      const grid = document.getElementById("grid");
      const direction = document.getElementById("direction");
      const dense = document.getElementById("dense");
      let gridAutoFlow = direction.value === "row" ? "row" : "column";
    
      if (dense.checked) {
        gridAutoFlow += " dense";
      }
    
      grid.style.gridAutoFlow = gridAutoFlow;
    }
    
    const selectElem = document.querySelector("select");
    const inputElem = document.querySelector("input");
    selectElem.addEventListener("change", changeGridAutoFlow);
    inputElem.addEventListener("change", changeGridAutoFlow);
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2  <br>\# grid-auto-flow-property](https://drafts.csswg.org/css-grid/#grid-auto-flow-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow#see_also)

----------------------------------------------------------------------------------------------------------

*   [`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
    
*   [`grid-auto-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-columns)
    
*   [`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid)
    
*   [Auto-placement in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Auto-placement)
    
*   Video: [Introducing grid auto-placement and order](https://gridbyexample.com/video/series-auto-placement-order/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/grid-auto-flow/index.md?plain=1 "Folder: en-us/web/css/reference/properties/grid-auto-flow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-auto-flow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-auto-flow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-auto-flow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-auto-flow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2f710bc43d966483d0204330b14f841b440a6b60%0A*+Document+last+modified%3A+2026-08-11T12%3A55%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")