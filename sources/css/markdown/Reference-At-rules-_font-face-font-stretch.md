*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#mdn-search)
    

`font-stretch` CSS at-rule descriptor
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** The `font-stretch` descriptor was renamed to [`font-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-width)
 in the [CSS Fonts specification](https://drafts.csswg.org/css-fonts/#font-stretch-desc "External link (opens in new tab)")
. To preserve compatibility, the specification retains `font-stretch` as a legacy alias for the `font-width` descriptor.

The **`font-stretch`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 descriptor allows authors to specify a normal, condensed, or expanded face for the fonts specified in the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule.

For a particular font family, authors can download various font faces corresponding to the different styles of the same font family, and then use the `font-stretch` descriptor to specify the font face's stretch explicitly.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#syntax)

-------------------------------------------------------------------------------------------------------------

The `font-stretch` descriptor can take a single value from the list below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#normal)

Specifies a normally condensed font face.

[`semi-condensed`, `condensed`, `extra-condensed`, `ultra-condensed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#semi-condensed)

Specifies a more condensed font face than normal, with ultra-condensed being the most condensed.

[`semi-expanded`, `expanded`, `extra-expanded`, `ultra-expanded`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#semi-expanded)

Specifies a more expanded font face than normal, with ultra-expanded being the most expanded.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#percentage)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value between 50% and 200% (inclusive). Negative values are not allowed for this descriptor.

In earlier versions of the `font-stretch` specification, the descriptor accepts only the nine keyword values. CSS Fonts Level 4 extends the syntax to accept a `<percentage>` value as well. This enables variable fonts to offer a continuous variation of character widths. For TrueType or OpenType variable fonts, the `wdth` variation is used to implement varying widths.

If the font does not provide a face that exactly matches the given value, then values less than `100%` map to a condensed face, and values greater than or equal to `100%` map to an expanded face.

### [Keyword to numeric mapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#keyword_to_numeric_mapping)

The table below shows the mapping between keyword values and numeric percentages:

| Keyword | Percentage |
| --- | --- |
| `ultra-condensed` | 50% |
| `extra-condensed` | 62.5% |
| `condensed` | 75% |
| `semi-condensed` | 87.5% |
| `normal` | 100% |
| `semi-expanded` | 112.5% |
| `expanded` | 125% |
| `extra-expanded` | 150% |
| `ultra-expanded` | 200% |

### [Variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#variable_fonts)

Most fonts have a particular width that corresponds to one of the keyterm values. However, variable fonts can support a range of widths with fine granularity, giving the designer a greater degree of control over the chosen weight. For this, percentage ranges are useful.

For TrueType or OpenType variable fonts, the `wdth` variation is used to implement varying glyph widths.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#accessibility)

---------------------------------------------------------------------------------------------------------------------------

People with dyslexia and other cognitive conditions may have difficulty reading fonts that are too condensed, especially if the font has a [low color contrast ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color#accessibility)
.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.8 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-visual-presentation.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

font-width =   
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<'font-width'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width)
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<font-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width)
 =   
  normal              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ultra-condensed     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  extra-condensed     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  condensed           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  semi-condensed      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  semi-expanded       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  expanded            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  extra-expanded      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ultra-expanded        

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#examples)

-----------------------------------------------------------------------------------------------------------------

### [Setting a percentage range for font-stretch](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#setting_a_percentage_range_for_font-stretch)

The following example uses the [League Mono](https://www.theleagueofmoveabletype.com/league-mono "External link (opens in new tab)")
 font. It synthesizes different font families from the same font file using the `font-stretch` descriptor with different keywords and percentages.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-stretch-desc](https://drafts.csswg.org/css-fonts/#font-stretch-desc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch#see_also)

-----------------------------------------------------------------------------------------------------------------

*   Modern [`font-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-width)
     descriptor, replacing `font-stretch`
*   [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
     descriptor
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
     descriptor
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
     descriptor
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
     descriptor
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
     descriptor
*   [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
     descriptor
*   [`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
     descriptor
*   [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
     descriptor

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-face/font-stretch/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-face/font-stretch (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-stretch&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-stretch%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-stretch%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-stretch%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")