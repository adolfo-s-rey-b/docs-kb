*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#mdn-search)
    

`<source>` HTML media or image source element
=============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<source>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element specifies one or more media resources for the [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
, [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
, and [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 elements. It is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)
, which means that it has no content and does not require a closing tag. This element is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
 and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#try_it)

---------------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#attributes)

-----------------------------------------------------------------------------------------------------

This element supports all [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
. In addition, the following attributes can be used with it:

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#type)

Specifies the [MIME media type of the image](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
 or [other media type](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Containers)
, optionally including a [`codecs` parameter](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/codecs_parameter)
.

[`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#src)

Specifies the URL of the media resource. Required if the parent of `<source>` is [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
. Not allowed if the parent is [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
.

[`srcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#srcset)

Specifies a comma-separated list of one or more image URLs and their descriptors. Required if the parent of `<source>` is [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
. Not allowed if the parent is [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
.

The list consists of strings separated by commas, indicating a set of possible images for the browser to use. Each string is composed of:

*   A URL specifying an image location.
*   An optional width descriptor—a positive integer directly followed by `"w"`, such as `300w`.
*   An optional pixel density descriptor—a positive floating number directly followed by `"x"`, such as `2x`.

Each string in the list must have either a width descriptor or a pixel density descriptor to be valid. These two descriptors should not be used together; only one should be used consistently throughout the list. The value of each descriptor in the list must be unique. The browser chooses the most adequate image to display at a given point of time based on these descriptors. If the descriptors are not specified, the default value used is `1x`. If the `sizes` attribute is also present, then each string must include a width descriptor. If the browser does not support `srcset`, then `src` will be used for the default image source.

[`sizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#sizes)

Specifies a list of source sizes that describe the final rendered width of the image. Allowed if the parent of `<source>` is [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
. Not allowed if the parent is [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
.

The list consists of source sizes separated by commas. Each source size is media condition-length pair. Before laying the page out, the browser uses this information to determine which image defined in [`srcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#srcset)
 to display. Note that `sizes` will take effect only if width descriptors are provided with `srcset`, not pixel density descriptors (i.e., `200w` should be used instead of `2x`).

[`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#media)

Specifies the [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
 for the resource's intended media.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#height)

Specifies the intrinsic height of the image in pixels. Allowed if the parent of `<source>` is a [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
. Not allowed if the parent is [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
.

The height value must be an integer without any units.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#width)

Specifies the intrinsic width of the image in pixels. Allowed if the parent of `<source>` is a [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
. Not allowed if the parent is [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
.

The width value must be an integer without any units.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#usage_notes)

-------------------------------------------------------------------------------------------------------

The `<source>` element is a **[void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)
**, which means that it not only has no content but also has no closing tag. That is, you _never_ use `</source>` in your HTML.

The browser goes through a list of `<source>` elements to find a format it supports. It uses the first one it can display. For each `<source>` element:

*   If the `type` attribute isn't specified, the browser retrieves the media's type from the server and determines if it can be displayed. If the media can't be rendered, the browser checks the next `<source>` in the list.
*   If the `type` attribute is specified, the browser immediately compares it with the media types it can display. If the type is not supported, the browser skips querying the server and directly checks the next `<source>` element.

If none of the `<source>` elements provide a usable source:

*   In the case of a `<picture>` element, the browser will fall back to using the image specified in the `<picture>` element's [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
     child.
*   In the case of an `<audio>` or `<video>` element, the browser will fall back to displaying the content included between the element's opening and closing tags.

For information about image formats supported by web browsers and guidance on selecting appropriate formats to use, see our [Image file type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
. For details on the video and audio media types you can use, see the [Media type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#examples)

-------------------------------------------------------------------------------------------------

### [Using the `type` attribute with `<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#using_the_type_attribute_with_video)

This example demonstrates how to offer a video in different formats: WebM for browsers that support it, Ogg for those that support Ogg, and QuickTime for browsers that support QuickTime. If the `<audio>` or `<video>` element is not supported by the browser, a notice is displayed instead. If the browser supports the element but does not support any of the specified formats, an `error` event is raised on the `<audio>` or `<video>` element and the default media controls (if enabled) will indicate an error. For more details on which media file formats to use and their browser support, refer to our [Media type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats)
.

### [Using the `media` attribute with `<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#using_the_media_attribute_with_video)

This example demonstrates how to offer an alternate source file for viewports above a certain width. When a user's browsing environment meets the specified `media` condition, the associated `<source>` element is chosen. The contents of its `src` attribute are then requested and rendered. If the `media` condition does not match, the browser will move on to the next `<source>` in the list. The second `<source>` option in the code below has no `media` condition, so it will be selected for all other browsing contexts.

For more examples, the [HTML video and audio](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_video_and_audio)
 article in the Learn area is a great resource.

### [Using the `media` attribute with `<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#using_the_media_attribute_with_picture)

In this example, two `<source>` elements are included within [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
, providing versions of an image to use when the available space exceeds certain widths. If the available width is less than the smallest of these widths, the browser will fall back to the image specified in the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element.

With the `<picture>` element, you must always include an `<img>` with a fallback image. Also, make sure to add an `alt` attribute for accessibility, unless the image is purely decorative and irrelevant to the content.

### [Using `height` and `width` attributes with `<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#using_height_and_width_attributes_with_picture)

In this example, three `<source>` elements with `height` and `width` attributes are included in a [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
 element. A [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
 allows the browser to select an image to display with the `height` and `width` attributes based on the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 size.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | A media element—[`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)<br> or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)<br>—and it must be placed before any [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br> or [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)<br> element.<br><br>A [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)<br> element, and it must be placed before the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)<br> element. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLSourceElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSourceElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-source-element](https://html.spec.whatwg.org/multipage/embedded-content.html#the-source-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#see_also)

-------------------------------------------------------------------------------------------------

*   [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
     element
*   [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
     element
*   [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
     element
*   [Image file type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
    
*   [Media type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats)
    
*   [Web performance](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/source/index.md?plain=1 "Folder: en-us/web/html/reference/elements/source (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsource&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsource%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsource%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsource%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")