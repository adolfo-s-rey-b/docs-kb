*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#mdn-search)
    

`border-inline` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-inline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the individual logical inline border property values in a single place in the style sheet.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#try_it)

-----------------------------------------------------------------------------------------------------

    border-inline: solid;
    writing-mode: horizontal-tb;
    

    border-inline: dashed red;
    writing-mode: vertical-rl;
    

    border-inline: 1rem solid;
    writing-mode: horizontal-tb;
    direction: rtl;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with a border around it.
      </div>
    </section>
    

    #example-element {
      background-color: #eeeeee;
      color: darkmagenta;
      padding: 0.75em;
      width: 80%;
      height: 100px;
      unicode-bidi: bidi-override;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`border-inline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color)
    
*   [`border-inline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-style)
    
*   [`border-inline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-width)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#syntax)

-----------------------------------------------------------------------------------------------------

css

    border-inline: 1px;
    border-inline: 2px dotted;
    border-inline: medium dashed blue;
    
    /* Global values */
    border-inline: inherit;
    border-inline: initial;
    border-inline: revert;
    border-inline: revert-layer;
    border-inline: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#values)

The `border-inline` is specified with one or more of the following, in any order:

[`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)

The width of the border. See [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
.

[`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)

The line style of the border. See [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
.

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The color of the border.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#description)

---------------------------------------------------------------------------------------------------------------

The physical borders to which `border-inline` maps depends on the element's writing mode, directionality, and text orientation. It corresponds to the [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
 and [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
 or [`border-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right)
, and [`border-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left)
 properties, depending on the values defined for [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
.

The borders in the other dimension can be set with [`border-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block)
, which sets [`border-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
, and [`border-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`border-inline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-width)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-inline-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-width)<br>        : `medium`<br>    *   [`border-inline-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width)<br>        : `medium`<br>*   [`border-inline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-style)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-inline-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-style)<br>        : `none`<br>    *   [`border-inline-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-style)<br>        : `none`<br>*   [`border-inline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)<br>        : `currentcolor`<br>    *   [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)<br>        : `currentcolor` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`border-inline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-width)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-inline-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-width)<br>        : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>        , snapped as a line width<br>    *   [`border-inline-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width)<br>        : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>        , snapped as a line width<br>*   [`border-inline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-style)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-inline-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-style)<br>        : as specified<br>    *   [`border-inline-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-style)<br>        : as specified<br>*   [`border-inline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)<br>        : computed color<br>    *   [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)<br>        : computed color |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`border-inline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-width)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-inline-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-width)<br>        : by computed value type<br>    *   [`border-inline-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width)<br>        : by computed value type<br>*   [`border-inline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-style)<br>    : discrete<br>*   [`border-inline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)<br>        : by computed value type<br>    *   [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)<br>        : by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

border-inline =   
  [<'border-block-start'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
    
  
[<border-block-start>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
 =   
  <line-width>  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <line-style>  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
         
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#examples)

---------------------------------------------------------------------------------------------------------

### [Border with vertical text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#border_with_vertical_text)

#### HTML

html

    <div>
      <p class="exampleText">Example text</p>
    </div>
    

#### CSS

css

    div {
      background-color: yellow;
      width: 120px;
      height: 120px;
    }
    
    .exampleText {
      writing-mode: vertical-rl;
      border-inline: 5px dashed blue;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Logical Properties and Values Module Level 1  <br>\# propdef-border-inline](https://drafts.csswg.org/css-logical/#propdef-border-inline) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline#see_also)

---------------------------------------------------------------------------------------------------------

*   [CSS Logical Properties and Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    
*   This property maps to one of the physical border properties: [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
    , [`border-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right)
    , [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
    , or [`border-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left)
    .
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    , [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-inline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-inline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-inline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-inline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-inline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-inline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")