*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#mdn-search)
    

`column-rule` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`column-rule`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the width, style, and color of the lines drawn between columns in multi-column grid, flex, and multi-col layouts.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#try_it)

---------------------------------------------------------------------------------------------------

    column-rule: solid;
    

    column-rule: groove 0.8em teal;
    

    column-rule:
      dotted thick teal,
      repeat(3, dashed pink 1px, outset olive 5px);
    

    column-rule:
      dotted thick teal,
      repeat(auto, dashed pink 1px, dashed pink 5px),
      dotted thick teal;
    

    column-rule:
      dashed medium olive,
      repeat(auto, dotted pink 1px),
      inset orange 5px;
    

    <section id="default-example">
      <p id="example-element">
        London. Lady Catnip sitting in Lincoln's Inn Hall. Nice May weather. As much
        mud in the streets as if the waters had but newly retired from the face of
        the earth, and it would not be great to meet a Fred, two feet long or so,
        waddling like an iguana up Holborn Hill.
      </p>
    </section>
    

    #example-element {
      columns: 7;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#constituent_properties)

-----------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
*   [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#syntax)

---------------------------------------------------------------------------------------------------

css

    /* One value */
    column-rule: dashed;
    column-rule: inset 8px;
    column-rule: solid teal;
    column-rule: thick outset rgb(18 122 67);
    
    /* Multiple values */
    column-rule: groove, dashed, solid;
    column-rule:
      dotted medium teal,
      dashed pink 0.5em,
      outset olive 1px;
    column-rule:
      solid #0ff,
      repeat(3, dashed pink 1px, outset olive 5px);
    column-rule:
      inset 3px yellow,
      repeat(auto, dashed pink 1px, groove olive 5px);
    
    /* Global values */
    column-rule: inherit;
    column-rule: initial;
    column-rule: revert;
    column-rule: revert-layer;
    column-rule: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#values)

This property is specified as a comma-separated list of values. Each value can be one of the following value types:

[`<gap-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#gap-rule)

Specified as one, two, or three of the values listed below, in any order.

[`<'line-width'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#line-width)

A [`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
: This can be one of the keywords `thin`, `medium`, or `thick`, or a positive [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value, representing the width of the line. The default value is `medium`.

[`<'line-style'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#line-style)

A [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
: one of `none`, `hidden`, `dotted`, `dashed`, `solid`, `double`, `groove`, `ridge`, `inset`, or `outset`. The default value is `none`. See [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
.

[`<'color'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#color)

A [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value representing the color of the line. The default value is `currentcolor`. See [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
.

[`<gap-repeat-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#gap-repeat-rule)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 of `1` or more as the first argument and one or more `<gap-rule>` values as subsequent arguments. The `<integer>` specifies how many times the list of `<gap-rule>` values should be repeated.

[`<gap-auto-repeat-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#gap-auto-repeat-rule)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with `auto` as the first argument and one or more `<gap-rule>` values as subsequent arguments. The provided list of `<gap-rule>` values is repeated as many times as needed to fill in values for any column-rules that are not explicitly specified by other components of the property value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#description)

-------------------------------------------------------------------------------------------------------------

The `column-rule` property defines the line style of any rule lines drawn in the gaps between columns in [multi-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
, [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 containers with more than one column.

The `column-rule` is shorthand for [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
, [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
, and [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
. The `column-rule`, along with the [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
 shorthand property, can also be set using the [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 shorthand.

The property value is a comma-separated list of components, which can include `<gap-rule>`, `<gap-repeat-rule>`, and `<gap-auto-repeat-rule>` types. Each `<gap-rule>` defines the width, color, and style of one or more rule lines.

If the property value consists of only one `<gap-rule>`, all the column rules will be that style. If we declare the following, all column rules will be `dashed maroon 3px`:

css

    column-rule: dashed maroon 3px;
    

When more than one `<gap-rule>` is declared, they will be applied to column-rules in the order specified. If there are more gutters between columns than `<gap-rule>` values, the list of values is repeated until every column rule has a gap line. If we declare the following, for example, every odd rule will be `dashed maroon 3px`, and every even rule will be `dotted navy 5px`.

css

    column-rule:
      dashed maroon 3px,
      dotted navy 5px;
    

### [Repeated line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#repeated_line_styles)

The `repeat()` function, with an integer of `1` or greater as the first argument, can be used to repeat a valid list of CSS [`<gap-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#gap-rule)
 values passed as subsequent arguments the specified number of times. This allows the same `<gap-rule>` to be repeated a set number of times without repeating the same CSS multiple times. The following declarations are equivalent:

css

    column-rule:
      solid maroon 5px,
      outset navy 10px,
      inset olive 1px,
      outset navy 10px,
      inset olive 1px,
      outset navy 10px,
      inset olive 1px;
    column-rule:
      solid maroon 5px,
      repeat(3, outset navy 10px, inset olive 1px);
    

This creates a list of seven rules. If the number of styles in the `column-rule` value's style list exceeds the number of gaps between columns, the excess style values are ignored. If the container on which this is applied has three columns, the rule in the first gutter will be `solid maroon 5px` and the second `outset navy 10px`.

If there are more gutters than styles, the list of styles is repeated. If the container has 8, 15, 22, or 29 columns, this sequence of styles will be repeated one, two, three, or four times, respectively, with the last rule being `inset olive 1px`.

### [Auto-repeating line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#auto-repeating_line_styles)

The `repeat()` function also accepts `auto` as the first argument instead of a positive integer. With `auto` as the first argument, the [`<gap-rule>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#gap-rule)
 values passed as subsequent arguments will be repeated as many times as needed to fill in values for any rules that are not explicitly specified by other components of the property value.

css

    column-rule:
      solid maroon 5px,
      repeat(auto, dotted olive 1px, dashed navy 1px),
      solid maroon 5px;
    

In this case, the first and last column rules will be `solid maroon 5px`, and all others will alternate between `dotted olive 1px` and `dashed navy 1px`. It doesn't matter if the container has 3, 6, 11, 16, or 21 columns; the first and last gutters will always have a thick solid maroon line painted between them (unless [`column-rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items)
 leads to no line being drawn), and all the other column rules will be thin, dotted olive or dashed navy lines. If there are only 2 or 3 columns, there will be no dotted or dashed lines.

The `auto` keyword within the `repeat()` function creates an auto-repeater that fills in values for column rules that would not otherwise receive values from other parts of the list, preventing the list from being cycled. At most, only one `repeat(auto, <gap-rule>)` can be present in a `column-rule` value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)<br>    : `medium`<br>*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)<br>    : `none`<br>*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)<br>    : `currentcolor` |
| Applies to | multicol elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)<br>    : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>    , snapped as a line width<br>*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)<br>    : as specified<br>*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)<br>    : computed color |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)<br>    : a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>    <br>*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)<br>    : discrete<br>*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)<br>    : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

