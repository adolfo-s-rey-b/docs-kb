*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#mdn-search)
    

`width` CSS property
====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`width`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets an element's width. By default, it sets the width of the [content area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#content_area)
, but if [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
 is set to `border-box`, it sets the width of the [border area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#border_area)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#try_it)

---------------------------------------------------------------------------------------------

    width: 150px;
    

    width: 20em;
    

    width: 75%;
    

    width: auto;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box where you can change the width.
      </div>
    </section>
    

    #example-element {
      display: flex;
      flex-direction: column;
      background-color: #5b6dcd;
      height: 80%;
      justify-content: center;
      color: white;
    }
    

The specified value of `width` applies to the content area so long as its value remains within the values defined by [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
 and [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
.

*   If the value for `width` is less than the value for `min-width`, then `min-width` overrides `width`.
*   If the value for `width` is greater than the value for `max-width`, then `max-width` overrides `width`.

**Note:** As a geometric property, `width` also applies to the [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
, [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
, [`<image>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/image)
, and [`<foreignObject>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/foreignObject)
 SVG elements, with `auto` resolving to `100%` for `<svg>` and `0` for other elements, and percent values being relative to the SVG viewport width for `<rect>`. The CSS `width` property value overrides any SVG [`width`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/width)
 attribute value set on the SVG element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#syntax)

---------------------------------------------------------------------------------------------

css

    /* <length> values */
    width: 300px;
    width: 25em;
    
    /* <percentage> value */
    width: 75%;
    
    /* Keyword values */
    width: max-content;
    width: min-content;
    width: fit-content;
    width: auto;
    width: stretch;
    
    /* function values */
    width: fit-content(20em);
    width: anchor-size(width);
    width: anchor-size(--my-anchor inline, 120%);
    width: calc-size(max-content, size / 2);
    
    /* Global values */
    width: inherit;
    width: initial;
    width: revert;
    width: revert-layer;
    width: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Defines the width as a distance value.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Defines the width as a percentage of the [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
's width.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#auto)

The browser will calculate and select a width for the specified element.

[`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)

The intrinsic preferred width.

[`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)

The intrinsic minimum width.

[`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)

Use the available space, but not more than [max-content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
, i.e., `min(max-content, max(min-content, stretch))`.

[`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)

Sets the width relative to a dimension of an anchor element. When defining the `width` of an anchor-positioned element, the first parameter defaults to the associated anchor's width. If applied to a non-anchor-positioned element, it sets the width to the fallback value. If no fallback is defined, the declaration is ignored.

[`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)

Sets the width to a modified intrinsic size.

[`fit-content(<length-percentage>)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)

Uses the fit-content formula with the available space replaced by the specified argument, clamping the width according to the formula `min(maximum size, max(minimum size, <length-percentage>))`.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#stretch)

Sets the width of the element's [margin box](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model#parts_of_a_box)
 to the width of its [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#identifying_the_containing_block)
. It attempts to make the margin box fill the available space in the containing block, so in a way behaving similar to `100%` but applying the resulting size to the margin box rather than the box determined by [box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#accessibility)

-----------------------------------------------------------------------------------------------------------

Ensure that elements set with a `width` aren't truncated and/or don't obscure other content when the page is zoomed to increase text size.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.4 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-scale.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#formal_definition)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements but non-replaced inline elements, table rows, and row groups |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the width of the containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | a percentage or `auto` or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#formal_syntax)

-----------------------------------------------------------------------------------------------------------

width =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#examples)

-------------------------------------------------------------------------------------------------

### [Default width](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#default_width)

This example demonstrates basic usage and the default `auto` value.

#### HTML

We include two paragraphs; one with a class name.

html

    <p>The MDN community writes really great documentation.</p>
    <p class="has-width">The MDN community writes really great documentation.</p>
    

#### CSS

We make all paragraphs have a gold background, explicitly setting the second paragraph's `width` to `auto`.

css

    p {
      background: gold;
    }
    p.has-width {
      width: auto;
    }
    

#### Results

As `width` defaults to `auto`, both paragraphs are the same width.

### [Using length units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#using_length_units)

This example demonstrates length width values.

#### HTML

We include two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements with some text.

html

    <div class="px_length">Width measured in px</div>
    <div class="em_length">Width measured in em</div>
    

#### CSS

The `px_length` element is set to `200px` while the `em_length` element is set to be `20em` wide. Both elements also have different [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
, and [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 values to enable differentiating between the two when rendered.

css

    .px_length {
      width: 200px;
    
      background-color: red;
      color: white;
      border: 1px solid black;
    }
    
    .em_length {
      width: 20em;
    
      background-color: white;
      color: red;
      border: 1px solid black;
    }
    

#### Results

The `px_length` element will always be 200px wide. The rendered width of the `em_length` element depends on the font size.

### [Using percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#using_percentages)

This example demonstrates using percentage values.

#### HTML

We include one [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element with some text.

html

    <div class="percent">Width in percentage</div>
    

#### CSS

We set the `width` of the element to be `20%` of the width of its parent container.

css

    .percent {
      width: 20%;
    
      background-color: silver;
      border: 1px solid red;
    }
    

#### Results

### [Using intrinsic sizes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#using_intrinsic_sizes)

This example compares `max-content` and `min-content`, and introduces `calc-size`.

#### HTML

We include three paragraphs with the same content; just their class names differ.

html

    <p class="max-green">The MDN community writes really great documentation.</p>
    <p class="min-blue">The MDN community writes really great documentation.</p>
    <p class="min-pink">The MDN community writes really great documentation.</p>
    

#### CSS

We set one paragraph's `width` to `max-content`, the second to `min-content`, and the third to be twice the size of the `min-content` by using the `calc-size()` function. Each is given a different [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 and [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 to enable differentiating between the two.

css

    p.max-green {
      width: max-content;
    
      background-color: lightgreen;
      border-style: dotted;
    }
    
    p.min-blue {
      width: min-content;
    
      background-color: lightblue;
      border-style: dashed;
    }
    
    p.min-pink {
      width: calc-size(min-content, size * 2);
    
      background-color: pink;
      border-style: solid;
    }
    

    @supports not (width: calc-size(min-content, size * 2)) {
      body::before {
        content: "Your browser doesn't support the calc-size() function yet.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Results

The `max-content` example is as wide as the text. The `min-content` example is as wide as the widest word. The `calc-size()` example is set to be twice as wide as the `min-content`.

### [Using the stretch keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#using_the_stretch_keyword)

This example demonstrates the `stretch` value within a [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 container.

#### HTML

We include a parent container with two child elements.

html

    <div class="parent">
      <div class="child">text</div>
      <div class="child stretch">stretch</div>
    </div>
    

#### CSS

We use the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to make the parent a flex container, and set the second child's `width` the `stretch`.

css

    .parent {
      border: solid;
      margin: 1rem;
      display: flex;
    }
    
    .child {
      background: #00999999;
      margin: 1rem;
    }
    
    .stretch {
      width: stretch;
    }
    

    @supports not (width: stretch) {
      body::before {
        content: "Your browser doesn't support the stretch value yet.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

By default, flex items are as wide as their content. The `stretch` value makes the element as wide as the available space allows, with the element's margin box otherwise clamped to the width of its containing block.

### [Using the anchor-size() function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#using_the_anchor-size_function)

This example demonstrates using the `anchor-size()` function to define the width of an anchor-positioned element; we defined its width as a multiple of its anchor's height.

#### HTML

We specify two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements: one `anchor` element and one `infobox` element that we'll position relative to the anchor.

html

    <div class="anchor">⚓︎</div>
    
    <div class="infobox">
      <p>Infobox.</p>
    </div>
    

#### CSS

We declare the `anchor` `<div>` as an anchor element by giving it an [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
. The positioned element has its [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 property set to `absolute`, and is associated with the anchor element via its [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property. We also set absolute [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 and `width` dimensions on the anchor and define the width of the anchor-positioned element to be the width of the anchor using the `anchor-size()` function as the value of the `width` property. As a bonus, we also use the `anchor-size()` function to define the infobox's [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 position, making the gap between the anchor and the infobox one quarter of the height of the anchor.

    .anchor {
      anchor-name: --my-anchor;
      width: 120px;
      height: 60px;
    
      font-size: 2rem;
      background-color: lightpink;
      text-align: center;
      align-content: center;
      outline: 1px solid black;
    }
    
    .infobox {
      position-anchor: --my-anchor;
      position: absolute;
      position-area: right;
      width: anchor-size(width);
    
      left: calc( anchor-size(height) / 4 )
    
      align-content: center;
      color: darkblue;
      background-color: azure;
      outline: 1px solid #dddddd;
    }
    

    body {
      padding: 5em;
    }
    
    @supports not (width: anchor-size(width)) {
      body::before {
        content: "Your browser doesn't support the anchor-size() function value.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Results

Note how the infobox's width is always the same as the anchor element's width.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 3  <br>\# propdef-width](https://drafts.csswg.org/css-sizing-3/#propdef-width) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#see_also)

-------------------------------------------------------------------------------------------------

*   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    
*   [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
    
*   [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
    , [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
    
*   [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
    , [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
    
*   SVG [`width`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/width)
     attribute
*   [Introduction to the CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
     guide
*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/width/index.md?plain=1 "Folder: en-us/web/css/reference/properties/width (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwidth&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwidth%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwidth%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwidth%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa8b7faffbd3fdeae5c0be97793d963d8a31cd1cf%0A*+Document+last+modified%3A+2026-04-22T11%3A39%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")