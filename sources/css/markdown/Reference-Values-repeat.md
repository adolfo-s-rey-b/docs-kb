*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#mdn-search)
    

`repeat()` CSS function
=======================

The **`repeat()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 represents a repeated fragment of the [track list](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts)
 or [rule-line list](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
. It allows repeated patterns of columns, rows, and their gap decorations, to be written in a compact form.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#try_it)

------------------------------------------------------------------------------------------

This function can be used with the following features:

CSS grid properties:

*   [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
    
*   [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
    

CSS gap properties:

*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
    
*   [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
     shorthand
*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
*   [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    
*   [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
     shorthand
*   [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    
*   [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
    
*   [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
     shorthand
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
     shorthand
*   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
     shorthand
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#syntax)

------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#values)

The `repeat()` function takes two arguments: The first argument specifies [**repeat count**](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#repeat_count_values)
, and the second specifies the [**repeated values list**](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#repeated_values_list)
 (the list of values to be repeated).

#### Repeat count values

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

A positive integer greater than or equal to `1` specifying the number of times the feature list in the second parameter will be repeated.

[`auto-fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#auto-fill)

Specifies an auto repeater that repeats to fill a space. Resolves to the largest number of repetitions that does not cause overflow of a constrained (has a maximum size) content box. Otherwise, if the content box has a minimum size, the fewest number of repetitions that meets the minimum size. If there is neither a minimum nor a maximum size, resolves to `1`. When used with subgrid, the second parameter must be a list of line names.

