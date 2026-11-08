*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#mdn-search)
    

`calc()` CSS function
=====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`calc()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 lets you perform calculations when specifying CSS property values. It can be used with [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
, [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
, and [`<color-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#try_it)

----------------------------------------------------------------------------------------

    width: calc(10px + 100px);
    

    width: calc(100% - 30px);
    

    width: calc(2em * 5);
    

    width: calc(var(--variable-width) + 20px);
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">Change my width.</div>
    </section>
    

    :root {
      --variable-width: 100px;
    }
    
    #example-element {
      border: 10px solid black;
      padding: 10px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#syntax)

----------------------------------------------------------------------------------------

css

    /* calc(expression) */
    calc(100% - 80px)
    
    /* Expression with a CSS function */
    calc(100px * sin(pi / 2))
    
    /* Expression containing a variable */
    calc(var(--hue) + 180)
    
    /* Expression with color channels in relative colors */
    lch(from aquamarine l c calc(h + 180))
    

The `calc()` function takes a single expression as its parameter, and the expression's result is used as the value for a CSS property. In this expression, the [operands](https://developer.mozilla.org/en-US/docs/Glossary/Operand)
 can be combined using the [operators](https://developer.mozilla.org/en-US/docs/Glossary/Operator)
 listed below. When the expression contains multiple operands, `calc()` uses the standard [operator precedence rules](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Math#operator_precedence)
:

[`+`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#sect)

Adds the specified operands.

[`-`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#-)

Subtracts the second operand from the first operand.

[`*`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#sect_2)

Multiplies the specified operands.

[`/`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#sect_3)

Divides the left-side operand (dividend) by the right-side operand (divisor).

All operands, except those of type [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, must be suffixed with an appropriate unit string, such as `px`, `em`, or `%`. You can use a different unit with each operand in your expression. You may also use parentheses to establish computation order when needed.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#description)

--------------------------------------------------------------------------------------------------

There are a few points to note about `calc()`, which are detailed in the sections below.

### [Resulting values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#resulting_values)

The `calc()` function must stand in place of a full CSS value of one of the following types:

*   [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    
*   [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
    
*   [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
    
*   [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    
*   [`<flex>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)
    
*   [`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
    
*   [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
*   [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    
*   [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
    
*   One of the mixed types like [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
    

`calc()` cannot only replace the numeric part of percentage values, length values, etc., without also replacing the unit after it. For example, `calc(100 / 4)%` is invalid, while `calc(100% / 4)` is valid.

The resulting value of `calc()` must be compatible with the context in which it is used. For example, `margin: calc(1px + 2px)` is valid, but `margin: calc(1 + 2)` is not: it is equivalent to specifying `margin: 3`, which results in the property being ignored.

When an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 is expected, the `calc()` expression can also evaluate to a `<number>`, which gets rounded to the nearest integer. So, `calc(1.4)` will result in a value of `1`. If the fractional part of the value is exactly `0.5`, the value is rounded towards positive infinity. For example, `calc(1.5)` will result in a value of `2`, while `calc(-1.5)` will round to `-1`.

`calc()` performs floating point math following the IEEE-754 standard, which results in some considerations concerning the `infinity` and `NaN` values. For more details on how constants are serialized, see the [`<calc-keyword>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
 page.

### [Input considerations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#input_considerations)

*   `calc()` cannot perform calculations on [intrinsic size values](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
     such as [`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#auto)
     and [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
    . Use the [`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
     function instead.
*   The `*` and `/` operators do not require whitespace, but adding it for consistency is recommended.
*   It is permitted to nest `calc()` functions, in which case, the inner ones are treated as simple parentheses.
*   Math expressions involving percentages for widths and heights on table columns, table column groups, table rows, table row groups, and table cells in both auto and fixed layout tables _may_ be treated as if `auto` is specified.
*   See [`<calc-sum>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
     for more information on the syntax of `+` and `-` expressions.

### [CSS typed arithmetic](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#css_typed_arithmetic)

When using `calc()` to multiply values, using the `*` operator, only one value can contain a unit. Calculations like `200px * 4px` are not supported as 800px2 is meaningless in CSS.

Inversely, `200px / 4px` resolves to `50`, which does make sense in CSS. Therefore, when using the `calc()` function to divide numbers, using the `/` operator, [supporting browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#browser_compatibility)
 allow units on both sides of the operand, provided they are of the same data type. For example, `100vw / 1px` is valid and results in a unitless value.

The quotient can then be used in the values of properties or functions that accept a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 as a value or parameter, or converted into a different data type by multiplying it by a typed value.

For a full explanation of typed arithmetic in CSS, along with examples, see [Using CSS typed arithmetic](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic)
.

### [Support for computing color channels in relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#support_for_computing_color_channels_in_relative_colors)

The `calc()` function can be used to manipulate color channels directly within the context of [relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
. This allows for dynamic adjustments of color channels in color models such as [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
, [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
, and [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
.

The relative color syntax defines several color-channel keywords, each of which represents the value of the color channel as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 (see [Channel values resolve to `<number>` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors#channel_values_resolve_to_number_values)
 for more information). The `calc()` function can use these color-channel keywords to perform dynamic adjustments on the color channels, for example, `calc(r + 10)`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#formal_syntax)

------------------------------------------------------------------------------------------------------

<calc()> =   
  calc( <calc-sum> )    
  
[<calc-sum>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 =   
  <calc-product> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '+' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '-' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-product> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-product> =   
  <calc-value> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '\*' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 / [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-value> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dimension>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <calc-sum> )    
  
[<calc-keyword>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
 =   
  e          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pi         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  NaN          

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#accessibility)

------------------------------------------------------------------------------------------------------

When `calc()` is used for controlling text size, be sure that one of the values includes a [relative length unit](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units)
, for example:

css

    h1 {
      font-size: calc(1.5rem + 3vw);
    }
    

This ensures that text size will scale if the page is zoomed.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.4: Resize Text | WAI | W3C](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#examples)

--------------------------------------------------------------------------------------------

### [Positioning an object on screen with a margin](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#positioning_an_object_on_screen_with_a_margin)

`calc()` enables positioning an object with a set margin. In this example, the CSS creates a banner that stretches across the window, with a 40-pixel gap between both sides of the banner and the edges of the window:

css

    .banner {
      position: absolute;
      left: 40px;
      width: calc(100% - 80px);
      border: solid black 1px;
      box-shadow: 1px 2px;
      background-color: yellow;
      padding: 6px;
      text-align: center;
      box-sizing: border-box;
    }
    

html

    <div class="banner">This is a banner!</div>
    

### [Automatically sizing form fields to fit their container](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#automatically_sizing_form_fields_to_fit_their_container)

Another use case for `calc()` is to help ensure that form fields fit in the available space, without extruding past the edge of their container while maintaining an appropriate margin.

Let's look at some CSS:

css

    input {
      padding: 2px;
      display: block;
      width: calc(100% - 1em);
    }
    
    #form-box {
      width: calc(100% / 6);
      border: 1px solid black;
      padding: 4px;
    }
    

Here, the container is established to use 1/6 of the available window width. Then, to ensure that input fields retain an appropriate size, we use `calc()` again to establish that they should be the width of their container minus 1em. Then, the following HTML makes use of this CSS:

html

    <div id="form-box">
      <label for="misc">Type something:</label>
      <input type="text" id="misc" name="misc" />
    </div>
    

### [Nesting with CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#nesting_with_css_variables)

You can use `calc()` with [CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables)
. Consider the following code:

css

    .foo {
      --width-a: 100px;
      --width-b: calc(var(--width-a) / 2);
      --width-c: calc(var(--width-b) / 2);
      width: var(--width-c);
    }
    

After all variables are expanded, `--width-c`'s value will be `calc(calc(100px / 2) / 2)`. When it's assigned to `.foo`'s width property, all inner `calc()` functions (no matter how deeply nested) will be flattened to just parentheses. Therefore, the `width` property's value will eventually be `calc((100px / 2) / 2)`, which equals `25px`. In short, a `calc()` inside of a `calc()` is identical to using parentheses.

### [Adjusting color channels in relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#adjusting_color_channels_in_relative_colors)

The `calc()` function can be used to adjust individual color channels in [relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
 without the need for storing color channel values as variables.

In the example below, the first paragraph uses a [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
. In the paragraphs that follow, `calc()` is used with the [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
 and [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
 functions to adjust the values of each color channel relative to the original named color.

html

    <p class="original">Original text color in rebeccapurple</p>
    <p class="increase-hue">Hue increased by 80</p>
    <p class="increase-lightness">Lightness increased by 20</p>
    <p class="decrease-lightness">Lightness decreased by 10</p>
    

    p {
      font-family: monospace;
      font-size: 16px;
    }
    

css

    .original {
      color: rebeccapurple;
    }
    
    .increase-hue {
      color: lch(from rebeccapurple l c calc(h + 80));
    }
    
    .increase-lightness {
      color: lch(from rebeccapurple calc(l + 20) c h);
    }
    
    .decrease-lightness {
      color: lch(from rebeccapurple calc(l - 10) c h);
    }
    

For another example of using the `calc()` function to derive relative colors, see the [Using math functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors#using_math_functions)
 section on the _Using relative colors_ page.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# calc-func](https://drafts.csswg.org/css-values/#calc-func) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#see_also)

--------------------------------------------------------------------------------------------

*   [`<calc-sum>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
    
*   [`<calc-keyword>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
    
*   [CSS functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
    
*   [A Complete Guide to calc() in CSS](https://css-tricks.com/a-complete-guide-to-calc-in-css/ "External link (opens in new tab)")
     (CSS-Tricks)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/calc/index.md?plain=1 "Folder: en-us/web/css/reference/values/calc (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcalc&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcalc%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcalc%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcalc%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")