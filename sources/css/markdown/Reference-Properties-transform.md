*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#mdn-search)
    

`transform` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transform`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property lets you rotate, scale, skew, or translate an element. It modifies the coordinate space of the CSS [visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
.

If the property has a value different from `none`, a [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
 will be created. In that case, the element will act as a [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 for any `position: fixed;` or `position: absolute;` elements that it contains.

You can also use the individual transform properties: [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
, [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
, and [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
. These properties are applied in the order: `translate`, `rotate`, `scale`, and finally `transform`.

**Warning:** Only transformable elements can be `transform`ed. That is, all elements whose layout is governed by the CSS box model except for: [non-replaced inline boxes](https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content)
, [table-column boxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
, and [table-column-group boxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#try_it)

-------------------------------------------------------------------------------------------------

    transform: matrix(1, 2, 3, 4, 5, 6);
    

    transform: translate(120px, 50%);
    

    transform: scale(2, 0.5);
    

    transform: rotate(0.5turn);
    

    transform: skew(30deg, 20deg);
    

    transform: scale(0.5) translate(-100%, -100%);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#syntax)

-------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    transform: none;
    
    /* Function values */
    transform: matrix(1, 2, 3, 4, 5, 6);
    transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
    transform: perspective(17px);
    transform: rotate(0.5turn);
    transform: rotate3d(1, 2, 3, 10deg);
    transform: rotateX(10deg);
    transform: rotateY(10deg);
    transform: rotateZ(10deg);
    transform: translate(12px, 50%);
    transform: translate3d(12px, 50%, 3em);
    transform: translateX(2em);
    transform: translateY(3in);
    transform: translateZ(2px);
    transform: scale(2, 0.5);
    transform: scale3d(2.5, 1.2, 0.3);
    transform: scaleX(2);
    transform: scaleY(0.5);
    transform: scaleZ(0.3);
    transform: skew(30deg, 20deg);
    transform: skewX(30deg);
    transform: skewY(1.07rad);
    
    /* Multiple function values */
    transform: translateX(10px) rotate(10deg) translateY(5px);
    transform: perspective(500px) translate3d(10px, 0, 20px) rotateY(30deg);
    
    /* Global values */
    transform: inherit;
    transform: initial;
    transform: revert;
    transform: revert-layer;
    transform: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#values)

This property is specified as either the keyword value `none` or as a space-separated list of `<transform-function>` values:

[`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)

