*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#mdn-search)
    

`border-top-right-radius` CSS property
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-top-right-radius`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property rounds the top-right corner of an element by specifying the radius (or the radius of the semi-major and semi-minor axes) of the ellipse defining the curvature of the corner.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#try_it)

---------------------------------------------------------------------------------------------------------------

    border-top-right-radius: 80px 80px;
    

    border-top-right-radius: 250px 100px;
    

    border-top-right-radius: 50%;
    

    border-top-right-radius: 50%;
    border: black 10px double;
    background-clip: content-box;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with a top right rounded corner.
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#syntax)

---------------------------------------------------------------------------------------------------------------

css

    /* the corner is a circle */
    /* border-top-right-radius: radius */
    border-top-right-radius: 3px;
    
    /* the corner is an ellipse */
    /* border-top-right-radius: horizontal vertical */
    border-top-right-radius: 0.5em 1em;
    
    border-top-right-radius: inherit;
    
    /* Global values */
    border-top-right-radius: inherit;
    border-top-right-radius: initial;
    border-top-right-radius: revert;
    border-top-right-radius: revert-layer;
    border-top-right-radius: unset;
    

With one value:

*   the value is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
     denoting the radius of the circle to use for the border in that corner.

With two values:

*   the first value is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
     denoting the horizontal semi-major axis of the ellipse to use for the border in that corner.
*   the second value is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
     denoting the vertical semi-major axis of the ellipse to use for the border in that corner.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#values)

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#length-percentage)

Denotes the size of the circle radius or the semi-major and semi-minor axes of the ellipse. As absolute length it can be expressed in any unit allowed by the CSS [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 data type. Percentages for the horizontal axis refer to the width of the box, percentages for the vertical axis refer to the height of the box. Negative values are invalid.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#description)

-------------------------------------------------------------------------------------------------------------------------

The rounding can be a circle or an ellipse, or if one of the values is `0` no rounding is done and the corner is square.

![border-top-right-radius.png](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius/border-top-right-radius.png)

A background, being an image or a color, is clipped at the border, even a rounded one; the exact location of the clipping is defined by the value of the [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
 property.

**Note:** If the value of this property is not set in a [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 shorthand property that is applied to the element after the `border-top-right-radius` CSS property, the value of this property is then reset to its initial value by the [shorthand property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements; but User Agents are not required to apply to `table` and `inline-table` elements when [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)<br> is `collapse`. The behavior on internal table elements is undefined for the moment.. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the corresponding dimension of the border box |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | two absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>s or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)<br>s |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

border-top-right-radius =   
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#examples)

-------------------------------------------------------------------------------------------------------------------

### [Arc of a circle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#arc_of_a_circle)

A single `<length>` value produces an arc of a circle.

    <div></div>
    

css

    div {
      border-top-right-radius: 40px;
      background-color: lightgreen;
      border: solid 1px black;
      width: 100px;
      height: 100px;
    }
    

### [Arc of an ellipse](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#arc_of_an_ellipse)

Two different `<length>` values produce an arc of an ellipse.

    <div></div>
    

css

    div {
      border-top-right-radius: 40px 20px;
      background-color: lightgreen;
      border: solid 1px black;
      width: 100px;
      height: 100px;
    }
    

### [Square element with percentage radius](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#square_element_with_percentage_radius)

A square element with a single `<percentage>` value produces an arc of a circle.

    <div></div>
    

css

    div {
      border-top-right-radius: 40%;
      background-color: lightgreen;
      border: solid 1px black;
      width: 100px;
      height: 100px;
    }
    

### [Non-square element with percentage radius](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#non-square_element_with_percentage_radius)

A non-square element with a single `<percentage>` value produces an arc of an ellipse.

    <div></div>
    

css

    div {
      border-top-right-radius: 40%;
      background-color: lightgreen;
      border: solid 1px black;
      width: 200px;
      height: 100px;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# propdef-border-top-right-radius](https://drafts.csswg.org/css-backgrounds/#propdef-border-top-right-radius) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
     shorthand property
*   [`border-bottom-right-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-right-radius)
    , [`border-bottom-left-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-left-radius)
    , and [`border-top-left-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-left-radius)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-top-right-radius/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-top-right-radius (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-top-right-radius&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-top-right-radius%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-top-right-radius%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-top-right-radius%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff78ca75460fbdbc7f17b6e366dad47b9760054b0%0A*+Document+last+modified%3A+2026-08-28T22%3A29%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")