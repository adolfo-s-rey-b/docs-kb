*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#mdn-search)
    

`<a>` HTML anchor element
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<a>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element (or _anchor_ element), with [its `href` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
, creates a hyperlink to web pages, files, email addresses, locations in the same page, or anything else a URL can address.

Content within each `<a>` _should_ indicate the link's destination. If the `href` attribute is present, pressing the enter key while focused on the `<a>` element will activate it.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#try_it)

----------------------------------------------------------------------------------------

    <p>You can reach Michael at:</p>
    
    <ul>
      <li><a href="https://example.com">Website</a></li>
      <li><a href="mailto:m.bluth@example.com">Email</a></li>
      <li><a href="tel:+123456789">Phone</a></li>
    </ul>
    

    li {
      margin-bottom: 0.5rem;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#attributes)

------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`attributionsrc`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#attributionsrc)

Specifies that you want the browser to send an [`Attribution-Reporting-Eligible`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Eligible)
 header. On the server-side this is used to trigger sending an [`Attribution-Reporting-Register-Source`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Source)
 header in the response, to register a [navigation-based attribution source](https://developer.mozilla.org/en-US/docs/Web/API/Attribution_Reporting_API/Registering_sources#navigation-based_attribution_sources)
.

The browser stores the source data associated with the navigation-based attribution source (as provided in the [`Attribution-Reporting-Register-Source`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Source)
 response header) when the user clicks the link. See the [Attribution Reporting API](https://developer.mozilla.org/en-US/docs/Web/API/Attribution_Reporting_API)
 for more details.

There are two versions of this attribute that you can set:

*   Boolean, i.e., just the `attributionsrc` name. This specifies that you want the [`Attribution-Reporting-Eligible`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Eligible)
     header sent to the same server as the `href` attribute points to. This is fine when you are handling the attribution source registration on the same server.
    
*   Value containing one or more URLs, for example:
    
    html
    
        attributionsrc="https://a.example/register-source
        https://b.example/register-source"
        
    
    This is useful in cases where the requested resource is not on a server you control, or you just want to handle registering the attribution source on a different server. In this case, you can specify one or more URLs as the value of `attributionsrc`. When the resource request occurs, the [`Attribution-Reporting-Eligible`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Eligible)
     header will be sent to the URL(s) specified in `attributionsrc` in addition to the resource origin. These URLs can then respond with the [`Attribution-Reporting-Register-Source`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Attribution-Reporting-Register-Source)
     to complete registration.
    
    **Note:** Specifying multiple URLs means that multiple attribution sources can be registered on the same feature. You might for example have different campaigns that you are trying to measure the success of, which involve generating different reports on different data.
    

`<a>` elements cannot be used as attribution triggers, only sources.

[`download`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#download)

Causes the browser to treat the linked URL as a download. Can be used with or without a `filename` value:

*   Without a value, the browser will suggest a filename/extension, generated from various sources:
    
    *   The [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Disposition)
         HTTP header
    *   The final segment in the URL [path](https://developer.mozilla.org/en-US/docs/Web/API/URL/pathname)
        
    *   The [media type](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type)
         (from the [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type)
         header, the start of a [`data:` URL](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data)
        , or [`Blob.type`](https://developer.mozilla.org/en-US/docs/Web/API/Blob/type)
         for a [`blob:` URL](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/blob)
        )
*   `filename`: defining a value suggests it as the filename. `/` and `\` characters are converted to underscores (`_`). Filesystems may forbid other characters in filenames, so browsers will adjust the suggested name if necessary. This adjustment happens when the download is triggered and is not observable via the [`HTMLAnchorElement.download`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/download)
     property.
    

**Note:**

*   `download` only works for [same-origin URLs](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy)
    , same-origin [`blob:`](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/blob)
    , and [`data:`](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data)
     schemes. For other URLs, the `download` attribute is ignored and a normal navigation happens, although the target page may still use `Content-Disposition` to instruct a download.
*   How browsers treat downloads varies by browser, user settings, and other factors. The user may be prompted before a download starts, or the file may be saved automatically, or it may open automatically, either in an external application or in the browser itself.
*   The `download` attribute, when honored, overrides the `Content-Disposition: inline` behavior, but the `filename` parameter of `Content-Disposition` overrides the name in the `download` attribute.

[`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)

The URL that the hyperlink points to. Links are not restricted to HTTP-based URLs — they can use any URL scheme supported by browsers:

*   Telephone numbers with `tel:` URLs
*   Email addresses with `mailto:` URLs
*   SMS text messages with `sms:` URLs
*   Executable code with [`javascript:` URLs](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/javascript)
    
*   While web browsers may not support other URL schemes, websites can with [`registerProtocolHandler()`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/registerProtocolHandler)
    

Moreover other URL features can locate specific parts of the resource, including:

*   Sections of a page with document fragments
*   Specific text portions with [text fragments](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment/Text_fragments)
    
*   Pieces of media files with media fragments

[`hreflang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#hreflang)

Hints at the human language of the linked URL. No built-in functionality. Allowed values are the same as [the global `lang` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
.

[`interestfor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#interestfor)

Defines the `<a>` element as an **interest invoker**. Its value is the `id` of the target element, which will be affected in some way (normally shown or hidden) when interest is shown or lost on the invoker element (for example, by hovering/unhovering or focusing/blurring it). See [Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
 for more details and examples.

[`ping`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#ping)

A space-separated list of URLs. When the link is followed, the browser will send [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST)
 requests with the body `PING` to the URLs. Typically for tracking.

[`referrerpolicy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#referrerpolicy)

How much of the [referrer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
 to send when fetching the linked resource.

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

The relationship of the linked URL as space-separated link types.

[`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#target)

Where to display the linked URL, as the name for a _browsing context_ (a tab, window, or [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
). The following keywords have special meanings for where to load the URL:

*   `_self`: The current browsing context. (Default)
*   `_blank`: Usually a new tab, but users can configure browsers to open a new window instead.
*   `_parent`: The parent browsing context of the current one. If no parent, behaves as `_self`.
*   `_top`: The topmost browsing context. To be specific, this means the "highest" context that's an ancestor of the current one. If no ancestors, behaves as `_self`.
*   `_unfencedTop`: Allows embedded [fenced frames](https://developer.mozilla.org/en-US/docs/Web/API/Fenced_frame_API)
     to navigate the top-level frame (i.e., traversing beyond the root of the fenced frame, unlike other reserved destinations). Note that the navigation will still succeed if this is used outside of a fenced frame context, but it will not act like a reserved keyword.

**Note:** Setting `target="_blank"` on `<a>` elements implicitly provides the same `rel` behavior as setting [`rel="noopener"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener)
 which does not set `window.opener`.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#type)

Hints at the linked URL's format with a [MIME type](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type)
. No built-in functionality.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#deprecated_attributes)

[`charset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#charset)

Hinted at the [character encoding](https://developer.mozilla.org/en-US/docs/Glossary/Character_encoding)
 of the linked URL.

**Note:** This attribute is deprecated and **should not be used by authors**. Use the HTTP [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type)
 header on the linked URL.

[`coords`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#coords)

Used with [the `shape` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#shape)
. A comma-separated list of coordinates.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#name)

Was required to define a possible target location in a page. In HTML 4.01, `id` and `name` could both be used on `<a>`, as long as they had identical values.

**Note:** Use the global attribute [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 instead.

[`rev`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#rev)

Specified a reverse link; the opposite of [the `rel` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#rel)
. Deprecated for being very confusing.

[`shape`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#shape)

The shape of the hyperlink's region in an image map.

**Note:** Use the [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 element for image maps instead.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#accessibility)

------------------------------------------------------------------------------------------------------

### [Strong link text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#strong_link_text)

**The content inside a link should indicate where the link goes**, even out of context.

#### Inaccessible, weak link text

A sadly common mistake is to only link the words "click here" or "here":

html

    <p>Learn more about our products <a href="/products">here</a>.</p>
    

##### Result

#### Accessible, strong link text

Luckily, this is an easy fix, and it's actually shorter than the inaccessible version!

html

    <p>Learn more <a href="/products">about our products</a>.</p>
    

##### Result

Assistive software has shortcuts to list all links on a page. However, strong link text benefits all users — the "list all links" shortcut emulates how sighted users quickly scan pages.

### [onclick events](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#onclick_events)

Anchor elements are often abused as fake buttons by setting their `href` to `#` or [`javascript:void(0)`](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/javascript)
 to prevent the page from refreshing, then listening for their `click` events.

These bogus `href` values cause unexpected behavior when copying/dragging links, opening links in a new tab/window, bookmarking, or when JavaScript is loading, errors, or is disabled. They also convey incorrect semantics to assistive technologies, like screen readers.

Use a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 instead. In general, **you should only use a hyperlink for navigation to a real URL**.

### [External links and linking to non-HTML resources](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#external_links_and_linking_to_non-html_resources)

Links that open in a new tab/window via `target="_blank"`, or links that point to a download file should indicate what will happen when the link is followed.

People experiencing low vision conditions, navigating with the aid of screen reading technology, or with cognitive concerns may be confused when a new tab, window, or application opens unexpectedly. Older screen-reading software may not even announce the behavior.

#### Link that opens a new tab/window

html

    <a target="_blank" href="https://www.wikipedia.org">
      Wikipedia (opens in new tab)
    </a>
    

##### Result

#### Link to a non-HTML resource

If an icon is used to signify link behavior, make sure it has an [`alt` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#alt)
 to describe its purpose. In case the icon is missing, the `alt` attribute's content will still convey the link's behavior.

html

    <p>
      <a href="https://www.wikipedia.org/" target="_blank">
        Wikipedia
        <img src="new-tab.svg" width="14" alt="(Opens in new tab)" />
      </a>
      <br />
      <a href="2017-annual-report.ppt">
        2017 annual report
        <img src="powerpoint.svg" width="14" alt="(PowerPoint file)" />
      </a>
    </p>
    <p>
      <a href="https://www.wikipedia.org/" target="_blank">
        Wikipedia
        <img src="missing-icon.svg" width="14" alt="(Opens in new tab)" />
      </a>
      <br />
      <a href="2017-annual-report.ppt">
        2017 annual report
        <img src="missing-icon.svg" width="14" alt="(PowerPoint file)" />
      </a>
    </p>
    

##### Result

*   [WebAIM: Links and Hypertext - Hypertext Links](https://webaim.org/techniques/hypertext/hypertext_links "External link (opens in new tab)")
    
*   [MDN / Understanding WCAG, Guideline 3.2](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Understandable#guideline_3.2_%E2%80%94_predictable_make_web_pages_appear_and_operate_in_predictable_ways)
    
*   [G200: Opening new windows and tabs from a link only when necessary](https://www.w3.org/TR/WCAG20-TECHS/G200.html "External link (opens in new tab)")
    
*   [G201: Giving users advanced warning when opening a new window](https://www.w3.org/TR/WCAG20-TECHS/G201.html "External link (opens in new tab)")
    

### [Skip links](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#skip_links)

A **skip link** is a link placed as early as possible in [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 content that points to the beginning of the page's main content. Usually, CSS hides a skip link offscreen until focused.

html

    <body>
      <a href="#content" class="skip-link">Skip to main content</a>
    
      <header>…</header>
    
      <!-- The skip link jumps to here -->
      <main id="content"></main>
    </body>
    

css

    .skip-link {
      position: absolute;
      top: -3em;
      background: white;
    }
    .skip-link:focus {
      top: 0;
    }
    

#### Result

Skip links let keyboard users bypass content repeated throughout multiple pages, such as header navigation.

Skip links are especially useful for people who navigate with the aid of assistive technology such as switch control, voice command, or mouth sticks/head wands, where the act of moving through repetitive links can be laborious.

*   [WebAIM: "Skip Navigation" Links](https://webaim.org/techniques/skipnav/ "External link (opens in new tab)")
    
*   [How-to: Use Skip Navigation links](https://www.a11yproject.com/posts/skip-nav-links/ "External link (opens in new tab)")
    
*   [MDN / Understanding WCAG, Guideline 2.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.4_%e2%80%94_navigable_provide_ways_to_help_users_navigate_find_content_and_determine_where_they_are)
    
*   [Understanding Success Criterion 2.4.1](https://www.w3.org/TR/UNDERSTANDING-WCAG20/navigation-mechanisms-skip.html "External link (opens in new tab)")
    

### [Size and proximity](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#size_and_proximity)

#### Size

Interactive elements, like links, should provide an area large enough that it is easy to activate them. This helps a variety of people, including those with motor control issues and those using imprecise inputs such as a touchscreen. A minimum size of 44×44 [CSS pixels](https://w3c.github.io/wcag/guidelines/22/#dfn-css-pixels "External link (opens in new tab)")
 is recommended.

Text-only links in prose content are exempt from this requirement, but it's still a good idea to make sure enough text is hyperlinked to be easily activated.

*   [Understanding Success Criterion 2.5.5: Target Size](https://www.w3.org/WAI/WCAG21/Understanding/target-size.html "External link (opens in new tab)")
    
*   [Target Size and 2.5.5](https://adrianroselli.com/2019/06/target-size-and-2-5-5.html "External link (opens in new tab)")
    
*   [Quick test: Large touch targets](https://www.a11yproject.com/posts/large-touch-targets/ "External link (opens in new tab)")
    

#### Proximity

Interactive elements, like links, placed in close visual proximity should have space separating them. Spacing helps people with motor control issues, who may otherwise accidentally activate the wrong interactive content.

Spacing may be created using CSS properties like [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
.

*   [Hand tremors and the giant-button-problem](https://axesslab.com/hand-tremors/ "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#examples)

--------------------------------------------------------------------------------------------

### [Linking to an absolute URL](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#linking_to_an_absolute_url)

#### HTML

html

    <a href="https://www.mozilla.com">Mozilla</a>
    

#### Result

### [Linking to relative URLs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#linking_to_relative_urls)

#### HTML

html

    <a href="//example.com">Scheme-relative URL</a>
    <a href="/en-US/docs/Web/HTML">Origin-relative URL</a>
    <a href="p">Directory-relative URL</a>
    <a href="./p">Directory-relative URL</a>
    <a href="../p">Parent-directory-relative URL</a>
    

    a {
      display: block;
      margin-bottom: 0.5em;
    }
    

#### Result

### [Linking to an element on the same page](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#linking_to_an_element_on_the_same_page)

html

    <!-- <a> element links to the section below -->
    <p><a href="#Section_further_down">Jump to the heading below</a></p>
    
    <!-- Heading to link to -->
    <h2 id="Section_further_down">Section further down</h2>
    

#### Result

**Note:** You can use `href="#top"` or the empty fragment (`href="#"`) to link to the top of the current page, [as defined in the HTML specification](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scroll-to-the-fragment-identifier "External link (opens in new tab)")
.

### [Linking to an email address](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#linking_to_an_email_address)

To create links that open in the user's email program to let them send a new message, use the `mailto:` scheme:

html

    <a href="mailto:nowhere@mozilla.org">Send email to nowhere</a>
    

#### Result

For details about `mailto:` URLs, such as including a subject or body, see [Email links](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Creating_links#email_links)
 or [RFC 6068](https://datatracker.ietf.org/doc/html/rfc6068 "External link (opens in new tab)")
.

### [Linking to telephone numbers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#linking_to_telephone_numbers)

html

    <a href="tel:+49.157.0156">+49 157 0156</a>
    <a href="tel:+1(800)555-0123">(800) 555-0123</a>
    

#### Result

`tel:` link behavior varies with device capabilities:

*   Cellular devices autodial the number.
*   Most operating systems have programs that can make calls, like Skype or FaceTime.
*   Websites can make phone calls with [`registerProtocolHandler`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/registerProtocolHandler "registerProtocolHandler")
    , such as `web.skype.com`.
*   Other behaviors include saving the number to contacts, or sending the number to another device.

See [RFC 3966](https://datatracker.ietf.org/doc/html/rfc3966 "External link (opens in new tab)")
 for syntax, additional features, and other details about the `tel:` URL scheme.

### [Using the download attribute to save a <canvas> as a PNG](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#using_the_download_attribute_to_save_a_canvas_as_a_png)

To save a [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 element's contents as an image, you can create a link where the `href` is the canvas data as a `data:` URL created with JavaScript and the `download` attribute provides the file name for the downloaded PNG file:

#### Example painting app with save link

##### HTML

html

    <p>
      Paint by holding down the mouse button and moving it.
      <a href="" download="my_painting.png">Download my painting</a>
    </p>
    
    <canvas width="300" height="300"></canvas>
    

##### CSS

css

    html {
      font-family: sans-serif;
    }
    canvas {
      background: white;
      border: 1px dashed;
    }
    a {
      display: inline-block;
      background: #6699cc;
      color: white;
      padding: 5px 10px;
    }
    

##### JavaScript

js

    const canvas = document.querySelector("canvas");
    const c = canvas.getContext("2d");
    c.fillStyle = "hotpink";
    let isDrawing;
    
    function draw(x, y) {
      if (isDrawing) {
        c.beginPath();
        c.arc(x, y, 10, 0, Math.PI * 2);
        c.closePath();
        c.fill();
      }
    }
    
    canvas.addEventListener("mousemove", (event) =>
      draw(event.offsetX, event.offsetY),
    );
    canvas.addEventListener("mousedown", () => (isDrawing = true));
    canvas.addEventListener("mouseup", () => (isDrawing = false));
    
    document
      .querySelector("a")
      .addEventListener(
        "click",
        (event) => (event.target.href = canvas.toDataURL()),
      );
    

##### Result

[Security and privacy](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#security_and_privacy)

--------------------------------------------------------------------------------------------------------------------

`<a>` elements can have consequences for the security and privacy of users. See [`Referer` header: privacy and security concerns](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Referer_header:_privacy_and_security_concerns)
 for information.

Using `target="_blank"` without [`rel="noreferrer"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noreferrer)
 and [`rel="noopener"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener)
 makes the website vulnerable to [`window.opener`](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)
 API exploitation attacks, although note that, in newer browser versions setting `target="_blank"` implicitly provides the same protection as setting `rel="noopener"`. See [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#browser_compatibility)
 for details.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#technical_summary)

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)<br>, palpable content. |
| Permitted content | [Transparent](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#transparent_content_model)<br>, except that no descendant may be [interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)<br> or an `<a>` element, and no descendant may have a specified [tabindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)<br> attribute. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, but not other `<a>` elements. |
| Implicit ARIA role | [`link`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/link_role)<br> when `href` attribute is present, otherwise [`generic`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) |
| Permitted ARIA roles | When `href` attribute is present:<br><br>*   [`button`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role)<br>    <br>*   [`checkbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/checkbox_role)<br>    <br>*   [`menuitem`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitem_role)<br>    <br>*   [`menuitemcheckbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role)<br>    <br>*   [`menuitemradio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemradio_role)<br>    <br>*   [`option`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/option_role)<br>    <br>*   [`radio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radio_role)<br>    <br>*   [`switch`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/switch_role)<br>    <br>*   [`tab`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role)<br>    <br>*   [`treeitem`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role)<br>    <br><br>When `href` attribute is not present:<br><br>*   any |
| DOM interface | [`HTMLAnchorElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-a-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#see_also)

--------------------------------------------------------------------------------------------

*   [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
     is similar to `<a>`, but for metadata hyperlinks that are invisible to users.
*   [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
     is a CSS pseudo-class that will match `<a>` elements with URL in `href` attribute that was not yet visited by the user.
*   [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
     is a CSS pseudo-class that will match `<a>` elements with URL in `href` attribute that was visited by the user in the past.
*   [`:any-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link)
     is a CSS pseudo-class that will match `<a>` elements with `href` attribute.
*   [Text fragments](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment/Text_fragments)
     are user-agent instructions added to URLs that allow content authors to link to specific text on a page, without IDs being required.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/a/index.md?plain=1 "Folder: en-us/web/html/reference/elements/a (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fa&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fa%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fa%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fa%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F94172439968170ab04c730b4f93a699688f7f367%0A*+Document+last+modified%3A+2026-10-28T20%3A26%3A19.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")