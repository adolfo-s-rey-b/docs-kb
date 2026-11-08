*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#mdn-search)
    

`<link>` HTML external resource link element
============================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<link>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element specifies relationships between the current document and an external resource. This element is most commonly used to link to [stylesheets](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
, but is also used to establish site icons (both "favicon" style icons and icons for the home screen and apps on mobile devices) among other things.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#try_it)

-------------------------------------------------------------------------------------------

To link an external stylesheet, you'd include a `<link>` element inside your [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
 like this:

This example provides the path to the stylesheet inside an `href` attribute and a [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)
 attribute with a value of `stylesheet`. The `rel` stands for "relationship", and is one of the key features of the `<link>` element — the value denotes how the item being linked to is related to the containing document.

There are a number of other common types you'll come across. For example, a link to the site's favicon:

There are a number of other icon `rel` values, mainly used to indicate special icon types for use on various mobile platforms, e.g.:

The `sizes` attribute indicates the icon size, while the `type` contains the MIME type of the resource being linked. These provide useful hints to allow the browser to choose the most appropriate icon available.

You can also provide a media type or query inside a `media` attribute; this resource will then only be loaded if the media condition is true. For example:

Some interesting new performance and security features have been added to the `<link>` element too. Take this example:

A `rel` value of `preload` indicates that the browser should preload this resource (see [`rel="preload"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)
 for more details), with the `as` attribute indicating the specific class of content being fetched. The `crossorigin` attribute indicates whether the resource should be fetched with a [CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)
 request.

Other usage notes:

*   A `<link>` element can occur either in the [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
     or [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
     element, depending on whether it has a [link type](https://html.spec.whatwg.org/multipage/links.html#body-ok "External link (opens in new tab)")
     that is **body-ok**. For example, the `stylesheet` link type is body-ok, and therefore `<link rel="stylesheet">` is permitted in the body. However, this isn't a good practice to follow; it makes more sense to separate your `<link>` elements from your body content, putting them in the `<head>`.
*   When using `<link>` to establish a favicon for a site, and your site uses a Content Security Policy (CSP) to enhance its security, the policy applies to the favicon. If you encounter problems with the favicon not loading, verify that the [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy)
     header's [`img-src` directive](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/img-src)
     is not preventing access to it.
*   The HTML and XHTML specifications define event handlers for the `<link>` element, but it is unclear how they would be used.
*   Under XHTML 1.0, [void elements](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)
     such as `<link>` require a trailing slash: `<link />`.
*   WebTV supports the use of the value `next` for `rel` to preload the next page in a document series.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#attributes)

---------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`as`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#as)

This attribute is required when [`rel="preload"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)
 has been set on the `<link>` element, optional when [`rel="modulepreload"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload)
 has been set, and otherwise should not be used. It specifies the type of content being loaded by the `<link>`, which is necessary for request matching, application of correct [content security policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
, and setting of correct [`Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept)
 request header.

Furthermore, `rel="preload"` uses this as a signal for request prioritization. The table below lists the valid values for this attribute and the elements or resources they apply to.

| `As` value | `Rel` value | Applies To |
| --- | --- | --- |
| audioworklet | modulepreload | [AudioWorklet](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet)<br> modules |
| fetch | preload | fetch, XHR<br><br>**Note:** This value also requires `<link>` to contain the crossorigin attribute, see [CORS-enabled fetches](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#cors-enabled_fetches)<br>. |
| font | preload | CSS @font-face<br><br>**Note:** This value also requires `<link>` to contain the crossorigin attribute, see [CORS-enabled fetches](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#cors-enabled_fetches)<br>. |
| image | preload | `<img>` and `<picture>` elements with srcset or imageset attributes, SVG `<image>` elements, CSS `*-image` rules |
| json | modulepreload | Supplementary JSON file |
| paintworklet | modulepreload | [PaintWorklet](https://developer.mozilla.org/en-US/docs/Web/API/PaintWorkletGlobalScope)<br> modules |
| script | preload or modulepreload | `<script>` elements, Worker `importScripts`, and `modulepreload` destinations. |
| serviceworker | modulepreload | [ServiceWorker](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorker)<br> modules |
| sharedworker | modulepreload | [SharedWorker](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker) |
| style | preload or modulepreload | `<link rel=stylesheet>` elements, CSS `@import` and `modulepreload` destinations. |
| text | modulepreload | Supplementary plain text file |
| track | preload | `<track>` elements ([WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API/Web_Video_Text_Tracks_Format)<br>, MIME type `text/vtt`) |
| worker | modulepreload | [Worker](https://developer.mozilla.org/en-US/docs/Web/API/Worker)<br> modules |

[`blocking`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#blocking)

This attribute explicitly indicates that certain operations should be blocked until specific conditions are met. It must only be used when the `rel` attribute contains the `expect` or `stylesheet` keywords. With [`rel="expect"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#expect)
, it indicates that operations should be blocked until a specific DOM node has been parsed. With [`rel="stylesheet"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#stylesheet)
, it indicates that operations should be blocked until an external stylesheet and its critical subresources have been fetched and applied to the document. The operations that are to be blocked must be a space-separated list of blocking tokens listed below. Currently there is only one token:

*   `render`: The rendering of content on the screen is blocked.

**Note:** Only `link` elements in the document's `<head>` can possibly block rendering. By default, a `link` element with `rel="stylesheet"` in the `<head>` blocks rendering when the browser discovers it during parsing. If such a `link` element is added dynamically via script, you must additionally set `blocking = "render"` for it to block rendering.

[`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)

This [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute indicates whether [CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)
 must be used when fetching the resource. [CORS-enabled images](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image)
 can be reused in the [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 element without being _tainted_. The allowed values are:

[`anonymous`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#anonymous)

A cross-origin request (i.e., with an [`Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin)
 HTTP header) is performed, but no credential is sent (i.e., no cookie, X.509 certificate, or HTTP Basic authentication). If the server does not give credentials to the origin site (by not setting the [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin)
 HTTP header) the resource will be tainted and its usage restricted.

[`use-credentials`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#use-credentials)

A cross-origin request (i.e., with an `Origin` HTTP header) is performed along with a credential sent (i.e., a cookie, certificate, and/or HTTP Basic authentication is performed). If the server does not give credentials to the origin site (through [`Access-Control-Allow-Credentials`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Credentials)
 HTTP header), the resource will be _tainted_ and its usage restricted.

If the attribute is not present, the resource is fetched without a [CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)
 request (i.e., without sending the `Origin` HTTP header), preventing its non-tainted usage. If invalid, it is handled as if the enumerated keyword **anonymous** was used. See [CORS settings attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)
 for additional information.

[`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#disabled)

For `rel="stylesheet"` only, the `disabled` Boolean attribute indicates whether the described stylesheet should be loaded and applied to the document. If `disabled` is specified in the HTML when it is loaded, the stylesheet will not be loaded during page load. Instead, the stylesheet will be loaded on-demand, if and when the `disabled` attribute is changed to `false` or removed.

Setting the `disabled` property in the DOM causes the stylesheet to be removed from the document's [`Document.styleSheets`](https://developer.mozilla.org/en-US/docs/Web/API/Document/styleSheets)
 list.

[`fetchpriority`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/fetchpriority)

Provides a hint of the relative priority to use when fetching a resource of a particular type. Allowed values:

[`high`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#high)

Fetch the resource at a high priority relative to other resources of the same type.

[`low`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#low)

Fetch the resource at a low priority relative to other resources of the same type.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#auto)

Don't set a preference for the fetch priority. This is the default. It is used if no value or an invalid value is set.

[`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#href)

This attribute specifies the [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)
 of the linked resource. A URL can be absolute or relative.

[`hreflang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#hreflang)

This attribute indicates the language of the linked resource. It is purely advisory. Values should be valid [BCP 47 language tags](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
. Use this attribute only if the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
 attribute is present.

[`imagesizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#imagesizes)

For `rel="preload"` and `as="image"` only, the `imagesizes` attribute has similar syntax and semantics as the [`sizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#sizes)
 attribute that indicates to preload the appropriate resource used by an `img` element with corresponding values for its `srcset` and `sizes` attributes.

[`imagesrcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#imagesrcset)

For `rel="preload"` and `as="image"` only, the `imagesrcset` attribute has similar syntax and semantics as the [`srcset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#srcset)
 attribute that indicates to preload the appropriate resource used by an `img` element with corresponding values for its `srcset` and `sizes` attributes.

[`integrity`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity)

This attribute contains one or more [hashes](https://developer.mozilla.org/en-US/docs/Glossary/Hash_function)
 of the resource. It is used to ensure that the content of the resource is what the developer expects it to be, and has not been replaced with a malicious copy in a [supply chain attack](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Supply_chain_attacks)
. The attribute must only be specified when the `rel` attribute is set to `stylesheet`, `preload`, or `modulepreload`. See [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity)
.

[`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#media)

This attribute specifies the media that the linked resource applies to. Its value must be a media type / [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
. This attribute is mainly useful when linking to external stylesheets — it allows the user agent to pick the best adapted one for the device it runs on.

[`referrerpolicy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#referrerpolicy)

A string indicating which referrer to use when fetching the resource. For detailed explanations and examples of each policy, see the [`Referrer-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy)
 header documentation.

*   `no-referrer` means that the [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
     header will not be sent.
*   `no-referrer-when-downgrade` means that no [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
     header will be sent when navigating to an origin without TLS (HTTPS). This is a user agent's default behavior, if no policy is otherwise specified.
*   `origin` means that the referrer will be the origin of the page, which is roughly the scheme, the host, and the port.
*   `origin-when-cross-origin` means that navigating to other origins will be limited to the scheme, the host, and the port, while navigating on the same origin will include the referrer's path.
*   `same-origin` means that the referrer (origin, path, and query string) is sent for same-origin requests, but no referrer is sent for cross-origin requests.
*   `strict-origin` means that only the origin is sent when the protocol security level stays the same (HTTPS→HTTPS). No referrer is sent to less secure destinations (HTTPS→HTTP). This is important for HTTPS pages because it prevents leaking referrer information to insecure origins.
*   `strict-origin-when-cross-origin` means that the full referrer is sent for same-origin requests. For cross-origin requests, only the origin is sent when the protocol stays the same (HTTPS→HTTPS), and no referrer is sent when downgrading to HTTP. This is the default value, which balances functionality with privacy and security for HTTPS sites.
*   `unsafe-url` means that the referrer will include the origin and the path (but not the fragment, password, or username). This case is unsafe because it can leak origins and paths from TLS-protected resources to insecure origins.

[`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)

This attribute names a relationship of the linked document to the current document. The attribute must be a space-separated list of [link type values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)
.

[`sizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#sizes)

This attribute defines the sizes of the icons for visual media contained in the resource. It must be present only if the [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#rel)
 contains a value of `icon` or a non-standard type such as Apple's `apple-touch-icon`. It may have the following values:

*   `any`, meaning that the icon can be scaled to any size as it is in a vector format, like `image/svg+xml`.
*   a white-space separated list of sizes, each in the format `<width in pixels>x<height in pixels>` or `<width in pixels>X<height in pixels>`. Each of these sizes must be contained in the resource.

**Note:** Most icon formats are only able to store one single icon; therefore, most of the time, the [`sizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#sizes)
 attribute contains only one entry. Microsoft's ICO format and Apple's ICNS format can store multiple icon sizes in a single file. ICO has better browser support, so you should use this format if cross-browser support is a concern.

[`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#title)

The `title` attribute has special semantics on the `<link>` element. When used on a `<link rel="stylesheet">` it defines a [default or an alternate stylesheet](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet)
.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#type)

This attribute is used to define the type of the content linked to. The value of the attribute should be a MIME type such as **text/html**, **text/css**, and so on. The common use of this attribute is to define the type of stylesheet being referenced (such as **text/css**), but given that CSS is the only stylesheet language used on the web, not only is it possible to omit the `type` attribute, but is actually now recommended practice. It is also used on `rel="preload"` link types, to make sure the browser only downloads file types that it supports.

### [Non-standard attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#non-standard_attributes)

[`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#target)

Defines the frame or window name that has the defined linking relationship or that will show the rendering of any linked resource.

### [Obsolete attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#obsolete_attributes)

[`charset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#charset)

This attribute defines the character encoding of the linked resource. The value is a space- and/or comma-delimited list of character sets as defined in [RFC 2045](https://datatracker.ietf.org/doc/html/rfc2045 "External link (opens in new tab)")
. The default value is `iso-8859-1`.

**Note:** To produce the same effect as this obsolete attribute, use the [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type)
 HTTP header on the linked resource.

[`rev`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#rev)

The value of this attribute shows the relationship of the current document to the linked document, as defined by the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#href)
 attribute. The attribute thus defines the reverse relationship compared to the value of the `rel` attribute. [Link type values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)
 for the attribute are similar to the possible values for [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#rel)
.

**Note:** Instead of `rev`, you should use the [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#rel)
 attribute with the opposite [link type value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)
. For example, to establish the reverse link for `made`, specify `author`. Also, this attribute doesn't stand for "revision" and must not be used with a version number, even though many sites misuse it in this way.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#examples)

-----------------------------------------------------------------------------------------------

### [Including a stylesheet](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#including_a_stylesheet)

To include a stylesheet in a page, use the following syntax:

### [Providing alternative stylesheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#providing_alternative_stylesheets)

You can also specify [alternative style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet)
.

The user can choose which style sheet to use by choosing it from the **View > Page Style** menu. This provides a way for users to see multiple versions of a page.

### [Providing icons for different usage contexts](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#providing_icons_for_different_usage_contexts)

You can include links to several icons on the same page, and the browser will choose which one works best for its particular context using the `rel` and `sizes` values as hints.

For information about what `sizes` to choose for Apple icons, see [Apple's documentation on configuring web applications](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html#//apple_ref/doc/uid/TP40002051-CH3-SW4 "External link (opens in new tab)")
 and the referenced [Apple human interface guidelines](https://developer.apple.com/design/human-interface-guidelines/app-icons#App-icon-sizes "External link (opens in new tab)")
. Usually, it is sufficient to provide a large image, such as 192x192, and let the browser scale it down as needed, but you may want to provide images with different levels of detail for different sizes, as the Apple design guideline recommends. Providing smaller icons for lower resolutions also saves bandwidth.

It may not be necessary to provide `<link>` elements at all. For example, browsers automatically request `/favicon.ico` from the root of a site, and Apple also automatically requests `/apple-touch-icon-[size].png`, `/apple-touch-icon.png`, etc. However, providing explicit links protects you against changes to these conventions.

### [Conditionally loading resources with media queries](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#conditionally_loading_resources_with_media_queries)

You can provide a media type or query inside a `media` attribute; this resource will then only be loaded if the media condition is true. For example:

### [Stylesheet load events](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#stylesheet_load_events)

You can determine when a style sheet has been loaded by watching for a `load` event to fire on it; similarly, you can detect if an error has occurred while processing a style sheet by watching for an `error` event:

**Note:** The `load` event fires once the stylesheet and all of its imported content has been loaded and parsed, and immediately before the styles start being applied to the content.

### [Preload examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#preload_examples)

You can find a number of `<link rel="preload">` examples in [Preloading content with `rel="preload"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)
.

### [Blocking rendering till a resource is fetched](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#blocking_rendering_till_a_resource_is_fetched)

You can include `render` token inside a `blocking` attribute; the rendering of the page will be blocked till the resource and its critical subresources are fetched and applied to the document. For example:

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | Metadata content. If `[itemprop](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop) ` is present: [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br> and [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | Any element that accepts metadata elements. If [itemprop](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)<br> is present: any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [`link`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/link_role)<br> with `href` attribute |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLLinkElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLinkElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-link-element](https://html.spec.whatwg.org/multipage/semantics.html#the-link-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#see_also)

-----------------------------------------------------------------------------------------------

*   [`Link`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Link)
     HTTP header
*   [`Referrer-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy)
     HTTP header

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/link/index.md?plain=1 "Folder: en-us/web/html/reference/elements/link (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Flink&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Flink%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Flink%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Flink%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffc7c0c6df803d5ce26e7b2a72725a7d021ed0694%0A*+Document+last+modified%3A+2026-05-20T15%3A49%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")