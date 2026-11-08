*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#mdn-search)
    

`hsl()` CSS function
====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** The `hsla()` functional notation is an alias for `hsl()`. They are exactly equivalent. It is recommended to use `hsl()`.

The **`hsl()`** functional notation expresses a color in the [sRGB](https://developer.mozilla.org/en-US/docs/Glossary/RGB)
 [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 according to its _hue_, _saturation_, and _lightness_ components. An optional _alpha_ component represents the color's transparency.

Defining _complementary colors_ with `hsl()` can be done by adding or subtracting 180 degrees from the hue value, as they are positioned on the same diameter of the [color wheel](https://developer.mozilla.org/en-US/docs/Glossary/Color_wheel)
. For example, if the hue angle of a color is `10deg`, its complementary has `190deg` as its hue angle.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#try_it)

---------------------------------------------------------------------------------------------------

    background: hsl(50 80% 40%);
    

    background: hsl(150deg 30% 60%);
    

    background: hsl(0.3turn 60% 45% / 0.7);
    

    background: hsl(0 80% 50% / 25%);
    

    <section id="default-example">
      <div class="transition-all" id="example-element"></div>
    </section>
    

    #example-element {
      min-width: 100%;
      min-height: 100%;
      padding: 10%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Absolute values */
    hsl(120deg 75% 25%)
    hsl(120 75 25) /* deg and % units are optional */
    hsl(120deg 75% 25% / 60%)
    hsl(none 75% 25%)
    
    /* Relative values */
    hsl(from green h s l / 0.5)
    hsl(from #123456 h s calc(l + 20))
    hsl(from rgb(200 0 0) calc(h + 30) s calc(l + 30))
    
    /* Legacy 'hsla()' alias */
    hsla(120deg 75% 25% / 60%)
    
    /* Legacy format */
    hsl(120, 75%, 25%)
    hsl(120deg, 75%, 25%, 0.8)
    

**Note:** `hsl()`/`hsla()` can also be written in a legacy form in which all values are separated with commas, for example `hsl(120, 75%, 25%)` or `hsla(120deg, 75%, 25%, 0.8)`. The `none` value is not permitted in the comma-separated legacy syntax, the `deg` on the hue value is optional, and the `%` units are required for the saturation and lightness values.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#values)

Below are descriptions of the allowed values for both absolute and [relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
.

#### Absolute value syntax

hsl(H S L\[ / A\])

The parameters are as follows:

[`H`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#h)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, or the keyword `none` (equivalent to `0deg` in this case) representing the color's [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
 angle.

**Note:** The angles corresponding to particular hues differ across the sRGB (used by `hsl()` and [`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
), CIELAB (used by [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
), and Oklab (used by [`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
) color spaces. See the [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
 reference page for more detail and examples.

[`S`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#s)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 or the keyword `none` (equivalent to `0%` in this case). This value represents the color's saturation. Here `100%` is completely saturated, while `0%` is completely unsaturated (gray).

[`L`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#l)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 or the keyword `none` (equivalent to `0%` in this case). This value represents the color's lightness. Here `100%` is white, `0%` is black, and `50%` is "normal".

[`A` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#a)

An [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 representing the alpha channel value of the color, where the number `0` corresponds to `0%` (fully transparent) and `1` corresponds to `100%` (fully opaque). Additionally, the keyword `none` can be used to explicitly specify no alpha channel. If the `A` channel value is not explicitly specified, it defaults to 100%. If included, the value is preceded by a slash (`/`).

**Note:** See [Missing color components](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#missing_color_components)
 for more information on the effect of `none`.

**Note:** Absolute `hsl()` colors are serialized to [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
 values. The values of the red, green, and blue components may be rounded in serialization.

#### Relative value syntax

hsl(from <color> H S L\[ / A\])

The parameters are as follows:

[`from <color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#from_color)

The keyword `from` is always included when defining a relative color, followed by a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value representing the **origin color**. This is the original color that the relative color is based on. The origin color can be _any_ valid [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 syntax, including another relative color.

[`H`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#h_2)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, or the keyword `none` (equivalent to `0deg` in this case) representing the output color's [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
 angle.

[`S`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#s_2)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 or the keyword `none` (equivalent to `0%` in this case). This represents the saturation of the output color. Here `100%` is completely saturated, while `0%` is completely unsaturated (gray).

[`L`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#l_2)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 or the keyword `none` (equivalent to `0%` in this case). This represents the lightness of the output color. Here `100%` is white, `0%` is black, and `50%` is "normal".

[`A` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#a_2)

An [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 representing the alpha channel value of the output color, where the number `0` corresponds to `0%` (fully transparent) and `1` corresponds to `100%` (fully opaque). Additionally, the keyword `none` can be used to explicitly specify no alpha channel. If the `A` channel value is not explicitly specified, it defaults to the alpha channel value of the origin color. If included, the value is preceded by a slash (`/`).

**Note:** To fully enable the representation of the full spectrum of visible colors, the output of relative `hsl()` color functions is serialized to `color(srgb)`. That means that querying the output color value via the [`HTMLElement.style`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)
 property or the [`CSSStyleDeclaration.getPropertyValue()`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration/getPropertyValue)
 method returns the output color as a [`color(srgb ...)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color)
 value.

#### Defining relative color output channel components

When using relative color syntax inside an `hsl()` function, the browser converts the origin color into an equivalent HSL color (if it is not already specified as such). The color is defined as three distinct color channel values — `h` (hue), `s` (saturation), and `l` (lightness) — plus an alpha channel value (`alpha`). These channel values are made available inside the function to be used when defining the output color channel values:

*   The `h` value is resolved to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
     between `0` and `360`, inclusive, that represents the origin color's [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
     degree value.
*   The `s` and `l` values are each resolved to a `<number>` between `0` and `100`, inclusive, where `100` is equivalent to `100%`.
*   The `alpha` value is resolved to a `<number>` between `0` and `1`, inclusive.

When defining a relative color, the different channels of the output color can be expressed in several different ways. Below, we'll study some examples to illustrate these.

In the first two examples below, we are using relative color syntax. However, the first one outputs the same color as the origin color and the second one outputs a color not based on the origin color at all. They don't really create relative colors! You'd be unlikely to ever use these in a real codebase, and would probably just use an absolute color value instead. We included these examples as a starting point for learning about relative `hsl()` syntax.

Let's start with an origin color of `rgb(255 0 0)` (equivalent to `hsl(0 100% 50%)`). The following function outputs the same color as the origin color — it uses the origin color's `h`, `s`, and `l` channel values (`0`, `100%`, and `50%`) as the output channel values:

css

    hsl(from rgb(255 0 0) h s l)
    

This function's output color is the sRGB `color()` equivalent of `hsl(0 100% 50%)`: `color(srgb 1 0 0)`.

The next function uses absolute values for the output color's channel values, outputting a completely different color not based on the origin color:

css

    hsl(from rgb(255 0 0) 240 60% 70%)
    

In the above case, the output color is the sRGB `color()` equivalent of `hsl(240 60% 70%)`: `color(srgb 0.52 0.52 0.88)`.

The following function creates a relative color based on the origin color:

css

    hsl(from rgb(255 0 0) h 30% 60%)
    

This example:

*   Converts the origin color (`rgb(255 0 0)`) into an `hsl()` equivalent (`hsl(0 100% 50%)`).
*   Sets the `H` channel value for the output color to those of the origin color `hsl()` equivalent's `H` channel value — `0`.
*   Sets the output color's `S` and `L` channel values to new values not based on the origin color: `30%` and `60%`, respectively.

The final output color is the equivalent of `hsl(0 30% 60%)` in the sRGB color space — `color(srgb 0.72 0.48 0.48)`.

**Note:** As mentioned above, if the output color is using a different color model to the origin color, the origin color is converted to the same model as the output color in the background so that it can be represented in a way that is compatible (i.e., using the same channels).

In the examples we've seen so far in this section, the alpha channels have not been explicitly specified for either the origin or output colors. When the output color alpha channel is not specified, it defaults to the same value as the origin color alpha channel. When the origin color alpha channel is not specified (and it is not a relative color), it defaults to `1`. Therefore, the origin and output alpha channel values are `1` for the above examples.

Let's look at some examples that specify origin and output alpha channel values. The first one specifies the output alpha channel value as being the same as the origin alpha channel value, whereas the second one specifies a different output alpha channel value, unrelated to the origin alpha channel value.

css

    hsl(from rgb(255 0 0 / 0.8) h s l / alpha)
    /* Computed output color: color(srgb 1 0 0 / 0.8) */
    
    hsl(from rgb(255 0 0 / 0.8) h s l / 0.5)
    /* Computed output color: color(srgb 1 0 0 / 0.5) */
    

In the following example, the `rgb()` origin color is again converted into an `hsl()` representation — `hsl(0 100% 50% / 0.8)`. [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 calculations are applied to the `H`, `S`, `L`, and `A` values, and the final output color is the equivalent of `hsl(60 80% 30% / 0.7)` in the sRGB color space: `color(srgb 0.72 0.72 0.08 / 0.7)`.

css

    hsl(from rgb(255 0 0 / 0.8) calc(h + 60) calc(s - 20) calc(l - 10) / calc(alpha - 0.1))
    

**Note:** Because the origin color channel values are resolved to `<number>` values, you have to add numbers to them when using them in calculations, even in cases where a channel would normally accept `<percentage>`, `<angle>`, or other value types. Adding a `<percentage>` to a `<number>`, for example, doesn't work.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

<hsl()> =   
  <legacy-hsl-syntax>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <modern-hsl-syntax>    
  
<legacy-hsl-syntax> =   
  hsl( <hue> , [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 , [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 , <alpha-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<modern-hsl-syntax> =   
  hsl( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 from [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <hue> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <alpha-value> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<hue>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
 =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
     
  
[<alpha-value>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#examples)

-------------------------------------------------------------------------------------------------------

### [Using hsl() with conic-gradient()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#using_hsl_with_conic-gradient)

The `hsl()` function works well with [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
 as both deal with angles.

    <div></div>
    

#### CSS

css

    div {
      width: 100px;
      height: 100px;
      background: conic-gradient(
        hsl(360 100% 50%),
        hsl(315 100% 50%),
        hsl(270 100% 50%),
        hsl(225 100% 50%),
        hsl(180 100% 50%),
        hsl(135 100% 50%),
        hsl(90 100% 50%),
        hsl(45 100% 50%),
        hsl(0 100% 50%)
      );
      clip-path: circle(closest-side);
    }
    

#### Result

### [Using relative colors with hsl()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#using_relative_colors_with_hsl)

This example styles three [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements with different background colors. The middle one is given the unmodified `--base-color`, while the left and right ones are given lightened and darkened variants of that `--base-color`.

These variants are defined using relative colors — the `--base-color` [custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 is passed into an `hsl()` function, and the output color has its lightness channel modified to achieve the desired effect via a `calc()` function, while the hue and saturation are left unchanged. The lightened color has 20% added to the lightness channel, and the darkened color has 20% subtracted from it.

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
    }
    
    #one {
      background-color: hsl(from var(--base-color) h s calc(l + 20));
    }
    
    #two {
      background-color: var(--base-color);
    }
    
    #three {
      background-color: hsl(from var(--base-color) h s calc(l - 20));
    }
    
    /* Use @supports to add in support for old syntax that requires % units to
       be specified in lightness calculations */
    @supports (color: hsl(from red h s calc(l - 20%))) {
      #one {
        background-color: hsl(from var(--base-color) h s calc(l + 20%));
      }
    
      #three {
        background-color: hsl(from var(--base-color) h s calc(l - 20%));
      }
    }
    

#### Result

The output is as follows:

### [Legacy syntax: comma-separated values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#legacy_syntax_comma-separated_values)

For legacy reasons, the `hsl()` function accepts a form in which all values are separated using commas.

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
      background-color: hsl(0 100% 50% / 50%);
    }
    
    div.comma-separated {
      background-color: hsl(0, 100%, 50%, 0.5);
    }
    

#### Result

### [Legacy versus modern syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#legacy_versus_modern_syntax)

The example demonstrates how the `hsla()` syntax is an alias for `hsl()`; both are supported using both modern and legacy (comma-separated) syntaxes.

#### HTML

html

    <div class="modern">HSL</div>
    <div class="legacy">HSL</div>
    <div class="modernWithAlpha">HSL</div>
    <div class="modernHSLA">HSLA</div>
    <div class="legacyHSLA">HSLA</div>
    

#### CSS

css

    div {
      width: 100px;
      min-height: 50px;
      font-family: sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    body {
      display: flex;
      gap: 20px;
    }
    

css

    div.modern {
      background-color: hsl(90 80% 50%);
    }
    
    div.legacy {
      background-color: hsl(90, 80%, 50%);
    }
    
    div.modernWithAlpha {
      background-color: hsl(90 80% 50% / 50%);
    }
    
    div.modernHSLA {
      background-color: hsla(90 80% 50% / 50%);
    }
    
    div.legacyHSLA {
      background-color: hsla(90, 80%, 50%, 0.5);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 5  <br>\# relative-HSL](https://drafts.csswg.org/css-color-5/#relative-HSL) |
| [CSS Color Module Level 4  <br>\# the-hsl-notation](https://drafts.csswg.org/css-color/#the-hsl-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl#see_also)

-------------------------------------------------------------------------------------------------------

*   [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
     data type
*   [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
     and [`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
     color functions
*   [Hue interpolation in `color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#using_hue_interpolation_in_color-mix)
    
*   [List of all color notations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [Color format converter tool](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_format_converter)
    
*   [Using relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
    
*   [CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module
*   [Color picker tool](https://apps.colorjs.io/picker/ "External link (opens in new tab)")
     by Lea Verou

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/color_value/hsl/index.md?plain=1 "Folder: en-us/web/css/reference/values/color_value/hsl (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Fhsl&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Fhsl%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Fhsl%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Fhsl%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")