*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#mdn-search)
    

`mask-image` CSS property
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`mask-image`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the image that is used as the mask layer for an element, hiding sections of the element on which the masking image is set based on the alpha channel of the mask image and, depending on the [`mask-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
 property value, the luminance of the mask image's colors.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    mask-image: none;
    
    /* <mask-source> value */
    mask-image: url("masks.svg#mask1");
    
    /* <image> values */
    mask-image: linear-gradient(black, transparent);
    mask-image: image(url("mask.png"), skyblue);
    
    /* Multiple values */
    mask-image: url("mask.png"), linear-gradient(black 25%, transparent 35%);
    
    /* Global values */
    mask-image: inherit;
    mask-image: initial;
    mask-image: revert;
    mask-image: revert-layer;
    mask-image: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#none)

This keyword is interpreted as a transparent black image layer.

[`<mask-source>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#mask-source)

A [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 reference to a [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 or to a CSS image.

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)

An image value used as a mask image layer.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#description)

------------------------------------------------------------------------------------------------------------

The `mask-image` property provides a mask that hides part of the element to which it is applied. The value is a comma-separated list of mask references. Each mask reference is an `<image>`, a `<mask-source>`, or the keyword `none`.

An `<image>` can be any type of image, including generated images such as [CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
.

If only one value is specified in the `mask-image` property value, and that value is `none`, no masking effect will be apparent. If multiple values are specified, a `none` value included in the list may have no direct effect, however, other `mask-*` values in the same list position will apply to a transparent black mask layer and have no visual effect.

Only image sources served over HTTP and HTTPS protocols are accepted as `<image>` values due to the [CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)
 policy. Images served locally, including relative or absolute `file://` protocols, are not accepted, and will render as transparent black. To test URL image sources locally, [set up a local server](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Tutorials/CycleTracker/Secure_connection#localhost)
.

A mask will be counted as a transparent black image layer, not revealing anything, in the following cases:

*   The mask image is empty (zero width or zero height).
*   The mask image fails to download.
*   The browser does not support the mask image format.
*   The mask image doesn't exist.
*   The mask value doesn't point to a mask image.

The default value of the [`mask-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
 property is `match-source`, which means the mode is defined by the mode of the mask image itself. The mask image's mode is generally `alpha` except when the mask source is an SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 element, in which case the mode is `luminance` unless the mode is changed to `alpha` via the CSS [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
 property or SVG [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/mask-type)
 attribute.

The `mask-mode` value is significant, because it determines whether the masking effect depends on the image source's alpha channel values alone or a combination of those and the mask's luminance (the lightness/darkness of the colors that make up the `mask-image`):

*   In all cases, the alpha transparency of the mask matters; element areas masked by opaque sections of the `mask-image` will be rendered, while areas masked by transparent image sections are hidden.
*   When the `mask-mode` value is set or resolves to `alpha`, only the alpha-channel of the colors matter; the hue, lightness, etc., don't matter.
*   If the `mask-mode` property is set or defaults to `luminance`, the masking value is the luminance value of each color multiplied by its alpha value. The `mask-mode` will resolve to `luminance` if explicitly set to that value, or if the property is set to `match-source` and the `mask-image` source is an SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
     that does not have its [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
     property or [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/mask-type)
     attribute explicitly set to `alpha`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements; In SVG, it applies to container elements excluding the [`<defs>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/defs)<br> element and all graphics elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)<br> values made absolute |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#formal_syntax)

----------------------------------------------------------------------------------------------------------------

mask-image =   
  <mask-reference>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<mask-reference> =   
  none           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mask-source>    
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-set()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cross-fade()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <element()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<gradient>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
        
  
<mask-source> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    
  
[<image()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  image( <image-tags>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image-src>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 , [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
! )    
  
[<image-set()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
 =   
  image-set( <image-set-option>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<cross-fade()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
 =   
  cross-fade( <cf-image>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<element()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
 =   
  element( <id-selector> )    
  
<image-tags> =   
  ltr  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rtl    
  
<image-src> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
<image-set-option> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<resolution>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 type( [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<cf-image> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<id-selector> =   
  <hash-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#examples)

------------------------------------------------------------------------------------------------------

### [Gradient as a mask image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#gradient_as_a_mask_image)

In this example, we use an `<image>` value as a mask, defining a CSS [radial gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
 as our mask image to create a round image with a soft edge.

#### HTML

We include an HTML [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element, which will also be used in all other examples.

html

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    

#### CSS

We use the CSS [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
 function to create a mask that has a black circle with a radius that is half the width of the mask, before transitioning to being transparent over 10%.

css

    img {
      mask-image: radial-gradient(black 50%, transparent 60%);
    }
    

#### Results

The part of the original element that is masked by the black circle is fully opaque, fading to transparent as the mask fades to transparent.

### [Image resource as a mask image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#image_resource_as_a_mask_image)

In this example, the `<mask-source>` used as our mask image is an external SVG.

#### HTML

We include the same image as the previous example. We've also included the image we will be using as the mask; a star whose [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
 is `0.5`, or 50% opaque.

html

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    
    <img
      src="https://mdn.github.io/shared-assets/images/examples/mask-star.svg"
      alt="A star" />
    

#### CSS

We use `mask-star.svg` as a mask image on our first image:

css

    img:first-of-type {
      mask-image: url("https://mdn.github.io/shared-assets/images/examples/mask-star.svg");
    }
    

#### Results

The mask is semi-opaque, which is why the colors are not as vibrant as the previous example. The part of the image that is visible is 50% opaque; the opacity of the mask applied. The mask is smaller than the image, so repeats by default. We could have used [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
 to control the repeating or [`mask-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
 to change the size of the mask, which we do in the next example.

### [Multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#multiple_masks)

This example demonstrates applying multiple masks.

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    

#### CSS

We apply two masks — the same semi-transparent SVG as in the previous example, and a [`repeating-radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
. We control the size of the masks using the [`mask-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
 property. Because our first mask is not sized at 100%, we make sure our masks are centered and don't repeat with the [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
 and [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
 properties, respectively.

css

    img {
      mask-size: 95%, 100%;
      mask-position: center;
      mask-repeat: no-repeat;
      mask-image:
        url("https://mdn.github.io/shared-assets/images/examples/mask-star.svg"),
        repeating-radial-gradient(transparent 0 5px, black 5px 10px);
    }
    

#### Results

### [Masking with SVG `<mask>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#masking_with_svg_mask)

This example demonstrates using SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 elements as masks. In this case, the color of the mask matters as the [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
 value for SVG masks defaults to `luminance`, which means white opaque areas (100% luminance) will be masked and visible, transparent and black areas (0% luminance) will be clipped, and anything in between will be partially masked.

#### HTML

We've included an `id` for each of our four images, and an SVG that contains an equal number of `<mask>` elements.

html

    <img
      id="green"
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      id="stroke"
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      id="both"
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      id="alphaMode"
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    
    <svg height="0" width="0">
      <mask id="greenMask">
        <path
          d="M20,70 A40,40,0,0,1,100,70 A40,40,0,0,1,180,70 Q180,130,100,190 Q20,130,20,70 Z"
          fill="green" />
      </mask>
      <mask id="strokeMask">
        <path
          d="M20,70 A40,40,0,0,1,100,70 A40,40,0,0,1,180,70 Q180,130,100,190 Q20,130,20,70 Z"
          fill="none"
          stroke="white"
          stroke-width="20" />
      </mask>
      <mask id="bothMask">
        <path
          d="M20,70 A40,40,0,0,1,100,70 A40,40,0,0,1,180,70 Q180,130,100,190 Q20,130,20,70 Z"
          fill="green"
          stroke="white"
          stroke-width="20" />
      </mask>
      <mask id="black">
        <path
          d="M20,70 A40,40,0,0,1,100,70 A40,40,0,0,1,180,70 Q180,130,100,190 Q20,130,20,70 Z"
          fill="black" />
      </mask>
    </svg>
    

    <p>
      <label>
        <input type="checkbox" />
        Set the <code>mask-mode</code> to <code>alpha</code>.
      </label>
    </p>
    

#### CSS

We apply a different `<mask>` to each `<img>`. No part of the last image, with the `black` fill, will be visible by default. In this case, while all colors used in this example are fully opaque, the `mask-mode` defaults to `match-type`, which resolves to `luminance` in this case.

css

    #green {
      mask-image: url("#greenMask");
    }
    #stroke {
      mask-image: url("#strokeMask");
    }
    #both {
      mask-image: url("#bothMask");
    }
    #alphaMode {
      mask-image: url("#black");
    }
    
    body:has(:checked) img {
      mask-mode: alpha;
    }
    

The luminance values of `black`, `white`, and `green` are `0`, `100`, and [`46.228`](https://www.colorhexa.com/008000 "External link (opens in new tab)")
, respectively. This means the areas where the mask is white will be visible, whereas areas where the mask is black or fully transparent will be clipped (not visible). Areas where the mask is green will be visible but lighter, equivalent to having a white mask that is 46.228% opaque.

#### Results

Toggle the checkbox to toggle the value of the `mask-mode` between `alpha` (checked) and the initial value, which resolves to `luminance` (unchecked). When `alpha` is used, the color of the mask doesn't matter; all that matters is the alpha-transparency. When the value resolves to `luminance`, `white` areas are visible, `black` areas are not, and `green` areas are visible but at an opacity that matches the luminance of the color `green`. When `mask-mode` is set to `alpha`, the colors are equivalent as they are all fully opaque.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-mask-image](https://drafts.csswg.org/css-masking/#the-mask-image) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image#see_also)

------------------------------------------------------------------------------------------------------

*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
     shorthand
*   [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
    
*   [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
    
*   [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
    
*   [`mask-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
    
*   [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
    
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    
*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS `mask` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
    
*   [Declaring multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/mask-image/index.md?plain=1 "Folder: en-us/web/css/reference/properties/mask-image (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-image&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-image%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmask-image%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmask-image%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")