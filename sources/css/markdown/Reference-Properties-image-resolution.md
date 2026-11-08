*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#mdn-search)
    

`image-resolution` CSS property
===============================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#browser_compatibility)
 carefully before using this in production.

The **`image-resolution`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the intrinsic resolution of all raster images used in or on the element. It affects content images such as replaced elements and generated content, and decorative images such as `background-image` images.

The image resolution is defined as the number of image pixels per unit length, e.g., pixels per inch. By default, CSS assumes a resolution of one image pixel per CSS px unit; however, the `image-resolution` property allows a different resolution to be specified.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#syntax)

--------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#values)

This property is specified as one or more space-separated values from the following list:

[`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)

Specifies the intrinsic resolution explicitly.

[`from-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#from-image)

Uses the intrinsic resolution as specified by the image format. If the image does not specify its own resolution, the explicitly specified resolution is used (if given), else it defaults to `1dppx` (1 image pixel per CSS px unit).

[`snap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#snap)

If the `snap` keyword is provided, the computed resolution is the specified resolution rounded to the nearest value that would map one image pixel to an integer number of [device pixels](https://developer.mozilla.org/en-US/docs/Glossary/Device_pixel)
. If the resolution is taken from the image, then the used intrinsic resolution is the image's native resolution similarly adjusted.

**Note:** As vector formats such as SVG do not have an intrinsic resolution, this property has no effect on vector images.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `1dppx` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, except with <resolution> possibly altered by computed for 'snap' value |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

image-resolution =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 from-image [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [<resolution>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  snap[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#examples)

------------------------------------------------------------------------------------------------------------

### [Setting a high dpi for print](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#setting_a_high_dpi_for_print)

When printing the document, use a higher resolution.

### [Use image resolution with fallback](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#use_image_resolution_with_fallback)

Uses the resolution from the image. If the image does not have a resolution, use 300dpi rather than the default 1dppx.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 4  <br>\# the-image-resolution](https://drafts.csswg.org/css-images-4/#the-image-resolution) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

Currently, no browsers support this feature.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution#see_also)

------------------------------------------------------------------------------------------------------------

*   Other image-related CSS properties: [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    , [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
    , [`image-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation)
    , [`image-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering)
    .
*   [Chromium bug: 1086473](https://crbug.com/1086473 "External link (opens in new tab)")
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/image-resolution/index.md?plain=1 "Folder: en-us/web/css/reference/properties/image-resolution (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fimage-resolution&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fimage-resolution%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fimage-resolution%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fimage-resolution%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")