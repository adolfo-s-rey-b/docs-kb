*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#mdn-search)
    

`mask-size` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mask-size`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the sizes of specified mask images. Mask image sizes can be fully or partially constrained to preserve their [intrinsic aspect ratios](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#syntax)

-------------------------------------------------------------------------------------------------

css

    /* Keyword syntax */
    mask-size: cover;
    mask-size: contain;
    mask-size: auto;
    
    /* One-value syntax */
    /* Mask width. Sets height to 'auto'. */
    mask-size: 50%;
    mask-size: 3em;
    mask-size: 12px;
    
    /* Two-value syntax */
    /* First value: mask width. Second value: mask height */
    mask-size: 3em 25%;
    mask-size: auto 6px;
    mask-size: auto 50%;
    
    /* Multiple values */
    mask-size: auto, contain;
    mask-size:
      50%,
      50% 25%,
      auto 25%;
    mask-size: 6px, auto, contain;
    
    /* Global values */
    mask-size: inherit;
    mask-size: initial;
    mask-size: revert;
    mask-size: revert-layer;
    mask-size: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#values)

The `mask-size` property accepts a comma-separated list of `<bg-size>` values. A `<bg-size>` value is either `cover`, `contain`, a pair of values specifying the width and height (in that order), or a single value specifying the width (in which case, the height is set to `auto`). Values include:

[`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#contain)

