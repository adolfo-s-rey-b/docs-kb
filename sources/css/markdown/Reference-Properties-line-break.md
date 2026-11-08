*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#mdn-search)
    

`line-break` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`line-break`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how to break lines of Chinese, Japanese, or Korean (CJK) text when working with punctuation and symbols.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#syntax)

--------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#auto)

Break text using the default line break rule.

[`loose`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#loose)

Break text using the least restrictive line break rule. Typically used for short lines, such as in newspapers.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#normal)

Break text using the most common line break rule.

[`strict`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#strict)

Break text using the most stringent line break rule.

[`anywhere`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#anywhere)

There is a soft wrap opportunity around every typographic character unit, including around any punctuation character or preserved white spaces, or in the middle of words, disregarding any prohibition against line breaks, even those introduced by characters with the GL, WJ, or ZWJ character class or mandated by the [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
 property. The different wrapping opportunities must not be prioritized. Hyphenation is not applied.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#formal_syntax)

----------------------------------------------------------------------------------------------------------------

line-break =   
  auto      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  loose     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  normal    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  strict    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  anywhere    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#examples)

------------------------------------------------------------------------------------------------------

### [Setting text wrapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#setting_text_wrapping)

See whether the text is wrapped before "々", "ぁ" and "。".

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# line-break-property](https://drafts.csswg.org/css-text/#line-break-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break#see_also)

------------------------------------------------------------------------------------------------------

*   [CSS and international text](https://www.w3.org/International/articles/css3-text/ "External link (opens in new tab)")
     on W3C

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/line-break/index.md?plain=1 "Folder: en-us/web/css/reference/properties/line-break (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fline-break&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fline-break%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fline-break%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fline-break%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")