*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#mdn-search)
    

`image-rendering` CSS property
==============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`image-rendering`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets an image scaling algorithm. The property applies to an element itself, to any images set in its other properties, and to its descendants.

The [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 will scale an image when the page author specifies dimensions other than its natural size. Scaling may also occur due to user interaction (zooming). For example, if the natural size of an image is `100×100px`_,_ but its actual dimensions are `200×200px` (or `50×50px`), then the image will be upscaled (or downscaled) using the algorithm specified by `image-rendering`. This property has no effect on non-scaled images.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#try_it)

-------------------------------------------------------------------------------------------------------

    image-rendering: auto;
    

    image-rendering: smooth;
    

    image-rendering: crisp-edges;
    

    image-rendering: pixelated;
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/lizard.png" />
    </section>
    

    #example-element {
      height: 480px;
      object-fit: cover;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    image-rendering: auto;
    image-rendering: smooth;
    image-rendering: crisp-edges;
    image-rendering: pixelated;
    
    /* Global values */
    image-rendering: inherit;
    image-rendering: initial;
    image-rendering: revert;
    image-rendering: revert-layer;
    image-rendering: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#auto)

The scaling algorithm is UA dependent. Since version 1.9 (Firefox 3.0), Gecko uses _bilinear_ resampling (high quality).

[`smooth`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#smooth)

The image should be scaled with an algorithm that maximizes the appearance of the image. In particular, scaling algorithms that "smooth" colors are acceptable, such as bilinear interpolation. This is intended for images such as photos.

[`crisp-edges`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#crisp-edges)

The image is scaled with an algorithm such as "nearest neighbor" that preserves contrast and edges in the image. Generally intended for images such as pixel art or line drawings, no blurring or color smoothing occurs.

[`pixelated`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#pixelated)

The image is scaled with the "nearest neighbor" or similar algorithm to the nearest integer multiple of the original image size, then uses smooth interpolation to bring the image to the final desired size. This is intended to preserve a "pixelated" look without introducing scaling artifacts when the upscaled resolution isn't an integer multiple of the original.

**Note:** The values `optimizeQuality` and `optimizeSpeed` present in an early draft (and coming from its SVG counterpart [`image-rendering`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/image-rendering)
) are defined as synonyms for the `smooth` and `pixelated` values respectively.

**Note:** The [CSS images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
 module defines a `high-quality` value for the `image-rendering` property to provide a preference for higher-quality scaling, however, this is not supported in any browsers.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

image-rendering =   
  auto          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  smooth        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  high-quality  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pixelated     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  crisp-edges     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#examples)

-----------------------------------------------------------------------------------------------------------

### [Setting image scaling algorithms](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#setting_image_scaling_algorithms)

In this example, an image is repeated four times, with each having a different `image-rendering` value applied.

    <div>
      <img
        class="auto"
        alt="A small photo of some white and yellow flower against a leafy green background. The image is about 33% smaller than the size it is being displayed at. This upscaling causes the image to appear blurry, with notable soft edges between objects."
        src="blumen.jpg" />
      <img
        class="smooth"
        alt="The same photo as the previous image, which is also being upscaled the same amount. Browsers that support the smooth value for the image-rendering property display the image with the maximize appearance."
        src="blumen.jpg" />
      <img
        class="pixelated"
        alt="The same photo as the previous image, which is also being upscaled the same amount. Browsers that support the pixelated value for the image-rendering property display the image as very pixelated. Individual pixels are clearly visible and edges appear much sharper."
        src="blumen.jpg" />
      <img
        class="crisp-edges"
        alt="The same photo as the previous images, which is also being upscaled the same amount. Browsers that support the crisp-edges value for the image-rendering property display the image as very pixelated. In these examples, there is virtually no perceivable difference between the pixelated and crisp-edges versions."
        src="blumen.jpg" />
    </div>
    

    img {
      height: 200px;
    }
    

#### CSS

css

    .auto {
      image-rendering: auto;
    }
    
    .smooth {
      image-rendering: smooth;
    }
    
    .pixelated {
      image-rendering: pixelated;
    }
    
    .crisp-edges {
      image-rendering: crisp-edges;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 3  <br>\# the-image-rendering](https://drafts.csswg.org/css-images/#the-image-rendering) |
| [Scalable Vector Graphics (SVG) 2  <br>\# ImageRendering](https://w3c.github.io/svgwg/svg2-draft/painting.html#ImageRendering) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    
*   [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
    
*   [`image-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation)
    
*   [`image-resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution)
    
*   [CSS images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
     module
*   SVG [`image-rendering`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/image-rendering)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/image-rendering/index.md?plain=1 "Folder: en-us/web/css/reference/properties/image-rendering (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fimage-rendering&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fimage-rendering%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fimage-rendering%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fimage-rendering%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")