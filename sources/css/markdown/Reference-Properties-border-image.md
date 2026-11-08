*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#mdn-search)
    

`border-image` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-image`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property draws an image around a given element. It replaces the element's regular [border](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
.

**Note:** You should specify a separate [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 in case the border image fails to load. Although the specification doesn't strictly require it, some browsers don't render the border image if [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 is `none` or [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
 is `0`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#try_it)

----------------------------------------------------------------------------------------------------

    border-image: url("/shared-assets/images/examples/border-diamonds.png") 30;
    

    border-image: url("/shared-assets/images/examples/border-diamonds.png") 30 /
      19px round;
    

    border-image: url("/shared-assets/images/examples/border-diamonds.png") 30
      fill / 30px / 30px space;
    

    border-image: linear-gradient(#f6b73c, #4d9f0c) 30;
    

    border-image: repeating-linear-gradient(30deg, #4d9f0c, #9198e5, #4d9f0c 20px)
      60;
    

    <section id="default-example">
      <div id="example-element">This is a box with a border around it.</div>
    </section>
    

    #example-element {
      width: 80%;
      height: 80%;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 50px;
      background: #fff3d4;
      color: black;
      border: 30px solid;
      border-image: url("/shared-assets/images/examples/border-diamonds.png") 30
        round;
      font-size: 1.2em;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#constituent_properties)

------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`border-image-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
    
