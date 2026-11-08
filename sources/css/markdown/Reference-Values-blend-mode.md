*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#mdn-search)
    

`<blend-mode>` CSS type
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<blend-mode>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 describes how colors should appear when elements overlap. It is used in the [`background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
 and [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
 properties.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#syntax)

----------------------------------------------------------------------------------------------

The `<blend-mode>` data type is defined using a keyword value chosen from the list below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#normal)

The final color is the top color, regardless of what the bottom color is. The effect is like two opaque pieces of paper overlapping.

[`multiply`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#multiply)

The final color is the result of multiplying the top and bottom colors. A black layer leads to a black final layer, and a white layer leads to no change. The effect is like two images printed on transparent film overlapping.

[`screen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#screen)

The final color is the result of inverting the colors, multiplying them, and inverting that value. A black layer leads to no change, and a white layer leads to a white final layer. The effect is like two images shining onto a projection screen.

[`overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#overlay)

The final color is the result of `multiply` if the bottom color is darker, or `screen` if the bottom color is lighter. This blend mode is equivalent to `hard-light` but with the layers swapped.

[`darken`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#darken)

The final color is composed of the darkest values of each color channel.

[`lighten`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#lighten)

The final color is composed of the lightest values of each color channel.

[`color-dodge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#color-dodge)

The final color is the result of dividing the bottom color by the inverse of the top color. A black foreground leads to no change. A foreground with the inverse color of the backdrop leads to a fully lit color. This blend mode is similar to `screen`, but the foreground only needs to be as light as the inverse of the backdrop to create a fully lit color.

[`color-burn`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#color-burn)

The final color is the result of inverting the bottom color, dividing the value by the top color, and inverting that value. A white foreground leads to no change. A foreground with the inverse color of the backdrop leads to a black final image. This blend mode is similar to `multiply`, but the foreground only needs to be as dark as the inverse of the backdrop to make the final image black.

[`hard-light`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#hard-light)

The final color is the result of `multiply` if the top color is darker, or `screen` if the top color is lighter. This blend mode is equivalent to `overlay` but with the layers swapped. The effect is similar to shining a _harsh_ spotlight on the backdrop.

[`soft-light`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#soft-light)

The final color is similar to `hard-light`, but softer. This blend mode behaves similar to `hard-light`. The effect is similar to shining a _diffused_ spotlight on the backdrop.

[`difference`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#difference)

The final color is the result of subtracting the darker of the two colors from the lighter one. A black layer has no effect, while a white layer inverts the other layer's color.

[`exclusion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#exclusion)

The final color is similar to `difference`, but with less contrast. As with `difference`, a black layer has no effect, while a white layer inverts the other layer's color.

[`hue`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#hue)

The final color has the _hue_ of the top color, while using the _saturation_ and _luminosity_ of the bottom color.

[`saturation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#saturation)

The final color has the _saturation_ of the top color, while using the _hue_ and _luminosity_ of the bottom color. A pure gray backdrop, having no saturation, will have no effect.

[`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#color)

The final color has the _hue_ and _saturation_ of the top color, while using the _luminosity_ of the bottom color. The effect preserves gray levels and can be used to colorize the foreground.

[`luminosity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#luminosity)

The final color has the _luminosity_ of the top color, while using the _hue_ and _saturation_ of the bottom color. This blend mode is equivalent to `color`, but with the layers swapped.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#description)

--------------------------------------------------------------------------------------------------------

For each pixel among the layers to which it is applied, a blend mode takes the colors of the foreground and the background, performs a calculation on them, and returns a new color value.

Changes between blend modes are not interpolated. Any change occurs immediately.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#formal_syntax)

------------------------------------------------------------------------------------------------------------

<blend-mode> =   
  normal       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  darken       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  multiply     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-burn   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  lighten      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  screen       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-dodge  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlay      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  soft-light   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hard-light   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  difference   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  exclusion    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hue          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  saturation   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  luminosity     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#examples)

--------------------------------------------------------------------------------------------------

### [Example using "normal"](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#example_using_normal)

    <div class="container"></div>
    

css

    .container {
      width: 150px;
      height: 150px;
      background: url("br.png"), url("tr.png");
      background-blend-mode: normal;
    }
    

Set other values for `background-blend-mode`, you will get different results.

### [Comparison between different values with `background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#comparison_between_different_values_with_background-blend-mode)

    <div class="container"></div>
    

css

    .container {
      width: 720px;
      height: 760px;
      display: grid;
      grid: auto-flow 190px / repeat(4, 180px);
      border-top: 1px solid #d8d8d8;
      border-left: 1px solid #d8d8d8;
    }
    
    .container > div {
      border-right: 1px solid #d8d8d8;
      border-bottom: 1px solid #d8d8d8;
    }
    
    .container div div {
      margin-left: 15px;
      width: 150px;
      height: 150px;
      background: url("br.png"), url("tr.png");
    }
    
    .container div p {
      line-height: 30px;
      margin: 0;
      color: #a33333;
      text-align: center;
    }
    

js

    const list = [\
      "normal",\
      "multiply",\
      "screen",\
      "overlay",\
      "darken",\
      "lighten",\
      "color-dodge",\
      "color-burn",\
      "hard-light",\
      "soft-light",\
      "difference",\
      "exclusion",\
      "hue",\
      "saturation",\
      "color",\
      "luminosity",\
    ];
    
    const containerElem = document.querySelector(".container");
    
    list.forEach((item) => {
      const innerElem = document.createElement("div");
      innerElem.style.backgroundBlendMode = item;
    
      const textElem = document.createElement("p");
      textElem.innerText = item;
    
      const outerElem = document.createElement("div");
      outerElem.appendChild(textElem);
      outerElem.appendChild(innerElem);
    
      containerElem.appendChild(outerElem);
    });
    

Create multiple `div` elements by traversing a list and set different `backgroundBlendMode` value for each.

### [Comparison between different values with `mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#comparison_between_different_values_with_mix-blend-mode)

    <div class="container"></div>
    

    .container {
      width: 640px;
      height: 800px;
      display: grid;
      grid: auto-flow 160px / repeat(4, 160px);
      border-top: 1px solid #d8d8d8;
      border-left: 1px solid #d8d8d8;
    }
    
    .container > div {
      border-right: 1px solid #d8d8d8;
      border-bottom: 1px solid #d8d8d8;
    }
    
    .container > div > div {
      position: relative;
      margin-left: 20px;
      width: 120px;
      height: 120px;
    }
    
    .container div p {
      margin: 0;
      line-height: 30px;
      color: #a33333;
      text-align: center;
    }
    .circle {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      mix-blend-mode: screen;
      position: absolute;
    }
    
    .circle-1 {
      background: red;
    }
    
    .circle-2 {
      background: lightgreen;
      left: 40px;
    }
    
    .circle-3 {
      background: blue;
      left: 20px;
      top: 40px;
    }
    
    .isolate {
      isolation: isolate; /* Without isolation, the background color will be taken into account */
      position: relative;
    }
    

    const list = [\
      "normal",\
      "multiply",\
      "screen",\
      "overlay",\
      "darken",\
      "lighten",\
      "color-dodge",\
      "color-burn",\
      "hard-light",\
      "soft-light",\
      "difference",\
      "exclusion",\
      "hue",\
      "saturation",\
      "color",\
      "luminosity",\
      "plus-darker",\
      "plus-lighter",\
    ];
    
    const containerElem = document.querySelector(".container");
    
    list.forEach((item) => {
      const innerElem = document.createElement("div");
      innerElem.innerHTML = `
        <div class="circle circle-1"></div>
        <div class="circle circle-2"></div>
        <div class="circle circle-3"></div>
      `;
    
      innerElem.querySelectorAll(".circle").forEach((circle) => {
        circle.style.mixBlendMode = item;
      });
    
      const textElem = document.createElement("p");
      textElem.innerText = item;
    
      const outerElem = document.createElement("div");
      outerElem.appendChild(textElem);
      outerElem.appendChild(innerElem);
    
      containerElem.appendChild(outerElem);
    });
    

In the following example, we create multiple `<div>` elements by traversing a list and set different `mixBlendMode` values for each.

### [Blend mode comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#blend_mode_comparison)

In the following example, we have a `<div>` with two background images set on it — a Firefox logo on top of a linear gradient. Below it, we have a provided a `<select>` menu that allows you to change the `background-blend-mode` applied to the `<div>`, allowing you to compare the different blend mode effects.

#### HTML

html

    <div></div>
    <p>Choose a blend-mode:</p>
    <select>
      <option selected>normal</option>
      <option>multiply</option>
      <option>screen</option>
      <option>overlay</option>
      <option>darken</option>
      <option>lighten</option>
      <option>color-dodge</option>
      <option>color-burn</option>
      <option>hard-light</option>
      <option>soft-light</option>
      <option>difference</option>
      <option>exclusion</option>
      <option>hue</option>
      <option>saturation</option>
      <option>color</option>
      <option>luminosity</option>
    </select>
    

#### CSS

css

    div {
      width: 300px;
      height: 300px;
      background:
        url("https://mdn.dev/archives/media/attachments/2020/07/29/17350/3b4892b7e820122ac6dd7678891d4507/firefox.png")
          no-repeat center,
        linear-gradient(to bottom, blue, orange);
    }
    

#### JavaScript

js

    const selectElem = document.querySelector("select");
    const divElem = document.querySelector("div");
    
    selectElem.addEventListener("change", () => {
      divElem.style.backgroundBlendMode = selectElem.value;
    });
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Compositing and Blending Module Level 2  <br>\# ltblendmodegt](https://drafts.csswg.org/compositing/#ltblendmodegt) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode#see_also)

--------------------------------------------------------------------------------------------------

*   The [CSS compositing and blending](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Compositing_and_blending)
     module that defines the `<blend-mode>` values.
*   Properties that use this data type: [`background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
    , [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
    

Description to various blend modes on other website:

*   [Blend modes](https://en.wikipedia.org/wiki/Blend_modes "External link (opens in new tab)")
     on Wikipedia
*   [Blending modes in Adobe Photoshop](https://helpx.adobe.com/photoshop/desktop/repair-retouch/adjust-light-tone/blending-mode-descriptions.html "External link (opens in new tab)")
     by Adobe

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/blend-mode/index.md?plain=1 "Folder: en-us/web/css/reference/values/blend-mode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fblend-mode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fblend-mode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fblend-mode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fblend-mode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6f1b699dd8891431bbfe0bc3bb803f929fa6032e%0A*+Document+last+modified%3A+2026-08-12T19%3A49%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")