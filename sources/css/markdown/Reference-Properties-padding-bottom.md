*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#mdn-search)
    

`padding-bottom` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`padding-bottom`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the height of the [padding area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#padding_area)
 on the bottom of an element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#try_it)

------------------------------------------------------------------------------------------------------

    padding-bottom: 1em;
    

    padding-bottom: 10%;
    

    padding-bottom: 20px;
    

    padding-bottom: 1ch;
    

    padding-bottom: 0;
    

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

![The effect of the CSS padding-bottom property on the element box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom/padding-bottom.svg)

**Note:** The [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 property can be used to set paddings on all four sides of an element with a single declaration.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#syntax)

------------------------------------------------------------------------------------------------------

css

    /* <length> values */
    padding-bottom: 0.5em;
    padding-bottom: 0;
    padding-bottom: 2cm;
    
    /* <percentage> value */
    padding-bottom: 10%;
    
    /* Global values */
    padding-bottom: inherit;
    padding-bottom: initial;
    padding-bottom: revert;
    padding-bottom: revert-layer;
    padding-bottom: unset;
    

The `padding-bottom` property is specified as a single value chosen from the list below. Unlike margins, negative values are not allowed for padding.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The size of the padding as a fixed value. Must be non-negative.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

The size of the padding as a percentage, relative to the inline size (_width_ in a horizontal language, defined by [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
) of the [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
. Must be non-negative.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements, except `table-row-group`, `table-header-group`, `table-footer-group`, `table-row`, `table-column-group` and `table-column`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the width of the containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

padding-bottom =   
  <length-percentage \[0,∞\]>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#examples)

----------------------------------------------------------------------------------------------------------

### [Setting padding bottom with pixels and percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#setting_padding_bottom_with_pixels_and_percentages)

css

    .content {
      padding-bottom: 5%;
    }
    .side-box {
      padding-bottom: 10px;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Model Module Level 3  <br>\# padding-physical](https://drafts.csswg.org/css-box/#padding-physical) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom#see_also)

----------------------------------------------------------------------------------------------------------

*   [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
    , [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)
    , and [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
    
*   [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
     shorthand
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

This page was last modified on Jul 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/padding-bottom/index.md?plain=1 "Folder: en-us/web/css/reference/properties/padding-bottom (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpadding-bottom&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpadding-bottom%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpadding-bottom%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpadding-bottom%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c62b082755017d0773ecaaee7e74efd5e066d0b%0A*+Document+last+modified%3A+2026-07-17T12%3A50%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")