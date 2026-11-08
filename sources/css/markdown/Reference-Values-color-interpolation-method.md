*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#mdn-search)
    

`<color-interpolation-method>` CSS type
=======================================

The **`<color-interpolation-method>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents the [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 used for interpolation between [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values. It can be used to override the default interpolation color space for color-related functional notations such as [`color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix)
 and [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
.

When interpolating `<color>` values, the interpolation color space defaults to Oklab.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#syntax)

--------------------------------------------------------------------------------------------------------------

The `<color-interpolation-method>` specifies whether interpolation should use a rectangular color space or a polar color space with an optional hue interpolation method:

in <rectangular-color-space>
// or
in <polar-color-space>\[ <hue-interpolation method>\]

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#values)

[`<rectangular-color-space>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#rectangular-color-space)

One of the keywords `srgb`, `srgb-linear`, `display-p3`, `a98-rgb`, `prophoto-rgb`, `rec2020`, `lab`, `oklab`, `xyz`, `xyz-d50`, or `xyz-d65`.

[`<polar-color-space>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#polar-color-space)

One of the keywords `hsl`, `hwb`, `lch`, or `oklch`.

[`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
 Optional

The algorithm for hue interpolation. It defaults to `shorter hue`.

[`<custom-color-space>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#custom-color-space)

A [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#using_with_color-profile)
 referring to a custom [@color profile](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile)
.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

<color-interpolation-method> =   
  in [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <rectangular-color-space> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <polar-color-space> <hue-interpolation-method>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <custom-color-space> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
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
    
  
<xyz-space> =   
  xyz      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d50  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d65    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#examples)

------------------------------------------------------------------------------------------------------------------

### [Comparing interpolation color spaces using gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#comparing_interpolation_color_spaces_using_gradients)

The following example shows the effect of using different interpolation color spaces for [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
.

#### HTML

html

    <div>sRGB:</div>
    <div class="gradient srgb"></div>
    <div>Oklab:</div>
    <div class="gradient oklab"></div>
    <div>Oklch (with <code>longer hue</code>):</div>
    <div class="gradient oklch-longer"></div>
    

#### CSS

css

    .gradient {
      height: 50px;
      width: 100%;
    }
    .srgb {
      background-image: linear-gradient(in srgb to right, blue, red);
    }
    .oklab {
      background-image: linear-gradient(in oklab to right, blue, red);
    }
    .oklch-longer {
      background-image: linear-gradient(in oklch longer hue to right, blue, red);
    }
    

#### Result

### [Color interpolation in repeating gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#color_interpolation_in_repeating_gradients)

The following example shows how to specify a color space when interpolating colors in repeating gradients. Three boxes show different types of repeating gradients using the [`repeating-conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)
, [`repeating-linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
, and [`repeating-radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
 functions. The first box uses the Lab color space to interpolate between two color values. The second and third boxes use OkLCh and additionally provide a [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
 to specify how to interpolate between hue values.

#### HTML

html

    <div class="gradient conic">conic</div>
    <div class="gradient linear">linear</div>
    <div class="gradient radial">radial</div>
    

#### CSS

We used the same two colors in each gradient to demonstrate the different effects of [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
 and [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 on color interpolation in gradients.

    .gradient {
      height: 200px;
      width: 200px;
      display: inline-block;
      font-family: monospace;
      margin: 10px;
      font-size: 16px;
    }
    

css

    .conic {
      background-image: repeating-conic-gradient(
        in lab,
        burlywood,
        blueviolet 120deg
      );
    }
    
    .linear {
      background-image: repeating-linear-gradient(
        in oklch,
        burlywood,
        blueviolet 75px
      );
    }
    
    .radial {
      background-image: repeating-radial-gradient(
        in oklch longer hue,
        blueviolet 50px,
        burlywood 100px
      );
    }
    

#### Result

Comparing the first and second boxes demonstrates the difference of interpolating between two colors in differing color spaces. Comparing the second and third boxes shows the difference between [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
s, with the linear gradient using the shorter method (default) and the radial gradient using the longer method.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 4  <br>\# interpolation-space](https://drafts.csswg.org/css-color/#interpolation-space) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

### [css.types.color.color-mix](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#css.types.color.color-mix)

### [css.types.color.color.display-p3-linear](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#css.types.color.color.display-p3-linear)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    , [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    
*   [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/color-interpolation-method/index.md?plain=1 "Folder: en-us/web/css/reference/values/color-interpolation-method (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor-interpolation-method&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor-interpolation-method%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor-interpolation-method%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor-interpolation-method%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")