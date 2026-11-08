*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#mdn-search)
    

`mask-origin` CSS property
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mask-origin`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the origin of a mask. This property determines the mask positioning area: the area within which a mask image is positioned. HTML elements can have masks contained within their content border box, padding box, or content box, whereas SVG elements (which don't have the associated CSS layout boxes) can have masks contained inside their fill, stroke, or view box. For elements rendered as multiple boxes, such as a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 of text that spans more than one line, the `mask-origin` property specifies which boxes the [`box-decoration-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
 property operates on to determine the mask positioning area.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    mask-origin: content-box;
    mask-origin: padding-box;
    mask-origin: border-box;
    mask-origin: fill-box;
    mask-origin: stroke-box;
    mask-origin: view-box;
    
    /* Multiple values */
    mask-origin: padding-box, content-box;
    mask-origin: view-box, fill-box, border-box;
    
    /* Global values */
    mask-origin: inherit;
    mask-origin: initial;
    mask-origin: revert;
    mask-origin: revert-layer;
    mask-origin: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#values)

The `mask-origin` property is a comma-separated list of `<coord-box>` keyword values, including:

[`content-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#content-box)

The position is relative to the [content box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_box_values#content-box)
.

[`padding-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#padding-box)

The position is relative to the [padding box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_box_values#padding-box)
.

[`border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#border-box)

The position is relative to the [border box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_box_values#border-box)
.

[`fill-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#fill-box)

The position is relative to the object bounding box.

[`stroke-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#stroke-box)

The position is relative to the stroke bounding box.

[`view-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#view-box)

Uses the nearest SVG viewport as reference box. If a [`viewBox`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)
 attribute is specified for the element creating the SVG viewport, the reference box is positioned at the origin of the coordinate system established by the `viewBox` attribute and the dimension of the reference box is set to the width and height values of the `viewBox` attribute.

There are three non-standard values that are shortcuts for standard `<coord-box>` values: `content` is an alias for `content-box`, `padding` is an alias for `padding-box`, and `border` is an alias for `border-box`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#description)

-------------------------------------------------------------------------------------------------------------

The `mask-origin` property is very similar to the [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
 property, but it has a different set of values and a different initial value. The initial value depends on if there is an associated CSS layout box; if yes, the default value is `border-box`. In comparison, the default for `background-origin` is `padding-box`.

For SVG elements without an associated CSS layout box, the values `content-box`, `padding-box`, and `border-box` (the default value) compute to `fill-box`, meaning the position is relative to the object bounding box. For HTML elements, if an SVG-related value of `fill-box`, `stroke-box`, or `view-box` is set, the value is computed to `border-box`.

An element can have multiple mask layers applied. The number of layers is determined by the number of comma-separated values in the [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 property value (even if one or more of those values is `none`). Each `mask-origin` value in the comma-separated list of values is matched with a comma-separated `mask-image` value, in the same order.

If the number of values in the two properties differs, any excess values of `mask-origin` are not used in cases where `mask-origin` has more values than `mask-image`. If `mask-origin` has fewer values than `mask-image`, the `mask-origin` values are repeated.

For elements rendered as a single box, this property specifies the mask positioning area — or the origin position — of the image referenced by the `mask-image` property.

For elements rendered as multiple boxes, such as inline boxes that span more than one line, the `mask-origin` property specifies which boxes the [`box-decoration-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
 property operates upon to determine the mask positioning area.

The `mask-origin` can cause the mask layer image to be clipped. For example, if the [`mask-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip)
 property is set to `padding-box`, the `mask-origin` is set to `border-box`, the [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
 is set to the `top left` edge, and the element has a border, then the mask layer image will be clipped at the top-left edge.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `border-box` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

mask-origin =   
  <coord-box>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<coord-box> =   
  <paint-box>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  view-box       
  
<paint-box> =   
  <visual-box>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fill-box      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stroke-box      
  
<visual-box> =   
  content-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  padding-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  border-box     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#examples)

-------------------------------------------------------------------------------------------------------

### [Comparing content, padding, and border](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#comparing_content_padding_and_border)

This example demonstrates basic usage while comparing three values of the `mask-origin` property.

#### HTML

We include four [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 elements, each containing one [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element.

html

    <section class="content">
      <div></div>
    </section>
    <section class="padding">
      <div></div>
    </section>
    <section class="border">
      <div></div>
    </section>
    <section class="comparison">
      <div></div>
    </section>
    

#### CSS

We apply [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
, [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, and [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 to every `<div>`. These create the reference points for the mask image origin. The `border` shorthand includes a [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
. We also include a [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
. These provide a green background and a blue border to mask. Finally, all our `<div>` elements are provided with a [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
.

css

    div {
      width: 100px;
      height: 100px;
      margin: 10px;
      border: 10px solid blue;
      background-color: #8cffa0;
      padding: 10px;
      mask-image: url("https://mdn.github.io/shared-assets/images/examples/mask-star.svg");
    }
    section {
      border: 1px solid black;
    }
    

We give each `<div>` a different `mask-origin` value.

css

    .content div {
      mask-origin: content-box;
    }
    
    .padding div {
      mask-origin: padding-box;
    }
    
    .border div {
      mask-origin: border-box;
    }
    
    .comparison div {
      mask-image: none;
    }
    

We also generate some text inside each `<section>` to indicate the mask origin for each `<div>` container.

css

    section::before {
      content: attr(class);
      display: block;
      text-align: center;
    }
    

    body {
      display: flex;
      flex-flow: row wrap;
      gap: 10px;
    }
    

#### Result

Notice the difference between the three values. In the first three boxes, respectively, the mask originates from:

*   The outside edge of the border.
*   The inside border edge, which is the outer edge of the padding box.
*   The inside padding edge, which is the outer edge of the content box.

The fourth box has no `mask-image` specified: it is a reference image, included to allow you to easily visualize the extent of the content and padding areas.

### [Multiple values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#multiple_values)

This example demonstrates using different `mask-origin` values for different `mask-image`s applied to a single element.

#### HTML

We include a single `<div>`.

html

    <div></div>
    

#### CSS

We apply three mask images instead of one, each with a different [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
. We also set the mask images not to repeat.

css

    div {
      width: 120px;
      height: 120px;
      margin: 10px;
      border: 10px solid blue;
      background-color: #8cffa0;
      padding: 10px;
      mask-image:
        url("https://mdn.github.io/shared-assets/images/examples/mask-star.svg"),
        url("https://mdn.github.io/shared-assets/images/examples/mask-star.svg"),
        url("https://mdn.github.io/shared-assets/images/examples/mask-star.svg");
      mask-position:
        top left,
        top right,
        bottom center;
      mask-repeat: no-repeat;
      mask-origin: content-box, border-box;
    }
    

#### Results

We have three `mask-image` values, but only two `mask-origin` values. This means the `mask-origin` values are repeated, as if we had set `mask-origin: content-box, padding-box, content-box;`. The `border-box` star, the only mask overlapping the border, is the top-right star.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-mask-origin](https://drafts.csswg.org/css-masking/#the-mask-origin) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin#see_also)

-------------------------------------------------------------------------------------------------------

*   [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    
*   [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    
*   [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
    
*   [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
    
*   [`mask-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
    
*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
     shorthand
*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS `mask` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
    
*   [Declaring multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mask-origin/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mask-origin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-origin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-origin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-origin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-origin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1474534461893381d54c502e655f334b5568e597%0A*+Document+last+modified%3A+2026-08-21T19%3A37%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")