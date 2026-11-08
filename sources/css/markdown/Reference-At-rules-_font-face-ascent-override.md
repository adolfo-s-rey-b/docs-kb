*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#mdn-search)
    

`ascent-override` CSS at-rule descriptor
========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/132)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`ascent-override`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 descriptor for the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule defines the ascent metric for the font. The ascent metric is the height above the baseline that CSS uses to lay out line boxes in an inline formatting context.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#syntax)

----------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#normal)

The default value. When used the metric value is obtained from the font file.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#percentage)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Percentages | as specified |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#formal_syntax)

------------------------------------------------------------------------------------------------------------------------------

ascent-override =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 normal [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#examples)

--------------------------------------------------------------------------------------------------------------------

### [Overriding metrics of a fallback font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#overriding_metrics_of_a_fallback_font)

The `ascent-override` property can help when overriding the metrics of a fallback font to better match those of a primary web font.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-metrics-override-desc](https://drafts.csswg.org/css-fonts/#font-metrics-override-desc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [`descent-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/descent-override)
    
*   [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
    
*   [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)
    
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    
*   [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
    
*   [`line-gap-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/line-gap-override)
    
*   [`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
    
*   [`size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust)
    
*   [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
     descriptor

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-face/ascent-override/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-face/ascent-override (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Fascent-override&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Fascent-override%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Fascent-override%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Fascent-override%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")