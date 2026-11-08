*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#mdn-search)
    

`<area>` HTML image map area element
====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<area>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [hypertext links](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink)
.

This element is used only within a [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
 element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#try_it)

-------------------------------------------------------------------------------------------

    <map name="infographic">
      <area
        shape="poly"
        coords="129,0,260,95,129,138"
        href="https://developer.mozilla.org/docs/Web/HTTP"
        alt="HTTP" />
      <area
        shape="poly"
        coords="260,96,209,249,130,138"
        href="https://developer.mozilla.org/docs/Web/HTML"
        alt="HTML" />
      <area
        shape="poly"
        coords="209,249,49,249,130,139"
        href="https://developer.mozilla.org/docs/Web/JavaScript"
        alt="JavaScript" />
      <area
        shape="poly"
        coords="48,249,0,96,129,138"
        href="https://developer.mozilla.org/docs/Web/API"
        alt="Web APIs" />
      <area
        shape="poly"
        coords="0,95,128,0,128,137"
        href="https://developer.mozilla.org/docs/Web/CSS"
        alt="CSS" />
    </map>
    <img
      usemap="#infographic"
      src="/shared-assets/images/examples/mdn-info.png"
      alt="MDN infographic" />
    

    img {
      display: block;
      margin: 0 auto;
      width: 260px;
      height: 260px;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#attributes)

---------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#alt)

A text string alternative to display on browsers that do not display images. The text should be phrased so that it presents the user with the same kind of choice as the image would offer when displayed without the alternative text. This attribute is required only if the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#href)
 attribute is used.

[`coords`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#coords)

The `coords` attribute details the coordinates of the [`shape`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#shape)
 attribute in size, shape, and placement of an `<area>`. This attribute must not be used if `shape` is set to `default`.

*   `rect`: the value is `x1,y1,x2,y2`. The value specifies the coordinates of the top-left and bottom-right corner of the rectangle. For example, in `<area shape="rect" coords="0,0,253,27" href="#" target="_blank" alt="Mozilla">` the coordinates are `0,0` and `253,27`, indicating the top-left and bottom-right corners of the rectangle, respectively.
*   `circle`: the value is `x,y,radius`. Value specifies the coordinates of the circle center and the radius. For example: `<area shape="circle" coords="130,136,60" href="#" target="_blank" alt="MDN">`
*   `poly`: the value is `x1,y1,x2,y2,..,xn,yn`. Value specifies the coordinates of the edges of the polygon. If the first and last coordinate pairs are not the same, the browser will add the last coordinate pair to close the polygon

The values are numbers of CSS pixels. Our [shape generator](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Shape_generator)
 can help you generate the `coords` syntax by selecting points on an image you upload.

[`download`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#download)

This attribute, if present, indicates that the linked resource is intended to be downloaded rather than displayed in the browser. See [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 for a full description of the [`download`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#download)
 attribute.

[`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#href)

The hyperlink target for the area. Its value is a valid URL. This attribute may be omitted; if so, the `<area>` element does not represent a hyperlink.

[`interestfor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#interestfor)

Defines the `<area>` element as an **interest invoker**. Its value is the `id` of the target element, which will be affected in some way (normally shown or hidden) when interest is shown or lost on the invoker element (for example, by hovering/unhovering or focusing/blurring it). See [Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
 for more details and examples.

[`ping`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#ping)

Contains a space-separated list of URLs to which, when the hyperlink is followed, [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST)
 requests with the body `PING` will be sent by the browser (in the background). Typically used for tracking.

[`referrerpolicy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#referrerpolicy)

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

[`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)

For anchors containing the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#href)
 attribute, this attribute specifies the relationship of the target object to the link object. The value is a space-separated list of link types. The values and their semantics will be registered by some authority that might have meaning to the document author. The default relationship, if no other is given, is void. Use this attribute only if the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#href)
 attribute is present.

[`shape`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#shape)

The shape of the associated hot spot. The specifications for HTML defines the values `rect`, which defines a rectangular region; `circle`, which defines a circular region; `poly`, which defines a polygon; and `default`, which indicates the entire region beyond any defined shapes.

[`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#target)

A keyword or author-defined name of the [browsing context](https://developer.mozilla.org/en-US/docs/Glossary/Browsing_context)
 to display the linked resource. The following keywords have special meanings:

*   `_self` (default): Show the resource in the current browsing context.
*   `_blank`: Show the resource in a new, unnamed browsing context.
*   `_parent`: Show the resource in the parent browsing context of the current one, if the current page is inside a frame. If there is no parent, acts the same as `_self`.
*   `_top`: Show the resource in the topmost browsing context (the browsing context that is an ancestor of the current one and has no parent). If there is no parent, acts the same as `_self`.

Use this attribute only if the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#href)
 attribute is present.

**Note:** Setting `target="_blank"` on `<area>` elements implicitly provides the same `rel` behavior as setting [`rel="noopener"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener)
 which does not set `window.opener`. See [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#browser_compatibility)
 for support status.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#examples)

-----------------------------------------------------------------------------------------------

### [Image with clickable areas](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#image_with_clickable_areas)

html

    <map name="primary">
      <area
        shape="circle"
        coords="75,75,75"
        href="left.html"
        alt="Click to go Left" />
      <area
        shape="circle"
        coords="275,75,75"
        href="right.html"
        alt="Click to go Right" />
    </map>
    <img
      usemap="#primary"
      src="https://dummyimage.com/350x150"
      alt="350 x 150 pic" />
    

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. The `<area>` element must have an ancestor [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)<br>, but it need not be a direct parent. |
| Implicit ARIA role | [`link`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/link_role)<br> when [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#href)<br> attribute is present, otherwise [`generic`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLAreaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAreaElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-area-element](https://html.spec.whatwg.org/multipage/image-maps.html#the-area-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/area/index.md?plain=1 "Folder: en-us/web/html/reference/elements/area (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Farea&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Farea%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Farea%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Farea%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")