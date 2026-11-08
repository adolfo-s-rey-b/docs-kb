*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#mdn-search)
    

`border-image-slice` CSS property
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-image-slice`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property divides the image specified by [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
 into regions. These regions form the components of an element's [border image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#try_it)

----------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#syntax)

----------------------------------------------------------------------------------------------------------

The `border-image-slice` property may be specified using one to four `<number-percentage>` values to represent the position of each image slice. Negative values are invalid; values greater than their corresponding dimension are clamped to `100%`.

*   When **one** position is specified, it creates all four slices at the same distance from their respective sides.
*   When **two** positions are specified, the first value creates slices measured from the **top and bottom**, the second creates slices measured from the **left and right**.
*   When **three** positions are specified, the first value creates a slice measured from the **top**, the second creates slices measured from the **left and right**, the third creates a slice measured from the **bottom**.
*   When **four** positions are specified, they create slices measured from the **top**, **right**, **bottom**, and **left** in that order (clockwise).

The optional `fill` value, if used, can be placed anywhere in the declaration.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#values)

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

Represents an edge offset in _pixels_ for raster images and _coordinates_ for vector images. For vector images, the number is relative to the element's size, not the size of the source image, so percentages are generally preferable in these cases.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Represents an edge offset as a percentage of the source image's size: the width of the image for horizontal offsets, the height for vertical offsets.

[`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#fill)

Preserves the middle image region and displays it like a background image, but stacked above the actual [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
. Its width and height are sized to match the top and left image regions, respectively.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#description)

--------------------------------------------------------------------------------------------------------------------

The slicing process creates nine regions in total: four corners, four edges, and a middle region. Four slice lines, set a given distance from their respective sides, control the size of the regions.

![The nine regions defined by the border-image or border-image-slice properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice/border-image-slice.png)

The above diagram illustrates the location of each region.

*   Zones 1-4 are corner regions. Each one is used a single time to form the corners of the final border image.
*   Zones 5-8 are edge regions. These are [repeated, scaled, or otherwise modified](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
     in the final border image to match the dimensions of the element.
*   Zone 9 is the middle region. It is discarded by default, but is used like a background image if the keyword `fill` is set.

The [`border-image-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
, [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)
, and [`border-image-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
 properties determine how these regions are used to form the final border image.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `100%` |
| Applies to | all elements, except internal table elements when [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)<br> is `collapse`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the size of the border image |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | one to four percentage(s) (as specified) or absolute length(s), plus the keyword `fill` if specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

border-image-slice =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  fill[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                                           

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#examples)

--------------------------------------------------------------------------------------------------------------

### [Adjustable border width and slice](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#adjustable_border_width_and_slice)

The following example shows a `<div>` with a border image set on it. The source image for the borders is as follows:

![Nine multi-colored diamonds laid out in three rows and three columns](https://developer.mozilla.org/shared-assets/images/examples/border-diamonds.png)

The diamonds in the source image are 30px across, so setting 30 pixels as the value for both [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
 and `border-image-slice` will get you complete and fairly crisp diamonds in your border:

These are the default values we have used in this example. However, we have also provided two sliders to allow you to dynamically change the values of the above two properties, allowing you to appreciate the effect they have:

`border-image-slice` Changes the size of the image slice sampled for use in each border and border corner (and the content area, if the `fill` keyword is used) — varying this away from 30 causes the border to look somewhat irregular, but can have some interesting effects.

`border-width`: Changes the width of the border. The sampled image size is scaled to fit inside the border, which means that if the width is bigger than the slice, the image can start to look somewhat pixelated (unless of course you use an SVG image).

#### HTML

#### CSS

#### JavaScript

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# border-image-slice](https://drafts.csswg.org/css-backgrounds/#border-image-slice) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Illustrated description of the 1-to-4-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties#tricky_edge_cases)
    
*   [Border images in CSS: A key focus area for Interop 2023](https://developer.mozilla.org/en-US/blog/border-images-interop-2023/)
     on MDN blog (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-image-slice/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-image-slice (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image-slice&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image-slice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image-slice%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image-slice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fedb731bcb1ee26be7a4da56cc5b79e552b78865a%0A*+Document+last+modified%3A+2026-08-18T21%3A42%3A40.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")