[`auto-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#auto-fit)

Behaves as `auto-fill`, except that after placing grid items, any empty repeated tracks are collapsed.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#auto)

Specifies an auto repeater. Once the values from other components of the property value have been applied, the values from the second parameter are repeated as many times as needed, filling any missing values.

#### Repeated values list

A list from one of the following track list types. Whether the components of the list are comma- or space-separated, depends on which separator is expected for that property value list type.

[`<line-names>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#line-names)

To add line names to subgrids, each `<line-names>` is zero or more [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 values, space-separated and enclosed in square brackets, such as `[start header-start]`.

[`<track-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#track-size)

Each `<track-size>` is a positive [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
, a [`minmax()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)
 function with the first parameter being the keyword `min-content`, `max-content`, or `auto`, or a positive `<length-percentage>`, or a [`fit-content()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)
 function.

[`<fixed-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#fixed-size)

Each `<fixed-size>` is either a positive `<length-percentage>`, or a `minmax()` function whose first parameter is a positive `<length-percentage>` and whose second parameter is a non-negative dimension with the unit `fr` specifying the track's flex factor or the keyword `min-content`, `max-content`, or `auto`, or a `minmax()` function whose first parameter is a positive `<length-percentage>` or the keyword `min-content`, `max-content`, or `auto`, and whose second parameter is a positive `<length-percentage>`.

[`<value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#value)

For defining gap rules, each `<value>` is a value that would be accepted by the property in which the `repeat()` appears, such as a [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
, [`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
, [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
, or all three as a `<gap-rule>`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#description)

----------------------------------------------------------------------------------------------------

The `repeat()` function represents a repeated fragment within a comma- or space-separated values list, that allows a recurring pattern to be written in a more compact form that can be repeated a specified number of times or can be auto-repeated.

The generic form of the `repeat()` syntax is, approximately,

The first argument, the **repeat count**, specifies the number of repetitions. It defines the number of times the list of values defined in the second parameter should be repeated. It is specified either as an integer value of `1` or more or as the keyword `auto-fill`, `auto-fit`, or `auto`.

The second argument is a comma- or space-separated list of values that are valid for the property in which the `repeat()` appears. It specifies the **repeated value type**, which is generally the _tracks_ or _rule feature(s)_ to be repeated.

[**tracks**:](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#tracks)

Specifies the set of tracks that will be repeated. Fundamentally this consists of one or more space-separated values, where each value represents the size of that track. Each size is specified using either a [`<track-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#track-size)
 value or a [`<fixed-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#fixed-size)
 value. You can also specify one or more [line names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Named_grid_lines)
 before or after each track, by providing [`<line-names>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#line-names)
 values before and/or after the track size.

[**rule feature**:](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#rule_feature)

Specifies the rule feature that will be repeated. This is either a comma separated list of [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
, [`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
, or [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 values, or a comma-separated list of shorthand declarations setting the line's color, width, and style.

### [Syntax forms](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#syntax_forms)

The syntax of the `repeat()` function has several forms:

[`<track-repeat>` = `repeat( <integer>, [ <line-names>? <track-size> ]+ <line-names>? )`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#track-repeat)

The `<integer>` sets the repeat count.

The `<track-size>` values set the track size. A `<track-size>` is either a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
, a [`<flex>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)
 value (a positive `fr` unit value), or the keyword `min-content`, `max-content`, or `auto`, a [`fit-content()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)
 function with a `<length-percentage>` parameter, or a [`minmax()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)
 function. For `minmax()` track values, the `min` is either a `<length-percentage>`, or the `min-content`, `max-content`, or `auto` keyword while the `max` can be any of those, or a `<flex>` value.

Each `<track-size>` is optionally preceded by `<line-names>`, which are zero or more space-separated [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 values enclosed in square brackets.

An ending `<line-names>` is optional.

[`<auto-repeat>` = `repeat( auto-fill | auto-fit, [ <line-names>? <fixed-size> ]+ <line-names>? )`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#auto-repeat)

The `auto-fill` or `auto-fit` keyword sets the repeat count

The `<fixed-size>` sets the track size. A `<fixed-size>` is either a `<length-percentage>` value, or a `minmax()` function with either the `min` or the `max` being a `<length-percentage>` and the other value also being a `<length-percentage>`, or set to the keyword `min-content`, `max-content`, or `auto`.

Each `<fixed-size>` is optionally preceded by `<line-names>`.

The ending `<line-names>` is optional.

[`<fixed-repeat>` = `repeat( <integer>, [ <line-names>? <fixed-size> ]+ <line-names>? )`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#fixed-repeat)

Same as `<auto-repeat>`, except the `<integer>` sets the repeat count, so there is no auto-repeating.

[`<name-repeat>` = `repeat( [ <integer> | auto-fill ], <line-names>+)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#name-repeat)

The integer or `auto-fill` keyword sets the repeat count

The `<line-names>` are one or more space-separated [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 values enclosed in square brackets.

These line names (rather than track sizes) are relevant for [`subgrid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Subgrid)
.

[`<repeat-value-type>` = `repeat( <integer> , <value># )`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#repeat-value-type)

The `<integer>` sets the repeat count.

The `<value>` is one or more comma-separated valid values for the property on which the `repeat()` function is applied.

Multiple `repeat()` functions of the `<repeat-value-type>` may be used within a single value declaration.

[`<auto-repeat-value-type>` = `repeat( auto , <value># )`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#auto-repeat-value-type)

The `auto` keyword specifies an auto repeater. An auto repeater will be used to fill in values for gaps that would not otherwise receive values from other parts of the list.

The `<value>` is one or more comma-separated valid values for the property on which the `repeat()` function is applied.

At most one `repeat()` in a given list of values may be an auto repeater.

### [Auto-fit versus auto-fill](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#auto-fit_versus_auto-fill)

When the first parameter of the `repeat()` function is a keyword, either `auto-fill`, `auto-fit`, or `auto`, rather than an integer, it creates an auto-repeater. An auto-repeating `repeat()` function repeats the values provided as the second parameter as many times as necessary.

With `auto-fill`, if the container has a definite or maximum size set in the relevant axis, the number of repetitions is the largest possible positive integer that does not cause the content to overflow its container. Treating each track as its maximal track sizing function (each independent value used to define `grid-template-rows` or `grid-template-columns`), if that is definite. Otherwise, if there is no definite or maximum size defined, the `repeat()` function is a minimum track sizing function. If any number of repetitions would overflow, the repetition is `1`. Otherwise, if the grid container has a definite minimal size in the relevant axis, the number of repetitions is the smallest possible positive integer that fulfills that minimum requirement. Otherwise, the specified track list repeats only once.

The `auto-fit` value behaves the same as `auto-fill`, except that after placing the grid items any empty repeated tracks are collapsed. An empty track is one with no in-flow grid items placed into or spanning across it. (This can result in all tracks being collapsed, if they're all empty.)

A collapsed track is treated as having a single fixed track sizing function of `0px`, and the gutters on either side of it collapse.

For the purpose of finding the number of auto-repeated tracks, the user agent floors the track size to a user agent specified value (e.g., `1px`), to avoid dividing by zero.

### [Use exceptions and rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#use_exceptions_and_rules)

There are some rules and restrictions when using `repeat()`:

A property value can contain multiple `repeat()` functions.

A property value can contain, at most, one auto-repeat `repeat()` function.

If a property declaration uses `<auto-repeat>`, it is only allowed to use `<fixed-repeat>` for any additional `repeat()` calls. Automatic repetitions (`auto-fill` or `auto-fit`) cannot be combined with fully intrinsic or flexible sizes. For example, this is invalid, because it combines the `<auto-repeat>` form with the `<track-repeat>` form:

The `repeat()` notation cannot be nested within another `repeat()` function.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#formal_syntax)

--------------------------------------------------------------------------------------------------------

<track-repeat> =   
  repeat( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[1,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <line-names>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 <track-size> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
 <line-names>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<auto-repeat> =   
  repeat( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto-fill [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 auto-fit [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <line-names>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 <track-size> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
 <line-names>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<fixed-repeat> =   
  repeat( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[1,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <line-names>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 <fixed-size> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
 <line-names>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<name-repeat> =   
  repeat( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[1,∞\]> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 auto-fill [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , <line-names>[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
 )    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
<line-names> =   
  '\[' [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)\
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 '\]'    
  
<track-size> =   
  <track-breadth>                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  minmax( <inflexible-breadth> , <track-breadth> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fit-content( <length-percentage \[0,∞\]> )            
  
<fixed-size> =   
  <fixed-breadth>                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  minmax( <fixed-breadth> , <track-breadth> )       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  minmax( <inflexible-breadth> , <fixed-breadth> )    
  
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
    
  
<fixed-breadth> =   
  <length-percentage \[0,∞\]>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#examples)

----------------------------------------------------------------------------------------------

### [Specifying grid columns using repeat()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#specifying_grid_columns_using_repeat)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2  <br>\# repeat-notation](https://drafts.csswg.org/css-grid/#repeat-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

### [css.properties.grid-template-columns.repeat](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#css.properties.grid-template-columns.repeat)

### [css.properties.row-rule.repeat](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#css.properties.row-rule.repeat)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat#see_also)

----------------------------------------------------------------------------------------------

*   [`grid-template`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template)
    
*   [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
    
*   [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
    
*   [`grid-template-areas`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas)
    
*   [`grid-auto-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-columns)
    
*   [`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
    
*   [`grid-auto-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow)
    
*   [Line-based placement with CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Line-based_placement)
    
*   [Grid template areas: grid definition shorthands](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_template_areas#grid_definition_shorthands)
    
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/repeat/index.md?plain=1 "Folder: en-us/web/css/reference/values/repeat (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frepeat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frepeat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frepeat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frepeat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F870fe25a3e6ed1a44222c52dd8a992b731c1a383%0A*+Document+last+modified%3A+2026-09-07T10%3A45%3A10.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")