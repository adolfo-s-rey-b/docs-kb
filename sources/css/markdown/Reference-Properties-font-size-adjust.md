*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#mdn-search)
    

`font-size-adjust` CSS property
===============================

Baseline 2024

Newly available

Since July 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-size-adjust`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property adjusts the size of a font to match a chosen font metric, such as the height of lowercase letters, to a specified proportion of the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
. This property is intended for adjusting fallback fonts to have similar metrics as the first-choice font.

Legibility can become an issue when the first-choice [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
 is unavailable and its replacement fallback font has a significantly different aspect value (height of lowercase letters divided by font size). Legibility of fonts, especially at small font sizes, is determined more by the size of lowercase letters than by the size of uppercase letters. The `font-size-adjust` property is useful for adjusting the font size of fallback fonts to keep the aspect value across fonts consistent, ensuring that the text appears similar regardless of the font used.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    font-size-adjust: none;
    
    /* One value: <number> or from-font */
    font-size-adjust: 0.5;
    font-size-adjust: from-font;
    
    /* Two values */
    font-size-adjust: ex-height 0.5;
    font-size-adjust: ch-width from-font;
    
    /* Global values */
    font-size-adjust: inherit;
    font-size-adjust: initial;
    font-size-adjust: revert;
    font-size-adjust: revert-layer;
    font-size-adjust: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#values)

This property is specified as the keyword `none`, or one (`<number>` or `from-font`) or two (`<font-metric>` and either `<number>` or `from-font`) values.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#none)

No font size adjustment is applied.

[`<font-metric>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#font-metric)

Defines the font metric to use for adjusting the font size. Defaulting to `ex-height`, this parameter is specified as one of the following keywords:

