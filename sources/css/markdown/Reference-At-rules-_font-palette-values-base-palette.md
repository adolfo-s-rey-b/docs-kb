*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#mdn-search)
    

`base-palette` CSS at-rule descriptor
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`base-palette`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [descriptor](https://developer.mozilla.org/en-US/docs/Glossary/CSS_Descriptor)
 is used to specify the name or index of a pre-defined palette to be used for creating a new palette. If the specified `base-palette` does not exist, then the palette defined at index 0 will be used.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#syntax)

-----------------------------------------------------------------------------------------------------------------------

The `base-palette` [descriptor](https://developer.mozilla.org/en-US/docs/Glossary/CSS_Descriptor)
 is specified using a zero-based index of the font-maker created palettes.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#values)

[`<index>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#index)

Specifies the index of the pre-defined palette to use.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `n/a (required)` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------------

base-palette =   
  light            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dark             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <integer \[0,∞\]>    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Changing the default palette in a font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#changing_the_default_palette_in_a_font)

Using the [Rocher Color Font](https://www.harbortype.com/fonts/rocher-color/ "External link (opens in new tab)")
, this example shows two instances of switching the default palette in the font to an alternate palette created by the font-maker.

#### HTML

#### CSS

#### Result

![Example showing 3 different base-palettes of Rocher color font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette/rocher-color-font-alt-base-palettes.jpg)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# base-palette-desc](https://drafts.csswg.org/css-fonts/#base-palette-desc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/font-family)
     descriptor
*   [`override-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors)
     descriptor
*   [`font-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
     property
*   [`CSSFontPaletteValuesRule.basePalette`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFontPaletteValuesRule/basePalette)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-palette-values/base-palette/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-palette-values/base-palette (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-palette-values%2Fbase-palette&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-palette-values%2Fbase-palette%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-palette-values%2Fbase-palette%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-palette-values%2Fbase-palette%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")