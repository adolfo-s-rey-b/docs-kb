*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#mdn-search)
    

`repeating-linear-gradient()` CSS function
==========================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`repeating-linear-gradient()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 creates an image consisting of repeating linear gradients. It is similar to [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
 and takes the same arguments, but it repeats the color stops infinitely in all directions so as to cover its entire container. The function's result is an object of the [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
 data type, which is a special kind of [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#try_it)

----------------------------------------------------------------------------------------------------------------------

    background: repeating-linear-gradient(
      #e66465,
      #e66465 20px,
      #9198e5 20px,
      #9198e5 25px
    );
    

    background: repeating-linear-gradient(45deg, #3f87a6, #ebf8e1 15%, #f69d3c 20%);
    

    background:
      repeating-linear-gradient(transparent, #4d9f0c 40px),
      repeating-linear-gradient(0.25turn, transparent, #3f87a6 20px);
    

    <section class="display-block" id="default-example">
      <div id="example-element"></div>
    </section>
    

    #example-element {
      min-height: 100%;
    }
    

The length of the gradient that repeats is the distance between the first and last color stop. If the first color does not have a color-stop-length, the color-stop-length defaults to 0. With each repetition, the positions of the color stops are shifted by a multiple of the length of the basic linear gradient. Thus, the position of each ending color stop coincides with a starting color stop; if the color values are different, this will result in a sharp visual transition. This can be altered with repeating the first color again as the last color.

As with any gradient, a repeating linear gradient has [no intrinsic dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image#description)
; i.e., it has no natural or preferred size, nor a preferred ratio. Its concrete size will match the size of the element it applies to.

Because `<gradient>`s belong to the `<image>` data type, they can only be used where `<image>`s can be used. For this reason, `repeating-linear-gradient()` won't work on [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 and other properties that use the [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 data type.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#syntax)

----------------------------------------------------------------------------------------------------------------------

css

    /* A repeating gradient tilted 45 degrees,
       starting blue and finishing red, repeating 3 times */
    repeating-linear-gradient(45deg, blue, red 33.3%)
    
    /* A repeating gradient going from the bottom right to the top left,
       starting blue and finishing red, repeating every 20px */
    repeating-linear-gradient(to left top, blue, red 20px)
    
    /* A gradient going from the bottom to top,
       starting blue, turning green after 40%,
       and finishing red. This gradient doesn't repeat because
       the last color stop defaults to 100% */
    repeating-linear-gradient(0deg, blue, green 40%, red)
    
    /* A gradient repeating five times, going from the left to right,
       starting red, turning green, and back to red */
    repeating-linear-gradient(to right, red 0%, green 10%, red 20%)
    
    /* Interpolation in rectangular color space */
    repeating-linear-gradient(in oklab, blue, red 50px)
    
    /* Interpolation in polar color space */
    repeating-linear-gradient(in hsl, blue, red 50px)
    
    /* Interpolation in polar color space
      with longer hue interpolation method */
    repeating-linear-gradient(in hsl longer hue, blue, red 50px)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#values)

[`<side-or-corner>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#side-or-corner)

The position of the gradient line's starting point. If specified, it consists of the word `to` and up to two keywords: one indicates the horizontal side (`left` or `right`), and the other the vertical side (`top` or `bottom`). The order of the side keywords does not matter. If unspecified, it defaults to `to bottom`.

The values `to top`, `to bottom`, `to left`, and `to right` are equivalent to the angles `0deg`, `180deg`, `270deg`, and `90deg` respectively. The other values are translated into an angle.

[`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)

The gradient line's angle of direction. A value of `0deg` is equivalent to `to top`; increasing values rotate clockwise from there.

[`<linear-color-stop>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#linear-color-stop)

A color-stop's [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value, followed by one or two optional stop positions, (each being either a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 or a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 along the gradient's axis). A percentage of `0%`, or a length of `0`, represents the start of the gradient; the value `100%` is 100% of the image size, meaning the gradient will not repeat.

[`<color-hint>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#color-hint)

The color-hint is an interpolation hint defining how the gradient progresses between adjacent color stops. The length defines at which point between two color stops the gradient color should reach the midpoint of the color transition. If omitted, the midpoint of the color transition is the midpoint between two color stops.

**Note:** Rendering of color stops in repeating linear gradients follows the same rules as [color stops in linear gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient#composition_of_a_linear_gradient)
.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#formal_syntax)

------------------------------------------------------------------------------------------------------------------------------------

<repeating-linear-gradient()> =   
  repeating-linear-gradient( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#examples)

--------------------------------------------------------------------------------------------------------------------------

### [Zebra stripes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#zebra_stripes)

    body {
      width: 100vw;
      height: 100vh;
    }
    

css

    body {
      background-image: repeating-linear-gradient(
        -45deg,
        transparent,
        transparent 20px,
        black 20px,
        black 40px
      );
      /* with multiple color stop lengths */
      background-image: repeating-linear-gradient(
        -45deg,
        transparent 0 20px,
        black 20px 40px
      );
    }
    

### [Ten repeating horizontal bars](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#ten_repeating_horizontal_bars)

    body {
      width: 100vw;
      height: 100vh;
    }
    

css

    body {
      background-image: repeating-linear-gradient(
        to bottom,
        rgb(26 198 204),
        rgb(26 198 204) 7%,
        rgb(100 100 100) 10%
      );
    }
    

Because the last color stop is 10% and the gradient is vertical, each gradient in the repeated gradient is 10% of the height, fitting 10 horizontal bars.

### [Interpolation in rectangular color space](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#interpolation_in_rectangular_color_space)

    body {
      width: 100vw;
      height: 100vh;
    }
    

css

    body {
      background: repeating-linear-gradient(90deg in oklab, blue, red 100px);
    }
    

### [Interpolating with hue](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#interpolating_with_hue)

    <div class="shorter">shorter hue</div>
    <div class="longer">longer hue</div>
    

    div {
      height: 50vh;
      color: #333300;
      font-weight: bolder;
      padding-left: 1.5rem;
    }
    

In this example for interpolation, [hsl](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
 color system is being used and [hue](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
 is being interpolated.

css

    .shorter {
      background: repeating-linear-gradient(
        90deg in hsl shorter hue,
        red,
        blue 300px
      );
    }
    
    .longer {
      background: repeating-linear-gradient(
        90deg in hsl longer hue,
        red,
        blue 300px
      );
    }
    

The box on the top uses [shorter interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#shorter)
, meaning the color goes from red to blue using the shorter arc on the [color wheel](https://developer.mozilla.org/en-US/docs/Glossary/Color_wheel)
. The box on the bottom uses [longer interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method#longer)
, meaning the color goes from red to blue using the longer arc, traversing through greens, yellows, and oranges.

**Note:** Please see [Using CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
 for more examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#specifications)

--------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 3  <br>\# repeating-gradients](https://drafts.csswg.org/css-images/#repeating-gradients) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient#see_also)

--------------------------------------------------------------------------------------------------------------------------

*   [Using CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
    
*   Other gradient functions: [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
    , [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
    , [`repeating-radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
    , [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
    , [`repeating-conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)
    
*   [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
    
*   [`<color-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
    
*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [`image()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image)
    
*   [`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
    
*   [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
    
*   [`cross-fade()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/gradient/repeating-linear-gradient/index.md?plain=1 "Folder: en-us/web/css/reference/values/gradient/repeating-linear-gradient (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fgradient%2Frepeating-linear-gradient&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fgradient%2Frepeating-linear-gradient%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fgradient%2Frepeating-linear-gradient%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fgradient%2Frepeating-linear-gradient%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")