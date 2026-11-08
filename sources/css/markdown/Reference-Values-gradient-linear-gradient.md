*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#mdn-search)
    

`linear-gradient()` CSS function
================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`linear-gradient()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 creates an image consisting of a progressive transition between two or more colors along a straight line. Its result is an object of the [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
 data type, which is a special kind of [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#try_it)

------------------------------------------------------------------------------------------------------------

    background: linear-gradient(#e66465, #9198e5);
    

    background: linear-gradient(0.25turn, #3f87a6, #ebf8e1, #f69d3c);
    

    background: linear-gradient(
      to left,
      #333333,
      #333333 50%,
      #eeeeee 75%,
      #333333 75%
    );
    

    background:
      linear-gradient(217deg, rgb(255 0 0 / 0.8), transparent 70.71%),
      linear-gradient(127deg, rgb(0 255 0 / 0.8), transparent 70.71%),
      linear-gradient(336deg, rgb(0 0 255 / 0.8), transparent 70.71%);
    

    <section class="display-block" id="default-example">
      <div id="example-element"></div>
    </section>
    

    #example-element {
      min-height: 100%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* A gradient with a single color of red */
    linear-gradient(red)
    
    /* A gradient tilted 45 degrees,
       starting blue and finishing red */
    linear-gradient(45deg, blue, red)
    
    /* A gradient going from the bottom right to the top left corner,
       starting blue and finishing red */
    linear-gradient(to left top, blue, red)
    
    /* Interpolation in rectangular color space */
    linear-gradient(in oklab, blue, red)
    
    /* Interpolation in polar color space */
    linear-gradient(in hsl, blue, red)
    
    /* Interpolation in polar color space
      with longer hue interpolation method */
    linear-gradient(in hsl longer hue, blue, red)
    
    /* Color stop: A gradient going from the bottom to top,
       starting blue, turning green at 40% of its length,
       and finishing red */
    linear-gradient(0deg, blue, green 40%, red)
    
    /* Color hint: A gradient going from the left to right,
       starting red, getting to the midpoint color
       10% of the way across the length of the gradient,
       taking the rest of the 90% of the length to change to blue */
    linear-gradient(.25turn, red, 10%, blue)
    
    /* Multi-position color stop: A gradient tilted 45 degrees,
       with a red bottom-left half and a blue top-right half,
       with a hard line where the gradient changes from red to blue */
    linear-gradient(45deg, red 0 50%, blue 50% 100%)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#values)

[`<side-or-corner>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#side-or-corner)

The position of the gradient line's starting point. If specified, it consists of the word `to` and up to two keywords: one indicates the horizontal side (`left` or `right`), and the other the vertical side (`top` or `bottom`). The order of the side keywords does not matter. If unspecified, it defaults to `to bottom`.

The values `to top`, `to bottom`, `to left`, and `to right` are equivalent to the angles `0deg`, `180deg`, `270deg`, and `90deg`, respectively. The other values are translated into an angle.

[`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)

The gradient line's angle of direction. A value of `0deg` is equivalent to `to top`; increasing values rotate clockwise from there.

[`<linear-color-stop>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#linear-color-stop)

A color-stop's [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value, followed by one or two optional stop positions, (each being either a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 or a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 along the gradient's axis).

