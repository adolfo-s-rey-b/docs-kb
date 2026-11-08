*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#mdn-search)
    

`-webkit-mask-repeat-x` CSS property
====================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `-webkit-mask-repeat-x` property specifies whether and how a mask image is repeated (tiled) horizontally.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#syntax)

-------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#values)

This property is specified as one or more comma-separated values:

[`repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#repeat)

The mask image is repeated both horizontally and vertically.

[`no-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#no-repeat)

The mask image is not repeated horizontally; only one copy of the mask image is drawn in that direction. The remainder of the masked element's content is not displayed.

[`space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#space)

The image is repeated as much as possible without clipping. The first and last images are pinned to either side of the element, and whitespace is distributed evenly between the images. The [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
 property is ignored unless only one image can be displayed without clipping. The only case where clipping happens using space is when there isn't enough room to display one image.

[`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#round)

As the allowed space increases in size, the repeated images will stretch (leaving no gaps) until there is room for another one to be added. When the next image is added, all of the current ones compress to allow room. Example: An image with an original width of 260px, repeated three times, might stretch until each repetition is 300px wide, and then another image will be added. They will then compress to 225px.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `repeat` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

\-webkit-mask-repeat-x =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 repeat [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 no-repeat [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 space [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 round [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using a repeating or non-repeating mask image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#using_a_repeating_or_non-repeating_mask_image)

### [Using multiple mask images](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#using_multiple_mask_images)

You can specify a different `<repeat-style>` for each mask image, separated by commas:

Each image is matched with the corresponding repeat style, from first specified to last.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#specifications)

-----------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`-webkit-mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
    
*   [`-webkit-mask-repeat-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-y)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/-webkit-mask-repeat-x/index.md?plain=1 "Folder: en-us/web/css/reference/properties/-webkit-mask-repeat-x (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-mask-repeat-x&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-mask-repeat-x%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-mask-repeat-x%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-mask-repeat-x%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22c0b3059ff71d769af670478cc41605581108d1%0A*+Document+last+modified%3A+2026-09-10T13%3A27%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")