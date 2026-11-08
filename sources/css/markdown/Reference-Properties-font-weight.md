*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#mdn-search)
    

`font-weight` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-weight`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the weight (or boldness) of the font. The weights available depend on the [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
 that is currently set.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#try_it)

---------------------------------------------------------------------------------------------------

    font-weight: normal;
    

    font-weight: bold;
    

    font-weight: lighter;
    

    font-weight: bolder;
    

    font-weight: 100;
    

    font-weight: 900;
    

    <section id="default-example">
      <p id="example-element">
        London. Michaelmas term lately over, and the Lord Chancellor sitting in
        Lincoln's Inn Hall. Implacable November weather. As much mud in the streets
        as if the waters had but newly retired from the face of the earth, and it
        would not be wonderful to meet a Megalosaurus, forty feet long or so,
        waddling like an elephantine lizard up Holborn Hill.
      </p>
    </section>
    

    section {
      font-size: 1.2em;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#syntax)

---------------------------------------------------------------------------------------------------

css

    /* <font-weight-absolute> keyword values */
    font-weight: normal;
    font-weight: bold;
    
    /* <font-weight-absolute> numeric values [1,1000] */
    font-weight: 100;
    font-weight: 200;
    font-weight: 300;
    font-weight: 400; /* normal */
    font-weight: 500;
    font-weight: 600;
    font-weight: 700; /* bold */
    font-weight: 800;
    font-weight: 900;
    
    /* Keyword values relative to the parent */
    font-weight: lighter;
    font-weight: bolder;
    
    /* Global values */
    font-weight: inherit;
    font-weight: initial;
    font-weight: revert;
    font-weight: revert-layer;
    font-weight: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#values)

This property is specified as a single value from the following list:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#normal)

Normal font weight. Same as `400`.

[`bold`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#bold)

Bold font weight. Same as `700`.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#number)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 value between 1 and 1000, both values included. Higher numbers represent weights that are bolder than (or as bold as) lower numbers. This allows fine-grain control for [variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#variable_fonts)
. For non-variable fonts, if the exact specified weight is unavailable, a [fallback weight](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#fallback_weights)
 algorithm is used — numeric values that are divisible by 100 correspond to common weight names, as described in the [Common weight name mapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#common_weight_name_mapping)
 section below.

[`lighter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#lighter)

