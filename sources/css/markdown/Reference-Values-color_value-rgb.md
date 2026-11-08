*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#mdn-search)
    

`rgb()` CSS function
====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** The `rgba()` functional notation is an alias for `rgb()`. They are exactly equivalent. It is recommended to use `rgb()`.

The **`rgb()`** functional notation expresses a color in the [sRGB](https://developer.mozilla.org/en-US/docs/Glossary/RGB)
 [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 according to its red, green, and blue components. An optional alpha component represents the color's transparency.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#try_it)

---------------------------------------------------------------------------------------------------

    background: rgb(31 120 50);
    

    background: rgb(30% 20% 50%);
    

    background: rgb(255 122 127 / 80%);
    

    background: rgb(255 122 127 / 0.2);
    

    <section id="default-example">
      <div class="transition-all" id="example-element"></div>
    </section>
    

    #example-element {
      min-width: 100%;
      min-height: 100%;
      padding: 10%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Absolute values */
    rgb(255 255 255)
    rgb(255 255 255 / 50%)
    
    /* Relative values */
    rgb(from green r g b / 0.5)
    rgb(from #123456 calc(r + 40) calc(g + 40) b)
    rgb(from hwb(120deg 10% 20%) r g calc(b + 200))
    
    /* Legacy 'rgba()' alias */
    rgba(0 255 255)
    
    /* Legacy format */
    rgb(0, 255, 255)
    rgb(0, 255, 255, 50%)
    

**Note:** For compatibility reasons, [Web API](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle)
\-serialized color values are expressed as `rgb()` colors if the alpha channel value is exactly 1, and `rgba()` colors otherwise. In both cases, legacy syntax is used, with commas as separators (for example `rgb(255, 0, 0)`).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#values)

Below are descriptions of the allowed values for both absolute and [relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
.

#### Absolute value syntax

rgb(R G B\[ / A\])

The parameters are as follows:

[`R`, `G`, `B`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#r)

Each value can be represented as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 between `0` and `255`, a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 between `0%` and `100%`, or the keyword `none` (equivalent to `0%` in this case). These values represent the red, green, and blue channels, respectively.

[`A` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#a)

An [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 representing the alpha channel value of the color, where the number `0` corresponds to `0%` (fully transparent) and `1` corresponds to `100%` (fully opaque). Additionally, the keyword `none` can be used to explicitly specify no alpha channel. If the `A` channel value is not explicitly specified, it defaults to 100%. If included, the value is preceded by a slash (`/`).

**Note:** See [Missing color components](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#missing_color_components)
 for more information on the effect of `none`.

#### Relative value syntax

rgb(from <color> R G B\[ / A\])

The parameters are as follows:

[`from <color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#from_color)

The keyword `from` is always included when defining a relative color, followed by a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value representing the **origin color**: This is the original color that the relative color is based on. The origin color can be _any_ valid [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 syntax, including another relative color.

[`R`, `G`, `B`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#r_2)

Each value can be represented as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 between `0` and `255`, a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 between `0%` and `100%`, or the keyword `none` (equivalent to `0%` in this case). These values represent the red, green, and blue channel values of the output color, respectively.

[`A` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#a_2)

An [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 representing the alpha channel value of the output color, where the number `0` corresponds to `0%` (fully transparent) and `1` corresponds to `100%` (fully opaque). Additionally, the keyword `none` can be used to explicitly specify no alpha channel. If the `A` channel value is not explicitly specified, it defaults to the alpha channel value of the origin color. If included, the value is preceded by a slash (`/`).

**Note:** To fully enable the representation of the full spectrum of visible colors, the output of relative `rgb()` color functions is serialized to `color(srgb)`. That means that querying the output color value via the [`HTMLElement.style`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)
 property or the [`CSSStyleDeclaration.getPropertyValue()`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration/getPropertyValue)
 method returns the output color as a [`color(srgb ...)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color)
 value.

#### Defining relative color output channel components

When using relative color syntax inside an `rgb()` function, the browser converts the origin color into an equivalent RGB color (if it is not already specified as such). The color is defined as three distinct color channel values — `r` (red), `g` (green), and `b` (blue) — plus an alpha channel value (`alpha`). These channel values are made available inside the function to be used when defining the output color channel values:

*   The `r`, `g` and `b` values are each resolved to `<number>`s between `0` and `255`, inclusive.
*   The `alpha` channel is resolved to a `<number>` between `0` and `1`, inclusive.

When defining a relative color, the different channels of the output color can be expressed in several different ways. Below, we'll study some examples to illustrate these.

In the first two examples below, we are using relative color syntax. However, the first one outputs the same color as the origin color and the second one outputs a color not based on the origin color at all. They don't really create relative colors! You'd be unlikely to ever use these in a real codebase, and would probably just use an absolute color value instead. We included these examples as a starting point for learning about relative `rgb()` syntax.

Let's start with an origin color of `hsl(0 100% 50%)` (equivalent to `rgb(255 0 0)`). The following function outputs the same color as the origin color — it uses the origin color's `r`, `g`, and `b` channel values (`255`, `0`, and `0`) as the output channel values:

css

    rgb(from hsl(0 100% 50%) r g b)
    

This function's output color is the sRGB `color()` equivalent of `rgb(255 0 0)`: `color(srgb 1 0 0)`.

The next function uses absolute values for the output color's channel values, outputting a completely different color not based on the origin color:

css

    rgb(from hsl(0 100% 50%) 132 132 224)
    

In the above case, the output color is the sRGB `color()` equivalent of `rgb(132 132 224)`: `color(srgb 0.517647 0.517647 0.878431)`.

The following function creates a relative color based on the origin color:

css

    rgb(from hsl(0 100% 50%) r 80 80)
    

This example:

*   Converts the origin color (`hsl(0 100% 50%)`) into an `rgb()` equivalent (`rgb(255 0 0)`).
*   Sets the `R` channel value for the output color to the origin color `rgb()` equivalent's `R` channel value — `255`.
*   Sets the output color's `G` and `B` channel values to new values not based on the origin color: `80` and `80`, respectively.

The final output color is the equivalent of `rgb(255 80 80)` in the sRGB color space — `color(srgb 1 0.313726 0.313726)`.

**Note:** As mentioned above, if the output color is using a different color model to the origin color, the origin color is converted to the same model or space as the output color in the background so that it can be represented in a way that is compatible (i.e., using the same channels).

In the examples we've seen so far in this section, the alpha channels have not been explicitly specified for either the origin or output colors. When the output color alpha channel is not specified, it defaults to the same value as the origin color alpha channel. When the origin color alpha channel is not specified (and it is not a relative color), it defaults to `1`. Therefore, the origin and output alpha channel values are `1` for the above examples.

Let's look at some examples that specify origin and output alpha channel values. The first one specifies the output alpha channel value as being the same as the origin alpha channel value, whereas the second one specifies a different output alpha channel value, unrelated to the origin alpha channel value.

css

    rgb(from hsl(0 100% 50% / 0.8) r g b / alpha)
    /* Computed output color: color(srgb 1 0 0 / 0.8) */
    
    rgb(from hsl(0 100% 50% / 0.8) r g b / 0.5)
    /* Computed output color: color(srgb 1 0 0 / 0.5) */
    

In the following example, the `hsl()` origin color is again converted into an `rgb()` representation — `rgb(255 0 0)`. [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 calculations are applied to the `R`, `G`, `B`, and `A` values. After calculating, the R, G, B and A values are `127.5`, `25`, `175`, and `0.9` respectively. The final output color is the equivalent of `rgb(127.5 25 175 / 0.9)` in the sRGB color space: `color(srgb 0.5 0.0980392 0.686275 / 0.9)`.

css

    rgb(from hsl(0 100% 50%) calc(r/2) calc(g + 25) calc(b + 175) / calc(alpha - 0.1))
    

**Note:** Because the origin color channel values are resolved to `<number>` values, you have to add numbers to them when using them in calculations, even in cases where a channel would normally accept `<percentage>`, `<angle>`, or other value types. Adding a `<percentage>` to a `<number>`, for example, doesn't work.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

<rgb()> =   
  <legacy-rgb-syntax>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <modern-rgb-syntax>    
  
<legacy-rgb-syntax> =   
  rgb( [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 , <alpha-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rgb( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 , <alpha-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )        
  
<modern-rgb-syntax> =   
  rgb( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 from [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <alpha-value> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<alpha-value>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#examples)

-------------------------------------------------------------------------------------------------------

### [Basic syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#basic_syntax)

In this example, we have three [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements with different background colors displayed over a striped background.

#### HTML

html

    <div>
      <div id="integer"></div>
      <div id="percent"></div>
      <div id="alpha"></div>
    </div>
    

#### CSS

The background colors are set using the `rgb()` color function. The three colors are the same. The third is semi-transparent, so we included a [`repeating-linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
 on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 to better demonstrate the transparency of alpha channels.

    div {
      display: flex;
      gap: 20px;
      height: 50px;
      flex: 1;
    }
    body {
      height: calc(100vh - 20px);
    }
    

css

    body {
      background: repeating-linear-gradient(-45deg, #eeeeee 0 2px, white 2px 6px);
      padding: 10px;
    }
    
    #integer {
      background-color: rgb(189 85 218);
    }
    
    #percent {
      background-color: rgb(74% 33% 85%);
    }
    
    #alpha {
      background-color: rgb(189 85 218 / 0.25);
    }
    

#### Result

### [Using relative colors with rgb()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#using_relative_colors_with_rgb)

This example styles three [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements with different background colors. The left-hand one is given the unmodified `--base-color`, while the middle and right ones are given variants of that `--base-color` that successively remove more from the red channel and add more to the blue channel.

These variants are defined using relative colors — the `--base-color` [custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 is passed into an `rgb()` function, and the output color has its red and blue channels modified to achieve the desired effect via `calc()` functions, while the green channel is left unchanged.

    <div id="container">
      <div class="item" id="one"></div>
      <div class="item" id="two"></div>
      <div class="item" id="three"></div>
    </div>
    

#### CSS

    #container {
      display: flex;
      width: 100vw;
      height: 100vh;
      box-sizing: border-box;
    }
    
    .item {
      flex: 1;
      margin: 20px;
    }
    

css

    :root {
      --base-color: orange;
      /* equal to rgb(255 165 0) */
    }
    
    #one {
      background-color: var(--base-color);
    }
    
    #two {
      background-color: rgb(from var(--base-color) calc(r - 76.5) g calc(b + 76.5));
      /* 76.5 is 30% of 255 */
    }
    
    #three {
      background-color: rgb(from var(--base-color) calc(r - 153) g calc(b + 153));
      /* 153 is 60% of 255 */
    }
    
    /* Use @supports to add in support for old syntax that requires r g b values to
       be specified as percentages (with units) in calculations. This is required
       for Safari 16.4+. */
    @supports (color: rgb(from red r g calc(b + 30%))) {
      #two {
        background-color: rgb(from var(--base-color) calc(r - 30%) g calc(b + 30%));
      }
    
      #three {
        background-color: rgb(from var(--base-color) calc(r - 60%) g calc(b + 60%));
      }
    }
    

#### Result

### [Legacy syntax: comma-separated values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#legacy_syntax_comma-separated_values)

For legacy reasons, the `rgb()` function accepts a form in which all values are separated using commas.

#### HTML

html

    <div class="space-separated"></div>
    <div class="comma-separated"></div>
    

#### CSS

css

    div {
      width: 100px;
      height: 50px;
      margin: 1rem;
    }
    
    div.space-separated {
      background-color: rgb(255 0 0 / 50%);
    }
    
    div.comma-separated {
      background-color: rgb(255, 0, 0, 0.5);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 5  <br>\# relative-RGB](https://drafts.csswg.org/css-color-5/#relative-RGB) |
| [CSS Color Module Level 4  <br>\# rgb-functions](https://drafts.csswg.org/css-color/#rgb-functions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb#see_also)

-------------------------------------------------------------------------------------------------------

*   The [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     data type for a list of all color notations
*   [Color format converter tool](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_format_converter)
    
*   [Using relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
    
*   [CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/color_value/rgb/index.md?plain=1 "Folder: en-us/web/css/reference/values/color_value/rgb (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Frgb&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Frgb%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Frgb%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Frgb%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")