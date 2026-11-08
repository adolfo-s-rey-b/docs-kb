*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#mdn-search)
    

`-webkit-border-before` CSS property
====================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`-webkit-border-before`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the individual logical block start border property values in a single place in the style sheet.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   `-webkit-border-before-color`
*   `-webkit-border-before-style`
*   `-webkit-border-before-width`

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Border values */
    -webkit-border-before: 1px;
    -webkit-border-before: 2px dotted;
    -webkit-border-before: medium dashed blue;
    
    /* Global values */
    -webkit-border-before: inherit;
    -webkit-border-before: initial;
    -webkit-border-before: revert;
    -webkit-border-before: revert-layer;
    -webkit-border-before: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#values)

This property is specified as a space-separated list of one to three of the following values:

[`<'border-width'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#border-width)

See [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)

[`<'border-style'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#border-style)

See [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)

[`<'color'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#color)

See [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#description)

-----------------------------------------------------------------------------------------------------------------------

The `-webkit-border-before` property maps to a physical border depending on the element's writing mode, directionality, and text orientation. It corresponds to the [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
, [`border-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right)
, [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
, or [`border-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left)
 property depending on the values defined for [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
.

It relates to `-webkit-border-after`, `-webkit-border-start`, and `-webkit-border-end`, which define the other borders of the element.

The standard-track equivalent of this property is [`border-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`border-block-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-width)<br>    : `medium`<br>*   [`border-block-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-style)<br>    : `none`<br>*   [`border-block-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-color)<br>    : `currentcolor` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`border-block-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-width)<br>    : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>    , snapped as a line width<br>*   [`border-block-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-style)<br>    : as specified<br>*   [`border-block-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-color)<br>    : computed color |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`border-block-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-width)<br>    : by computed value type<br>*   [`border-block-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-style)<br>    : discrete<br>*   [`border-block-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-color)<br>    : by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

\-webkit-border-before =   
  [<'border-width'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'border-style'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
             
  
[<border-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
 =   
  [<'border-top-width'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<border-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 =   
  [<'border-top-style'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<border-top-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)
 =   
  <line-width>    
  
[<border-top-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
 =   
  <line-style>    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#examples)

-----------------------------------------------------------------------------------------------------------------

### [Applying a border with vertical text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#applying_a_border_with_vertical_text)

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
      -webkit-border-before: 5px dashed blue;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#specifications)

-----------------------------------------------------------------------------------------------------------------------------

Not part of any standard, but it relates to the standards-track [`border-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
 property.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`border-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
    
*   The mapped physical properties: [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
    , [`border-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right)
    , [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
    , and [`border-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left)
    
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    , [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/-webkit-border-before/index.md?plain=1 "Folder: en-us/web/css/reference/properties/-webkit-border-before (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-border-before&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-border-before%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-border-before%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-border-before%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6354422058e438a2599e4eab71eaec8eb40850fa%0A*+Document+last+modified%3A+2026-09-14T09%3A57%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")