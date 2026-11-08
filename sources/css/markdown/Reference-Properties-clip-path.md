*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#mdn-search)
    

`clip-path` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`clip-path`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property creates a clipping region that sets what part of an element should be shown. Parts that are inside the region are shown, while those outside are hidden.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#try_it)

-------------------------------------------------------------------------------------------------

    clip-path: circle(40%);
    

    clip-path: ellipse(130px 140px at 10% 20%);
    

    clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);
    

    clip-path: path("M 0 200 L 0,75 A 5,5 0,0,1 150,75 L 200 200 z");
    

    clip-path: rect(5px 145px 160px 5px round 20%);
    

    clip-path: xywh(0 5px 100% 75% round 15% 0);
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <img
          class="transition-all"
          id="example-element"
          src="/shared-assets/images/examples/balloon-small.jpg"
          width="150" />
        We had agreed, my companion and I, that I should call for him at his house,
        after dinner, not later than eleven o'clock. This athletic young Frenchman
        belongs to a small set of Parisian sportsmen, who have taken up "ballooning"
        as a pastime. After having exhausted all the sensations that are to be found
        in ordinary sports, even those of "automobiling" at a breakneck speed, the
        members of the "Aéro Club" now seek in the air, where they indulge in all
        kinds of daring feats, the nerve-racking excitement that they have ceased to
        find on earth.
      </div>
    </section>
    

    section {
      align-items: flex-start;
    }
    
    .example-container {
      text-align: left;
      padding: 20px;
    }
    
    #example-element {
      float: left;
      width: 150px;
      margin: 20px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#syntax)

-------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    clip-path: none;
    
    /* <clip-source> values */
    clip-path: url("resources.svg#c1");
    
    /* <geometry-box> values */
    clip-path: margin-box;
    clip-path: border-box;
    clip-path: padding-box;
    clip-path: content-box;
    clip-path: fill-box;
    clip-path: stroke-box;
    clip-path: view-box;
    
    /* <basic-shape> values */
    clip-path: inset(100px 50px);
    clip-path: circle(50px at 0 100px);
    clip-path: ellipse(50px 60px at 10% 20%);
    clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
    clip-path: path(
      "M0.5,1 C0.5,1,0,0.7,0,0.3 A0.25,0.25,1,1,1,0.5,0.3 A0.25,0.25,1,1,1,1,0.3 C1,0.7,0.5,1,0.5,1 Z"
    );
    clip-path: rect(5px 5px 160px 145px round 20%);
    clip-path: shape(from 0% 0%, line to 100% 0%, line to 50% 100%, close);
    clip-path: xywh(0 5px 100% 75% round 15% 0);
    
    /* Box and shape values combined */
    clip-path: padding-box circle(50px at 0 100px);
    
    /* Global values */
    clip-path: inherit;
    clip-path: initial;
    clip-path: revert;
    clip-path: revert-layer;
    clip-path: unset;
    

The `clip-path` property is specified as one or a combination of the values listed below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#values)

[`<clip-source>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#clip-source)

A [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 referencing an [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
 element.

[`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)

A shape whose size and position is defined by the `<geometry-box>` value. If no geometry box is specified, the `border-box` will be used as the reference box. One of:

[`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)

Defines an inset rectangle.

[`circle()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/circle)

Defines a circle using a radius and a position.

[`ellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/ellipse)

Defines an ellipse using two radii and a position.

[`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)

Defines a polygon using an SVG filling rule and a set of vertices.

[`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)

Defines a shape using an optional SVG filling rule and an SVG path definition.

[`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)

Defines a rectangle using the specified distances from the edges of the reference box.

[`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)

Defines a shape using an optional SVG filling rule and shape commands for lines, curves, and arcs.

[`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)

Defines a rectangle using the specified distances from the top and left edges of the reference box and the specified width and height of the rectangle.

