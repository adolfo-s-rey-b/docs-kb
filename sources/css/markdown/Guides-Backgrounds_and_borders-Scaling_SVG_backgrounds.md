*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#mdn-search)
    

Scaling SVG backgrounds
=======================

Given the flexibility of SVG images, there's a lot to keep in mind when using them as background images with the [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 property, and even more to keep in mind when scaling them using the [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 property. This article describes how scaling of SVG images is handled when using these properties.

[The background sizing algorithm](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#the_background_sizing_algorithm)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The algorithm used to determine the background size of a background image can, for the most part, be summarized by these four rules. There are some edge cases that aren't covered by these rules, but this covers the majority of cases.

1.  If [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
     specifies a fixed dimension (that is, percentages and relative units are fixed by their context), that dimension wins.
2.  If the image has an intrinsic ratio (that is, its width:height ratio is constant, such as 16:9, 4:3, 2.39:1, 1:1, and so forth), the rendered size preserves that ratio.
3.  If the image specifies a size, and the size isn't modified by `constrain` or `cover`, that specified size wins.
4.  If none of the above cases are met, the image is rendered at the same size as the background area.

It's worth noting that the background sizing algorithm only cares about the image's dimensions and proportions, or lack thereof. An SVG image with fixed dimensions will be treated just like a raster image of the same size.

**Note:** If you are trying to stretch your SVG to a different [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 with CSS—for example in order to stretch it over the page background—make sure your SVG includes `preserveAspectRatio="none"`. Find out more about [`preserveAspectRatio`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/preserveAspectRatio)
.

[Source image examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#source_image_examples)

-------------------------------------------------------------------------------------------------------------------------------------------------------

Before diving in to look at the results of using different kinds of SVG source images and seeing how they look when used with [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
, it will be helpful to look at a few example source images that have different dimensions and sizing settings, which we will later use as our `background-image` values in our examples. The browser renders [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
 images as `300px` wide and `150px` tall by default.

### [Dimensionless and proportionless](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#dimensionless_and_proportionless)

This SVG gradient image is both dimensionless and proportionless. It doesn't care what size it is, nor does it care about remaining at a particular aspect ratio. This would make a good gradient desktop background that would work regardless of your screen size and its aspect ratio.

### [One specified dimension and proportionless](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#one_specified_dimension_and_proportionless)

This image specifies a width of 100 pixels but no height or intrinsic ratio. This is, basically, a thin strip of wallpaper that could be stretched across the entire height of a block.

html

    <svg width="100">
      <title>Vertical gradient, with a fixed width</title>
      <defs>
        <linearGradient id="g" x1="0%" x2="0%" y1="0%" y2="100%">
          <stop stop-color="purple" offset="0" />
          <stop stop-color="lime" offset="1" />
        </linearGradient>
      </defs>
      <rect fill="url('#g')" width="100%" height="100%" />
    </svg>
    

### [One specified dimension with intrinsic ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#one_specified_dimension_with_intrinsic_ratio)

This image specifies a 100 pixel height but no width. It also specifies an intrinsic aspect ratio of 3:4. This ensures that its width:height ratio is always 3:4, unless it's deliberately scaled to a disproportionate size (that is, by explicitly specifying both width and height that aren't of that ratio).

This is very much like specifying a specific width and height; since once you have one dimension and a ratio, the other dimension is implied.

html

    <svg height="100" viewBox="0 0 3 4" preserveAspectRatio="none">
      <title>Vertical gradient, with a fixed height and intrinsic ratio</title>
      <defs>
        <linearGradient id="g" x1="0%" x2="0%" y1="0%" y2="100%">
          <stop stop-color="teal" offset="0" />
          <stop stop-color="orange" offset="1" />
        </linearGradient>
      </defs>
      <rect fill="url('#g')" width="100%" height="100%" />
    </svg>
    

### [No width or height with intrinsic ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#no_width_or_height_with_intrinsic_ratio)

This image doesn't specify either a width or a height; instead, it specifies an intrinsic ratio of 1:1. It's always square, and is usable at any size, such as 32x32, 128x128, or 512x512, for example.

html

    <svg viewBox="0 0 1 1" preserveAspectRatio="none">
      <title>Intrinsic ratio</title>
      <defs>
        <linearGradient id="g" x1="0%" x2="100%" y1="0%" y2="0%">
          <stop stop-color="navy" offset="0" />
          <stop stop-color="maroon" offset="1" />
        </linearGradient>
      </defs>
      <rect fill="url('#g')" width="100%" height="100%" />
    </svg>
    

[Scaling examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#scaling_examples)

---------------------------------------------------------------------------------------------------------------------------------------------

Now let's see some examples of what happens as we apply different scaling to these images. In each of the examples below, the enclosing [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements are 300 pixels wide and 200 pixels tall, with a 2 pixel-wide border. To ensure we display the SVG background image only once for these demonstrations, we set [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
 to `no-repeat`.

### [Specifying fixed lengths for both dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#specifying_fixed_lengths_for_both_dimensions)

If you use [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 to specify fixed lengths for both dimensions, those lengths are always used, per rule 1 above. In other words, the image will always get stretched to the dimensions you specify, regardless of whether or not the source image has specified its dimensions and/or aspect ratio.

#### No dimensions or intrinsic ratio

In this example, the image has no dimensions or intrinsic ratio set:

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("no-dimensions-or-ratio.svg");
      background-size: 125px 175px;
    }
    

#### One specified dimension, no intrinsic ratio

In this example, the image has one dimension specified, and no intrinsic ratio set:

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-wide-no-height-or-ratio.svg");
      background-size: 250px 150px;
    }
    

#### One specified dimension with intrinsic ratio

    <div></div>
    

In this example, the image has one dimension explicitly set, along with an intrinsic ratio, meaning both dimensions are effectively defined. Setting an absolute height and width for `background-size` overrides the dimensions set in the SVG:

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-height-3x4-ratio.svg");
      background-size: 275px 125px;
    }
    

#### No specified width or height with intrinsic ratio

In this example, the image has an intrinsic ratio but no dimensions set:

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("no-dimensions-1x1-ratio.svg");
      background-size: 250px 100px;
    }
    

### [Using contain or cover](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#using_contain_or_cover)

Specifying `cover` for [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 makes the picture as small as possible while still covering the entire background area. `contain`, on the other hand, makes the image as large as possible while not being clipped by the background area.

For an image with an intrinsic ratio, exactly one size matches the `cover`/fit criteria alone. But if there is no intrinsic ratio specified, `cover`/fit isn't sufficient, so the large/small constraints choose the resulting size.

#### No dimensions or intrinsic ratio

In this example, the image has no dimensions or intrinsic ratio set. If an image doesn't specify either dimensions or an intrinsic ratio, neither rule 2 nor rule 3 apply, so rule 4 takes over: the background image is rendered covering the entire background area. This satisfies the largest-or-smallest constraint.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("no-dimensions-or-ratio.svg");
      background-size: contain;
    }
    

#### One specified dimension, no intrinsic ratio

In this example, with the image having one dimension specified but no intrinsic ratio, rule 4 applies, and the image is scaled to cover the entire background area.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-wide-no-height-or-ratio.svg");
      background-size: contain;
    }
    

#### One specified dimension with intrinsic ratio

In these examples, the image has one dimension explicitly set, along with an intrinsic ratio.

Things change when you specify an intrinsic ratio. In this case, rule 1 isn't relevant, so rule 2 is applied: we try to preserve any intrinsic ratio (while respecting `contain` or `cover`). For example, preserving a 3:4 intrinsic aspect ratio for a 300x200 box with `contain` means drawing a 150x200 background.

##### contain case

    <div></div>
    

Given this CSS:

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-height-3x4-ratio.svg");
      background-size: contain;
    }
    

Notice how the entire image is rendered, fitting as best as possible into the box without clipping any of it away.

##### cover case

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-height-3x4-ratio.svg");
      background-size: cover;
    }
    

