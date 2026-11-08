*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#mdn-search)
    

`palette-mix()` CSS function
============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/229)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#browser_compatibility)
 carefully before using this in production.

The **`palette-mix()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 can be used to create a new [`font-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
 value by blending together two `font-palette` values by specified percentages and color interpolation methods.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#syntax)

----------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#values)

Functional notation:

palette-mix(method, palette1 \[p1\], palette2 \[p2\])

[`method`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#method)

A [`<color-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
 specifying the interpolation color space.

[`palette1`, `palette2`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#palette1)

The [`font-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
 values to blend together. These can be _any_ `font-palette` values, including `palette-mix()` functions, `normal`, `dark`, and `light`.

[`p1`, `p2` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#p1)

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values between `0%` and `100%` specifying the amount of each palette to mix. They are normalized as follows:

*   If both `p1` and `p2` are omitted, then `p1 = p2 = 50%`.
*   If `p1` is omitted, then `p1 = 100% - p2`.
*   If `p2` is omitted, then `p2 = 100% - p1`.
*   If `p1 = p2 = 0%`, the function is invalid.
*   If `p1 + p2 ≠ 100%`, then `p1' = p1 / (p1 + p2)` and `p2' = p2 / (p1 + p2)`, where `p1'` and `p2'` are the normalization results.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#formal_syntax)

------------------------------------------------------------------------------------------------------------------------------

<palette-mix()> =   
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
    
  
[<font-palette>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
 =   
  normal                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  light                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dark                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <palette-identifier>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<palette-mix()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix)
         
  
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
    
  
<palette-identifier> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
  
<xyz-space> =   
  xyz      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d50  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  xyz-d65    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#examples)

--------------------------------------------------------------------------------------------------------------------

### [Using `palette-mix()` to blend two palettes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#using_palette-mix_to_blend_two_palettes)

This example shows how to use the `palette-mix()` function to create a new palette by blending two others.

#### HTML

The HTML contains three paragraphs to apply our font information to:

#### CSS

In the CSS, we import a color font from Google Fonts, and define two custom `font-palette` values using the [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
 at-rule. We then apply three different `font-palette` values to the paragraphs — `--yellow`, `--blue`, and a new green palette, created using `palette-mix()` to blend the blue and yellow palettes together.

#### Result

The output looks like this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# typedef-font-palette-palette-mix](https://drafts.csswg.org/css-fonts/#typedef-font-palette-palette-mix) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [`font-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
    
*   [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
    
*   [`color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix)
    
*   [CSS color values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_values)
     guide
*   [Color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-palette/palette-mix/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-palette/palette-mix (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-palette%2Fpalette-mix&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-palette%2Fpalette-mix%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-palette%2Fpalette-mix%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-palette%2Fpalette-mix%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")