One relative font weight lighter than the parent element. Note that only four font weights are considered for relative weight calculation; see the [Meaning of relative weights](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#meaning_of_relative_weights)
 section below.

[`bolder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#bolder)

One relative font weight heavier than the parent element. Note that only four font weights are considered for relative weight calculation; see the [Meaning of relative weights](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#meaning_of_relative_weights)
 section below.

### [Fallback weights](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#fallback_weights)

If the exact weight given is unavailable, then the following rule is used to determine the weight actually rendered:

*   If the target weight given is between `400` and `500` inclusive:
    
    *   Look for available weights between the target and `500`, in ascending order.
    *   If no match is found, look for available weights less than the target, in descending order.
    *   If no match is found, look for available weights greater than `500`, in ascending order.
*   If a weight less than `400` is given, look for available weights less than the target, in descending order. If no match is found, look for available weights greater than the target, in ascending order.
    
*   If a weight greater than `500` is given, look for available weights greater than the target, in ascending order. If no match is found, look for available weights less than the target, in descending order.
    

**Note:** The fallback weight algorithm is only used for rendering. The computed value of the property is still the specified value.

### [Meaning of relative weights](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#meaning_of_relative_weights)

When `lighter` or `bolder` is specified, the below chart shows how the absolute font weight of the element is determined.

Note that when using relative weights, only four font weights are considered — thin (100), normal (400), bold (700), and heavy (900). If a font family has more weights available, they are ignored for the purposes of relative weight calculation.

| Inherited value | `bolder` | `lighter` |
| --- | --- | --- |
| 100 | 400 | 100 |
| 200 | 400 | 100 |
| 300 | 400 | 100 |
| 400 | 700 | 100 |
| 500 | 700 | 100 |
| 600 | 900 | 400 |
| 700 | 900 | 400 |
| 800 | 900 | 700 |
| 900 | 900 | 700 |

### [Common weight name mapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#common_weight_name_mapping)

The numerical values `100` to `900` roughly correspond to the following common weight names (see the [OpenType specification](https://learn.microsoft.com/en-us/typography/opentype/spec/os2#usweightclass "External link (opens in new tab)")
):

| Value | Common weight name |
| --- | --- |
| 100 | Thin (Hairline) |
| 200 | Extra Light (Ultra Light) |
| 300 | Light |
| 400 | Normal (Regular) |
| 500 | Medium |
| 600 | Semi Bold (Demi Bold) |
| 700 | Bold |
| 800 | Extra Bold (Ultra Bold) |
| 900 | Black (Heavy) |
| 950 | [Extra Black (Ultra Black)](https://learn.microsoft.com/en-us/dotnet/api/system.windows.fontweights?view=netframework-4.8#remarks "External link (opens in new tab)") |

### [Variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#variable_fonts)

While many fonts have a particular weight corresponding to one of the numbers in [Common weight name mapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#common_weight_name_mapping)
, most variable fonts support a range of weights providing much finer granularity, giving designers and developers more control over the chosen weight.

For TrueType or OpenType variable fonts, the "wght" variation is used to implement varying widths.

This demo loads with `font-weight: 500;` set. Change the value of the `font-weight` property in the `.sample` selector to see the weight of the text change (e.g., 200, 700). Click "Play" in the code blocks below to edit the example in the MDN Playground:

html

    <p class="sample">
      ...it would not be wonderful to meet a Megalosaurus, forty feet long or so,
      waddling like an elephantine lizard up Holborn Hill.
    </p>
    

css

    @font-face {
      src: url("https://mdn.github.io/shared-assets/fonts/variable-fonts/MutatorSans.ttf");
      font-family: "MutatorSans";
      font-style: normal;
      font-weight: 1 1000;
    }
    
    .sample {
      text-transform: uppercase;
      font-weight: 500;
      font-size: 1.5rem;
      font-family: "MutatorSans", sans-serif;
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#accessibility)

-----------------------------------------------------------------------------------------------------------------

People experiencing low vision conditions may have difficulty reading text set with a `font-weight` value of `100` (Thin/Hairline) or `200` (Extra Light), especially if the font has a [low contrast color ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color#accessibility)
.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.8 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-visual-presentation.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the keyword or the numerical value as specified, with `bolder` and `lighter` transformed to the real value |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

font-weight =   
  <font-weight-absolute>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bolder                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  lighter                   
  
<font-weight-absolute> =   
  normal             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bold               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<number \[1,1000\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#examples)

-------------------------------------------------------------------------------------------------------

### [Setting font weights](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#setting_font_weights)

#### HTML

html

    <p>
      Alice was beginning to get very tired of sitting by her sister on the bank,
      and of having nothing to do: once or twice she had peeped into the book her
      sister was reading, but it had no pictures or conversations in it, "and what
      is the use of a book," thought Alice "without pictures or conversations?"
    </p>
    
    <div>
      I'm heavy<br />
      <span>I'm lighter</span>
    </div>
    

#### CSS

css

    /* Set paragraph text to be bold. */
    p {
      font-weight: bold;
    }
    
    /* Set div text to two steps heavier than
       normal but less than a standard bold. */
    div {
      font-weight: 600;
    }
    
    /* Set span text to be one step lighter
       than its parent. */
    span {
      font-weight: lighter;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-weight-prop](https://drafts.csswg.org/css-fonts/#font-weight-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#see_also)

-------------------------------------------------------------------------------------------------------

*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    
*   SVG [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-weight)
     attribute
*   [Learn: Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
    
*   [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-weight/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-weight (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-weight&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-weight%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-weight%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-weight%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")