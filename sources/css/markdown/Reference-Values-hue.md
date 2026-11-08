*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#mdn-search)
    

`<hue>` CSS type
================

The **`<hue>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents the hue angle of a color. It is used in the color functions that accept hue expressed as a single value, specifically [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
, [`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
, [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
, and [`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
 functional notations.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#syntax)

---------------------------------------------------------------------------------------

A `<hue>` can be either an `<angle>` or a `<number>`.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#values)

[`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)

An angle expressed in degrees, gradians, radians, or turns using the `deg`, `grad`, `rad`, or `turn`, respectively.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#number)

A real number, representing degrees of the hue angle.

As an `<angle>` is periodic, `<hue>` is normalized to the range `[0deg, 360deg)`. It implicitly wraps around such that `480deg` is the same as `120deg`, `-120deg` is the same as `240deg`, `-1turn` is the same as `1turn`, and so on.\
\
[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#description)\
\
-------------------------------------------------------------------------------------------------\
\
![An sRGB color wheel](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue/color_wheel.svg)\
\
The color wheel above shows hues at all angles in the [sRGB](https://en.wikipedia.org/wiki/SRGB "External link (opens in new tab)")\
 [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)\
. In particular, _red_ is at `0deg`, _yellow_ is at `60deg`, _lime_ is at `120deg`, _cyan_ is at `180deg`, _blue_ is at `240deg`, and _magenta_ is at `300deg`.\
\
The angles corresponding to particular hues differ depending on the color space. For example, the hue angle of sRGB green is `120deg` in the sRGB color space, but `134.39deg` in the CIELAB color space.\
\
The following table lists typical colors at various angles in the sRGB (used by [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)\
 and [`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)\
), CIELAB (used by [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)\
), and Oklab (used by [`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)\
) color spaces:\
\
 \
|     | 0°  | 60° | 120° | 180° | 240° | 300° |\
| --- | --- | --- | --- | --- | --- | --- |\
| sRGB |     |     |     |     |     |     |\
| CIELAB |     |     |     |     |     |     |\
| Oklab |     |     |     |     |     |     |\
\
[Interpolation of `<hue>` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#interpolation_of_hue_values)\
\
-------------------------------------------------------------------------------------------------------------------------------------\
\
`<hue>` values are interpolated as [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 values, and the default interpolation algorithm is [`shorter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#values)\
. In some color-related CSS functions, this can be overridden by the [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)\
 component.\
\
[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#formal_syntax)\
\
-----------------------------------------------------------------------------------------------------\
\
<hue> =   \
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
  \
  [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
     \
\
[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#examples)\
\
-------------------------------------------------------------------------------------------\
\
### [Changing the hue of a color using a slider](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#changing_the_hue_of_a_color_using_a_slider)\
\
The following example shows the effect of changing the `hue` value of the [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)\
 functional notation on a color.\
\
#### HTML\
\
html\
\
    <input type="range" min="0" max="360" value="0" id="hue-slider" />\
    <p>Hue: <span id="hue-value">0deg</span></p>\
    <div id="box"></div>\
    \
\
#### CSS\
\
    div {\
      width: 100px;\
      height: 100px;\
      margin: 10px;\
      border: 1px solid black;\
    }\
    p {\
      font-family: sans-serif;\
    }\
    span {\
      font-family: monospace;\
      background: rgb(0 0 0 / 10%);\
      padding: 3px;\
    }\
    #hue-slider {\
      width: 90%;\
    }\
    \
\
css\
\
    #box {\
      background-color: hsl(0 100% 50%);\
    }\
    \
\
#### JavaScript\
\
js\
\
    const hue = document.querySelector("#hue-slider");\
    const box = document.querySelector("#box");\
    hue.addEventListener("input", () => {\
      box.style.backgroundColor = `hsl(${hue.value} 100% 50%)`;\
      document.querySelector("#hue-value").textContent = `${hue.value}deg`;\
    });\
    \
\
#### Result\
\
### [Approximating red hues in different color spaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#approximating_red_hues_in_different_color_spaces)\
\
The following example shows a similar red color in different color spaces. The values in the `lch()` and `oklch()` functions are rounded for readability.\
\
#### HTML\
\
html\
\
    <div data-color="hsl-red">hsl()</div>\
    <div data-color="hwb-red">hwb()</div>\
    <div data-color="lch-red">lch()</div>\
    <div data-color="oklch-red">oklch()</div>\
    \
\
#### CSS\
\
css\
\
    [data-color="hsl-red"] {\
      /* hsl(<hue> <saturation> <lightness>) */\
      background-color: hsl(0 100% 50%);\
    }\
    [data-color="hwb-red"] {\
      /* hwb(<hue> <whiteness> <blackness>) */\
      background-color: hwb(0 0% 0%);\
    }\
    [data-color="lch-red"] {\
      /* lch(<lightness> <chroma> <hue>) */\
      background-color: lch(50 150 40);\
    }\
    [data-color="oklch-red"] {\
      /* oklch(<lightness> <chroma> <hue>) */\
      background-color: oklch(0.6 0.4 20);\
    }\
    \
\
    div {\
      font-family: monospace;\
      width: 100px;\
      height: 100px;\
      margin: 10px;\
      border: 1px solid black;\
      display: inline-block;\
    }\
    \
\
#### Result\
\
[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#specifications)\
\
-------------------------------------------------------------------------------------------------------\
\
| Specification |\
| --- |\
| [CSS Color Module Level 4  <br>\# typedef-hue](https://drafts.csswg.org/css-color/#typedef-hue) |\
\
[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#browser_compatibility)\
\
---------------------------------------------------------------------------------------------------------------------\
\
### [css.types.color.hsl](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#css.types.color.hsl)\
\
### [css.types.color.hwb](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#css.types.color.hwb)\
\
### [css.types.color.lch](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#css.types.color.lch)\
\
### [css.types.color.oklch](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#css.types.color.oklch)\
\
[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue#see_also)\
\
-------------------------------------------------------------------------------------------\
\
*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
    \
*   [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)\
    \
\
Help improve MDN\
----------------\
\
[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)\
\
This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue/contributors.txt)\
.\
\
[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/hue/index.md?plain=1 "Folder: en-us/web/css/reference/values/hue (Opens in a new tab)")\
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fhue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fhue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fhue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fhue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")