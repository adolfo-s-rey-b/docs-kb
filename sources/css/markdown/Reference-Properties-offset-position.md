*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#mdn-search)
    

`offset-position` CSS property
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2024.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`offset-position`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the initial position of an element along a path. This property is typically used in combination with the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 property to create a motion effect. The value of `offset-position` determines where the element gets placed initially for moving along an offset path if an `offset-path` function such as [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
 does not specify its own starting position.

The `offset-position` property is part of a motion system based on [`offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset)
 constituent properties, including [`offset-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-anchor)
, [`offset-distance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance)
, and `offset-path`. These properties work together to create various motion effects along a path.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    offset-position: normal;
    offset-position: auto;
    offset-position: top;
    offset-position: bottom;
    offset-position: left;
    offset-position: right;
    offset-position: center;
    
    /* <percentage> values */
    offset-position: 25% 75%;
    
    /* <length> values */
    offset-position: 0 0;
    offset-position: 1cm 2cm;
    offset-position: 10ch 8em;
    
    /* Edge offsets values */
    offset-position: bottom 10px right 20px;
    offset-position: right 3em bottom 10px;
    offset-position: bottom 10px right;
    offset-position: top right 10px;
    
    /* Global values */
    offset-position: inherit;
    offset-position: initial;
    offset-position: revert;
    offset-position: revert-layer;
    offset-position: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#normal)

Indicates that the element does not have an offset starting position and places the element at `50% 50%` of the containing block. This is the default value.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#auto)

Indicates that the offset starting position is the top-left corner of the element's box.

[`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)

Specifies the position as an x/y coordinate to place an element relative to its box edges. The position can be defined using one to four values. If two non-keyword values are used, the first value represents the horizontal position and the second represents the vertical position. If only one value is specified, the second value is assumed to be `center`. If three or four values are used, the [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 values are offsets for the preceding keyword value(s). For more explanation of these value types, see [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the size of containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | for [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br> the absolute value, otherwise a percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [position](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value#interpolation "Values of the <position> data type are interpolated independently for the abscissa and ordinate. As the speed is defined by the same <easing-function> for both, the point will move following a line.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

offset-position =   
  normal      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <position>    
  
[<position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
 =   
  <position-one>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <position-two>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <position-four>    
  
<position-one> =   
  left                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  top                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x-start              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x-end                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y-start              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y-end                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block-start          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block-end            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-start         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-end           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>    
  
<position-two> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 block-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 block-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 inline-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
                           
  
<position-four> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 block-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 block-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 inline-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
            
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#examples)

-----------------------------------------------------------------------------------------------------------

### [Setting initial offset-position for an offset-path](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#setting_initial_offset-position_for_an_offset-path)

In this example, the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 property is used to define the path along which the `cyan` element should move. The value of the [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
 CSS function is an [SVG data path](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d)
 that describes a curved path. The element moves along this curved path during the `move` animation.

#### HTML

html

    <div id="wrap">
      <div id="motion-demo"></div>
    </div>
    

#### CSS

    #wrap {
      width: 260px;
      height: 160px;
      border: 1px dashed black;
    }
    

css

    #motion-demo {
      offset-path: path("M20,20 C20,100 200,0 200,100");
      offset-position: left top;
      animation: move 3000ms infinite alternate ease-in-out;
      width: 40px;
      height: 40px;
      background: cyan;
    }
    
    @keyframes move {
      0%,
      20% {
        offset-distance: 0%;
      }
      80%,
      100% {
        offset-distance: 100%;
      }
    }
    

#### Result

### [Comparing various offset starting positions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#comparing_various_offset_starting_positions)

This example visually compares various initial offset starting position of an element when [`ray()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ray)
 is used to specify a value for the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 property. The number inside the element box indicates the element to which CSS is applied as well as the element's anchor point.

    <div class="wrap">
      <div class="box">0</div>
      <div class="box box0">0</div>
      <pre>
        offset-position: normal;
        /* No offset-path specified */
      </pre>
    </div>
    
    <div class="wrap">
      <div class="box">0</div>
      <div class="box box1">1</div>
      <pre>
        offset-position: normal;
        offset-path: ray(0deg);
      </pre>
    </div>
    
    <div class="wrap">
      <div class="box">0</div>
      <div class="box box2">2</div>
      <pre>
        offset-position: auto;
        offset-path: ray(0deg);
      </pre>
    </div>
    
    <div class="wrap">
      <div class="box">0</div>
      <div class="box box3">3</div>
      <pre>
        offset-position: left top;
        offset-path: ray(0deg);
      </pre>
    </div>
    
    <div class="wrap">
      <div class="box">0</div>
      <div class="box box4">4</div>
      <pre>
        offset-position: 30% 70%;
        offset-path: ray(120deg);
      </pre>
    </div>
    

    .wrap {
      position: relative;
      width: 80vw;
      height: 120px;
      border: 1px solid black;
      margin: 0 2em 4em 5em;
      text-align: center;
    }
    
    pre {
      font-size: 1em;
      text-align: right;
      padding-right: 10px;
      line-height: 1em;
    }
    
    .box {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 50px;
      height: 50px;
    }
    
    .box + .box {
      opacity: 1;
    }
    

css

    .box {
      background-color: green;
      border-top: 6px dashed white;
      background-clip: border-box;
      position: absolute;
      top: 20px;
      left: 20px;
      opacity: 20%;
      color: white;
    }
    
    .box0 {
      offset-position: normal;
    }
    
    .box1 {
      offset-position: normal;
      offset-path: ray(0deg);
    }
    
    .box2 {
      offset-position: auto;
      offset-path: ray(0deg);
    }
    
    .box3 {
      offset-position: left top;
      offset-path: ray(0deg);
    }
    
    .box4 {
      offset-position: 30% 70%;
      offset-path: ray(120deg);
    }
    

#### Result

In `box0`, the absence of the `offset-path` property means that an `offset-position` of either `normal` or `auto` has no effect. When `offset-position` is `normal`, the ray starts at the center of the containing block (i.e., `50% 50%`). This is the default starting position of an offset path and is used when no `offset-position` is specified. Notice the difference between offset starting positions `auto` and `left top`. The value `auto` aligns the element's anchor point to its own top-left corner, whereas the value `left top` aligns the element's anchor point to the top-left corner of the containing block.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Motion Path Module Level 1  <br>\# offset-position-property](https://drafts.csswg.org/motion/#offset-position-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset)
    
*   [`offset-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-anchor)
    
*   [`offset-distance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance)
    
*   [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
    
*   [`offset-rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/offset-position/index.md?plain=1 "Folder: en-us/web/css/reference/properties/offset-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foffset-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foffset-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foffset-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foffset-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")