One or more of the [CSS transform functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 to be applied. The transform functions are combined from left to right – each function establishes a new coordinate space for the next function and so on – so the visual result matches the written order of the functions. Alternatively, keeping the parent coordinate space fixed, the same transformation can be described as applying the functions in reverse order (right to left).

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#none)

Specifies that no transform should be applied.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#accessibility)

---------------------------------------------------------------------------------------------------------------

Scaling/zooming animations are problematic for accessibility, as they are a common trigger for certain types of migraine. If you need to include such animations on your website, you should provide a control to allow users to turn off animations, preferably site-wide.

Also, consider making use of the [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
 media feature — use it to write a [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
 that will turn off animations if the user has reduced animation specified in their system preferences.

Find out more:

*   [MDN Understanding WCAG, Guideline 2.3 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.3_%E2%80%94_seizures_and_physical_reactions_do_not_design_content_in_a_way_that_is_known_to_cause_seizures_or_physical_reactions)
    
*   [Understanding Success Criterion 2.3.3 | W3C Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the size of bounding box |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with relative lengths converted into absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a transform |
| Creates [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context) | yes |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#formal_syntax)

---------------------------------------------------------------------------------------------------------------

transform =   
  none              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <transform-list>    
  
<transform-list> =   
  <transform-function>[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    
  
[<transform-function>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 =   
  <scale3d()>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <scale()>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <scaleX()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <scaleY()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <scaleZ()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <translate3d()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <translate()>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <translateX()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <translateY()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <translateZ()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <rotate3d()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <rotate()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <rotateX()>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <rotateY()>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <rotateZ()>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <skew()>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <skewX()>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <skewY()>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <matrix3d()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <matrix()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <perspective()>    
  
[<scale3d()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d)
 =   
  scale3d( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    
  
[<scale()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale)
 =   
  scale( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<scaleX()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleX)
 =   
  scaleX( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 )    
  
[<scaleY()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY)
 =   
  scaleY( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 )    
  
[<scaleZ()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ)
 =   
  scaleZ( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<translate3d()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d)
 =   
  translate3d( <length-percentage> , <length-percentage> , [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 )    
  
[<translate()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate)
 =   
  translate( <length-percentage> , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<translateX()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX)
 =   
  translateX( <length-percentage> )    
  
[<translateY()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateY)
 =   
  translateY( <length-percentage> )    
  
[<translateZ()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ)
 =   
  translateZ( [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 )    
  
[<rotate3d()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d)
 =   
  rotate3d( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<rotate()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
 =   
  rotate( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<rotateX()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX)
 =   
  rotateX( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<rotateY()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateY)
 =   
  rotateY( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<rotateZ()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateZ)
 =   
  rotateZ( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<skew()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew)
 =   
  skew( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<skewX()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewX)
 =   
  skewX( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<skewY()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewY)
 =   
  skewY( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<matrix3d()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d)
 =   
  matrix3d( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{16}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    
  
[<matrix()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix)
 =   
  matrix( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{6}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    
  
[<perspective()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/perspective)
 =   
  perspective( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#examples)

-----------------------------------------------------------------------------------------------------

### [Translating and rotating an element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#translating_and_rotating_an_element)

#### HTML

html

    <div>Transformed element</div>
    

#### CSS

css

    div {
      border: solid red;
      transform: translate(30px, 20px) rotate(20deg);
      width: 140px;
      height: 60px;
    }
    

#### Result

### [Comparing the order of transform functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#comparing_the_order_of_transform_functions)

The order of transform functions matters.

In this example, two boxes are rotated and translated by the same values, but the functions are in the opposite order. The dotted lines mark the X-axis before and after rotation.

#### HTML

html

    <div class="original"></div>
    <div class="one">1</div>
    <div class="two">2</div>
    

#### CSS

    div {
      height: 200px;
      width: 200px;
      position: absolute;
      left: 200px;
      top: 50px;
      font-size: 4rem;
      line-height: 200px;
      text-align: center;
    }
    .original {
      border: 1px dashed;
    }
    .original::before,
    .original::after {
      content: "";
      position: absolute;
      top: 100px;
      width: 500px;
      left: -150px;
      height: 1px;
      border-top: 2px dotted;
    }
    .original::after {
      transform: rotate(135deg);
    }
    .one {
      background-color: #cccccc;
    }
    .two {
      background-color: #d6bb72;
    }
    

css

    .one {
      transform: translateX(200px) rotate(135deg);
    }
    .two {
      transform: rotate(135deg) translateX(200px);
    }
    

#### Result

*   Box 1 (first `translateX()`, then `rotate()`): The coordinate space first shifts `200px` along the X axis, then rotates `135deg` within that shifted space, so the element ends up to the right of its original position, rotated.
*   Box 2 (first `rotate()`, then `translateX()`): The coordinate space first rotates `135deg`, so the element then moves `200px` along the rotated axis, in the direction shown by the dotted lines. Please see [Using CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
     and [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
     for more examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# transform-functions](https://drafts.csswg.org/css-transforms-2/#transform-functions) |
| [CSS Transforms Module Level 1  <br>\# transform-property](https://drafts.csswg.org/css-transforms/#transform-property) |
| [Scalable Vector Graphics (SVG) 2  <br>\# TransformProperty](https://w3c.github.io/svgwg/svg2-draft/coords.html#TransformProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform#see_also)

-----------------------------------------------------------------------------------------------------

*   [Using CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
     data type with all the transform functions explained.
*   Individual CSS properties: [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
    , [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
    , and [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
     (there is no `skew` property).
*   SVG [`transform`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/transform)
     attribute
*   Online tool to visualize CSS Transform functions: [CSS Transform Playground](https://css-transform.moro.es/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transform/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transform (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransform&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransform%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransform%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransform%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")