*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#mdn-search)
    

`font-width` CSS property
=========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/285)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** The `font-width` property is the modern replacement for [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
, which is a legacy alias. While `font-width` is the specification's preferred name, `font-stretch` currently has broader browser support. Check the [fallback example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#providing_a_font-stretch_fallback)
 and [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#browser_compatibility)
 table for details.

The **`font-width`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property selects a normal, condensed, or expanded face from a font.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#syntax)

--------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#values)

This property is specified as a single value from the following list:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#normal)

Specifies a normally condensed font face.

[`semi-condensed`, `condensed`, `extra-condensed`, `ultra-condensed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#semi-condensed)

Specifies a more condensed font face than normal, with `ultra-condensed` being the most condensed.

[`semi-expanded`, `expanded`, `extra-expanded`, `ultra-expanded`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#semi-expanded)

Specifies a more expanded font face than normal, with `ultra-expanded` being the most expanded.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#percentage)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value between 50% and 200% (inclusive). Negative values are not allowed for this property.

### [Keyword to numeric mapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#keyword_to_numeric_mapping)

The table below shows the mapping between the keyword values and numeric percentages:

| Keyword | Percentage |
| --- | --- |
| `ultra-condensed` | 50% |
| `extra-condensed` | 62.5% |
| `condensed` | 75% |
| `semi-condensed` | 87.5% |
| `normal` | 100% |
| `semi-expanded` | 112.5% |
| `expanded` | 125% |
| `extra-expanded` | 150% |
| `ultra-expanded` | 200% |

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#description)

------------------------------------------------------------------------------------------------------------

Some font families offer additional faces in which the characters are narrower than the normal face (_condensed_ faces) or wider than the normal face (_expanded_ faces).

You can use `font-width` to select a condensed or expanded face from such fonts. If the font you are using does not offer condensed or expanded faces, this property has no effect.

### [Font face selection](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#font_face_selection)

The face selected for a given value of `font-width` depends on the faces supported by the font in question. If the font does not provide a face that exactly matches the given value, then values less than 100% map to a condensed face, and values greater than or equal to 100% map to an expanded face.

The table below demonstrates the effect of setting different percentage values of `font-width` on two different fonts:

The following screenshot shows how the above table is rendered, in case your browser doesn't support the `font-width` property:

![A two-row comparison table showing the lowercase letter e rendered at different widths (50%, 62.5%, 75%, 87.5%, 100%, 112.5%, 125%, 150%, 200%). The top row is labeled Inconsolata and the bottom row Anek Malayalam. Both fonts are sans-serif and Inconsolata's letters are slightly wider compared to Anek Malayalam's.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width/font-face-selection.png)

*   [Inconsolata](https://fonts.google.com/specimen/Inconsolata "External link (opens in new tab)")
     is a variable font that offers a continuous range of widths from 50% to 200%.
*   [Anek Malayalam](https://fonts.google.com/specimen/Anek+Malayalam "External link (opens in new tab)")
     is a variable google font that supports widths from 75% to 125%. Values below and above this range select the closest matching font.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#formal_syntax)

----------------------------------------------------------------------------------------------------------------

font-width =   
  normal              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ultra-condensed     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  extra-condensed     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  condensed           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  semi-condensed      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  semi-expanded       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  expanded            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  extra-expanded      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ultra-expanded        

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#examples)

------------------------------------------------------------------------------------------------------

### [Setting font width percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#setting_font_width_percentages)

html

    <p class="condensed">an elephantine lizard</p>
    <p class="normal">an elephantine lizard</p>
    <p class="expanded">an elephantine lizard</p>
    

css

    @font-face {
      src: url("/shared-assets/fonts/LeagueMono-VF.ttf") format("truetype");
      font-family: "LeagueMonoVariable";
      font-style: normal;
    }
    
    p {
      font:
        1.5rem "LeagueMonoVariable",
        sans-serif;
    }
    
    .condensed {
      font-width: 50%;
    }
    
    .normal {
      font-width: 100%;
    }
    
    .expanded {
      font-width: 200%;
    }
    

### [Providing a font-stretch fallback](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#providing_a_font-stretch_fallback)

Because `font-width` does not yet have broad browser support, you may want to include the legacy [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
 property as a fallback. Place `font-stretch` before `font-width` so that supporting browsers use the modern property:

**Note:** You can automate this fallback pattern using the [postcss-preset-env](https://preset-env.cssdb.org/ "External link (opens in new tab)")
 plugin for PostCSS, which includes the [postcss-font-width-property](https://github.com/csstools/postcss-plugins/tree/main/plugins/postcss-font-width-property "External link (opens in new tab)")
 transform to convert `font-width` properties to `font-stretch` automatically.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# propdef-font-width](https://drafts.csswg.org/css-fonts/#propdef-font-width) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width#see_also)

------------------------------------------------------------------------------------------------------

*   [`font-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-width)
     descriptor for [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
    
*   Legacy [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
     alias property with better browser support
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
     property
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
     property
*   SVG [`font-width`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-width)
     attribute
*   SVG [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-stretch)
     attribute
*   [Learn: Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
    
*   [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-width/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-width (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-width&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-width%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-width%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-width%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F72af34c38ae0d97bc3c9bde4998d538bcc56634a%0A*+Document+last+modified%3A+2026-10-20T18%3A56%3A59.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")