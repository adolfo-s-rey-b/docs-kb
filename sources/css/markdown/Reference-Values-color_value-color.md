*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#mdn-search)
    

`color()` CSS function
======================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since May 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`color()`** functional notation allows a color to be specified in a particular, specified [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 rather than the implicit sRGB color space that most of the other color functions operate in.

Support for a particular color space can be detected with the [`color-gamut`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut)
 CSS media feature.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Absolute values */
    color(display-p3 1 0.5 0);
    color(display-p3 1 0.5 0 / .5);
    
    /* Relative values */
    color(from green srgb r g b / 0.5)
    color(from #123456 xyz calc(x + 0.75) y calc(z - 0.35))
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#values)

Below are descriptions of the allowed values for both absolute and [relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
.

#### Absolute value syntax

color(colorspace c1 c2 c3\[ / A\])

The parameters are as follows:

[`colorspace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#colorspace)

An [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
 denoting one of the predefined color spaces: `srgb`, `srgb-linear`, `display-p3`, `display-p3-linear`, `a98-rgb`, `prophoto-rgb`, `rec2020`, `xyz`, `xyz-d50`, or `xyz-d65`.

[`c1`, `c2`, `c3`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#c1)

Each value can be written as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or the keyword `none` (equivalent to `0` in this case). These values represent the component values for the colorspace. When using a `<number>` value, generally, `0` to `1` represents the bounds of the color space. Values outside of that range are permitted but will be out of [gamut](https://developer.mozilla.org/en-US/docs/Glossary/Gamut)
 for the given color space. When using a percentage value, `100%` represents `1` and `0%` represents `0`.

[`A` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#a)

An [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 representing the alpha channel value of the color, where the number `0` corresponds to `0%` (fully transparent) and `1` corresponds to `100%` (fully opaque). Additionally, the keyword `none` can be used to explicitly specify no alpha channel. If the `A` channel value is not explicitly specified, it defaults to 100%. If included, the value is preceded by a slash (`/`).

**Note:** See [Missing color components](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#missing_color_components)
 for more information on the effect of `none`.

#### Relative value syntax

color(from <color> colorspace c1 c2 c3\[ / A\])

The parameters are as follows:

[`from <color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#from_color)

The keyword `from` is always included when defining a relative color, followed by a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value representing the **origin color**. This is the original color that the relative color is based on. The origin color can be _any_ valid [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 syntax, including another relative color.

[`colorspace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#colorspace_2)

An [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
 denoting the [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 of the output color, generally one of the predefined color spaces: `srgb`, `srgb-linear`, `display-p3`, `display-p3-linear`, `a98-rgb`, `prophoto-rgb`, `rec2020`, `xyz`, `xyz-d50`, or `xyz-d65`.

[`c1`, `c2`, `c3`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#c1_2)

Each value can be written as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or the keyword `none` (equivalent to `0` in this case). These values represent the component values for the output color. When using a `<number>` value, generally `0` to `1` represents the bounds of the color space. Values outside of that range are permitted but will be out of [gamut](https://developer.mozilla.org/en-US/docs/Glossary/Gamut)
 for the given color space. Generally, when using a percentage value, `100%` represents `1` and `0%` represents `0`.

[`A` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#a_2)

An [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 representing the alpha channel value of the output color, where the number `0` corresponds to `0%` (fully transparent) and `1` corresponds to `100%` (fully opaque). Additionally, the keyword `none` can be used to explicitly specify no alpha channel. If the `A` channel value is not explicitly specified, it defaults to the alpha channel value of the origin color. If included, the value is preceded by a slash (`/`).

#### Defining relative color output channel components

When using relative color syntax inside a `color()` function, the browser converts the origin color into an equivalent color in the specified color space (if it is not already specified as such). The color is defined as three distinct color channel values plus an alpha channel value (`alpha`). These channel values are made available inside the function to be used when defining the output color channel values:

*   The three color channel values of the origin color are resolved to a `<number>`. For predefined color spaces, depending on which is specified, these values will be one of the following:
    
    *   `r`, `g`, and `b`: Color channel values for the RGB-based color spaces `srgb`, `srgb-linear`, `display-p3`, `display-p3-linear`, `a98-rgb`, `prophoto-rgb`, and `rec2020`.
        
    *   `x`, `y`, and `z`: Color channel values for the CIE XYZ-based color spaces `xyz`, `xyz-d50`, and `xyz-d65`.
        
        **Note:** Each of these values is usually between `0` and `1` but, as explained above, they may be outside these bounds.
        
        **Note:** Referencing `r`, `g`, and `b` values inside a `color()` function with an XYZ-based colorspace, `x`, `y`, and `z` values inside a `color()` function with an RGB-based colorspace, or any other characters, is invalid. The origin color channel values available inside the function must match the specified type of colorspace.
        
*   `alpha`: The color's transparency value, resolved to a `<number>` between `0` and `1`, inclusive.
    

When defining a relative color, the different channels of the output color can be expressed in several different ways. Below, we'll study some examples to illustrate these.

In the first two examples below, we are using relative color syntax. However, the first one outputs the same color as the origin color and the second one outputs a color not based on the origin color at all. They don't really create relative colors! You'd be unlikely to ever use these in a real codebase, and would probably just use an absolute color value instead. We included these examples as a starting point for learning about relative `color()` syntax.

Let's start with an origin color of `hsl(0 100% 50%)` (equivalent to `red`). While you are unlikely to ever write the following functions because they output the same color as the origin color, this demonstrates how to use the origin color channel values as the output channel values:

css

    color(from hsl(0 100% 50%) srgb r g b)
    color(from hsl(0 100% 50%) xyz x y z)
    

These functions' output colors are `color(srgb 1 0 0)` and `color(xyz-d65 0.412426 0.212648 0.0193173)`, respectively.

The next functions use absolute values for the output color channel values, outputting completely different colors not based on the origin color:

css

    color(from hsl(0 100% 50%) srgb 0.749938 0 0.609579)
    /* Computed output color: color(srgb 0.749938 0 0.609579) */
    
    color(from hsl(0 100% 50%) xyz 0.75 0.6554 0.1)
    /* Computed output color: color(xyz-d65 0.75 0.6554 0.1 */
    

The following functions use two of the origin color channel values for the output color channel values (`r` and `b`, and `x` and `y`, respectively), but use a new value for the other output channel value (`g` and `z`, respectively), creating a relative color based on the origin color in each case:

css

    color(from hsl(0 100% 50%) srgb r 1 b)
    /* Computed output color: color(srgb 1 1 0) */
    
    color(from hsl(0 100% 50%) xyz x y 0.5)
    /* Computed output color: color(xyz-d65 0.412426 0.212648 0.5) */
    

**Note:** As mentioned above, if the output color is using a different color model to the origin color, the origin color is converted to the same model as the output color in the background so that it can be represented in a way that is compatible (i.e., using the same channels). For example, the [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
 color `hsl(0 100% 50%)` is converted to `color(srgb 1 0 0)` in the first case above and `color(xyz 0.412426 0.212648 0.5)` in the second case.

In the examples we've seen so far in this section, the alpha channels have not been explicitly specified for either the origin or output colors. When the output color alpha channel is not specified, it defaults to the same value as the origin color alpha channel. When the origin color alpha channel is not specified (and it is not a relative color), it defaults to `1`. Therefore, the origin and output alpha channel values are `1` for the above examples.

Let's look at some examples that specify origin and output alpha channel values. The first one specifies the output alpha channel value as being the same as the origin alpha channel value, whereas the second one specifies a different output alpha channel value, unrelated to the origin alpha channel value.

css

    color(from hsl(0 100% 50% / 0.8) srgb r g b / alpha)
    /* Computed output color: color(srgb 1 0 0 / 0.8) */
    
    color(from hsl(0 100% 50% / 0.8) xyz x y z / 0.5)
    /* Computed output color: color(xyz-d65 0.412426 0.212648 0.0193173 / 0.5) */
    

The following examples use [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 functions to calculate new channel values for the output colors that are relative to the origin color channel values:

css

    color(from hsl(0 100% 50%) srgb calc(r - 0.4) calc(g + 0.1) calc(b + 0.6) / calc(alpha - 0.1))
    /* Computed output color: color(srgb 0.6 0.1 0.6 / 0.9)  */
    
    color(from hsl(0 100% 50%) xyz calc(x - 0.3) calc(y + 0.3) calc(z + 0.3) / calc(alpha - 0.1))
    /* Computed output color: color(xyz-d65 0.112426 0.512648 0.319317 / 0.9) */
    

**Note:** Because the origin color channel values are resolved to `<number>` values, you have to add numbers to them when using them in calculations, even in cases where a channel would normally accept `<percentage>`, `<angle>`, or other value types. Adding a `<percentage>` to a `<number>`, for example, doesn't work.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

<color()> =   
  color( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 from [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 <colorspace-params> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <alpha-value> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<colorspace-params> =   
  <custom-params>          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <predefined-rgb-params>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <xyz-params>               
  
[<alpha-value>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
<custom-params> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    
  
<predefined-rgb-params> =   
  <predefined-rgb> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
<xyz-params> =   
  <xyz-space> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
<predefined-rgb> =   
  srgb               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  srgb-linear        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  display-p3         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  display-p3-linear  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  a98-rgb            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  prophoto-rgb       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rec2020            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rec2100-pq         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rec2100-hlg        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rec2100-linear       
  
<xyz-space> =   
  xyz      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d50  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d65    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#examples)

---------------------------------------------------------------------------------------------------------

### [Using predefined color spaces with color()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#using_predefined_color_spaces_with_color)

The following example shows the effect of varying the lightness, a-axis, and b-axis values of the `color()` function.

#### HTML

html

    <div data-color="red-a98-rgb"></div>
    <div data-color="red-prophoto-rgb"></div>
    <div data-color="green-srgb-linear"></div>
    <div data-color="green-display-p3"></div>
    <div data-color="green-display-p3-linear"></div>
    <div data-color="blue-rec2020"></div>
    <div data-color="blue-srgb"></div>
    

#### CSS

    div {
      width: 50px;
      height: 50px;
      padding: 5px;
      margin: 5px;
      display: inline-block;
      border: 1px solid black;
    }
    

css

    [data-color="red-a98-rgb"] {
      background-color: color(a98-rgb 1 0 0);
    }
    [data-color="red-prophoto-rgb"] {
      background-color: color(prophoto-rgb 1 0 0);
    }
    /* sRGB gamut, linear-light — full brightness (green channel 100%) */
    [data-color="green-srgb-linear"] {
      background-color: color(srgb-linear 0 1 0);
    }
    /* P3 gamut (wider), gamma-encoded — low brightness (green channel ~21% light output) */
    [data-color="green-display-p3"] {
      background-color: color(display-p3 0 0.5 0);
    }
    /* P3 gamut (wider), linear-light — half brightness (green channel at 50% light output) */
    [data-color="green-display-p3-linear"] {
      background-color: color(display-p3-linear 0 0.5 0);
    }
    [data-color="blue-rec2020"] {
      background-color: color(rec2020 0 0 1);
    }
    [data-color="blue-srgb"] {
      background-color: color(srgb 0 0 1);
    }
    

#### Result

### [Using the xyz color space with color()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#using_the_xyz_color_space_with_color)

The following example shows how to use the `xyz` color space to specify a color.

#### HTML

html

    <div data-color="red"></div>
    <div data-color="green"></div>
    <div data-color="blue"></div>
    

#### CSS

    div {
      width: 50px;
      height: 50px;
      padding: 5px;
      margin: 5px;
      display: inline-block;
      border: 1px solid black;
    }
    

css

    [data-color="red"] {
      background-color: color(xyz 45 20 0);
    }
    
    [data-color="green"] {
      background-color: color(xyz-d50 0.3 80 0.3);
    }
    
    [data-color="blue"] {
      background-color: color(xyz-d65 5 0 50);
    }
    

#### Result

### [Using color-gamut media queries with color()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#using_color-gamut_media_queries_with_color)

This example shows how to use the [`color-gamut`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut)
 media query to detect support for a particular color space and use that color space to specify a color.

#### HTML

html

    <div></div>
    <div></div>
    <div></div>
    

#### CSS

    div {
      width: 50px;
      height: 50px;
      padding: 5px;
      margin: 5px;
      display: inline-block;
      border: 1px solid black;
    }
    

css

    @media (color-gamut: p3) {
      div {
        background-color: color(display-p3 1 0 0);
      }
    }
    
    @media (color-gamut: srgb) {
      div:nth-child(2) {
        background-color: color(srgb 1 0 0);
      }
    }
    
    @media (color-gamut: rec2020) {
      div:nth-child(3) {
        background-color: color(rec2020 1 0 0);
      }
    }
    

#### Result

### [Using relative colors with color()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#using_relative_colors_with_color)

This example styles three [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements with different background colors. The middle one is given the unmodified `--base-color`, while the left and right ones are given lightened and darkened variants of that `--base-color`.

These variants are defined using relative colors — the `--base-color` [custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 is passed into a `color()` function, and the output colors have their `g` and `b` channels modified to achieve the desired effect via `calc()` functions. The lightened color has 15% added to those channels, and the darkened color has 15% subtracted from those channels.

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
      background-color: color(
        from var(--base-color) display-p3 r calc(g + 0.15) calc(b + 0.15)
      );
    }
    
    #two {
      background-color: var(--base-color);
    }
    
    #three {
      background-color: color(
        from var(--base-color) display-p3 r calc(g - 0.15) calc(b - 0.15)
      );
    }
    
    /* Use @supports to add in support old syntax that requires r g b values
       to be specified as percentages (with units) in calculations.
       This is required for Safari 16.4+ */
    @supports (color: color(from red display-p3 r g calc(b + 30%))) {
      #one {
        background-color: color(
          from var(--base-color) display-p3 r calc(g + 15%) calc(b + 15%)
        );
      }
    
      #three {
        background-color: color(
          from var(--base-color) display-p3 r calc(g - 15%) calc(b - 15%)
        );
      }
    }
    

#### Result

The output is as follows:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 5  <br>\# color-function](https://drafts.csswg.org/css-color-5/#color-function) |
| [CSS Color Module Level 5  <br>\# relative-color-function](https://drafts.csswg.org/css-color-5/#relative-color-function) |
| [CSS Color Module Level 4  <br>\# color-function](https://drafts.csswg.org/css-color/#color-function) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#see_also)

---------------------------------------------------------------------------------------------------------

*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
     property
*   [The `<color>` data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     for a list of all color notations
*   [Using relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
    
*   [Color\_format\_converter tool](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_format_converter)
    
*   [CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module
*   [`color-gamut`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut)
     media feature
*   [Wide Gamut Color in CSS with Display-p3](https://webkit.org/blog/10042/wide-gamut-color-in-css-with-display-p3/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/color_value/color/index.md?plain=1 "Folder: en-us/web/css/reference/values/color_value/color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Fcolor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Fcolor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Fcolor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Fcolor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc44003c788a907ef19e0d766e98f29ffca5b6798%0A*+Document+last+modified%3A+2026-10-08T10%3A49%3A18.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")