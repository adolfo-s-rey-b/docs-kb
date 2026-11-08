*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#mdn-search)
    

`letter-spacing` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`letter-spacing`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the spacing between text characters. This value is added to the natural spacing between characters while rendering the text. Positive values of `letter-spacing` spread characters further apart, while negative values of `letter-spacing` bring characters closer together.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#try_it)

------------------------------------------------------------------------------------------------------

    letter-spacing: normal;
    

    letter-spacing: 0.2rem;
    

    letter-spacing: 1px;
    

    letter-spacing: 30%;
    

    letter-spacing: -1px;
    

    <section id="default-example">
      <p id="example-element">
        As much mud in the streets as if the waters had but newly retired from the
        face of the earth, and it would not be wonderful to meet a Megalosaurus,
        forty feet long or so, waddling like an elephantine lizard up Holborn Hill.
      </p>
    </section>
    

    @font-face {
      src: url("/shared-assets/fonts/variable-fonts/AmstelvarAlpha-VF.woff2");
      font-family: "Amstelvar";
      font-style: normal;
    }
    
    section {
      font-size: 1.2em;
      font-family: "Amstelvar", serif;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    letter-spacing: normal;
    
    /* <length-percentage> values */
    letter-spacing: 0.3em;
    letter-spacing: 3px;
    letter-spacing: -0.5px;
    letter-spacing: 50%;
    
    /* Global values */
    letter-spacing: inherit;
    letter-spacing: initial;
    letter-spacing: revert;
    letter-spacing: revert-layer;
    letter-spacing: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#values)

This property is specified as a single value from the following list:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#normal)

The normal letter spacing for the current font. Unlike a value of `0`, this keyword allows the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 to alter the space between characters in order to justify text.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies extra inter-character space _in addition to_ the default space between characters. While values can be negative, these may be constrained to implementation-specific limits. User agents may not further increase or decrease the inter-character space in order to justify text.

Percentage values are calculated relative to the width of the space character of the font applied to the text.

**Note:** When `letter-spacing` is non-zero, user agents do not apply optional ligatures, such as the `liga` (standard ligatures) and `clig` (contextual ligatures) OpenType features normally controlled by [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
. These features can be explicitly re-enabled with [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#accessibility)

--------------------------------------------------------------------------------------------------------------------

A large positive or negative `letter-spacing` value will make the word(s) the styling is applied to unreadable. For text styled with a very large positive value, the letters will be so far apart that the word(s) will appear like a series of individual, unconnected letters. For text styled with a very large negative value, the letters can overlap each other to the point where the word(s) may be unrecognizable.

Legible letter-spacing must be determined on a case-by-case basis, as different font families have different character widths. There is no one value that can ensure all font families automatically maintain their legibility.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.8 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-visual-presentation.html "External link (opens in new tab)")
    

[Internationalization concerns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#internationalization_concerns)

----------------------------------------------------------------------------------------------------------------------------------------------------

Some written languages should not have any letter spacing applied. For instance, languages that use the Arabic script expect connected letters to remain visually connected, as in the following example. Applying letter spacing may lead to the text looking broken.

html

    <p lang="ar" dir="rtl">شسيبتنمك</p>
    

    p {
      font-size: 3em;
      margin-inline-start: 5px;
    }
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | an optimum value consisting of either an absolute length or the keyword `normal` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

letter-spacing =   
  normal               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#examples)

----------------------------------------------------------------------------------------------------------

### [Setting letter-spacing with length values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#setting_letter-spacing_with_length_values)

This example shows several paragraphs with different length `letter-spacing` values set, allowing you to compare them.

#### HTML

The HTML contains several [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements containing text content.

html

    <p class="normal">letter spacing</p>
    <p class="em-wide">letter spacing</p>
    <p class="em-wider">letter spacing</p>
    <p class="em-tight">letter spacing</p>
    <p class="px-wide">letter spacing</p>
    

#### CSS

Our CSS applies a different `letting-spacing` value to each paragraph.

css

    .normal {
      letter-spacing: normal;
    }
    .em-wide {
      letter-spacing: 0.4em;
    }
    .em-wider {
      letter-spacing: 1em;
    }
    .em-tight {
      letter-spacing: -0.05em;
    }
    .px-wide {
      letter-spacing: 6px;
    }
    

#### Result

The rendered result looks like this:

### [Comparing letter-spacing set with length and percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#comparing_letter-spacing_set_with_length_and_percentage)

This example demonstrates that percentage `letter-spacing` values are useful for responsive text sizing.

The code displays several paragraphs that have the same `letter-spacing` set on text with increasing font size. We provide functionality to switch between a length and a percentage `letter-spacing` value, so that you can observe the responsive qualities of using a percentage value.

#### HTML

The HTML contains several [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements containing text content, and an [`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
 that we'll use to toggle between a length `letter-spacing` and a percentage `letter-spacing` value.

html

    <p class="x-small">X-small font-size (0.8em)</p>
    <p class="small">Small font-size (1.3em)</p>
    <p class="medium">Medium font-size (2em)</p>
    <p class="large">Large font-size (3em)</p>
    <p class="x-large">X-Large (3.5em)</p>
    
    <form>
      <label for="ls-toggle">
        Toggle <code>letter-spacing</code> (off: <code>8px</code>, on:
        <code>12%</code>)
      </label>
      <input type="checkbox" id="ls-toggle" />
    </form>
    

#### CSS

Our CSS starts by applying increasing [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 values to each successive paragraph:

    html {
      font-family: "Arial", sans-serif;
    }
    

css

    .x-small {
      font-size: 0.8em;
    }
    
    .small {
      font-size: 1.3em;
    }
    
    .medium {
      font-size: 2em;
    }
    
    .large {
      font-size: 3em;
    }
    
    .x-large {
      font-size: 3.5em;
    }
    

We apply a `letter-spacing` value of `8px` to all paragraphs by default. When the checkbox is checked, however, we change the `letter-spacing` value to `12%`:

css

    p {
      letter-spacing: 8px;
    }
    
    p:has(~ form > input:checked) {
      letter-spacing: 12%;
    }
    

#### Result

The rendered result looks like this:

First, note how the initial length letter spacing value looks OK when applied to the larger font sizes, but it doesn't look good on the smaller font sizes. Now toggle the checkbox, and note how the percentage letter spacing looks appropriate on all lines, as it scales with the font size.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# letter-spacing-property](https://drafts.csswg.org/css-text/#letter-spacing-property) |
| [Scalable Vector Graphics (SVG) 2  <br>\# LetterSpacingProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#LetterSpacingProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing#see_also)

----------------------------------------------------------------------------------------------------------

*   [`font-kerning`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning)
    
*   [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
    
*   SVG [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/letter-spacing)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/letter-spacing/index.md?plain=1 "Folder: en-us/web/css/reference/properties/letter-spacing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fletter-spacing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fletter-spacing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fletter-spacing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fletter-spacing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F91e08923c809ca8deded3e3294f49bbe1a4a00b3%0A*+Document+last+modified%3A+2026-09-10T06%3A51%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")