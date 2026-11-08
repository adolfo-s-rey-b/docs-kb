*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#mdn-search)
    

`font-display` CSS at-rule descriptor
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-display`** descriptor for the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule determines how a font face is displayed based on whether and when it is downloaded and ready to use.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#syntax)

-------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#auto)

The font display strategy is defined by the user agent.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#block)

Gives the font face a short block period and an infinite swap period.

[`swap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#swap)

Gives the font face an extremely small block period and an infinite swap period.

[`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#fallback)

Gives the font face an extremely small block period and a short swap period.

[`optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#optional)

Gives the font face an extremely small block period and no swap period.

**Note:** In Firefox, the preferences `gfx.downloadable_fonts.fallback_delay` and `gfx.downloadable_fonts.fallback_delay_short` provide the duration of the "short" and "extremely small" periods, respectively.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#description)

-----------------------------------------------------------------------------------------------------------------------

The font display timeline is based on a timer that begins the moment the user agent attempts to use a given downloaded font face. The timeline is divided into the three periods below which dictate the rendering behavior of any elements using the font face:

*   Font block period: If the font face is not loaded, any element attempting to use it must render an _invisible_ fallback font face. If the font face successfully loads during this period, it is used normally.
*   Font swap period: If the font face is not loaded, any element attempting to use it must render a fallback font face. If the font face successfully loads during this period, it is used normally.
*   Font failure period: If the font face is not loaded, the user agent treats it as a failed load causing normal font fallback.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

font-display =   
  auto      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  swap      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fallback  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  optional    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#examples)

-----------------------------------------------------------------------------------------------------------------

### [Specifying fallback font-display](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#specifying_fallback_font-display)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-display-desc](https://drafts.csswg.org/css-fonts/#font-display-desc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
    
*   [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
    
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    
*   [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
    
*   [`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
    
*   [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-face/font-display/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-face/font-display (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-display&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-display%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-display%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-display%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F91e08923c809ca8deded3e3294f49bbe1a4a00b3%0A*+Document+last+modified%3A+2026-09-10T06%3A51%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")