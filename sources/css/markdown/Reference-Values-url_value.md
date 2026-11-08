*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value#mdn-search)
    

`<url>` CSS type
================

The **`<url>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 is a pointer to a resource.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value#syntax)

---------------------------------------------------------------------------------------------

<url> = url()

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value#values)

The value may be an absolute or relative URL.

[`<url()>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_function)

The `url()` function accepts a URL, which may be written as a quoted string or as an unquoted URL token.

**Note:** The [CSS values and units module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
 also introduces the `src()` function as a `<url>` value. Currently, no browser supports this feature.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value#description)

-------------------------------------------------------------------------------------------------------

The `<url>` data type, written with the [`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_function)
 function, represents a `URL`, which is a pointer to an internal or external resource. The resource can be an image, a video, a CSS file, a font file, an SVG feature, etc. The URL may be absolute or relative.

### [External resources and CORS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value#external_resources_and_cors)

The ability to import external resources via the `<url>` value is implementation-defined and often restricted for security reasons.

Depending on the CSS property on which a `<url>` referencing external resources is applied, the resource may be subject to [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
 restrictions.

Some CSS properties, including [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
, [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
, as well as [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 and a few others when referring to [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
 image elements, may require successful CORS validation when they cause external, cross-origin resources to be fetched in CORS mode. If CORS validation fails, the resource may be blocked and therefore not used for rendering.

Note that the `<url>` value type does not enforce CORS validation itself, but individual CSS properties do.

When opening an HTML file directly with `file://`, resources may fail because CORS rules apply locally. Modern browsers treat `file://` as a unique origin, meaning cross-file resources can get blocked. In this case, an [HTTP server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/set_up_a_local_testing_server)
 may be hosted to avoid CORS errors. The security behavior of `file://` URLs also varies depending on the browser and the operating system's file permissions.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value#examples)

-------------------------------------------------------------------------------------------------

Relative URL

Absolute URL

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# url-value](https://drafts.csswg.org/css-values/#url-value) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value#see_also)

-------------------------------------------------------------------------------------------------

*   [`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/url_value/index.md?plain=1 "Folder: en-us/web/css/reference/values/url_value (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Furl_value&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Furl_value%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Furl_value%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Furl_value%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F91e08923c809ca8deded3e3294f49bbe1a4a00b3%0A*+Document+last+modified%3A+2026-09-10T06%3A51%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")