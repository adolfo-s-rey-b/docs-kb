*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#mdn-search)
    

`font-variation-settings` CSS property
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-variation-settings`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property provides low-level control over [variable font](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts)
 characteristics by letting you specify the four letter axis names of the characteristics you want to vary along with their values.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#try_it)

---------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#syntax)

---------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#values)

This property is specified as `normal` or a comma-separated list of string-number value pairs:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#normal)

Text is laid out using default settings.

[`<string> <number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#string_number)

When rendering text, the list of variable font axis names is passed to the text layout engine to enable or disable font features. Each setting is always one or more pairs consisting of a [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 of 4 ASCII characters followed by a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 indicating the axis value to set. If the `<string>` has more or fewer characters or contains characters outside the U+20 - U+7E code point range, the whole property is invalid. The `<number>` can be fractional or negative, depending on the value range available in your font, as defined by the font designer.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#description)

-------------------------------------------------------------------------------------------------------------------------

This property is a low-level mechanism designed to set variable font features where no other way to enable or access those features exist. You should only use it when no basic properties exist to set those features (e.g., [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
, [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
).

Font characteristics set using `font-variation-settings` will always override those set using the corresponding basic font properties, e.g., `font-weight`, no matter where they appear in the cascade. In some browsers, this is currently only true when the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 declaration includes a [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
 range.

### [Registered and custom axes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#registered_and_custom_axes)

Variable font axes come in two types: **registered** and **custom**.

Registered axes are the most commonly encountered — common enough that the authors of the specification felt they were worth standardizing. Note that this doesn't mean that the author has to include all of these in their font.

Here are the registered axes along with their corresponding CSS properties:

| Axis Tag | CSS Property |
| --- | --- |
| "wght" | [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight) |
| "wdth" | [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch) |
| "slnt" (slant) | [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)<br>: `oblique + angle` |
| "ital" | [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)<br>: `italic` |
| "opsz" | [`font-optical-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-optical-sizing) |

Custom axes can be anything the font designer wants to vary in their font, for example ascender or descender heights, the size of serifs, or anything else they can imagine. Any axis can be used as long as it is given a unique 4-character axis. Some will end up becoming more common, and may even become registered over time.

**Note:** Registered axis tags are identified using lower-case tags, whereas custom axes should be given upper-case tags. Note that font designers aren't forced to follow this practice in any way, and some won't. The important takeaway here is that axis tags are case-sensitive.

To use variable fonts on your operating system, you need to make sure that it is up to date. For example Linux OSes need the latest Linux FreeType version, and macOS before 10.13 does not support variable fonts. If your operating system is not up to date, you will not be able to use variable fonts in web pages or the Firefox Developer Tools.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a transform |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

font-variation-settings =   
  normal                        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <opentype-tag> [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<opentype-tag> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#examples)

-------------------------------------------------------------------------------------------------------------------

You can find a number of other variable font examples in our [Variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts)
 guide.

### [Controlling variable font weight (wght)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#controlling_variable_font_weight_wght)

Click "Play" in the code blocks below to edit the example in the MDN Playground. Edit the CSS to play with different font weight values. See what happens when you specify a value outside the weight range.

### [Controlling variable font slant (slnt)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#controlling_variable_font_slant_slnt)

Click "Play" in the code blocks below to edit the example in the MDN Playground. Edit the CSS to play with different font slant/oblique values.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-variation-settings-def](https://drafts.csswg.org/css-fonts/#font-variation-settings-def) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [Variable fonts guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts)
    
*   [OpenType font variations overview](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview "External link (opens in new tab)")
     on microsoft.com
*   [OpenType design-variation axis tag registry](https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg "External link (opens in new tab)")
     on microsoft.com
*   [OpenType variable fonts](https://www.axis-praxis.org/ "External link (opens in new tab)")
     on axis-praxis.org
*   [Variable fonts](https://v-fonts.com/ "External link (opens in new tab)")
     on v-fonts.com

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-variation-settings/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-variation-settings (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variation-settings&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variation-settings%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variation-settings%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variation-settings%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F91e08923c809ca8deded3e3294f49bbe1a4a00b3%0A*+Document+last+modified%3A+2026-09-10T06%3A51%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")