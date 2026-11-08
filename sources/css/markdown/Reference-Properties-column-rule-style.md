*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#mdn-search)
    

`column-rule-style` CSS property
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`column-rule-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the line style of the lines drawn between columns in multi-column grid, flex, and multi-col layouts.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#try_it)

---------------------------------------------------------------------------------------------------------

    column-rule-style: dotted;
    

    column-rule-style: dashed, dotted;
    

    column-rule-style: repeat(2, inset, outset), double;
    

    column-rule-style: double, repeat(auto, dashed, solid), double;
    

    column-rule-style: hidden;
    

    <section id="default-example">
      <p id="example-element">
        London. Noel term lately over, and the Lord George sitting in Lincoln's Inn
        Hall. Great May weather. As much mud in the streets as if the waters had but
        newly retired from the face of the earth, and it would not be weird to meet
        an platypus, two feet long or so, waddling like an lizard up Morgan Hill.
      </p>
    </section>
    

    #example-element {
      columns: 6;
      column-rule-width: thick;
      column-rule-color: teal;
      gap: 7px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    column-rule-style: none;
    column-rule-style: hidden;
    column-rule-style: dotted;
    column-rule-style: dashed;
    column-rule-style: solid;
    column-rule-style: double;
    column-rule-style: groove;
    column-rule-style: ridge;
    column-rule-style: inset;
    column-rule-style: outset;
    
    /* Multiple values */
    column-rule-style: groove, double, dashed;
    column-rule-style: solid, repeat(5, ridge), solid;
    column-rule-style: dotted, repeat(auto, inset, outset), dotted;
    
    /* Global values */
    column-rule-style: inherit;
    column-rule-style: initial;
    column-rule-style: revert;
    column-rule-style: revert-layer;
    column-rule-style: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#values)

The `column-rule-style` property accepts a comma-separated list of values, including:

[`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#line-style)

