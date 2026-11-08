*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#mdn-search)
    

`row-rule-color` CSS property
=============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#browser_compatibility)
 carefully before using this in production.

The **`row-rule-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the colors of the lines drawn between rows in multi-row grid, flex, and multi-col layouts.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#try_it)

------------------------------------------------------------------------------------------------------

    row-rule-color: magenta;
    

    row-rule-color: magenta, goldenrod;
    

    row-rule-color: repeat(2, magenta), goldenrod;
    

    row-rule-color: goldenrod, repeat(auto, magenta), goldenrod;
    

    row-rule-color: currentColor;
    

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
      row-rule-style: solid;
      row-rule-width: 5px;
      gap: 5px;
      text-align: left;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Single value */
    row-rule-color: red;
    row-rule-color: rgb(192 56 78);
    row-rule-color: transparent;
    row-rule-color: hsl(0 100% 50% / 60%);
    row-rule-color: var(--primaryColor);
    
    /* Multiple values */
    row-rule-color: red, transparent;
    row-rule-color: repeat(3, red), repeat(3, transparent);
    row-rule-color: repeat(3, red), repeat(3, yellow, blue);
    row-rule-color: red, repeat(auto, transparent), red;
    row-rule-color: red, repeat(auto, blue, yellow), red;
    row-rule-color: repeat(3, red), repeat(auto, transparent), repeat(3, red);
    
    /* Global values */
    row-rule-color: inherit;
    row-rule-color: initial;
    row-rule-color: revert;
    row-rule-color: revert-layer;
    row-rule-color: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#values)

The `row-rule-color` property accepts a comma-separated list of values, including:

[`<line-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#line-color)

