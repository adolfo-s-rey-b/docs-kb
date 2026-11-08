*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#mdn-search)
    

`font-variant-position` CSS property
====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/48)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-variant-position`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls the use of alternate, smaller glyphs that are positioned as superscript or subscript.

The glyphs are positioned relative to the baseline of the font, which remains unchanged. These glyphs are typically used in [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
 and [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
 elements.

When the usage of these alternate glyphs is activated, if one character in the run doesn't have such a typographically-enhanced glyph, the whole set of characters of the run is rendered using a fallback method, synthesizing these glyphs.

These alternate glyphs share the same em-box and the same baseline as the rest of the font. They are merely graphically enhanced, and have no effect on the line-height and other box characteristics.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#syntax)

-------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#values)

This property is specified as one of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#normal)

Deactivates alternate superscript and subscript glyphs.

[`sub`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#sub)

Activates subscript alternate glyphs. If, in a given run, one such glyph is not available for a character, all the characters in the run are rendered using synthesized glyphs.

[`super`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#super)

Activates superscript alternate glyphs. If, in a given run, one such glyph is not available for a character, all the characters in the run are rendered using synthesized glyphs.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

font-variant-position =   
  normal  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sub     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  super     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#examples)

-----------------------------------------------------------------------------------------------------------------

### [Setting superscript and subscript forms](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#setting_superscript_and_subscript_forms)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-variant-position-prop](https://drafts.csswg.org/css-fonts/#font-variant-position-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    
*   [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    
*   [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    
*   [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-variant-position/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-variant-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")