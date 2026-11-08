*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#mdn-search)
    

`line-height` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`line-height`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the height of a line box in horizontal [writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#vertical-rl)
. In vertical writing modes, it sets the width of a line box. It's commonly used to set the distance between lines of text. On block-level elements in horizontal writing modes, it specifies the preferred height of line boxes within the element, and on non-[replaced](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
 inline elements, it specifies the height that is used to calculate line box height.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#try_it)

---------------------------------------------------------------------------------------------------

    line-height: normal;
    

    line-height: 2.5;
    

    line-height: 3em;
    

    line-height: 150%;
    

    line-height: 32px;
    

    <section id="default-example">
      <div class="transition-all" id="example-element">
        Far out in the uncharted backwaters of the unfashionable end of the western
        spiral arm of the Galaxy lies a small unregarded yellow sun.
      </div>
    </section>
    

    #example-element {
      font-family: "Georgia", serif;
      max-width: 200px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    line-height: normal;
    
    /* Unitless values: use this number multiplied
    by the element's font size */
    line-height: 3.5;
    
    /* <length> values */
    line-height: 3em;
    
    /* <percentage> values */
    line-height: 34%;
    
    /* Global values */
    line-height: inherit;
    line-height: initial;
    line-height: revert;
    line-height: revert-layer;
    line-height: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#values)

This property is specified as a single value from the following list:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#normal)

Depends on the user agent. Desktop browsers (including Firefox) use a default value of roughly **`1.2`**, depending on the element's `font-family`.

[`<number>` (unitless)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#number)

The used value is this unitless [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 multiplied by the element's own font size. The computed value is the same as the specified `<number>`. In most cases, **this is the preferred way** to set `line-height` and avoid unexpected results due to inheritance.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#length)

The specified [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 is used in the calculation of the line box height. Values given in **em** units may produce unexpected results (see example below).

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#percentage)

Relative to the font size of the element itself. The computed value is this [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 multiplied by the element's computed font size. **Percentage** values may produce unexpected results (see the second example below).

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#accessibility)

-----------------------------------------------------------------------------------------------------------------

Use a minimum value of `1.5` for `line-height` for main paragraph content. This will help people experiencing low vision conditions, as well as people with cognitive concerns such as Dyslexia. If the page is zoomed to increase the text size, using a unitless value ensures that the line height will scale proportionately.

[W3C Understanding WCAG 2.2](https://w3c.github.io/wcag/guidelines/22/#visual-presentation "External link (opens in new tab)")

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| Percentages | refer to the font size of the element itself |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | for percentage and length values, the absolute length, otherwise as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | either number or length |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

line-height =   
  normal                     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage \[0,∞\]>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#examples)

-------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#basic_example)

css

    /* All rules below have the same resultant line height */
    
    /* number/unitless */
    div {
      line-height: 1.2;
      font-size: 10pt;
    }
    
    /* length */
    div {
      line-height: 1.2em;
      font-size: 10pt;
    }
    
    /* percentage */
    div {
      line-height: 120%;
      font-size: 10pt;
    }
    
    /* font shorthand */
    div {
      font:
        10pt/1.2 "Bitstream Charter",
        "Georgia",
        serif;
    }
    

It is often more convenient to set `line-height` by using the [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 shorthand as shown above, but this requires the `font-family` property to be specified as well.

### [Prefer unitless numbers for line-height values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#prefer_unitless_numbers_for_line-height_values)

This example shows why it is better to use [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 values instead of [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 values. We will use two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements. The first div, with the green border, uses a unitless `line-height` value. The second div, with the red border, uses a `line-height` value defined in `em`s.

#### HTML

html

    <div class="box green">
      <h1>Avoid unexpected results by using unitless line-height.</h1>
      Length and percentage line-heights have poor inheritance behavior.
    </div>
    
    <div class="box red">
      <h1>Avoid unexpected results by using unitless line-height.</h1>
      Length and percentage line-heights have poor inheritance behavior
    </div>
    
    <!-- The first <h1> line-height is calculated from its own font-size   (30px × 1.1) = 33px -->
    <!-- The second <h1> line-height results from the red div's font-size  (15px × 1.1) = 16.5px, probably not what you want -->
    

#### CSS

css

    .green {
      line-height: 1.1;
      border: solid limegreen;
    }
    
    .red {
      line-height: 1.1em;
      border: solid red;
    }
    
    h1 {
      font-size: 30px;
    }
    
    .box {
      width: 18em;
      display: inline-block;
      vertical-align: top;
      font-size: 15px;
    }
    

#### Result

### [Space between lines in vertical writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#space_between_lines_in_vertical_writing_modes)

The `line-height` property can be used to adjust space between vertical lines in vertical writing modes.

    <div class="haiku">
      古池や蛙飛び込む水の音<br />
      ふるいけやかわずとびこむみずのおと<br />
      富士の風や扇にのせて江戸土産<br />
      ふじのかぜやおうぎにのせてえどみやげ<br />
    </div>
    
    <div class="haiku wide">
      古池や蛙飛び込む水の音<br />
      ふるいけやかわずとびこむみずのおと<br />
      富士の風や扇にのせて江戸土産<br />
      ふじのかぜやおうぎにのせてえどみやげ<br />
    </div>
    

css

    .haiku {
      border: 1px solid;
      margin-bottom: 1rem;
      padding: 0.5rem;
      background-color: wheat;
    
      writing-mode: vertical-rl;
    }
    
    .wide {
      line-height: 2;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# line-height-property](https://drafts.csswg.org/css-inline/#line-height-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height#see_also)

-------------------------------------------------------------------------------------------------------

*   [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
    , [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    
*   [Leading](https://developer.mozilla.org/en-US/docs/Glossary/Leading)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/line-height/index.md?plain=1 "Folder: en-us/web/css/reference/properties/line-height (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fline-height&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fline-height%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fline-height%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fline-height%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")