Here, the 3:4 ratio is preserved while still stretching the image to fill the entire box. That causes the bottom of the image to be clipped away.

#### No dimensions with intrinsic ratio

These example use the image with an intrinsic ratio set but no defined dimensions. When using an image with no intrinsic dimensions but an intrinsic ratio, things work similarly.

##### contain case

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("no-dimensions-1x1-ratio.svg");
      background-size: contain;
    }
    

Notice that the image is sized to fit the smallest dimension while preserving the 1:1 aspect ratio.

##### cover case

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("no-dimensions-1x1-ratio.svg");
      background-size: cover;
    }
    

Here, the image is sized so that it fills the largest dimension. The 1:1 aspect ratio has been preserved, although with this source image, that can be difficult to see.

### [Automatic sizing using "auto" for both dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#automatic_sizing_using_auto_for_both_dimensions)

If [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 is set to `auto` or `auto auto`, rule 2 says that rendering must preserve any intrinsic ratio that's provided.

#### No dimensions or intrinsic ratio

When auto-sizing background images with no intrinsic ratio or dimensions specified, rule 4 takes effect, and the image is rendered to fill the background area.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("no-dimensions-or-ratio.svg");
      background-size: auto auto;
    }
    

#### One dimension and no intrinsic ratio

If no intrinsic ratio is specified, but at least one dimension is specified, rule 3 takes effect, and we render the image obeying those dimensions.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-wide-no-height-or-ratio.svg");
      background-size: auto auto;
    }
    

