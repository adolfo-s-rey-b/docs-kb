*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#mdn-search)
    

Understanding and setting aspect ratios
=======================================

Every element rendered to the page has a height and a width, and, therefore, an [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
, which is the ratio between the width and height. The natural dimensions of a media object, which are its size without any sizing, scaling, zooming, or borders applied, are known as its natural or [intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
. An element's intrinsic size is determined by the element itself, not by applying formatting such as [box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
 or setting border, margin, or padding widths.

When developing sites, you often want to be able to set the width of an element to a percentage of the viewport or parent container size and have the height change size proportionally, thereby maintaining a specific aspect ratio depending on the size of the viewport. For replaced elements, like images and videos, maintaining a specific aspect ratio is not only necessary for creating [responsive web design](https://developer.mozilla.org/en-US/docs/Glossary/Responsive_web_design)
, but also a vital component of providing good user experience. Setting an asset's aspect ratio prevents loading [jank](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/Multimedia#rendering_strategy_preventing_jank_when_loading_images)
—the layout shift that occurs when media loads after the page has already been painted, causing a reflow because the space for the asset has not been reserved.

Using CSS, you can adjust the size of replaced and non-replaced elements based on their aspect ratio. In this guide, we will learn about the `aspect-ratio` property, discuss aspect ratios for replaced and non-replaced elements, and then examine some common aspect ratio use cases.

[How the `aspect-ratio` property works](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#how_the_aspect-ratio_property_works)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

The CSS [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
 property value defines the preferred width-to-height ratio of an element's box. The value is either a [`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
, the keyword `auto`, or a space-separated combination of both.

The `<ratio>` is the ratio of the width and height, in that order. It is represented by two positive [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 values separated by a forward slash (`/`) or a single `<number>`. When a single number is used, it is the same as writing the ratio as `<number> / 1`, which is also the width divided by the height.

The following values are all equivalent:

The following values are also all equivalent:

The effect of the `auto` keyword depends on whether the element on which it is applied is a replaced element or not. For replaced elements with an intrinsic aspect ratio, `auto` means the intrinsic aspect ratio should be used. In all other instances, the `auto` value means the box has no preferred aspect ratio. In both cases, this is the default behavior as if no `aspect-ratio` property were applied.

When the value contains both the `auto` keyword and a `<ratio>` value, such as `aspect-ratio: auto 2 / 3;` or `aspect-ratio: 0.75 auto;`, the `auto` value is applied to replaced elements with a natural aspect ratio and the specified ratio of the `width / height` or `<number>` is used as the preferred aspect ratio.

You will have noticed the word "preferred" in the definitions above. The `aspect-ratio` value is not always applied when set. The `aspect-ratio` property sets a "preferred" aspect ratio, so only ever has an effect if at least one of the box's sizes is automatic.

When both the height and width or inline and block sizes are explicitly set, the `aspect-ratio` property value is ignored. In this case, no dimension is allowed to be automatically sized - the preferred sizes are explicitly set - so the `aspect-ratio` property has no effect. When you declare both the inline and block dimensions, those take precedence.

With replaced elements, if you don't explicitly set a value (other than `auto`) to either dimension, both will default to their intrinsic size (any `aspect-ratio` value isn't applied). The `aspect-ratio` will apply to non-replaced elements that don't have a dimension explicitly set, as non-replaced elements are either [intrinsically](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
 or [extrinsically](https://developer.mozilla.org/en-US/docs/Glossary/Extrinsic_size)
 sized, getting their size from their content, container, [box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)
 properties, etc.

When an element is rendered to the page, if no CSS is applied and no HTML sizing attributes are included, the user agent will render the object at its natural size.

[Adjusting aspect ratios of replaced elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#adjusting_aspect_ratios_of_replaced_elements)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Replaced elements like [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 and [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 are replaced with media that have set dimensions and, therefore, an intrinsic aspect ratio. Consider a raster image, such as a JPEG, PNG, or GIF. If you place an image on a page and do not set a height or width, either via [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 attributes or with CSS, it will be displayed at its intrinsic size.

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg?image=good"
      alt="220 pixel square pride flag" />
    

This is a `220px` square image with no CSS applied; it is displayed at its intrinsic or default size.

If replaced content is auto-sized or you provide a size for only one dimension, such as setting a value for `width`, the browser will automatically resize the other dimension, in this case, the height, while maintaining the media's original aspect ratio.

In this example, only the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 is set on the image, so the user agent preserves its aspect ratio. The same image is repeated three times, displayed at different widths: `55px`, `110px`, and at its natural size of `220px` via the [`width: auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 value.

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    

    img {
      width: 55px;
      margin-right: 5px;
    }
    
    img + img {
      width: 110px;
    }
    
    img + img + img {
      width: auto;
    }
    

Only when you provide sizes for both dimensions is there a risk of distorting the replaced element. For example, setting `width: 100vw;` and `height: 100vh;` on an image creates a variable aspect ratio; the image will appear either stretched or squashed when the viewport's aspect ratio differs from the image's natural aspect ratio.

In this example, the same image is repeated three times, explicitly sized with the same [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 value (`110px`) but different [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 values (`55px`, `110px`, and `220px`).

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    

    img {
      width: 55px;
      height: 110px;
    }
    
    img + img {
      width: 110px;
    }
    
    img + img + img {
      width: 220px;
    }
    

We have distorted the images intentionally by setting both a `height` and `width`: we've squashed the first one and stretched the third.

We could have created this same distorted effect using the CSS [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
 property, by setting a single dimension (not both or neither) and providing a value other than `1` (or `1 / 1`). You likely don't want to do this, but it's good to know that it's possible.

    <img
      src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
      alt="Pride flag" />
    

css

    img {
      height: 90vh;
      aspect-ratio: 3;
    }
    

We have declared a single dimension; `100vh` is the full height of the example [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 viewport. For `aspect-ratio` to apply to replaced elements, only one dimension must be set. Setting both or neither doesn't work.

### [Fitting replaced elements within their containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#fitting_replaced_elements_within_their_containers)

To fit a replaced element to the dimensions of its container while maintaining its intrinsic aspect ratio, set the [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 property value to `cover` or `contain`. This will resize the replaced element and either clip it to "cover" the container or display it at a smaller size, fully "contained" within it.

In this example, the square image is placed into a grid of three items, each with an aspect ratio of `5 / 2`.

To begin with, we create a container with three items, each containing one image:

html

    <div class="grid">
      <div>
        <img
          src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
          alt="Pride flag" />
      </div>
      <div>
        <img
          class="cover"
          src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
          alt="Pride flag" />
      </div>
      <div>
        <img
          class="contain"
          src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
          alt="Pride flag" />
      </div>
    </div>
    

Next, we designate the container as a grid, where each item has an aspect ratio of `2.5` (`5/2`) with a minimum width of `150px`. Therefore, the minimum height will be `60px`. However, the final width and height are determined by the width of the example's iframe, which will be based on your viewport size:

css

    .grid {
      display: grid;
      gap: 20px;
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      font-size: 0; /* to minimize whitespace */
    }
    
    div div {
      aspect-ratio: 5 / 2;
      background-color: #cccccc;
    }
    

We then size the images and set the `object-fit` property on the last two images:

css

    img {
      height: 100%;
      width: 100%;
    }
    
    .cover {
      object-fit: cover;
    }
    
    .contain {
      object-fit: contain;
    }
    

Only the first image is distorted (stretched). We could have used the `fill` value of `object-fit` to create the same effect. The `cover` image spans the full width of the container, centered vertically, and clipped to fit in the container. The `contain` value ensures the image is contained within the container, centered horizontally, and shrunk to fit.

[Defining aspect ratios for non-replaced elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#defining_aspect_ratios_for_non-replaced_elements)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While the aspect ratio of a replaced element is maintained by default, adjusting the intrinsic size of a non-replaced element usually changes its aspect ratio. For example, identical content may appear as three lines on a widescreen or in a wide parent container, but as eight lines on a narrow screen or container.

In this example, the same quote is displayed in `200px` and `600px` wide containers, and a square is set with a height matching its `200px` width:

    <p>Narrow:</p>
    <blockquote>
      <q
        >When you stop living your life based on what others think of you real life
        begins. At that moment, you will finally see the door of self acceptance
        opened.</q
      >
      - Shannon L. Alder
    </blockquote>
    <p>Wide:</p>
    <blockquote>
      <q
        >When you stop living your life based on what others think of you real life
        begins. At that moment, you will finally see the door of self acceptance
        opened.</q
      >
      - Shannon L. Alder
    </blockquote>
    <p>Aspect ratio with overflow:</p>
    <blockquote>
      <q
        >When you stop living your life based on what others think of you real life
        begins. At that moment, you will finally see the door of self acceptance
        opened.</q
      >
      - Shannon L. Alder
    </blockquote>
    <p>
      <label
        ><input type="checkbox" checked /> Toggle between
        <code>overflow</code> values <code>auto</code> and
        <code>visible</code></label
      >
    </p>
    

To highlight the issue with setting a non-replaced element's aspect ratio via size dimensions, toggle the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 property between `auto` and `visible`.

    blockquote {
      border: 3px dotted #cccccc;
      padding: 0 3px;
      margin: 20px 0;
      font-size: 1.25rem;
      line-height: 1.5;
    }
    
    body:has(:checked) blockquote {
      overflow: auto;
    }
    
    :checked + code,
    :not(:checked) + code + code {
      outline: 1px solid green;
    }
    
    p:nth-last-of-type(n + 2) {
      font-weight: bold;
    }
    

css

    blockquote {
      width: 200px;
    }
    
    blockquote:nth-of-type(2) {
      width: 600px;
    }
    
    blockquote:nth-of-type(3) {
      height: 200px;
    }
    

While it's possible to define an aspect ratio on non-replaced elements by setting both the dimensions and hiding overflowing content, the CSS [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
 property provides explicit aspect ratio support. This means a specific aspect ratio can be set even when you don't know the content or screen sizes.

In the next example, we render square boxes regardless of the width of the text by setting `aspect ratio: 1` on [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
, a non-replaced element:

    <p>Short text:</p>
    <blockquote>Breath.</blockquote>
    <p>Longer text:</p>
    <blockquote>You're perfect just as you are.</blockquote>
    

css

    blockquote {
      inline-size: max-content;
      aspect-ratio: 1;
    }
    

    blockquote {
      border: 1px solid #cccccc;
      padding: 1px;
      margin: 20px 0;
      background-color: #ededed;
    }
    

Each box has one dimension defined: the [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
, which is the width in horizontal languages, is set to [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
, which sets the size to be as wide as it needs to be to fit the content without wrapping. The second dimension, in this case, the [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
 or [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, is set to be the same length as the first dimension. This is accomplished with the [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
 property. We defined the desired width-to-height ratio of the element's box to be `1`, which is the same as `1 / 1`, a square. This sets the block direction to match the width of the element, without using the [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 or [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
 properties.

In these examples, a size was explicitly set on the element itself. When working with non-replaced elements, aspect ratio comes into play when no size dimension is explicitly set.

### [Creating a circle based on the container size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#creating_a_circle_based_on_the_container_size)

The inline-size of non-replaced block-level elements is the size of their container's [content box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#content-box)
. Because they have a size by default, they don't need to have an explicit size set for the `aspect-ratio` property to work.

In this example, we have a container [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 that is `200px` wide, which includes `5px` of padding on each side. Therefore, the inline-size of the content box is `190px`. Without setting a height or width on the nested [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element, we know its inline-size is `190px`. With `aspect-ratio: 1` set, the paragraph will be `190px` tall, unless it has visible overflowing content causing it to be taller (which it doesn't).

The height of the `<div>` element is not explicitly set, but it contains the `190px` tall paragraph, the `5px` of padding on top and bottom, and the combined heights of the default top and bottom margins of `<p>`. As a result, it is taller than it is wide. Both elements have a [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 of `50%`, so the container is an oval while the child, with an `aspect-ratio` of `1` but no inline or block sizing explicitly defined, is a circle.

html

    <div><p>Hello world</p></div>
    

css

    div,
    p {
      border-radius: 50%;
    }
    
    div {
      width: 200px;
      padding: 5px;
      border: 1px solid black;
      background-color: #66ccff;
    }
    
    p {
      aspect-ratio: 1;
      text-align: center;
      border: 10px solid white;
      background-color: #f4aab9;
    }
    

To make the `<div>` a circle, we can set the `height` and `width` to the same value, or set `aspect-ratio: 1` and set the `overflow` to `auto` or `hidden`. Alternatively, we can simply remove the margins on the paragraph with [`margin-block: 0`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
. Both these options are shown below.

html

    <div><p>Hello world</p></div>
    <div><p>Hello world</p></div>
    

    div {
      width: 200px;
      padding: 5px;
      margin: 1rem;
      border: 1px solid black;
      background-color: #66ccff;
    }
    
    p {
      text-align: center;
      border: 10px solid white;
      background-color: #f4aab9;
    }
    

css

    div,
    p {
      aspect-ratio: 1;
      border-radius: 50%;
    }
    
    div:first-of-type {
      overflow: hidden;
    }
    
    div:last-of-type p {
      margin-block: 0;
    }
    

[Common `aspect-ratio` use cases](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#common_aspect-ratio_use_cases)

--------------------------------------------------------------------------------------------------------------------------------------------------

Let's look at a few situations where you can use `aspect-ratio` to address some common challenges while creating responsive designs.

### [Making external assets responsive](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#making_external_assets_responsive)

All content should be responsive, even when that content is third-party embeds, such as videos from TikTok, YouTube, or Instagram. The code snippet you include to embed these external videos generally creates an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
.

While a [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 element typically adopts the aspect ratio of its media file, `iframe` elements lack this capability. This poses the challenge of ensuring that the `<iframe>` is responsive while always maintaining the aspect ratio of the video it contains. One of the techniques we can use is to set the iframe's width to `100%` of its container or `100vw` to match the viewport width regardless of the viewport's size. However, setting a fixed height might stretch or squash the video. Instead, we set the `aspect-ratio` on the video's container, aligning it to be the same aspect ratio as the video. Problem solved!

For context, the standard aspect ratio of YouTube videos is 16:9 when viewed on a desktop computer or laptop, while TikTok and Instagram videos have a 9:16 aspect ratio.

We can use the `aspect-ratio` feature within the [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 query alongside the `aspect-ratio` property to adjust the size of both the iframe and the video it contains. This ensures that the video content is always as large as possible - taking up either the full width or height of the viewport, regardless of the viewport size - while maintaining a specific aspect ratio.

We can set the landscape-oriented YouTube videos to be as wide as the viewport and the portrait-oriented TitTok and Instagram video iframes to be as tall as the viewport. If a viewport's aspect ratio is wider than 16:9, we set the YouTube video to be the height of the viewport. If the viewport is narrower than 9:16, we set both Instagram and TikTok videos to the width of the viewport.

### [Making grid cells square](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#making_grid_cells_square)

A grid of square cells can be created by defining fixed [column track sizes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
, ensuring each row matches the size of the column track. However, when creating responsive grids using `auto-fill` to fit as many column tracks as possible within the container, the width of each item becomes uncertain. This makes it challenging to determine the appropriate height for creating square items.

By setting an aspect ratio on the items, we can ensure when the grid items are laid out, each grid item will be as tall as it is wide, creating square grid items regardless of the container's dimensions.

In this example of square grid items, the grid tracks are auto-sized, taking their size from the items. Each item will be at least `95px` wide but could be much wider. No matter the width, each item will be a square, with the height determined by the `aspect-ratio` to match its width.

css

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(95px, 1fr));
    }
    
    .item {
      aspect-ratio: 1;
    }
    

    div {
      gap: 20px;
      font-size: 1.1rem;
    }
    
    div div {
      background-color: #cccccc;
      aspect-ratio: 1;
      counter-increment: items;
    }
    
    div div::after {
      content: counter(items);
    }
    
    .item::after {
      /*  hide the number if there's content  */
      position: absolute;
      color: transparent;
    }
    

    <div class="grid">
      <div></div>
      <div></div>
      <div class="item">
        This text would overflow the parent, but we've set properties to prevent it
        from doing so.
      </div>
      <div></div>
      <div></div>
      <div></div>
      <div class="item">
        <img
          src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
          alt="Pride flag" />
      </div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    

For the content of a grid item to not grow beyond the preferred height set by the `aspect-ratio`, set the [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
 to `0` and the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 to a value other than `visible`. This will work for intrinsically sized content. If you have content that is intrinsically larger than the available space, set that content to not be larger than the grid item by setting the [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
 (or [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
, depending on the content) to `100%`.

css

    .item {
      min-height: 0;
      overflow: auto;
    }
    
    .item > * {
      max-height: 100%;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 3  <br>\# aspect-ratio](https://drafts.csswg.org/css-sizing/#aspect-ratio) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios#see_also)

------------------------------------------------------------------------------------------------------

*   [CSS box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/box_sizing/aspect_ratios/index.md?plain=1 "Folder: en-us/web/css/guides/box_sizing/aspect_ratios (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_sizing%2FAspect_ratios&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbox_sizing%2Faspect_ratios%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_sizing%2FAspect_ratios%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbox_sizing%2Faspect_ratios%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")