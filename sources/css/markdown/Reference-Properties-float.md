*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#mdn-search)
    

`float` CSS property
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`float`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property places an element on the left or right side of its container, allowing text and inline elements to wrap around it. The element is removed from the normal flow of the page, though still remaining a part of the flow (in contrast to [absolute positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#absolute_positioning)
).

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#try_it)

---------------------------------------------------------------------------------------------

    float: none;
    

    float: left;
    

    float: right;
    

    float: inline-start;
    

    float: inline-end;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element">Float me</div>
        As much mud in the streets as if the waters had but newly retired from the
        face of the earth, and it would not be wonderful to meet a Megalosaurus,
        forty feet long or so, waddling like an elephantine lizard up Holborn Hill.
      </div>
    </section>
    

    .example-container {
      border: 1px solid #c5c5c5;
      padding: 0.75em;
      text-align: left;
      width: 80%;
      line-height: normal;
    }
    
    #example-element {
      border: solid 10px #efac09;
      background-color: #040d46;
      color: white;
      padding: 1em;
      width: 40%;
    }
    

A _floating element_ is one where the computed value of `float` is not `none`.

As `float` implies the use of the block layout, it modifies the computed value of the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 values, in some cases:

| Specified value | Computed value |
| --- | --- |
| `inline` | `block` |
| `inline-block` | `block` |
| `inline-table` | `table` |
| `table-row` | `block` |
| `table-row-group` | `block` |
| `table-column` | `block` |
| `table-column-group` | `block` |
| `table-cell` | `block` |
| `table-caption` | `block` |
| `table-header-group` | `block` |
| `table-footer-group` | `block` |
| `inline-flex` | `flex` |
| `inline-grid` | `grid` |
| _other_ | _unchanged_ |

**Note:** When accessing a CSS property in JavaScript through the [`HTMLElement.style`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)
 object, single-word property names are used as is. Although `float` is a reserved keyword in JavaScript, the CSS `float` property is accessed as `float` in modern browsers. In older browsers, you must use `cssFloat` to access the `float` property. (This is similar to how the "class" attribute is accessed as "className" and the "for" attribute of a `<label>` element is accessed as "htmlFor".)

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#syntax)

---------------------------------------------------------------------------------------------

css

    /* Keyword values */
    float: left;
    float: right;
    float: none;
    float: inline-start;
    float: inline-end;
    
    /* Global values */
    float: inherit;
    float: initial;
    float: revert;
    float: revert-layer;
    float: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#values)

This property is specified as one of the following keyword values:

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#left)

The element must float on the left side of its containing block.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#right)

The element must float on the right side of its containing block.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#none)

The element must not float.

[`inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#inline-start)

The element must float on the start side of its containing block. That is the left side with `ltr` scripts, and the right side with `rtl` scripts.

[`inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#inline-end)

The element must float on the end side of its containing block. That is the right side with `ltr` scripts, and the left side with `rtl` scripts.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#formal_definition)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements, but has no effect if the value of [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)<br> is `none`. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#formal_syntax)

-----------------------------------------------------------------------------------------------------------

float =   
  block-start      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block-end        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-start     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-end       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  snap-block       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <snap-block()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  snap-inline      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <snap-inline()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  top              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  footnote           
  
<snap-block()> =   
  snap-block( [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 near [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<snap-inline()> =   
  snap-inline( [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 near [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#examples)

-------------------------------------------------------------------------------------------------

### [How floated elements are positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#how_floated_elements_are_positioned)

As mentioned above, when an element is floated, it is taken out of the normal flow of the document (though still remaining part of it). It is shifted to the left, or right, until it touches the edge of its containing box, _or another floated element_.

In this example, there are three colored squares. Two are floated left, and one is floated right. Note that the second "left" square is placed to the right of the first. Additional squares would continue to stack to the right, until they filled the containing box, after which they would wrap to the next line.

A floated element is at least as tall as its tallest nested floated children. We gave the parent `width: 100%` and floated it to ensure it is tall enough to encompass its floated children, and to make sure it takes up the width of the parent so we don't have to clear its adjacent sibling.

#### HTML

html

    <section>
      <div class="left">1</div>
      <div class="left">2</div>
      <div class="right">3</div>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tristique
        sapien ac erat tincidunt, sit amet dignissim lectus vulputate. Donec id
        iaculis velit. Aliquam vel malesuada erat. Praesent non magna ac massa
        aliquet tincidunt vel in massa. Phasellus feugiat est vel leo finibus
        congue.
      </p>
    </section>
    

#### CSS

css

    section {
      box-sizing: border-box;
      border: 1px solid blue;
      width: 100%;
      float: left;
    }
    
    div {
      margin: 5px;
      width: 50px;
      height: 150px;
    }
    
    .left {
      float: left;
      background: pink;
    }
    
    .right {
      float: right;
      background: cyan;
    }
    

#### Result

### [Clearing floats](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#clearing_floats)

Sometimes you may want to force an item to move below any floated elements. For instance, you may want paragraphs to remain adjacent to floats, but force headings to be on their own line. See [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)
 for examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Cascading Style Sheets Level 2  <br>\# propdef-float](https://drafts.csswg.org/css2/#propdef-float) |
| [CSS Logical Properties and Values Module Level 1  <br>\# float-clear](https://drafts.csswg.org/css-logical/#float-clear) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float#see_also)

-------------------------------------------------------------------------------------------------

*   [Block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
    
*   Use [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)
     to force an item to move below a floated element.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/float/index.md?plain=1 "Folder: en-us/web/css/reference/properties/float (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffloat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffloat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffloat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffloat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")