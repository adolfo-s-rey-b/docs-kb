*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#mdn-search)
    

`aspect-ratio` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`aspect-ratio`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property allows you to define the desired width-to-height ratio of an element's box.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#syntax)

----------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#values)

This property is specified as one or both of the keyword `auto` or a `<ratio>`.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#auto)

[Replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
 with an intrinsic aspect ratio use _that_ aspect ratio, otherwise the box has no preferred aspect ratio. Size calculations involving intrinsic aspect ratio always work with the content box dimensions.

[`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)

The box's preferred aspect ratio is the specified ratio of `width` / `height`. If `height` and the preceding slash character are omitted, `height` defaults to `1`. Size calculations involving preferred aspect ratio work with the dimensions of the box specified by `box-sizing`.

[`auto && <ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#auto_ratio)

When both `auto` and a `<ratio>` are specified together, `auto` is used if the element is a replaced element with a natural aspect ratio, like an `<img>` element. Otherwise, the specified ratio of `width` / `height` is used as the preferred aspect ratio.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#description)

--------------------------------------------------------------------------------------------------------------

The `aspect-ratio` property defines a desired width-to-height ratio of an element's box. This means that even if the parent container or viewport size changes, the browser will adjust the element's dimensions to maintain the specified width-to-height ratio. The specified [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 is used in the calculation of auto sizes and some other layout functions.

At least one of the box's sizes needs to be automatic in order for `aspect-ratio` to have any effect. If neither the width nor height is an automatic size, then the provided aspect ratio has no effect on the box's preferred sizes.

This property is specified as one or both of the keyword auto or a `<ratio>`. If both are given, and the element is a [replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
, such as [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
, then the given ratio is used until the content is loaded. After the content is loaded, the `auto` value is applied, so the intrinsic aspect ratio of the loaded content is used.

If the element is not a replaced element, then the given `ratio` is used.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements except inline boxes and internal ruby or table boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#formal_syntax)

------------------------------------------------------------------------------------------------------------------

aspect-ratio =   
  auto     [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <ratio>    
  
[<ratio>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
 =   
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#examples)

--------------------------------------------------------------------------------------------------------

### [Exploring aspect-ratio effects with fixed width](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#exploring_aspect-ratio_effects_with_fixed_width)

In this example, the width of the `<div>` elements has been set to `100px` and height to `auto`. Since the width value is fixed here, the `aspect-ratio` property affects only the height of the `<div>` elements to maintain the specified width-to-height ratio.

### [Fallback to natural aspect ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#fallback_to_natural_aspect_ratio)

In this example we are using two `<img>` elements. The first element does not have its `src` attribute set to an image file.

The following code sets `3/2` as the preferred aspect ratio and `auto` as a fallback.

Note how the first image without replaced content keeps the `3/2` aspect ratio, while the second image after the content is loaded uses the image's natural aspect ratio.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 4  <br>\# aspect-ratio](https://drafts.csswg.org/css-sizing-4/#aspect-ratio) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio#see_also)

--------------------------------------------------------------------------------------------------------

*   [Understanding aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    
*   [Image aspect-ratio: preventing jank](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/Multimedia#rendering_strategy_preventing_jank_when_loading_images)
    
*   [Designing an aspect ratio unit for CSS](https://www.smashingmagazine.com/2019/03/aspect-ratio-unit-css/ "External link (opens in new tab)")
    
*   [Setting Height And Width On Images Is Important Again](https://www.smashingmagazine.com/2020/03/setting-height-width-images-important-again/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/aspect-ratio/index.md?plain=1 "Folder: en-us/web/css/reference/properties/aspect-ratio (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Faspect-ratio&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Faspect-ratio%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Faspect-ratio%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Faspect-ratio%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")