[`ex-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#ex-height)

Uses the ratio of x-height (height of lowercase "x" in a font) to font size (aspect value) to adjust the font size. This keyword value is used to normalize lowercase letters across fonts.

[`cap-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#cap-height)

Uses the ratio of cap-height (height of uppercase letters) to font size to adjust the font size. This keyword value is used to normalize uppercase letters across fonts.

[`ch-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#ch-width)

Uses the ratio of the advance width (horizontal space taken up by a character in a font) of the character "0" (ZERO, U+0030) to font size. This keyword value is used to normalize horizontal narrow pitch of fonts.

[`ic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#ic-width)

Uses the ratio of the advance width of the character "水" (CJK water ideograph, U+6C34) to font size. This keyword value is used to normalize horizontal wide pitch of fonts, particularly those that include CJK (Chinese, Japanese, Korean) characters.

[`ic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#ic-height)

Uses the ratio of the advance height (vertical space taken up by a character in a font) of the character "水" (CJK water ideograph, U+6C34) to font size. This keyword value is used to normalize vertical wide pitch of fonts, particularly those that include CJK characters.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

The proportion to adjust the font size used, depending on the specified `<font-metric>`.

When a `<font-metric>` value is specified, the `<number>` value adjusts the font size as per the chosen `<font-metric>` to maintain a consistent appearance for the specified font metric across different fonts.

The `<number>` value accepts any number from `0` to infinity. `0` yields text of zero height (that is, the text is hidden). Negative values are invalid.

[`from-font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#from-font)

Uses the `<number>` value for the specified `<font-metric>` from the first available font.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#description)

------------------------------------------------------------------------------------------------------------------

The `font-size-adjust` property adjusts the size of a font to match a chosen font metric, such as the height of lowercase letters, to a specified proportion of the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
. The adjustment is applied to each font used to render text, not only to fallback fonts.

Setting a `<number>` adjusts the font size based on the default or stated `<font-metric>`. For example, when set to `ex-height`, the `<number>` value adjusts the selected font size so the height of its `x` glyph is the specified multiple of the font size. This value should generally match the aspect value (ratio of x-height to font size) of the first-choice font. This means that the first-choice font, when available, will display consistently across browsers. Selecting a different value also scales the first-choice font, but in this case, you should prefer to change the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 instead.

**Note:** If the specified `<font-metric>` has been overridden in [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
, e.g., by using the [`size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust)
 descriptor, then the overridden metric will be used in the `font-size-adjust` calculation. This means that when `font-size-adjust` and `size-adjust` are applied together, `size-adjust` does not have any effect.

**Note:** Font metrics like x-height and cap height can vary between font faces (such as bold or italic variants) within the same [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
. When `font-size-adjust` uses `from-font` or a fixed value, the metrics of each font face are adjusted independently, regardless of the relative differences between font faces in the same font family.

The adjusted font size is calculated using the formula `u = ( m / m′ ) s`, where:

*   `m` is the desired ratio specified by `<number>` or obtained using `from-font`.
*   `m′` is the ratio of the chosen metric to the font size in the font being adjusted.
*   `s` is the value of the `font-size` property.
*   `u` is the new, adjusted font size.

Consider this example to see how the adjusted font size is calculated. A first-choice font has a `font-size` of `12px` (`s`), and the ratio of `cap-height` to font size is `0.20` (`m`). The `cap-height` to font size ratio in the fallback font is `0.15` (`m′`). The `font-size-adjust` value has been specified as `cap-height 0.20`. If the primary font is unavailable, the adjusted font size of the fallback font will be calculated to be `16px` (`(0.20 / 0.15) * 12`). This will ensure that the `cap-height` of the fallback font is similar to that of the first-choice font when displayed.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [number](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#interpolation "Values of the <number> CSS data type are interpolated as real, floating-point, numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

font-size-adjust =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 ex-height [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 cap-height [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ch-width [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ic-width [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ic-height [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 from-font [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#examples)

------------------------------------------------------------------------------------------------------------

### [Normalizing font size by lowercase and uppercase letters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#normalizing_font_size_by_lowercase_and_uppercase_letters)

This example demonstrates how the `font-size-adjust` property can be used to retain the same aspect value across fonts. The Verdana font has a relatively high aspect value of `0.545`, which means that the lowercase letters are relatively tall compared to uppercase letters. This makes the text in small font sizes appear legible. However, the Times font has a lower aspect value of `0.447`, so the text is less legible at small sizes. If Verdana is the first-choice font and Times is the fallback font, specifying the `font-size-adjust` property can help to retain the same aspect value in Times. So if the font falls back to Times, the text will maintain a similar level of legibility as it would have with Verdana.

Similarly, the cap-height to font size ratio in Verdana is `0.73` and that in Times is `0.66`. When `font-size-adjust` property is applied to Times to adjust its uppercase letters to match the ratio in Verdana, the Times font displays in adjusted font size ((0.73 / 0.66) \* 14) `15.48px`.

html

    <p class="verdana">
      A: This text uses the Verdana font (14px), which has relatively large
      lowercase letters.
    </p>
    <p class="times">
      B: This text uses the Times font (14px), which is hard to read in small sizes.
    </p>
    <p class="times adj-times-ex-height">
      C: This text in 14px Times font is adjusted to the same aspect value as the
      Verdana font, so lowercase letters are normalized across the two fonts.
    </p>
    <p class="times adj-times-cap-height">
      D: This text in 14px Times font is adjusted to the same cap-height to font
      size ratio as the Verdana font, so uppercase letters are normalized across the
      two fonts.
    </p>
    

css

    .times {
      font-family: "Times", serif;
      font-size: 14px;
    }
    
    .verdana {
      font-family: "Verdana", sans-serif;
      font-size: 14px;
    }
    
    .adj-times-ex-height {
      font-size-adjust: 0.545;
    }
    
    .adj-times-cap-height {
      font-size-adjust: cap-height 0.73;
    }
    

Without `font-size-adjust` in `B`, the switch from Verdana font to Times font could result in a noticeable decrease in legibility due to its lower aspect value. In `C`, notice that only one value is specified for the `font-size-adjust` property, so the default `<font-metric>` value `ex-height` is used. `D` shows how the font would look compared to `A` if its uppercase letter height is adjusted.

### [Determining the aspect value of a font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#determining_the_aspect_value_of_a_font)

For a given font, the same content in two side-by-side [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 elements can be used to determine the font's aspect value. If the same font size is used for content in both spans, the spans will match when the `font-size-adjust` value in one span is accurate for the given font.

In the example below, there are three pairs of side-by-side `<span>` elements, each containing the letter "b". The goal is to adjust the `font-size-adjust` property for the right `<span>` in each pair until the borders around the two letters align. The resulting `font-size-adjust` value can be considered the aspect value for the font.

Starting at `0.6` in the first pair and adjusting to `0.5` in the second, we continue adjusting the `font-size-adjust` property value until the borders around the "b" letters align perfectly in the third pair. In this example, the aspect value is determined to be `0.482`.

html

    <div>
      <p><span>b</span><span class="adjust1">b</span></p>
      0.6
    </div>
    
    <div>
      <p><span>b</span><span class="adjust2">b</span></p>
      0.5
    </div>
    
    <div>
      <p><span>b</span><span class="adjust3">b</span></p>
      0.482
    </div>
    

    body {
      display: flex;
    }
    
    div {
      text-align: center;
    }
    
    p {
      margin: 0 30px 10px 30px;
    }
    

css

    body {
      display: flex;
    }
    
    div {
      text-align: center;
    }
    
    p {
      font-family: "Futura", sans-serif;
      font-size: 50px;
    }
    
    span {
      border: solid 1px red;
    }
    
    .adjust1 {
      font-size-adjust: 0.6;
    }
    
    .adjust2 {
      font-size-adjust: 0.5;
    }
    
    .adjust3 {
      font-size-adjust: 0.482;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 5  <br>\# font-size-adjust-prop](https://drafts.csswg.org/css-fonts-5/#font-size-adjust-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust#see_also)

------------------------------------------------------------------------------------------------------------

*   [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    
*   [`size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust)
     `@font-face` descriptor
*   SVG [`font-size-adjust`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-size-adjust)
     attribute
*   [Learn: Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-size-adjust/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-size-adjust (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-size-adjust&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-size-adjust%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-size-adjust%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-size-adjust%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")