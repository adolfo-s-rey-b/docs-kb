*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#mdn-search)
    

`font-style` CSS at-rule descriptor
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 descriptor allows authors to specify font styles for the fonts specified in the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule.

For a particular font family, authors can download various font faces that correspond to the different styles of the same font family and then use the `font-style` descriptor to explicitly specify the font face's style. The values for this CSS descriptor are the same as that of the corresponding [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#syntax)

-----------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#normal)

Selects the normal version of the font-family.

[`italic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#italic)

Specifies that font-face is an italicized version of the normal font.

[`oblique`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#oblique)

Specifies that the font-face is an artificially sloped version of the normal font.

[`oblique` with angle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#oblique_2)

Selects a font classified as `oblique`, and additionally specifies an angle for the slant of the text.

[`oblique` with angle range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#oblique_3)

Selects a font classified as `oblique`, and additionally specifies a range of allowable angle for the slant of the text. Note that a range is only supported when the `font-style` is `oblique`; for `font-style: normal` or `italic`, no second value is allowed.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

font-style =   
  auto                                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  normal                                    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  italic                                    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left                                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right                                     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  oblique [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle \[-90deg,90deg\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#examples)

---------------------------------------------------------------------------------------------------------------

### [Specifying an italic font style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#specifying_an_italic_font_style)

As an example, consider the garamond font family, in its normal form, we get the following result:

![unstyled Garamond](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style/garamondunstyled.jpg)

The italicized version of this text uses the same glyphs present in the unstyled version, but they are artificially sloped by a few degrees.

![artificially sloped garamond](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style/garamondartificialstyle.jpg)

On the other hand, if a true italicized version of the font family exists, we can include it in the `src` descriptor and specify the font style as italic, so that it is clear that the font is italicized. True italics use different glyphs and are a bit different from their upright counterparts, having some unique features and generally have a rounded and calligraphic quality. These fonts are specially created by font designers and are **not** artificially sloped.

![italic garamond](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style/garamonditalic.jpg)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-prop-desc](https://drafts.csswg.org/css-fonts/#font-prop-desc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
    
*   [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
    
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    
*   [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
    
*   [`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
    
*   [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-face/font-style/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-face/font-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Ffont-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Ffont-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F91e08923c809ca8deded3e3294f49bbe1a4a00b3%0A*+Document+last+modified%3A+2026-09-10T06%3A51%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")