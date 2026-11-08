*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#mdn-search)
    

`override-colors` CSS at-rule descriptor
========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`override-colors`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [descriptor](https://developer.mozilla.org/en-US/docs/Glossary/CSS_Descriptor)
 is used to override colors in the chosen [base-palette](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)
 for a color font.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#syntax)

--------------------------------------------------------------------------------------------------------------------------

css

    /* basic syntax */
    override-colors: <index of color> <color>;
    
    /* using color names */
    override-colors: 0 red;
    
    /* using hex-color */
    override-colors: 0 #ff0000;
    
    /* using rgb */
    override-colors: 0 rgb(255 0 0);
    
    /* overriding multiple colors */
    override-colors:
      0 red,
      1 green,
      2 blue;
    

The `override-colors` [descriptor](https://developer.mozilla.org/en-US/docs/Glossary/CSS_Descriptor)
 takes a comma-separated list of the color index and new color value.

The color index is zero-based and any [color value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 can be used.

For each key-value pair of index and color, the color with the index in the specified [base-palette](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)
 will be overwritten. If the color font does not have a color at the specified index, it will be ignored.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#values)

[`[ <integer [0,∞]> <absolute-color-base> ]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#integer_0%E2%88%9E_absolute-color-base)

Specifies the index of a color in a [base-palette](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)
 and the color to overwrite it with.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `n/a (required)` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------------------

override-colors =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[0,∞\]> [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#examples)

------------------------------------------------------------------------------------------------------------------------------

### [Changing colors of emojis](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#changing_colors_of_emojis)

This example shows how to override colors in the [Noto Color Emoji](https://fonts.google.com/noto/specimen/Noto+Color+Emoji "External link (opens in new tab)")
 color font to match your site's brand.

#### HTML

html

    <section class="hats">
      <div class="hat">
        <h2>Original Hat</h2>
        <div class="emoji">🎩</div>
      </div>
      <div class="hat">
        <h2>Red Hat</h2>
        <div class="emoji red-hat">🎩</div>
      </div>
    </section>
    

#### CSS

    .hats {
      display: flex;
      flex-direction: row;
      justify-content: space-around;
    }
    

css

    @font-face {
      font-family: "Noto Color Emoji";
      font-style: normal;
      font-weight: normal;
      src: url("https://mdn.github.io/shared-assets/fonts/noto-color-emoji/NotoColorEmoji-Regular.woff2")
        format("woff2");
    }
    
    .emoji {
      font-family: "Noto Color Emoji", emoji;
      font-size: 3rem;
    }
    @font-palette-values --red {
      font-family: "Noto Color Emoji";
      override-colors:
        720 rgb(74 11 0),
        1192 rgb(149 22 1),
        2052 rgb(183 27 1),
        3426 rgb(193 28 1),
        4614 rgb(230 34 1);
    }
    .red-hat {
      font-palette: --red;
    }
    

#### Result

### [Changing a color in an alternate base-palette](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#changing_a_color_in_an_alternate_base-palette)

Using [Rocher Color Font](https://www.harbortype.com/fonts/rocher-color/ "External link (opens in new tab)")
, this example shows how to override one color in the font.

#### HTML

html

    <h2 class="normal-palette">Normal Palette</h2>
    <h2 class="override-palette">Override Palette</h2>
    

#### CSS

css

    @font-face {
      font-family: "Rocher";
      src: url("[path-to-font]/RocherColorGX.woff2") format("woff2");
    }
    h2 {
      font-family: "Rocher", fantasy;
    }
    @font-palette-values --override-palette {
      font-family: "Rocher";
      base-palette: 3;
    }
    @font-palette-values --override-palette {
      font-family: "Rocher";
      base-palette: 3;
      override-colors: 0 rebeccapurple;
    }
    .normal-palette {
      font-palette: --normal-palette;
    }
    .override-palette {
      font-palette: --override-palette;
    }
    

#### Result

This example shows that in `base-palette` `3`, the color at index 0 is overridden with `rebeccapurple`.

![Example showing base-palette and base-palette with 1 color overridden](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors/override-base-palette-color.jpg)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#specifications)

------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# override-color](https://drafts.csswg.org/css-fonts/#override-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors#see_also)

------------------------------------------------------------------------------------------------------------------------------

*   [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
    
*   [`base-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/font-family)
    
*   [`font-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
    
*   [`CSSFontPaletteValuesRule.overrideColors`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFontPaletteValuesRule/overrideColors)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-palette-values/override-colors/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-palette-values/override-colors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-palette-values%2Foverride-colors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-palette-values%2Foverride-colors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-palette-values%2Foverride-colors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-palette-values%2Foverride-colors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F72af34c38ae0d97bc3c9bde4998d538bcc56634a%0A*+Document+last+modified%3A+2026-10-20T18%3A56%3A59.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")