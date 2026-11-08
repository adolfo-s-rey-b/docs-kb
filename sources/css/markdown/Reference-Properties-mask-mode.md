*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#mdn-search)
    

`mask-mode` CSS property
========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mask-mode`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property is set on the element being masked. It sets whether the mask reference defined by the [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 is treated as a luminance or alpha mask.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#syntax)

-------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    mask-mode: alpha;
    mask-mode: luminance;
    mask-mode: match-source;
    
    /* Multiple values */
    mask-mode: alpha, match-source;
    
    /* Global values */
    mask-mode: inherit;
    mask-mode: initial;
    mask-mode: revert;
    mask-mode: revert-layer;
    mask-mode: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#values)

The `mask-mode` property can take multiple comma-separated `<masking-mode>` keyword values, including:

[`alpha`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#alpha)

Indicates that the alpha (transparency) values of the mask image should be used.

[`luminance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#luminance)

Indicates that the [luminance (brightness)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#understanding_luminance)
 values of the mask image should be used.

[`match-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#match-source)

Indicates that the type of mask is determined by the source. This is the default property value.

*   If the [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
     references an SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
    , its [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
     property value is used, or its [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/mask-type)
     attribute, if present. If neither is explicitly set, this value defaults to `luminance`.
*   If the mask image source is an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
     or a [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    , the `alpha` values of the mask image are used.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#description)

-----------------------------------------------------------------------------------------------------------

A mask transfers its transparency, and depending on the mask type, its luminance, to the element it is masking. If the mask is of type [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
, by default the alpha values of the mask image determine the visibility of each part of the masked element: where the mask is opaque, the corresponding part of the masked element is visible; where the mask is translucent, the element is as well, with those areas of the element being hidden. This is the default behavior for `<image>` masks when the `mask-mode` property is set to or defaults to `match-source`, and it is always the case when the `mask-mode` is explicitly set to `alpha`.

### [Understanding luminance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#understanding_luminance)

In the case of `luminance` masks, the visibility of the masked element depends on both the opacity of the mask and the lightness of the color of the opaque areas. White (100% luminance) opaque areas (alpha = 1) will be masked and visible, and black areas (0% luminance) transparent (alpha = 0) will be clipped. Areas with colors in between white and black and with partial opacity will be partially masked, reflecting the luminance and alpha transparency of each color making up the mask.

The opacity of a `luminance` mask is determined by the `R`, `G`, `B`, and `A` values of an `rgb()` color using the formula:

`((0.2125 * R) + (0.7154 * G) + (0.0721 * B)) * A`

For example, the color `green` is `#008000` or `rgb(0% 50% 0% / 1)`. In a `luminance` mask, any area masked by a solid `green` mask will be `35.77%` opaque. If the `mask-mode` for this mask is set to `alpha`, since `green` is a fully opaque color, the masked area will be `100%` opaque.

### [Multiple values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#multiple_values)

Each `mask-mode` value is a comma-separated list of values. When multiple values are present, each value corresponds to a mask layer in the same position in the [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 property. The values define whether the associated mask images are treated as a `luminance` or an `alpha` mask.

### [Understanding `match-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#understanding_match-source)

In the case of `match-source`, whether `luminance` or `alpha` is used depends on the mask mode of the mask source. If the `mask-image` property values is a reference to an SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 element, the `<mask>` element's [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
 property value is used. If there is no CSS `mask-type` property set on the `<mask>` element, the value of the `<mask>` element's [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/mask-type)
 attribute is used, if present and supported. If neither is explicitly set, this value defaults to `luminance`; but only in the case of the `<mask>` element as the mask source. Otherwise, as noted before, if the mask image source is an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
, rather than an SVG `<mask>`, the `alpha` values of the mask layer image is used.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `match-source` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#formal_syntax)

---------------------------------------------------------------------------------------------------------------

mask-mode =   
  <masking-mode>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<masking-mode> =   
  alpha         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  luminance     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  match-source    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#examples)

-----------------------------------------------------------------------------------------------------

### [Usage and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#usage_and_values)

This example demonstrates the basic usage and different values of the `mask-mode` property.

#### HTML

We include three `<div>` elements, so we can demonstrate the three enumerated `mask-mode` keyword values.

html

    <div class="alpha">ALPHA</div>
    <div class="luminance">LUMINANCE</div>
    <div class="matchSource">MATCH-SOURCE</div>
    

#### CSS

Each `<div>` is provided with the same background and masking image. The only difference between each `<div>` is the value of the `mask-mode` property:

css

    div {
      background: blue linear-gradient(red, blue);
      mask-image: url("https://mdn.github.io/shared-assets/images/examples/mdn.svg");
    }
    
    .alpha {
      mask-mode: alpha;
    }
    
    .luminance {
      mask-mode: luminance;
    }
    
    .matchSource {
      mask-mode: match-source;
    }
    

    div {
      width: 227px;
      height: 200px;
      float: left;
      text-align: center;
      line-height: 65px;
      color: white;
      text-shadow: 1px 1px 2px black;
      font-family: sans-serif;
    }
    

#### Results

Because the mask source is an `<image>` and not an SVG `<mask>`, the `match-source` value resolves to `alpha`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-mask-mode](https://drafts.csswg.org/css-masking/#the-mask-mode) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode#see_also)

-----------------------------------------------------------------------------------------------------

*   [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
    
*   [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    
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

This page was last modified on Aug 31, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mask-mode/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mask-mode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-mode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-mode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-mode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-mode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4ad860d817cf6d8ca24f41b3846b29e158934d27%0A*+Document+last+modified%3A+2026-08-31T05%3A51%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")