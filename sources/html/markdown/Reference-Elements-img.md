*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#mdn-search)
    

`<img>` HTML image embed element
================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<img>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element embeds an image into the document.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#try_it)

------------------------------------------------------------------------------------------

    <img
      class="fit-picture"
      src="/shared-assets/images/examples/grapefruit-slice.jpg"
      alt="Grapefruit slice atop a pile of other slices" />
    

    .fit-picture {
      width: 250px;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#attributes)

--------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#alt)

Defines text that can replace the image in the page.

**Note:** Browsers do not always display images. There are a number of situations in which a browser might not display images, such as:

*   Non-visual browsers (such as those used by people with visual impairments)
*   The user chooses not to display images (saving bandwidth, privacy reasons)
*   The image is invalid or an [unsupported type](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
    

In these cases, the browser may replace the image with the text in the element's `alt` attribute. For these reasons and others, provide a useful value for `alt` whenever possible.

Setting this attribute to an empty string (`alt=""`) indicates that this image is _not_ a key part of the content (it's decoration or a tracking pixel), and that non-visual browsers may omit it from [rendering](https://developer.mozilla.org/en-US/docs/Glossary/Engine/Rendering)
. Visual browsers will also hide the broken image icon if the `alt` attribute is empty and the image failed to display.

This attribute is also used when copying and pasting the image to text, or saving a linked image to a bookmark.

[`attributionsrc`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#attributionsrc)

Specifies that you want the browser to send an [`Attribution-Reporting-Eligible`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Eligible)
 header along with the image request.

On the server-side this is used to trigger sending an [`Attribution-Reporting-Register-Source`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Source)
 or [`Attribution-Reporting-Register-Trigger`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Trigger)
 header in the response, to register an image-based [attribution source](https://developer.mozilla.org/en-US/docs/Web/API/Attribution_Reporting_API/Registering_sources#html-based_event_sources)
 or [attribution trigger](https://developer.mozilla.org/en-US/docs/Web/API/Attribution_Reporting_API/Registering_triggers#html-based_attribution_triggers)
, respectively. Which response header should be sent back depends on the value of the `Attribution-Reporting-Eligible` header that triggered the registration.

The corresponding source or trigger event is set off once the browser receives the response containing the image file.

**Note:** See the [Attribution Reporting API](https://developer.mozilla.org/en-US/docs/Web/API/Attribution_Reporting_API)
 for more details.

There are two versions of this attribute that you can set:

*   Boolean, i.e., just the `attributionsrc` name. This specifies that you want the [`Attribution-Reporting-Eligible`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Eligible)
     header sent to the same server as the `src` attribute points to. This is fine when you are handling the attribution source or trigger registration on the same server. When registering an attribution trigger this property is optional, and a boolean value will be used if it is omitted.
*   Value containing one or more URLs, for example:

html

    <img
      src="image-file.png"
      alt="My image file description"
      attributionsrc="https://a.example/register-source
                         https://b.example/register-source" />
    

This is useful in cases where the requested resource is not on a server you control, or you just want to handle registering the attribution source on a different server. In this case, you can specify one or more URLs as the value of `attributionsrc`. When the resource request occurs the [`Attribution-Reporting-Eligible`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Eligible)
 header will be sent to the URL(s) specified in `attributionSrc` in addition to the resource origin. These URLs can then respond with an [`Attribution-Reporting-Register-Source`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Source)
 or [`Attribution-Reporting-Register-Trigger`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Trigger)
 header as appropriate to complete registration.

**Note:** Specifying multiple URLs means that multiple attribution sources can be registered on the same feature. You might for example have different campaigns that you are trying to measure the success of, which involve generating different reports on different data.

[`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)

Indicates if the fetching of the image must be done using a [CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)
 request. Image data from a [CORS-enabled image](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image)
 returned from a CORS request can be reused in the [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 element without being marked "[tainted](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image#security_and_tainted_canvases)
".

If the `crossorigin` attribute is _not_ specified, then a non-CORS request is sent (without the [`Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin)
 request header), and the browser marks the image as tainted and restricts access to its image data, preventing its usage in [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 elements.

If the `crossorigin` attribute _is_ specified, then a CORS request is sent (with the [`Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin)
 request header); but if the server does not opt into allowing cross-origin access to the image data by the origin site (by not sending any [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin)
 response header, or by not including the site's origin in any [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin)
 response header it does send), then the browser blocks the image from loading, and logs a CORS error to the devtools console.

Allowed values:

[`anonymous`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#anonymous)

A CORS request is sent with credentials omitted (that is, no [cookies](https://developer.mozilla.org/en-US/docs/Glossary/Cookie)
, [X.509 certificates](https://datatracker.ietf.org/doc/html/rfc5280 "External link (opens in new tab)")
, or [`Authorization`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Authorization)
 request header).

[`use-credentials`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#use-credentials)

The CORS request is sent with any credentials included (that is, cookies, X.509 certificates, and the `Authorization` request header). If the server does not opt into sharing credentials with the origin site (by sending back the `Access-Control-Allow-Credentials: true` response header), then the browser marks the image as tainted and restricts access to its image data.

If the attribute has an invalid value, browsers handle it as if the `anonymous` value was used. See [CORS settings attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)
 for additional information.

[`decoding`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#decoding)

This attribute provides a hint to the browser as to whether it should perform image decoding along with rendering the other DOM content in a single presentation step that looks more "correct" (`sync`), or render and present the other DOM content first and then decode the image and present it later (`async`). In practice, `async` means that the next paint does not wait for the image to decode.

It is often difficult to perceive any noticeable effect when using `decoding` on static `<img>` elements. They'll likely be initially rendered as empty images while the image files are fetched (either from the network or from the cache) and then handled independently anyway, so the "syncing" of content updates is less apparent. However, the blocking of rendering while decoding happens, while often quite small, _can_ be measured — even if it is difficult to observe with the human eye. See [What does the image decoding attribute actually do?](https://www.tunetheweb.com/blog/what-does-the-image-decoding-attribute-actually-do/ "External link (opens in new tab)")
 for a more detailed analysis (tunetheweb.com, 2023).

Using different `decoding` types can result in more noticeable differences when dynamically inserting `<img>` elements into the DOM via JavaScript — see [`HTMLImageElement.decoding`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decoding)
 for more details.

Allowed values:

[`sync`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#sync)

Decode the image synchronously along with rendering the other DOM content, and present everything together.

[`async`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#async)

Decode the image asynchronously, after rendering and presenting the other DOM content.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#auto)

No preference for the decoding mode; the browser decides what is best for the user. This is the default value.

[`elementtiming`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/elementtiming)

Marks the image for observation by the [`PerformanceElementTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceElementTiming)
 API. The value given becomes an identifier for the observed image element. See also the [`elementtiming`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/elementtiming)
 attribute page.

[`fetchpriority`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority)

Provides a hint of the relative priority to use when fetching the image. Allowed values:

[`high`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#high)

Fetch the image at a high priority relative to other images.

[`low`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#low)

Fetch the image at a low priority relative to other images.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#auto_2)

Don't set a preference for the fetch priority. This is the default. It is used if no value or an invalid value is set.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#height)

The intrinsic height of the image, in pixels. Must be an integer without a unit.

**Note:** Including `height` and [`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#width)
 enables the [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 of the image to be calculated by the browser prior to the image being loaded. This aspect ratio is used to reserve the space needed to display the image, reducing or even preventing a layout shift when the image is downloaded and painted to the screen. Reducing layout shift is a major component of good user experience and web performance.

[`ismap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#ismap)

This Boolean attribute indicates that the image is part of a [server-side map](https://en.wikipedia.org/wiki/Image_map#Server-side "External link (opens in new tab)")
. If so, the coordinates where the user clicked on the image are sent to the server.

**Note:** This attribute is allowed only if the `<img>` element is a descendant of an [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 element with a valid [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
 attribute. This gives users without pointing devices a fallback destination.

[`loading`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#loading)

Indicates how the browser should load the image:

[`eager`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#eager)

Loads the image immediately, regardless of whether or not the image is currently within the [visual viewport](https://developer.mozilla.org/en-US/docs/Glossary/Visual_Viewport)
 (this is the default value).

[`lazy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#lazy)

Defers loading the image until it reaches a calculated distance from the viewport, as defined by the browser.

Lazy loading avoids the network and storage bandwidth required to handle the image until it's reasonably certain that it will be needed. This improves the performance in most typical use cases.

While explicit [`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#height)
 attributes are recommended for all images to avoid layout shift, they are especially important for lazy-loaded ones. Lazy-loaded images will never be loaded if they do not intersect a visible part of an element, even if loading them would change that, because unloaded images have a `width` and `height` of `0`. It creates an even more disruptive user experience when the content visible in the viewport reflows in the middle of reading it.

Lazy-loaded images located in the visual viewport may not yet be visible when the Window [`load`](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event "load")
 event is fired. This is because the event is fired based on eager-loaded images — lazy-loaded images are not considered even if they are located within the visual viewport upon initial page load.

Loading is only deferred when JavaScript is enabled. This is an anti-tracking measure, because if a user agent supported lazy loading when scripting is disabled, it would still be possible for a site to track a user's approximate scroll position throughout a session, by strategically placing images in a page's markup such that a server can track how many images are requested and when.

[`referrerpolicy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#referrerpolicy)

A string indicating which referrer to use when fetching the resource:

*   `no-referrer`: The [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
     header will not be sent.
*   `no-referrer-when-downgrade`: The [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
     header will not be sent to [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin)
    s without [TLS](https://developer.mozilla.org/en-US/docs/Glossary/TLS)
     ([HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS)
    ).
*   `origin`: The sent referrer will be limited to the origin of the referring page: its [scheme](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)
    , [host](https://developer.mozilla.org/en-US/docs/Glossary/Host)
    , and [port](https://developer.mozilla.org/en-US/docs/Glossary/Port)
    .
*   `origin-when-cross-origin`: The referrer sent to other origins will be limited to the scheme, the host, and the port. Navigations on the same origin will still include the path.
*   `same-origin`: A referrer will be sent for [same origin](https://developer.mozilla.org/en-US/docs/Glossary/Same-origin_policy)
    , but cross-origin requests will contain no referrer information.
*   `strict-origin`: Only send the origin of the document as the referrer when the protocol security level stays the same (HTTPS→HTTPS), but don't send it to a less secure destination (HTTPS→HTTP).
*   `strict-origin-when-cross-origin` (default): Send a full URL when performing a same-origin request, only send the origin when the protocol security level stays the same (HTTPS→HTTPS), and send no header to a less secure destination (HTTPS→HTTP).
*   `unsafe-url`: The referrer will include the origin _and_ the path (but not the [fragment](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/hash)
    , [password](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/password)
    , or [username](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/username)
    ). **This value is unsafe**, because it leaks origins and paths from TLS-protected resources to insecure origins.

[`sizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#sizes)

One or more values separated by commas, which can be source sizes or the `auto` keyword. The spec requires that the `sizes` attribute only be present when `srcset` uses width descriptors.

[**source size**](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#source_size)

A **source size** consists of:

1.  A [media condition](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#syntax)
    , omitted for the last item in the list.
2.  A source size value.

For example, the following source size proposes using a `1000px`\-wide image source if the _viewport_ width is 500px or less.

css

    (width <= 500px) 1000px
    

Media conditions describe properties of the _[viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
_, not the _image_. Because a source size descriptor specifies the width to use for the image during layout, the media condition is typically (but not necessarily) based on the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/width)
.

Source size values specify the intended display size of the image. [User agents](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 use the current source size to select one of the sources supplied by the `srcset` attribute, when those sources are described using width (`w`) descriptors. The `w` value defined in sizes determines the image's default layout width. In the absence of [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
, the browser will render the image at this size, regardless of the physical pixel dimensions of the downloaded file.

A source size value can be any non-negative [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
. It must not use CSS functions other than the [math functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#math_functions)
. Units are interpreted in the same way as [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
, meaning that all relative length units are relative to the document root rather than the `<img>` element. For example, an `em` value is relative to the root font size, not the font size of the image. [Percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values are not allowed. If the `sizes` attribute is not provided, it has a default value of `100vw` (the viewport width).

[`auto`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#auto_3)

The `auto` keyword indicates that the browser should use the expected layout width of the element to select the image to display. That is, it should use the [concrete size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image#concrete_size)
 of the image, calculated after layout from HTML and CSS has been applied. This is only valid when combined with `loading="lazy"`, as the page is expected to already have CSS and other layout information by the time the image loads.

Using `auto` saves you having to specify your layout media conditions twice: once for layout, and once for selection of an appropriate image to fetch and display.

If `auto` cannot resolve — either because the browser does not support it, or because the image has no layout size yet — the browser falls back to the _source sizes_ in the list to determine the width, then to `width`/`height` attributes defined on the element, and finally to the default intrinsic size for `<img>` elements defined in the user agent stylesheet (300px by 150px).

For better backward compatibility with browsers that do not support `auto`, you can include fallback sizes after `auto` in the `sizes` attribute. You should also set the element's `width` and `height` attributes to the intrinsic dimensions of the largest image in your `srcset`, so the browser can reserve space using the correct aspect ratio:

html

    <img
      loading="lazy"
      width="200"
      height="200"
      sizes="auto, (max-width: 30em) 100vw, (max-width: 50em) 50vw, calc(33vw - 100px)"
      srcset="
        swing-200.jpg   200w,
        swing-400.jpg   400w,
        swing-800.jpg   800w,
        swing-1600.jpg 1600w
      "
      src="swing-400.jpg"
      alt="Kettlebell Swing" />
    

[`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#src)

The image [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)
. At least one of `src` and [`srcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#srcset)
 is required for an `<img>` element. If [`srcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#srcset)
 is specified, `src` is used in one of two ways:

*   as a fallback for browsers that don't support `srcset`.
*   if `srcset` uses the "x" descriptor, then `src` is equivalent to a source with the density descriptor `1x`; that is, the image specified by `src` is used on low-density screens (such as typical 72 DPI or 96 DPI displays).

[`srcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#srcset)

One or more strings separated by commas, indicating possible image sources for the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 to use.

Each string is composed of:

1.  A [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)
     to an image
2.  Optionally, whitespace followed by one of:
    *   A width descriptor (a positive integer directly followed by `w`). It _must_ match the intrinsic width of the referenced image. The width descriptor is divided by the source size given in the `sizes` attribute to calculate the effective pixel density. For example, to provide an image resource to be used when the renderer needs a 450 pixel wide image, use the width descriptor `450w`. When a `srcset` contains "w" descriptors, the browser uses those descriptors together with the `sizes` attribute to pick a resource.
    *   A pixel density descriptor (a positive floating point number directly followed by `x`). It specifies the condition in which the corresponding image resource should be used as the display's pixel density. For example, to provide an image resource to be used when the pixel density is double the standard density, use the pixel density descriptor `2x` or `2.0x`.

If no descriptor is specified, the source is assigned the default descriptor of `1x`. It is incorrect to mix width descriptors and pixel density descriptors in the same `srcset` attribute. Duplicate descriptors (for instance, two sources in the same `srcset` which are both described with `2x`) are also invalid.

Space characters, other than the whitespace separating the URL and the corresponding condition descriptor, are ignored; this includes both leading and trailing space, as well as space before or after each comma. However, if an image candidate string contains no descriptors and no whitespace after the URL, the following image candidate string, if there is one, must begin with one or more whitespace, or the comma will be considered part of the URL.

When the `<img>` element's `srcset` uses `x` descriptors, browsers also consider the URL in the `src` attribute (if present) as a candidate, and assign it a default descriptor of `1x`. On the other hand, if the `srcset` attribute uses width descriptors, `src` is not considered, and the `sizes` attribute is used instead.

The user agent selects any of the available sources at its discretion. This provides them with significant leeway to tailor their selection based on things like user preferences or [bandwidth](https://developer.mozilla.org/en-US/docs/Glossary/Bandwidth)
 conditions. See our [Responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)
 tutorial for an example.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#width)

The intrinsic width of the image in pixels. Must be an integer without a unit.

[`usemap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#usemap)

The partial [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)
 (starting with `#`) of an [image map](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
 associated with the element.

**Note:** You cannot use this attribute if the `<img>` element is inside an [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 or [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#deprecated_attributes)

[`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#align)

Aligns the image with its surrounding context. Use the [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
 and/or [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
 properties instead of this attribute. Allowed values:

[`top`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#top)

Equivalent to `vertical-align: top` or `vertical-align: text-top`

[`middle`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#middle)

Equivalent to `vertical-align: -moz-middle-with-baseline`

[`bottom`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#bottom)

The default, equivalent to `vertical-align: unset` or `vertical-align: initial`

[`left`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#left)

Equivalent to `float: left`

[`right`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#right)

Equivalent to `float: right`

[`border`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#border)

The width of a border around the image. Use the [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
 property instead.

[`hspace`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#hspace)

The number of pixels of white space on the left and right of the image. Use the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 CSS property instead.

[`longdesc`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#longdesc)

A link to a more detailed description of the image. Possible values are a [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)
 or an element [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
.

**Note:** This attribute is considered obsolete in the [HTML spec](https://html.spec.whatwg.org/multipage/obsolete.html#element-attrdef-img-longdesc "External link (opens in new tab)")
. It has an uncertain future; authors should use a [WAI](https://developer.mozilla.org/en-US/docs/Glossary/WAI)
\-[ARIA](https://developer.mozilla.org/en-US/docs/Glossary/ARIA)
 alternative such as [`aria-describedby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby)
 or [`aria-details`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-details)
.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#name)

A name for the element. Use the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attribute instead.

[`vspace`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#vspace)

The number of pixels of white space above and below the image. Use the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 CSS property instead.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#usage_notes)

----------------------------------------------------------------------------------------------------

You need at least two attributes for each `<img>` element. Most commonly, they are `src` and `alt`.

*   The `src` attribute holds the path to the image you want to embed. It is not mandatory if the [srcset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/srcset)
     attribute is available. However, at least one of the `src` or `srcset` attributes must be provided.
*   The `alt` attribute holds a textual replacement for the image, which is mandatory and **incredibly useful** for accessibility — screen readers read the attribute value out to their users so they know what the image means. Alt text is also displayed on the page if the image can't be loaded for some reason: for example, network errors, content blocking, or link rot.

There are many other attributes to achieve various purposes:

*   [Referrer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy)
    /[CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)
     control for security and privacy: see [`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#crossorigin)
     and [`referrerpolicy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#referrerpolicy)
    .
*   Use both [`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#width)
     and [`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#height)
     to set the intrinsic size of the image, allowing it to take up space before it loads, to mitigate content layout shifts.
*   Responsive image hints with [`sizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#sizes)
     and [`srcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#srcset)
     (see also the [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
     element and our [Responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)
     tutorial).

The [Image file type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
 provides information about the supported image formats and broad recommendations about where they should be used.

### [Image loading errors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#image_loading_errors)

If an error occurs while loading or rendering an image, and an `onerror` event handler has been set for the [`error`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/error_event "error")
 event, that event handler will get called. This can happen in several situations, including:

*   The `src` or `srcset` attributes are empty (`""`) or `null`.
*   The `src` [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)
     is the same as the URL of the page the user is currently on.
*   The image is corrupted in some way that prevents it from being loaded.
*   The image's metadata is corrupted in such a way that it's impossible to retrieve its dimensions, and no dimensions were specified in the `<img>` element's attributes.
*   The image is in a format not supported by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
    .

### [Styling with CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#styling_with_css)

`<img>` is a [replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
; it has a [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value of `inline` by default, but its default dimensions are defined by the embedded image's intrinsic values, like it were `inline-block`. You can set properties like [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
/[`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
, [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
/[`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
, [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, etc. on an image.

`<img>` has no baseline, so when images are used in an inline formatting context with [`vertical-align: baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
, the bottom of the image will be placed on the text baseline.

You can use the [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
 property to position the image within the element's box, and the [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 property to adjust the sizing of the image within the box (for example, whether the image should fit the box or fill it even if clipping is required).

Depending on its type, an image may have an intrinsic width and height. For some image types, however, intrinsic dimensions are unnecessary. [SVG](https://developer.mozilla.org/en-US/docs/Glossary/SVG)
 images, for instance, have no intrinsic dimensions if their root [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
 element doesn't have a `width` or `height` set on it.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#accessibility)

--------------------------------------------------------------------------------------------------------

### [Authoring meaningful alternate descriptions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#authoring_meaningful_alternate_descriptions)

An `alt` attribute's value should provide a clear and concise text replacement for the image's content. It should not describe the presence of the image itself or the file name of the image. If the `alt` attribute is purposefully left off because the image has no textual equivalent, consider alternate methods to present what the image is trying to communicate.

#### Don't

html

    <img alt="image" src="penguin.jpg" />
    

#### Do

html

    <img alt="A Penguin on a beach." src="penguin.jpg" />
    

An important accessibility test is to read the `alt` attribute content together with preceding textual content to see if it conveys the same meaning as the image. For example, if the image was preceded by the sentence "On my travels, I saw a cute little animal:", the _Don't_ example could be read by a screen reader as "On my travels, I saw a cute little animal: image", which doesn't make sense. The _Do_ example could be read by a screen reader as "On my travels, I saw a cute little animal: A Penguin on a beach.", which does make sense.

For images used to trigger an action, for example, images nested inside an [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 or [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element, consider describing the triggered action inside the `alt` attribute value. For example, you could write `alt="next page"` instead of `alt="arrow right"`. You could also consider adding an optional further description inside a `title` attribute; this may be read by screen readers if requested by the user.

When an `alt` attribute is not present on an image, some screen readers may announce the image's file name instead. This can be a confusing experience if the file name isn't representative of the image's contents.

*   [An alt Decision Tree • Images • WAI Web Accessibility Tutorials](https://www.w3.org/WAI/tutorials/images/decision-tree/ "External link (opens in new tab)")
    
*   [Alt-texts: The Ultimate Guide — Axess Lab](https://axesslab.com/alt-texts/ "External link (opens in new tab)")
    
*   [How to Design Great Alt Text: An Introduction | Deque](https://www.deque.com/blog/great-alt-text-introduction/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 1.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.1_%E2%80%94_providing_text_alternatives_for_non-text_content)
    
*   [Understanding Success Criterion 1.1.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/text-equiv-all.html "External link (opens in new tab)")
    

### [Identifying SVG as an image](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#identifying_svg_as_an_image)

Due to a [VoiceOver bug](https://webkit.org/b/216364 "External link (opens in new tab)")
, VoiceOver does not correctly announce SVG images as images. Include [`role="img"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/img_role)
 to all `<img>` elements with SVG source files to ensure assistive technologies correctly announce the SVG as image content.

html

    <img src="mdn.svg" alt="MDN" role="img" />
    

### [The title attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#the_title_attribute)

The [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attribute is not an acceptable substitute for the `alt` attribute. Additionally, avoid duplicating the `alt` attribute's value in a `title` attribute declared on the same image. Doing so may cause some screen readers to announce the same text twice, creating a confusing experience.

The `title` attribute should also not be used as supplemental captioning information to accompany an image's `alt` description. If an image needs a caption, use the [`figure`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure)
 and [`figcaption`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
 elements.

The value of the `title` attribute is usually presented to the user as a tooltip, which appears shortly after the cursor stops moving over the image. While this _can_ provide additional information to the user, you should not assume that the user will ever see it: the user may only have keyboard or touchscreen. If you have information that's particularly important or valuable for the user, present it inline using one of the methods mentioned above instead of using `title`.

*   [Using the HTML title attribute – updated | Vispero](https://vispero.com/resources/using-the-html-title-attribute-updated/ "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#examples)

----------------------------------------------------------------------------------------------

### [Alternative text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#alternative_text)

The following example embeds an image into the page and includes alternative text for accessibility.

html

    <img src="/shared-assets/images/examples/favicon144.png" alt="MDN" />
    

### [Image link](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#image_link)

This example builds upon the previous one, showing how to turn the image into a link. To do so, nest the `<img>` tag inside the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
. You should make the alternative text describe the resource the link is pointing to, as if you were using a text link instead.

html

    <a href="https://developer.mozilla.org">
      <img
        src="/shared-assets/images/examples/favicon144.png"
        alt="Visit the MDN site" />
    </a>
    

### [Using the srcset attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#using_the_srcset_attribute)

In this example we include a `srcset` attribute with a reference to a high-resolution version of the logo; this will be loaded instead of the `src` image on high-resolution devices. The image referenced in the `src` attribute is counted as a `1x` candidate in [user agents](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 that support `srcset`.

html

    <img
      src="/shared-assets/images/examples/favicon72.png"
      alt="MDN"
      srcset="/shared-assets/images/examples/favicon144.png 2x" />
    

### [Using the srcset and sizes attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#using_the_srcset_and_sizes_attributes)

The `src` attribute is ignored in [user agents](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 that support `srcset` when `w` descriptors are included. When the `(width <= 600px)` media condition matches, the 200 pixel-wide image will load (it is the one that matches `200px` most closely), otherwise the other image will load.

html

    <img
      src="clock-demo-200px.png"
      alt="The time is 12:45."
      srcset="clock-demo-200px.png 200w, clock-demo-400px.png 400w"
      sizes="(width <= 600px) 200px, 50vw" />
    

**Note:** To see the resizing in action, [view the example on a separate page](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#livesample_fullscreen=using_the_srcset_and_sizes_attributes)
, so you can actually resize the content area.

[Security and privacy concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#security_and_privacy_concerns)

----------------------------------------------------------------------------------------------------------------------------------------

Although `<img>` elements have innocent uses, they can have undesirable consequences for user security and privacy. See [Referer header: privacy and security concerns](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Referer_header:_privacy_and_security_concerns)
 for more information and mitigations.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [embedded content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#embedded_content)<br>, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. If the element has a `usemap` attribute, it also is a part of the interactive content category. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | Any element that accepts embedded content. |
| Implicit ARIA role | *   with non-empty `alt` attribute or no `alt` attribute: ``[`img`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/img_role) ``<br>*   with empty `alt` attribute: [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role) |
| Permitted ARIA roles | *   with non-empty `alt` attribute:<br>    *   `[button](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role) `<br>    *   `[checkbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/checkbox_role) `<br>    *   [`link`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/link_role)<br>        <br>    *   [`menuitem`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitem_role)<br>        <br>    *   [`menuitemcheckbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role)<br>        <br>    *   [`menuitemradio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemradio_role)<br>        <br>    *   [`option`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/option_role)<br>        <br>    *   [`progressbar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/progressbar_role)<br>        <br>    *   [`scrollbar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/scrollbar_role)<br>        <br>    *   [`separator`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/separator_role)<br>        <br>    *   [`slider`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/slider_role)<br>        <br>    *   `[switch](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/switch_role) `<br>    *   `[tab](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role) `<br>    *   [`treeitem`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role)<br>        <br>*   with empty `alt` attribute, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>     or [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br>    <br>*   with no `alt` attribute, no `role` permitted |
| DOM interface | [`HTMLImageElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-img-element](https://html.spec.whatwg.org/multipage/embedded-content.html#the-img-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#see_also)

----------------------------------------------------------------------------------------------

*   [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
    , [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
    , and [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
     elements
*   [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    , [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
    , [`image-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation)
    , [`image-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering)
    , and [`image-resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution)
    : Image-related CSS properties.
*   [`HTMLImageElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement)
     interface for this element
*   [HTML images](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_images)
    
*   [Image file type and format guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)
    
*   [Responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/img/index.md?plain=1 "Folder: en-us/web/html/reference/elements/img (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fimg&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fimg%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fimg%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fimg%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F74a39db9d03ec63426b0740dc0bd3cb85e5461a4%0A*+Document+last+modified%3A+2026-09-11T00%3A44%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")