*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#mdn-search)
    

`font-variant-ligatures` CSS property
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-variant-ligatures`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls which [ligatures](https://developer.mozilla.org/en-US/docs/Glossary/Ligature)
 and contextual forms are used in the textual content of the elements it applies to. This leads to more harmonized forms in the resulting text.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#try_it)

--------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#syntax)

--------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#values)

This property is specified as a single keyword or as a space-separated list of the following values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#normal)

This keyword activates the usual ligatures and contextual forms needed for correct rendering. The ligatures and forms activated depend on the font, language, and kind of script. This is the default value.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#none)

This keyword specifies that all ligatures and contextual forms are disabled, even common ones.

[_`<common-lig-values>`_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#common-lig-values)

These values control the most common ligatures, like for `fi`, `ffi`, `th`, or similar. They correspond to the OpenType values `liga` and `clig`. Two values are possible:

*   `common-ligatures` activating these ligatures. Note that the keyword `normal` activates these ligatures.
*   `no-common-ligatures` deactivating these ligatures.

[_`<discretionary-lig-values>`_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#discretionary-lig-values)

These values control specific ligatures, specific to the font and defined by the type designer. They correspond to the OpenType values `dlig`. Two values are possible:

*   `discretionary-ligatures` activating these ligatures.
*   `no-discretionary-ligatures` deactivating the ligatures. Note that the keyword `normal` usually deactivates these ligatures.

[_`<historical-lig-values>`_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#historical-lig-values)

These values control the ligatures used historically, in old books, like the German tz digraph being displayed as ꜩ. They correspond to the OpenType values `hlig`. Two values are possible:

*   `historical-ligatures` activating these ligatures.
*   `no-historical-ligatures` deactivating the ligatures. Note that the keyword `normal` usually deactivates these ligatures.

[_`<contextual-alt-values>`_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#contextual-alt-values)

These values control whether letters adapt to their context—that is, whether they adapt to the surrounding letters. These values correspond to the OpenType values `calt`. Two values are possible:

*   `contextual` specifies that the contextual alternates are to be used. Note that the keyword `normal` usually activates these ligatures too.
*   `no-contextual` prevents their use.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

font-variant-ligatures =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <common-lig-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <discretionary-lig-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <historical-lig-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <contextual-alt-values> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<common-lig-values> =   
  common-ligatures     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-common-ligatures    
  
<discretionary-lig-values> =   
  discretionary-ligatures     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-discretionary-ligatures    
  
<historical-lig-values> =   
  historical-ligatures     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-historical-ligatures    
  
<contextual-alt-values> =   
  contextual     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-contextual    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#examples)

------------------------------------------------------------------------------------------------------------------

### [Setting font ligatures and contextual forms](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#setting_font_ligatures_and_contextual_forms)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-variant-ligatures-prop](https://drafts.csswg.org/css-fonts/#font-variant-ligatures-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    
*   [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    
*   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    
*   [CSS fonts module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-variant-ligatures/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-variant-ligatures (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-ligatures&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-ligatures%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-ligatures%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-ligatures%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")