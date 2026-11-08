*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#mdn-search)
    

`image-orientation` CSS property
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`image-orientation`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies a layout-independent correction to the orientation of an image.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#try_it)

---------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#syntax)

---------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#none)

Does not apply any additional image rotation; the image is oriented as encoded or as other CSS property values dictate.

[`from-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#from-image)

Default initial value. The [EXIF](https://en.wikipedia.org/wiki/EXIF "External link (opens in new tab)")
 information contained in the image is used to rotate the image appropriately.

**Warning:** `image-orientation: none;` **does not** override the orientation of non-secure-origin images as encoded by their [EXIF](https://en.wikipedia.org/wiki/EXIF "External link (opens in new tab)")
 information, due to security concerns. Find out more from [the CSS working group draft issue](https://github.com/w3c/csswg-drafts/issues/5165 "External link (opens in new tab)")
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#description)

-------------------------------------------------------------------------------------------------------------------

This property is intended _only_ to be used for the purpose of correcting the orientation of images which were shot with the camera rotated. It should _not_ be used for arbitrary rotations. For any purpose other than correcting an image's orientation due to how it was shot or scanned, use a [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 property with the `rotate` keyword to specify rotation. This includes any user-directed changes to the orientation of the image, or changes required for printing in portrait versus landscape orientation.

If used in conjunction with other CSS properties, such as a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
, any `image-orientation` rotation is applied before any other transformations.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `from-image` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)<br>, rounded to the next quarter turn from `0deg` and normalized, that is moduloing the value by `1turn` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

image-orientation =   
  from-image           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 flip [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#examples)

-------------------------------------------------------------------------------------------------------------

### [Orienting image from image data](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#orienting_image_from_image_data)

The following image has been rotated through 180 degrees, and the `image-orientation` property is used to correct its orientation based on the EXIF data in the image. By changing the `image-orientation` to `none` you can see the effect of the property.

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 3  <br>\# the-image-orientation](https://drafts.csswg.org/css-images/#the-image-orientation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation#see_also)

-------------------------------------------------------------------------------------------------------------

*   Other image-related CSS properties: [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    , [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
    , [`image-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering)
    , [`image-resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution)
    .
*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
     and [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/image-orientation/index.md?plain=1 "Folder: en-us/web/css/reference/properties/image-orientation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fimage-orientation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fimage-orientation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fimage-orientation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fimage-orientation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")