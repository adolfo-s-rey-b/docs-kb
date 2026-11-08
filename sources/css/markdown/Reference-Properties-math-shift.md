*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#mdn-search)
    

`math-shift` CSS property
=========================

Baseline 2025

Newly available

Since December 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The `math-shift` property indicates whether superscripts inside MathML formulas should be raised by a normal or compact shift.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    math-shift: normal;
    math-shift: compact;
    
    /* Global values */
    math-shift: inherit;
    math-shift: initial;
    math-shift: revert;
    math-shift: revert-layer;
    math-shift: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#values)

This property is specified as one of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#normal)

The initial value, indicates normal rendering. Superscripts in MathML formulas use the [superscriptShiftUp](https://w3c.github.io/mathml-core/#dfn-superscriptshiftup "External link (opens in new tab)")
 parameter from the OpenType MATH table.

[`compact`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#compact)

Indicates compact rendering. Superscripts in MathML formulas use the [superscriptShiftUpCramped](https://w3c.github.io/mathml-core/#dfn-superscriptshiftupcramped "External link (opens in new tab)")
 parameter from the OpenType MATH table, which is generally smaller.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#formal_syntax)

----------------------------------------------------------------------------------------------------------------

math-shift =   
  normal   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  compact    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#examples)

------------------------------------------------------------------------------------------------------

### [Normal and compact shift](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#normal_and_compact_shift)

The following MathML displays two versions of "x squared" using a font with an OpenType MATH table. The `math-shift` property is used to raise the superscripts using the `normal` and `compact` shift.

#### CSS

css

    math {
      font-size: 64pt;
      math-shift: normal;
    }
    
    .compact-shift {
      math-shift: compact;
    }
    

#### MathML

html

    <math>
      <msup>
        <mi>x</mi>
        <mn>2</mn>
      </msup>
      <msup class="compact-shift">
        <mi>x</mi>
        <mn>2</mn>
      </msup>
    </math>
    

#### Results

Note that the second "2" has a more compact (lower) shift.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [MathML Core  <br>\# the-math-shift](https://w3c.github.io/mathml-core/#the-math-shift) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift#see_also)

------------------------------------------------------------------------------------------------------

*   [`math-depth`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth)
    
*   [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/math-shift/index.md?plain=1 "Folder: en-us/web/css/reference/properties/math-shift (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmath-shift&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmath-shift%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmath-shift%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmath-shift%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")