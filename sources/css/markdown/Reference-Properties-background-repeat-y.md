*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#mdn-search)
    

`background-repeat-y` CSS property
==================================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#browser_compatibility)
 carefully before using this in production.

The **`background-repeat-y`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how background images are repeated, or not, along the vertical axis.

The [`background-repeat-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x)
 and `background-repeat-y` properties can also be set using the [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
 or [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
 shorthand properties.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#try_it)

-----------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#syntax)

-----------------------------------------------------------------------------------------------------------

The `background-repeat-y` property is specified as one or more values, separated by commas.

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#values)

-----------------------------------------------------------------------------------------------------------

[`repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#repeat)

The default value. The image is repeated as many times as needed to cover the entire height of the background image painting area. The edge image is clipped if multiple images do not fit exactly into the background height.

[`no-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#no-repeat)

The image is not repeated. The position of the non-repeated background image is defined by the [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 CSS property.

[`space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#space)

The image is repeated as much as possible without clipping. The first and last images are pinned to the top and bottom of the element, and the whitespace is distributed evenly between the images. The [`background-position-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-y)
 property is ignored unless one or more images can be displayed without clipping. If the image is taller than the element, it is clipped, as there isn't enough room to display it.

[`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#round)

The image is repeated vertically. As the available space increases in size, the repeated images will stretch (leaving no gaps) until there is room for another one to be added. If multiple images don't fit the background exactly, they are rescaled to fit.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#description)

---------------------------------------------------------------------------------------------------------------------

The `background-repeat-y` property accepts a comma-separated list of [`<repetition>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#values)
 keyterms, which define how background image(s) should repeat vertically, or not repeat at all.

The default value is `repeat`. With this value, the background image repeats vertically, covering the entire height of the background paint area, with edge images being clipped to the size of the element. Whether the top, bottom, or both edges are clipped depends on the value of the corresponding [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 value. How many times images are repeated and how much the images on the edges are clipped depends on the size of the background painting area and height value of the corresponding [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 property.

The repeating images can be evenly spaced apart, ensuring the repeated images aren't clipped in the vertical direction. With the `space` value, if the height of the background paint area is not a multiple of the image's height or does not otherwise have a size that is a multiple of the background size in along the y-axis, there will be areas not covered by the background image.

Alternatively, the repeated background image can be stretched to cover the entire height of the background area without clipping. With `round`, if the height of the background paint area is not a multiple of the height of the background image, the repeated image is stretched to fill all the available space until there is room to add an additional repeated image.

For example, given a background image that is 100px x 100px and a background paint area that is 1099px tall, the image will be repeated 10 times in the vertical direction with each image stretched to be 109.9px tall, possibly altering the image's [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 and distorting it. If the height of the paint area increases by 1px, becoming 1100px tall, an 11th image will fit vertically, with each image will be painted at 100px tall, no longer being stretched in the vertical direction.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

background-repeat-y =   
  <repetition>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<repetition> =   
  repeat     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  round      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-repeat    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#examples)

---------------------------------------------------------------------------------------------------------------

### [Setting background-repeat-y](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#setting_background-repeat-y)

#### HTML

#### CSS

#### Result

In this example, each list item is matched with a different value of `background-repeat-y`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds Module Level 4  <br>\# background-repeat-longhands](https://drafts.csswg.org/css-backgrounds-4/#background-repeat-longhands) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`background-repeat-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x)
     and the [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
     shorthand.
*   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
     shorthand components: [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
    , [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    , [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    , [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    , [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
     ([`background-position-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x)
     and [`background-position-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-y)
    ), and [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [Using multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
    
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
     module
*   [Understanding aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-repeat-y/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-repeat-y (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-repeat-y&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-repeat-y%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-repeat-y%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-repeat-y%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa8b7faffbd3fdeae5c0be97793d963d8a31cd1cf%0A*+Document+last+modified%3A+2026-04-22T11%3A39%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")