*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#mdn-search)
    

`font-language-override` CSS property
=====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/49)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-language-override`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls the use of language-specific glyphs in a typeface.

By default, HTML's `lang` attribute tells browsers to display glyphs designed specifically for that language. For example, a lot of fonts have a special character for the digraph `fi` that merge the dot on the "i" with the "f." However, if the language is set to Turkish the typeface will likely know not to use the merged glyph; Turkish has two versions of the "i," one with a dot (`i`) and one without (`ı`), and using the ligature would incorrectly transform a dotted "i" into a dotless "i."

The `font-language-override` property lets you override the typeface behavior for a specific language. This is useful, for example, when the typeface you're using lacks proper support for the language. For instance, if a typeface doesn't have proper rules for the Azeri language, you can force the font to use Turkish glyphs, which follow similar rules.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#syntax)

--------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#values)

This property is specified as a single value from the following list:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#normal)

Tells the browser to use font glyphs that are appropriate for the language specified by the `lang` attribute. This is the default value.

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)

Tells the browser to use font glyphs that are appropriate for the language specified by the string. The string must match a language tag found in the [OpenType language system](https://learn.microsoft.com/en-us/typography/opentype/spec/languagetags "External link (opens in new tab)")
. For example, "ENG" is English, and "KOR" is Korean.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

font-language-override =   
  normal    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#examples)

------------------------------------------------------------------------------------------------------------------

### [Using Danish glyphs](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#using_danish_glyphs)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-language-override-prop](https://drafts.csswg.org/css-fonts/#font-language-override-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    , [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    , [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    , [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    , [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    , [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    , [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    , [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
    , [`font-kerning`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-language-override/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-language-override (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-language-override&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-language-override%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-language-override%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-language-override%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")