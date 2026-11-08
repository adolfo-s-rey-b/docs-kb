*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#mdn-search)
    

`grid-area` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`grid-area`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property specifies a grid item's size and location within a [grid](https://developer.mozilla.org/en-US/docs/Glossary/Grid)
 by contributing a line, a span, or nothing (automatic) to its grid placement, thereby specifying the edges of its [grid area](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Areas)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#try_it)

-------------------------------------------------------------------------------------------------

If four `<grid-line>` values are specified, `grid-row-start` is set to the first value, `grid-column-start` is set to the second value, `grid-row-end` is set to the third value, and `grid-column-end` is set to the fourth value.

When `grid-column-end` is omitted, if `grid-column-start` is a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
, `grid-column-end` is set to that `<custom-ident>`; otherwise, it is set to `auto`.

When `grid-row-end` is omitted, if `grid-row-start` is a `<custom-ident>`, `grid-row-end` is set to that `<custom-ident>`; otherwise, it is set to `auto`.

When `grid-column-start` is omitted, if `grid-row-start` is a `<custom-ident>`, all four longhands are set to that value. Otherwise, it is set to `auto`.

The `grid-area` property can also be set to a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 which acts as a name for the area, which can then be placed using [`grid-template-areas`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas)
.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
    
*   [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
    
*   [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
    
*   [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#syntax)

-------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#auto)

Is a keyword indicating that the property contributes nothing to the grid item's placement, indicating auto-placement or a default span of `1`.

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#custom-ident)

If there is a named line with the name `<custom-ident>-start` or `<custom-ident>-end`, it contributes the first such line to the grid item's placement.

**Note:** Named grid areas automatically generate implicit named lines of this form, so specifying `grid-area: foo;` will choose the start/end edge of that named grid area (unless another line named `foo-start`/`foo-end` was explicitly specified before it).

Otherwise, this is treated as if the integer `1` had been specified along with the `<custom-ident>`.

[`<integer> && <custom-ident>?`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#integer_custom-ident)

Contributes the n-th grid line to the grid item's placement. If a negative integer is given, it instead counts in reverse, starting from the end edge of the explicit grid.

If a name is given as a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
, only lines with that name are counted. If not enough lines with that name exist, all implicit grid lines are assumed to have that name for the purpose of finding this position.

An [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 value of `0` is invalid.

[`span && [ <integer> || <custom-ident> ]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#span_integer_custom-ident)

Contributes a grid span to the grid item's placement such that the corresponding edge of the grid item's grid area is _n_ lines from the opposite edge.

If a name is given as a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
, only lines with that name are counted. If not enough lines with that name exist, all implicit grid lines on the side of the explicit grid corresponding to the search direction are assumed to have that name for the purpose of counting this span.

If the [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 is omitted, it defaults to `1`. Negative integers or 0 are invalid.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)<br>    : `auto`<br>*   [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)<br>    : `auto`<br>*   [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)<br>    : `auto`<br>*   [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)<br>    : `auto` |
| Applies to | grid items and absolutely-positioned boxes whose containing block is a grid container |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)<br>    : as specified<br>*   [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)<br>    : as specified<br>*   [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)<br>    : as specified<br>*   [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#formal_syntax)

---------------------------------------------------------------------------------------------------------------

grid-area =   
  <grid-line> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <grid-line> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{0,3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#examples)

-----------------------------------------------------------------------------------------------------

### [Setting grid areas](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#setting_grid_areas)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2  <br>\# propdef-grid-area](https://drafts.csswg.org/css-grid/#propdef-grid-area) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area#see_also)

-----------------------------------------------------------------------------------------------------

*   [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
    
*   [`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
    
*   [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
    
*   [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
    
*   [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
    
*   [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
    
*   [`grid-template-areas`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas)
    
*   [Grid template areas](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_template_areas)
    
*   Video: [Grid template areas](https://gridbyexample.com/video/grid-template-areas/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/grid-area/index.md?plain=1 "Folder: en-us/web/css/reference/properties/grid-area (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-area&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-area%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fgrid-area%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fgrid-area%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")