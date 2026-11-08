*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#mdn-search)
    

`image()` CSS function
======================

The **`image()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 in a similar fashion to the [`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_function)
 function, but with added functionality including specifying the image's directionality, displaying just a part of that image defined by a media fragment, and specifying a solid color as a fallback in case none of the specified images are able to be rendered.

**Note:** The CSS `image()` function should not be confused with [`Image()`, the `HTMLImageElement` constructor](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/Image "<code>Image()</code>, the <code>HTMLImageElement</code> constructor")
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#syntax)

-----------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#values)

[`image-tags` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#image-tags)

The directionality of the image, either `ltr` for left-to-right or `rtl` for right-to-left.

[`image-src` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#image-src)

Zero or more [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
s or [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
s specifying the image sources, with optional image fragment identifiers.

[`color` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#color)

A color, specifying a solid background color to use as a fallback if no `image-src` is found, supported, or declared.

### [Bi-directional awareness](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#bi-directional_awareness)

The first, optional parameter of the `image()` notation is the directionality of the image. If included, and the image is used on an element with opposite directionality, the image will be flipped horizontally in horizontal writing modes. If the directionality is omitted, the image won't be flipped if the language direction is changed.

### [Image fragments](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#image_fragments)

One key difference between `url()` and `image()` is the ability to add a media fragment identifier — a starting point along the x and y axis, along with a width and height — onto the image source to display only a section of the source image. The section of the image defined in the parameter becomes a standalone image. The syntax looks like so:

The background image of the element will be the portion of the image _myImage.webp_ that starts at the coordinate 0px, 20px (the top left-hand corner) and is 40px wide and 60px tall.

The `#xywh=#,#,#,#` media fragment syntax takes four comma separated numeric values. The first two represent the X and Y coordinates for the starting point of the box that will be created. The third value is the width of the box, and the last value is the height. By default, these are pixel values. The [spatial dimension definition in the media specification](https://www.w3.org/TR/media-frags/#naming-space "External link (opens in new tab)")
 indicates that percentages will be supported as well:

xywh=160,120,320,240        /\* results in a 320x240 image at x=160 and y=120 \*/
xywh=pixel:160,120,320,240  /\* results in a 320x240 image at x=160 and y=120 \*/
xywh=percent:25,25,50,50    /\* results in a 50%x50% image at x=25% and y=25% \*/

The image fragments can be used in `url()` notation as well. The `#xywh=#,#,#,#` media fragment syntax is 'backwards compatible' in that a media fragment will be ignored if not understood, and won't break the source call when used with `url()`. If the browser doesn't understand the media fragments notation, it ignores the fragment, displaying the entire image.

Browsers that understand `image()` also understand the fragment notation. Therefore, if the fragment is not understood within `image()`, the image will be considered invalid.

### [Color fallback](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#color_fallback)

If a color is specified in `image()` along with your image sources, it acts as a fallback if the images are invalid and do not appear. In such cases, the `image()` function renders as if no image were included, generating a solid-color image. As a use case, consider a dark image being used as a background for some white text. A dark background color may be needed for foreground text to be legible, if the image does not render.

Omitting image sources while including a color is valid and creates a color swatch. Unlike declaring a [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, which is placed under or behind all the background images, this can be used to put (generally semi-transparent) colors over other images.

The size of the color swatch can be set with the [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 property. This is different from the `background-color`, which sets a color to cover the entire element. Both `image(color)` and `background-color` placements are impacted by the [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
 and [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
 properties.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#formal_syntax)

-------------------------------------------------------------------------------------------------------------

<image()> =   
  image( <image-tags>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image-src>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 , [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
! )    
  
<image-tags> =   
  ltr  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rtl    
  
<image-src> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#accessibility)

-------------------------------------------------------------------------------------------------------------

Browsers do not provide any special information on background images to assistive technology. This is important primarily for screen readers, as a screen reader will not announce its presence and therefore convey nothing to its users. If the image contains information critical to understanding the page's overall purpose, it is better to describe it semantically in the document.

*   [MDN Understanding WCAG, Guideline 1.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.1_%E2%80%94_providing_text_alternatives_for_non-text_content)
    
*   [Understanding Success Criterion 1.1.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/text-equiv-all.html "External link (opens in new tab)")
    

This feature can help improve accessibility by providing a fallback color when an image fails to load. While this can and should be done by including a background-color on every background image, the CSS `image()` function allows adding allows only including background colors should an image fail to load, which means you can add a fallback color should a transparent PNG/GIF/WebP not load.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#examples)

---------------------------------------------------------------------------------------------------

### [Directionally-sensitive images](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#directionally-sensitive_images)

In the left-to-right list items — those with `dir="ltr"` set on the element itself or inheriting the directionality from an ancestor or default value for the page — the image will be used as-is. List items with `dir="rtl"` set on the `<li>` or inheriting the right-to-left directionality from an ancestor, such as documents set to Arabic or Hebrew, will have the bullet display on the right, horizontally flipped, as if `transform: scaleX(-1)` had been set. The text will also be displayed left-to-right.

### [Displaying a section of the background image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#displaying_a_section_of_the_background_image)

html

    <div class="box">Hover over me. What cursor do you see?</div>
    

css

    .box:hover {
      cursor: image("sprite.png#xywh=32,64,16,16"), auto;
    }
    

When the user hovers over the box, the cursor will change to display the 16x16 px section of the sprite image, starting at x=32 and y=64.

### [Putting color on top of a background image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#putting_color_on_top_of_a_background_image)

    .quarter-logo {
      height: 200px;
      width: 200px;
      border: 1px solid;
    }
    

css

    .quarter-logo {
      background-image: image(rgb(0 0 0 / 25%)), url("firefox.png");
      background-size: 25%;
      background-repeat: no-repeat;
    }
    

html

    <div class="quarter-logo">
      If supported, a quarter of this div has a darkened logo
    </div>
    

The above will put a semi-transparent black mask over the Firefox logo background image. Had we used the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 property instead, the color would have appeared behind the logo image instead of on top of it. Additionally, the entire container would have had the same background color. Because we used `image()` along with the [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 property (and prevented the image from repeating with the [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
 property), the color swatch will only cover a quarter of the container.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 4  <br>\# funcdef-image](https://drafts.csswg.org/css-images-4/#funcdef-image) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

Currently, no browsers support this feature.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image#see_also)

---------------------------------------------------------------------------------------------------

*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
    
*   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    
*   [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
    
*   [`cross-fade()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
    
*   [CSS images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/image/image/index.md?plain=1 "Folder: en-us/web/css/reference/values/image/image (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fimage%2Fimage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fimage%2Fimage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fimage%2Fimage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fimage%2Fimage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3a4e7cc6b2104a8b8e64bfece1924ef065328784%0A*+Document+last+modified%3A+2026-10-12T21%3A09%3A48.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")