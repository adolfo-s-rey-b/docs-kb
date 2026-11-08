*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#mdn-search)
    

`font-display` CSS at-rule descriptor
=====================================

The **`font-display`** descriptor for the [`@font-feature-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)
 at-rule sets the default value of how a font face is displayed based on whether and when it is downloaded. Setting a value for the `font-display` descriptor within a `@font-feature-values` block sets the default value of the `font-display` descriptor for the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule for all the fonts with the same [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
 value.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#syntax)

-----------------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#auto)

The font display strategy is defined by the user agent.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#block)

Gives the font face a short block period, generally around 3 seconds, and an infinite swap period.

[`swap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#swap)

Gives the font face an extremely small block period and an infinite swap period.

[`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#fallback)

Gives the font face an extremely small block period and a short swap period.

[`optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#optional)

Gives the font face an extremely small block period and no swap period.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#description)

---------------------------------------------------------------------------------------------------------------------------------

The `font-display` descriptor for `@font-feature-values` determines the font display timeline; it does so by setting a default `font-display` value for `@font-face` for the same `font-family` name. When `font-display` is omitted in `@font-face`, the user agent first looks for the `font-display` value that has been set via `@font-feature-values` for the relevant font-family. If no value is found, the user agent uses the `auto` value for `font-display`, in which case, the user agent determines the font display strategy.

The font display timeline is based on a timer that starts when the user agent attempts to use a specific downloaded font face. The timeline is divided into three periods, as listed below. These periods dictate the rendering behavior of any element that uses the font face.

*   Font **block** period: If the font face is not loaded, elements attempting to use the font are rendered with an _invisible_ fallback font face. The browser blocks visible text rendering, saving a space for the to-be-displayed text based on metrics of the fallback font. During the block period, text is not visible. At the end of the block period, if the font has not loaded, the text is rendered in the fallback font.
    
*   Font **swap** period: The swap period occurs after the block period (if there is one) and if the font face has not yet been loaded successfully. Elements attempting to use the not-yet-loaded font are rendered using the next available fallback font face. The formerly invisible fallback font face is painted onto the screen. If the font loads successfully during the swap period, the text that was rendered in the fallback font is updated — or swapped — with the newly loaded font. This step triggers a repaint.
    
*   Font **failure** period: If the font face has not loaded by the time the swap period expires or by the time the block period expires (if there is no swap period, as is the case with `optional`), the user agent treats the font as a failed load. As a result, the content becomes visible in the fallback font.
    

The `font-display` descriptor allows you to set a default display policy for all `@font-face` rules, including those not under author control, such as third-party `@font-face` rules. When the `font-display` value is set via `@font-feature-values`, it becomes the default `font-display` value, and is applied to the entire font-family. However, any `font-display` value defined within individual `@font-face` blocks will override this default, but only for those blocks where the descriptor is defined.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#examples)

---------------------------------------------------------------------------------------------------------------------------

The `font-display` descriptor in this example sets the default `font-display` value for the "Leitura" font to `swap` for all the `@font-face` blocks. Now there might be several `@font-face` blocks importing multiple font files for a single font-family. If one of those `@font-face` blocks includes a `font-display` descriptor, the specified value will be used for that specific font file only. All other blocks not including a `font-display` descriptor will default to `swap` instead of the user-agent's standard default `auto`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# descdef-font-feature-values-font-display](https://drafts.csswg.org/css-fonts/#descdef-font-feature-values-font-display) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

Currently, no browsers support this feature.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
     descriptor for [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
     at-rule
*   [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-feature-values/font-display/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-feature-values/font-display (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-feature-values%2Ffont-display&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-feature-values%2Ffont-display%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-feature-values%2Ffont-display%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-feature-values%2Ffont-display%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")