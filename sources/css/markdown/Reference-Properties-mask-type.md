*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#mdn-search)
    

`mask-type` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mask-type`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property applies to the SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 element. It defines whether to use the _luminance_ (brightness) or _alpha_ (transparency) content of the mask. This property may be overridden by the [`mask-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
 property. The `mask-type` property has no effect on image or gradient masks.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#syntax)

-------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#values)

[`alpha`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#alpha)

Indicates that the alpha (transparency) values of the `<mask>` should be used.

[`luminance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#luminance)

Indicates that the [luminance (brightness) values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#understanding_luminance)
 of the `<mask>` should be used.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#description)

-----------------------------------------------------------------------------------------------------------

The `mask-type` property is only relevant for the SVG `<mask>` element. If you set `mask-type: luminance`, the mask will use how bright each part of the mask is; if you set `mask-type: alpha`, it will use how transparent or opaque each part of the mask is.

### [Default behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#default_behavior)

By default, the SVG `<mask>` element uses `mask-type: luminance`. This means both the color and the transparency of the mask content affect masking. Whether the mask is opaque partially depends on the lightness of the color of the opaque areas:

*   Fully opaque white areas (100% luminance) will be masked and visible.
*   Black (0% luminance) or fully transparent areas will be clipped and invisible.
*   Areas with intermediate luminance values will be partially masked, reflecting both the luminance, or lightness of the mask color, and the alpha transparency of each area of the mask.

### [Understanding luminance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#understanding_luminance)

The opacity of a `luminance` mask is determined by the `R`, `G`, `B`, and `A` values of an `rgb()` color using the following formula:

`((0.2125 * R) + (0.7154 * G) + (0.0721 * B)) * A`

For example, the color `green` (`#008000` or `rgb(0% 50% 0% / 1)`) has a luminance value of `35.77%`. Any area masked by a solid `green` luminance mask will be `35.77%` visible. If the `mask-type` is set to `alpha`, the same fully opaque `green` color will make the masked area `100%` visible.

If the SVG `<mask>` element has `fill="rgb(0 0 0 / 0.5)"`, which is a 50% transparent black, the corresponding shape on the masked element will display at 50% opacity when `mask-type` is set to `alpha` because the alpha values is `0.5` (50% opacity). But if the `mask-type` defaults to or is set as `luminance` the masked area will be fully clipped and invisible because its luminance is `0`.

### [Effect of `mask-mode` on `mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#effect_of_mask-mode_on_mask-type)

While the `mask-type` property is set on the SVG `<mask>` element, the [`mask-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
 property is set on the element being masked (the element you're applying the mask to). If the mask image source is not an SVG `<mask>`, this property has no effect.

The default value of `mask-mode` is `match-source`, which means the browser uses the `mask-type` value from the `<mask>` element to determine how to interpret it. If `mask-mode` is set to a value other than `match-source`, that value takes precedence and overrides the `mask-type` value of the applied mask.

If the `<mask>` is defined as the mask image's source, and the `mask-mode` is set as or defaults to `match-source`, the `mask-mode` will resolve to the `<mask>` element's `mask-type` value: `luminance` or `alpha`. If not explicitly set, the value defaults to `luminance`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `luminance` |
| Applies to | [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)<br> elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#formal_syntax)

---------------------------------------------------------------------------------------------------------------

mask-type =   
  luminance  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  alpha        

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#examples)

-----------------------------------------------------------------------------------------------------

### [Using the `mask-type` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#using_the_mask-type_property)

This example demonstrates how to use the `mask-type` property and the effect of its different values.

#### HTML

We've included two images that will be masked. Other than their class names, the two images are identical. We've also included an SVG with two `<mask>` elements. Other than their `id` values, the two masks are also identical: each has a green and white heart shape and a semi-transparent white-and-black-filled circle.

#### CSS

We apply the `mask-type` property to the `<mask>` elements, and then apply the `<mask>` elements and the mask source to the images.

#### Result

As the default value for the `mask-mode` property is `match-source`, the first mask uses the alpha channels only to define the mask: the white and green are fully opaque, and the 50% white and black colors are 50% opaque because only the alpha value of the colors matters. The second example uses the luminance of the colors to determine the opacity of the mask, with white being brighter than green, and semi-transparent white being brighter than semi-transparent black.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-mask-type](https://drafts.csswg.org/css-masking/#the-mask-type) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type#see_also)

-----------------------------------------------------------------------------------------------------

*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
    
*   [`mask-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
    
*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module
*   SVG [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/mask-type)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mask-type/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mask-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")