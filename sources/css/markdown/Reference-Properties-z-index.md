*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#mdn-search)
    

`z-index` CSS property
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`z-index`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the z-order of a [positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 element and its descendants or flex and grid items. Overlapping elements with a larger z-index cover those with a smaller one.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#try_it)

-----------------------------------------------------------------------------------------------

    z-index: auto;
    

    z-index: 1;
    

    z-index: 3;
    

    z-index: 5;
    

    z-index: 7;
    

    <section class="default-example container" id="default-example">
      <div id="example-element">Change my z-index</div>
      <div class="block blue position1">z-index: 6</div>
      <div class="block blue position2">z-index: 4</div>
      <div class="block blue position3">z-index: 2</div>
      <div class="block red position4">z-index: auto</div>
      <div class="block red position5">z-index: auto</div>
      <div class="block red position6">z-index: auto</div>
    </section>
    

    #example-element {
      top: 15px;
      left: 15px;
      width: 180px;
      height: 230px;
      position: absolute;
      /* center the text so it is visible even when z-index is set to auto */
      line-height: 215px;
      font-family: monospace;
      background-color: #fcfbe5;
      border: solid 5px #e3e0a1;
      z-index: auto;
      color: black;
    }
    
    .container {
      display: inline-block;
      width: 250px;
      position: relative;
    }
    
    .block {
      width: 150px;
      height: 50px;
      position: absolute;
      font-family: monospace;
      color: black;
    }
    
    .blue {
      background-color: #e5e8fc;
      border: solid 5px #112382;
      /* move text to the bottom of the box */
      line-height: 55px;
    }
    
    .red {
      background-color: #fce5e7;
      border: solid 5px #e3a1a7;
    }
    
    .position1 {
      top: 0;
      left: 0;
      z-index: 6;
    }
    
    .position2 {
      top: 30px;
      left: 30px;
      z-index: 4;
    }
    
    .position3 {
      top: 60px;
      left: 60px;
      z-index: 2;
    }
    
    .position4 {
      top: 150px;
      left: 0;
      z-index: auto;
    }
    
    .position5 {
      top: 180px;
      left: 30px;
      z-index: auto;
    }
    
    .position6 {
      top: 210px;
      left: 60px;
      z-index: auto;
    }
    

For a positioned box (that is, one with any `position` other than `static`), the `z-index` property specifies:

1.  The stack level of the box in the current [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    .
2.  Whether the box establishes a local stacking context.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#syntax)

-----------------------------------------------------------------------------------------------

css

    /* Keyword value */
    z-index: auto;
    
    /* <integer> values */
    z-index: 0;
    z-index: 3;
    z-index: 289;
    z-index: -1; /* Negative values to lower the priority */
    
    /* Global values */
    z-index: inherit;
    z-index: initial;
    z-index: revert;
    z-index: revert-layer;
    z-index: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#values)

This property is specified as one of the following values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#auto)

The box does not establish a new local stacking context. The stack level of the generated box in the current stacking context is `0`.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#integer)

This [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 is the stack level of the generated box in the current stacking context. The box also establishes a local stacking context. This means that the z-indexes of descendants are not compared to the z-indexes of elements outside this element.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#formal_definition)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | positioned elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | an [integer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#interpolation "Values of the <integer> CSS data type are interpolated via integer discrete steps. The calculation is done as if they were real, floating-point numbers and the discrete value is obtained using the floor function.") |
| Creates [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context) | yes |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#formal_syntax)

-------------------------------------------------------------------------------------------------------------

z-index =   
  auto       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <integer>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inherit      
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#examples)

---------------------------------------------------------------------------------------------------

### [Visually layering elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#visually_layering_elements)

#### HTML

html

    <div class="wrapper">
      <div class="dashed-box">Dashed box</div>
      <div class="gold-box">Gold box</div>
      <div class="green-box">Green box</div>
    </div>
    

#### CSS

css

    .wrapper {
      position: relative;
    }
    
    .dashed-box {
      position: relative;
      z-index: 1;
      border: dashed;
      height: 8em;
      margin-bottom: 1em;
      margin-top: 2em;
    }
    .gold-box {
      position: absolute;
      z-index: 3; /* put .gold-box above .green-box and .dashed-box */
      background: gold;
      width: 80%;
      left: 60px;
      top: 3em;
    }
    .green-box {
      position: absolute;
      z-index: 2; /* put .green-box above .dashed-box */
      background: lightgreen;
      width: 20%;
      left: 65%;
      top: -25px;
      height: 7em;
      opacity: 0.9;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Cascading Style Sheets Level 2  <br>\# z-index](https://drafts.csswg.org/css2/#z-index) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index#see_also)

---------------------------------------------------------------------------------------------------

*   CSS [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
     property
*   [Understanding CSS z-indexes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Understanding_z-index)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/z-index/index.md?plain=1 "Folder: en-us/web/css/reference/properties/z-index (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fz-index&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fz-index%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fz-index%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fz-index%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")