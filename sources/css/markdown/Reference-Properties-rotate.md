*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#mdn-search)
    

`rotate` CSS property
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since August 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`rotate`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property allows you to specify rotation transforms individually and independently of the [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 property. This maps better to typical user interface usage, and saves having to remember the exact order of transform functions to specify in the `transform` property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#try_it)

----------------------------------------------------------------------------------------------

    rotate: none;
    

    rotate: -45deg;
    

    rotate: z 45deg;
    

    rotate: x 45deg;
    

    rotate: y 45deg;
    

    rotate: 3 0.5 2 45deg;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        <div class="face front">1</div>
        <div class="face back">2</div>
        <div class="face right">3</div>
        <div class="face left">4</div>
        <div class="face top">5</div>
        <div class="face bottom">6</div>
      </div>
    </section>
    

    #default-example {
      background: linear-gradient(skyblue, khaki);
      perspective: 550px;
    }
    
    #example-element {
      width: 100px;
      height: 100px;
      transform-style: preserve-3d;
    }
    
    .face {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 100%;
      position: absolute;
      backface-visibility: inherit;
      font-size: 60px;
      color: white;
    }
    
    .front {
      background: rgb(90 90 90 / 0.7);
      transform: translateZ(50px);
    }
    
    .back {
      background: rgb(0 210 0 / 0.7);
      transform: rotateY(180deg) translateZ(50px);
    }
    
    .right {
      background: rgb(210 0 0 / 0.7);
      transform: rotateY(90deg) translateZ(50px);
    }
    
    .left {
      background: rgb(0 0 210 / 0.7);
      transform: rotateY(-90deg) translateZ(50px);
    }
    
    .top {
      background: rgb(210 210 0 / 0.7);
      transform: rotateX(90deg) translateZ(50px);
    }
    
    .bottom {
      background: rgb(210 0 210 / 0.7);
      transform: rotateX(-90deg) translateZ(50px);
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#syntax)

----------------------------------------------------------------------------------------------

css

    /* Keyword value */
    rotate: none;
    
    /* Angle value */
    rotate: 90deg;
    rotate: 0.25turn;
    rotate: 1.57rad;
    
    /* x, y, or z axis name plus angle */
    rotate: x 90deg;
    rotate: y 0.25turn;
    rotate: z 1.57rad;
    
    /* Vector plus angle value */
    rotate: 1 1 1 90deg;
    
    /* Global values */
    rotate: inherit;
    rotate: initial;
    rotate: revert;
    rotate: revert-layer;
    rotate: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#values)

[angle value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#angle_value)

An [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 specifying the angle to rotate the affected element through, around the Z axis. Equivalent to a `rotate()` (2D rotation) function.

[x, y, or z axis name plus angle value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#x_y_or_z_axis_name_plus_angle_value)

The name of the axis you want to rotate the affected element around (`x`, `y`, or `z`), plus an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 specifying the angle to rotate the element through. Equivalent to a `rotateX()`/`rotateY()`/`rotateZ()` (3D rotation) function.

[vector plus angle value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#vector_plus_angle_value)

Three [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
s representing an origin-centered vector that defines a line around which you want to rotate the element, plus an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 specifying the angle to rotate the element through. Equivalent to a `rotate3d()` (3D rotation) function.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#none)

Specifies that no rotation should be applied.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#formal_definition)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a transform |
| Creates [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context) | yes |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#formal_syntax)

------------------------------------------------------------------------------------------------------------

rotate =   
  none                                    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
                                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 x [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 z [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
[{3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#examples)

--------------------------------------------------------------------------------------------------

### [Rotating an element on hover](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#rotating_an_element_on_hover)

The following example shows how to use the `rotate` property to rotate an element along various axes on hover. The first box rotates 90 degrees on the Z axis hover, the second rotates 180 degrees on the Y axis on hover, and the third rotates 360 degrees on hover around a vector defined by coordinates.

#### HTML

html

    <div class="box" id="box1">rotate Z</div>
    <div class="box" id="box2">rotate Y</div>
    <div class="box" id="box3">vector & angle</div>
    

#### CSS

css

    .box {
      display: inline-block;
      margin: 1em;
      min-width: 6.5em;
      line-height: 6.5em;
      text-align: center;
      transition: 1s ease-in-out;
      border: 0.25em dotted;
    }
    
    #box1:hover {
      rotate: 90deg;
    }
    
    #box2:hover {
      rotate: y 180deg;
    }
    
    #box3:hover {
      rotate: 1 2 1 360deg;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# propdef-rotate](https://drafts.csswg.org/css-transforms-2/#propdef-rotate) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate#see_also)

--------------------------------------------------------------------------------------------------

*   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
    
*   [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
    
*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    

Note: `skew` is not an independent `transform` value

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/rotate/index.md?plain=1 "Folder: en-us/web/css/reference/properties/rotate (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frotate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frotate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frotate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frotate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")