[`<color-hint>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#color-hint)

An [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 hint defining how the gradient progresses between adjacent color stops. The length defines at which point between two color stops the gradient color should reach the midpoint of the color transition. If omitted, the midpoint of the color transition is the midpoint between two color stops.

**Note:** Rendering of [color stops in CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#composition_of_a_linear_gradient)
 follows the same rules as color stops in [SVG gradients](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Gradients)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#description)

----------------------------------------------------------------------------------------------------------------------

As with any gradient, a linear gradient has [no intrinsic dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image#description)
; i.e., it has no natural or preferred size, nor a preferred ratio. Its concrete size will match the size of the element it applies to.

To create a linear gradient that repeats to fill its container, use the [`repeating-linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
 function instead.

Because `<gradient>`s belong to the `<image>` data type, they can only be used where [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
s can be used. For this reason, `linear-gradient()` won't work on [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 and other properties that use the [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 data type.

### [Composition of a linear gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#composition_of_a_linear_gradient)

A linear gradient is defined by an axis—the _gradient line_—and two or more _color-stop points_. Each point on the axis is a distinct color; to create a smooth gradient, the `linear-gradient()` function draws a series of colored lines perpendicular to the gradient line, each one matching the color of the point where it intersects the gradient line.

![linear-gradient.png](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient/linear-gradient.png)

The gradient line is defined by the center of the box containing the gradient image and by an angle. The colors of the gradient are determined by two or more points: the starting point, the ending point, and, in between, optional color-stop points.

The _starting point_ is the location on the gradient line where the first color begins. The _ending point_ is the point where the last color ends. Each of these two points is defined by the intersection of the gradient line with a perpendicular line passing from the box corner which is in the same quadrant. The ending point can be understood as the symmetrical point of the starting point. These somewhat complex definitions lead to an interesting effect sometimes called _magic corners_: the corners nearest to the starting and ending points have the same color as their respective starting or ending points.

#### Customizing Gradients

By adding more color-stop points on the gradient line, you can create a highly customized transition between multiple colors. A color-stop's position can be explicitly defined by using a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
. If you don't specify the location of a color, it is placed halfway between the one that precedes it and the one that follows it. The following two gradients are equivalent.

css

    linear-gradient(red, orange, yellow, green, blue);
    linear-gradient(red 0%, orange 25%, yellow 50%, green 75%, blue 100%);
    

By default, colors transition smoothly from the color at one color-stop to the color at the subsequent color-stop, with the midpoint between the colors being the halfway point between the color transition. You can move this midpoint to any position between two color-stops by adding an unlabeled % color hint between the two colors to indicate where the middle of the color transition should be. The following example is solid red from the start to the 10% mark and solid blue from 90% to the end. Between 10% and 90% the color transitions from red to blue, however, the midpoint of the transition is at the 30% mark rather than 50% as would have happened without the 30% color hint.

css

    linear-gradient(red 10%, 30%, blue 90%);
    

If two or more color-stops are at the same location, the transition will be a hard line between the first and last colors declared at that location.

Color-stops should be listed in ascending order. Subsequent color-stops of lower value will override the value of the previous color-stop creating a hard transition. The following changes from red to yellow at the 40% mark, and then transitions from yellow to blue over 25% of the gradient:

css

    linear-gradient(red 40%, yellow 30%, blue 65%);
    

Multi-position color-stops are allowed. A color can be declared as two adjacent color-stops by including both positions in the CSS declaration. The following three gradients are equivalent:

css

    linear-gradient(red 0%, orange 10%, orange 30%, yellow 50%, yellow 70%, green 90%, green 100%);
    linear-gradient(red, orange 10% 30%, yellow 50% 70%, green 90%);
    linear-gradient(red 0%, orange 10% 30%, yellow 50% 70%, green 90% 100%);
    

By default, if there is no color with a `0%` stop, the first color declared will be at that point. Similarly, the last color will continue to the `100%` mark, or be at the `100%` mark if no length has been declared on that last stop.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

<linear-gradient()> =   
  linear-gradient( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <linear-gradient-syntax> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
<linear-gradient-syntax> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 to <side-or-corner> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <color-interpolation-method> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <color-stop-list>    
  
<side-or-corner> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
[<color-interpolation-method>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
 =   
  in [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <rectangular-color-space> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <polar-color-space> <hue-interpolation-method>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <custom-color-space> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<color-stop-list> =   
  <linear-color-stop> , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <linear-color-hint>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 , <linear-color-stop> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<rectangular-color-space> =   
  srgb               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  srgb-linear        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  display-p3         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  display-p3-linear  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  a98-rgb            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  prophoto-rgb       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rec2020            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  lab                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  oklab              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <xyz-space>          
  
<polar-color-space> =   
  hsl    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hwb    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  lch    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  oklch    
  
[<hue-interpolation-method>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 shorter [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 longer [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 increasing [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 decreasing [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 hue    
  
<custom-color-space> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
  
<linear-color-stop> =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 <color-stop-length>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<linear-color-hint> =   
  <length-percentage>    
  
<xyz-space> =   
  xyz      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d50  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d65    
  
<color-stop-length> =   
  <length-percentage>[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#examples)

----------------------------------------------------------------------------------------------------------------

### [Gradient at a 45-degree angle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#gradient_at_a_45-degree_angle)

    body {
      width: 100vw;
      height: 100vh;
    }
    

css

    body {
      background: linear-gradient(45deg, red, blue);
    }
    

### [Gradient that starts at 60% of the gradient line](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#gradient_that_starts_at_60_of_the_gradient_line)

    body {
      width: 100vw;
      height: 100vh;
    }
    

css

    body {
      background: linear-gradient(135deg, orange 60%, cyan);
    }
    

### [Interpolation in rectangular color space](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#interpolation_in_rectangular_color_space)

    body {
      width: 100vw;
      height: 100vh;
    }
    

css

    body {
      background: linear-gradient(90deg in oklab, blue, red);
    }
    

### [Interpolating with hue](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#interpolating_with_hue)

    <div class="shorter">shorter hue</div>
    <div class="longer">longer hue</div>
    

    div {
      height: 50vh;
      color: white;
      font-weight: bolder;
    }
    

In this example for interpolation, [hsl](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
 color system is being used and [hue](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
 is being interpolated.

css

    .shorter {
      background: linear-gradient(90deg in hsl shorter hue, red, blue);
    }
    
    .longer {
      background: linear-gradient(90deg in hsl longer hue, red, blue);
    }
    

The box on the top uses [shorter interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#shorter)
, meaning color goes straight from red to blue using the shorter arc on [color wheel](https://developer.mozilla.org/en-US/docs/Glossary/Color_wheel)
. The box on the bottom uses [longer interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#longer)
, meaning the color goes from red to blue using the longer arc, traversing through greens, yellows, and oranges.

### [Gradient with multi-position color-stops](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#gradient_with_multi-position_color-stops)

This example uses multi-position color-stops, with adjacent colors having the same color-stop value, creating a striped effect.

    body {
      width: 100vw;
      height: 100vh;
    }
    

css

    body {
      background: linear-gradient(
        to right,
        red 20%,
        orange 20% 40%,
        yellow 40% 60%,
        green 60% 80%,
        blue 80%
      );
    }
    

### [More linear-gradient examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#more_linear-gradient_examples)

Please see [using CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
 for more examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 3  <br>\# funcdef-linear-gradient](https://drafts.csswg.org/css-images-3/#funcdef-linear-gradient) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Using CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
    
*   Other gradient functions: [`repeating-linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
    , [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
    , [`repeating-radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
    , [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
    , [`repeating-conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)
    
*   [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
    
*   [`<color-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
    
*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [CSS images module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/gradient/linear-gradient/index.md?plain=1 "Folder: en-us/web/css/reference/values/gradient/linear-gradient (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fgradient%2Flinear-gradient&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fgradient%2Flinear-gradient%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fgradient%2Flinear-gradient%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fgradient%2Flinear-gradient%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F11a5944cd0a3bf015b2ee9c7ee4c55025dd878ca%0A*+Document+last+modified%3A+2026-08-28T11%3A00%3A42.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")