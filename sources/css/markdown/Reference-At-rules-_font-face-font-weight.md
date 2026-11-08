*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#mdn-search)
    

`font-weight` CSS at-rule descriptor
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-weight`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 descriptor enables authors to specify a single font weight, or a range of font weights, for the font specified in a [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule. This is then used by the browser to select the appropriate font when a CSS rule sets a desired [font weight](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
.

Typically, a developer will want to use fonts from a single font family in a range of different weights. With traditional, or _static_ fonts, a single font file contains characters from a font family in a specific weight and style: for example, "Helvetica bold italic". To enable displaying light, regular, bold, or extra-bold fonts when the `font-weight` property calls a specific weight, you can define multiple [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rules for the same family (all with the same [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
 descriptor value), one for each weight or range of weights.

To declare the font to be used for a range of font weights, declare a space-separated pair of font-weight values as the value for the `font-weight` descriptor. When CSS rules set a font weight by setting the [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 property or the [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 shorthand property, the appropriate font will then be used.

For example, if the descriptor is `font-weight: 400 600;`, when the property is `font-weight: 450` or `font-weight: 550`, that font will be used for that font-family. Whether the font is a static or a [variable font](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts)
, the font matching the range will be used. In this case, if the font is a static font, `450` and `550` will appear the same. If the font is a variable font, the latter will be bolder.

The descriptor is the same for all fonts, but the range you'll set for a variable font will generally be greater, possibly even `1 1000` to use the same font for all font weight property values.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* Single values */
    font-weight: normal;
    font-weight: bold;
    font-weight: 400;
    
    /* Defining a range */
    font-weight: normal bold;
    font-weight: 300 500;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#values)

The `font-weight` descriptor takes one of the following forms:

*   The keyword `auto`.
*   A single `<font-weight-absolute>` value.
*   A pair of `<font-weight-absolute>` values, separated by a space.

Each `<font-weight-absolute>` may be any one of the following:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#normal)

Normal font weight. Same as `400`.

[`bold`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#bold)

Bold font weight. Same as `700`.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#number)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 value between 1 and 1000, inclusive. Higher numbers represent weights that are bolder than (or as bold as) lower numbers. Certain commonly used values correspond to common weight names, as described in the [Common weight name mapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#common_weight_name_mapping)
 section below.

### [Common weight name mapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#common_weight_name_mapping)

The numerical values `100` to `900` roughly correspond to the following common weight names:

| Value | Common weight name |
| --- | --- |
| 100 | Thin (Hairline) |
| 200 | Extra Light (Ultra Light) |
| 300 | Light |
| 400 | Normal |
| 500 | Medium |
| 600 | Semi Bold (Demi Bold) |
| 700 | Bold |
| 800 | Extra Bold (Ultra Bold) |
| 900 | Black (Heavy) |

### [Variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#variable_fonts)

Most fonts have a particular weight which corresponds to one of the numbers in [Common weight name mapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#common_weight_name_mapping)
. However some fonts, called variable fonts, can support a range of weights with more or less fine granularity, and this can give the designer a much closer degree of control over the chosen weight.

For TrueType or OpenType variable fonts, the "wght" variation is used to implement varying weights.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#accessibility)

--------------------------------------------------------------------------------------------------------------------------

People experiencing low vision conditions may have difficulty reading text set with a `font-weight` value of `100` (Thin/Hairline) or `200` (Extra Light), especially if the font has a [low contrast color ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color#accessibility)
.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.8 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-visual-presentation.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

font-weight =   
  auto                         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <font-weight-absolute>[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
<font-weight-absolute> =   
  normal             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bold               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<number \[1,1000\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#examples)

----------------------------------------------------------------------------------------------------------------

### [Selecting normal and bold fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#selecting_normal_and_bold_fonts)

In this example we include two fonts, one normal weight, one bold weight, from the ["Fira Sans"](https://fonts.google.com/specimen/Fira+Sans "External link (opens in new tab)")
 font family using two `@font-face` at rules. We set `font-weight` descriptors to match the weight of the fonts.

After this, CSS rules can select the normal or the bold font for the "Fira Sans" family just by setting the [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 property. Note that the [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
 HTML element also selects the bold font, because by default `<strong>` elements have a CSS `font-weight` property value of `bold`.

#### HTML

html

    <p class="one">Fira Sans, `normal` weight paragraph</p>
    <p class="two">Fira Sans, `bold` weight paragraph</p>
    <p><strong>Fira Sans, &lt;strong&gt; element (`bold`)</strong></p>
    

#### CSS

css

    @font-face {
      font-family: "Fira Sans";
      font-weight: normal;
      src: url("https://mdn.github.io/shared-assets/fonts/FiraSans-Regular.woff2");
    }
    
    @font-face {
      font-family: "Fira Sans";
      font-weight: bold;
      src: url("https://mdn.github.io/shared-assets/fonts/FiraSans-Bold.woff2");
    }
    
    body {
      font-family: "Fira Sans", serif;
      font-size: 2rem;
    }
    
    p.one {
      font-weight: normal;
    }
    
    p.two {
      font-weight: bold;
    }
    

#### Result

### [Setting font-weight ranges](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#setting_font-weight_ranges)

This example demonstrates how authors can include multiple fonts for multiple font-weights (and font-styles), by including multiple `@font-face` declarations with the same `font-family` value. By setting the `font-weight` descriptors using ranges from 1 to 1000, in the rest of your stylesheets, you can declare a `font-weight` (or `font-style`), and know the appropriate font will be used.

#### HTML

html

    <p class="one">This has a font weight of 100</p>
    <p class="three">This has a font weight of 300</p>
    <p class="four">This has a font weight of 400</p>
    <p class="five">This has a font weight of 500</p>
    <p class="seven">This has a font weight of 700</p>
    <p class="nine">This has a font weight of 900</p>
    

#### CSS

We include four `@font-face` declarations for four different fonts from the `FireSans` font family, as seen in the previous example. Each declaration is set to a different range of font-weight values, but all use the same font name.

The first declaration uses `FiraSans-Regular` and its associated `font-weight` range includes the entire possible range of font weight values.

The other three declarations use the light, bold, and extra-bold versions of the font, and their associated `font-weight` ranges define subsets of the range as follows:

*   the light font is associated with the range 1-300
*   the bold font is associated with the range 500-700
*   the extra-bold font is associated with the range 700-1000

The CSS [cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
 ensures that the three latter declarations override parts of the range that was set in the `FiraSans-Regular` declaration.

css

    @font-face {
      font-family: "Fira Sans";
      font-weight: 1 1000;
      src: url("https://mdn.github.io/shared-assets/fonts/FiraSans-Regular.woff2");
    }
    
    @font-face {
      font-family: "Fira Sans";
      font-weight: 1 300;
      src: url("https://mdn.github.io/shared-assets/fonts/FiraSans-Light.woff2");
    }
    
    @font-face {
      font-family: "Fira Sans";
      font-weight: 500 700;
      src: url("https://mdn.github.io/shared-assets/fonts/FiraSans-Bold.woff2");
    }
    
    @font-face {
      font-family: "Fira Sans";
      font-weight: 700 1000;
      src: url("https://mdn.github.io/shared-assets/fonts/FiraSans-ExtraBold.woff2");
    }
    
    body {
      font-family: "Fira Sans", serif;
      font-size: 2rem;
    }
    
    p.one {
      font-weight: 100;
    }
    
    p.three {
      font-weight: 300;
    }
    
    p.four {
      font-weight: 400;
    }
    
    p.five {
      font-weight: 500;
    }
    
    p.seven {
      font-weight: 700;
    }
    
    p.nine {
      font-weight: 900;
    }
    

#### Result

The `seven` paragraph uses the extra bold font. While `font-weight: 700` matches both the `FiraSans-Bold` and `FiraSans-ExtraBold` declarations, as the FiraSans-ExtraBold is declared later, it overrides the `FiraSans-Bold` for that value.

Similarly, the `100` and `300` both use the light font; although `FiraSans-Regular` and `FiraSans-Light` both include `300` in their ranges, `FiraSans-Light` is declared later. Alternatively, we could have declared `FiraSans-Regular` after `FiraSans-Light`, but we would need to change the `font-weight` descriptor range if we do so.

### [Setting a range for a variable font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#setting_a_range_for_a_variable_font)

In this example we're using the `font-weight` descriptor to restrict the range of weights that can be set when using a variable font.

We include a variable font, ["League Mono"](https://www.theleagueofmoveabletype.com/league-mono "External link (opens in new tab)")
, using a single `@font-face` at-rule. We use a `font-weight: 300 700` value to effectively limit the range of weights that are available. If a CSS rule uses our "League Mono" font, then if it specifies a weight outside this range the weight it gets is clamped to the range.

#### HTML

We include a paragraph with `<output>` initially set to `400`, as that is the default font-weight for unstyled paragraph text. This paragraph is nestled between two other paragraphs, so you can compare rendered versus declared font weight values.

We include an [`<input/range>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 of type `range`, nested in a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
, setting the `step` to `50`.

