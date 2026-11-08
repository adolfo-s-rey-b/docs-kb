*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#mdn-search)
    

`math-depth` CSS property
=========================

Baseline 2026

Newly available

Since March 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`math-depth`** property describes a notion of _depth_ for each element of a mathematical formula, with respect to the top-level container of that formula. This is used to scale the computed value of the [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 of elements when `font-size: math` is applied.

**Note:** `font-size: math` is the default for `<math>` elements in the MathML Core [User Agent stylesheet](https://w3c.github.io/mathml-core/#user-agent-stylesheet "External link (opens in new tab)")
, so it's not necessary to specify it explicitly.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#syntax)

--------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#values)

[`auto-add`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#auto-add)

Set to the inherited `math-depth` plus 1 when inherited [math-style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style)
 is `compact`.

``add([`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer) )``

Set to the inherited `math-depth` plus the specified integer.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

Set to the specified integer.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#formal_syntax)

----------------------------------------------------------------------------------------------------------------

math-depth =   
  auto-add          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  add( <integer> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <integer>           
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#examples)

------------------------------------------------------------------------------------------------------

### [Specifying a math depth](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#specifying_a_math_depth)

The following example shows the effect of changing the `math-depth` property on the font size of subformulas. The numbers in each subformula indicate the `math-depth` and scale factor applied.

The first `<mtext>` element is used as a reference to other subformulas and has no specific styles applied. The second and third subformulas have `math-depth` set to `auto-add` and show the effect of scaling depending on the `math-style`.

The last two subformulas show the effect of setting `math-depth` to a specific value.

#### HTML

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [MathML Core  <br>\# the-math-script-level-property](https://w3c.github.io/mathml-core/#the-math-script-level-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth#see_also)

------------------------------------------------------------------------------------------------------

*   [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    
*   [`math-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/math-depth/index.md?plain=1 "Folder: en-us/web/css/reference/properties/math-depth (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmath-depth&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmath-depth%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmath-depth%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmath-depth%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")