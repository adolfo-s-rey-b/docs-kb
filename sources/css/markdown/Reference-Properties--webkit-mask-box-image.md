*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#mdn-search)
    

`-webkit-mask-box-image` CSS property
=====================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The non-standard prefixed **`-webkit-mask-box-image`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the mask image for an element's border box.

**Note:** This property is not standard and is not on any standards track. Consider using the [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
 property instead.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`-webkit-mask-border-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-source)
    
*   [`-webkit-mask-border-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset)
    
*   [`-webkit-mask-border-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-repeat)
    

The values includes the `<image>` to be used as the mask border, and optionally four border outset values and up to two border repeat styles.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#syntax)

--------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#values)

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)

The location of the image resource to be used as a mask image, [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
, or other [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 value.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#none)

Used to specify that a border box is to have no mask image.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The size of the mask image's offset. See [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 for possible units.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

The mask image's offset has a percentage value relative to the border box's corresponding dimension (width or height).

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

The size of the mask image's offset in pixels.

[`repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#repeat)

The mask image is repeated as many times as is necessary to span the border box. May include a partial image if the mask image does not divide evenly into the border box.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#stretch)

The mask image is stretched to contain the border box exactly.

[`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#round)

The mask image is stretched somewhat and repeated such that there is no partial mask image at the end of the border box.

[`space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#space)

The mask image is repeated as many times as possible without stretching. There is no partial mask image at the end of the border box.

The outset values, or edge offsets, define the distances from the top, right, bottom, and left edges of the image, in that order. The values can be set as [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, with numbers interpreted as pixel lengths.

Border repeat styles, when included, are interpreted in the order of `<repeat-x> <repeat-y>`. If only one value is declared, the value is the same for both axes. While similar to [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
, the `cover` and `contain` values are not supported.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

*   [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
    : `none`
*   Applies to: all elements
*   [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    : no
*   [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
    : as specified

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

\-webkit-mask-box-image =   
  <mask-image-source> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <mask-image-offset>[{4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 <mask-border-repeat>[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#examples)

------------------------------------------------------------------------------------------------------------------

### [Setting an image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#setting_an_image)

### [Offsetting and filling an image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#offsetting_and_filling_an_image)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#specifications)

------------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image#see_also)

------------------------------------------------------------------------------------------------------------------

*   CSS [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
     property
*   CSS [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
     property
*   [Safari CSS reference: `-webkit-mask-box-image`](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/StandardCSSProperties.html#//apple_ref/doc/uid/TP30001266-SW14 "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/-webkit-mask-box-image/index.md?plain=1 "Folder: en-us/web/css/reference/properties/-webkit-mask-box-image (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-mask-box-image&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-mask-box-image%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-mask-box-image%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-mask-box-image%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")