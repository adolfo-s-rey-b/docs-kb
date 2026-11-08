*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#mdn-search)
    

`contrast-color()` CSS function
===============================

Baseline 2026

Newly available

Since April 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`contrast-color()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 takes a [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value and returns a contrasting color. The function commonly ensures [the WCAG AA minimum contrast](https://w3c.github.io/wcag/guidelines/22/#contrast-minimum "External link (opens in new tab)")
. The browsers may use different and better algorithms.

The `contrast-color()` function enables specifying a text color and automatically generating a contrasting background color, or vice versa. It avoids the need to maintain background-text color pairs.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#syntax)

--------------------------------------------------------------------------------------------------------------

css

    contrast-color(red)
    contrast-color(var(--backgroundColor))
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#parameters)

[`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#color)

Any valid [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#return_value)

A [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
 of either `white` or `black`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#description)

------------------------------------------------------------------------------------------------------------------------

The `contrast-color()` function returns a value of `white` or `black`, depending on which value has the greatest contrast with the input color. If both `white` and `black` have the same contrast with the input color, `white` is returned.

**Warning:** WCAG AA (4.5:1) contrast is not capable of producing clearly readable text in all cases. Mid-tone background colors generally don't provide enough contrast with either black or white foreground. For example, `contrast-color()` on a royal bluish (`#2277d3`) background produces black text, which is not readable for small text. It is recommended, therefore, to use light or dark colors with the `contrast-color()` function.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#examples)

------------------------------------------------------------------------------------------------------------------

### [Contrasting text for a button](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#contrasting_text_for_a_button)

In the following example, the browser automatically applies the selected color to the background of the "Button" [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, and the contrasting color (black or white) to its text.

    <label>
      Select background color of the button:
      <input type="color" id="colorPicker" value="#660066" />
    </label>
    <br />
    <button>Button</button>
    

css

    :root {
      --button-color: lightblue;
    }
    
    button {
      background-color: var(--button-color);
    
      /* Set contrasting text color automatically */
      color: contrast-color(var(--button-color));
    }
    

    body {
      padding: 1rem;
    }
    
    button {
      margin: 3rem;
      padding: 1rem;
      width: 150px;
      font-size: 2rem;
      border-radius: 1rem;
    }
    
    @supports not (color: contrast-color(red)) {
      body::before {
        content: "Your browser doesn't support the contrast-color() function.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

    const colorPicker = document.getElementById("colorPicker");
    const root = document.documentElement;
    
    function updateColor(color) {
      root.style.setProperty("--button-color", colorPicker.value);
    }
    
    colorPicker.addEventListener("input", updateColor);
    updateColor();
    

### [Light and dark mode usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#light_and_dark_mode_usage)

In the following example, the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
 is used to set a background color based on operating system or browser color scheme settings. The `contrast-color()` function is used to set the text color automatically.

Try changing the browser or OS dark mode setting to see the effect.

    <pre>
        Q: How does CSS transform light into energy?
      Ans: Using <a href="/en-US/docs/Web/CSS/Reference/Properties/font-synthesis">font-synthesis</a>.
    </pre>
    

css

    :root {
      --background-color: navy;
    }
    
    @media (prefers-color-scheme: light) {
      :root {
        --background-color: wheat;
      }
    }
    
    body,
    a {
      background-color: var(--background-color);
      color: contrast-color(var(--background-color));
    }
    

    body {
      padding: 2rem;
      font-size: 1.2rem;
    }
    
    pre {
      margin-top: 3rem;
    }
    
    @supports not (color: contrast-color(red)) {
      body::before {
        content: "Your browser doesn't support the contrast-color() function.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 5  <br>\# contrast-color](https://drafts.csswg.org/css-color-5/#contrast-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
    
*   [CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module
*   [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
     and [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    
*   [`prefers-contrast`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast)
     and [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
     [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     features
*   [WCAG: color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast)
    
*   [How to have the browser pick a contrasting color in CSS](https://webkit.org/blog/16929/contrast-color/ "External link (opens in new tab)")
     on webkit.org (2025)
*   [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/ "External link (opens in new tab)")
     on webaim.org (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/color_value/contrast-color/index.md?plain=1 "Folder: en-us/web/css/reference/values/color_value/contrast-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Fcontrast-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Fcontrast-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Fcontrast-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Fcontrast-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa8b7faffbd3fdeae5c0be97793d963d8a31cd1cf%0A*+Document+last+modified%3A+2026-04-22T11%3A39%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")