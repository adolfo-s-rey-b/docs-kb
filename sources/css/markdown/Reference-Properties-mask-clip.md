*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#mdn-search)
    

`mask-clip` CSS property
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mask-clip`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property determines the area which is affected by a mask. The painted content of an element must be restricted to this area.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#syntax)

-------------------------------------------------------------------------------------------------

css

    /* <coord-box> values */
    mask-clip: content-box;
    mask-clip: padding-box;
    mask-clip: border-box;
    mask-clip: fill-box;
    mask-clip: stroke-box;
    mask-clip: view-box;
    
    /* Keyword value */
    mask-clip: no-clip;
    
    /* Multiple values */
    mask-clip: padding-box, no-clip;
    mask-clip: view-box, fill-box, border-box;
    
    /* Global values */
    mask-clip: inherit;
    mask-clip: initial;
    mask-clip: revert;
    mask-clip: revert-layer;
    mask-clip: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#values)

The property accepts a comma-separated list of keyword values. Each value is a `<coord-box>` or `no-clip`:

[`content-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#content-box)

The painted content is clipped to the content box.

[`padding-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#padding-box)

The painted content is clipped to the padding box.

[`border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#border-box)

The painted content is clipped to the border box.

[`fill-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#fill-box)

The painted content is clipped to the object bounding box.

[`stroke-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#stroke-box)

The painted content is clipped to the stroke bounding box.

[`view-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#view-box)

Uses the nearest SVG viewport as reference box. If a [`viewBox`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)
 attribute is specified for the element creating the SVG viewport, the reference box is positioned at the origin of the coordinate system established by the `viewBox` attribute and the dimension of the reference box is set to the width and height values of the `viewBox` attribute.

[`no-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#no-clip)

The painted content is not clipped.

[`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#border)

This keyword behaves the same as `border-box`.

[`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#padding)

This keyword behaves the same as `padding-box`.

[`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#content)

This keyword behaves the same as `content-box`.

[`text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#text)

This keyword clips the mask image to the text of the element.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#description)

-----------------------------------------------------------------------------------------------------------

The `mask-clip` property defines the area of the element that is affected by the applied mask.

For mask layer images that do not reference an SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 element, the `mask-clip` property defines the mask painting area, or the area affected by the mask. The painted content of the element will be restricted to this area.

The `mask-clip` property has no effect on a mask layer image that references a `<mask>` element. The `<mask>` element's [`x`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/x)
, [`y`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/y)
, [`width`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/height)
, and [`maskUnits`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/maskUnits)
 attributes determine the mask painting area when the source of the [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 is a `<mask>`.

An element can have multiple mask layers applied. The number of layers is determined by the number of comma-separated values in the `mask-image` property value (even if a value is `none`). Each `mask-clip` value in the comma-separated list of values is matched up with the `mask-image` values, in order. If the number of values in the two properties differs, any excess values of `mask-clip` are not used, or, if `mask-clip` has fewer values than `mask-image`, the `mask-clip` values are repeated.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `border-box` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#formal_syntax)

---------------------------------------------------------------------------------------------------------------

mask-clip =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <coord-box> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 no-clip [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#examples)

-----------------------------------------------------------------------------------------------------

### [Clipping a mask to the border box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#clipping_a_mask_to_the_border_box)

This examples demonstrates three `mask-clip` values.

#### HTML

We include three elements, each with a different `<coord-box>` value as a class name.

html

    <div class="border-box"></div>
    <div class="padding-box"></div>
    <div class="content-box"></div>
    

#### CSS

The CSS defines the element to have a background, border, padding, and margin, along with a mask image, with each `<div>` having a different `<coord-box>`. We generated content with the name of the class, moving that text up 10px to prevent it from being masked out of view.

css

    div {
      width: 100px;
      height: 100px;
      background-color: #8cffa0;
      margin: 10px;
      border: 20px solid #8ca0ff;
      padding: 20px;
      mask-image: url("https://mdn.github.io/shared-assets/images/examples/mdn.svg");
      mask-size: 100% 100%;
    }
    .content-box {
      mask-clip: content-box;
    }
    .border-box {
      mask-clip: border-box;
    }
    .padding-box {
      mask-clip: padding-box;
    }
    div::before {
      content: attr(class);
      position: relative;
      top: -10px;
    }
    

    body {
      display: flex;
      flex-flow: row wrap;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-mask-clip](https://drafts.csswg.org/css-masking/#the-mask-clip) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip#see_also)

-----------------------------------------------------------------------------------------------------

*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
     shorthand
*   [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    
*   [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
    
*   [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
    
*   [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
    
*   [`mask-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
    
*   [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
    
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    
*   [Introduction to CSS clipping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping)
    
*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS `mask` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
    
*   [Declaring multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mask-clip/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mask-clip (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-clip&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-clip%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-clip%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-clip%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")