*   [`border-image-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
    
*   [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
    
*   [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
    
*   [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)
    

This shorthand property is reset, with all the longhand properties set to their initial values, by the CSS [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 shorthand property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#syntax)

----------------------------------------------------------------------------------------------------

css

    /* source | slice */
    border-image: linear-gradient(red, blue) 27;
    
    /* source | slice | repeat */
    border-image: url("/images/border.png") 27 space;
    
    /* source | slice | width */
    border-image: linear-gradient(red, blue) 27 / 35px;
    
    /* source | slice | width | outset | repeat */
    border-image: url("/images/border.png") 27 23 / 50px 30px / 1rem round space;
    
    /* Global values */
    border-image: inherit;
    border-image: initial;
    border-image: revert;
    border-image: revert-layer;
    border-image: unset;
    

The `border-image` property may be specified with anywhere from one to five of the values listed below.

**Note:** If the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 of [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
 is `none`, or if the image cannot be displayed, the [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 will be displayed instead.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#values)

[`<'border-image-source'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#border-image-source)

The source image. See [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
.

[`<'border-image-slice'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#border-image-slice)

The dimensions for slicing the source image into regions. Up to four values may be specified. See [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
.

[`<'border-image-width'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#border-image-width)

The width of the border image. Up to four values may be specified. See [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)
.

[`<'border-image-outset'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#border-image-outset)

The distance of the border image from the element's outside edge. Up to four values may be specified. See [`border-image-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
.

[`<'border-image-repeat'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#border-image-repeat)

Defines how the edge regions of the source image are adjusted to fit the dimensions of the border image. Up to two values may be specified. See [`border-image-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#accessibility)

------------------------------------------------------------------------------------------------------------------

Assistive technology cannot parse border images. If the image contains information critical to understanding the page's overall purpose, it is better to describe it semantically in the document.

*   [MDN Understanding WCAG, Guideline 1.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.1_%E2%80%94_providing_text_alternatives_for_non-text_content)
    
*   [Understanding Success Criterion 1.1.1 | Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/text-equiv-all.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)<br>    : `none`<br>*   [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)<br>    : `100%`<br>*   [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)<br>    : `1`<br>*   [`border-image-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)<br>    : `0`<br>*   [`border-image-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)<br>    : `stretch` |
| Applies to | all elements, except internal table elements when [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)<br> is `collapse`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | as each of the properties of the shorthand:  <br><br>*   [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)<br>    : refer to the size of the border image<br>*   [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)<br>    : refer to the width or height of the border image area |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)<br>    : `none` or the image with its URI made absolute<br>*   [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)<br>    : one to four percentage(s) (as specified) or absolute length(s), plus the keyword `fill` if specified<br>*   [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)<br>    : as specified, but with relative lengths converted into absolute lengths<br>*   [`border-image-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)<br>    : as specified, but with relative lengths converted into absolute lengths<br>*   [`border-image-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)<br>    : discrete<br>*   [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)<br>    : by computed value type<br>*   [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)<br>    : by computed value type<br>*   [`border-image-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)<br>    : by computed value type<br>*   [`border-image-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)<br>    : discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#formal_syntax)

------------------------------------------------------------------------------------------------------------------

border-image =   
  [<'border-image-source'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
                             [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'border-image-slice'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / [<'border-image-width'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 / [<'border-image-width'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 / [<'border-image-outset'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'border-image-repeat'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
                               
  
[<border-image-source>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
 =   
  none     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image>    
  
[<border-image-slice>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  fill[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                                           
  
[<border-image-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage \[0,∞\]> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 auto [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<border-image-outset>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<border-image-repeat>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 stretch [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 repeat [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 round [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 space [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-set()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cross-fade()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <element()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<gradient>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
        
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<image()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  image( <image-tags>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image-src>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 , [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
! )    
  
[<image-set()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
 =   
  image-set( <image-set-option>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<cross-fade()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
 =   
  cross-fade( <cf-image>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<element()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
 =   
  element( <id-selector> )    
  
<image-tags> =   
  ltr  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rtl    
  
<image-src> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
<image-set-option> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<resolution>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 type( [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<cf-image> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<id-selector> =   
  <hash-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#examples)

--------------------------------------------------------------------------------------------------------

### [Bitmap](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#bitmap)

In this example, we will apply a diamond pattern to an element's borders. The source for the border image is a ".png" file of 81 by 81 pixels, with three diamonds going vertically and horizontally:

![Eight diamonds: four red diamonds, one in each corner, and four orange diamonds, one on each side. The middle is empty.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image/border.png)

#### HTML

html

    <div id="bitmap">
      This element is surrounded by a bitmap-based border image!
    </div>
    

#### CSS

To match the size of a single diamond, we will use a value of 81 divided by 3, or `27`, for slicing the image into corner and edge regions. To center the border image on the edge of the element's background, we will make the outset values equal to half of the width values. Finally, a repeat value of `round` will make the border slices fit evenly, i.e., without clipping or gaps.

css

    #bitmap {
      width: 200px;
      background-color: #ffffaa;
      border: 36px solid orange;
      margin: 30px;
      padding: 10px;
    
      border-image: url("border.png") 27 / 36px 28px 18px 8px / 18px 14px 9px 4px
        round;
    }
    

#### Result

### [Gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#gradient)

#### HTML

html

    <div id="gradient">
      This element is surrounded by a gradient-based border image!
    </div>
    

#### CSS

css

    #gradient {
      width: 200px;
      border: 30px solid;
      border-image: repeating-linear-gradient(45deg, #ff3333, #33bbff, #ff3333 30px)
        60;
      padding: 20px;
    }
    

#### Result

### [Rounded borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#rounded_borders)

[`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 has no effect on the border image. This is because [`border-image-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
 is able to place the image outside the border box, so it doesn't make sense for the border image to be clipped by the border area. To create rounded borders when using a border image, you should create the image itself with rounded corners, or, in the case of a gradient, draw it as the background instead. Below, we show one approach to do this, which is to use two [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
s: one that extends the border box, and another for the padding box.

#### HTML

html

    <div id="rounded">
      This element is surrounded by a border image with rounded corners!
    </div>
    

#### CSS

css

    #rounded {
      width: 200px;
      /* Use transparent so the background image is visible */
      border: 10px solid transparent;
      padding: 20px;
      border-radius: 20px;
      background-image:
        linear-gradient(white, white), linear-gradient(to right, cyan, lime);
      background-origin: border-box;
      background-clip: padding-box, border-box;
    }
    

#### Result

**Note:** There is a new ``[`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip) : border-area`` value [being proposed](https://github.com/w3c/csswg-drafts/issues/9456 "External link (opens in new tab)")
 to address this use case.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# border-image](https://drafts.csswg.org/css-backgrounds/#border-image) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image#see_also)

--------------------------------------------------------------------------------------------------------

*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    
*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    
*   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    
*   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    
*   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     type
*   Gradient functions: [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
    , [`repeating-conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)
    , [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
    , [`repeating-linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
    , [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
    , [`repeating-radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
    
*   [Border images in CSS: A key focus area for Interop 2023](https://developer.mozilla.org/en-US/blog/border-images-interop-2023/)
     on MDN blog (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-image/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-image (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")