*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#mdn-search)
    

`color-mix()` CSS function
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since May 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`color-mix()`** functional notation takes one or more [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values and returns the result of mixing them in a given colorspace by a given amount.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#syntax)

---------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#parameters)

The `color-mix( <color-interpolation-method>? , [ <color> && <percentage [0,100]>? ]#)` accepts the following parameters:

[`<color-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
 Optional

Specifies what interpolation method should be used to mix the colors. It consists of the `in` keyword followed by a [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 (one of the color spaces listed in the [formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#formal_syntax)
, defaulting to `oklab`), and, optionally, a [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
, which defaults to `shorter hue`.

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

A color to mix; can be any valid `<color>` value.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 Optional

A percentage value specifying the amount of the corresponding color to mix; can be any `<percentage>` value between `0%` and `100%`, inclusive.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#return_value)

A `<color>`; the result of mixing the colors, in the given `<color-space>`, in the specified amounts and hue direction.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#description)

-------------------------------------------------------------------------------------------------------------------

The `color-mix()` function enables mixing one or more [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values of any type, in a specific ratio, in a given colorspace, using either a shorter or longer hue interpolation method. Browsers support a plethora of color spaces; the `color-mix()` function enables a wide range of colors to be mixed, not limited to the sRGB color space.

This demo allows you to select two colors, `color-one` and `color-two`, and mix them, optionally setting each color's percentage, the color space in which the colors are mixed, and the interpolation method. The source colors are shown on the outside, and the mixed color is shown in the middle. You can change colors by clicking on them and choosing a new color using the resulting color picker. Change the percentage values of each color using the sliders. Change the color space via the drop-down menu.

### [Choosing a color space](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#choosing_a_color_space)

Choosing the correct color space is important for producing desired results. Given the same colors to mix, different color spaces may be more appropriate depending on the interpolation use case.

*   If the result of physically mixing colored lights is desired, the CIE XYZ or srgb-linear color space is appropriate, because they are linear in light intensity.
*   If colors need to be evenly spaced perceptually (such as in a gradient), the Oklab (and older Lab) color spaces are appropriate, because they are designed to be perceptually uniform.
*   If avoiding graying out in color mixing is desired, i.e., maximizing chroma throughout the transition, the Oklch (and older LCH) color spaces work well.
*   Only use sRGB if you need to match the behavior of a specific device or software that uses sRGB. The sRGB color space is neither linear-light nor perceptually uniform, and produces poorer results such as overly dark or grayish mixes.

### [Color interpolation method](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#color_interpolation_method)

The [`<color-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
 specifies what interpolation method should be used to mix the colors. It consists of the `in` keyword and the color space the colors should be mixed in. The color space must be one of the available color spaces listed in the [formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#formal_syntax)
. Depending on the color space used, you can optionally direct the hue to be mixed along a longer or shorter path.

The [`<rectangular-color-space>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#rectangular-color-space)
 category includes [`srgb`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#srgb)
, [`srgb-linear`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#srgb-linear)
, [`display-p3`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#display-p3)
, [`a98-rgb`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#a98-rgb)
, [`prophoto-rgb`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#prophoto-rgb)
, [`rec2020`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#rec2020)
, [`lab`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#cielab_color_spaces)
, [`oklab`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#oklab)
, [`xyz`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#xyz_color_spaces)
, [`xyz-d50`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#xyz)
, and [`xyz-d65`](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#xyz-d50)
.

The `<polar-color-space>` category includes [`hsl`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
, [`hwb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
, [`lch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
, and [`oklch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
. With these you can optionally follow the color space name with a [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
. This value defaults to `shorter hue`, but can also be set to `longer hue`, `increasing hue`, or `decreasing hue`.

### [Default color space and interpolation method](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#default_color_space_and_interpolation_method)

When mixing colors without specifying a color space, the `oklab` color space is used.

The following two declarations are equivalent:

When using a polar color space such as `oklch`, the hue interpolation method defaults to `shorter hue`. The following two declarations are equivalent:

### [Color percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#color_percentages)

Each color can be declared with a `<percentage>` value between `0%` and `100%`, which specifies the amount of the corresponding color to mix. The percentages are normalized if the total value of the declared percentages does not equal `100%`.

When two colors are being mixed, the two color percentages (we'll refer to them as `p1` and `p2`) are normalized as follows:

*   If both `p1` and `p2` are omitted, then `p1 = p2 = 50%`.
*   If `p1` is omitted, then `p1 = 100% - p2`.
*   If `p2` is omitted, then `p2 = 100% - p1`.
*   If `p1 = p2 = 0%`, the function is invalid.
*   If `p1 + p2 ≠ 100%`, then `p1' = p1 / (p1 + p2)` and `p2' = p2 / (p1 + p2)`, where `p1'` and `p2'` are the normalization results.
    *   If `p1 + p2 < 100%`, then an alpha multiplier of `p1 + p2` is applied to the resulting color. This is similar to mixing in [`transparent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color#transparent)
        , with percentage `pt = 100% - p1 - p2`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

<color-mix()> =   
  color-mix( <color-interpolation-method>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<color-interpolation-method>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
 =   
  in [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <rectangular-color-space> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <polar-color-space> <hue-interpolation-method>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <custom-color-space> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<rectangular-color-space> =   
  srgb               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  srgb-linear        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  display-p3         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  display-p3-linear  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  a98-rgb            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  prophoto-rgb       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rec2020            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  lab                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  oklab              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <xyz-space>          
  
<polar-color-space> =   
  hsl    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hwb    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  lch    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  oklch    
  
[<hue-interpolation-method>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 shorter [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 longer [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 increasing [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 decreasing [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 hue    
  
<custom-color-space> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
  
<xyz-space> =   
  xyz      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d50  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d65    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#examples)

-------------------------------------------------------------------------------------------------------------

### [Mixing two colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#mixing_two_colors)

This example demonstrates mixing two colors, red `#a71e14` at different percentages and white with no percentage given. The higher the percentage of `#a71e14` is mixed, the more red and less white the output color is.

#### HTML

#### CSS

The `color-mix()` function is used to add increasing percentages of red, up to 100%. The 6th [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 doesn't include a percentage for either color.

#### Result

The total value of both colors in a `color-mix()` function is 100%, even if the values set by the developer don't total 100%. In this example, as only one color has a percentage assigned, the other color is implicitly given a percentage value so that the combined total equals 100%. In the last [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
, where neither color is assigned a percentage, both default to 50%.

### [Mixing a list of colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#mixing_a_list_of_colors)

This example demonstrates passing a color argument list to `color-mix()`. The function accepts any number of colors, not just two, and each of them can optionally be given a percentage.

#### HTML

#### CSS

The first [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 mixes a single color, which resolves to that color. The second mixes three colors whose percentages total 100%. The third mixes four colors with no percentage, so each one gets an equal share.

#### Result

### [Adding transparency](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#adding_transparency)

This example demonstrates using the `color-mix()` function to add transparency to a color by mixing any color with [`transparent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color#transparent)
.

#### HTML

#### CSS

The `color-mix()` function is used to add increasing percentages of `red`, which is declared using a [custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 named `--base`, defined on the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
. The 6th [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 doesn't include a percentage, creating an output color that is half as opaque as the `--base` color. We include a striped background on the [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 to make the transparency visible.

#### Result

In this way, the `color-mix()` function can be used to add transparency to any color, even if the color is already non-opaque (with an alpha channel value < 1). However, `color-mix()` can't be used to make a semi-transparent color fully opaque. For this, use a [relative color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
 with a CSS [color function](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#functions)
. Relative colors can alter the value of any color channel, including increasing a color's alpha channel to render the color fully opaque.

### [Using hue interpolation in color-mix()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#using_hue_interpolation_in_color-mix)

This example demonstrates the hue interpolation methods available to the `color-mix()` function. When using hue [interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation)
, the resulting hue is between the hue values of the colors being mixed. The value will be different based on which route is taken around the color wheel.

For more information, see [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
.

#### CSS

The `shorter hue` interpolation method takes the shorter route around the color wheel, whereas the `longer hue` interpolation method takes the longer route. With `increasing hue`, the route starts with increasing values. With `decreasing hue` the value decreases. We mix two [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
 values to create a series of `lch()` intermediary colors that differ based on which route is taken around the color wheel. The mixed colors include `red`, `blue`, and `yellow` with LCH hue values of approximately 41deg, 301deg, and 100deg, respectively.

To reduce code redundancy, we used [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 for both colors and for the interpolation method, setting different values on each [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
.

#### Result

With `longer hue` the increments or decrements between colors will always be the same or larger than when using `shorter hue`. Use `increasing hue` or `decreasing hue` when the direction of the hue value change is more important than the length between values.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 5  <br>\# color-mix](https://drafts.csswg.org/css-color-5/#color-mix) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`<color-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
    
*   [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
    
*   [CSS relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/color_value/color-mix/index.md?plain=1 "Folder: en-us/web/css/reference/values/color_value/color-mix (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Fcolor-mix&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Fcolor-mix%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Fcolor-mix%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Fcolor-mix%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb7e9f482c51817d3a885e26092f8219fd0d9d278%0A*+Document+last+modified%3A+2026-09-28T21%3A00%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")