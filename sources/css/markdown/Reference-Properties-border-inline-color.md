*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#mdn-search)
    

`border-inline-color` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-inline-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the color of the logical inline borders of an element, which maps to a physical border color depending on the element's writing mode, directionality, and text orientation. It corresponds to the [`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
 and [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
, or [`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color)
 and [`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color)
 property depending on the values defined for [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
.

The border color in the other dimension can be set with [`border-block-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-color)
 which sets [`border-block-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-color)
, and [`border-block-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-color)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#try_it)

-----------------------------------------------------------------------------------------------------------

    border-inline-color: red;
    writing-mode: horizontal-tb;
    

    border-inline-color: #32a1ce;
    writing-mode: vertical-rl;
    

    border-inline-color: rgb(170 50 220 / 0.6);
    writing-mode: horizontal-tb;
    direction: rtl;
    

    <section class="default-example" id="default-example">
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
      unicode-bidi: bidi-override;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#syntax)

-----------------------------------------------------------------------------------------------------------

css

    border-inline-color: yellow;
    border-inline-color: #f5f6f7;
    
    /* Global values */
    border-inline-color: inherit;
    border-inline-color: initial;
    border-inline-color: revert;
    border-inline-color: revert-layer;
    border-inline-color: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#values)

This property is specified as one `<color>` value:

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The color of the border.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)<br>    : `currentcolor`<br>*   [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)<br>    : `currentcolor` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)<br>    : computed color<br>*   [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)<br>    : computed color |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)<br>    : by computed value type<br>*   [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)<br>    : by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

border-inline-color =   
  [<'border-top-color'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<border-top-color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
 =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-1D>    
  
<image-1D> =   
  <stripes()>    
  
<stripes()> =   
  stripes( <color-stripe>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<color-stripe> =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
                            [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<flex>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#examples)

---------------------------------------------------------------------------------------------------------------

### [Border color with vertical text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#border_color_with_vertical_text)

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
      writing-mode: vertical-lr;
      border: 10px solid blue;
      border-inline-color: red;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Logical Properties and Values Module Level 1  <br>\# propdef-border-inline-color](https://drafts.csswg.org/css-logical/#propdef-border-inline-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color#see_also)

---------------------------------------------------------------------------------------------------------------

*   [CSS Logical Properties and Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    
*   This property maps to the physical border properties: [`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
    , [`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color)
    , [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
    , or [`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color)
    .
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    , [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-inline-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-inline-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-inline-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-inline-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-inline-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-inline-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")