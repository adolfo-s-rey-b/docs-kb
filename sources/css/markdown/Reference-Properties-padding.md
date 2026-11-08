*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#mdn-search)
    

`padding` CSS property
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`padding`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the [padding area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#padding_area)
 on all four sides of an element at once.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#try_it)

-----------------------------------------------------------------------------------------------

    padding: 1em;
    

    padding: 10% 0;
    

    padding: 10px 50px 20px;
    

    padding: 10px 50px 30px 0;
    

    padding: 0;
    

    <section id="default-example">
      <div class="transition-all" id="example-element">
        <div class="box">
          Far out in the uncharted backwaters of the unfashionable end of the
          western spiral arm of the Galaxy lies a small unregarded yellow sun.
        </div>
      </div>
    </section>
    

    #example-element {
      border: 10px solid #ffc129;
      overflow: hidden;
      text-align: left;
    }
    
    .box {
      border: dashed 1px;
    }
    

An element's padding area is the space between its content and its border.

**Note:** Padding creates extra space within an element. In contrast, [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 creates extra space _around_ an element.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
    
*   [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)
    
*   [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)
    
*   [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#syntax)

-----------------------------------------------------------------------------------------------

css

    /* Apply to all four sides */
    padding: 1em;
    
    /* top and bottom | left and right */
    padding: 5% 10%;
    
    /* top | left and right | bottom */
    padding: 1em 2em 2em;
    
    /* top | right | bottom | left */
    padding: 5px 1em 0 2em;
    
    /* Global values */
    padding: inherit;
    padding: initial;
    padding: revert;
    padding: revert-layer;
    padding: unset;
    

The `padding` property may be specified using one, two, three, or four values. Each value is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
. Negative values are invalid.

*   When **one** value is specified, it applies the same padding to **all four sides**.
*   When **two** values are specified, the first padding applies to the **top and bottom**, the second to the **left and right**.
*   When **three** values are specified, the first padding applies to the **top**, the second to the **right and left**, the third to the **bottom**.
*   When **four** values are specified, the paddings apply to the **top**, **right**, **bottom**, and **left** in that order (clockwise).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The size of the padding as a fixed value.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

The size of the padding as a percentage, relative to the inline size (_width_ in a horizontal language, defined by [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
) of the [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#formal_definition)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)<br>    : `0`<br>*   [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)<br>    : `0`<br>*   [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)<br>    : `0`<br>*   [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)<br>    : `0` |
| Applies to | all elements, except `table-row-group`, `table-header-group`, `table-footer-group`, `table-row`, `table-column-group` and `table-column`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the width of the containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)<br>    : the percentage as specified or the absolute length<br>*   [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)<br>    : the percentage as specified or the absolute length<br>*   [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)<br>    : the percentage as specified or the absolute length<br>*   [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)<br>    : the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#formal_syntax)

-------------------------------------------------------------------------------------------------------------

padding =   
  [<'padding-top'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<padding-top>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
 =   
  <length-percentage \[0,∞\]>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#examples)

---------------------------------------------------------------------------------------------------

### [Setting padding with pixels](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#setting_padding_with_pixels)

#### HTML

html

    <h4>This element has moderate padding.</h4>
    <h3>The padding is huge in this element!</h3>
    

#### CSS

css

    h4 {
      background-color: lime;
      padding: 20px 50px;
    }
    
    h3 {
      background-color: cyan;
      padding: 110px 50px 50px 110px;
    }
    

#### Result

### [Setting padding with pixels and percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#setting_padding_with_pixels_and_percentages)

css

    padding: 5%; /* All sides: 5% padding */
    
    padding: 10px; /* All sides: 10px padding */
    
    padding: 10px 20px; /* top and bottom: 10px padding */
    /* left and right: 20px padding */
    
    padding: 10px 3% 20px; /* top:            10px padding */
    /* left and right: 3% padding   */
    /* bottom:         20px padding */
    
    padding: 1em 3px 30px 5px; /* top:    1em padding  */
    /* right:  3px padding  */
    /* bottom: 30px padding */
    /* left:   5px padding  */
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Model Module Level 3  <br>\# padding-shorthand](https://drafts.csswg.org/css-box/#padding-shorthand) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding#see_also)

---------------------------------------------------------------------------------------------------

*   [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
    , [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)
    , [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)
    , and [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
    
*   [`padding-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block-start)
    , [`padding-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block-end)
    , [`padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-start)
    , and [`padding-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-end)
    
*   [`padding-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block)
     and [`padding-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline)
     shorthands
*   [Introduction to the CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
     guide
*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/padding/index.md?plain=1 "Folder: en-us/web/css/reference/properties/padding (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpadding&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpadding%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpadding%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpadding%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")