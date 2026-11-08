*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#mdn-search)
    

`grid-template-areas` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`grid-template-areas`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies named [grid areas](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Areas)
, establishing the cells in the grid and assigning them names.

Those areas are not associated with any particular grid item, but can be referenced from the grid-placement properties [`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
, [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
, [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
, [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
, and their shorthands [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
, [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
, and [`grid-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#try_it)

-----------------------------------------------------------------------------------------------------------

    grid-template-areas:
      "a a a"
      "b c c"
      "b c c";
    

    grid-template-areas:
      "b b a"
      "b b c"
      "b b c";
    

    grid-template-areas:
      "a a ."
      "a a ."
      ". b c";
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element">
          <div>One (a)</div>
          <div>Two (b)</div>
          <div>Three (c)</div>
        </div>
      </div>
    </section>
    

    #example-element {
      border: 1px solid #c5c5c5;
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      grid-template-rows: repeat(3, minmax(40px, auto));
      grid-gap: 10px;
      width: 200px;
    }
    
    #example-element :nth-child(1) {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      grid-area: a;
    }
    
    #example-element :nth-child(2) {
      background-color: rgb(255 0 200 / 0.2);
      border: 3px solid rebeccapurple;
      grid-area: b;
    }
    
    #example-element :nth-child(3) {
      background-color: rgb(94 255 0 / 0.2);
      border: 3px solid green;
      grid-area: c;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    grid-template-areas: none;
    
    /* <string> values */
    grid-template-areas: "a b";
    grid-template-areas:
      "a b ."
      "a c d";
    
    /* Global values */
    grid-template-areas: inherit;
    grid-template-areas: initial;
    grid-template-areas: revert;
    grid-template-areas: revert-layer;
    grid-template-areas: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#none)

The grid container doesn't define any named grid areas.

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)

A row is created for every separate string listed, and a column is created for each cell in the string. Multiple cell tokens with the same name within and between rows create a single named grid area that spans the corresponding grid cells. Unless those cells form a rectangle, the declaration is invalid.

All the remaining unnamed areas in a grid can be referred using _null cell tokens_. A null cell token is a sequence of one or more `.` (U+002E FULL STOP) characters, e.g., `.`, `...`, or `.....` etc. A null cell token can be used to create empty spaces in the grid.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

grid-template-areas =   
  none       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#examples)

---------------------------------------------------------------------------------------------------------------

### [Specifying named grid areas](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#specifying_named_grid_areas)

#### HTML

html

    <div id="page">
      <header>Header</header>
      <nav>Navigation</nav>
      <main>Main area</main>
      <footer>Footer</footer>
    </div>
    

#### CSS

css

    #page {
      display: grid;
      width: 100%;
      height: 250px;
      grid-template-areas:
        "head head"
        "nav  main"
        ".  foot";
      grid-template-rows: 50px 1fr 30px;
      grid-template-columns: 150px 1fr;
    }
    
    #page > header {
      grid-area: head;
      background-color: #8ca0ff;
    }
    
    #page > nav {
      grid-area: nav;
      background-color: #ffa08c;
    }
    
    #page > main {
      grid-area: main;
      background-color: #ffff64;
    }
    
    #page > footer {
      grid-area: foot;
      background-color: #8cffa0;
    }
    

In the above code, a null token (`.`) was used to create an unnamed area in the grid container, which we used to create an empty space at the bottom left corner of the grid.

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2  <br>\# grid-template-areas-property](https://drafts.csswg.org/css-grid/#grid-template-areas-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
    
*   [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
    
*   [`grid-template`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template)
    
*   [Grid template areas](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_template_areas)
    
*   Video: [Grid template areas](https://gridbyexample.com/video/grid-template-areas/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/grid-template-areas/index.md?plain=1 "Folder: en-us/web/css/reference/properties/grid-template-areas (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-template-areas&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-template-areas%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-template-areas%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-template-areas%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")