*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#mdn-search)
    

`word-spacing` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`word-spacing`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the spacing between words and between tags.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#try_it)

----------------------------------------------------------------------------------------------------

    word-spacing: normal;
    

    word-spacing: 1rem;
    

    word-spacing: 4px;
    

    word-spacing: 50%;
    

    word-spacing: -0.4ch;
    

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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    word-spacing: normal;
    
    /* <length> values */
    word-spacing: 3px;
    word-spacing: 0.3em;
    word-spacing: 65%;
    word-spacing: -1ex;
    
    /* Global values */
    word-spacing: inherit;
    word-spacing: initial;
    word-spacing: revert;
    word-spacing: revert-layer;
    word-spacing: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#values)

This property is specified as the keyword `normal` or a `<length-percentage>`:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#normal)

The normal inter-word spacing, as defined by the current font and/or the browser.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies extra spacing in addition to the intrinsic inter-word spacing defined by the font. Percentage values are calculated relative to the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 of the text.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#accessibility)

------------------------------------------------------------------------------------------------------------------

A large positive or negative `word-spacing` value will make the sentences the styling is applied to unreadable. For text styled with a very large positive value, the words will be so far apart that it will no longer appear to be a sentence. For text styled with a large negative value, the words can overlap each other to the point where the beginning and end of each word is unrecognizable.

Legible `word-spacing` must be determined on a case-by-case basis, as different font families have different character widths. There is no one value that can ensure all font families automatically maintain their legibility.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.8 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-visual-presentation.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#examples)

--------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#basic_usage)

This example demonstrates basic usage of `word-spacing`.

#### HTML

Our HTML contains two paragraphs of text:

html

    <p id="mozdiv1">Lorem ipsum dolor sit amet.</p>
    <p id="mozdiv2">Lorem ipsum dolor sit amet.</p>
    

#### CSS

Our CSS applies a different `word-spacing` to each paragraph:

css

    #mozdiv1 {
      word-spacing: 15px;
    }
    
    #mozdiv2 {
      word-spacing: 5em;
    }
    

#### Result

The example renders like so:

### [Comparing word-spacing set with length and percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#comparing_word-spacing_set_with_length_and_percentage)

This example demonstrates that percentage `word-spacing` values are useful for responsive text sizing.

The code displays several paragraphs that have the same `word-spacing` set on text with increasing font size. We provide functionality to switch between a length and a percentage `word-spacing` value, so that you can observe the responsive qualities of using a percentage value.

#### HTML

The HTML contains several [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements containing text content, and an [`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
 that we'll use to toggle between a length `word-spacing` and a percentage `word-spacing` value.

html

    <p class="x-small">X-small font-size (0.8em)</p>
    <p class="small">Small font-size (1.3em)</p>
    <p class="medium">Medium font-size (2em)</p>
    <p class="large">Large font-size (3em)</p>
    <p class="x-large">X-Large (3.5em)</p>
    
    <form>
      <label for="ls-toggle">
        Toggle <code>word-spacing</code> (off: <code>10px</code>, on:
        <code>15%</code>)
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
    

We apply a `word-spacing` value of `10px` to all paragraphs by default. When the checkbox is checked, however, we change the `word-spacing` value to `15%`:

css

    p {
      word-spacing: 10px;
    }
    
    p:has(~ form > input:checked) {
      word-spacing: 15%;
    }
    

#### Result

The rendered result looks like this:

First, note how the initial length letter spacing value looks OK when applied to the larger font sizes, but it doesn't look good on the smaller font sizes. Now toggle the checkbox, and note how the percentage letter spacing looks appropriate on all lines, as it scales with the font size.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| Percentages | refer to the width of the affected glyph |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length) |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#formal_syntax)

------------------------------------------------------------------------------------------------------------------

word-spacing =   
  normal               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# word-spacing-property](https://drafts.csswg.org/css-text/#word-spacing-property) |
| [Scalable Vector Graphics (SVG) 2  <br>\# WordSpacingProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#WordSpacingProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing#see_also)

--------------------------------------------------------------------------------------------------------

*   [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
    
*   SVG [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/word-spacing)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/word-spacing/index.md?plain=1 "Folder: en-us/web/css/reference/properties/word-spacing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fword-spacing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fword-spacing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fword-spacing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fword-spacing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F91e08923c809ca8deded3e3294f49bbe1a4a00b3%0A*+Document+last+modified%3A+2026-09-10T06%3A51%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")