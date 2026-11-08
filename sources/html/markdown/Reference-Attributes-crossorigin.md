*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#mdn-search)
    

`crossorigin` HTML attribute
============================

The **`crossorigin`** attribute, valid on the [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
, [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
, and [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 elements, provides support for [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
, defining how the element handles cross-origin requests, thereby enabling the configuration of the CORS requests for the element's fetched data. Depending on the element, the attribute can be a CORS settings attribute.

The `crossorigin` content attribute on media elements is a CORS settings attribute.

These attributes are [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
, and have the following possible values:

[`anonymous`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#anonymous)

Request uses CORS headers ([`mode`](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#mode)
 is set to `cors`) and [`credentials`](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#credentials)
 is set to `'same-origin'`, meaning that credentials such as cookies, client-side TLS certificates, and HTTP authentication headers are only included if the destination has the same origin.

[`use-credentials`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#use-credentials)

Request uses CORS headers ([`mode`](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#mode)
 is set to `cors`) and [`credentials`](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#credentials)
 is set to `'include'`, so credentials are always included, even for cross-origin requests.

[`""`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#sect)

Setting the attribute name to an empty value, like `crossorigin` or `crossorigin=""`, is the same as `anonymous`. Invalid values are also treated as the empty string.

By default (that is, when the attribute is not specified), resources are generally fetched without CORS, except [module scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#module)
 which always use CORS so only `crossorigin="use-credentials"` has an effect. The user agent will not ask for permission for full access to the resource and in the case of a cross-origin request, certain limitations will be applied based on the type of element concerned:

|     |     |
| --- | --- |
| `img`, `audio`, `video` | When resource is placed in [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)<br>, element is marked as [_tainted_](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image#security_and_tainted_canvases)<br>. |
| `script` | Access to error logging via [`window.onerror`](https://developer.mozilla.org/en-US/docs/Web/API/Window/error_event "window.onerror")<br> will be limited. |
| `link` | Request with no appropriate `crossorigin` header may be discarded. |

**Note:** The `crossorigin` attribute is not supported for [`rel="icon"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#icon)
 in Chromium-based browsers. See the [open Chromium issue](https://crbug.com/1121645 "External link (opens in new tab)")
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#examples)

--------------------------------------------------------------------------------------------------------

### [`crossorigin` with the `<script>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#crossorigin_with_the_script_element)

You can use the following [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 element to tell a browser to execute the `https://example.com/example-framework.js` script without sending user-credentials.

html

    <script
      src="https://example.com/example-framework.js"
      crossorigin="anonymous"></script>
    

### [Web manifest with credentials](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#web_manifest_with_credentials)

The `use-credentials` value must be used when fetching a [manifest](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest)
 that requires credentials, even if the file is from the same origin.

html

    <link rel="manifest" href="/app.webmanifest" crossorigin="use-credentials" />
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# cors-settings-attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cors-settings-attributes) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

### [html.elements.audio.crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#html.elements.audio.crossorigin)

### [html.elements.img.crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#html.elements.img.crossorigin)

### [html.elements.link.crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#html.elements.link.crossorigin)

### [html.elements.script.crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#html.elements.script.crossorigin)

### [html.elements.video.crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#html.elements.video.crossorigin)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#see_also)

--------------------------------------------------------------------------------------------------------

*   [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
    
*   [HTML attribute: `rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/crossorigin/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/crossorigin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fcrossorigin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fcrossorigin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fcrossorigin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fcrossorigin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F210eb1d964922bbae94774dc6676ce92056e0423%0A*+Document+last+modified%3A+2026-10-28T10%3A06%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")