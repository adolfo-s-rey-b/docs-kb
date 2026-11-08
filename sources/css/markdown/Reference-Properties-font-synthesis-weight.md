*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#mdn-search)
    

`font-synthesis-weight` CSS property
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-synthesis-weight`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property lets you specify whether or not the browser may synthesize the bold typeface when it is missing in a font family.

It is often convenient to use the shorthand property [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
 to control all typeface synthesis values.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    font-synthesis-weight: auto;
    font-synthesis-weight: none;
    
    /* Global values */
    font-synthesis-weight: inherit;
    font-synthesis-weight: initial;
    font-synthesis-weight: revert;
    font-synthesis-weight: revert-layer;
    font-synthesis-weight: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#auto)

Indicates that the missing bold typeface may be synthesized by the browser if needed.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#none)

Indicates that the synthesis of the missing bold typeface by the browser is not allowed.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

font-synthesis-weight =   
  auto  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#examples)

-----------------------------------------------------------------------------------------------------------------

### [Disabling synthesis of bold typeface](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#disabling_synthesis_of_bold_typeface)

This example shows turning off synthesis of the bold typeface by the browser in the `Montserrat` font.

#### HTML

html

    <p class="english">
      This is the default <strong>bold typeface</strong> and
      <em>oblique typeface</em>.
    </p>
    
    <p class="english no-syn">
      The <strong>bold typeface</strong> is turned off here but not the
      <em>oblique typeface</em>.
    </p>
    

#### CSS

css

    @import "https://fonts.googleapis.com/css2?family=Montserrat&display=swap";
    
    .english {
      font-family: "Montserrat", sans-serif;
    }
    .no-syn {
      font-synthesis-weight: none;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-synthesis-weight](https://drafts.csswg.org/css-fonts/#font-synthesis-weight) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [font-synthesis](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
     shorthand, [font-synthesis-small-caps](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-small-caps)
    , [font-synthesis-style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    , [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    , [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-synthesis-weight/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-synthesis-weight (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-synthesis-weight&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-synthesis-weight%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-synthesis-weight%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-synthesis-weight%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")