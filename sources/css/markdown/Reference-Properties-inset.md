*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#mdn-search)
    

`inset` CSS property
====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`inset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property corresponds to the [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
, [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
, [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
, and/or [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 properties. It has the same multi-value syntax of the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 shorthand.

This [inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
, including `inset`, have no effect on non-positioned elements.

While part of the [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
 module, it does not define _logical_ offsets. It defines _physical_ offsets, regardless of the element's writing mode, directionality, and text orientation.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#try_it)

---------------------------------------------------------------------------------------------

    inset: 1em;
    

    inset: 5% 0;
    

    inset: 2em 50px 20px;
    

    inset: 10px 30% 20px 0;
    

    inset: 0;
    

    <section id="default-example">
      <div class="example-container">
        <div id="example-element">I am absolutely positioned.</div>
        <p>
          As much mud in the streets as if the waters had but newly retired from the
          face of the earth, and it would not be wonderful to meet a Megalosaurus,
          forty feet long or so, waddling like an elephantine lizard up Holborn
          Hill.
        </p>
      </div>
    </section>
    

    .example-container {
      border: 0.75em solid #ad1457;
      padding: 0.75em;
      text-align: left;
      position: relative;
      width: 100%;
      min-height: 200px;
    }
    
    #example-element {
      background-color: #07136c;
      border: 6px solid #ffa000;
      color: white;
      position: absolute;
      inset: 0;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#constituent_properties)

-----------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    
*   [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    
*   [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
    
*   [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#syntax)

---------------------------------------------------------------------------------------------

css

    /* <length> values */
    inset: 10px; /* value applied to all edges */
    inset: 4px 8px; /* top/bottom left/right */
    inset: 5px 15px 10px; /* top left/right bottom */
    inset: 2.4em 3em 3em 3em; /* top right bottom left */
    inset: calc(anchor(50%) + 10px) anchor(self-start) auto auto;
    inset: anchor-size(block) calc(anchor(50%) + 10px) auto
      calc(anchor-size(width) / 4);
    
    /* <percentage>s of the width (left/right) or height (top/bottom) of the containing block */
    inset: 10% 5% 5% 5%;
    
    /* Keyword value */
    inset: auto;
    
    /* Global values */
    inset: inherit;
    inset: initial;
    inset: revert;
    inset: revert-layer;
    inset: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#values)

The `inset` property takes the same values as the [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
 property.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#formal_definition)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)<br>    : `auto`<br>*   [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)<br>    : `auto`<br>*   [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)<br>    : `auto`<br>*   [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)<br>    : `auto` |
| Applies to | positioned elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | relative to the containing block's size in the corresponding axis (e.g. width for left or right, height for top or bottom) |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)<br>    : if specified as a length, the corresponding absolute length; if specified as a percentage, the specified value; otherwise, `auto`<br>*   [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)<br>    : if specified as a length, the corresponding absolute length; if specified as a percentage, the specified value; otherwise, `auto`<br>*   [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)<br>    : if specified as a length, the corresponding absolute length; if specified as a percentage, the specified value; otherwise, `auto`<br>*   [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)<br>    : if specified as a length, the corresponding absolute length; if specified as a percentage, the specified value; otherwise, `auto` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#formal_syntax)

-----------------------------------------------------------------------------------------------------------

inset =   
  [<'top'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<top>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
 =   
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor()>           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-size()>        
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<anchor()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
 =   
  anchor( <anchor-name>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  <anchor-side> , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
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
    
  
<anchor-side> =   
  inside        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outside       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  top           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  start         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-start    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-end      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center          
  
[<anchor-size>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  width        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  height       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-inline    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#examples)

-------------------------------------------------------------------------------------------------

### [Setting offsets for an element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#setting_offsets_for_an_element)

#### HTML

html

    <div>
      <span class="exampleText">Example text</span>
    </div>
    

#### CSS

css

    div {
      background-color: yellow;
      width: 150px;
      height: 120px;
      position: relative;
    }
    
    .exampleText {
      writing-mode: sideways-rl;
      position: absolute;
      inset: 20px 40px 30px 10px;
      background-color: #c8c800;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Logical Properties and Values Module Level 1  <br>\# propdef-inset](https://drafts.csswg.org/css-logical/#propdef-inset) |
| [CSS Positioned Layout Module Level 3  <br>\# propdef-inset](https://drafts.csswg.org/css-position/#propdef-inset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset#see_also)

-------------------------------------------------------------------------------------------------

*   [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    , [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    , [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
    , and [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
    
*   [`inset-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block)
     and [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
    
*   [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
    
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module
*   [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/inset/index.md?plain=1 "Folder: en-us/web/css/reference/properties/inset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")