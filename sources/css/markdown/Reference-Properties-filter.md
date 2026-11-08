*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#mdn-search)
    

`filter` CSS property
=====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`filter`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property applies graphical effects like blur or color shift to an element. Filters are commonly used to adjust the rendering of images, backgrounds, and borders.

Several [functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#functions)
, such as `blur()` and `contrast()`, are available to help you achieve predefined effects.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#try_it)

----------------------------------------------------------------------------------------------

    filter: url("/shared-assets/images/examples/shadow.svg#element-id");
    

    filter: blur(5px);
    

    filter: contrast(200%);
    

    filter: grayscale(80%);
    

    filter: hue-rotate(90deg);
    

    filter: drop-shadow(16px 16px 20px red) invert(75%);
    

    <section id="default-example">
      <div class="example-container">
        <img
          id="example-element"
          src="/shared-assets/images/examples/firefox-logo.svg"
          width="200" />
      </div>
    </section>
    

    .example-container {
      background-color: white;
      width: 260px;
      height: 260px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    
    #example-element {
      flex: 1;
      padding: 30px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#syntax)

----------------------------------------------------------------------------------------------

css

    /* <filter-function> values */
    filter: blur(5px);
    filter: brightness(0.4);
    filter: contrast(200%);
    filter: drop-shadow(16px 16px 20px blue);
    filter: grayscale(50%);
    filter: hue-rotate(90deg);
    filter: invert(75%);
    filter: opacity(25%);
    filter: saturate(30%);
    filter: sepia(60%);
    
    /* URL */
    filter: url("filters.svg#filter-id");
    
    /* Multiple filters */
    filter: contrast(175%) brightness(3%);
    filter: drop-shadow(3px 3px red) sepia(100%) drop-shadow(-3px -3px blue);
    
    /* Use no filter */
    filter: none;
    
    /* Global values */
    filter: inherit;
    filter: initial;
    filter: revert;
    filter: revert-layer;
    filter: unset;
    

### [Referencing an SVG filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#referencing_an_svg_filter)

You can use `url()` to reference an [SVG filter element](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
. For a reference to an SVG [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
 element, use the following syntax:

css

    filter: url("file.svg#filter-element-id");
    

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#functions)

The `filter` property is specified as `none` or one or more of the functions listed below. If the parameter for any function is invalid, the function returns `none`. Except where noted, the functions that take a value expressed with a percent sign (as in `34%`) also accept the value expressed as decimal (as in `0.34`).

When the `filter` property values contains multiple functions, the filters are applied in order.

[`blur()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)

Applies a Gaussian blur to the input image.

css

    filter: blur(5px);
    

[`brightness()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)

Applies a linear multiplier to the input image, making it appear more or less bright. Values are linear multipliers on the effect, with `0%` creating a completely black image, `100%` having no effect, and values over `100%` brightening the image.

css

    filter: brightness(2);
    

[`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)

Adjusts the contrast of the input image. A value of `0%` makes the image gray, `100%` has no effect, and values over `100%` create a contrast.

css

    filter: contrast(200%);
    

[`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)

Applies the parameter `<shadow>` as a drop shadow, following the contours of the image. The shadow syntax is similar to `<box-shadow>` (defined in the [CSS backgrounds and borders module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
), with the exception that the `inset` keyword and `spread` parameter are not allowed. As with all `filter` property values, any filters after the `drop-shadow()` are applied to the shadow.

css

    filter: drop-shadow(16px 16px 10px black);
    

[`grayscale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)

Converts the image to grayscale. A value of `100%` is completely grayscale. The initial value of `0%` leaves the input unchanged. Values between `0%` and `100%` produce linear multipliers on the effect.

css

    filter: grayscale(100%);
    

[`hue-rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)

Applies a hue rotation. The `<angle>` value defines the number of degrees around the hue color circle at which the input samples will be adjusted. A value of `0deg` leaves the input unchanged.

css

    filter: hue-rotate(90deg);
    

[`invert()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)

Inverts the samples in the input image. A value of `100%` completely inverts the image. A value of `0%` leaves the input unchanged. Values between `0%` and `100%` have linear multipliers on the effect.

css

    filter: invert(100%);
    

[`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)

Applies transparency. `0%` makes the image completely transparent and `100%` leaves the image unchanged.

css

    filter: opacity(50%);
    

[`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)

Saturates the image, with `0%` being completely unsaturated, `100%` leaving the image unchanged, and values of over `100%` increasing saturation.

css

    filter: saturate(200%);
    

[`sepia()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)

Converts the image to sepia, with a value of `100%` making the image completely sepia and `0%` making no change.

css

    filter: sepia(100%);
    

### [Combining functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#combining_functions)

You may combine any number of functions to manipulate the rendering. The filters are applied in the order declared. The following example enhances the contrast and brightness of the image:

css

    filter: contrast(175%) brightness(103%);
    

### [Interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#interpolation)

When animated, if both the beginning and end filters have a function list of the same length without [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 in the same order, each of their filter functions is [interpolated](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 according to the filter function's specific rules.

If the filter lists are of different lengths, the missing equivalent filter functions from the longer list are added to the end of the shorter list. The added functions use their initial, no filter modification values. All the filters listed are then interpolated according to the filter function's specific rules. Otherwise, discrete interpolation is used.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#formal_definition)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [filter function list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#interpolation "If both filters have a function list of same length without URL, each of their filters functions is interpolated according to its specific rules. If they have different lengths, the missing equivalent filter functions from the longer list are added to the end of the shorter list using their default values, then all filter functions are interpolated according to their specific rules. If one filter is 'none', it is replaced with the filter functions list of the other one using the filter function default values, then all filter functions are interpolated according to their specific rules. Otherwise discrete interpolation is used.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#formal_syntax)

------------------------------------------------------------------------------------------------------------

filter =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#examples)

--------------------------------------------------------------------------------------------------

### [Applying filter functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#applying_filter_functions)

The `filter` property is applied to the second image, graying and blurring both the image and its border.

css

    img {
      border: 5px solid yellow;
    }
    /* Gray the second image by 40% and blur by 5px */
    img:nth-of-type(2) {
      filter: grayscale(0.4) blur(5px);
    }
    

html

    <img src="pencil.jpg" alt="Original image is sharp" />
    <img src="pencil.jpg" alt="The image and border are blurred and muted" />
    

### [Repeating filter functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#repeating_filter_functions)

Filter functions are applied in order of appearance. The same filter function can be repeated.

css

    #MDN-logo {
      border: 1px solid blue;
      filter: drop-shadow(5px 5px 0 red) hue-rotate(180deg)
        drop-shadow(5px 5px 0 red);
    }
    

    <svg
      id="MDN-logo"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 361 104.2"
      xml:space="preserve"
      role="img">
      <title>MDN Web Docs</title>
      <path
        d="M197.6 73.2h-17.1v-5.5h3.8V51.9c0-3.7-.7-6.3-2.1-7.9-1.4-1.6-3.3-2.3-5.7-2.3-3.2 0-5.6 1.1-7.2 3.4s-2.4 4.6-2.5 6.9v15.6h6v5.5h-17.1v-5.5h3.8V51.9c0-3.8-.7-6.4-2.1-7.9-1.4-1.5-3.3-2.3-5.6-2.3-3.2 0-5.5 1.1-7.2 3.3-1.6 2.2-2.4 4.5-2.5 6.9v15.8h6.9v5.5h-20.2v-5.5h6V42.4h-6.1v-5.6h13.4v6.4c1.2-2.1 2.7-3.8 4.7-5.2 2-1.3 4.4-2 7.3-2s5.3.7 7.5 2.1c2.2 1.4 3.7 3.5 4.5 6.4 1.1-2.5 2.7-4.5 4.9-6.1s4.8-2.4 7.9-2.4c3.5 0 6.5 1.1 8.9 3.3s3.7 5.6 3.7 10.2v18.2h6.1v5.5zm42.5 0h-13.2V66c-1.2 2.2-2.8 4.1-4.9 5.6-2.1 1.6-4.8 2.4-8.3 2.4-4.8 0-8.7-1.6-11.6-4.9-2.9-3.2-4.3-7.7-4.3-13.3 0-5 1.3-9.6 4-13.7 2.6-4.1 6.9-6.2 12.8-6.2s9.8 2.2 12.3 6.5V22.7h-8.6v-5.6h15.8v50.6h6v5.5zm-13.3-16.8V52c-.1-3-1.2-5.5-3.2-7.3s-4.4-2.8-7.2-2.8c-3.6 0-6.3 1.3-8.2 3.9-1.9 2.6-2.8 5.8-2.8 9.6 0 4.1 1 7.3 3 9.5s4.5 3.3 7.4 3.3c3.2 0 5.8-1.3 7.8-3.8 2.1-2.6 3.1-5.3 3.2-8zm61.5 16.8H269v-5.5h6V51.9c0-3.7-.7-6.3-2.2-7.9-1.4-1.6-3.4-2.3-5.7-2.3-3.1 0-5.6 1-7.4 3s-2.8 4.4-2.9 7v15.9h6v5.5h-19.3v-5.5h6V42.4h-6.2v-5.6h13.6V43c2.6-4.6 6.8-6.9 12.7-6.9 3.6 0 6.7 1.1 9.2 3.3s3.7 5.6 3.7 10.2v18.2h6v5.4h-.2z"></path>
      <g fill="blue">
        <path
          d="M42 .2 13.4 92.3H1.7L30.2.2H42zM52.4.2v92.1H42V.2h10.4zm40.3 0L64.2 92.3H52.5L81 .2h11.7zM103.1.2v92.1H92.7V.2h10.4zM294 95h67v8.8h-67V95z"></path>
      </g>
    </svg>
    

The filters are applied in order. This is why the drop shadows are not the same color: the first drop shadow's hue is altered by the `hue-rotate()` function but the second one is not.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# FilterProperty](https://drafts.csswg.org/filter-effects/#FilterProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter#see_also)

--------------------------------------------------------------------------------------------------

*   [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
    
*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
    
*   SVG [`filter`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/filter)
     attribute
*   CSS [compositing and blending](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Compositing_and_blending)
     module, including the CSS [`background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
     and [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
     properties.
*   [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
    , including the SVG [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
     element and SVG [`filter`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/filter)
     attribute.
*   [Applying SVG effects to HTML content](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Applying_SVG_effects_to_HTML_content)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/filter/index.md?plain=1 "Folder: en-us/web/css/reference/properties/filter (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffilter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffilter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffilter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffilter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd19dec85109590176f946fcceef48c787d578b1e%0A*+Document+last+modified%3A+2026-08-27T15%3A03%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")