*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#mdn-search)
    

`-webkit-mask-composite` CSS property
=====================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`-webkit-mask-composite`** property specifies the manner in which multiple mask images applied to the same element are composited with one another. Mask images are composited in the opposite order that they are declared with the [`-webkit-mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 property.

**Note:** There is a standardized [`mask-composite`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite)
 property covering parts of this non-standard property using different keywords.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#syntax)

--------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#values)

This property is specified as one of the following keyword values:

[`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#clear)

Overlapping pixels in the source mask image and the destination mask image are cleared.

[`copy`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#copy)

The source mask image replaces the destination mask image.

[`source-over`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#source-over)

The source mask image is rendered over the destination mask image.

[`source-in`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#source-in)

Overlapping pixels in the source mask image and the destination mask image are replaced by the pixels of the source mask image; all other pixels are cleared.

[`source-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#source-out)

Overlapping pixels in the source mask image and the destination mask image are cleared; all remaining pixels of the source mask image are rendered.

[`source-atop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#source-atop)

The pixels of the destination mask image are rendered. The pixels of the source mask image are rendered only if they overlap a nontransparent portion of the destination mask image. This causes the source mask image to have no effect.

[`destination-over`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#destination-over)

The destination mask image is rendered over the source mask image.

[`destination-in`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#destination-in)

Overlapping pixels in the source mask image and the destination mask image remain the pixels of the destination mask image; all other pixels are cleared.

[`destination-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#destination-out)

Overlapping pixels in the source mask image and the destination mask image are cleared; all remaining pixels of the source mask image are rendered.

[`destination-atop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#destination-atop)

The pixels of the source mask image are rendered. The pixels of the destination mask image are rendered only if they overlap a nontransparent portion of the destination mask image. This causes the destination mask image to have no effect.

[`xor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#xor)

Overlapping pixels in the source mask image and the destination mask image become fully transparent if they are both fully opaque.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `source-over` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

\-webkit-mask-composite =   
  <composite-style>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#examples)

------------------------------------------------------------------------------------------------------------------

### [Compositing with XOR](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#compositing_with_xor)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#specifications)

------------------------------------------------------------------------------------------------------------------------------

Not part of any standard. This property is specified as [`mask-composite`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite)
 using different values.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`mask-composite`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/-webkit-mask-composite/index.md?plain=1 "Folder: en-us/web/css/reference/properties/-webkit-mask-composite (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-mask-composite&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-mask-composite%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-mask-composite%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-mask-composite%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22c0b3059ff71d769af670478cc41605581108d1%0A*+Document+last+modified%3A+2026-09-10T13%3A27%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")