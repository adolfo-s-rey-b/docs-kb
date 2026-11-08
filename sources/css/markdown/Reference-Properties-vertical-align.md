*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#mdn-search)
    

`vertical-align` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`vertical-align`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the vertical alignment of an inline, inline-block, or table-cell box.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#constituent_properties)

--------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`alignment-baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline)
    
*   [`baseline-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source)
    
*   [`baseline-shift`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift)
    

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#try_it)

------------------------------------------------------------------------------------------------------

    vertical-align: baseline;
    

    vertical-align: top;
    

    vertical-align: middle;
    

    vertical-align: bottom;
    

    vertical-align: sub;
    

    vertical-align: text-top;
    

    <section class="default-example" id="default-example">
      <p>
        Align the star:
        <img id="example-element" src="/shared-assets/images/examples/star2.png" />
      </p>
    </section>
    

    #default-example > p {
      line-height: 3em;
      font-family: monospace;
      font-size: 1.2em;
      text-decoration: underline overline;
    }
    

The `vertical-align` property can be used in two contexts:

*   To vertically align an inline-level element's box inside its containing line box. For example, it could be used to [vertically position an image in a line of text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#vertical_alignment_in_a_line_box)
    .
*   To vertically align [the content of a cell in a table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#vertical_alignment_in_a_table_cell)
    .

Use this shorthand (`vertical-align`) instead of its corresponding longhand properties, unless you need to cascade them independently or (on SVG elements) to support legacy SVG implementations.

Note that `vertical-align` only applies to inline, inline-block and table-cell elements: you can't use it to vertically align [block-level elements](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    vertical-align: baseline;
    vertical-align: sub;
    vertical-align: super;
    vertical-align: text-top;
    vertical-align: text-bottom;
    vertical-align: middle;
    vertical-align: top;
    vertical-align: bottom;
    
    /* <length> values */
    vertical-align: 10em;
    vertical-align: 4px;
    
    /* <percentage> values */
    vertical-align: 20%;
    
    /* Global values */
    vertical-align: inherit;
    vertical-align: initial;
    vertical-align: revert;
    vertical-align: revert-layer;
    vertical-align: unset;
    

The `vertical-align` property is specified as one of the values listed below.

### [Values for inline elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#values_for_inline_elements)

#### Parent-relative values

These values vertically align the element relative to its parent element:

[`baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#baseline)

Aligns the baseline of the element with the baseline of its parent. The baseline of some [replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
, like [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
, is not specified by the HTML specification, meaning that their behavior with this keyword may vary between browsers.

[`sub`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#sub)

Aligns the baseline of the element with the subscript-baseline of its parent.

[`super`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#super)

Aligns the baseline of the element with the superscript-baseline of its parent.

[`text-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#text-top)

Aligns the top of the element with the top of the parent element's font.

[`text-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#text-bottom)

Aligns the bottom of the element with the bottom of the parent element's font.

[`middle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#middle)

Aligns the middle of the element with the baseline plus half the x-height of the parent.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Aligns the baseline of the element to the given length above the baseline of its parent. A negative value is allowed.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Aligns the baseline of the element to the given percentage above the baseline of its parent, with the value being a percentage of the [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
 property. A negative value is allowed.

#### Line-relative values

The following values vertically align the element relative to the entire line:

[`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#top)

Aligns the top of the element and its descendants with the top of the entire line.

[`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#bottom)

Aligns the bottom of the element and its descendants with the bottom of the entire line.

For elements that do not have a baseline, the bottom margin edge is used instead.

### [Values for table cells](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#values_for_table_cells)

[`baseline` (and `sub`, `super`, `text-top`, `text-bottom`, `<length>`, and `<percentage>`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#baseline_2)

Aligns the baseline of the cell with the baseline of all other cells in the row that are baseline-aligned.

[`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#top_2)

Aligns the top padding edge of the cell with the top of the row.

[`middle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#middle_2)

Centers the padding box of the cell within the row.

[`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#bottom_2)

Aligns the bottom padding edge of the cell with the bottom of the row.

Negative values are allowed.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `baseline` |
| Applies to | as each of the properties of the shorthand:. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand: |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

vertical-align =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 first [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 last [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
        [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'alignment-baseline'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'baseline-shift'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift)
        
  
[<alignment-baseline>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline)
 =   
  baseline           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-metric>    
  
[<baseline-shift>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift)
 =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sub                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  super                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  top                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom                 
  
<baseline-metric> =   
  text-bottom   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  alphabetic    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ideographic   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  middle        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  central       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  mathematical  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hanging       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  text-top        
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#examples)

----------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#basic_example)

#### HTML

html

    <div>
      An <img src="frame_image.svg" alt="link" width="32" height="32" /> image with
      a default alignment.
    </div>
    <div>
      An
      <img class="top" src="frame_image.svg" alt="link" width="32" height="32" />
      image with a text-top alignment.
    </div>
    <div>
      An
      <img class="bottom" src="frame_image.svg" alt="link" width="32" height="32" />
      image with a text-bottom alignment.
    </div>
    <div>
      An
      <img class="middle" src="frame_image.svg" alt="link" width="32" height="32" />
      image with a middle alignment.
    </div>
    

#### CSS

css

    img.top {
      vertical-align: text-top;
    }
    img.bottom {
      vertical-align: text-bottom;
    }
    img.middle {
      vertical-align: middle;
    }
    

#### Result

### [Vertical alignment in a line box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#vertical_alignment_in_a_line_box)

#### HTML

html

    <p>
    top:         <img style="vertical-align: top" src="star.png" alt="star"/>
    middle:      <img style="vertical-align: middle" src="star.png" alt="star"/>
    bottom:      <img style="vertical-align: bottom" src="star.png" alt="star"/>
    super:       <img style="vertical-align: super" src="star.png" alt="star"/>
    sub:         <img style="vertical-align: sub" src="star.png" alt="star"/>
    </p>
    
    <p>
    text-top:    <img style="vertical-align: text-top" src="star.png" alt="star"/>
    text-bottom: <img style="vertical-align: text-bottom" src="star.png" alt="star"/>
    0.2em:       <img style="vertical-align: 0.2em" src="star.png" alt="star"/>
    -1em:        <img style="vertical-align: -1em" src="star.png" alt="star"/>
    20%:         <img style="vertical-align: 20%" src="star.png" alt="star"/>
    -100%:       <img style="vertical-align: -100%" src="star.png" alt="star"/>
    </p>
    

    #* {
      box-sizing: border-box;
    }
    
    img {
      margin-right: 0.5em;
    }
    
    p {
      height: 3em;
      padding: 0 0.5em;
      font-family: monospace;
      text-decoration: underline overline;
      margin-left: auto;
      margin-right: auto;
      width: 80%;
    }
    

#### Result

### [Vertical alignment in a table cell](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#vertical_alignment_in_a_table_cell)

In this example, we have a table with a single row containing six cells. The row sets `vertical-align` to `bottom` as the default value.

*   The first four cells each set their own `vertical-align` values, and these override the row's value.
*   The fifth cell does not set any `vertical-align` value, so inherits the row's value.

The sixth cell is only used to ensure that the cells are tall enough to see the effect.

#### HTML

html

    <table>
      <tbody>
        <tr class="bottom">
          <td class="baseline">baseline</td>
          <td class="top">top</td>
          <td class="middle">middle</td>
          <td>bottom</td>
          <td>Row's style</td>
          <td>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
            pretium felis eu sem mattis vulputate.
          </td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    table {
      margin-left: auto;
      margin-right: auto;
      width: 80%;
    }
    
    table,
    th,
    td {
      border: 1px solid black;
    }
    
    td {
      padding: 0.5em;
      font-family: monospace;
    }
    
    .bottom {
      vertical-align: bottom;
    }
    
    .baseline {
      vertical-align: baseline;
    }
    
    .top {
      vertical-align: top;
    }
    
    .middle {
      vertical-align: middle;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# propdef-vertical-align](https://drafts.csswg.org/css-inline/#propdef-vertical-align) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align#see_also)

----------------------------------------------------------------------------------------------------------

*   [Typical use cases of flexbox, section "Center item"](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Use_cases#center_item)
    
*   [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
    , [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    , [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
    
*   [Understanding `vertical-align`, or "How (Not) To Vertically Center Content"](https://phrogz.net/css/vertical-align/index.html "External link (opens in new tab)")
    
*   [Vertical-Align: All You Need To Know](https://christopheraue.net/design/vertical-align "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/vertical-align/index.md?plain=1 "Folder: en-us/web/css/reference/properties/vertical-align (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fvertical-align&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fvertical-align%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fvertical-align%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fvertical-align%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")