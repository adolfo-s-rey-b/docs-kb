*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#mdn-search)
    

`<iframe>` HTML inline frame element
====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<iframe>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a nested [browsing context](https://developer.mozilla.org/en-US/docs/Glossary/Browsing_context)
, embedding another document into the current one.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#try_it)

---------------------------------------------------------------------------------------------

    <iframe
      id="inlineFrameExample"
      title="Inline Frame Example"
      width="300"
      height="200"
      src="https://www.openstreetmap.org/export/embed.html?bbox=-0.004017949104309083%2C51.47612752641776%2C0.00030577182769775396%2C51.478569861898606&amp;layer=mapnik">
    </iframe>
    

    iframe {
      border: 1px solid black;
      width: 100%; /* takes precedence over the width set with the HTML width attribute */
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#attributes)

-----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`allow`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow)

Specifies a [Permissions Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Permissions_Policy)
 for the `<iframe>`. The policy defines what features are available to the `<iframe>` (for example, access to the microphone, camera, battery, web-share, etc.) based on the origin of the request.

See [iframes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy#iframes)
 in the `Permissions-Policy` topic for examples.

**Note:** A Permissions Policy specified by the `allow` attribute implements a further restriction on top of the policy specified in the [`Permissions-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy)
 header. It doesn't replace it.

[`allowfullscreen`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allowfullscreen)

Set to `true` if the `<iframe>` can activate fullscreen mode by calling the [`requestFullscreen()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/requestFullscreen "requestFullscreen()")
 method.

**Note:** This attribute is considered a legacy attribute and redefined as `allow="fullscreen *"`.

[`allowpaymentrequest`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allowpaymentrequest)

Set to `true` if a cross-origin `<iframe>` should be allowed to invoke the [Payment Request API](https://developer.mozilla.org/en-US/docs/Web/API/Payment_Request_API)
.

**Note:** This attribute is considered a legacy attribute and redefined as `allow="payment *"`.

[`browsingtopics`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#browsingtopics)

A boolean attribute that, if present, specifies that the selected topics for the current user should be sent with the request for the `<iframe>`'s source.

[`credentialless`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#credentialless)

Set to `true` to make the `<iframe>` credentialless, meaning that its content will be loaded in a new, ephemeral context. It doesn't have access to the network, cookies, and storage data associated with its origin. It uses a new context local to the top-level document lifetime. In return, the [`Cross-Origin-Embedder-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)
 (COEP) embedding rules can be lifted, so documents with COEP set can embed third-party documents that do not. See [IFrame credentialless](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/IFrame_credentialless)
 for more details.

[`csp`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#csp)

A [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 enforced for the embedded resource. See [`HTMLIFrameElement.csp`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/csp)
 for details.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#height)

The height of the frame in CSS pixels. Default is `150`.

[`loading`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#loading)

Indicates when the browser should load the iframe:

[`eager`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#eager)

Load the iframe immediately on page load (this is the default value).

[`lazy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#lazy)

Defer loading of the iframe until it reaches a calculated distance from the [visual viewport](https://developer.mozilla.org/en-US/docs/Glossary/Visual_Viewport)
, as defined by the browser. The intent is to avoid using the network and storage bandwidth required to fetch the frame until the browser is reasonably certain that it will be needed. This improves the performance and cost in most typical use cases, in particular by reducing initial page load times.

Loading is only deferred when JavaScript is enabled. This is an anti-tracking measure, because if a user agent supported lazy loading when scripting is disabled, it would still be possible for a site to track a user's approximate scroll position throughout a session, by strategically placing iframes in a page's markup such that a server can track how many iframes are requested and when.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#name)

A targetable name for the embedded browsing context. This can be used in the `target` attribute of the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, or [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base)
 elements; the `formtarget` attribute of the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements; or the `windowName` parameter in the [`window.open()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/open "window.open()")
 method. In addition, the name becomes a property of the [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 and [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document)
 objects, containing a reference to the embedded window or the element itself.

[`privateToken`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#privatetoken)

Contains a string representation of an options object representing a [private state token](https://developer.mozilla.org/en-US/docs/Web/API/Private_State_Token_API/Using)
 operation; this object has the same structure as the `RequestInit` dictionary's [`privateToken`](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#privatetoken)
 property. IFrames containing this attribute can initiate operations such as issuing or redeeming tokens when their embedded content is loaded.

[`referrerpolicy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#referrerpolicy)

Indicates which [referrer](https://developer.mozilla.org/en-US/docs/Web/API/Document/referrer)
 to send when fetching the frame's resource:

[`no-referrer`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#no-referrer)

The [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
 header will not be sent.

[`no-referrer-when-downgrade`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#no-referrer-when-downgrade)

The [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
 header will not be sent to [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin)
s without [TLS](https://developer.mozilla.org/en-US/docs/Glossary/TLS)
 ([HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS)
).

[`origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#origin)

The sent referrer will be limited to the origin of the referring page: its [scheme](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)
, [host](https://developer.mozilla.org/en-US/docs/Glossary/Host)
, and [port](https://developer.mozilla.org/en-US/docs/Glossary/Port)
.

[`origin-when-cross-origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#origin-when-cross-origin)

The referrer sent to other origins will be limited to the scheme, the host, and the port. Navigations on the same origin will still include the path.

[`same-origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#same-origin)

A referrer will be sent for [same origin](https://developer.mozilla.org/en-US/docs/Glossary/Same-origin_policy)
, but cross-origin requests will contain no referrer information.

[`strict-origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#strict-origin)

Only send the origin of the document as the referrer when the protocol security level stays the same (HTTPS→HTTPS), but don't send it to a less secure destination (HTTPS→HTTP).

[`strict-origin-when-cross-origin` (default)](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#strict-origin-when-cross-origin)

Send a full URL when performing a same-origin request, only send the origin when the protocol security level stays the same (HTTPS→HTTPS), and send no header to a less secure destination (HTTPS→HTTP).

[`unsafe-url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#unsafe-url)

The referrer will include the origin _and_ the path (but not the [fragment](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/hash)
, [password](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/password)
, or [username](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/username)
). **This value is unsafe**, because it leaks origins and paths from TLS-protected resources to insecure origins.

[`sandbox`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#sandbox)

Controls the restrictions applied to the content embedded in the `<iframe>`. The value of the attribute can either be empty to apply all restrictions, or space-separated tokens to lift particular restrictions:

[`allow-downloads`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-downloads)

Allows downloading files through an [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 or [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 element with the [download](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#download)
 attribute, as well as through the navigation that leads to a download of a file. This works regardless of whether the user clicked on the link, or JS code initiated it without user interaction.

[`allow-forms`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-forms)

Allows the page to submit forms. If this keyword is not used, a form will be displayed as normal, but submitting it will not trigger input validation, send data to a web server, or close a dialog.

[`allow-modals`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-modals)

Allows the page to open modal windows by [`Window.alert()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert)
, [`Window.confirm()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm)
, [`Window.print()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/print)
 and [`Window.prompt()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt)
, while opening a [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 is allowed regardless of this keyword. It also allows the page to receive [`BeforeUnloadEvent`](https://developer.mozilla.org/en-US/docs/Web/API/BeforeUnloadEvent)
 event.

[`allow-orientation-lock`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-orientation-lock)

Lets the resource [lock the screen orientation](https://developer.mozilla.org/en-US/docs/Web/API/Screen/lockOrientation)
.

[`allow-pointer-lock`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-pointer-lock)

Allows the page to use the [Pointer Lock API](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_Lock_API)
.

[`allow-popups`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-popups)

Allows popups (created, for example, by [`Window.open()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/open)
 or `target="_blank"`). If this keyword is not used, such functionality will silently fail.

[`allow-popups-to-escape-sandbox`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-popups-to-escape-sandbox)

Allows a sandboxed document to open a new browsing context without forcing the sandboxing flags upon it. This will allow, for example, a third-party advertisement to be safely sandboxed without forcing the same restrictions upon the page the ad links to. If this flag is not included, a redirected page, popup window, or new tab will be subject to the same sandbox restrictions as the originating `<iframe>`.

[`allow-presentation`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-presentation)

Allows embedders to have control over whether an iframe can start a [presentation session](https://developer.mozilla.org/en-US/docs/Web/API/PresentationRequest)
.

[`allow-same-origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-same-origin)

If this token is not used, the resource is treated as being from a special origin that always fails the [same-origin policy](https://developer.mozilla.org/en-US/docs/Glossary/Same-origin_policy)
 (potentially preventing access to [data storage/cookies](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy#cross-origin_data_storage_access)
 and some JavaScript APIs).

**Note:** When `allow-same-origin` is present, a same-origin parent document can still access and interact with the iframe's DOM even if `allow-scripts` is not set. The `allow-scripts` token only controls script execution within the embedded browsing context and does not affect DOM access from the parent.

[`allow-scripts`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-scripts)

Allows the page to run scripts (but not create pop-up windows). If this keyword is not used, this operation is not allowed.

[`allow-storage-access-by-user-activation`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-storage-access-by-user-activation)

Allows a document loaded in the `<iframe>` to use the [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API "Storage Access API")
 to request access to unpartitioned cookies.

[`allow-top-navigation`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-top-navigation)

Lets the resource navigate the top-level browsing context (the one named `_top`).

[`allow-top-navigation-by-user-activation`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-top-navigation-by-user-activation)

Lets the resource navigate the top-level browsing context, but only if initiated by a user gesture.

[`allow-top-navigation-to-custom-protocols`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-top-navigation-to-custom-protocols)

Allows navigations to non-`http` protocols built into browser or [registered by a website](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/registerProtocolHandler)
. This feature is also activated by `allow-popups` or `allow-top-navigation` keyword.

**Note:**

*   The `sandbox` attribute can block the browser's built-in PDF viewer. See [Embedding PDFs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#embedding_pdfs)
    .
*   When the embedded document has the same origin as the embedding page, it is **strongly discouraged** to use both `allow-scripts` and `allow-same-origin`, as that lets the embedded document remove the `sandbox` attribute — making it no more secure than not using the `sandbox` attribute at all.
*   Sandboxing is useless if the attacker can display content outside a sandboxed `iframe` — such as if the viewer opens the frame in a new tab. Such content should be also served from a _separate origin_ to limit potential damage.

**Note:** When redirecting the user, opening a popup window, or opening a new tab from an embedded page within an `<iframe>` with the `sandbox` attribute, the new browsing context is subject to the same `sandbox` restrictions. This can create issues — for example, if a page embedded within an `<iframe>` without a `sandbox="allow-forms"` or `sandbox="allow-popups-to-escape-sandbox"` attribute set on it opens a new site in a separate tab, form submission in that new browsing context will silently fail.

[`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#src)

The URL of the page to embed. Use a value of `about:blank` to embed an empty page that conforms to the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy#inherited_origins)
. Also note that programmatically removing an `<iframe>`'s src attribute (e.g., via [`Element.removeAttribute()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttribute)
) causes `about:blank` to be loaded in the frame in Firefox (from version 65), Chromium-based browsers, and Safari/iOS.

**Note:** The `about:blank` page uses the embedding document's URL as its base URL when resolving any relative URLs, such as anchor links.

[`srcdoc`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#srcdoc)

Inline HTML to embed, overriding the `src` attribute. Its content should follow the syntax of a full HTML document, which includes the doctype directive, `<html>`, `<body>` tags, etc., although most of them can be omitted, leaving only the body content. This doc will have `about:srcdoc` as its location. If a browser does not support the `srcdoc` attribute, it will fall back to the URL in the `src` attribute.

**Note:** The `about:srcdoc` page uses the embedding document's URL as its base URL when resolving any relative URLs, such as anchor links.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#width)

The width of the frame in CSS pixels. Default is `300`.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#deprecated_attributes)

These attributes are deprecated and may no longer be supported by all user agents. You should not use them in new content, and try to remove them from existing content.

[`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#align)

The alignment of this element with respect to the surrounding context.

[`frameborder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#frameborder)

The value `1` (the default) draws a border around this frame. The value `0` removes the border around this frame, but you should instead use the CSS property [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 to control `<iframe>` borders.

[`longdesc`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#longdesc)

A URL of a long description of the frame's content. Due to widespread misuse, this is not helpful for non-visual browsers.

[`marginheight`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#marginheight)

The amount of space in pixels between the frame's content and its top and bottom borders.

[`marginwidth`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#marginwidth)

The amount of space in pixels between the frame's content and its left and right borders.

[`scrolling`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#scrolling)

Indicates when the browser should provide a scrollbar for the frame:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#auto)

Only when the frame's content is larger than its dimensions.

[`yes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#yes)

Always show a scrollbar.

[`no`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#no)

Never show a scrollbar.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#usage_notes)

-------------------------------------------------------------------------------------------------------

Each embedded browsing context has its own [document](https://developer.mozilla.org/en-US/docs/Web/API/Document)
 and allows URL navigations. The navigations of each embedded browsing context are linearized into the [session history](https://developer.mozilla.org/en-US/docs/Web/API/History)
 of the _topmost_ browsing context. The browsing context that embeds the others is called the _parent browsing context_. The _topmost_ browsing context — the one with no parent — is usually the browser window, represented by the [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 object.

**Warning:** Because each browsing context is a complete document environment, every `<iframe>` in a page requires increased memory and other computing resources. While theoretically you can use as many `<iframe>`s as you like, check for performance problems.

### [Scripting](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#scripting)

Inline frames, like [`<frame>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame)
 elements, are included in the [`window.frames`](https://developer.mozilla.org/en-US/docs/Web/API/Window/frames)
 pseudo-array.

With the DOM [`HTMLIFrameElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement)
 object, scripts can access the [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 object of the framed resource via the [`contentWindow`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/contentWindow "contentWindow")
 property. The [`contentDocument`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/contentDocument "contentDocument")
 property refers to the `document` inside the `<iframe>`, same as `contentWindow.document`.

From the inside of a frame, a script can get a reference to its parent window with [`window.parent`](https://developer.mozilla.org/en-US/docs/Web/API/Window/parent)
.

Script access to a frame's content is subject to the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy)
. Scripts cannot access most properties in other `window` objects if the script was loaded from a different origin, including scripts inside a frame accessing the frame's parent. Cross-origin communication can be achieved using [`Window.postMessage()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)
.

#### Top navigation in cross-origin frames

Scripts running in a same-origin frame can access the [`Window.top`](https://developer.mozilla.org/en-US/docs/Web/API/Window/top)
 property and set [`window.top.location`](https://developer.mozilla.org/en-US/docs/Web/API/Window/location "window.top.location")
 to redirect the top-level page to a new location. This behavior is referred to as "top navigation".

A cross-origin frame is allowed to redirect the top-level page using `top` only if the frame has [sticky activation](https://developer.mozilla.org/en-US/docs/Glossary/Sticky_activation)
. If top navigation is blocked, browsers may either prompt for user permission to redirect or report the error in the developer console (or both). This restriction by browsers is called _framebusting intervention_. What this means is that a cross-origin frame can't immediately redirect the top-level page — the user must have previously interacted with the frame or granted permission to redirect.

A sandboxed frame blocks all top navigation unless the `sandbox` attribute values are set to [`allow-top-navigation`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-top-navigation)
 or [`allow-top-navigation-by-user-activation`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allow-top-navigation-by-user-activation)
. Note that top-navigation permissions are inherited, so a nested frame can perform a top navigation only if its parent frames are also allowed to.

### [Embedding PDFs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#embedding_pdfs)

An `<iframe>` can display a PDF using the browser's built-in PDF viewer. Unlike [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
, it does not support child content as a fallback if the PDF cannot be displayed. Provide a link outside the `<iframe>` so users can open the PDF separately.

The [`sandbox`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#sandbox)
 attribute can prevent the built-in PDF viewer from loading, even with `allow-scripts` or `allow-downloads`. It is not a portable way to add restrictions to a native PDF preview. The browser's PDF viewer already sandboxes all executable content.

### [Positioning and scaling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#positioning_and_scaling)

Being a [replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
, the `<iframe>` allows the position of the embedded document within its box to be adjusted using the [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
 property.

**Note:** The [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 property has no effect on `<iframe>` elements.

### [`error` and `load` event behavior](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#error_and_load_event_behavior)

The `error` and `load` events fired on `<iframe>`s could be used to probe the URL space of the local network's HTTP servers. Therefore, as a security precaution user agents do not fire the [error](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/error_event)
 event on `<iframe>`s, and the [load](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/load_event)
 event is always triggered even if the `<iframe>` content fails to load.

### [Responsive `<iframe>` sizing](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#responsive_iframe_sizing)

For security and privacy reasons, `<iframe>` elements do not by default expose any information to the parent document about the size of the content in the document they are embedding.

To enable responsive sizing of `<iframe>` elements based on their content, the [`<meta name="responsive-embedded-sizing">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/responsive-embedded-sizing)
 tag can be included in an embedded document to opt it in to sharing its size information with the parent document. The [`frame-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing)
 CSS property can then be set on the `<iframe>` to cause it to adopt the same horizontal or vertical size as the embedded document's actual content size. This ensures that `<iframe>` content fits seamlessly into its embedder, avoiding unnecessary scrollbars.

To resize the `<iframe>` dynamically as the embedded document changes layout size, you can call the [`Window.requestResize()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestResize)
 method from the embedded document to make it report an updated size.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#accessibility)

-----------------------------------------------------------------------------------------------------------

People navigating with assistive technology such as a screen reader can use the [`title` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 on an `<iframe>` to label its content. The title's value should concisely describe the embedded content:

html

    <iframe
      title="Wikipedia page for Avocados"
      src="https://en.wikipedia.org/wiki/Avocado"></iframe>
    

Without this title, they have to navigate into the `<iframe>` to determine what its embedded content is. This context shift can be confusing and time-consuming, especially for pages with multiple `<iframe>`s and/or if embeds contain interactive content like video or audio.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#examples)

-------------------------------------------------------------------------------------------------

### [A basic <iframe>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#a_basic_iframe)

This example embeds the page at [https://example.org](https://example.org/ "External link (opens in new tab)")
 in an iframe. This is a common use case of iframes: to embed content from another site. For example, the live sample itself, and the [try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#try_it)
 example at the top, are both `<iframe>` embeds of content from another MDN site.

#### HTML

html

    <iframe
      src="https://example.org"
      title="iframe Example 1"
      width="400"
      height="300">
    </iframe>
    

#### Result

### [Embedding source code in an <iframe>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#embedding_source_code_in_an_iframe)

This example directly renders source code in an iframe. This can be used as a technique to prevent script injection when displaying user-generated content, when combined with the `sandbox` attribute.

Note that when using `srcdoc`, any relative URLs in the embedded content will be resolved relative to the URL of the embedding page. If you want to use anchor links that point to places in the embedded content, you need to explicitly specify `about:srcdoc` as the base URL.

#### HTML

html

    <article>
      <footer>Nine minutes ago, <i>jc</i> wrote:</footer>
      <iframe
        sandbox
        srcdoc="<p>There are two ways to use the <code>iframe</code> element:</p>
    <ol>
    <li><a href=&quot;about:srcdoc#embed_another&quot;>To embed content from another page</a></li>
    <li><a href=&quot;about:srcdoc#embed_user&quot;>To embed user-generated content</a></li>
    </ol>
    <h2 id=&quot;embed_another&quot;>Embedding content from another page</h2>
    <p>Use the <code>src</code> attribute to specify the URL of the page to embed:</p>
    <pre><code>&amp;lt;iframe src=&quot;https://example.org&quot;&amp;gt;&amp;lt;/iframe&amp;gt;</code></pre>
    <h2 id=&quot;embed_user&quot;>Embedding user-generated content</h2>
    <p>Use the <code>srcdoc</code> attribute to specify the content to embed. This post is already an example!</p>
    "
        width="500"
        height="250"
    ></iframe>
    </article>
    

Here's how to write escape sequences when using `srcdoc`:

*   First, write the HTML out, escaping anything you would escape in a normal HTML document (such as `<`, `>`, `&`, etc.).
*   `&lt;` and `<` represent the exact same character in the `srcdoc` attribute. Therefore, to make it an actual escape sequence in the HTML document, replace any ampersands (`&`) with `&amp;`. For example, `&lt;` becomes `&amp;lt;`, and `&amp;` becomes `&amp;amp;`.
*   Replace any double quotes (`"`) with `&quot;` to prevent the `srcdoc` attribute from being prematurely terminated (if you use `'` instead, then you should replace `'` with `&apos;` instead). This step happens after the previous one, so `&quot;` generated in this step doesn't become `&amp;quot;`.

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, embedded content, interactive content, palpable content. |
| Permitted content | None. |
| Tag omission | None, both the starting and ending tags are mandatory. |
| Permitted parents | Any element that accepts embedded content. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | [`application`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role)<br>, [`document`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/document_role)<br>, [`img`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/img_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role) |
| DOM interface | [`HTMLIFrameElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-iframe-element](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-iframe-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#see_also)

-------------------------------------------------------------------------------------------------

*   [CSP: frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/frame-ancestors)
    
*   [Privacy, permissions, and information security](https://developer.mozilla.org/en-US/docs/Web/Privacy)
    
*   [Local network access](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Local_network_access)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/iframe/index.md?plain=1 "Folder: en-us/web/html/reference/elements/iframe (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fiframe&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fiframe%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fiframe%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fiframe%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcb7d4dde9f0a43664c64587d9d70b8835286eb7%0A*+Document+last+modified%3A+2026-10-01T19%3A41%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")