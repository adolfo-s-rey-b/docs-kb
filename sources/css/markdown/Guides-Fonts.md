*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#mdn-search)
    

CSS fonts
=========

The **CSS fonts** module defines font-related properties and how font resources are loaded. It lets you define the style of a font, such as its family, size and weight, and the glyph variants to use when multiple are available for a single character.

A font is a resource file containing the visual representation of characters, mapping character codes to glyphs that represent letters, numbers, punctuation and even emojis of a typeface. A font family is a group of fonts that share common design styles and font properties, with each member of the group providing different ways of displaying the glyphs, varying by stroke weight, slant, or relative width, among other attributes. A font typically represents a single style of a typeface, such as Helvetica that is Bold and Italic. A font family is the complete set of styles. Including such a font in a document or design is done by defining a separate `@font-face` declaration for each font resource.

The properties, at-rules, and descriptors of the CSS fonts module enable the downloading of multiple variations of a font. They also define the font file to use for a particular font characteristic, along with fallback instructions in case a resource fails to load. The CSS font selection mechanism describes the process of matching a given set of CSS font properties to a single font face.

The CSS fonts module also supports variable fonts. Unlike regular fonts, where each style is implemented as a separate font file, variable fonts can contain all styles within a single file. By using a single `@font-face` declaration, you can import a variable font that includes all the styles. Depending on the font, this can include a multitude of font variants. Variable fonts are a part of the OpenType font specification.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#reference)

-------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#properties)

*   [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
     shorthand
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
    
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    
*   [`font-kerning`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning)
    
*   [`font-language-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override)
    
*   [`font-optical-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-optical-sizing)
    
*   [`font-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
    
*   [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    
*   [`font-size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust)
    
*   [`font-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width)
     and its legacy alias [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    
*   [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
     shorthand
    
*   [`font-synthesis-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position)
    
*   [`font-synthesis-small-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-small-caps)
    
*   [`font-synthesis-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style)
    
*   [`font-synthesis-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight)
    
*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
     shorthand
    
*   [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    
*   [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    
*   [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    
*   [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    
*   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    
*   [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings)
    

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#at-rules_and_descriptors)

At-rule: [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)

Descriptors:

*   [`ascent-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override)
    
*   [`descent-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/descent-override)
    
*   [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
    
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings)
    
*   [`font-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-width)
     and its legacy alias [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
    
*   [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
    
*   [`line-gap-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/line-gap-override)
    
*   [`size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust)
    
*   [`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
    
*   [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
    

The CSS fonts module also defines the `font-language-override`, `font-named-instance`, `font-size`, `subscript-position-override`, `subscript-size-override`, `superscript-position-override`, and `superscript-size-override` descriptors. Currently, no browsers support these features.

*   At-rule: [`@font-feature-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)
    

The CSS fonts module also defines the [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display)
 descriptor. Currently, no browsers support this feature.

At-rule: [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)

Descriptors:

*   [`base-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/font-family)
    
*   [`override-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors)
    

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#functions)

The CSS fonts module defines the `generic()` function. Currently, no browsers support this feature.

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#data_types)

`font-size` types:

*   [`<absolute-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/absolute-size)
    
*   [`<relative-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size)
    

`font-family` type:

*   [`<generic-family>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family)
    

`font-feature-settings` type:

*   [`<feature-tag-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings#values)
    

`font-format` type:

*   [`<font-format>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#font-format)
    

`font-stretch` type:

*   [`<font-stretch-css3>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#values)
    

`font-tech` types:

*   [`<color-font-tech>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#font-tech)
    
*   [`<font-features-tech>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#font-tech)
    
*   [`<font-tech>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#font-tech)
    

`font-variant` types:

*   [`<font-variant-css2>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`<east-asian-variant-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#values)
    
*   [`<east-asian-width-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#values)
    

`font-variant-ligatures` types:

*   [`<common-lig-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#values)
    
*   [`<contextual-alt-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#values)
    
*   [`<discretionary-lig-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#values)
    
*   [`<historical-lig-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#values)
    

`font-variant-numeric` types:

*   [`<numeric-figure-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#values)
    
*   [`<numeric-fraction-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#values)
    
*   [`<numeric-spacing-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#values)
    

`font-weight` type:

*   [`<font-weight-absolute>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#values)
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#interfaces)

*   [`CSSFontFaceRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFontFaceRule)
    
*   [`CSSFontFeatureValuesRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFontFeatureValuesRule)
    
*   [`CSSFontPaletteValuesRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFontPaletteValuesRule)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#guides)

-------------------------------------------------------------------------------

[Learn: Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)

This beginner's learning article covers the basic fundamentals of text and font styling. It covers how to set the font weight, family, and style by using the [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 shorthand and how to align text and manage line and letter spacing.

[Learn: Web fonts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Web_fonts)

This beginner's learning article explains how to use custom fonts on your web page to allow for more varied and custom text styling.

[OpenType font features](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/OpenType_fonts)

Font features or variants refer to different glyphs or character styles contained within an OpenType font. These include things like ligatures (special glyphs that combine characters like 'fi' or 'ffl'), kerning (adjustments to the spacing between specific letterform pairings), fractions, numeral styles, and a number of others. These are all referred to as OpenType Features, and are made available to use on the web via specific properties and a low-level control property — [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
. This article provides you with all you need to know about using OpenType font features in CSS.

[Web Open Font Format (WOFF)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF)

WOFF uses a compressed version of the same table-based `sfnt` structure used by TrueType, OpenType, and Open Font Format, but adds metadata and private-use data structures, including predefined fields allowing foundries and vendors to provide license information if desired.

[Variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts)

This article will help you get started with using variable fonts.

[Improving font performance](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/CSS#improving_font_performance)

This article, part of the CSS performance guide, discusses font loading, loading only the required glyphs, and defining font display behavior with the `font-display` descriptor.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#related_concepts)

---------------------------------------------------------------------------------------------------

*   [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
     CSS property
*   [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
     CSS property
*   [`text-transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
     CSS property

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#specifications)

-----------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4](https://drafts.csswg.org/css-fonts/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts#see_also)

-----------------------------------------------------------------------------------

*   [CSS font loading](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Font_loading)
     module
*   [CSS font loading API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Font_Loading_API)
    
*   [CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
     module
*   [CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/fonts/index.md?plain=1 "Folder: en-us/web/css/guides/fonts (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFonts&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ffonts%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFonts%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ffonts%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3c91c067a4d36b532a4bce72e5d8a2c5a9279db5%0A*+Document+last+modified%3A+2026-02-27T15%3A24%3A40.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")