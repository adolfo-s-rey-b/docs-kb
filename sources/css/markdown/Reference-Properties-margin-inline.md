*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#mdn-search)
    

`margin-inline` CSS property
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`margin-inline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property defines both the logical inline start and end margins of an element, which maps to physical margins depending on the element's writing mode, directionality, and text orientation.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#try_it)

-----------------------------------------------------------------------------------------------------

    margin-inline: 5% 10%;
    writing-mode: horizontal-tb;
    

    margin-inline: 10px 40px;
    writing-mode: vertical-rl;
    

    margin-inline: 5% 10%;
    writing-mode: horizontal-tb;
    direction: rtl;
    

    <section id="default-example">
      <div id="container">
        <div class="col">One</div>
        <div class="col transition-all" id="example-element">Two</div>
        <div class="col">Three</div>
      </div>
    </section>
    

    #container {
      width: 300px;
      height: 200px;
      display: flex;
      align-content: flex-start;
      justify-content: flex-start;
    }
    
    .col {
      width: 33.33%;
      border: solid #ce7777 10px;
      background-color: #2b3a55;
      color: white;
      flex-shrink: 0;
    }
    
    #example-element {
      border: solid 10px #ffbf00;
      background-color: #2b3a55;
      unicode-bidi: bidi-override;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
    
*   [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* <length> values */
    margin-inline: 10px 20px; /* An absolute length */
    margin-inline: 1em 2em; /* relative to the text size */
    margin-inline: 5% 2%; /* relative to the nearest block container's width */
    margin-inline: 10px; /* sets both start and end values */
    margin-inline: anchor-size(width);
    margin-inline: calc(anchor-size(self-block) / 5) auto;
    
    /* Keyword value */
    margin-inline: auto;
    
    /* Global values */
    margin-inline: inherit;
    margin-inline: initial;
    margin-inline: revert;
    margin-inline: revert-layer;
    margin-inline: unset;
    

This property corresponds to the [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
 and [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
, or the [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
 and [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
 properties, depending on the values defined for [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
.

The `margin-inline` property may be specified using one or two values.

*   When **one** value is specified, it applies the same margin to **both start and end**.
*   When **two** values are specified, the first margin applies to the **start**, the second to the **end**.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#values)

The `margin-inline` property takes the same values as the [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top#values)
 property.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)<br>    : `0`<br>*   [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)<br>    : `0` |
| Applies to | same as [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | depends on layout model |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)<br>    : if specified as a length, the corresponding absolute length; if specified as a percentage, the specified value; otherwise, `auto`<br>*   [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)<br>    : if specified as a length, the corresponding absolute length; if specified as a percentage, the specified value; otherwise, `auto` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

margin-inline =   
  [<'margin-top'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#examples)

---------------------------------------------------------------------------------------------------------

### [Setting inline start and end margins](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#setting_inline_start_and_end_margins)

#### CSS

css

    div {
      background-color: yellow;
      width: 120px;
      height: auto;
      border: 1px solid green;
    }
    
    p {
      margin: 0;
      margin-inline: 20px 40px;
      background-color: tan;
    }
    
    .verticalExample {
      writing-mode: vertical-rl;
    }
    

#### HTML

html

    <div>
      <p>Example text</p>
    </div>
    <div class="verticalExample">
      <p>Example text</p>
    </div>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Logical Properties and Values Module Level 1  <br>\# propdef-margin-inline](https://drafts.csswg.org/css-logical/#propdef-margin-inline) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline#see_also)

---------------------------------------------------------------------------------------------------------

*   [CSS Logical Properties and Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    
*   The mapped physical properties: [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
    , [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
    , [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
    , and [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
    
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    , [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/margin-inline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/margin-inline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin-inline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin-inline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin-inline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin-inline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")