[`<geometry-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#geometry-box)

If specified in combination with a `<basic-shape>`, this value defines the reference box for the basic shape. If specified by itself, it causes the edges of the specified box, including any corner shaping (such as a [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
), to be the clipping path. The geometry box can be one of the following values:

[`margin-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#margin-box)

Uses the [margin box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_box_values#margin-box)
 as the reference box.

[`border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#border-box)

Uses the [border box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_box_values#border-box)
 as the reference box.

[`padding-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#padding-box)

Uses the [padding box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_box_values#padding-box)
 as the reference box.

[`content-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#content-box)

Uses the [content box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_box_values#content-box)
 as the reference box.

[`fill-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#fill-box)

Uses the object bounding box as the reference box.

[`stroke-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#stroke-box)

Uses the stroke bounding box as the reference box.

[`view-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#view-box)

Uses the nearest SVG viewport as the reference box. If a [`viewBox`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)
 attribute is specified for the element creating the SVG viewport, the reference box is positioned at the origin of the coordinate system established by the `viewBox` attribute and the dimension of the size of the reference box is set to the width and height values of the `viewBox` attribute.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#none)

No clipping path is created.

**Note:** A computed value other than **`none`** results in the creation of a new [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
 the same way that CSS [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 does for values other than `1`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to reference box when specified, otherwise border-box |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)<br> values made absolute |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | yes, as specified for [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)<br>, otherwise no |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#formal_syntax)

---------------------------------------------------------------------------------------------------------------

clip-path =   
  <clip-source>                        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <basic-shape> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <geometry-box> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                                   
  
<clip-source> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    
  
[<basic-shape>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 =   
  <basic-shape-rect>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <circle()>          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <ellipse()>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <polygon()>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <path()>            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <shape()>             
  
<geometry-box> =   
  <shape-box>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fill-box     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stroke-box   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  view-box       
  
<basic-shape-rect> =   
  <inset()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <rect()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <xywh()>     
  
[<circle()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/circle)
 =   
  circle( <radial-size>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 at <position> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<ellipse()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/ellipse)
 =   
  ellipse( <radial-size>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 at <position> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<polygon()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
 =   
  polygon( [<'fill-rule'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 round [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<path()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
 =   
  path( [<'fill-rule'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 )    
  
[<shape()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape)
 =   
  shape( [<'fill-rule'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 from <position> , <shape-command>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<shape-box> =   
  <visual-box>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  margin-box       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  half-border-box    
  
[<inset()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
 =   
  inset( <length-percentage>[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 round [<'border-radius'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<rect()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
 =   
  rect( <top> , <right> , <bottom> , <left> )    
  
[<xywh()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
 =   
  xywh( <length-percentage>[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 <length-percentage \[0,∞\]>[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 round [<'border-radius'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<radial-size> =   
  <radial-extent>               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage \[0,∞\]>[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
 =   
  <position-one>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <position-two>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <position-four>    
  
[<fill-rule>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
 =   
  nonzero  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  evenodd    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
<shape-command> =   
  <move-command>             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <line-command>             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  close                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <horizontal-line-command>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <vertical-line-command>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <curve-command>            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <smooth-command>           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <arc-command>                
  
<visual-box> =   
  content-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  padding-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  border-box     
  
[<border-radius>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 =   
  <length-percentage \[0,∞\]>[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <length-percentage \[0,∞\]>[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<radial-extent> =   
  closest-corner   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  closest-side     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  farthest-corner  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  farthest-side      
  
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
            
  
<move-command> =   
  move <command-end-point>    
  
<line-command> =   
  line <command-end-point>    
  
<horizontal-line-command> =   
  hline [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 to [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 by <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<vertical-line-command> =   
  vline [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 to [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 by <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<curve-command> =   
  curve [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 to <position> with <control-point> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <control-point> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 by <coordinate-pair> with <relative-control-point> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <relative-control-point> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<smooth-command> =   
  smooth [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 to <position> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 with <control-point> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 by <coordinate-pair> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 with <relative-control-point> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<arc-command> =   
  arc <command-end-point> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 of <length-percentage>[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 <arc-sweep>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 <arc-size>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 rotate [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<command-end-point> =   
  to <position>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  by <coordinate-pair>    
  
<control-point> =   
  <position>                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <relative-control-point>    
  
<coordinate-pair> =   
  <length-percentage>[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
<relative-control-point> =   
  <coordinate-pair> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 from [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 origin [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<arc-sweep> =   
  cw   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ccw    
  
<arc-size> =   
  large  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  small    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#examples)

-----------------------------------------------------------------------------------------------------

### [Shapes and geometry boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#shapes_and_geometry_boxes)

In this example, two triangles are created by defining a `polygon()` as the clip path on [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements. Each one has a solid colored background and a thick [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
. The second `<div>` element has its reference box set to `content-box`:

#### HTML

html

    <div></div>
    <div></div>
    

#### CSS

    body {
      display: flex;
      gap: 20px;
      flex-flow: row wrap;
    }
    

css

    div {
      height: 200px;
      width: 200px;
      box-sizing: border-box;
      background-color: rebeccapurple;
      border: 20px solid magenta;
    
      clip-path: polygon(50% 0, 100% 100%, 0 100%);
    }
    
    div:last-of-type {
      clip-path: content-box polygon(50% 0, 100% 100%, 0 100%);
    }
    

#### Results

For the first triangle, we didn't specify a reference box; it therefore defaults to `border-box`, with the 0% and 100% positions located on the outside edge of the border. In the second example, we set the `<geometry-box>` to `content-box`, meaning the reference box for the basic shape is the outer edge of the content area, which is inside the padding box. Because our example has no `padding`, this is the inner edge of the border.

### [`shape()` versus `path()` functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#shape_versus_path_functions)

Expanding on the previous example, we create the same triangle with different `<basic-shape>` values, demonstrating how the [`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)
 and [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
 functions can also be used to create clipping paths, with `shape()` being a more flexible solution.

We use `path()` to define the first element's clipping path, and `shape()` for the second, both using the default `border-box` as their reference box:

css

    div {
      clip-path: path("M100 0 L200 200 L0 200 Z");
    }
    
    div:last-of-type {
      clip-path: shape(from 50% 0, line to 100% 100%, line to 0 100%, close);
    }
    

As a result, the path defined with the shape() function grows with the element, whereas the path() version does not:

Because the `shape()` function allows using [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values (and [custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 too), it is more robust.

We'll demonstrate this by increasing the size of the underlying element:

css

    div {
      width: 250px;
      height: 250px;
    }
    

The visibility, or at least partial visibility, of the four border sides in the clip path example defined by the `shape()` function is due to the percentage values allowing the path to grow with the element. In the `path()` version, the element grew, but not the shape. As a result, the top and left borders are partially visible while the right and bottom borders are clipped out.

### [SVG as clip source](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#svg_as_clip_source)

In this example, we define SVG [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
 elements to use as a `clip-path` source.

#### HTML

We include two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements and an `<svg>` element containing two `<clipPath>` elements. One `<clipPath>` contains four [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 elements that together define window panes, leaving a cross of blank space in the middle, and the other contains two crossing `<rect>` elements.

html

    <svg height="0" width="0">
      <defs>
        <clipPath id="window">
          <rect y="0" x="0" width="80" height="80" />
          <rect y="0" x="120" width="80" height="80" />
          <rect y="120" x="0" width="80" height="80" />
          <rect y="120" x="120" width="80" height="80" />
        </clipPath>
        <clipPath id="cross">
          <rect y="0" x="80" width="40" height="200" />
          <rect y="80" x="0" width="200" height="40" />
        </clipPath>
      </defs>
    </svg>
    
    <div class="window">Window</div>
    <div class="cross">Cross</div>
    

#### CSS

We use [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 to allow our elements to sit side-by-side with a gap between them, if there is space available. We define a [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
 background image on both `<div>` elements, providing an interesting visual to clip, along with a [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
.

css

    body {
      display: flex;
      gap: 20px;
      flex-flow: row wrap;
      font: 2em sans-serif;
    }
    
    div {
      width: 200px;
      height: 200px;
      background-image: conic-gradient(
        at center,
        rebeccapurple,
        green,
        lightblue,
        rebeccapurple
      );
    
      border: 5px solid;
      box-sizing: border-box;
    }
    

We then set the `id` of the `<clipPath>` as the `<clip-source>`. We center the text in the `cross` example vertically using [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
, as otherwise the text would be clipped, as is happening in the `window` example.

css

    .window {
      clip-path: url("#window");
    }
    
    .cross {
      clip-path: url("#cross");
      align-content: center;
    }
    

#### Results

The elements, including their border and text, are clipped, with only the parts overlapping the `<clipPath>` elements being drawn to the page.

### [The various value types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#the_various_value_types)

This example demonstrates the various values of the `clip-path` property clipping an HTML [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
.

#### HTML

The HTML includes an `<img>` that will be clipped, a star-shaped `<clipPath>`, and a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element to choose a `clip-path` property value from.

html

    <img
      id="clipped"
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <svg height="0" width="0">
      <defs>
        <clipPath id="star">
          <path d="M100,0 42,180 196,70 4,70 158,180z" />
        </clipPath>
      </defs>
    </svg>
    
    <select id="clipPath">
      <option value="none">none</option>
      <option value="circle(100px at 110px 100px)">circle</option>
      <option value="url(#star)" selected>star</option>
      <option value="inset(20px round 20px)">inset</option>
      <option value="rect(20px 150px 200px 20px round 10%)">rect</option>
      <option value="xywh(0 20% 90% 67% round 0 0 5% 5px)">xywh</option>
      <option value="path('M 0 200 L 0,110 A 110,90 0,0,1 240,100 L 200 340 z')">
        path
      </option>
    </select>
    

    <pre id="log"></pre>
    

#### CSS

The initial rendering includes the star as the `clip-path` source.

css

    #clipped {
      margin-bottom: 20px;
      clip-path: url("#star");
    }
    

#### JavaScript

When you select a new option from the `<select>` menu, an event handler updates the value of the `clip-path` set on the `<img>`.

js

    const clipPathSelect = document.getElementById("clipPath");
    clipPathSelect.addEventListener("change", (evt) => {
      const path = evt.target.value;
      document.getElementById("clipped").style.clipPath = path;
      log(`clip-path: ${path};`);
    });
    

    function log(text) {
      const logElement = document.querySelector("#log");
      logElement.innerText = `${text}`;
      logElement.scrollTop = logElement.scrollHeight;
    }
    

#### Result

Select different options to change the `clip-path` value.

**Note:** While it is possible to define a path of text, if you want to clip a background image to text rather than a shape, see the [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
 property.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# propdef-clip-path](https://drafts.csswg.org/css-masking/#propdef-clip-path) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path#see_also)

-----------------------------------------------------------------------------------------------------

*   [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
    
*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
    
*   [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
    
*   [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    
*   [Introduction to CSS clipping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module
*   SVG [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/clip-path)
     attribute
*   [Applying SVG effects to HTML content](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Applying_SVG_effects_to_HTML_content)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/clip-path/index.md?plain=1 "Folder: en-us/web/css/reference/properties/clip-path (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fclip-path&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fclip-path%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fclip-path%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fclip-path%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")