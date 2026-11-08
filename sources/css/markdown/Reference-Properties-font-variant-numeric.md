*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#mdn-search)
    

`font-variant-numeric` CSS property
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-variant-numeric`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls the usage of alternate glyphs for numbers, fractions, and ordinal markers.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#try_it)

------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#syntax)

------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#values)

This property is specified either as `normal` or a space-separated list of the following values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#normal)

This keyword leads to the deactivation of the use of such alternate glyphs.

[`ordinal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#ordinal)

This keyword forces the use of special glyphs for the ordinal markers, like 1st, 2nd, 3rd, 4th in English or a 1a in Italian. It corresponds to the OpenType values `ordn`.

[`slashed-zero`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#slashed-zero)

This keyword forces the use of a 0 with a slash; this is useful when a clear distinction between O and 0 is needed. It corresponds to the OpenType values `zero`.

[_`<numeric-figure-values>`_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#numeric-figure-values)

These values control the figures used for numbers. Two values are possible:

*   `lining-nums` activating the set of figures where numbers are all lying on the baseline. It corresponds to the OpenType values `lnum`.
*   `oldstyle-nums` activating the set of figures where some numbers, like 3, 4, 7, 9 have descenders. It corresponds to the OpenType values `onum`.

[_`<numeric-spacing-values>`_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#numeric-spacing-values)

These values controls the sizing of figures used for numbers. Two values are possible:

*   `proportional-nums` activating the set of figures where numbers are not all of the same size. It corresponds to the OpenType values `pnum`.
*   `tabular-nums` activating the set of figures where numbers are all of the same size, allowing them to be easily aligned like in tables. It corresponds to the OpenType values `tnum`.

[_`<numeric-fraction-values>`_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#numeric-fraction-values)

These values controls the glyphs used to display fractions. Two values are possible:

*   `diagonal-fractions` activating the set of figures where the numerator and denominator are made smaller and separated by a slash. It corresponds to the OpenType values `frac`.
*   `stacked-fractions` activating the set of figures where the numerator and denominator are made smaller, stacked and separated by a horizontal line. It corresponds to the OpenType values `afrc`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

font-variant-numeric =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <numeric-figure-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <numeric-spacing-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <numeric-fraction-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 ordinal [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 slashed-zero [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<numeric-figure-values> =   
  lining-nums    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  oldstyle-nums    
  
<numeric-spacing-values> =   
  proportional-nums  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  tabular-nums         
  
<numeric-fraction-values> =   
  diagonal-fractions  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stacked-fractions     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#examples)

----------------------------------------------------------------------------------------------------------------

### [Setting ordinal numeric forms](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#setting_ordinal_numeric_forms)

Click "Play" in the code blocks below to edit the example in the MDN Playground:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-variant-numeric-prop](https://drafts.csswg.org/css-fonts/#font-variant-numeric-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    
*   [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    
*   [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    
*   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-variant-numeric/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-variant-numeric (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-numeric&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-numeric%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-numeric%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-numeric%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")