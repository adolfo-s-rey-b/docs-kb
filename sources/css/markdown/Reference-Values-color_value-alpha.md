*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#mdn-search)
    

`alpha()` CSS function
======================

Baseline 2026

Newly available

Since September 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`alpha()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 takes an origin [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 and returns that same color with a modified alpha (transparency) channel. The color components of the origin color are preserved unchanged. The result is in the same color space as the origin color.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Replace alpha with a fixed value */
    alpha(from red / 50%)
    alpha(from var(--my-color) / 80%)
    
    /* Derive alpha relative to the origin color's alpha */
    alpha(from var(--my-color) / calc(alpha * 0.5))
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#parameters)

[`from <color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#from_color)

The [relative color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
 syntax keyword `from` followed by any valid [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value, defining the **origin color**. The color components of the origin color are carried through to the result unchanged; only the alpha channel is affected.

[`/ <alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#alpha-value)

An [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 specifying the alpha of the output color. This can be a `<number>` between `0` and `1`, a `<percentage>` between `0%` and `100%`, or a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 expression. Within this value, the keyword **`alpha`** may be used to refer to the alpha channel of the origin color as a `<number>` (where `1.0` is equivalent to `100%`).

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#return_value)

A color value in the same color space as the origin color, with identical color components and a modified alpha channel value as specified.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#description)

---------------------------------------------------------------------------------------------------------------

The `alpha()` function is a [relative color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
 function that lets you adjust the transparency of any color without rewriting its other components. This is particularly useful when you need a semi-transparent variant of a design token or custom property color, and you want to derive it automatically from the original rather than maintaining a separate value.

Within the alpha value argument, the component keyword `alpha` resolves to the alpha channel of the origin color as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 in the range `[0, 1]`. This allows you to express the output alpha relative to the input, for example halving it with `calc(alpha * 0.5)`, or clamping it with `clamp(0.2, alpha, 0.8)`.

Unlike general [relative color syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
 (e.g., `oklch(from ...)`), the `alpha()` function does not expose the individual color channel keywords of the origin color space. It is solely concerned with the alpha channel, keeping the rest of the color intact.

The return value is always in the same color space as the origin color. For example, if the origin color is an [`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
 color, the result will also be resolved in OKLCh, with the same lightness, chroma, and hue.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

<alpha()> =   
  alpha( from [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 / [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <alpha-value> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<alpha-value>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
 =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#examples)

---------------------------------------------------------------------------------------------------------

### [Replacing the alpha of a color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#replacing_the_alpha_of_a_color)

In this example, we specify two colors. The second color is defined by passing the first color into the `alpha()` function, setting its alpha channel to a fixed value of `80%` in the process. The two colors are set as the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 of two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements to demonstrate the difference.

html

    <div class="box1">Original</div>
    <div class="box2">Fixed 80% alpha</div>
    

css

    :root {
      --my-color: oklch(60% 0.25 315 / 0.3);
    
      /* Same color, but with alpha set to 80% */
      --my-color-80: alpha(from var(--my-color) / 80%);
    }
    
    .box1 {
      background-color: var(--my-color);
    }
    
    .box2 {
      background-color: var(--my-color-80);
    }
    

    body {
      font-family: sans-serif;
      display: flex;
      gap: 10%;
      justify-content: center;
    }
    
    div {
      width: 40%;
      height: 100px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    

### [Deriving a semi-transparent variant](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#deriving_a_semi-transparent_variant)

This example is very similar to the previous one, except that this time the alpha of the second color is computed as half of the first color's alpha, using the `alpha` component keyword inside a `calc()` expression.

html

    <div class="box1">Original</div>
    <div class="box2">Derived 50% alpha</div>
    

css

    :root {
      --my-color: oklch(60% 0.25 315 / 0.8);
    
      /* Half the opacity of --my-color */
      --my-color-half-opacity: alpha(from var(--my-color) / calc(alpha * 0.5));
    }
    
    .box1 {
      background-color: var(--my-color);
    }
    
    .box2 {
      background-color: var(--my-color-half-opacity);
    }
    

### [Fading a color on hover](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#fading_a_color_on_hover)

In this example, an element's background fades to `40%` opacity on [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
, while the color itself stays the same.

html

    <button class="card">Hover over me</button>
    

css

    :root {
      --brand: oklch(55% 0.22 270);
    }
    
    .card {
      background-color: var(--brand);
      color: white;
      padding: 1rem 2rem;
      border: none;
      border-radius: 0.5rem;
      font-size: 1.1rem;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    
    .card:hover {
      background-color: alpha(from var(--brand) / 40%);
    }
    

    body {
      padding: 2rem;
    }
    

    @supports not (color: alpha(from red / 50%)) {
      body::before {
        font-family: sans-serif;
        content: "Your browser does not support the CSS alpha() function.";
        background-color: wheat;
        padding: 1rem 0;
        text-align: center;
    
        z-index: 1;
        position: fixed;
        inset: 30% 0 auto;
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 5  <br>\# relative-alpha](https://drafts.csswg.org/css-color-5/#relative-alpha) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha#see_also)

---------------------------------------------------------------------------------------------------------

*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     data type
*   [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
     data type
*   [Relative color syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
    
*   [CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module
*   [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
     and [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/color_value/alpha/index.md?plain=1 "Folder: en-us/web/css/reference/values/color_value/alpha (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Falpha&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Falpha%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Falpha%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Falpha%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F77ee105b32c153b8822321ce54462134d4767c50%0A*+Document+last+modified%3A+2026-08-24T13%3A45%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")