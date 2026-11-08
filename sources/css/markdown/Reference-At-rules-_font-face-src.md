*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#mdn-search)
    

`src` CSS at-rule descriptor
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`src`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 descriptor for the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule specifies the resource containing font data. It is required for the `@font-face` rule to be valid.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#syntax)

----------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#values)

[`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#url)

Specifies an external reference consisting of a [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
, followed by optional hints using the `format()` and `tech()` component values that specify the format and font technology of the resource referenced by the URL. The `format()` and `tech()` components are a comma-separated list of strings of known [font formats](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#font_formats)
 and technologies. If a user agent doesn't support the font technology or formats, it skips downloading the font resource. If no format or technology hints are supplied, the font resource is always downloaded.

[`format()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#format)

An optional declaration that follows the `url()` value that provides a hint for the user agent on the font format. If the value is not supported or invalid, the browser may not download the resource, potentially saving bandwidth. If omitted, the browser will download the resource and then detect the format. If including a font source for backward-compatibility that is not in the list of [defined keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#formal_syntax)
, enclose the format string in quotes. Possible values are described in the [Font formats](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#font_formats)
 section below.

[`tech()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#tech)

An optional declaration that follows the `url()` value that provides a hint for the user agent on the font technology. The value for `tech()` may be one of the keywords described in [Font technologies](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#font_technologies)
.

[`local(<font-face-name>)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#localfont-face-name)

Specifies the font name should the font be available on the user's device. Enclosing the font name in quotes is optional.

**Note:** For OpenType and TrueType fonts, `<font-face-name>` is used to match either the Postscript name or the full font name in the name table of locally available fonts. Which type of name is used varies by platform and font, so you should include both of these names to assure proper matching across platforms. Platform substitutions for a given font name must not be used.

**Note:** Locally available fonts may have been preinstalled on the user's device, or may have been actively installed by the user.

While the set of preinstalled fonts is likely to be the same for all users of a particular device, the set of user-installed fonts is not. By discovering the set of user-installed fonts, a site can therefore build a [fingerprint](https://developer.mozilla.org/en-US/docs/Glossary/Fingerprinting)
 for the device, helping the site to track users across the web.

To prevent this, user agents may ignore user-installed fonts when using `local()`.

[`<font-face-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#font-face-name)

Specifies the full name or postscript name of a locally-installed font face using the `local()` component value, which uniquely identifies a single font face within a larger family. The name can optionally be enclosed in quotes. The font face name [is not case-sensitive](https://drafts.csswg.org/css-fonts-3/#font-family-casing "External link (opens in new tab)")
.

**Note:** The [Local Font Access API](https://developer.mozilla.org/en-US/docs/Web/API/Local_Font_Access_API "Local Font Access API")
 can be used to access the user's locally installed font data — this includes higher-level details such as names, styles, and families, as well as the raw bytes of the underlying font files.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#description)

--------------------------------------------------------------------------------------------------------------

The value of this descriptor is a prioritized, comma-separated list of external references or locally-installed font face names, where each resource is specified using `url()` or `local()`. When a font is needed, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 iterates over the set of references listed using the first one it can successfully activate. Fonts containing invalid data or local font faces that are not found are ignored and the user agent loads the next font in the list.

If multiple `src` descriptors are set, only the last declared rule that is able to load a resource is applied. If the last `src` descriptor can load a resource and doesn't include a `local()` font, the browser may download external font files and ignore the local version even if there is one available on the device.

**Note:** Values within descriptors that the browser considers invalid are ignored. Some browsers will ignore the whole descriptor if any item is invalid, even if only one item is invalid. This may affect design of fallbacks. See [Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#browser_compatibility)
 for more information.

As with other URLs in CSS, the URL may be relative, in which case it is resolved relative to the location of the style sheet containing the `@font-face` rule. In the case of SVG fonts, the URL points to an element within a document containing SVG font definitions. If the element reference is omitted, a reference to the first defined font is implied. Similarly, font container formats that can contain more than one font load only one of the fonts for a given `@font-face` rule. Fragment identifiers are used to indicate which font to load. If a container format lacks a defined fragment identifier scheme, a 1-based indexing scheme (e.g., "font-collection#1" for the first font, "font-collection#2" for the second font, etc.) is used.

If the font file is a container for multiple fonts, a fragment identifier is included to indicate the sub-font that should be used, as shown below:

### [Font formats](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#font_formats)

The following table shows the valid font keywords and their corresponding font formats. To check if a font format is supported by a browser within CSS, use the [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 rule.

| Keyword | Font Format | Common extensions |
| --- | --- | --- |
| `collection` | OpenType Collection | .otc, .ttc |
| `embedded-opentype` | Embedded OpenType | .eot |
| `opentype` | OpenType | .otf, .ttf |
| `svg` | SVG Font (deprecated) | .svg, .svgz |
| `truetype` | TrueType | .ttf |
| `woff` | WOFF 1.0 | .woff |
| `woff2` | WOFF 2.0 | .woff2 |

**Note:**

*   `format(svg)` stands for [SVG fonts](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Using_fonts)
    , and `tech(color-SVG)` stands for [OpenType fonts with SVG table](https://learn.microsoft.com/en-us/typography/opentype/spec/svg "External link (opens in new tab)")
     (also called OpenType-SVG color fonts), which are completely different.
*   The `opentype` and `truetype` values are equivalent whether the font file uses cubic bezier curves (within CFF/CFF2 table) or quadratic bezier curves (within glyph table).

Older non-normalized `format()` values have the following equivalent syntax; provided as a string enclosed in quotes for backward-compatibility reasons:

| Old syntax | Equivalent syntax |
| --- | --- |
| `format("woff2-variations")` | `format(woff2) tech(variations)` |
| `format("woff-variations")` | `format(woff) tech(variations)` |
| `format("opentype-variations")` | `format(opentype) tech(variations)` |
| `format("truetype-variations")` | `format(truetype) tech(variations)` |

### [Font technologies](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#font_technologies)

The following table shows valid values for the `tech()` descriptor and their corresponding font technologies. To check if a font technology is supported by a browser within CSS, use the [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 at-rule.

| Keyword | Description |
| --- | --- |
| `color-cbdt` | Color bitmap data tables |
| `color-colrv0` | Multi-colored glyphs via COLR version 0 table |
| `color-colrv1` | Multi-colored glyphs via COLR version 1 table |
| `color-sbix` | Standard bitmap graphics tables |
| `color-svg` | SVG multi-colored tables |
| `features-aat` | TrueType `morx` and `kerx` tables |
| `features-graphite` | Graphite features, namely `Silf`, `Glat`, `Gloc`, `Feat`, and `Sill` tables |
| `features-opentype` | OpenType `GSUB` and `GPOS` tables |
| `incremental` | Incremental font loading |
| `palettes` | Font palettes by means of `font-palette` to select one of many color palettes in the font |
| `variations` | Font variations in TrueType and OpenType fonts to control the font axis, weight, glyphs, etc. |

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `n/a (required)` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#formal_syntax)

------------------------------------------------------------------------------------------------------------------

src =   
  <font-src-list>    

<font-src> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 format( <font-format> ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 tech( <font-tech>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  local( <font-family-name> )                           
  
<font-format> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  collection         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  embedded-opentype  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  opentype           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  svg                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  truetype           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  woff               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  woff2                
  
<font-tech> =   
  <font-features-tech>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <color-font-tech>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  variations            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  palettes              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  incremental             
  
<font-family-name> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    
  
<font-features-tech> =   
  features-opentype  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  features-aat       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  features-graphite    
  
<color-font-tech> =   
  color-COLRv0  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-COLRv1  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-SVG     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-sbix    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-CBDT      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#examples)

--------------------------------------------------------------------------------------------------------

### [Specifying font resources using url() and local()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#specifying_font_resources_using_url_and_local)

The example below shows how to define two font faces with the same font family. The `font-family` is named `MainText`. The first font face has a regular font, and the second one is a bold version of the same font family.

### [Specifying font resources using tech() and format() values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#specifying_font_resources_using_tech_and_format_values)

The following example shows how to use the `tech()` and `format()` values to specify font resources. A font using `color-colrv1` technology and `opentype` format is specified using the `tech()` and `format()` values. A color font will be activated if the user agent supports it, and an `opentype` non-color is provided as a fallback.

### [Specifying fallbacks for older browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#specifying_fallbacks_for_older_browsers)

Browsers should use a `@font-face` with a single `src` descriptor listing possible sources for the font. Since the browser will use the first resource that it is able to load, items should be specified in the order of your preference for their usage.

Generally this means that local files should appear before remote files and that resources with `format()` or `tech()` constraints should appear before resources that don't have them (otherwise the less-constrained version would always be selected). For example:

A browser that does not support `tech()` above should ignore the first item and attempt to load the second resource.

Some browsers do not yet [ignore invalid items](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#browser_compatibility)
, and instead fail the whole `src` descriptor if any value is invalid. If working with these browsers you can specify multiple `src` descriptors as fallbacks. Note that multiple `src` descriptors are attempted in reverse-order, so at the end we have our normal descriptor with all the items.

### [Checking if the user agent supports a font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#checking_if_the_user_agent_supports_a_font)

The following example shows how to check if the user agent supports a font technology using the [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 rule. The block of CSS inside `@supports` will be applied if the user agent supports `color-COLRv1` technology.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# src-desc](https://drafts.csswg.org/css-fonts/#src-desc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src#see_also)

--------------------------------------------------------------------------------------------------------

*   [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
    
*   [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
    
*   [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
    
*   [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
    
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    
*   [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
    
*   [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-face/src/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-face/src (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Fsrc&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Fsrc%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-face%2Fsrc%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-face%2Fsrc%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb7e9f482c51817d3a885e26092f8219fd0d9d278%0A*+Document+last+modified%3A+2026-09-28T21%3A00%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")