A [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
: one of `none`, `hidden`, `dotted`, `dashed`, `solid`, `double`, `groove`, `ridge`, `inset`, or `outset`. The default value is `none`.

[`<repeat-line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#repeat-line-style)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with the first argument being an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 of `1` or more, and subsequent arguments being [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 values. The integer specifies how many times the `<line-style>` values should be repeated.

[`<auto-repeat-line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#auto-repeat-line-style)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with `auto` as the first argument and one or more `<line-style>` values as subsequent arguments. The provided `<line-style>` values are repeated as many times as needed to fill in values for any column-rules that are not explicitly specified by other components of the property value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#description)

-------------------------------------------------------------------------------------------------------------------

The `column-rule-style` property defines the line style of any column rule lines drawn in the gaps between columns in [multi-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
, [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 containers with more than one column.

The value is a comma-separated list of components, which can include `<line-style>`, `<repeat-line-style>`, and `<auto-repeat-line-style>` types.

The `column-rule-style`, along with the [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
 and [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
 properties, can be set using the [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
 shorthand. The `column-rule-style`, along with the [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
 property, can also be set using the [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
 shorthand.

If the property value has only one `<line-style>`, all the column rules will be that style. If we declare the following, all column rules will be `double`:

css

    column-rule-style: double;
    

When more than one `<line-style>` is declared, they will be applied to column-rules in the order specified. If there are more column-rules than `<line-style>` values, the list of line styles is repeated until every column rule has a style. If we declare the following, for example, every odd rule will be `double`, and every even rule will be `groove`.

css

    column-rule-style: double, groove;
    

### [Repeated line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#repeated_line_styles)

The `repeat()` function, with an integer of `1` or greater as the first argument, can be used to repeat a valid list of CSS [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 values passed as subsequent arguments the specified number of times. This allows the same style to be repeated a set number of times without repeating the same value. You can include `<line-style>` keyword values or custom properties that resolve to a valid `<line-style>`. Using `repeat()` can make values easier to write, enabling recurring patterns to be written using a single function, regardless of the number of columns. The following declarations are equivalent:

css

    column-rule-style: solid, outset, inset, outset, inset;
    column-rule-style: solid, repeat(2, outset, inset);
    

This creates a list of five styles. If the number of styles in the `column-rule-style` value's style list exceeds the number of gaps between columns, the excess style values are ignored. If the container has three columns, the rule in the first gutter will be `solid` and the second `outset`.

If there are more gutters than styles, the list of styles is repeated. If the container has 6, 11, 16, or 21 columns, this sequence of styles will be repeated one, two, three, or four times, respectively, with the last rule being `inset`.

### [Auto-repeating line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#auto-repeating_line_styles)

The `repeat()` function also accepts `auto` as the first argument instead of a positive integer. With `auto` as the first argument, the `<line-style>` values passed as subsequent parameters will be repeated as many times as needed to fill in values for any column-rules that are not explicitly specified by other components of the property value.

css

    column-rule-style: solid, repeat(auto, dotted), solid;
    

In this case, it doesn't matter if the container has 3, 6, 11, 16, or 21 columns; the first and last column rules will always be `solid`, and all the other column rules will be `dotted`. If there are only 2 or 3 columns, there will be no dotted column rules.

The `auto` keyword within the `repeat()` function creates an auto repeater that fills in values for column rules that would not otherwise receive values from other parts of the list, preventing the list from being cycled. Only one `repeat(auto, <line-style>)` is allowed within a `column-rule-style` value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | multicol elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

column-rule-style =   
  <line-style-list>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <auto-line-style-list>    
  
<line-style-list> =   
  <line-style-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<auto-line-style-list> =   
  <line-style-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <auto-repeat-line-style> , <line-style-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<line-style-or-repeat> =   
  <line-style>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <repeat-line-style>    
  
<auto-repeat-line-style> =   
  repeat( auto , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <line-style> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
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
  
<repeat-line-style> =   
  repeat( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[1,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <line-style> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#examples)

-------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#basic_usage)

#### HTML

html

    <p>
      This is a bunch of text split into three columns. The `column-rule-style`
      property is used to change the style of the line that is drawn between
      columns. Don't you think that's wonderful?
    </p>
    

#### CSS

css

    p {
      column-count: 3;
      column-rule-style: dashed;
    }
    

#### Result

### [Multiple values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#multiple_values)

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
 of `5px` to provide enough room between the columns to fit our `3px` double teal rule:

css

    ul {
      display: flex;
      flex-flow: row;
      gap: 5px;
      column-rule-width: 3px;
      column-rule-color: teal;
    
      column-rule-style:
        dotted, dashed, solid, double, groove, ridge, inset, outset, none, hidden;
    }
    

#### Result

As there are more values (10) than gutters (8), the `none` and `hidden` values are not used.

### [Repeating values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#repeating_values)

This example demonstrates how, when there are fewer values in the list of styles than column rules, the values are repeated.

#### CSS

Using the same HTML and CSS as in the previous example, we include three comma-separated styles as the `column-rule-style` value:

css

    ul {
      column-rule-style: solid, groove, double;
    }
    

#### Result

### [Using the `repeat()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#using_the_repeat_function)

This example demonstrates using the `repeat()` function within the `column-rule-style` property value.

#### CSS

We use the same HTML and CSS as in the previous examples. We include a `repeat()` function, setting the list of two `<line-style>` values to be repeated 3 times.

css

    ul {
      column-rule-style: solid, repeat(3, inset, outset), solid;
    }
    

#### Result

The flex container has six columns, so five gutters. The `repeat()` function repeats two style values three times, creating a list of eight style values, so the last three values in the list are discarded.

### [Using `auto` within `repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#using_auto_within_repeat)

This example demonstrates using `auto` instead of an integer within the `repeat()` function.

#### CSS

Using `repeat(auto, <line-style>)` we set all column rules to `groove`, except the first and last, which we set to `solid`.

css

    ul {
      column-rule-style: solid, repeat(auto, groove), solid;
    }
    

#### Result

    @layer no-support {
      @supports not (column-rule-style: solid, groove) {
        body::before {
          content: "Your browser doesn't support multiple values for the column-rule-style property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Multi-column Layout Module Level 1  <br>\# crs](https://drafts.csswg.org/css-multicol/#crs) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    
*   [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
     shorthand
*   [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
     shorthand
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)
    
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-rule-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-rule-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5fd3b03e9ad1ee4e8bc64d4f6888570690a7fbc8%0A*+Document+last+modified%3A+2026-10-06T14%3A57%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")