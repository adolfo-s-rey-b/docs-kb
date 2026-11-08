*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#mdn-search)
    

`font-feature-settings` CSS at-rule descriptor
==============================================

Baseline 2025

Newly available

Since September 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-feature-settings`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 descriptor allows you to define the initial settings to use for the font defined by the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule. You can further use this descriptor to control typographic font features such as ligatures, small caps, and swashes, for the font defined by `@font-face`. The values for this descriptor are the same as the [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
 property, except for the global keyword values.

Since this descriptor sets feature values on the font object in the `@font-face` at-rule and not on an entire element, only some glyphs in an element may be rendered using this descriptor.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#syntax)

----------------------------------------------------------------------------------------------------------------------

css

    /* Use the default settings */
    font-feature-settings: normal;
    
    /* Set values for OpenType feature tags */
    font-feature-settings: "smcp";
    font-feature-settings: "smcp" on;
    font-feature-settings: "swsh" 2;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#values)

This descriptor is specified as either the keyword `normal` or as a comma-separated list of `<feature-tag-value>` values. When rendering text, the list of OpenType `<feature-tag-value>` values are passed to the text layout engine to enable or disable font features.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#normal)

Indicates that text is laid out using default font settings. This is the default value.

[`<feature-tag-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#feature-tag-value)

Represents a space-separated tuple consisting of a tag name and an optional value.

The tag name is always a [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 of four [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 characters. If the tag name has more or fewer characters or if it contains characters outside the `U+20` – `U+7E` code point range, the descriptor is invalid.

The optional value can be a positive integer or the keyword `on` or `off`. The keywords `on` and `off` are synonyms for the values `1` and `0`, respectively. If no value is set, the default is `1`. For non-boolean OpenType features (e.g., [stylistic alternates](https://learn.microsoft.com/en-ca/typography/opentype/spec/features_pt#tag-salt "External link (opens in new tab)")
), the value implies a particular glyph to be selected; for boolean features, the value turns the feature on or off.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#formal_syntax)

------------------------------------------------------------------------------------------------------------------------------------

font-feature-settings =   
  normal                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <feature-tag-value>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<feature-tag-value> =   
  <opentype-tag> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[0,∞\]> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 on [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 off [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<opentype-tag> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#examples)

--------------------------------------------------------------------------------------------------------------------------

### [Enabling swash glyphs using the @font-face at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#enabling_swash_glyphs_using_the_font-face_at-rule)

In this example, the tag name `swsh` and a boolean value `1` are used as the value for the `font-feature-settings` descriptor in the `@font-face` at-rule.

#### HTML

html

    <p class="swash-off">Swash is off here</p>
    <p class="swash-on">Swash is on here</p>
    

#### CSS

css

    @font-face {
      font-family: "MonteCarlo";
      src: url("/shared-assets/fonts/monte-carlo/monte-carlo-regular.woff2");
    }
    @font-face {
      font-family: "MonteCarlo2";
      src: url("/shared-assets/fonts/monte-carlo/monte-carlo-regular.woff2");
      font-feature-settings: "swsh" 1;
    }
    p {
      font-size: 3rem;
      margin: 0.7rem 3rem;
    }
    .swash-off {
      font-family: "MonteCarlo", cursive;
    }
    .swash-on {
      font-family: "MonteCarlo2", cursive;
    }
    

#### Result

Line 1 shows the default ornate design of the [MonteCarlo](https://github.com/googlefonts/monte-carlo "External link (opens in new tab)")
 font, and line 2 shows the default glyphs being replaced with [swash](https://learn.microsoft.com/en-ca/typography/opentype/spec/features_pt#tag-swsh "External link (opens in new tab)")
 glyphs.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#specifications)

--------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-rend-desc](https://drafts.csswg.org/css-fonts/#font-rend-desc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings#see_also)

--------------------------------------------------------------------------------------------------------------------------

*   Other `@font-face` descriptors: [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
    , [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
    , [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
    , [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
    , [`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
    
*   Related font properties: [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    , [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    , [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-face/font-feature-settings/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-face/font-feature-settings (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-feature-settings&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-feature-settings%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-feature-settings%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-feature-settings%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")