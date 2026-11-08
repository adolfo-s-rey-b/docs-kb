*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#mdn-search)
    

`mask-position` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mask-position`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the initial position, relative to the mask position layer set by [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
, for each defined mask image.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Single <position> keyword value */
    /* Sets second value to 'center' */
    mask-position: left;
    mask-position: center;
    mask-position: right;
    mask-position: top;
    mask-position: bottom;
    
    /* Two <position> keyword values */
    mask-position: left center;
    mask-position: right top;
    
    /* One length or percentage <position> value */
    /* Horizontal position. Vertical position set to 'center' */
    mask-position: 25%;
    mask-position: 0px;
    mask-position: 8em;
    
    /* Two length or percentage <position> values */
    /* First value: horizontal position. Second value: vertical position */
    mask-position: 25% 75%;
    mask-position: 0px 0px;
    mask-position: 10% 8em;
    
    /* Edge offsets: Four <position> values */
    mask-position: bottom 10px right 20px;
    mask-position: right 3em bottom 10px;
    mask-position: bottom 10px right 0;
    
    /* Multiple <position> values */
    mask-position:
      top left,
      bottom 10px right 10px;
    mask-position:
      1rem 1rem,
      center;
    
    /* Global values */
    mask-position: inherit;
    mask-position: initial;
    mask-position: revert;
    mask-position: revert-layer;
    mask-position: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#values)

This property is specified as a comma-separated list of values. Each value has the following type:

[`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)

One, two, or four values representing a 2D position specifying the edges of the element's box. Relative or absolute offsets can be given.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#description)

---------------------------------------------------------------------------------------------------------------