A [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 representing the color of the line.

[`<repeat-line-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#repeat-line-color)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 of `1` or more as the first argument and one or more `<color>` values as subsequent arguments. The `<integer>` specifies how many times the `<color>` values should be repeated.

[`<auto-repeat-line-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#auto-repeat-line-color)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with `auto` as the first argument and one or more `<color>` values as subsequent arguments. The provided `<color>` values are repeated as many times as needed to fill in values for any row-rules that are not explicitly specified by other components of the property value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#description)

----------------------------------------------------------------------------------------------------------------

The `row-rule-color` property defines the colors of any lines drawn in the gaps between rows in [multi-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
, [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 containers with more than one row.

The value is a comma-separated list of components, which can include `<line-color>`, `<repeat-line-color>`, and `<auto-repeat-line-color>` types.

The `row-rule-color`, along with the [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
 and [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
 properties, can be set using the [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
 shorthand. The `row-rule-color`, along with the [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
 property, can also be set using the [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
 shorthand.

A `<line-color>` can be declared as any valid CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value. If the property value consists of only one `<color>`, all the rule lines will be that color. If we declare the following, the lines will all be blue:

css

    row-rule-color: blue;
    

When more than one `<line-color>` is declared, they will be applied to row-rules in the order specified. If there are more row-rules than `<line-color>` values, the list of line colors is repeated until every row-rule has a color. If we declare the following, for example, every odd rule will be blue, and every even rule will be yellow.

css

    row-rule-color: blue, yellow;
    

### [Repeated line colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#repeated_line_colors)

The `repeat()` function, with an integer of `1` or greater as the first argument, can be used to repeat a valid list of CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values passed as subsequent arguments the specified number of times. This allows the same color to be repeated a set number of times without repeating the same `<line-color>` multiple times. The following declarations are equivalent:

css

    row-rule-color: blue, yellow, red, yellow, red;
    row-rule-color: blue, repeat(2, yellow, red);
    

You can use any valid color value from any color space, including CSS color functions, custom properties, etc. Using `repeat()` can make values easier to write, especially as your color values become more complex. It enables a recurring pattern to be written using a single function, regardless of the number of rows.

If we set `--base: yellow` and `--mixin: blue`, the following will provide similar results to the previous declaration:

css

    row-rule-color:
      color-mix(in lch decreasing hue, var(--base) 0%, var(--mixin)),
      repeat(
        2,
        color-mix(in lch decreasing hue, var(--base) 100%, var(--mixin)),
        color-mix(in lch decreasing hue, var(--base) 58%, var(--mixin))
      );
    

This creates a list of five colors. If the number of colors in the `row-rule-color` value's color list exceeds the number of gaps between rows, the excess color values are ignored. If the container has three rows, the rule in the first gutter will be blue and the second yellow.

If there are more gutters than colors, the list of colors is repeated until all row-rules receive a color. If the container has 6, 11, 16, or 21 rows, this sequence of colors will be repeated one, two, three, or four times, respectively, with the last one being red.

### [Auto-repeating line colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#auto-repeating_line_colors)

The `repeat()` function also accepts `auto` as the first argument instead of a positive integer. With `auto` as the first argument, the `<color>` values passed in subsequent arguments will be repeated as many times as needed to fill in values for any row-rules that are not explicitly specified by other components of the property value, if any.

css

    row-rule-color: blue, repeat(auto, yellow), red;
    

In this case, the first row-rule will be blue, the last will be red, and all others will be yellow. It doesn't matter if the container has 3, 6, 11, 16, or 21 rows; the first will always be blue and, as long as there are at least two row-rules, the last will always be red. All the other rules will be yellow, which means if there are only 2 or 3 rows, there will be no yellow lines.

The `auto` keyword within the `repeat()` function creates an auto-repeater that fills in values for the row-rule line colors that would not otherwise receive values from other parts of the list, preventing the list from being cycled. A `row-rule-color` value can include, at most, one `repeat(auto, <color>)`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

row-rule-color =   
  <line-color-list>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <auto-line-color-list>    
  
<line-color-list> =   
  <line-color-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<auto-line-color-list> =   
  <line-color-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <auto-repeat-line-color> , <line-color-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<line-color-or-repeat> =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <repeat-line-color>    
  
<auto-repeat-line-color> =   
  repeat( auto , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<repeat-line-color> =   
  repeat( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[1,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#examples)

----------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#basic_example)

In this example, we define a single color for the lines drawn between flex items.

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

We define the list as a flex container, creating rows by setting [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 to `column` with the [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 shorthand. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `5px` to provide enough room between the rows to fit our `3px` dashed rule:

css

    ul {
      display: flex;
      flex-flow: column;
      gap: 5px;
      row-rule-style: dashed;
      row-rule-width: 3px;
      row-rule-color: blue;
    }
    

#### Result

### [Repeating values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#repeating_values)

This example demonstrates how, when there are fewer values in the list of colors than gutters between rows, the values are repeated.

#### CSS

Using the same HTML and CSS as in the previous example, we include three comma-separated colors as the `row-rule-color` value:

css

    ul {
      row-rule-color: blue, yellow, red;
    }
    

#### Result

### [Using the `repeat()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#using_the_repeat_function)

This example demonstrates using the `repeat()` function within the `row-rule-color` property value and how this function can help prevent complex values from becoming unwieldy.

#### CSS

We use the same HTML and CSS as in the previous examples. To demonstrate how values can become complicated and the utility of the `repeat()` function, we declare two custom properties, which we use in three [`color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix)
 color function declarations to create the same blue, red, and yellow colors as in the previous example. The second declaration is within a `repeat()` function, set to repeat 3 times.

css

    ul {
      --base: yellow;
      --mixin: blue;
      row-rule-color:
        color-mix(in lch decreasing hue, var(--base) 0%, var(--mixin)),
        repeat(3, color-mix(in lch decreasing hue, var(--base) 100%, var(--mixin))),
        color-mix(in lch decreasing hue, var(--base) 58%, var(--mixin));
    }
    

#### Result

The flex container has six rows, so five gutters. The `repeat()` function repeats our second color three times, creating a color list with five colors. Since there are as many row gutters as there are total colors, the colors are not repeated.

### [Using `auto` within `repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#using_auto_within_repeat)

This example demonstrates using `auto`, instead of an integer, within the `repeat()` function.

#### CSS

Using `repeat(auto, <color>)`, we set all the lines to be almost transparent black (`#00000033`), except the first and last, which we set to a solid `black`.

css

    ul {
      row-rule-color: black, repeat(auto, #00000033), black;
    }
    

#### Result

    @layer no-support {
      @supports not (row-rule-color: red, blue) {
        body::before {
          content: "Your browser doesn't support the row-rule-color property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-row-rule-color](https://drafts.csswg.org/css-gaps-1/#propdef-row-rule-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color#see_also)

----------------------------------------------------------------------------------------------------------

*   [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
    
*   [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    
*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
     shorthand
*   [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
     shorthand
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)
    
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/row-rule-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/row-rule-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5fd3b03e9ad1ee4e8bc64d4f6888570690a7fbc8%0A*+Document+last+modified%3A+2026-10-06T14%3A57%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")