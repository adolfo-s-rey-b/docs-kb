*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#mdn-search)
    

`font-synthesis-style` CSS property
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-synthesis-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property lets you specify whether or not the browser may synthesize the oblique typeface when it is missing in a font family.

It is often convenient to use the shorthand property [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
 to control all typeface synthesis values.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    font-synthesis-style: auto;
    font-synthesis-style: none;
    font-synthesis-style: oblique-only;
    
    /* Global values */
    font-synthesis-style: inherit;
    font-synthesis-style: initial;
    font-synthesis-style: revert;
    font-synthesis-style: revert-layer;
    font-synthesis-style: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#auto)

Indicates that the missing oblique typeface may be synthesized by the browser if needed.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#none)

Indicates that the synthesis of the missing oblique typeface by the browser is _not_ allowed.

[`oblique-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#oblique-only)

Same as `auto`, but no font synthesis occurs if `font-style: italic` is set.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

font-synthesis-style =   
  auto          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  oblique-only    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#examples)

----------------------------------------------------------------------------------------------------------------

### [Disabling synthesis of oblique typeface](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#disabling_synthesis_of_oblique_typeface)

This example shows turning off synthesis of the oblique typeface by the browser in the `Montserrat` font.

#### HTML

html

    <p class="english">
      This is the default <em>oblique typeface</em> and
      <strong>bold typeface</strong>.
    </p>
    
    <p class="english no-syn">
      The <em>oblique typeface</em> is turned off here but not the
      <strong>bold typeface</strong>.
    </p>
    

#### CSS

css

    @import "https://fonts.googleapis.com/css2?family=Montserrat&display=swap";
    
    .english {
      font-family: "Montserrat", sans-serif;
    }
    
    .no-syn {
      font-synthesis-style: none;
    }
    

#### Result

### [Comparison of font-synthesis-style values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#comparison_of_font-synthesis-style_values)

This example compares all the `font-synthesis-style` values using italic and oblique styled texts.

#### HTML

html

    <div class="fss-none">
      <h2>font-synthesis-style: none</h2>
      <p class="oblique">This text is set to <code>oblique</code></p>
      <p class="italic">This text is set to <code>italic</code></p>
    </div>
    
    <div class="fss-auto">
      <h2>font-synthesis-style: auto</h2>
      <p class="oblique">This text is set to <code>oblique</code></p>
      <p class="italic">This text is set to <code>italic</code></p>
    </div>
    
    <div class="fss-oblique-only">
      <h2>font-synthesis-style: oblique-only</h2>
      <p class="oblique">This text is set to <code>oblique</code></p>
      <p class="italic">This text is set to <code>italic</code></p>
    </div>
    

#### CSS

    @import "https://fonts.googleapis.com/css2?family=Montserrat&display=swap";
    
    p {
      font-family: "Montserrat", sans-serif;
      font-size: 1.2rem;
    }
    
    @supports not (font-synthesis-style: oblique-only) {
      body::before {
        content: "Your browser doesn't support the 'oblique-only' value.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    /* Specify style of the font synthesis */
    .fss-none {
      font-synthesis-style: none;
    }
    
    .fss-auto {
      font-synthesis-style: auto;
    }
    
    .fss-oblique-only {
      font-synthesis-style: oblique-only;
    }
    
    /* Set font styles */
    .oblique {
      font-style: oblique;
    }
    
    .italic {
      font-style: italic;
    }
    
    /* Styles for the demonstration */
    .oblique::after {
      content: " (font-style: oblique)";
      font-size: 0.8rem;
      vertical-align: sub;
    }
    
    .italic::after {
      content: " (font-style: italic)";
      font-size: 0.8rem;
      vertical-align: sub;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-synthesis-style](https://drafts.csswg.org/css-fonts/#font-synthesis-style) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style#see_also)

----------------------------------------------------------------------------------------------------------------

*   [font-synthesis](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
     shorthand, [font-synthesis-small-caps](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-small-caps)
    , [font-synthesis-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    , [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    , [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-synthesis-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-synthesis-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-synthesis-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-synthesis-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-synthesis-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-synthesis-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")