*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#mdn-search)
    

`math-style` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since August 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The `math-style` property indicates whether MathML equations should render with normal or compact height.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    math-style: normal;
    math-style: compact;
    
    /* Global values */
    math-style: inherit;
    math-style: initial;
    math-style: revert;
    math-style: revert-layer;
    math-style: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#values)

This property is specified as one of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#normal)

The initial value, indicates normal rendering.

[`compact`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#compact)

The math layout on descendants tries to minimize the logical height.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#formal_syntax)

----------------------------------------------------------------------------------------------------------------

math-style =   
  normal   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  compact    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#examples)

------------------------------------------------------------------------------------------------------

### [Changing the style of a formula to compact](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#changing_the_style_of_a_formula_to_compact)

#### CSS

css

    math {
      math-style: normal;
    }
    .compact {
      math-style: compact;
    }
    

#### HTML

html

    <p>
      Normal height
      <math>
        <mrow>
          <munderover>
            <mo>∑</mo>
            <mrow>
              <mi>n</mi>
              <mo>=</mo>
              <mn>1</mn>
            </mrow>
            <mrow>
              <mo>+</mo>
              <mn>∞</mn>
            </mrow>
          </munderover>
        </mrow>
      </math>
      and compact height
      <math class="compact">
        <mrow>
          <munderover>
            <mo>∑</mo>
            <mrow>
              <mi>n</mi>
              <mo>=</mo>
              <mn>1</mn>
            </mrow>
            <mrow>
              <mo>+</mo>
              <mn>∞</mn>
            </mrow>
          </munderover>
        </mrow>
      </math>
      equations.
    </p>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [MathML Core  <br>\# the-math-style-property](https://w3c.github.io/mathml-core/#the-math-style-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style#see_also)

------------------------------------------------------------------------------------------------------

*   [`math-depth`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth)
    
*   [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/math-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/math-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmath-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmath-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmath-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmath-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")