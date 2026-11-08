*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#mdn-search)
    

`<picture>` HTML picture element
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<picture>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element contains zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 elements and one [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element to offer alternative versions of an image for different display/device scenarios.

The browser will consider each child `<source>` element and choose the best match among them. If no matches are found—or the browser doesn't support the `<picture>` element—the URL of the `<img>` element's [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#src)
 attribute is selected. The selected image is then presented in the space occupied by the `<img>` element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#try_it)

----------------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#attributes)

------------------------------------------------------------------------------------------------------

This element includes only [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#usage_notes)

--------------------------------------------------------------------------------------------------------

To decide which URL to load, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 examines each `<source>`'s [`srcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#srcset)
, [`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#media)
, and [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#type)
 attributes to select a compatible image that best matches the current layout and capabilities of the display device.

The `<img>` element serves two purposes:

1.  It describes the size and other attributes of the image and its presentation.
2.  It provides a fallback in case none of the offered `<source>` elements are able to provide a usable image.

Common use cases for `<picture>`:

*   **Art direction.** Cropping or modifying images for different `media` conditions (for example, loading a simpler version of an image which has too many details, on smaller displays).
    
*   **Offering alternative image formats**, for cases where certain formats are not supported.
    
    **Note:** For example, newer formats like [AVIF](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types#avif_image)
     or [WEBP](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types#webp_image)
     have many advantages, but might not be supported by the browser. A list of supported image formats can be found in: [Image file type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
    .
    
*   **Saving bandwidth and speeding page load times** by loading the most appropriate image for the viewer's display.
    

If providing higher-density versions of an image for high-DPI (Retina) display, use [`srcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#srcset)
 on the `<img>` element instead. This lets browsers opt for lower-density versions in data-saving modes, and you don't have to write explicit `media` conditions.

You can use the [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
 property to adjust the positioning of the image within the element's frame, and the [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 property to control how the image is resized to fit within the frame.

**Note:** Use these properties on the child `<img>` element, **not** the `<picture>` element.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#examples)

--------------------------------------------------------------------------------------------------

These examples demonstrate how different attributes of the [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 element change the selection of the image inside `<picture>`.

### [The media attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#the_media_attribute)

The `media` attribute specifies a media condition (similar to a media query) that the user agent will evaluate for each [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 element.

If the [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
's media condition evaluates to `false`, the browser skips it and evaluates the next element inside `<picture>`.

You can swap image assets for light and dark themes using the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 media feature:

### [The srcset attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#the_srcset_attribute)

The [srcset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#srcset)
 attribute is used to offer a list of possible images based on size or the display's pixel density.

It is composed of a comma-separated list of image descriptors. Each image descriptor is composed of a URL of the image, and _either_:

*   a _width descriptor_, followed by a `w` (such as `300w`); _OR_
*   a _pixel density descriptor_, followed by an `x` (such as `2x`) to serve a high-res image for high-DPI screens.

Make sure to note that:

*   width and pixel density descriptors should not be used together
*   a missing pixel density descriptor implies 1x
*   duplicate descriptor values are not allowed (2x & 2x, 100w & 100w)

The following example illustrates the usage of `srcset` attribute with the `<source>` element to specify a high-density and standard-resolution image:

The `srcset` attribute can also be used on the `<img>` element without needing the `<picture>` element. The following example demonstrates how to use the `srcset` attribute to specify standard-resolution and high-density images, respectively:

### [The sizes attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#the_sizes_attribute)

The [`sizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#sizes)
 attribute of the `<source>` element allows you to specify a set of media condition-length pairs and indicate the image display size for each condition. This helps the browser select the most appropriate image from the `srcset` attribute, which lists images with their [intrinsic](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
 widths.

The browser evaluates the media conditions in the sizes attribute before it downloads any images. See the sizes attribute of the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#sizes)
 and [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#sizes)
 elements for more information.

For example:

In this example:

*   If the viewport is 600px wide or less, the slot size is 400px; otherwise, it is 800px.
*   The browser multiplies the slot size by the device pixel ratio to determine the ideal image width, then picks the closest available image from `srcset`.

Without sizes, the browser will use the default size of the image as specified by its dimensions in pixels. This may not be the best fit for all devices, especially if the image is displayed on different screen sizes or in different contexts.

Please note that sizes will have its effect only if width dimension descriptors are provided with srcset instead of pixel ratio values (200w instead of 2x for example). For more information on using `srcset`, see the [Responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)
 documentation.

### [The type attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#the_type_attribute)

The `type` attribute specifies a [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types)
 for the resource URL(s) in the [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 element's `srcset` attribute. If the user agent does not support the given type, the [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 element is skipped.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#technical_summary)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, phrasing content, embedded content |
| Permitted content | Zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)<br> elements, followed by one [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)<br> element, optionally intermixed with script-supporting elements. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that allows embedded content. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLPictureElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLPictureElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-picture-element](https://html.spec.whatwg.org/multipage/embedded-content.html#the-picture-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture#see_also)

--------------------------------------------------------------------------------------------------

*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
     element
*   [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
     element
*   Positioning and sizing the picture within its frame: [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
     and [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    
*   [Image file type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
    
*   [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
     media feature

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/picture/index.md?plain=1 "Folder: en-us/web/html/reference/elements/picture (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fpicture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fpicture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fpicture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fpicture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcb7d4dde9f0a43664c64587d9d70b8835286eb7%0A*+Document+last+modified%3A+2026-10-01T19%3A41%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")