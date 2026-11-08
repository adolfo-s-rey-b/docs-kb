*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#mdn-search)
    

`fit-content()` CSS function
============================

The **`fit-content()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 clamps a given size to an available size according to the formula `min(maximum size, max(minimum size, argument))`.

It is distinct from the [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
 keyword, which takes no argument and sizes a box based on its content within the available space. Only `fit-content()` is valid in grid track sizing properties such as [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#try_it)

--------------------------------------------------------------------------------------------------------

    grid-template-columns: fit-content(8ch) fit-content(8ch) 1fr;
    

    grid-template-columns: fit-content(100px) fit-content(100px) 1fr;
    

    grid-template-columns: fit-content(40%) fit-content(40%) 1fr;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element">
          <div>One. This column has more text in it.</div>
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
      grid-gap: 10px;
      width: 250px;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      text-align: left;
    }
    

The function can be used as a track size in [CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 properties, where the maximum size is defined by `max-content` and the minimum size by `auto`, which is calculated similar to `auto` (i.e., [`minmax(auto, max-content)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)
), except that the track size is clamped at _argument_ if it is greater than the `auto` minimum.

See the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 page for more information on the `max-content` and `auto` keywords.

The `fit-content()` function can also be used as laid out box size for [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
, [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
, [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 and [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
, where the maximum and minimum sizes refer to the content size.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* <length> values */
    fit-content(200px)
    fit-content(5cm)
    fit-content(30vw)
    fit-content(100ch)
    
    /* <percentage> value */
    fit-content(40%)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

An absolute length.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A percentage relative to the available space in the given axis.

In grid properties it is relative to the inline size of the grid container in column tracks and to the block size of the grid container for row tracks. Otherwise it is relative to the available inline size or block size of the laid out box depending on the writing mode.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

<fit-content()> =   
  fit-content( <length-percentage> )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#examples)

------------------------------------------------------------------------------------------------------------

### [Sizing grid columns with fit-content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#sizing_grid_columns_with_fit-content)

#### HTML

html

    <div id="container">
      <div>Item as wide as the content.</div>
      <div>
        Item with more text in it. Because the contents of it are wider than the
        maximum width, it is clamped at 300 pixels.
      </div>
      <div>Flexible item</div>
    </div>
    

#### CSS

css

    #container {
      display: grid;
      grid-template-columns: fit-content(300px) fit-content(300px) 1fr;
      grid-gap: 5px;
      box-sizing: border-box;
      height: 200px;
      width: 100%;
      background-color: #8cffa0;
      padding: 10px;
    }
    
    #container > div {
      background-color: #8ca0ff;
      padding: 5px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2  <br>\# funcdef-grid-template-columns-fit-content](https://drafts.csswg.org/css-grid/#funcdef-grid-template-columns-fit-content) |
| [CSS Box Sizing Module Level 4  <br>\# funcdef-width-fit-content](https://drafts.csswg.org/css-sizing-4/#funcdef-width-fit-content) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

### [css.properties.grid-template-columns.fit-content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#css.properties.grid-template-columns.fit-content)

### [css.properties.width.fit-content\_function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#css.properties.width.fit-content_function)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function#see_also)

------------------------------------------------------------------------------------------------------------

*   [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
     keyterm
*   [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
     keyterm
*   [CSS box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
     module
*   [`grid-template`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template)
    
*   [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
    
*   [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
    
*   [`grid-template-areas`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas)
    
*   [`grid-auto-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-columns)
    
*   [`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
    
*   [`grid-auto-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow)
    
*   [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
     keyterm
*   [Line-based placement with CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement)
    
*   [Grid template areas: grid definition shorthands](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_template_areas#grid_definition_shorthands)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/fit-content_function/index.md?plain=1 "Folder: en-us/web/css/reference/values/fit-content_function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffit-content_function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffit-content_function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffit-content_function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffit-content_function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5e4520f9cd84f65d470ec57efef7a73bbe9fd686%0A*+Document+last+modified%3A+2026-07-03T05%3A31%3A05.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")