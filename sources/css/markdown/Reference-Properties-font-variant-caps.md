*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#mdn-search)
    

`font-variant-caps` CSS property
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-variant-caps`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls the use of alternate glyphs used for small or petite capitals or for titling.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#try_it)

---------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#syntax)

---------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#values)

This property is specified as one of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#normal)

Deactivates of the use of alternate glyphs.

[`small-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#small-caps)

Enables display of small capitals (OpenType feature: `smcp`). Small-caps glyphs typically use the form of uppercase letters but are displayed using the same size as lowercase letters.

[`all-small-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#all-small-caps)

Enables display of small capitals for both upper and lowercase letters (OpenType features: `c2sc`, `smcp`).

[`petite-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#petite-caps)

Enables display of petite capitals (OpenType feature: `pcap`).

[`all-petite-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#all-petite-caps)

Enables display of petite capitals for both upper and lowercase letters (OpenType features: `c2pc`, `pcap`).

[`unicase`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#unicase)

Enables display of mixture of small capitals for uppercase letters with normal lowercase letters (OpenType feature: `unic`).

[`titling-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#titling-caps)

Enables display of titling capitals (OpenType feature: `titl`). Uppercase letter glyphs are often designed for use with lowercase letters. When used in all uppercase titling sequences they can appear too strong. Titling capitals are designed specifically for this situation.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#description)

-------------------------------------------------------------------------------------------------------------------

The `font-variant-caps` property controls the use of alternate glyphs used for small or petite capitals or for titling.

When a given font includes capital letter glyphs of multiple different sizes, this property selects the most appropriate ones. If petite capital glyphs are not available, they are rendered using small capital glyphs. If these are not present, the browser synthesizes them from the uppercase glyphs.

The value is a single keyword. For each value, if the font doesn't support the OpenType value, then it synthesizes the glyphs. Fonts sometimes include special glyphs for various caseless characters (such as punctuation marks) to better match the capitalized characters around them. However, small capital glyphs are never synthesized for caseless characters.

### [Language-specific rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#language-specific_rules)

This property accounts for language-specific case mapping rules. For example:

*   In Turkic languages, such as Turkish (tr), Azerbaijani (az), Crimean Tatar (crh), Volga Tatar (tt), and Bashkir (ba), there are two kinds of `i` (one with the dot, one without) and two case pairings: `i`/`İ` and `ı`/`I`.
*   In German (de), the `ß` may become `ẞ` (U+1E9E) in uppercase.
*   In Greek (el), vowels lose their accent when the whole word is in uppercase (`ά`/`Α`), except for the disjunctive eta (`ή`/`Ή`). Also, diphthongs with an accent on the first vowel lose the accent and gain a diacritic on the second vowel (`άι`/`ΑΪ`).

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#accessibility)

-----------------------------------------------------------------------------------------------------------------------

Large sections of text set with a `font-variant` value of `all-small-caps` or `all-petite-caps` may be difficult for people with cognitive concerns such as Dyslexia to read.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [W3C Understanding WCAG 2.2](https://w3c.github.io/wcag/guidelines/22/#visual-presentation "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

font-variant-caps =   
  normal           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  small-caps       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all-small-caps   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  petite-caps      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all-petite-caps  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  unicase          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  titling-caps       

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#examples)

-------------------------------------------------------------------------------------------------------------

### [Setting the small-caps font variant](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#setting_the_small-caps_font_variant)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-variant-caps-prop](https://drafts.csswg.org/css-fonts/#font-variant-caps-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    
*   [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    
*   [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    
*   [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    
*   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-variant-caps/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-variant-caps (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-caps&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-caps%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-caps%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-caps%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")