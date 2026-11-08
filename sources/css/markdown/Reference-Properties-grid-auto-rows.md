*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#mdn-search)
    

`grid-auto-rows` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`grid-auto-rows`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the size of an implicitly-created grid row [track](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Tracks)
 or pattern of tracks.

If a grid item is positioned into a row that is not explicitly sized by [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
, implicit [grid](https://developer.mozilla.org/en-US/docs/Glossary/Grid)
 tracks are created to hold it. This can happen either by explicitly positioning into a row that is out of range, or by the auto-placement algorithm creating additional rows.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#try_it)

------------------------------------------------------------------------------------------------------

    grid-auto-rows: auto;
    

    grid-auto-rows: 50px;
    

    grid-auto-rows: min-content;
    

    grid-auto-rows: minmax(30px, auto);
    

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
      grid-template-columns: 1fr 1fr;
      grid-auto-rows: 40px;
      grid-gap: 10px;
      width: 220px;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      font-size: 22px;
    }
    
    #example-element div:last-child {
      font-size: 13px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    grid-auto-rows: min-content;
    grid-auto-rows: max-content;
    grid-auto-rows: auto;
    
    /* <length> values */
    grid-auto-rows: 100px;
    grid-auto-rows: 20cm;
    grid-auto-rows: 50vmax;
    
    /* <percentage> values */
    grid-auto-rows: 10%;
    grid-auto-rows: 33.3%;
    
    /* <flex> values */
    grid-auto-rows: 0.5fr;
    grid-auto-rows: 3fr;
    
    /* minmax() values */
    grid-auto-rows: minmax(100px, auto);
    grid-auto-rows: minmax(max-content, 2fr);
    grid-auto-rows: minmax(20%, 80vmax);
    
    /* fit-content() values */
    grid-auto-rows: fit-content(400px);
    grid-auto-rows: fit-content(5cm);
    grid-auto-rows: fit-content(20%);
    
    /* multiple track-size values */
    grid-auto-rows: min-content max-content auto;
    grid-auto-rows: 100px 150px 390px;
    grid-auto-rows: 10% 33.3%;
    grid-auto-rows: 0.5fr 3fr 1fr;
    grid-auto-rows: minmax(100px, auto) minmax(max-content, 2fr) minmax(20%, 80vmax);
    grid-auto-rows: 100px minmax(100px, auto) 10% 0.5fr fit-content(400px);
    
    /* Global values */
    grid-auto-rows: inherit;
    grid-auto-rows: initial;
    grid-auto-rows: revert;
    grid-auto-rows: revert-layer;
    grid-auto-rows: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Is a non-negative length.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Is a non-negative [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value relative to the block size of the grid container. If the block size of the grid container is indefinite, the percentage value is treated like `auto`.

[`<flex>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)

Is a non-negative dimension with the unit `fr` specifying the track's flex factor. Each `<flex>`\-sized track takes a share of the remaining space in proportion to its flex factor.

When appearing outside a `minmax()` notation, it implies an automatic minimum (i.e., `minmax(auto, <flex>)`).

[`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)

Is a keyword representing the largest maximal content contribution of the grid items occupying the grid track.

[`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)

Is a keyword representing the largest minimal content contribution of the grid items occupying the grid track.

[`minmax(min, max)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)

Is a functional notation that defines a size range greater than or equal to _min_ and less than or equal to _max_. If _max_ is smaller than _min_, then _max_ is ignored and the function is treated as _min_. As a maximum, a `<flex>` value sets the track's flex factor. As a minimum, it is treated as zero (or minimal content, if the grid container is sized under a minimal content constraint).

[`fit-content( [ <length> | <percentage> ] )`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)

Represents the formula `min(max-content, max(auto, argument))`, which is calculated similar to `auto` (i.e., `minmax(auto, max-content)`), except that the track size is clamped at _argument_ if it is greater than the `auto` minimum.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#auto)

As a maximum represents the largest [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
 size of the items in that track.

As a minimum represents the largest minimum size of items in that track (specified by the [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
/[`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
 of the items). This is often, though not always, the [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
 size.

If used outside of [`minmax()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)
 notation, `auto` represents the range between the minimum and maximum described above. This behaves similarly to `minmax(min-content,max-content)` in most cases.

**Note:** `auto` track sizes (and only `auto` track sizes) can be stretched by the [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 and [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 properties. Therefore by default, an `auto` sized track will take up any remaining space in the grid container.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to corresponding dimension of the content area |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

grid-auto-rows =   
  <track-size>[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    
  
<track-size> =   
  <track-breadth>                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  minmax( <inflexible-breadth> , <track-breadth> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fit-content( <length-percentage \[0,∞\]> )            
  
<track-breadth> =   
  <length-percentage \[0,∞\]>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<flex \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)
               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  min-content                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  max-content                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto                         
  
<inflexible-breadth> =   
  <length-percentage \[0,∞\]>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  min-content                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  max-content                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto                         
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#examples)

----------------------------------------------------------------------------------------------------------

### [Setting grid row size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#setting_grid_row_size)

#### HTML

html

    <div id="grid">
      <div id="item1"></div>
      <div id="item2"></div>
      <div id="item3"></div>
    </div>
    

#### CSS

css

    #grid {
      width: 200px;
      display: grid;
      grid-template-areas: "a a";
      gap: 10px;
      grid-auto-rows: 100px;
    }
    
    #grid > div {
      background-color: lime;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2  <br>\# auto-tracks](https://drafts.csswg.org/css-grid/#auto-tracks) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows#see_also)

----------------------------------------------------------------------------------------------------------

*   [`grid-auto-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-columns)
    
*   [`grid-auto-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow)
    
*   [`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid)
    
*   [Auto-placement in grid layout - sizing rows in the implicit grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Auto-placement#sizing_rows_in_the_implicit_grid)
    
*   Video: [Introducing grid auto-placement and order](https://gridbyexample.com/video/series-auto-placement-order/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/grid-auto-rows/index.md?plain=1 "Folder: en-us/web/css/reference/properties/grid-auto-rows (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-auto-rows&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-auto-rows%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-auto-rows%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-auto-rows%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")