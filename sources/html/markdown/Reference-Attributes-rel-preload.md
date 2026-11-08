*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#mdn-search)
    

`rel="preload"` HTML attribute value
====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2021.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The `preload` value of the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 element's [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#rel)
 attribute lets you declare fetch requests in the HTML's [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
, specifying resources that your page will need very soon, which you want to start loading early in the page lifecycle, before browsers' main rendering machinery kicks in. This ensures they are available earlier and are less likely to block the page's render, improving performance. Even though the name contains the term _load_, it doesn't load and execute the script but only schedules it to be downloaded and cached with a higher priority.

[The basics](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#the_basics)

------------------------------------------------------------------------------------------------------------

You most commonly use `<link>` to load a CSS file to style your page with:

Here however, we will use a `rel` value of `preload`, which turns `<link>` into a preloader for any resource we want. You will also need to specify:

*   The path to the resource in the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#href)
     attribute.
*   The type of resource in the [`as`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#as)
     attribute.

An example might look like this (see our [JS and CSS example source](https://github.com/mdn/html-examples/tree/main/link-rel-preload/js-and-css "External link (opens in new tab)")
, and [also live](https://mdn.github.io/html-examples/link-rel-preload/js-and-css/ "External link (opens in new tab)")
):

Here we preload our CSS and JavaScript files so they will be available as soon as they are required for the rendering of the page later on. This example is trivial, as the browser probably discovers the `<link rel="stylesheet">` and `<script>` elements in the same chunk of HTML as the preloads, but the benefits can be seen much more clearly the later resources are discovered and the larger they are. For example:

*   Resources that are pointed to from inside CSS, like fonts or images.
*   Resources that JavaScript can request, like imported scripts.

`preload` has other advantages too. Using `as` to specify the type of content to be preloaded allows the browser to:

*   Store in the cache for future requests, reusing the resource if appropriate.
*   Apply the correct [content security policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
     to the resource.
*   Set the correct [`Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept)
     request headers for it.

### [What types of content can be preloaded?](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#what_types_of_content_can_be_preloaded)

Many content types can be preloaded. The possible `as` attribute values are:

*   `fetch`: Resource to be accessed by a fetch or XHR request, such as an ArrayBuffer, WebAssembly binary, or JSON file.
*   `font`: Font file.
*   `image`: Image file.
*   `script`: JavaScript file.
*   `style`: CSS stylesheet.
*   `track`: WebVTT file.

**Note:** `font` and `fetch` preloading requires the `crossorigin` attribute to be set; see [CORS-enabled fetches](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#cors-enabled_fetches)
 below.

**Note:** There's more detail about these values and the web features they expect to be consumed by in the HTML spec — see [Link type "preload"](https://html.spec.whatwg.org/multipage/links.html#link-type-preload "External link (opens in new tab)")
. Also note that the full list of values the `as` attribute can take is governed by the HTML spec — see [Link type "preload" destinations](https://html.spec.whatwg.org/multipage/links.html#preload-destination "External link (opens in new tab)")
.

[Including a MIME type](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#including_a_mime_type)

----------------------------------------------------------------------------------------------------------------------------------

`<link>` elements can accept a [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#type)
 attribute, which contains the MIME type of the resource the element points to. This is especially useful when preloading resources — the browser will use the `type` attribute value to work out if it supports that resource, and will only download it if so, ignoring it if not.

The code in the example above causes the `image/avif` image to be preloaded only in supporting browsers — and for users who have `image/avif` support in their browsers, causes the `image/avif` image to actually be used (since it's the first [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 specified). That makes the image download hopefully smaller for users who have `image/avif` support in their browsers.

Note that for users whose browsers have both `image/avif` and `image/webp` support, if in that code a `<link rel="preload" href="flower.webp" as="image" type="image/webp">` element were also specified, then _both_ the `image/avif` and `image/webp` images would be preloaded — even though only one of them would actually be used.

Therefore, specifying preloading for multiple types of the same resource is discouraged. Instead, the best practice is to specify preloading only for the type the majority of your users are likely to actually use. That's why the code in the example above doesn't specify preloading for the `image/webp` image.

However, the lack of preloading doesn't prevent the `image/webp` image from actually being used by those who need it: for users whose browsers don't have `image/avif` support but do have `image/webp` support, the code in the example above does still cause the `image/webp` image to be used — but it does so without also causing it to also be preloaded unnecessarily for the majority of other users.

[CORS-enabled fetches](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#cors-enabled_fetches)

--------------------------------------------------------------------------------------------------------------------------------

When preloading resources that are fetched with [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
 enabled (e.g., [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch)
, [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
 or [fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
), special care needs to be taken to setting the [`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#crossorigin)
 attribute on your [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 element. The attribute needs to be set to match the resource's CORS and credentials mode, even when the fetch is not cross-origin.

As mentioned above, one interesting case where this applies is font files. Because of various reasons, these have to be fetched using anonymous-mode CORS (see [Font fetching requirements](https://drafts.csswg.org/css-fonts/#font-fetching-requirements "External link (opens in new tab)")
).

Let's use this case as an example. You can see the full [example source code on GitHub](https://github.com/mdn/html-examples/tree/main/link-rel-preload/fonts "External link (opens in new tab)")
 ([also see it live](https://mdn.github.io/html-examples/link-rel-preload/fonts/ "External link (opens in new tab)")
):

Not only are we providing the MIME type hints in the `type` attributes, but we are also providing the `crossorigin` attribute to make sure the preload's CORS mode matches the eventual font resource request.

[Including media](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#including_media)

----------------------------------------------------------------------------------------------------------------------

One nice feature of `<link>` elements is their ability to accept [`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#media)
 attributes. These can accept [media types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_types)
 or full-blown [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
, allowing you to do responsive preloading!

Let's look at an example (see it on GitHub — [source code](https://github.com/mdn/html-examples/tree/main/link-rel-preload/media "External link (opens in new tab)")
, [live example](https://mdn.github.io/html-examples/link-rel-preload/media/ "External link (opens in new tab)")
):

We include `media` attributes on our `<link>` elements so that a narrow image is preloaded if the user has a narrow viewport, and a wider image is loaded if they have a wide viewport. We use [`Window.matchMedia`](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia)
 / [`MediaQueryList`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList)
 to do this (see [Testing media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing)
 for more).

This same technique also applies to other resource types. For example, when used with fonts, preloading makes it more likely the font will be available at render time, reducing the chance of a flash of unstyled text (FOUT).

This doesn't have to be limited to images, or even files of the same type — think big! You could perhaps preload and display a simplified SVG diagram if the user is on a narrow screen where bandwidth and CPU is potentially more limited, or preload a complex chunk of JavaScript then use it to render an interactive 3D model if the user's resources are more plentiful.

[Scripting and preloads](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#scripting_and_preloads)

------------------------------------------------------------------------------------------------------------------------------------

**Note:** Use [`<link rel="modulepreload">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload)
 instead if you are working with [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
.

Another nice thing about these preloads is that you can execute them with script. For example, here we create a [`HTMLLinkElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLinkElement)
 instance, then attach it to the DOM:

This means that the browser will preload the `myscript.js` file, but not actually use it yet. To use it, you could do this:

This is useful when you want to preload a script, but then defer execution until exactly when you need it.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# link-type-preload](https://html.spec.whatwg.org/multipage/links.html#link-type-preload) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload#see_also)

--------------------------------------------------------------------------------------------------------

*   [Speculative loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Speculative_loading)
     for a comparison of `<link rel="preload">` and other similar performance improvement features.
*   [Preload: What Is It Good For?](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/ "External link (opens in new tab)")
     by Yoav Weiss

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/rel/preload/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/rel/preload (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fpreload&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fpreload%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fpreload%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fpreload%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffc7c0c6df803d5ce26e7b2a72725a7d021ed0694%0A*+Document+last+modified%3A+2026-05-20T15%3A49%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")