*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#mdn-search)
    

`row-rule` CSS property
=======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#browser_compatibility)
 carefully before using this in production.

The **`row-rule`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the width, style, and color of the line drawn between rows in multi-row grid, flex, and multi-col layouts.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#try_it)

------------------------------------------------------------------------------------------------

    row-rule: solid;
    

    row-rule: dotted medium blue;
    

    row-rule:
      dotted medium blue,
      repeat(3, dashed magenta 1px, outset green 5px);
    

    row-rule:
      dotted medium blue,
      repeat(auto, dashed magenta 1px, dashed magenta 5px),
      dotted medium blue;
    

    row-rule:
      dotted medium blue,
      repeat(auto, dashed magenta 1px),
      outset green 5px;
    

    <section id="default-example">
      <ul id="example-element">
        <li>One fish</li>
        <li>Two fish</li>
        <li>Red fish</li>
        <li>Blue fish</li>
      </ul>
    </section>
    

    #example-element {
      display: flex;
      flex-flow: column;
      gap: 7px;
      text-align: left;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#constituent_properties)

--------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
    
*   [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    
*   [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#syntax)

------------------------------------------------------------------------------------------------

css

    /* One value */
    row-rule: dotted;
    row-rule: solid 8px;
    row-rule: solid blue;
    row-rule: thick inset blue;
    
    /* Multiple values */
    row-rule: groove, dashed, solid;
    row-rule:
      dotted medium blue,
      dashed magenta 1px,
      outset green 5px;
    row-rule:
      solid #0ff,
      repeat(3, dashed magenta 1px, outset green 5px);
    row-rule:
      inset 3px yellow,
      repeat(auto, dashed magenta 1px, groove green 5px);
    
    /* Global values */
    row-rule: inherit;
    row-rule: initial;
    row-rule: revert;
    row-rule: revert-layer;
    row-rule: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#values)

This property is specified as a comma-separated list of values. Each value can be one of the following value types:

[`<gap-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#gap-rule)

Specified as one, two, or three of the values listed below, in any order.

[`<'line-width'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#line-width)

A [`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
: a positive [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or one of the three keywords, `thin`, `medium`, or `thick`. The default value is `medium`. See [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
.

[`<'line-style'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#line-style)

A [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
: one of `none`, `hidden`, `dotted`, `dashed`, `solid`, `double`, `groove`, `ridge`, `inset`, or `outset`. The default value is `none`. See [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
.

[`<'color'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#color)

A [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value representing the color of the line. The default value is `currentcolor`. See [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
.

[`<gap-repeat-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#gap-repeat-rule)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 of `1` or more as the first argument and one or more `<gap-rule>` values as subsequent arguments. The `<integer>` specifies how many times the list of `<gap-rule>` values should be repeated.

[`<gap-auto-repeat-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#gap-auto-repeat-rule)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with `auto` as the first argument and one or more `<gap-rule>` values as subsequent arguments. The provided list of `<gap-rule>` values is repeated as many times as needed to fill in values for any row-rules that are not explicitly specified by other components of the property value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#description)

----------------------------------------------------------------------------------------------------------

The `row-rule` property defines the line style of any rule lines drawn in the gaps between rows in [multi-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
, [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 containers with more than one row.

The `row-rule` is shorthand for [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
, [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
, and [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
. The `row-rule`, along with the [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
 shorthand property, can also be set using the [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 shorthand.

The property value is a comma-separated list of components, which can include `<gap-rule>`, `<gap-repeat-rule>`, and `<gap-auto-repeat-rule>` types. Each `<gap-rule>` defines the width, color, and style of one or more rule lines.

If the property value consists of only one `<gap-rule>`, all the row rules will be that style. If we declare the following, all row rules will be `dashed red 3px`:

css

    row-rule: dashed red 3px;
    

When more than one `<gap-rule>` is declared, they will be applied to row-rules in the order specified. If there are more gutters between rows than `<gap-rule>` values, the list of values is repeated until every row rule has a gap line. If we declare the following, for example, every odd rule will be `dashed red 3px`, and every even rule will be `dotted blue 5px`.

css

    row-rule:
      dashed red 3px,
      dotted blue 5px;
    

### [Repeated line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#repeated_line_styles)

The `repeat()` function, with an integer of `1` or greater as the first argument, can be used to repeat a valid list of CSS [`<gap-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#gap-rule)
 values passed as subsequent arguments the specified number of times. This allows the same `<gap-rule>` to be repeated a set number of times without repeating the same CSS multiple times. The following declarations are equivalent:

css

    row-rule:
      solid red 5px,
      outset blue 10px,
      inset green 1px,
      outset blue 10px,
      inset green 1px,
      outset blue 10px,
      inset green 1px;
    row-rule:
      solid red 5px,
      repeat(3, outset blue 10px, inset green 1px);
    

This creates a list of seven rules. If the number of styles in the `row-rule` value's style list exceeds the number of gaps between rows, the excess style values are ignored. If the container on which this is applied has three rows, the rule in the first gutter will be `solid red 5px` and the second `outset blue 10px`.

If there are more gutters than styles, the list of styles is repeated. If the container has 8, 15, 22, or 29 rows, this sequence of styles will be repeated one, two, three, or four times, respectively, with the last rule being `inset green 1px`.

### [Auto-repeating line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#auto-repeating_line_styles)

The `repeat()` function also accepts `auto` as the first argument instead of a positive integer. With `auto` as the first argument, the [`<gap-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#gap-rule)
 values passed as subsequent arguments will be repeated as many times as needed to fill in values for any rules that are not explicitly specified by other components of the property value.

css

    row-rule:
      solid red 5px,
      repeat(auto, dotted green 1px, dashed blue 1px),
      solid red 5px;
    

In this case, the first and last row rules will be `solid red 5px`, and all others will alternate between `dotted green 1px` and `dashed blue 1px`. It doesn't matter if the container has 3, 6, 11, 16, or 21 rows; the first and last gutters will always have a thick solid red line painted between them (unless [`row-rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-visibility-items)
 leads to no line being drawn), and all the other row rules will be thin, dotted green or dashed blue lines. If there are only 2 or 3 rows, there will be no dotted or dashed lines.

The `auto` keyword within the `repeat()` function creates an auto-repeater that fills in values for row rules that would not otherwise receive values from other parts of the list, preventing the list from being cycled. At most, only one `repeat(auto, <gap-rule>)` can be present in a `row-rule` value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#formal_definition)

----------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#formal_syntax)

--------------------------------------------------------------------------------------------------------------

row-rule =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#examples)

----------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#basic_example)

In this example, we define a single rule for the lines drawn between flex items.

#### HTML

We include a list of dynamic sports duos:

html

    <ul>
      <li>Simone Biles + Jonathan Owens</li>
      <li>Serena Williams + Venus Williams</li>
      <li>Aaron Judge + Giancarlo Stanton</li>
      <li>LeBron James + Dwyane Wade</li>
      <li>Xavi Hernandez + Andres Iniesta</li>
      <li>Kerri Walsh + Misty May Treanor</li>
    </ul>
    

#### CSS

We define the list to be a flex container, creating rows by setting the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 to `column` using the [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 shorthand. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `5px` to provide enough room between the rows to fit our `3px dashed red` rule:

css

    ul {
      display: flex;
      flex-flow: column;
      gap: 5px;
    
      row-rule: 3px red dashed;
    }
    

#### Result

### [Repeating values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#repeating_values)

This example demonstrates how the values are repeated when there are fewer values in the list of styles than row rules. It also demonstrates the default values for the width, color, and style of `medium`, `currentcolor` and `none`, respectively.

#### CSS

Using the same HTML and CSS as in the previous example, we include four comma-separated `<gap-rule>` values as the `row-rule` value, omitting the width in the first `<gap-rule>`, the color in the second, and the style from the third, with the fourth including all three components:

css

    ul {
      row-rule:
        red dashed,
        1px dotted,
        5px blue,
        10px magenta solid;
    }
    

#### Result

The red line is `3px` wide, the dotted line is the same color as the text, and there is no `5px`\-wide blue line, as the style of the third `<gap-rule>` defaults to `none`, so no line is painted.

### [Using the `repeat()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#using_the_repeat_function)

This example demonstrates using the `repeat()` function within the `row-rule` property value.

#### CSS

We use the same HTML and CSS as in the previous examples. We include a `repeat()` function, setting the list of two `<gap-rule>` values to repeat 3 times.

css

    ul {
      row-rule:
        3px red dashed,
        repeat(3, dotted green 1px, dashed blue 1px),
        3px red dashed;
    }
    

#### Result

The flex container has six rows, so five gutters. The `repeat()` function repeats two style values three times, creating a list of eight style values. As there are fewer row gutters than total gap-rules, the last three values in the list are discarded.

### [Using `auto` within `repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#using_auto_within_repeat)

This example demonstrates using the `auto` argument instead of an integer in the `repeat()` function.

#### CSS

Using `repeat(auto, <gap-rule>)`, we set all row rules to `1px dotted` and default to the current color, except the first and last, which we set to `3px solid red`.

css

    ul {
      row-rule:
        3px red solid,
        repeat(auto, 1px dotted),
        3px red solid;
    }
    

#### Result

    @layer no-support {
      @supports not (row-rule: thin, thick) {
        body::before {
          content: "Your browser doesn't support the row-rule property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-row-rule](https://drafts.csswg.org/css-gaps-1/#propdef-row-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule#see_also)

----------------------------------------------------------------------------------------------------

*   [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
    
*   [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
    
*   [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
     shorthand
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/row-rule/index.md?plain=1 "Folder: en-us/web/css/reference/properties/row-rule (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5fd3b03e9ad1ee4e8bc64d4f6888570690a7fbc8%0A*+Document+last+modified%3A+2026-10-06T14%3A57%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")