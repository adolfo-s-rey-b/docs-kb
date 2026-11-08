*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#mdn-search)
    

`@font-face` CSS at-rule
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@font-face`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 specifies a custom font with which to display text; the font can be loaded from either a remote server or a locally-installed font on the user's own computer.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#syntax)

------------------------------------------------------------------------------------------------

### [Descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#descriptors)

[`ascent-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override)

Defines the ascent metric for the font.

[`descent-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/descent-override)

Defines the descent metric for the font.

[`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)

Determines how a font face is displayed based on whether and when it is downloaded and ready to use.

[`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)

Specifies a name that will be used as the font face value for font properties. A `font-family` name is required for the `@font-face` rule to be valid.

[`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)

A [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
 value. Accepts two values to specify a range that is supported by a font face, for example `font-stretch: 50% 200%;`

[`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)

A [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 value. Accepts two values to specify a range that is supported by a font face, for example `font-style: oblique 20deg 50deg;`

[`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)

A [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 value. Accepts two values to specify a range that is supported by a font face, for example `font-weight: 100 400;`

[`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings)

Allows control over advanced typographic features in OpenType fonts.

[`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)

Allows low-level control over OpenType or TrueType font variations, by specifying the four-letter axis names of the features to vary, along with their variation values.

[`font-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-width)

Allows authors to specify a normal, condensed, or expanded face for the specified fonts.

[`line-gap-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/line-gap-override)

Defines the line gap metric for the font.

[`size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust)

Defines a multiplier for glyph outlines and metrics associated with this font. This makes it easier to harmonize the designs of various fonts when rendered at the same font size.

[`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)

Specifies references to font resources including hints about the font format and technology. A `src` is required for the `@font-face` rule to be valid.

[`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)

The range of Unicode code points to be used from the font.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#description)

----------------------------------------------------------------------------------------------------------

It's common to use both `url()` and `local()` together, so that the user's installed copy of the font is used if available, falling back to downloading a copy of the font if it's not found on the user's device.

If the `local()` function is provided, specifying a font name to look for on the user's device, and if the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 finds a match, that local font is used. Otherwise, the font resource specified using the `url()` function is downloaded and used.

Browsers attempt to load resources in their list declaration order, so usually `local()` should be written before `url()`. Both functions are optional, so a rule block containing only one or more `local()` without `url()` is possible. If more specific fonts with `format()` or `tech()` values are desired, these should be listed _before_ versions that don't have these values, as the less specific variant would otherwise be tried and used first.

For web delivery, it's generally best to serve fonts in WOFF2 format, because it compresses fonts more efficiently than older formats like WOFF or OpenType, reducing file size and improving load times. WOFF2 is also well supported in modern browsers, making it a safe default choice for most websites.

By allowing authors to provide their own fonts, `@font-face` makes it possible to design content without being limited to the so-called "web-safe" fonts (that is, the fonts that are so common that they're considered to be universally available). The ability to specify the name of a locally-installed font to look for and use makes it possible to customize the font beyond the basics while making it possible to do so without relying on an internet connection.

**Note:** Fallback strategies for loading fonts on older browsers are described in the [`src` descriptor page](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#specifying_fallbacks_for_older_browsers)
.

The `@font-face` at-rule may be used not only at the top level of a CSS, but also inside any [CSS conditional-group at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules#at-rules_and_descriptors)
.

### [Font MIME Types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#font_mime_types)

| Format | MIME type |
| --- | --- |
| TrueType | `font/ttf` |
| OpenType | `font/otf` |
| Web Open Font Format | `font/woff` |
| Web Open Font Format 2 | `font/woff2` |

### [Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#notes)

*   Web fonts are subject to the same domain restriction (font files must be on the same domain as the page using them), unless [HTTP access controls](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
     are used to relax this restriction.
    
*   `@font-face` cannot be declared within a CSS selector. For example, the following will not work:
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#formal_syntax)

--------------------------------------------------------------------------------------------------------------

@font-face =   
  @font-face { <declaration-list> }    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#examples)

----------------------------------------------------------------------------------------------------

### [Specifying a downloadable font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#specifying_a_downloadable_font)

This example specifies a downloadable font to use, applying it to the entire body of the document:

### [Specifying local font alternatives](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#specifying_local_font_alternatives)

In this example, the user's local copy of "Helvetica Neue Bold" is used; if the user does not have that font installed (both the full font name and the Postscript name are tried), then the downloadable font named "MgOpenModernaBold.woff2" is used instead:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-face-rule](https://drafts.csswg.org/css-fonts/#font-face-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face#see_also)

----------------------------------------------------------------------------------------------------

*   [About WOFF](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF)
    
*   [Transfonter webfont generator](https://transfonter.org/ "External link (opens in new tab)")
    
*   [Beautiful fonts with @font-face](https://hacks.mozilla.org/2009/06/beautiful-fonts-with-font-face/ "External link (opens in new tab)")
    
*   [Font Library](https://fontlibrary.org/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-face/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-face (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F91e08923c809ca8deded3e3294f49bbe1a4a00b3%0A*+Document+last+modified%3A+2026-09-10T06%3A51%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")