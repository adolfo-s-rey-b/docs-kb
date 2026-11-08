*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#mdn-search)
    

`text-underline-offset` CSS property
====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-underline-offset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the offset distance of an underline text decoration line (applied using [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
) from its original position.

`text-underline-offset` is not part of the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 shorthand. While an element can have multiple `text-decoration` lines, `text-underline-offset` only impacts underlining, and **not** other possible line decoration options such as `overline` or `line-through`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#try_it)

-------------------------------------------------------------------------------------------------------------

    text-underline-offset: auto;
    

    text-underline-offset: 8px;
    

    text-underline-offset: -0.5rem;
    

    <section id="default-example">
      <p id="example-element">And after all we are only ordinary</p>
    </section>
    

    p {
      font: 1.5em sans-serif;
      text-decoration-line: underline;
      text-decoration-color: red;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Single keyword */
    text-underline-offset: auto;
    
    /* length */
    text-underline-offset: 0.1em;
    text-underline-offset: 3px;
    
    /* percentage */
    text-underline-offset: 20%;
    
    /* Global values */
    text-underline-offset: inherit;
    text-underline-offset: initial;
    text-underline-offset: revert;
    text-underline-offset: revert-layer;
    text-underline-offset: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#values)

This property is specified as one of the following values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#auto)

The browser chooses the appropriate offset for underlines.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#length)

Specifies the offset of underlines as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, overriding the font file suggestion and the browser default. It is recommended to use `em` units so the offset scales with the font size.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#percentage)

Specifies the offset of underlines as a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 of **1 em** in the element's font. A percentage inherits as a relative value, and so therefore scales with changes in the font. For a given application of this property, the offset is constant across the whole box that the underline is applied to, even if there are child elements with different font sizes or vertical alignment.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| Percentages | refer to the font size of the element itself |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

text-underline-offset =   
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#examples)

-----------------------------------------------------------------------------------------------------------------

### [Demonstration of text-underline-offset](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#demonstration_of_text-underline-offset)

html

    <p class="one-line">Here's some text with an offset wavy red underline!</p>
    <br />
    <p class="two-lines">
      This text has lines both above and below it. Only the bottom one is offset.
    </p>
    

css

    p {
      text-decoration: underline wavy red;
      text-underline-offset: 1em;
    }
    
    .two-lines {
      text-decoration-color: purple;
      text-decoration-line: underline overline;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 4  <br>\# underline-offset](https://drafts.csswg.org/css-text-decor-4/#underline-offset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    
*   [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-underline-offset/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-underline-offset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-underline-offset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-underline-offset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-underline-offset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-underline-offset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")