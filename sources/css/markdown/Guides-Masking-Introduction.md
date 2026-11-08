*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#mdn-search)
    

Introduction to CSS masking
===========================

CSS masking enables you to reveal or hide parts of an element selectively by applying one or more mask images to it. These mask images can be gradients, images, or SVG sources. Unlike [CSS clipping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping)
, which either fully shows or hides areas of an element based on the shape of a single path, masking allows for nuanced transparency and blending effects based on the alpha transparency and, optionally, luminance of the mask images.

This guide introduces the concept of masking, the various mask image types, and how the luminance and alpha-transparency of the mask impact the portions of the element that are masked (made visible), versus the portions that are clipped (or hidden).

[What is masking in CSS?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#what_is_masking_in_css)

-------------------------------------------------------------------------------------------------------------------------------

In CSS, masks can be used to define areas of an element that are visible and other areas that are hidden. Mask layers, defined by one or more [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 sources, determine the areas of an element that should be visible and at what opacity.

**Note:** Multiple CSS masking property values can be set using the [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
 shorthand property.

With `alpha` masks, the opacity of the masked element matches the opacity of the mask applied. In CSS, masking is the opposite of a masquerade mask, where the face is hidden wherever the mask is opaque. In CSS, the areas of the element where its mask is fully opaque will be fully opaque and visible. Wherever the mask is fully transparent, the element will be fully hidden. Areas of the element that are masked by partially opaque mask areas will be partially opaque, matching the mask's opacity.

With alpha masks, the color of the mask is irrelevant. Only the opacity of the mask matters. With [luminance masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#alpha_transparency_versus_luminance)
, the brightness of the mask colors is taken into account when determining the opacity of the masked element. The brighter and more opaque the color, the more opaque the element. The darker and more transparent the color, the less opaque the mask will be.

Masks can be defined using CSS gradients, raster images (such as PNGs), and SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 elements. In this guide, we introduce the various mask image types as we discuss [opaqueness and transparency](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#opaqueness_versus_transparency)
, [luminance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#alpha_transparency_versus_luminance)
, and [masking versus CSS clipping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#svg_mask_as_mask_source)
.

Each mask layer consists of a [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
, which is [positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
 relative to an origin box. The mask images can be [sized](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
, [repeated](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
, and [clipped](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip)
. In cases where multiple mask images are declared, the way the [mask layers are composited](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite)
, or combined, can be set. These are discussed in the [masking properties guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
.

**Note:** All examples will be using the following image as the underlying element upon which masks will be applied:

![Pride flag](https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg)

[Opaqueness versus transparency](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#opaqueness_versus_transparency)

----------------------------------------------------------------------------------------------------------------------------------------------

With alpha masks, the visible areas of an element are defined by the alpha-transparency of the mask applied to it. Wherever the mask is fully opaque, the element will be visible. At every pixel where the mask is fully transparent, the element too will be fully hidden. Areas of the element that are masked by a partially opaque section of a mask will be partially opaque, matching the opacity of the mask applied to it.

### [With gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#with_gradients)

To demonstrate this, let's look at an example using a [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
 as the `mask-image`. CSS gradients, including conic gradients, can be used to create smooth transitions between visible and hidden areas.

In this case, the top-right corner of the mask is fully opaque, the top-left quadrant is fully transparent, and the bottom half has a smooth transition between opaque and transparent.

Note how the element on which the mask is applied has a fully visible top-right corner, the top-left quarter is hidden, and the bottom half transitions smoothly from visible to transparent, reflecting the visibility of the applied mask image.

With alpha masks, the color of the mask doesn't matter, only the transparency. In this example, we have a striped gradient with fully opaque red, semi-opaque red, and fully transparent stripes.

css

    .applied-mask {
      mask-image: repeating-linear-gradient(
        to bottom right,
        red 0 20px,
        #ff000055 20px 40px,
        transparent 40px 60px
      );
    }
    .mask-source {
      background: repeating-linear-gradient(
        to bottom right,
        red 0 20px,
        #ff000055 20px 40px,
        transparent 40px 60px
      );
    }
    

Note how the fully opaque mask areas reveal fully opaque element pixels, semi-transparent mask areas create semi-transparent areas, and fully transparent mask areas hide the associated areas completely.

### [With imported images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#with_imported_images)

The previous two examples used gradients as masks and background images. The mask image doesn't have to be a CSS image. It can be an external image or an SVG.

In this case we use an external PNG. The image contains a colorful heart with a transparent background.

css

    .applied-mask {
      mask-image: url("https://mdn.github.io/shared-assets/images/examples/colorful-heart.png");
      mask-size: 220px 220px;
    }
    .mask-source {
      background: url("https://mdn.github.io/shared-assets/images/examples/colorful-heart.png");
      background-size: 220px 220px;
    }
    

Note how the transparent mask areas crop the element; the only parts of the element that are visible are the areas where the mask is opaque. The color of the mask itself doesn't matter.

[Alpha transparency versus luminance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#alpha_transparency_versus_luminance)

--------------------------------------------------------------------------------------------------------------------------------------------------------

The `mask-mode` property's default value — `match-source` — sets the mode to either `alpha` or `luminance`, depending on the value. The `match-source` value resolves to `alpha` for all mask sources other than SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 elements. If the mask source is a `<mask>` element, `match-source` resolves to the `<mask>`'s [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
 property value, if set. Otherwise, it resolves to the value of the SVG [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/mask-type)
 attribute set on the `<mask>` element. If that is not explicitly set either, `match-source` will resolve to `luminance`.

If `mask-mode` resolves to `luminance`, or we explicitly set it to `luminance`, the colors of the mask will affect the mask opacity. In the previous demo, the `mask-mode` was not set, so the value defaulted to `match-source`. As the colorful heart image is a transparent PNG, `match-source` resolves to `alpha`. By explicitly setting this property, we can control the mode. In this demo, we change the `mask-mode` to `luminance`.

css

    .applied-mask {
      mask-mode: luminance;
    }
    

When applying `mask-mode: luminance` to the same mask as in the previous example, the areas of the element where the mask is **lightest** are more opaque, while **darker** areas are less opaque.

The opacity of a luminance mask is determined by the `R`, `G`, `B`, and `A` values of an [RGB](https://developer.mozilla.org/en-US/docs/Glossary/RGB)
 color using the formula:

`((0.2125 * R) + (0.7154 * G) + (0.0721 * B)) * A`

For example, the newest [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
 is `rebeccapurple`, which is `#663399`. While one might assume the lightness might be equivalent to the L of the `hsl()` color function, it's not that simple. The value `#663399` is equivalent to `rgb(40% 20% 60% / 1)` and `hsl(270 50% 40% / 1)`, but the brightness value is `27.134%`, not `40%`.

`((0.2125 * 0.4) + (0.7154 * 0.2) + (0.0721 * 0.6)) * 1 = 0.27134`

White has a brightness value of `100%`.

`((0.2125 * 1) + (0.7154 * 1) + (0.0721 * 1)) * 1 = 1`

Black's brightness is `0%`.

`((0.2125 * 0) + (0.7154 * 0) + (0.0721 * 0)) * 1 = 0`

We'll demonstrate this by adding white (`rgb(100% 100% 100%)`) with a lightness of `100%` at `27.234%` opacity to a `rebeccapurple`, `white`, and `black` linear gradient, which we'll then use to mask our image. This white resolves to the same opacity value:

`((0.2125 * 1) + (0.7154 * 1) + (0.0721 * 1)) * 0.27134 = 0.27134`

css

    .applied-mask {
      mask-image: repeating-linear-gradient(
        to bottom left,
        rebeccapurple 0 20px,
        rgb(100% 100% 100% / 0.27134) 20px 40px,
        black 40px 45px,
        white 45px 50px
      );
      mask-mode: luminance;
    }
    .mask-source {
      background: repeating-linear-gradient(
        to bottom left,
        rebeccapurple 0 20px,
        rgb(100% 100% 100% / 0.27134) 20px 40px,
        black 40px 45px,
        white 45px 50px
      );
    }
    

    :has(:checked) .applied-mask {
      mask-mode: alpha;
    }
    

    <label><input type="checkbox" /><code>mask-mode: alpha;</code></label>
    

The areas with a `white` mask are fully opaque. The areas with a `black` mask are fully transparent. The areas with a `rebeccapurple` mask and the areas with a `27.1234%` opaque white mask are both `27.1234%` opaque.

If you toggle the `mask-mode` to `alpha`, the color of the gradient no longer matters. The entire element will be opaque except the areas covered by the semi-opaque white.

The `mask-mode` property enables using raster images without alpha transparency, such as JPEGs, as mask images. A JPEG is made up of opaque pixels. Using a JPEG as a mask with its default `alpha` mask mode would hide the entire element. The `luminance` value of `mask-mode`, on the other hand, clips the element where the mask is black (has no lightness), is fully opaque where the mask is opaque white (100% lightness), with other areas being semi-transparent based on the lightness of the mask area masking it.

In this example, we have a white moon against a black night sky.

css

    .applied-mask {
      mask-image: url("https://mdn.github.io/shared-assets/images/examples/moon.jpg");
      mask-mode: luminance;
      mask-size: 220px;
    }
    .mask-source {
      background: url("https://mdn.github.io/shared-assets/images/examples/moon.jpg");
      background-size: 220px;
    }
    

The element is clipped and not visible where the sky is black. The image is most visible where the moon is at it's lightest.

In this case, if you toggle the `mask-mode` to `alpha`, the entire element will be visible as the entire mask is opaque.

[SVG `<mask>` as mask source](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#svg_mask_as_mask_source)

------------------------------------------------------------------------------------------------------------------------------------

A mask can be any type of CSS [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 or a `<mask-source>`. A `<mask-source>` is a [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 reference to an SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 element. This is similar to clipping with the CSS [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 property, in which case the "mask" is an SVG [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
 element instead (with `clip-path`, the luminance of the path doesn't matter).

In this example, we define an SVG with a `<mask>` element, an identical [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
 element, and an identical [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
 element so you can view the mask and clip path source.

html

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag"
      class="applied-mask" />
    <svg class="mask-source">
      <mask id="mask-heart">
        <path
          d="M20,70 A40,40,0,0,1,100,70 A40,40,0,0,1,180,70 Q180,130,100,190 Q20,130,20,70 Z"
          fill="rgb(255 0 0 / 0.5)"
          stroke="rgb(255 255 255 / 1)"
          stroke-width="20" />
      </mask>
      <clippath id="clip-heart">
        <path
          d="M20,70 A40,40,0,0,1,100,70 A40,40,0,0,1,180,70 Q180,130,100,190 Q20,130,20,70 Z"
          fill="rgb(255 0 0 / 0.5)"
          stroke="rgb(255 255 255 / 1)"
          stroke-width="20" />
      </clippath>
      <path
        d="M20,70 A40,40,0,0,1,100,70 A40,40,0,0,1,180,70 Q180,130,100,190 Q20,130,20,70 Z"
        fill="rgb(255 0 0 / 0.5)"
        stroke="rgb(255 255 255 / 1)"
        stroke-width="20" />
    </svg>
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag"
      class="applied-clip" />
    

css

    .applied-mask {
      mask-image: url("#mask-heart");
    }
    .applied-clip {
      clip-path: url("#clip-heart");
    }
    

    :has(:checked) .applied-mask {
      mask-mode: alpha;
    }
    body {
      flex-flow: row wrap;
    }
    

    <label><input type="checkbox" /><code>mask-mode: alpha;</code></label>
    

Because the image source is a `<mask>`, and the mask has neither the `mask-type` CSS property nor the `mask-type` SVG attribute set, the `mask-type` defaults to `alpha`, so the default of `mask-mode: match-source` resolves to `luminance`. This is because, for mask sources that are SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 elements, the `mask-type` defaults to `luminance` unless the [`mask-type`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/mask-type)
 attribute is explicitly set to `alpha`.

As we haven't set the `mask-type` attribute or CSS property on our mask, the `mask-mode` property default of `match-source` resolves to `luminance`. Toggle the checkbox to set the `mask-mode` value to `alpha` or allow it to default to `match-source`.

This example also demonstrated the difference between masking and clipping in CSS. You'll note that luminance and alpha-transparency are relevant to masking but not to clipping. Masking can be used to control the opacity of an element, while clipping shows everything inside the clipping path and fully hides the parts of the element outside the clip path. Clipped areas are completely invisible, whereas masked areas can be partially or fully visible.

If all you need are shapes, clipping may suffice. But if you need fading, variable opacity, or even control of position and size (which we'll discuss in a separate guide), masking is more suitable.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction#see_also)

--------------------------------------------------------------------------------------------------

*   [Introduction to CSS clipping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping)
    
*   [CSS `mask` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
    
*   [Declaring multiple masks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/masking/introduction/index.md?plain=1 "Folder: en-us/web/css/guides/masking/introduction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMasking%2FIntroduction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmasking%2Fintroduction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMasking%2FIntroduction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmasking%2Fintroduction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")