*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#mdn-search)
    

`font-stretch` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** The `font-stretch` property was renamed to [`font-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width)
 in the [CSS Fonts specification](https://drafts.csswg.org/css-fonts/#font-stretch-prop "External link (opens in new tab)")
. To preserve compatibility, the specification retains `font-stretch` as a legacy alias for the `font-width` property.

The **`font-stretch`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property selects a normal, condensed, or expanded face from a font.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#try_it)

----------------------------------------------------------------------------------------------------

    font-stretch: condensed;
    

    font-stretch: expanded;
    

    font-stretch: ultra-expanded;
    

    font-stretch: 50%;
    

    font-stretch: 100%;
    

    font-stretch: 150%;
    

    <section class="default-example" id="default-example">
      <p class="transition-all" id="example-element">
        London. Michaelmas term lately over, and the Lord Chancellor sitting in
        Lincoln's Inn Hall. Implacable November weather. As much mud in the streets
        as if the waters had but newly retired from the face of the earth, and it
        would not be wonderful to meet a Megalosaurus, forty feet long or so,
        waddling like an elephantine lizard up Holborn Hill.
      </p>
    </section>
    

    @font-face {
      src: url("/shared-assets/fonts/LeagueMono-VF.ttf") format("truetype");
      font-family: "League";
      font-style: normal;
      font-weight: normal;
    }
    
    section {
      font-size: 1.2em;
      font-family: "League", sans-serif;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    font-stretch: normal;
    font-stretch: ultra-condensed;
    font-stretch: extra-condensed;
    font-stretch: condensed;
    font-stretch: semi-condensed;
    font-stretch: semi-expanded;
    font-stretch: expanded;
    font-stretch: extra-expanded;
    font-stretch: ultra-expanded;
    
    /* Percentage values */
    font-stretch: 50%;
    font-stretch: 100%;
    font-stretch: 200%;
    
    /* Global values */
    font-stretch: inherit;
    font-stretch: initial;
    font-stretch: revert;
    font-stretch: revert-layer;
    font-stretch: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#values)

This property is specified as a single value from the following list:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#normal)

Specifies a normally condensed font face.

[`semi-condensed`, `condensed`, `extra-condensed`, `ultra-condensed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#semi-condensed)

Specifies a more condensed font face than normal, with `ultra-condensed` being the most condensed.

[`semi-expanded`, `expanded`, `extra-expanded`, `ultra-expanded`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#semi-expanded)

Specifies a more expanded font face than normal, with `ultra-expanded` being the most expanded.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#percentage)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value between 50% and 200% (inclusive). Negative values are not allowed for this property.

### [Keyword to numeric mapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#keyword_to_numeric_mapping)

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

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#description)

--------------------------------------------------------------------------------------------------------------

Some font families offer additional faces in which the characters are narrower than the normal face (_condensed_ faces) or wider than the normal face (_expanded_ faces).

You can use `font-stretch` to select a condensed or expanded face from such fonts. If the font you are using does not offer condensed or expanded faces, this property has no effect.

### [Font face selection](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#font_face_selection)

The face selected for a given value of `font-stretch` depends on the faces supported by the font in question. If the font does not provide a face that exactly matches the given value, then values less than `100%` map to a condensed face, and values greater than or equal to `100%` map to an expanded face.

The table below demonstrates the effect of setting different percentage values of `font-stretch` on two different fonts:

    @font-face {
      font-family: "Inconsolata";
      src: url("https://mdn.github.io/shared-assets/fonts/inconsolata/Inconsolata-VF.woff2")
        format("woff2");
    }
    
    @font-face {
      font-family: "Anek Malayalam";
      src: url("https://mdn.github.io/shared-assets/fonts/anek-malayalam/AnekMalayalam-VF.woff2")
        format("woff2");
    }
    
    body {
      font-family: system-ui;
    }
    
    table {
      border-collapse: collapse;
      width: 100%;
    }
    
    tbody th {
      text-align: right;
    }
    
    th,
    td {
      padding: 0.25rem;
      font-weight: normal;
      text-align: center;
    }
    
    td {
      border: solid;
      border-width: 1px;
      font-size: 5rem;
    }
    
    .inconsolata {
      font-family: "Inconsolata", sans-serif;
    }
    
    .anek-malayalam {
      font-family: "Anek Malayalam", sans-serif;
    }
    
    td:nth-child(2) {
      font-stretch: 50%;
    }
    td:nth-child(3) {
      font-stretch: 62.5%;
    }
    td:nth-child(4) {
      font-stretch: 75%;
    }
    td:nth-child(5) {
      font-stretch: 87.5%;
    }
    td:nth-child(6) {
      font-stretch: 100%;
    }
    td:nth-child(7) {
      font-stretch: 112.5%;
    }
    td:nth-child(8) {
      font-stretch: 125%;
    }
    td:nth-child(9) {
      font-stretch: 150%;
    }
    td:nth-child(10) {
      font-stretch: 200%;
    }
    

    <table>
      <thead>
        <tr>
          <th scope="row"></th>
          <th scope="col">50%</th>
          <th scope="col">62.5%</th>
          <th scope="col">75%</th>
          <th scope="col">87.5%</th>
          <th scope="col">100%</th>
          <th scope="col">112.5%</th>
          <th scope="col">125%</th>
          <th scope="col">150%</th>
          <th scope="col">200%</th>
        </tr>
      </thead>
      <tbody>
        <tr class="inconsolata">
          <th scope="row">Inconsolata</th>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
        </tr>
        <tr class="anek-malayalam">
          <th scope="row">Anek Malayalam</th>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
          <td>e</td>
        </tr>
      </tbody>
    </table>
    

*   [Inconsolata](https://fonts.google.com/specimen/Inconsolata "External link (opens in new tab)")
     is a variable font that offers a continuous range of widths from 50% to 200%.
*   [Anek Malayalam](https://fonts.google.com/specimen/Anek+Malayalam "External link (opens in new tab)")
     is a variable google font that supports widths from 75% to 125%. Values below and above this range select the closest matching font.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#formal_syntax)

------------------------------------------------------------------------------------------------------------------

font-stretch =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#examples)

--------------------------------------------------------------------------------------------------------

### [Setting font stretch percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#setting_font_stretch_percentages)

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
      font-stretch: 50%;
    }
    
    .normal {
      font-stretch: 100%;
    }
    
    .expanded {
      font-stretch: 200%;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-stretch-prop](https://drafts.csswg.org/css-fonts/#font-stretch-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch#see_also)

--------------------------------------------------------------------------------------------------------

*   [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)
     descriptor for [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
    
*   Modern [`font-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width)
     property, replacing `font-stretch`
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
     property
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
     property
*   SVG [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-stretch)
     attribute
*   [Learn: Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
    
*   [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-stretch/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-stretch (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-stretch&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-stretch%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-stretch%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-stretch%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F72af34c38ae0d97bc3c9bde4998d538bcc56634a%0A*+Document+last+modified%3A+2026-10-20T18%3A56%3A59.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")