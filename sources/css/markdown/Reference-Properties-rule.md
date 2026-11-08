*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#mdn-search)
    

`rule` CSS property
===================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#browser_compatibility)
 carefully before using this in production.

The **`rule`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the width, style, and color of the line drawn between rows and columns in multi-row grid, flex, and multi-col layouts, setting both the column and row rules to the same values.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#try_it)

--------------------------------------------------------------------------------------------

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
    
*   [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
    
*   [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#syntax)

--------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#values)

The `rule` property accepts a comma-separated list of values, including:

[`<gap-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#gap-rule)

Specified as one, two, or three of the values listed below, in any order.

[`<'line-width'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#line-width)

A [`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
: a positive [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or one of the three keywords, `thin`, `medium`, or `thick`. The default value is `medium`. See [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
.

[`<'line-style'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#line-style)

A [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
: one of `none`, `hidden`, `dotted`, `dashed`, `solid`, `double`, `groove`, `ridge`, `inset`, or `outset`. The default value is `none`. See [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
.

[`<'color'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#color)

A [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value representing the color of the line. The default value is `currentcolor`. See [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
.

[`<gap-repeat-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#gap-repeat-rule)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 of `1` or more as the first argument and one or more `<gap-rule>` values as subsequent arguments. The `<integer>` specifies how many times the list of `<gap-rule>` values should be repeated.

[`<gap-auto-repeat-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#gap-auto-repeat-rule)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with `auto` as the first argument and one or more `<gap-rule>` values as subsequent arguments. The provided list of `<gap-rule>` values is repeated as many times as needed to fill in values for any rules that are not explicitly specified by other components of the property value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#description)

------------------------------------------------------------------------------------------------------

The `rule` property defines the line style of any rule lines drawn in the gaps between rows and columns in [multi-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
, [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 containers with more than one row or column.

The `rule` is shorthand for [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
, [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
, and [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
. It sets the [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
 and [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
 shorthand properties to the same value.

The property value is a comma-separated list of components, which can include `<gap-rule>`, `<gap-repeat-rule>`, and `<gap-auto-repeat-rule>` types. Each `<gap-rule>` defines the width, color, and style of one or more rule lines.

If the property value consists of only one `<gap-rule>`, all the row and column rules will be that style, color, and size. If we declare the following, all row and column rules will be `dashed red 3px`:

When more than one `<gap-rule>` is declared, they will be applied to rules in the order specified. If there are more gutters between rows and columns than `<gap-rule>` values, the list of values is repeated until every row and column rule has a gap line. If we declare the following, for example, every odd rule will be `dashed red 3px`, and every even rule will be `dotted blue 5px`, in both directions.

### [Repeated line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#repeated_line_styles)

The `repeat()` function, with an integer of `1` or greater as the first argument, can be used to repeat a valid list of CSS [`<gap-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#gap-rule)
 values passed as subsequent arguments the specified number of times. This allows the same `<gap-rule>` to be repeated a set number of times without repeating the same CSS multiple times. The following declarations are equivalent:

This creates a list of seven rules. If the number of styles in the `rule` value's style list exceeds the number of gaps between rows and columns, the excess style values are ignored. If the container on which this is applied has three rows and columns, the rule in the first gutter will be `solid red 5px` and the second `outset blue 10px`, in both directions.

If there are more gutters than styles, the list of styles is repeated. If the container has 8, 15, 22, or 29 rows or columns, this sequence of styles will be repeated in that direction one, two, three, or four times, respectively, with the last rule being `inset green 1px`.

### [Auto-repeating line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#auto-repeating_line_styles)

The `repeat()` function also accepts `auto` as the first argument instead of a positive integer. With `auto` as the first argument, the [`<gap-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#gap-rule)
 values passed as subsequent arguments will be repeated as many times as needed to fill in values for any row and column rules that are not explicitly specified by other components of the property value.

In this case, the first and last row and column rules will be `solid red 5px`, and all others will alternate between `dotted green 1px` and `dashed blue 1px`. It doesn't matter if the container has 3, 6, 11, 16, or 21 rows and columns; the first and last gutters will always have a thick solid red line painted between them (unless [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
 leads to no line being drawn), and all the other row and column rules will be thin, dotted green or dashed blue lines. If there are only 2 or 3 rows and columns, there will be no dotted or dashed lines.

The `auto` keyword within the `repeat()` function creates an auto-repeater that fills in values for row and column rules that would not otherwise receive values from other parts of the list, preventing the list from being cycled. At most, only one `repeat(auto, <gap-rule>)` can be present in a `rule` value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#formal_definition)

------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#formal_syntax)

----------------------------------------------------------------------------------------------------------

rule =   
  [<'column-rule'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
    
  
[<column-rule>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
 =   
  <gap-rule-list>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <gap-auto-rule-list>    
  
<gap-rule-list> =   
  <gap-rule-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<gap-auto-rule-list> =   
  <gap-rule-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <gap-auto-repeat-rule> , <gap-rule-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<gap-rule-or-repeat> =   
  <gap-rule>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <gap-repeat-rule>    
  
<gap-auto-repeat-rule> =   
  repeat( auto , <gap-rule>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<gap-rule> =   
  <line-width>  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <line-style>  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
         
  
<gap-repeat-rule> =   
  repeat( <integer \[1,∞\]> , <gap-rule>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             
  
[<line-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 =   
  none    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dotted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dashed  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  solid   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  double  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  groove  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ridge   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inset   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outset    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#examples)

------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#basic_example)

In this example, we define a single rule for the lines drawn in the gutters between grid items.

#### HTML

We create a list of 75 items. Most of the HTML is hidden for brevity.

#### CSS

We define the unordered list as a 10-column container, creating columns and rows with the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 property and setting [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 to `none` to remove the bullets. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `5px` to provide enough room between the columns and rows to fit our `dashed 3px magenta` rule.

#### Result

### [Multiple gap-rules and default values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#multiple_gap-rules_and_default_values)

This example demonstrates using multiple, comma-separated values. It also demonstrates the default values for the width, color, and style of `medium`, `currentcolor` and `none`, respectively.

#### CSS

Using the same HTML and CSS as in the previous example, we include four comma-separated `<gap-rule>` values as the `rule` value, omitting the `<line-width>` in the first `<gap-rule>`, the `<color>` in the second, and the `<line-style>` from the third, with the fourth including all three components:

#### Result

The red line is `3px` wide, the dotted line is the same color as the text, and there is no `5px`\-wide blue line, as the style of the third `<gap-rule>` defaults to `none`, so no line is painted. As there are fewer rule styles than gutters, the list of rules is repeated until all rule lines are styled.

### [Using the `repeat()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#using_the_repeat_function)

This example demonstrates using the `repeat()` function within the `rule` property value.

#### CSS

We use the same HTML and CSS as in the previous examples, overriding the `rule` value with a comma-separated list of three components: two `<gap-rule>` values and a `<gap-repeat-rule>` that sets a list of two `<gap-rule>` values to repeat 3 times.

#### Result

The grid has ten columns and eight rows, so nine column gutters and seven row gutters. The `repeat()` function repeats two style values three times, creating a list of eight style values. As there are fewer row gutters than values, the last value is not used in the row direction. As there are more column gutters than values, the list repeats in the column direction.

### [Using `auto` within `repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#using_auto_within_repeat)

This example demonstrates using the `auto` argument instead of an integer in the `repeat()` function.

#### CSS

Using `repeat(auto, <gap-rule>)`, we set all row and column rules to `1px dotted` (with the color defaulting to the current color), except the first and last rules, which we set to `3px solid red`.

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-rule](https://drafts.csswg.org/css-gaps-1/#propdef-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule#see_also)

------------------------------------------------------------------------------------------------

*   [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
    
*   [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
    
*   [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
     shorthand
*   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
     shorthand
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/rule/index.md?plain=1 "Folder: en-us/web/css/reference/properties/rule (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5fd3b03e9ad1ee4e8bc64d4f6888570690a7fbc8%0A*+Document+last+modified%3A+2026-10-06T14%3A57%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")