Note here that the width, which is specified in the source SVG at 100 pixels, is obeyed, while the height fills the background area since it's not specified (either explicitly or by an intrinsic ratio).

#### One dimension and an intrinsic ratio

If we have an intrinsic ratio with a fixed dimension, that fixes both dimensions in place. As previously mentioned, knowing one dimension and a ratio is the same as specifying both dimensions explicitly.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-height-3x4-ratio.svg");
      background-size: auto auto;
    }
    

Since this image has an explicit height of `100px`. With the 3:4 ratio set in the SVG, in the case of `auto`, the image's width is 75 pixels.

#### No fixed dimensions with intrinsic ratio

When an intrinsic ratio is specified, but no dimensions, rule 4 is applied — except that rule 2 also applies. The image is therefore rendered just like for the `contain` case.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("no-dimensions-1x1-ratio.svg");
      background-size: auto auto;
    }
    

### [Using "auto" and one specific length](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#using_auto_and_one_specific_length)

Given rule 1, specified dimensions are always used, so we need to use our rules only to determine the second dimension.

#### No dimensions or intrinsic ratio

If the image has no dimensions or intrinsic ratio, rule 4 applies, and we use the background area's dimension to determine the value for the `auto` dimension.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("no-dimensions-or-ratio.svg");
      background-size: auto 140px;
    }
    

Here, the width is determined using the background area's width per rule 4, while the height is the `140px` specified in the CSS.

#### One specified dimension with no intrinsic ratio

If the image has one specified dimension but no intrinsic ratio, that specified dimension is used per rule 3 if that dimension is set to `auto` in the CSS.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-wide-no-height-or-ratio.svg");
      background-size: 200px auto;
    }
    

Here, the `200px` specified in the CSS overrides the `100px` width specified in the SVG, per rule 1. Since there's no intrinsic ratio or height provided, `auto` selects the height of the background area as the height for the rendered image.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-wide-no-height-or-ratio.svg");
      background-size: auto 125px;
    }
    

In this case, the width is specified as `auto` in the CSS, so the `100px` width specified in the SVG is selected, per rule 3. The height is set at `125px` in the CSS, so that is selected per rule 1.

#### One specified dimension with intrinsic ratio

When a dimension is specified, rule 1 applies that dimension from the SVG to the rendered background unless specifically overridden by the CSS. When an intrinsic ratio is also specified, that's used to determine the other dimension.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("100px-height-3x4-ratio.svg");
      background-size: 150px auto;
    }
    

In this case, we use the width of the image specified in the CSS set at `150px`, so rule 1 is applied. The intrinsic 3:4 aspect ratio then determines the height for the `auto` case.

#### No specified dimensions with intrinsic ratio

If no dimensions are specified in the SVG, the specified dimension in the CSS is applied, then the intrinsic ratio is used to select the other dimension, per rule 2.

    <div></div>
    

    div {
      width: 300px;
      height: 200px;
      background-repeat: no-repeat;
      border: 2px solid black;
    }
    

css

    div {
      background-image: url("no-dimensions-1x1-ratio.svg");
      background-size: 150px auto;
    }
    

The width is set by the CSS to `150px`. The `auto` value for the height is computed using that width and the 1:1 aspect ratio to be `150px` as well.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds#see_also)

-----------------------------------------------------------------------------------------------------------------------------

*   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/backgrounds_and_borders/scaling_svg_backgrounds/index.md?plain=1 "Folder: en-us/web/css/guides/backgrounds_and_borders/scaling_svg_backgrounds (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBackgrounds_and_borders%2FScaling_SVG_backgrounds&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbackgrounds_and_borders%2Fscaling_svg_backgrounds%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBackgrounds_and_borders%2FScaling_SVG_backgrounds%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbackgrounds_and_borders%2Fscaling_svg_backgrounds%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")