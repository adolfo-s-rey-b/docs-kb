*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#mdn-search)
    

`font-palette` CSS property
===========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2022.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-palette`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property allows specifying one of the many palettes contained in a [color font](https://www.colorfonts.wtf/ "External link (opens in new tab)")
 that a user agent may use for the font. Users can also override the values in a palette or create a new palette by using the [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
 at-rule.

**Note:** A `font-palette` palette takes precedence when coloring a font. The [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property will not override a font palette, even if specified with [`!important`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/important)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Using a font-defined palette */
    font-palette: normal;
    
    /* Using a user-defined palette */
    font-palette: --one;
    
    /* Creating a new palette by blending two others */
    font-palette: palette-mix(in lch, --blue, --yellow);
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#values)

This property is specified as a single value from the following list:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#normal)

Specifies the default color palette or the default glyph colorization (set by the font maker) to be used for the font. With this setting, the palette in the font at index 0 is rendered.

[`light`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#light)

Specifies the first palette in the font that matches 'light' to be used for the font. Some fonts contain metadata that identify a palette as applicable for a light (close to white) background. If a font does not have this metadata, the `light` value behaves as `normal`.

[`dark`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#dark)

Specifies the first palette in the font that matches 'dark' to be used for the font. Some fonts contain metadata that identify a palette as applicable for a dark (close to black) background. If a font does not have this metadata, the value behaves as `normal`.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

Allows you to specify your own values for the font palette by using the `<palette-identifier>` of a [@font-palette-values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
 at-rule.

[`palette-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix)

Creates a new `font-palette` value by blending together two `font-palette` values by specified percentages and color interpolation methods.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#formal_syntax)

------------------------------------------------------------------------------------------------------------------

font-palette =   
  normal                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  light                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dark                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <palette-identifier>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <palette-mix()>         
  
<palette-identifier> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
  
[<palette-mix()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix)
 =   
  palette-mix( <color-interpolation-method>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<'font-palette'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<color-interpolation-method>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
 =   
  in [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <rectangular-color-space> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <polar-color-space> <hue-interpolation-method>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <custom-color-space> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<font-palette> =   
  normal                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  light                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dark                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <palette-identifier>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <palette-mix()>         
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#examples)

--------------------------------------------------------------------------------------------------------

### [Specifying a dark palette](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#specifying_a_dark_palette)

This example allows you to use the first palette marked as _dark_ (works best on a near black background) by the font-maker.

css

    @media (prefers-color-scheme: dark) {
      .banner {
        font-palette: dark;
      }
    }
    

### [Animating between two palettes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#animating_between_two_palettes)

This example illustrates how to animate `font-palette` value changes to create a smooth font animation.

#### HTML

The HTML contains a single paragraph of text to animate:

html

    <p>color-palette<br />animation</p>
    

#### CSS

In the CSS, we import a [color font](https://www.colorfonts.wtf/ "External link (opens in new tab)")
 called [Nabla](https://nabla.typearture.com/ "External link (opens in new tab)")
 from [Google Fonts](https://fonts.google.com/?coloronly=true "External link (opens in new tab)")
, and define two custom `font-palette` values using the [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
 at-rule. We then create [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 that animate between these two palettes, and apply this animation to our paragraph.

css

    @import "https://fonts.googleapis.com/css2?family=Nabla&display=swap";
    
    @font-palette-values --blue-nabla {
      font-family: "Nabla";
      base-palette: 2; /* this is Nabla's blue palette */
    }
    
    @font-palette-values --grey-nabla {
      font-family: "Nabla";
      base-palette: 3; /* this is Nabla's grey palette */
    }
    
    @keyframes animate-palette {
      from {
        font-palette: --grey-nabla;
      }
    
      to {
        font-palette: --blue-nabla;
      }
    }
    
    p {
      font-family: "Nabla", fantasy;
      font-size: 5rem;
      margin: 0;
      text-align: center;
      animation: animate-palette 4s infinite alternate linear;
    }
    

#### Result

The output looks like this:

**Note:** Browsers that still implement `discrete` `font-palette` animation will flip between the two palettes rather than smoothly animating.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-palette-prop](https://drafts.csswg.org/css-fonts/#font-palette-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette#see_also)

--------------------------------------------------------------------------------------------------------

*   [`palette-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix)
    
*   [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
    
*   [`base-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)
     descriptor
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/font-family)
     descriptor
*   [`override-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors)
     descriptor

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-palette/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-palette (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-palette&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-palette%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-palette%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-palette%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")