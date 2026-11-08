*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#mdn-search)
    

`grid-row-start` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`grid-row-start`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies a grid item's start position within the grid row by contributing a line, a span, or nothing (automatic) to its grid placement, thereby specifying the inline-start edge of its [grid area](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Areas)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#try_it)

------------------------------------------------------------------------------------------------------

    grid-row-start: auto;
    

    grid-row-start: 3;
    

    grid-row-start: -1;
    

    grid-row-start: span 2;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element">One</div>
        <div>Two</div>
        <div>Three</div>
      </div>
    </section>
    

    .example-container {
      border: 1px solid #c5c5c5;
      display: grid;
      grid-template-columns: 1fr 1.5fr 1fr;
      grid-template-rows: repeat(3, minmax(40px, auto));
      grid-gap: 10px;
      width: 200px;
    }
    
    .example-container > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    
    #example-element {
      background-color: rgb(255 0 200 / 0.2);
      border: 3px solid rebeccapurple;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    grid-row-start: auto;
    
    /* <custom-ident> values */
    grid-row-start: some-grid-area;
    
    /* <integer> + <custom-ident> values */
    grid-row-start: 2;
    grid-row-start: some-grid-area 4;
    
    /* span + <integer> + <custom-ident> values */
    grid-row-start: span 3;
    grid-row-start: span some-grid-area;
    grid-row-start: 5 some-grid-area span;
    
    /* Global values */
    grid-row-start: inherit;
    grid-row-start: initial;
    grid-row-start: revert;
    grid-row-start: revert-layer;
    grid-row-start: unset;
    

This property is specified as a single `<grid-line>` value. A `<grid-line>` value can be specified as:

*   either the `auto` keyword
*   or a `<custom-ident>` value
*   or an `<integer>` value
*   or both `<custom-ident>` and `<integer>`, separated by a space
*   or the keyword `span` together with either a `<custom-ident>` or an `<integer>` or both.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#auto)

Is a keyword indicating that the property contributes nothing to the grid item's placement, indicating auto-placement, an automatic span, or a default span of `1`.

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#custom-ident)

If there is a named line with the name '<custom-ident>-start', it contributes the first such line to the grid item's placement.

**Note:** Named grid areas automatically generate implicit named lines of this form, so specifying `grid-row-start: foo;` will choose the start edge of that named grid area (unless another line named `foo-start` was explicitly specified before it).

Otherwise, this is treated as if the integer `1` had been specified along with the `<custom-ident>`.

[`<integer> && <custom-ident>?`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#integer_custom-ident)

Contributes the nth grid line to the grid item's placement. If a negative integer is given, it instead counts in reverse, starting from the end edge of the explicit grid.

If a name is given as a <custom-ident>, only lines with that name are counted. If not enough lines with that name exist, all implicit grid lines are assumed to have that name for the purpose of finding this position.

An [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 value of `0` is invalid.

[`span && [ <integer> || <custom-ident> ]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#span_integer_custom-ident)

Contributes a grid span to the grid item's placement; such that the row start edge of the grid item's grid area is n lines from the end edge.

If a name is given as a <custom-ident>, only lines with that name are counted. If not enough lines with that name exist, all implicit grid lines on the side of the explicit grid, corresponding to the search direction, are assumed to have that name for the purpose of counting this span.

If the <integer> is omitted, it defaults to `1`. Negative integers or 0 are invalid.

The `<custom-ident>` cannot take the `span` and `auto` values.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | grid items and absolutely-positioned boxes whose containing block is a grid container |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

grid-row-start =   
  <grid-line>    
  
<grid-line> =   
  auto                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
                                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[-∞,-1\]> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <integer \[1,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 span [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[1,∞\]> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
     
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#examples)

----------------------------------------------------------------------------------------------------------

### [Setting row start for a grid item](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#setting_row_start_for_a_grid_item)

#### HTML

html

    <div class="wrapper">
      <div class="box1">One</div>
      <div class="box2">Two</div>
      <div class="box3">Three</div>
      <div class="box4">Four</div>
      <div class="box5">Five</div>
    </div>
    

#### CSS

css

    .wrapper {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-auto-rows: 100px;
    }
    
    .box1 {
      grid-column-start: 1;
      grid-column-end: 4;
      grid-row-start: 1;
      grid-row-end: 3;
    }
    
    .box2 {
      grid-column-start: 1;
      grid-row-start: 3;
      grid-row-end: 5;
    }
    

    * {
      box-sizing: border-box;
    }
    
    .wrapper {
      border: 2px solid #f76707;
      border-radius: 5px;
      background-color: #fff4e6;
    }
    
    .wrapper > div {
      border: 2px solid #ffa94d;
      border-radius: 5px;
      background-color: #ffd8a8;
      padding: 1em;
      color: #d9480f;
    }
    
    .nested {
      border: 2px solid #ffec99;
      border-radius: 5px;
      background-color: #fff9db;
      padding: 1em;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2  <br>\# line-placement](https://drafts.csswg.org/css-grid/#line-placement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start#see_also)

----------------------------------------------------------------------------------------------------------

*   [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
    
*   [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
    
*   [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
    
*   [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
    
*   [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
    
*   [Line-based placement with CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement)
    
*   Video: [Line-based placement](https://gridbyexample.com/video/series-line-based-placement/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/grid-row-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/grid-row-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-row-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-row-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-row-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-row-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")