column-rule =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#examples)

-------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#basic_example)

In this example, we define a single rule for the lines drawn between flex items.

#### HTML

We include a list of authors:

html

    <ul>
      <li>Kimberlé Crenshaw</li>
      <li>Angela Y. Davis</li>
      <li>Bernardine Evaristo</li>
      <li>Audre Lorde</li>
      <li>Cathy Park Hong</li>
      <li>Zoya Patel</li>
      <li>Juno Mac</li>
      <li>Molly Smith</li>
      <li>Tara Westover</li>
    </ul>
    

#### CSS

We define the list to be a flex container, creating columns by setting the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 to `row` using the [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 shorthand. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `12px` to provide enough room between the columns to fit our `10px groove maroon` rule:

css

    ul {
      display: flex;
      flex-flow: row;
      gap: 12px;
      list-style-type: none;
    
      column-rule: 10px groove maroon;
    }
    

#### Result

### [Repeating values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#repeating_values)

This example demonstrates how the values are repeated when there are fewer values in the list of styles than column rules. It also demonstrates the default values for the width, color, and style of `medium`, `currentcolor` and `none`, respectively.

Using the same HTML and CSS as in the previous example, we include four comma-separated `<gap-rule>` values as the `column-rule` value, omitting the width in the first `<gap-rule>`, the color in the second, and the style from the third, with the fourth including all three components:

css

    ul {
      column-rule:
        maroon dashed,
        1px dotted,
        5px teal,
        10px orange solid;
    }
    

The maroon line is `3px` wide. The dotted line is the same color as the text. There are no teal lines, as the `<line-style>` of the third `<gap-rule>` defaults to `none`, so no line is painted. There are more gutters than `<gap-rule>` values, so the list of values gets repeated.

### [Using the `repeat()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#using_the_repeat_function)

This example demonstrates using the `repeat()` function within the `column-rule` property value. We use the same HTML and CSS as in the previous examples. We include a `repeat()` function, setting the list of two `<gap-rule>` values to repeat four times.

css

    ul {
      column-rule:
        10px maroon dashed,
        repeat(4, dotted olive 3px, dashed teal 3px),
        10px maroon dashed;
    }
    

The flex container has nine columns, so eight gutters. The `repeat()` function repeats two style values four times, creating a list of ten `<gap-rule>` values. As there are fewer column gutters than total `<gap-rule>` values, the last two values in the list are discarded.

### [Using `auto` within `repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#using_auto_within_repeat)

This example demonstrates using the `auto` argument instead of an integer in the `repeat()` function.

Using `repeat(auto, <gap-rule>)`, we set all column rules to `1px dotted` and default to the current color, except the first and last, which we set to `10px groove maroon`.

css

    ul {
      column-rule:
        10px groove maroon,
        repeat(auto, 3px dotted maroon),
        10px groove maroon;
    }
    

    @layer no-support {
      @supports not (column-rule: thin, thick) {
        body::before {
          content: "Your browser doesn't support multiple values for the column-rule property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Multi-column Layout Module Level 1  <br>\# column-rule](https://drafts.csswg.org/css-multicol/#column-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule#see_also)

-------------------------------------------------------------------------------------------------------

*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    
*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
*   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
     shorthand
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)
    
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-rule/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-rule (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F04dfe418f2942ae739d41592c22fafa3679fc03c%0A*+Document+last+modified%3A+2026-10-05T17%3A37%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")