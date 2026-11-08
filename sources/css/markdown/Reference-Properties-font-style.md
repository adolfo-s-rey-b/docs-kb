*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#mdn-search)
    

`font-style` CSS property
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether a font should be styled with a normal, italic, or oblique face from its [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
.

**Italic** font faces are generally cursive in nature, usually using less horizontal space than their unstyled counterparts, while **oblique** faces are usually just sloped versions of the regular face. When the specified style is not available, both italic and oblique faces are simulated by artificially sloping the glyphs of the regular face (use [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
 to control this behavior).

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#try_it)

--------------------------------------------------------------------------------------------------

    font-style: normal;
    

    font-style: italic;
    

    font-style: oblique;
    

    font-style: oblique 40deg;
    

    <section id="default-example">
      <p id="example-element">
        London. Michaelmas term lately over, and the Lord Chancellor sitting in
        Lincoln's Inn Hall. Implacable November weather. As much mud in the streets
        as if the waters had but newly retired from the face of the earth, and it
        would not be wonderful to meet a Megalosaurus, forty feet long or so,
        waddling like an elephantine lizard up Holborn Hill.
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#syntax)

--------------------------------------------------------------------------------------------------

css

    font-style: normal;
    font-style: italic;
    font-style: oblique;
    font-style: oblique 10deg;
    
    /* Global values */
    font-style: inherit;
    font-style: initial;
    font-style: revert;
    font-style: revert-layer;
    font-style: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#values)

This property is specified as one of the following keyword values. The `oblique` keyword can optionally be followed by an `<angle>`:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#normal)

Selects a font that is classified as `normal` within a [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
.

[`italic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#italic)

Selects a font that is classified as `italic`. If no italic version of the face is available, one classified as `oblique` is used instead. If neither is available, the style is artificially simulated.

[`oblique`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#oblique)

Selects a font that is classified as `oblique`. If no oblique version of the face is available, one classified as `italic` is used instead. If neither is available, the style is artificially simulated.

`oblique` [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)

Selects a font classified as `oblique`, and additionally specifies an angle for the slant of the text. If one or more oblique faces are available in the chosen font family, the one that most closely matches the specified angle is chosen. If no oblique faces are available, the browser will synthesize an oblique version of the font by slanting a normal face by the specified amount. Valid values are degree values of `-90deg` to `90deg` inclusive. If an angle is not specified, an angle of 14 degrees is used. Positive values are slanted to the end of the line, while negative values are slanted towards the beginning.

In general, for a requested angle of 14 degrees or greater, larger angles are preferred; otherwise, smaller angles are preferred (see the spec's [font matching section](https://drafts.csswg.org/css-fonts-4/#font-matching-algorithm "External link (opens in new tab)")
 for the precise algorithm).

The [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
 module also defines `left` and `right` values to select an italic or oblique face with a specific slant direction; however, these values are not supported in any browsers.

### [Variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#variable_fonts)

Variable fonts can offer a fine control over the degree to which an oblique face is slanted. You can select this using the `<angle>` modifier for the `oblique` keyword.

For TrueType or OpenType variable fonts, the `"slnt"` variation is used to implement varying slant angles for oblique, and the `"ital"` variation with a value of 1 is used to implement italic values. See [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings)
.

Click "Play" in the code blocks below to edit the example in the MDN Playground. Change the angle value to see the slant of the text change.

html

    <p class="sample">
      ...it would not be wonderful to meet a Megalosaurus, forty feet long or so,
      waddling like an elephantine lizard up Holborn Hill.
    </p>
    

css

    @font-face {
      src: url("https://mdn.github.io/shared-assets/fonts/variable-fonts/AmstelvarAlpha-VF.woff2");
      font-family: "AmstelvarAlpha";
      font-style: normal;
    }
    
    .sample {
      font:
        2rem "AmstelvarAlpha",
        sans-serif;
      /* font-variation-settings: "slnt" 12; */
      font-style: oblique 23deg;
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#accessibility)

----------------------------------------------------------------------------------------------------------------

Large sections of text set with a `font-style` value of `italic` may be difficult for people with cognitive concerns such as Dyslexia to read.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [W3C Understanding WCAG 2.2](https://w3c.github.io/wcag/guidelines/22/#visual-presentation "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type; `normal` animates as `oblique 0deg` |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#formal_syntax)

----------------------------------------------------------------------------------------------------------------

font-style =   
  normal                           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  italic                           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left                             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right                            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  oblique [<angle \[-90deg,90deg\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#examples)

------------------------------------------------------------------------------------------------------

### [Font styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#font_styles)

    <p class="normal">This paragraph is normal.</p>
    <p class="italic">This paragraph is italic.</p>
    <p class="oblique">This paragraph is oblique.</p>
    

css

    .normal {
      font-style: normal;
    }
    
    .italic {
      font-style: italic;
    }
    
    .oblique {
      font-style: oblique;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-style-prop](https://drafts.csswg.org/css-fonts/#font-style-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style#see_also)

------------------------------------------------------------------------------------------------------

*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    
*   SVG [`font-style`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-style)
     attribute
*   [Learn: Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")