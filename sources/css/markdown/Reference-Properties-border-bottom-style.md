*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#mdn-search)
    

`border-bottom-style` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-bottom-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the line style of an element's bottom [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
.

**Note:** The specification doesn't define how borders of different styles connect in the corners.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#try_it)

-----------------------------------------------------------------------------------------------------------

    border-bottom-style: none;
    

    border-bottom-style: dotted;
    

    border-bottom-style: dashed;
    

    border-bottom-style: solid;
    

    border-bottom-style: groove;
    

    border-bottom-style: inset;
    

    <section id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with a border around it.
      </div>
    </section>
    

    #example-element {
      background-color: #eeeeee;
      color: black;
      border: 0.75em solid;
      padding: 0.75em;
      width: 80%;
      height: 100px;
    }
    
    body {
      background-color: white;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    border-bottom-style: none;
    border-bottom-style: hidden;
    border-bottom-style: dotted;
    border-bottom-style: dashed;
    border-bottom-style: solid;
    border-bottom-style: double;
    border-bottom-style: groove;
    border-bottom-style: ridge;
    border-bottom-style: inset;
    border-bottom-style: outset;
    
    /* Global values */
    border-bottom-style: inherit;
    border-bottom-style: initial;
    border-bottom-style: revert;
    border-bottom-style: revert-layer;
    border-bottom-style: unset;
    

The `border-bottom-style` property is specified as a single [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 keyword value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

border-bottom-style =   
  <line-style>    
  
[<line-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 =   
  none    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dotted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dashed  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  solid   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  double  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  groove  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ridge   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inset   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outset    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#examples)

---------------------------------------------------------------------------------------------------------------

### [Demonstrating all border styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#demonstrating_all_border_styles)

#### HTML

html

    <table>
      <tbody>
        <tr>
          <td class="b1">none</td>
          <td class="b2">hidden</td>
          <td class="b3">dotted</td>
          <td class="b4">dashed</td>
        </tr>
        <tr>
          <td class="b5">solid</td>
          <td class="b6">double</td>
          <td class="b7">groove</td>
          <td class="b8">ridge</td>
        </tr>
        <tr>
          <td class="b9">inset</td>
          <td class="b10">outset</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    /* Define look of the table */
    table {
      border-width: 3px;
      background-color: #52e385;
    }
    tr,
    td {
      padding: 3px;
    }
    
    /* border-bottom-style example classes */
    .b1 {
      border-bottom-style: none;
    }
    .b2 {
      border-bottom-style: hidden;
    }
    .b3 {
      border-bottom-style: dotted;
    }
    .b4 {
      border-bottom-style: dashed;
    }
    .b5 {
      border-bottom-style: solid;
    }
    .b6 {
      border-bottom-style: double;
    }
    .b7 {
      border-bottom-style: groove;
    }
    .b8 {
      border-bottom-style: ridge;
    }
    .b9 {
      border-bottom-style: inset;
    }
    .b10 {
      border-bottom-style: outset;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# border-style](https://drafts.csswg.org/css-backgrounds/#border-style) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style#see_also)

---------------------------------------------------------------------------------------------------------------

*   The other style-related border properties: [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)
    , [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)
    , [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
    , and [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    .
*   The other bottom-border-related properties: [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
    , [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
    , and [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-bottom-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-bottom-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-bottom-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-bottom-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-bottom-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-bottom-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")