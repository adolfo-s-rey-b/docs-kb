*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#mdn-search)
    

`flex` CSS property
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`flex`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets how a [flex item](https://developer.mozilla.org/en-US/docs/Glossary/Flex_Item)
 will grow or shrink to fit the space available in its flex container.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#try_it)

--------------------------------------------------------------------------------------------

    flex: 1;
    

    flex: 2;
    

    flex: 1 30px;
    

    flex: 1 1 100px;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">Change me</div>
      <div>flex: 1</div>
      <div>flex: 1</div>
    </section>
    

    .default-example {
      border: 1px solid #c5c5c5;
      width: auto;
      max-height: 300px;
      display: flex;
    }
    
    .default-example > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      margin: 10px;
      flex-grow: 1;
      flex-shrink: 1;
      flex-basis: 0;
    }
    
    #example-element {
      background-color: rgb(255 0 200 / 0.2);
      border: 3px solid rebeccapurple;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
    
*   [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
    
*   [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#syntax)

--------------------------------------------------------------------------------------------

css

    /* Keyword values */
    flex: none; /* 0 0 auto */
    
    /* One value, unitless number: flex-grow
    flex-basis is then equal to 0%. */
    flex: 2; /* 2 1 0% */
    
    /* One value, width/height: flex-basis */
    flex: auto; /* 1 1 auto */
    flex: 10em; /* 1 1 10em */
    flex: 30%;
    flex: min-content;
    
    /* Two values: flex-grow | flex-basis */
    flex: 1 30px; /* 1 1 30px */
    
    /* Two values: flex-grow | flex-shrink */
    flex: 2 2; /* 2 2 0% */
    
    /* Three values: flex-grow | flex-shrink | flex-basis */
    flex: 2 2 10%;
    
    /* Global values */
    flex: inherit;
    flex: initial; /* 0 1 auto */
    flex: revert;
    flex: revert-layer;
    flex: unset;
    

The `flex` property may be specified using one, two, or three values.

*   **One-value syntax:** the value must be one of:
    
    *   a valid value for [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
        : then the shorthand expands to `flex: <flex-grow> 1 0%`.
    *   a valid value for [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
        : then the shorthand expands to `flex: 1 1 <flex-basis>`.
    *   the keyword `none` or one of the global keywords.
*   **Two-value syntax:**
    
    *   The first value must be a valid value for [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
        .
        
    *   The second value must be one of:
        
        *   a valid value for [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
            : then the shorthand expands to `flex: <flex-grow> <flex-shrink> 0%`.
        *   a valid value for [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
            : then the shorthand expands to `flex: <flex-grow> 1 <flex-basis>`.
*   **Three-value syntax:** the values must be in the following order:
    
    1.  a valid value for [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
        .
    2.  a valid value for [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
        .
    3.  a valid value for [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
        .

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#values)

[`<'flex-grow'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#flex-grow)

Defines the [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
 of the flex item. Negative values are considered invalid. Defaults to `1` when omitted. (initial is `0`)

[`<'flex-shrink'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#flex-shrink)

Defines the [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
 of the flex item. Negative values are considered invalid. Defaults to `1` when omitted. (initial is `1`)

[`<'flex-basis'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#flex-basis)

Defines the [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
 of the flex item. Defaults to `0%` when omitted. The initial value is `auto`.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#none)

The item is sized according to its `width` and `height` properties. It is fully inflexible: it neither shrinks nor grows in relation to the flex container. This is equivalent to setting `flex: 0 0 auto`.

Commonly desired flexbox effects can be achieved using the following `flex` values:

*   `initial`: Flex item doesn't grow but can shrink. This default value expands to `flex: 0 1 auto`. The item is sized according to its `width` or `height` properties, depending on the `flex-direction`. If there is negative available space, the item will shrink to its minimum size to fit within the container but will not grow to absorb any positive space available in the flex container.
*   `auto`: Flex item can grow and shrink. This value expands to `flex: 1 1 auto`. The item is sized according to its `width` or `height` properties, depending on the `flex-direction`, but grows to absorb available positive space in the flex container or shrink down to its minimum size to fit the container in the case of negative space. The flex item is fully flexible.
*   `none`: The flex item neither grows nor shrinks. This value expands to `flex: 0 0 auto`. The item is sized according to its `width` or `height` properties, depending on the direction of the flex container. The flex item is fully inflexible.
*   `flex: <number [1,∞]>`: The flex item's main size will be proportional to the number set. This value expands to `flex: <number> 1 0%`. This sets the `flex-basis` to `0%` and makes the flex item flexible. The item will be at least as wide or tall as its minimum size, with the container's positive available space being proportionally distributed based on the growth factors of this item and its sibling flex items. If all the flex items use this pattern, all will be sized in proportion to their numeric values.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#description)

------------------------------------------------------------------------------------------------------

For most purposes, authors should set `flex` to one of the following values: `auto`, `initial`, `none`, or a positive unitless number. To see the effect of these values, try resizing the flex containers below:

    <div class="flex-container">
      <div class="item auto">auto</div>
      <div class="item auto">auto</div>
      <div class="item auto">auto</div>
    </div>
    
    <div class="flex-container">
      <div class="item auto">auto</div>
      <div class="item initial">initial</div>
      <div class="item initial">initial</div>
    </div>
    
    <div class="flex-container">
      <div class="item auto">auto</div>
      <div class="item auto">auto</div>
      <div class="item none">none</div>
    </div>
    
    <div class="flex-container">
      <div class="item initial">initial</div>
      <div class="item none">none</div>
      <div class="item none">none</div>
    </div>
    
    <div class="flex-container">
      <div class="item four">4</div>
      <div class="item two">2</div>
      <div class="item one">1</div>
    </div>
    

    * {
      box-sizing: border-box;
    }
    
    .flex-container {
      background-color: #f4f7f8;
      resize: horizontal;
      overflow: hidden;
      display: flex;
      margin: 1em;
    }
    
    .item {
      margin: 1em;
      padding: 0.5em;
      width: 110px;
      min-width: 0;
      background-color: #1b5385;
      color: white;
      font-family: monospace;
      font-size: 13px;
    }
    
    .initial {
      flex: initial;
    }
    
    .auto {
      flex: auto;
    }
    
    .none {
      flex: none;
    }
    
    .four {
      flex: 4;
    }
    
    .two {
      flex: 2;
    }
    
    .one {
      flex: 1;
    }
    

By default flex items don't shrink below their [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
 size. To change this, set the item's [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
 or [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#formal_definition)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)<br>    : `0`<br>*   [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)<br>    : `1`<br>*   [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)<br>    : `auto` |
| Applies to | flex items, including in-flow pseudo-elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)<br>    : as specified<br>*   [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)<br>    : as specified<br>*   [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)<br>    : as specified, but with relative lengths converted into absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)<br>    : a [number](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#interpolation "Values of the <number> CSS data type are interpolated as real, floating-point, numbers.")<br>    <br>*   [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)<br>    : a [number](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#interpolation "Values of the <number> CSS data type are interpolated as real, floating-point, numbers.")<br>    <br>*   [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)<br>    : a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>    , [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br>     or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#formal_syntax)

----------------------------------------------------------------------------------------------------------

flex =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<'flex-grow'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)\
 [<'flex-shrink'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [<'flex-basis'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
[<flex-grow>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
 =   
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    
  
[<flex-shrink>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
 =   
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    
  
[<flex-basis>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
 =   
  content    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<'width'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    
  
[<width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 =   
  auto             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <box-size>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-size()>    
  
<box-size> =   
  <length-percentage \[0,∞\]>                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  contain                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  min-content                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  max-content                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fit-content                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch( <length-percentage \[0,∞\]> )      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fit-content( <length-percentage \[0,∞\]> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-size()>                               
  
[<anchor-size()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  anchor-size( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <anchor-name> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <anchor-size> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<calc-size()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
 =   
  calc-size( <calc-size-basis> , <calc-sum> )    
  
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
  
<calc-size-basis> =   
  <size-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-sum>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-size()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  any               
  
[<calc-sum>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 =   
  <calc-product> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '+' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '-' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-product> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-product> =   
  <calc-value> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '\*' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 / [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-value> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dimension>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <calc-sum> )    
  
[<calc-keyword>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
 =   
  e          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pi         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  NaN          

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#examples)

------------------------------------------------------------------------------------------------

### [Setting flex: auto](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#setting_flex_auto)

This example shows how a flex item with `flex: auto` grows to absorb any free space in the container.

#### HTML

html

    <div id="flex-container">
      <div id="flex-auto">
        flex: auto (click to remove/add the `flex: initial` box)
      </div>
      <div id="default">flex: initial</div>
    </div>
    

#### CSS

    body * {
      padding: 1rem;
      user-select: none;
      box-sizing: border-box;
      font-family: "Consolas", "Arial", sans-serif;
    }
    

css

    #flex-container {
      border: 2px dashed gray;
      display: flex;
    }
    
    #flex-auto {
      cursor: pointer;
      background-color: wheat;
    
      flex: auto;
    }
    
    #default {
      background-color: lightblue;
    }
    

#### JavaScript

js

    const flexAutoItem = document.getElementById("flex-auto");
    const defaultItem = document.getElementById("default");
    flexAutoItem.addEventListener("click", () => {
      defaultItem.style.display =
        defaultItem.style.display === "none" ? "block" : "none";
    });
    

#### Result

The flex container contains two flex items:

*   The `#flex-auto` item has a `flex` value of `auto`. The `auto` value expands to `1 1 auto`, i.e., the item is allowed to expand.
*   The `#default` item has no `flex` value set so it defaults to the `initial` value. The `initial` value expands to `0 1 auto`, i.e., the item is not allowed to expand.

The `#default` item takes up as much space as its width requires, but does not expand to take up any more space. All the remaining space is taken up by the `#flex-auto` item.

When you click the `#flex-auto` item, we set the `#default` item's [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to `none`, removing it from the layout. The `#flex-auto` item then expands to occupy all the available space in the container. Clicking the `#flex-auto` item again adds the `#default` item back to the container.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Flexible Box Layout Module Level 1  <br>\# flex-property](https://drafts.csswg.org/css-flexbox/#flex-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#see_also)

------------------------------------------------------------------------------------------------

*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Controlling ratios of flex items along the main axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Controlling_flex_item_ratios)
    
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flex/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flex (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")