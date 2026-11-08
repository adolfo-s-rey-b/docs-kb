*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#mdn-search)
    

`margin` CSS property
=====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`margin`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 shorthand property sets the [margin area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#margin_area)
 on all four sides of an element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#try_it)

----------------------------------------------------------------------------------------------

    margin: 1em;
    

    margin: 5% 0;
    

    margin: 10px 50px 20px;
    

    margin: 10px 50px 20px 0;
    

    margin: 0;
    

    <section id="default-example">
      <div id="container">
        <div class="row"></div>
        <div class="row transition-all" id="example-element"></div>
        <div class="row"></div>
      </div>
    </section>
    

    #container {
      width: 300px;
      height: 200px;
      display: flex;
      align-content: flex-start;
      flex-direction: column;
      justify-content: flex-start;
    }
    
    .row {
      height: 33.33%;
      display: inline-block;
      border: solid #ce7777 10px;
      background-color: #2b3a55;
      flex-shrink: 0;
    }
    
    #example-element {
      border: solid 10px #ffbf00;
      background-color: #2b3a55;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#constituent_properties)

------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
    
*   [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
    
*   [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
    
*   [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#syntax)

----------------------------------------------------------------------------------------------

The `margin` property may be specified using one, two, three, or four values. Each value is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or the keyword `auto`. Negative values draw the element closer to its neighbors than it would be by default.

*   When **one** value is specified, it applies the same margin to **all four sides**.
*   When **two** values are specified, the first margin applies to the **top and bottom**, the second to the **left and right**.
*   When **three** values are specified, the first margin applies to the **top**, the second to the **right and left**, the third to the **bottom**.
*   When **four** values are specified, the margins apply to the **top**, **right**, **bottom**, and **left** in that order (clockwise).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The size of the margin as a fixed value.

*   For _anchor-positioned elements_, the [`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
     function resolves to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     value relative to the associated _anchor element_'s width or height (see [Setting element margin based on anchor size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#setting_element_margin_based_on_anchor_size)
    ).

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

The size of the margin as a percentage, relative to the inline size (_width_ in a horizontal language, defined by [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
) of the [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#auto)

The browser selects a suitable margin to use. For example, in certain cases this value can be used to center an element.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#description)

--------------------------------------------------------------------------------------------------------

This property can be used to set a margin on all four sides of an element. Margins create extra space _around_ an element, unlike [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, which creates extra space _within_ an element.

The top and bottom margins have no effect on _non-[replaced](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
_ inline elements, such as [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 or [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
.

### [Horizontal centering](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#horizontal_centering)

You can horizontally center an element within its parent by setting `margin: 0 auto;`.

A more common method to center an element horizontally is by setting `display: flex;` and [`justify-content: center;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 on a container, which [centers its flex item](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
 children.

### [Margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#margin_collapsing)

Elements' top and bottom margins are sometimes collapsed into a single margin that is equal to the larger of the two margins. See [Mastering margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
 for more information.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#formal_definition)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)<br>    : `0`<br>*   [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)<br>    : `0`<br>*   [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)<br>    : `0`<br>*   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)<br>    : `0` |
| Applies to | all elements, except elements with table [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)<br> types other than `table-caption`, `table` and `inline-table`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the width of the containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)<br>    : the percentage as specified or the absolute length<br>*   [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)<br>    : the percentage as specified or the absolute length<br>*   [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)<br>    : the percentage as specified or the absolute length<br>*   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)<br>    : the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#formal_syntax)

------------------------------------------------------------------------------------------------------------

margin =   
  [<'margin-top'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<margin-top>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
 =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-size()>        
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<anchor-size()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  anchor-size( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <anchor-name> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <anchor-size> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<anchor-name> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
  
[<anchor-size>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  width        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  height       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-inline    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#examples)

--------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#basic_example)

#### HTML

#### CSS

### [More examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#more_examples)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Model Module Level 3  <br>\# margin](https://drafts.csswg.org/css-box/#margin) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin#see_also)

--------------------------------------------------------------------------------------------------

*   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
    , [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
    , [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
    , and [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
    
*   [`margin-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start)
    , [`margin-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-end)
    , [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
    , and [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
    
*   [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
     and [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
     shorthands
*   [Mastering margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
    
*   [Introduction to the CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
     guide
*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/margin/index.md?plain=1 "Folder: en-us/web/css/reference/properties/margin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")