*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#mdn-search)
    

`border-image-width` CSS property
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-image-width`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the width of an element's [border image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
.

If this property's value is greater than the element's [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
, the border image will extend beyond the padding (and/or content) edge.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#try_it)

----------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#syntax)

----------------------------------------------------------------------------------------------------------

The `border-image-width` property may be specified using one, two, three, or four values chosen from the list of values below.

*   When **one** value is specified, it applies the same width to **all four sides**.
*   When **two** values are specified, the first width applies to the **top and bottom**, the second to the **left and right**.
*   When **three** values are specified, the first width applies to the **top**, the second to the **left and right**, the third to the **bottom**.
*   When **four** values are specified, the widths apply to the **top**, **right**, **bottom**, and **left** in that order (clockwise).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#values)

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#length-percentage)

The width of the border, specified as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
. Percentages are relative to the _width_ of the border image area for horizontal offsets and the _height_ of the border image area for vertical offsets. Must not be negative.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#number)

The width of the border, specified as a multiple of the corresponding [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
. Must not be negative.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#auto)

The width of the border is made equal to the intrinsic width or height (whichever is applicable) of the corresponding [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
. If the image does not have the required intrinsic dimension, the corresponding `border-width` is used instead.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `1` |
| Applies to | all elements, except internal table elements when [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)<br> is `collapse`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the width or height of the border image area |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with relative lengths converted into absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

border-image-width =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage \[0,∞\]> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 auto [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#examples)

--------------------------------------------------------------------------------------------------------------

### [Tiling a border image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#tiling_a_border_image)

This example creates a border image using the following ".png" file, which is 90 by 90 pixels:

![Square image containing eight circles. The circles in each corner are light purple. The four side circles are blue. The area in the middle, where a ninth circle could fit, is blank.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width/border.png)

Thus, each circle in the source image is 30 by 30 pixels.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# border-image-width](https://drafts.csswg.org/css-backgrounds/#border-image-width) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
    
*   [Learn CSS: Backgrounds and borders](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Backgrounds_and_borders)
    
*   [Border images in CSS: A key focus area for Interop 2023](https://developer.mozilla.org/en-US/blog/border-images-interop-2023/)
     on MDN blog (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-image-width/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-image-width (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image-width&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image-width%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image-width%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image-width%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")