html

    <p>LeagueMono, font-weight: 300 (comparison)</p>
    <p id="example">LeagueMono, font-weight: <output>400</output> (example)</p>
    <p>LeagueMono, font-weight: 700 (comparison)</p>
    <label
      >Change the font weight:
      <input type="range" min="50" max="1000" step="50" value="400" />
    </label>
    

#### CSS

We set the `font-weight` descriptor range to `300 700`, clamping the variable font to that range.

css

    @font-face {
      font-family: "LeagueMono";
      src: url("https://mdn.github.io/shared-assets/fonts/LeagueMono-VF.ttf");
      font-weight: 300 700;
    }
    
    p {
      font-family: "LeagueMono", serif;
      font-size: 1.5rem;
    }
    
    p:first-of-type {
      font-weight: 300;
    }
    
    p:last-of-type {
      font-weight: 700;
    }
    

#### JavaScript

We include an event handler that updates the paragraph's `font-weight` property value, and updates the text to reflect the change:

js

    const text = document.querySelector("#example");
    const log = document.querySelector("output");
    const range = document.querySelector("input");
    
    range.addEventListener("change", () => {
      text.style.fontWeight = range.value;
      log.innerText = range.value;
    });
    

#### Result

Change the font weight of the paragraph via the range. Note that the example paragraph does not get lighter than the `300` paragraph above it or bolder than the `700` paragraph below it; the font weight is clamped to the range defined by the `font-weight` descriptor.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-prop-desc](https://drafts.csswg.org/css-fonts/#font-prop-desc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
    
*   [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
    
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    
*   [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
    
*   [`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
    
*   [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
     descriptor

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-face/font-weight/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-face/font-weight (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-weight&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-weight%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-weight%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-weight%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc66cecb0ec58ddea1bd624aa89dd355d9b90b5c3%0A*+Document+last+modified%3A+2026-07-24T02%3A38%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")