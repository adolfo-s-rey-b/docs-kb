*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#mdn-search)
    

`background-size` CSS property
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`background-size`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the size of the element's background image. The image can be left to its natural size, stretched, or constrained to fit the available space.

Spaces not covered by a background image are filled with the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 property, and the background color will be visible behind background images that have transparency/translucency.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#syntax)

-------------------------------------------------------------------------------------------------------

The `background-size` property is specified in one of the following ways:

*   Using the keyword values `contain` or `cover`.
*   Using a width value only, in which case the height defaults to `auto`.
*   Using both a width and a height value, in which case the first sets the width and the second sets the height. Each value can be a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    , a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    , or `auto`.

To specify the size of multiple background images, separate the value for each one with a comma.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#values)

[`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#contain)

Scales the image as large as possible within its container without cropping or stretching the image. If the container is larger than the image, this will result in image tiling, unless the [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
 property is set to `no-repeat`.

[`cover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#cover)

Scales the image (while preserving its ratio) to the smallest possible size to fill the container (that is: both its height and width completely _cover_ the container), leaving no empty space. If the proportions of the background differ from the element, the image is cropped either vertically or horizontally.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#auto)

Scales the background image in the corresponding direction such that its intrinsic proportions are maintained.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Stretches the image in the corresponding dimension to the specified length. Negative values are not allowed.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Stretches the image in the corresponding dimension to the specified percentage of the _background positioning area_. The background positioning area is determined by the value of [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
 (by default, the padding box). However, if the background's [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
 value is `fixed`, the positioning area is instead the entire [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
. Negative values are not allowed.

### [Intrinsic dimensions and proportions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#intrinsic_dimensions_and_proportions)

The computation of values depends on the image's intrinsic dimensions (width and height) and intrinsic proportions (width-to-height ratio). These attributes are as follows:

*   A bitmap image (such as JPG) always has intrinsic dimensions and proportions.
*   A vector image (such as SVG) does not necessarily have intrinsic dimensions. If it has both horizontal and vertical intrinsic dimensions, it also has intrinsic proportions. If it has no dimensions or only one dimension, it may or may not have proportions.
*   CSS [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    s have no intrinsic dimensions or intrinsic proportions.
*   Background images created with the [`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
     function use the intrinsic dimensions and proportions of the generating element.

**Note:** In Gecko, background images created using the [`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
 function are currently treated as images with the dimensions of the element, or of the background positioning area if the element is SVG, with the corresponding intrinsic proportion. This is non-standard behavior.

Based on the intrinsic dimensions and proportions, the rendered size of the background image is computed as follows:

*   **If both components of `background-size` are specified and are not `auto`:** The background image is rendered at the specified size.
    
*   **If the `background-size` is `contain` or `cover`:** While preserving its intrinsic proportions, the image is rendered at the largest size contained within, or covering, the background positioning area. If the image has no intrinsic proportions, then it's rendered at the size of the background positioning area.
    
*   **If the `background-size` is `auto` or `auto auto`:**
    
    *   If the image has both horizontal and vertical intrinsic dimensions, it's rendered at that size.
    *   If the image has no intrinsic dimensions and has no intrinsic proportions, it's rendered at the size of the background positioning area.
    *   If the image has no intrinsic dimensions but has intrinsic proportions, it's rendered as if `contain` had been specified instead.
    *   If the image has only one intrinsic dimension and has intrinsic proportions, it's rendered at the size corresponding to that one dimension. The other dimension is computed using the specified dimension and the intrinsic proportions.
    *   If the image has only one intrinsic dimension but has no intrinsic proportions, it's rendered using the specified dimension and the other dimension of the background positioning area.
    
    **Note:** SVG images have a [`preserveAspectRatio`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/preserveAspectRatio)
     attribute that defaults to the equivalent of `contain`; an explicit `background-size` causes `preserveAspectRatio` to be ignored.
    
*   **If the `background-size` has one `auto` component and one non-`auto` component:**
    
    *   If the image has intrinsic proportions, it's stretched to the specified dimension. The unspecified dimension is computed using the specified dimension and the intrinsic proportions.
    *   If the image has no intrinsic proportions, it's stretched to the specified dimension. The unspecified dimension is computed using the image's corresponding intrinsic dimension, if there is one. If there is no such intrinsic dimension, it becomes the corresponding dimension of the background positioning area.

**Note:** Background sizing for vector images that lack intrinsic dimensions or proportions is not yet fully implemented in all browsers. Be careful about relying on the behavior described above, and test in multiple browsers to be sure the results are acceptable.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto auto` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | relative to the background positioning area |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with relative lengths converted into absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a repeatable list |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

background-size =   
  <bg-size>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<bg-size> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage \[0,∞\]> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 auto [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  cover                                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  contain                                      
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#examples)

-----------------------------------------------------------------------------------------------------------

### [Tiling a large image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#tiling_a_large_image)

Let's consider a large image, a 2982x2808 Firefox logo image. We want to tile four copies of this image into a 300x300-pixel element. To do this, we can use a fixed `background-size` value of 150 pixels.

#### HTML

#### CSS

#### Result

See [Resizing background images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images)
 for more examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# background-size](https://drafts.csswg.org/css-backgrounds/#background-size) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Resizing background images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images)
    
*   [Scaling SVG backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds)
    
*   [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-size/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")