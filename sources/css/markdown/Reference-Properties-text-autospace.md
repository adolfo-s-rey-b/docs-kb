*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#mdn-search)
    

`text-autospace` CSS property
=============================

Baseline 2025

Newly available

\*

Since November 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/284)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-autospace`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property allows you to specify the space applied between Chinese/Japanese/Korean (CJK) and non-CJK characters.

Many CJK typographic conventions require a small amount of space between CJK characters and Western letters or numbers (see W3C's descriptions for [Chinese](https://www.w3.org/International/clreq/#mixed_text_composition_in_horizontal_writing_mode "External link (opens in new tab)")
 and [Japanese](https://www.w3.org/International/jlreq/#japanese_and_western_mixed_text_composition "External link (opens in new tab)")
 text layout conventions). Some authors would manually insert a space character for this purpose, but `text-autospace` adds this spacing at the layout engine level, without requiring extra characters in the textual content.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#try_it)

------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#syntax)

------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#normal)

Creates the default behavior to automatically apply spacing between CJK and non-CJK characters and around punctuation. This value has the same effect as applying both [`ideograph-alpha`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#ideograph-alpha)
 and [`ideograph-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#ideograph-numeric)
.

[`<autospace>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#autospace)

Provides more control over spacing behaviors. It accepts the keyword `no-autospace`, or a combination of one or more of `ideograph-alpha`, `ideograph-numeric`, and `punctuation`, optionally followed by `insert` or `replace`.

[`no-autospace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#no-autospace)

Disables automatic spacing between CJK and non-CJK characters.

[`ideograph-alpha`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#ideograph-alpha)

Adds spacing only between ideographic characters (such as Katakana and Han) and non-ideographic letters (such as Latin). It does not add spacing between ideographic characters and non-ideographic numbers.

[`ideograph-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#ideograph-numeric)

Adds spacing only between ideographic characters (such as Katakana and Han) and non-ideographic numbers (such as Latin). It does not add spacing between ideographic characters and non-ideographic letters.

[`punctuation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#punctuation)

Adds non-breaking spacing around punctuation as required by language-specific typographic conventions.

[`insert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#insert)

Adds the specified spacing only if there are no existing spaces between the ideographic and non-ideographic scripts.

[`replace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#replace)

Replaces existing spacing (such as [U+0020](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
) between ideographic and non-ideographic characters with the specified spacing.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#auto)

Lets the browser choose typographically appropriate spacing. The spacing may vary across browsers and platforms.

**Note:** If neither `insert` nor `replace` are specified, the behavior is the same as `insert`.

**Note:** This property is additive with the [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
 and [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
 properties. The amount of spacing contributed by the `letter-spacing` setting is added to the spacing created by `text-autospace`. The same applies to `word-spacing`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | text elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

text-autospace =   
  normal       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <autospace>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto           
  
<autospace> =   
  no-autospace                                        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 ideograph-alpha [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 ideograph-numeric [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 punctuation [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 insert [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 replace [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# propdef-text-autospace](https://drafts.csswg.org/css-text-4/#propdef-text-autospace) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace#see_also)

----------------------------------------------------------------------------------------------------------

*   [`text-spacing-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim)
    
*   [`ic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types#local_font-relative_lengths)
     and [`ric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types#root_font-relative_lengths)
     units
*   [CSS Text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
     module
*   [Mixed text composition in horizontal writing mode](https://www.w3.org/International/clreq/#mixed_text_composition_in_horizontal_writing_mode "External link (opens in new tab)")
     in Requirements for Chinese Text Layout on w3.org
*   [Japanese and Western mixed text composition](https://www.w3.org/International/jlreq/#japanese_and_western_mixed_text_composition "External link (opens in new tab)")
     in Requirements for Japanese Text Layout on w3.org

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-autospace/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-autospace (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-autospace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-autospace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-autospace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-autospace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F05b21c9303964f221febe77f053e5636f230afe9%0A*+Document+last+modified%3A+2026-11-03T06%3A59%3A05.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")