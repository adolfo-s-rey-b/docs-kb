*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#mdn-search)
    

`stroke` CSS property
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`stroke`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the color or SVG paint server used to draw an element's stroke. As such, `stroke` only has an effect on elements that can be given a stroke (for example, [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 or [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)
); see the page on the SVG [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
 attribute for a complete list. When declared, the CSS value overrides any value of the element's [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
 SVG attribute.

**Note:** According to the 4 April 2017 draft of the [CSS Fill and Stroke Module Level 3](https://drafts.csswg.org/fill-stroke-3/#stroke-shorthand "External link (opens in new tab)")
 specification, the `stroke` property is a shorthand for a number of other stroke properties. In practice, as of August 2024, browsers do not support the setting of other stroke-related values such as width or dash patterns via the `stroke` property, treating it instead as a direct analogue of the SVG [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
 attribute.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#syntax)

----------------------------------------------------------------------------------------------

css

    /* assorted color values */
    stroke: rgb(153 51 102 / 1);
    stroke: color-mix(in lch, var(--primaryColor) 35%, gray 15%);
    stroke: dodgerblue;
    stroke: currentColor;
    stroke: transparent;
    stroke: context-stroke;
    
    /* Global values */
    stroke: inherit;
    stroke: initial;
    stroke: revert;
    stroke: revert-layer;
    stroke: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#values)

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

Sets the painting of the stroke with any valid CSS color value.

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#image)

Sets the painting of the stroke with what SVG calls a [_paint server_](https://w3c.github.io/svgwg/svg2-draft/pservers.html "External link (opens in new tab)")
, which in this context is an SVG gradient or pattern. CSS gradients cannot be used with the `stroke` property.

[`context-stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#context-stroke)

Causes an element to "inherit" its stroke definition from its [_context element_](https://w3c.github.io/svgwg/svg2-draft/painting.html#TermContextElement "External link (opens in new tab)")
. If there is no valid context element, then this value will result in no paint being used for the stroke.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#formal_definition)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray)<br>    : `none`<br>*   [`stroke-dashoffset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)<br>    : `0`<br>*   [`stroke-linecap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)<br>    : `butt`<br>*   [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin)<br>    : `miter`<br>*   [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)<br>    : `4`<br>*   [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)<br>    : `1`<br>*   [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)<br>    : `1px` |
| Applies to | as each of the properties of the shorthand: |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand: |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray)<br>    : a repeatable list<br>*   [`stroke-dashoffset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)<br>    : by computed value type<br>*   [`stroke-linecap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)<br>    : discrete<br>*   [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin)<br>    : discrete<br>*   [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)<br>    : by computed value type<br>*   [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)<br>    : by computed value type<br>*   [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)<br>    : by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#formal_syntax)

------------------------------------------------------------------------------------------------------------

stroke =   
  <paint>    
  
[<paint>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint)
 =   
  none         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <svg-paint>    
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-set()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cross-fade()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <element()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<gradient>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
        
  
<svg-paint> =   
  child               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  child( <integer> )    
  
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
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#examples)

--------------------------------------------------------------------------------------------------

### [Basic color stroking](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#basic_color_stroking)

In this example, we create two different shapes, a circle and a rectangle, which are part of a [`<g>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/g)
 (group) that has a gray stroke color as a default for the two shapes.

html

    <svg>
      <g fill="none" stroke="gray" stroke-width="10">
        <circle cx="100" cy="100" r="40" />
        <rect x="20" y="20" width="80" height="80" />
      </g>
    </svg>
    

Via CSS, we then apply a dusky purple color to the rectangle and a red to the circle.

css

    rect {
      stroke: rebeccapurple;
    }
    circle {
      stroke: red;
    }
    

### [Pattern stroking](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#pattern_stroking)

This example uses the same group and shapes (with the circle moved over a bit) as seen in the previous example, but also has an SVG pattern defined.

html

    <svg>
      <g fill="none" stroke="gray" stroke-width="23">
        <circle cx="150" cy="90" r="40" />
        <rect x="20" y="20" width="80" height="80" />
      </g>
      <defs>
        <pattern id="star" viewBox="0,0,10,10" width="10%" height="10%">
          <polygon points="0,0 2,5 0,10 5,8 10,10 8,5 10,0 5,2" />
        </pattern>
      </defs>
    </svg>
    

The pattern is then referenced in the CSS with a URL value pointing to the ID of the pattern. This pattern is applied to both shapes as a stroking paint, with the result shown.

css

    rect,
    circle {
      stroke: url("#star");
    }
    

The pattern is drawn relative to the shapes' bounding boxes, which can lead to visual interference where they overlap, because parts of the pattern are transparent.

### [SVG versus CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#svg_versus_css_gradients)

Here, we once again use the same group-and-shapes markup as the first example, but also add a definition for an SVG gradient.

html

    <svg>
      <g fill="none" stroke="gray" stroke-width="10">
        <circle cx="100" cy="100" r="40" />
        <rect x="20" y="20" width="80" height="80" />
      </g>
      <defs>
        <linearGradient id="greenwhite">
          <stop offset="0%" stop-color="green" />
          <stop offset="100%" stop-color="white" />
        </linearGradient>
      </defs>
    </svg>
    

In the CSS, we apply that SVG gradient to the rectangle using a URL value pointing to the ID of the linear gradient. To the circle, we apply a CSS linear gradient that is equivalent in intent to the SVG gradient.

css

    rect {
      stroke: url("#greenwhite");
    }
    circle {
      stroke: linear-gradient(90deg, green, white);
    }
    

Only the rectangle receives a gradient stroke, whereas the circle falls back to the gray stroke set by the group element. This happens because CSS gradients are not valid values for the `stroke` property, whereas URL references to SVG gradients are permitted.

### [Contextual stroking](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#contextual_stroking)

In this case, we again start with a group element, inside of which two rectangle-shaped paths are defined. After that, a linear gradient and an SVG marker are defined.

html

    <svg>
      <g fill="none" stroke="gray" stroke-width="4">
        <path d="M 20,20 l 180,0 0,100 -180,0 z" />
        <path d="M 100,40 l 180,0 0,100 -180,0 z" />
      </g>
      <defs>
        <linearGradient id="orangered">
          <stop offset="0%" stop-color="orange" />
          <stop offset="100%" stop-color="red" />
        </linearGradient>
        <marker
          id="circle"
          markerWidth="20"
          markerHeight="20"
          refX="10"
          refY="10"
          markerUnits="userSpaceOnUse">
          <circle
            cx="10"
            cy="10"
            r="8"
            stroke-width="4"
            stroke="none"
            fill="none" />
        </marker>
      </defs>
    </svg>
    

We then write CSS to add a marker to both paths, and also to have a dusky purple stroke color. This is overridden for the second path, which is given a URL value to apply the orange-to-red gradient as its stroke. Finally, we set the circle element in the marker element to have a stroke value of `context-stroke`.

css

    path {
      stroke: rebeccapurple;
      marker: url("#circle");
    }
    path:nth-of-type(2) {
      stroke: url("#orangered");
    }
    marker circle {
      stroke: context-stroke;
    }
    

Because `stroke-context` is being applied to an element that descends from a [`<marker>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/marker)
 element, the context element for every circle is the element that called the `<marker>` element; that is, the [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
 elements. The result is that the markers on the first path use the color of the calling path, and are purple. The markers on the second path, by contrast, use the same orange-to-red SVG gradient the path uses. This latter case illustrates how SVG gradients are applied as a single gradient to the entire shape, rather than being applied independently to each individual part of the shape.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# StrokeProperty](https://w3c.github.io/svgwg/svg2-draft/painting.html#StrokeProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke#see_also)

--------------------------------------------------------------------------------------------------

*   [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray)
    
*   [`stroke-dashoffset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)
    
*   [`stroke-linecap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)
    
*   [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin)
    
*   [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
    
*   [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)
    
*   [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
    
*   [`paint-order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order)
    
*   SVG [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/stroke/index.md?plain=1 "Folder: en-us/web/css/reference/properties/stroke (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstroke&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstroke%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstroke%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstroke%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")