Scales the mask image up or down, while preserving its aspect-ratio, making the mask as large as possible within its container without cropping or stretching it. If the mask image is smaller than the container, the mask will tile, or repeat, unless the [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
 property is set to `no-repeat`.

[`cover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#cover)

Scales the mask image to the smallest possible size to fill the container while preserving its aspect ratio. If the aspect ratio of the mask image differs from the element, it will be cropped vertically or horizontally.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#auto)

Maintains the original aspect ratio of the mask source. When set for both the width and height, the origin size of the mask resource is used. Otherwise, `auto` scales the mask image in the corresponding direction such that its original aspect ratio is maintained.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Renders the mask image at the specified length in the corresponding dimension (width if set as the first or only value, height if set as the second value). Negative values are not allowed.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Renders the mask image in the corresponding dimension to the specified percentage of the box origin area as defined by the [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
 property, which defaults to `padding-box`. Negative values are not allowed.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#description)

-----------------------------------------------------------------------------------------------------------

The `mask-size` property is used to size mask layers.

An element can have multiple mask layers applied. The number of mask layers is determined by the number of comma-separated values in the [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 property value (a value creates a mask layer, even if it is `none`).

Each `mask-size` value in the comma-separated list of values is matched up with an associated mask layer as defined by the list of `mask-image` values, in order. If the number of values in the two properties differs:

*   If `mask-size` has more values than `mask-image`, the excess values of `mask-size` are not used.
*   If `mask-size` has fewer values than `mask-image`, the `mask-size` values are repeated.

Each `mask-size` value is a `<bg-size>` value. There are three ways to declare each `<bg-size>`: one keyword, two lengths, percentages or the keyword `auto`, or one length, percentage, or `auto`:

*   The available keywords are `cover` and `contain`.
*   When two values are specified, the first defines the mask width and the second defines its height.
*   When one value is specified, it defines only the mask width, with the height set to `auto`.

The width and height values are a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or the `auto` keyword, which is the default. Setting one or both values to `auto` maintains the mask image's original aspect ratio.

The rendered size of the mask image is computed as follows:

*   If both components of `mask-size` are specified and are not `auto`, the mask image renders at the specified size.
*   If the `mask-size` is `contain` or `cover`, the image is rendered by preserving its aspect ratio at the largest size contained within or covering the mask positioning area. If the image has no intrinsic proportion, such as with gradients, then it is rendered at the size of the mask positioning area.
*   If the `mask-size` is `auto` (which resolves to `auto auto`), it is rendered at the size at which the mask would be displayed if no CSS were applied to change the rendering; this is its [intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
    . If it has no intrinsic dimensions and no intrinsic proportion, as is the case with [CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    , it is rendered at the size of the mask positioning area, defined by the [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
     (which defaults to `border-box`). If the mask source has no dimensions but has a proportion (aspect-ratio), a value of `auto` will render it as if `contain` had been specified instead. If the image has one intrinsic dimension and a proportion, it is rendered at the size determined by that one dimension and the proportion. If the image has one intrinsic dimension but no proportion, it's rendered using the intrinsic dimension and the corresponding dimension of the mask positioning area.
*   If `mask-size` has one `auto` component and one non-`auto` component, which applies to all single-value values, the aspect ratio is maintained if the mask source has an intrinsic proportion. If there are no intrinsic proportions, the `auto` value is assumed to be the dimension of the mask positioning area.

Like with all longhand components of shorthand property, if the [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
 shorthand property is set and the value of the `mask-size` property is not defined within any mask layer, the `mask-size` value is reset to its initial value of `auto` for those mask layers.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with relative lengths converted into absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a repeatable list |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#formal_syntax)

---------------------------------------------------------------------------------------------------------------

mask-size =   
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#examples)

-----------------------------------------------------------------------------------------------------

### [Setting mask size as a percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#setting_mask_size_as_a_percentage)

This example demonstrates basic usage, while also demonstrating percentage values for `mask-size`.

#### HTML

We include two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements:

html

    <div class="width"></div>
    <div class="height"></div>
    

#### CSS

The `<div>` elements are defined to be twice as tall as they are wide, with a gradient background and mask:

css

    div {
      width: 200px;
      height: 400px;
      background: blue linear-gradient(red, blue);
      mask-image: url("/shared-assets/images/examples/mdn.svg");
    }
    

The width of one `<div>` element's mask is set to `50%`, with the height defaulting to `auto`. The mask's height for the second `<div>` element is set to `50%` with the width set to `auto`:

css

    .width {
      mask-size: 50%;
    }
    
    .height {
      mask-size: auto 50%;
    }
    

In the `width` case, the mask is rendered `100px` wide (`50%` of the `200px`\-wide element). The height defaults to `auto`, maintaining the mask's aspect ratio. In the `height` case, the mask is rendered `200px` tall (`50%` of the `400px`\-high container). The width is explicitly set to `auto`, maintaining the mask's aspect ratio.

    body {
      display: flex;
      gap: 20px;
    }
    

#### Results

### [Cover and contain](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#cover_and_contain)

This example demonstrates the keyword values for `mask-size`.

#### HTML

Three [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 elements are defined, each with a different class name, and each containing a `<div>`.

html

    <section class="auto">
      <div></div>
    </section>
    <section class="cover">
      <div></div>
    </section>
    <section class="contain">
      <div></div>
    </section>
    

#### CSS

The `<div>` elements are defined to be twice as tall as they are wide, with a gradient background and mask:

css

    div {
      width: 200px;
      height: 400px;
      background: blue linear-gradient(red, blue);
      mask-image: url("/shared-assets/images/examples/mask-star.svg");
    }
    

The `mask-size` of two of the `<div>` elements is set to one of the property's keyword values. The third `<div>` has a `mask-size` of `auto` set demonstrating the original intrinsic dimensions of the mask:

css

    .auto div {
      mask-size: auto;
    }
    
    .cover div {
      mask-size: cover;
    }
    
    .contain div {
      mask-size: contain;
    }
    

The property values is displayed using [generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
.

css

    section::before {
      content: "mask-size: " attr(class) ";";
      display: block;
      text-align: center;
      border-bottom: 1px solid;
    }
    

    body {
      display: flex;
      flex-flow: row wrap;
      gap: 10px;
    }
    section {
      border: 1px solid;
    }
    

#### Results

With `auto`, the star is displayed at its intrinsic `100px` by `100px` size. With `cover`, the star grows to be `400px` tall, covering the entire origin box. With `contain`, the star grows until one dimension equals the same dimension of the [origin box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
, meaning that the star is as large as it can be (`200px` wide) but still contained by it.

### [When the mask is larger than the container](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#when_the_mask_is_larger_than_the_container)

Using the same HTML and CSS as above, with just a different origin box size, this example explores what happens when the origin box is smaller than the intrinsic dimensions of the mask.

    <section class="auto">
      <div></div>
    </section>
    <section class="cover">
      <div></div>
    </section>
    <section class="contain">
      <div></div>
    </section>
    

    div {
      background: blue linear-gradient(red, blue);
      mask-image: url("/shared-assets/images/examples/mask-star.svg");
    }
    
    .auto div {
      mask-size: auto;
    }
    
    .cover div {
      mask-size: cover;
    }
    
    .contain div {
      mask-size: contain;
    }
    
    section::before {
      content: attr(class);
      display: block;
      text-align: center;
      border-bottom: 1px solid;
    }
    
    body {
      display: flex;
      flex-flow: row wrap;
      gap: 10px;
    }
    section {
      border: 1px solid;
    }
    

The only difference is the size of the containing box (and the generated content):

css

    div {
      width: 70px;
      height: 70px;
    }
    

The `contain` value contains the mask within the origin box. The `cover` value covers it. In both cases, the mask shrinks while maintaining the original aspect ratio. With `auto`, the mask is clipped because the intrinsic dimensions are larger than the box dimensions.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-mask-size](https://drafts.csswg.org/css-masking/#the-mask-size) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size#see_also)

-----------------------------------------------------------------------------------------------------

*   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
     shorthand
*   [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    
*   [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
    
*   [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
    
*   [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
    
*   [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    
*   [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
    
*   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [`mask-border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-width)
    
*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS `mask` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
    
*   [Declaring multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mask-size/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mask-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")