The `mask-position` property defines the position of each mask layer. An element can have multiple mask layers applied. The number of layers is determined by the number of comma-separated values in the [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 property value (even `none` values create a layer).

Each `mask-position` value in the comma-separated list of values is matched up with an associated mask layer as defined by the list of `mask-image` values, in order. If the number of values in the two properties differs:

*   If `mask-position` has more values than mask-image, the excess values of `mask-position` are not used.
*   If `mask-position` has fewer values than mask-image, the `mask-position` values are repeated.

Each `mask-position` defines the associated mask layer's position relative to the associated [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
 value. The `mask-origin` property values are similarly matched up with the `mask-image` values, in order, with excess `mask-position` values being unused or `mask-position` values being repeated if they are fewer in number than the `mask-origin` values. Each mask layer, therefore, has an associated `mask-origin` and `mask-position` value.

If no `mask-origin` is set, the value defaults to `padding-box`, meaning the origin of each `mask-position` is the element's [padding-box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#padding-box)
.

### [One-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#one-value_syntax)

If only one `mask-position` value is specified, the second value is assumed to be `center`. If the value is a `<length>` or `<percentage>`, it defines the position of the mask along the horizontal axis, with the mask being vertically centered within the origin box. For example, `mask-position: 0%;` is equal to `mask-position: 0% center`.

If you use a single keyword for positioning, the other value will resolve to `center`. The default of `mask-position` is `0% 0%`, which equates to `mask-position: top left`. However:

*   `mask-position: top;` is equivalent to `mask-position: top center;`.
*   `mask-position: left;` is equivalent to `mask-position: center left`.
*   `mask-position: center;` is equal to `mask-position: center center`.

If the value is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value, it represents the horizontal position as an offset from the left edge of the mask positioning. A positive value represents an offset inward from the left edge of the box container. The position can be set outside of the element's box using a negative value — this creates an outward offset that places the item outside the container's left edge.

#### Percentage values

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value represents the mask's horizontal position value relative to the width of the container, positioned relative to the left edge. However, the offset is not from the mask edge to the box edge. Instead, the mask image dimension is [subtracted from the container's dimension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position#regarding_percentages)
, and then a percentage of the resulting value is used as the direct offset from the box's left edge, which is the same as [percentage values for `background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position#regarding_percentages)
.

The equation is:

`(container dimension - mask dimension) * position percentage = dimension offset value`

Given a `100px`\-wide mask and a `1000px`\-wide origin box, setting `mask-position: 10%;` (the equivalent of `10% 50%`) results in the mask being vertically centered at `90px` from the left edge. The equation is `(1000 - 100) * 10% = 90`. If the left offset had been `0%`, the mask's left edge would be flush to the left of the container (`(1000 - 100) * 0% = 0`).

If the left offset had been `100%`, the mask's right edge would be flush to the right of the container as the left edge of the `100px` wide mask would be `900px` (`(1000 - 100) * 100% = 900`) from the left edge of the container (the `100px` mask width plus `900px` distance from the left edge means the right edge would be `1000px` from the left edge, which is the right edge of the container).

### [Two-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#two-value_syntax)

A two-value `<position>` specifies the position of the mask image inside its mask positioning area, with length and percentage values specifying offsets from the `left` and `top` of the area.

If the two values are [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 values, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values, or the keyword `center`, the first value represents the horizontal position as an offset from the left edge of the mask positioning area, and the second value represents the vertical position as an offset from it's top edge, with [percentages being offset](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#percentage_values)
 by the mask's size in that dimension.

In addition, if [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values are specified, the first value is also the horizontal position value relative to the left edge, and the second value is also the vertical position value relative to the top edge.

A pair of axis-specific keywords can be reordered, as can an axis-specific keyword and a length or percentage, but two length or percentage values are not interchangeable. If one of the two values is `top`, `right`, `bottom`, or `left`, the order of the two values doesn't matter. Any `center` or `<length-percentage>` value in the pair of values will be applied to the other dimension.

### [Four-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#four-value_syntax)

The four-value syntax consists of two pairs of values, each pair containing a keyword specifying the edge to offset from, and a `<length>` and `<percentage>` value specifying the offset distance. For example, `mask-position: left 1em top 2em` specifies a `1em` horizontal offset from the left box edge and a `2em` vertical offset from the top edge. The two-value equivalent would be `mask-position: 1em 2em`.

Because we're defining the offset edges when using the four-value syntax, the order isn't important: `mask-position: top 2em left 1em` and `mask-position: left 1em top 2em` both produce the same result.

The real power of the four-value syntax is that it allows us to specify offset edges other than `left` and `top`. For example, `mask-position: bottom 10px right 20px` creates a `10px` vertical offset up from the bottom edge and a `20px` horizontal offset leftward from the right edge. Usually, the four-value syntax is used to offset from the bottom and/or right. But this syntax is also helpful if you can't remember the offset edge order for the two-value syntax.

One thing to note is that, unlike the `<bg-position>` data type values for [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
, the `<position>` values for `mask-position` do not allow for a 3-value syntax and do not allow offsetting from `center`. When offsetting the mask from the `bottom` or `right`, the `mask-position` requires all four values to be declared.

For the four-value syntax to be valid, it needs to specify either `top` or `bottom` as the vertical offset edge, along with the vertical length or percentage offset value, and either `left` or `right` as the horizontal offset edge, along with the horizontal length or percentage offset value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0% 0%` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to size of mask painting area minus size of mask layer image (see the text for [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)<br>) |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | Consists of two keywords representing the origin and two offsets from that origin, each given as an absolute length (if given a <length>), otherwise as a percentage. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a repeatable list |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

mask-position =   
  <position>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#examples)

---------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#basic_usage)

html

    <section>
      <div></div>
    </section>
    

css

    section {
      border: 1px solid black;
      width: 250px;
      height: 250px;
    }
    
    div {
      width: 250px;
      height: 250px;
      margin-bottom: 10px;
      background: blue linear-gradient(red, blue);
    
      mask-image: url("/shared-assets/images/examples/mask-star.svg");
      mask-repeat: no-repeat;
      mask-position: top right;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-mask-position](https://drafts.csswg.org/css-masking/#the-mask-position) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position#see_also)

---------------------------------------------------------------------------------------------------------

*   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
    
*   [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    
*   [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
    
*   [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
    
*   [`mask-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
    
*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
     shorthand
*   [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
    
*   [`mask-border-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset)
    
*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS `mask` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
    
*   [Declaring multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module
*   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
    
*   [`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mask-position/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mask-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6354422058e438a2599e4eab71eaec8eb40850fa%0A*+Document+last+modified%3A+2026-09-14T09%3A57%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")