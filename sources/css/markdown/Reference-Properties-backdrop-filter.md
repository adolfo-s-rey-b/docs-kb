*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#mdn-search)
    

`backdrop-filter` CSS property
==============================

Baseline 2024

Newly available

Since September 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`backdrop-filter`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property lets you apply graphical effects such as blurring or color shifting to the area behind an element. Because it applies to everything _behind_ the element, to see the effect the element or its background needs to be transparent or partially transparent.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#try_it)

-------------------------------------------------------------------------------------------------------

    backdrop-filter: blur(10px);
    

    backdrop-filter: invert(80%);
    

    backdrop-filter: sepia(90%);
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div id="example-element">Example</div>
      </div>
    </section>
    

    .example-container {
      background-image: url("/shared-assets/images/examples/balloon.jpg");
      background-size: cover;
      width: 200px;
      height: 200px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: black;
    }
    
    #example-element {
      font-weight: bold;
      flex: 1;
      text-align: center;
      padding: 20px 10px;
      background-color: rgb(255 255 255 / 0.2);
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    backdrop-filter: none;
    
    /* URL to SVG filter */
    backdrop-filter: url("common-filters.svg#filter");
    
    /* <filter-function> values */
    backdrop-filter: blur(2px);
    backdrop-filter: brightness(60%);
    backdrop-filter: contrast(40%);
    backdrop-filter: drop-shadow(4px 4px 10px blue);
    backdrop-filter: grayscale(30%);
    backdrop-filter: hue-rotate(120deg);
    backdrop-filter: invert(70%);
    backdrop-filter: opacity(20%);
    backdrop-filter: sepia(90%);
    backdrop-filter: saturate(80%);
    
    /* Multiple filters */
    backdrop-filter: url("filters.svg#filter") blur(4px) saturate(150%);
    
    /* Global values */
    backdrop-filter: inherit;
    backdrop-filter: initial;
    backdrop-filter: revert;
    backdrop-filter: revert-layer;
    backdrop-filter: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#none)

No filter is applied to the backdrop.

[`<filter-value-list>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#filter-value-list)

A space-separated list of [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
s or an [SVG filter](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
 that will be applied to the backdrop. CSS `<filter-function>`s include [`blur()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
, [`brightness()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)
, [`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
, [`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
, [`grayscale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)
, [`hue-rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
, [`invert()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
, [`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
, [`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
, and [`sepia()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#description)

-----------------------------------------------------------------------------------------------------------------

The `backdrop-filter` property applies filter effects to the pixels painted _behind_ an element, up to the nearest ancestor that is a **backdrop root**. Content above the backdrop root is not affected.

### [Backdrop root](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#backdrop_root)

A backdrop root is an element that establishes a boundary for `backdrop-filter` effects. The following elements are backdrop roots:

*   The root element ([`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
    )
*   An element with a [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
     value other than `none`
*   An element with an [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
     value less than `1`
*   An element with a [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
    , [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    , [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
    , or [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
     value other than `none`
*   An element with a `backdrop-filter` value other than `none`
*   An element with a [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
     value other than `normal`
*   An element with [`will-change`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)
     set to any of the above properties

This means that if a parent element has `opacity: 0.9`, it becomes a backdrop root and any child's `backdrop-filter` will only blur the content between that parent and the child - not the content behind the parent. This is a common source of confusion when `backdrop-filter` appears to have no visible effect despite being correctly applied.

The following example demonstrates how backdrop roots affect `backdrop-filter`. The first container has `will-change: opacity`, making it a backdrop root - notice that the blur circle only affects the text and square inside the container, not the checkered background behind it. The second container is not a backdrop root, so its blur circle affects everything behind it, including the page background.

html

    <div class="parent backdrop-root">
      <div class="text">Text</div>
      <div class="square"></div>
      <div class="overlay"></div>
    </div>
    <div class="parent">
      <div class="text">Text</div>
      <div class="square"></div>
      <div class="overlay"></div>
    </div>
    

css

    body {
      display: flex;
      column-gap: 16px;
      padding: 16px;
      background-image: conic-gradient(
        gray 90deg,
        silver 90deg 180deg,
        gray 180deg 270deg,
        silver 270deg
      );
      background-size: 32px 32px;
    }
    
    .parent {
      position: relative;
      width: 256px;
      height: 256px;
    }
    
    .backdrop-root {
      outline: 2px solid crimson;
      will-change: opacity;
    }
    
    .square {
      position: absolute;
      top: 35px;
      left: 40%;
      width: 25%;
      height: 25%;
      border: 10px solid white;
    }
    
    .text {
      position: absolute;
      left: 40%;
      color: white;
      font-size: 32px;
      font-weight: 500;
      text-align: center;
      line-height: 256px;
      filter: blur(1px);
    }
    
    .overlay {
      position: absolute;
      top: 25%;
      left: 50%;
      width: 50%;
      height: 50%;
      outline: 3px solid gainsboro;
      border-radius: 9999px;
      backdrop-filter: blur(10px);
    }
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [filter function list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#interpolation "If both filters have a function list of same length without URL, each of their filters functions is interpolated according to its specific rules. If they have different lengths, the missing equivalent filter functions from the longer list are added to the end of the shorter list using their default values, then all filter functions are interpolated according to their specific rules. If one filter is 'none', it is replaced with the filter functions list of the other one using the filter function default values, then all filter functions are interpolated according to their specific rules. Otherwise discrete interpolation is used.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

backdrop-filter =   
  none                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <filter-value-list>    
  
<filter-value-list> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <filter-function> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    
  
[<filter-function>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
 =   
  <blur()>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <brightness()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <contrast()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <drop-shadow()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <grayscale()>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <hue-rotate()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <invert()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <opacity()>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <sepia()>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <saturate()>       
  
[<blur()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
 =   
  blur( [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<brightness()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)
 =   
  brightness( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<contrast()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
 =   
  contrast( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<drop-shadow()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
 =   
  drop-shadow( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
[{2,3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<grayscale()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)
 =   
  grayscale( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<hue-rotate()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
 =   
  hue-rotate( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<invert()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
 =   
  invert( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<opacity()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
 =   
  opacity( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<sepia()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
 =   
  sepia( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<saturate()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
 =   
  saturate( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#examples)

-----------------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#css)

css

    .box {
      background-color: rgb(255 255 255 / 30%);
      backdrop-filter: blur(10px);
    }
    
    body {
      background-image: url("anemones.jpg");
    }
    

    html,
    body {
      height: 100%;
      width: 100%;
    }
    
    .container {
      background-size: cover;
      align-items: center;
      display: flex;
      justify-content: center;
      height: 100%;
      width: 100%;
    }
    .box {
      border-radius: 5px;
      font-family: sans-serif;
      text-align: center;
      max-width: 50%;
      max-height: 50%;
      padding: 20px 40px;
    }
    

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#html)

html

    <div class="container">
      <div class="box">
        <p>backdrop-filter: blur(10px)</p>
      </div>
    </div>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 2  <br>\# BackdropFilterProperty](https://drafts.csswg.org/filter-effects-2/#BackdropFilterProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
    
*   [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
    
*   [`background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
    , [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
    
*   [CSS filter effects](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Filter_effects)
    
*   [CSS compositing and blending](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Compositing_and_blending)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/backdrop-filter/index.md?plain=1 "Folder: en-us/web/css/reference/properties/backdrop-filter (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackdrop-filter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackdrop-filter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackdrop-filter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackdrop-filter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")