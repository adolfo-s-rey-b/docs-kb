*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#mdn-search)
    

`border-start-start-radius` CSS property
========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-start-start-radius`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines a logical border radius on an element, which maps to a physical border radius that depends on the element's [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
. This is useful when building styles to work regardless of the [text orientation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
 and [writing mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
.

This property affects the corner between the block-start and the inline-start sides of the element. For instance, in a `horizontal-tb` writing mode with `ltr` direction, it corresponds to the [`border-top-left-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-left-radius)
 property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#try_it)

-----------------------------------------------------------------------------------------------------------------

    border-start-start-radius: 80px 80px;
    

    border-start-start-radius: 250px 100px;
    direction: rtl;
    

    border-start-start-radius: 50%;
    writing-mode: vertical-lr;
    

    border-start-start-radius: 50%;
    writing-mode: vertical-rl;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with a top left rounded corner.
      </div>
    </section>
    

    #example-element {
      width: 80%;
      height: 80%;
      display: flex;
      justify-content: center;
      flex-direction: column;
      background-color: #5b6dcd;
      color: white;
      padding: 10px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#syntax)

-----------------------------------------------------------------------------------------------------------------

css

    /* <length> values */
    /* With one value the corner will be a circle */
    border-start-start-radius: 10px;
    border-start-start-radius: 1em;
    
    /* With two values the corner will be an ellipse */
    border-start-start-radius: 1em 2em;
    
    /* Global values */
    border-start-start-radius: inherit;
    border-start-start-radius: initial;
    border-start-start-radius: revert;
    border-start-start-radius: revert-layer;
    border-start-start-radius: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#values)

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#length-percentage)

Denotes the size of the circle radius or the semi-major and semi-minor axes of the ellipse. As absolute length it can be expressed in any unit allowed by the CSS [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 data type. Percentages for the horizontal axis refer to the width of the box, percentages for the vertical axis refer to the height of the box. Negative values are invalid.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements; but User Agents are not required to apply to `table` and `inline-table` elements when [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)<br> is `collapse`. The behavior on internal table elements is undefined for the moment.. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the corresponding dimension of the border box |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | two absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>s or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)<br>s |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

border-start-start-radius =   
  <border-radius>    
  
<border-radius> =   
  <slash-separated-border-radius-syntax>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <legacy-border-radius-syntax>             
  
<slash-separated-border-radius-syntax> =   
  <length-percentage \[0,∞\]> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <length-percentage \[0,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<legacy-border-radius-syntax> =   
  <length-percentage \[0,∞\]>[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#examples)

---------------------------------------------------------------------------------------------------------------------

### [Border radius with vertical text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#border_radius_with_vertical_text)

#### HTML

html

    <div>
      <p class="exampleText">Example</p>
    </div>
    

#### CSS

css

    div {
      background-color: rebeccapurple;
      width: 120px;
      height: 120px;
      border-start-start-radius: 10px;
    }
    
    .exampleText {
      writing-mode: vertical-rl;
      padding: 10px;
      background-color: white;
      border-start-start-radius: 10px;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Logical Properties and Values Module Level 1  <br>\# border-radius-properties](https://drafts.csswg.org/css-logical/#border-radius-properties) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [CSS Logical Properties and Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    
*   The mapped physical property: [`border-top-left-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-left-radius)
    
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    , [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-start-start-radius/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-start-start-radius (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-start-start-radius&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-start-start-radius%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-start-start-radius%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-start-start-radius%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")