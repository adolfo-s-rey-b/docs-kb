*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#mdn-search)
    

`<meta name>` HTML attribute
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`name`** attribute of the [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 element provides metadata in name-value pairs. When a `<meta>` element has a `name` attribute, a [`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/content)
 attribute defines the corresponding value. The metadata is _document-level metadata_ that applies to the whole page.

For example, the following `<meta>` tag provides a `description` as metadata for a document:

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#value)

----------------------------------------------------------------------------------------------

### [Meta names defined in the HTML specification](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#meta_names_defined_in_the_html_specification)

The HTML specification defines the following set of standard metadata names:

[`application-name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#application-name)

Browsers may use this to identify the application running in the web page. It is different from the [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)
 element, which may contain an application (or website) name, but a `<title>` may add contextual information like a document name or a status. Individual pages shouldn't define their own, unique `application-name`. To provide translations, use multiple `<meta>` tags with the `lang` attribute for each language:

[`author`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#author)

The document author's name.

[`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme)

Specifies one or more color schemes with which the document is compatible. The browser will use this information in tandem with the user's browser or device settings to determine what colors to use for everything from background and foregrounds to form controls and scrollbars. The primary use for `<meta name="color-scheme">` is to indicate compatibility and order of preference for light and dark color modes.

[`description`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#description)

A short and accurate summary of the content of the page usually referred to as a "meta description". Search engines like Google use this metadata to adjust [the appearance of a webpage in search](https://developers.google.com/search/docs/appearance/snippet#meta-descriptions "External link (opens in new tab)")
 results.

[`generator`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#generator)

The identifier of the software that generated the page.

[`keywords`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#keywords)

Words relevant to the page's content separated by commas.

[`referrer`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer)

Controls the HTTP [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
 header of requests sent from the document.

[`theme-color`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color)

Indicates a suggested color that user agents should use to customize the display of the page or of the surrounding user interface. The [`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/content)
 attribute contains a valid CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
. The [`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#media)
 attribute with a valid media query list can be included to set the media that the theme color metadata applies to.

### [Meta names defined in other specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#meta_names_defined_in_other_specifications)

[`responsive-embedded-sizing`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/responsive-embedded-sizing)

Opts in an embedded document to sharing its size information with the parent page. Defined in the [CSS box sizing module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
.

[`text-scale`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale)

Enables opting the page in to having the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 root element's [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 scale in proportion to OS and browser-level text scale settings. Defined in the [CSS fonts module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
.

[`viewport`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport)

Gives hints about the initial size of the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
. Defined in the [CSS viewport module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport)
.

### [Meta names defined in the WHATWG MetaExtensions wiki](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#meta_names_defined_in_the_whatwg_metaextensions_wiki)

The [WHATWG Wiki MetaExtensions page](https://wiki.whatwg.org/wiki/MetaExtensions "External link (opens in new tab)")
 contains a large set of non-standard metadata names. Some of the names included are used quite commonly in practice, notably the following:

[`creator`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#creator)

The name of the creator of the document, such as an organization or institution. If there are more than one, several [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 elements should be used.

[`googlebot`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#googlebot)

A synonym of `robots`, is only followed by Googlebot (the indexing crawler for Google).

[`publisher`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#publisher)

The document publisher's name.

[`robots`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots)

A comma-separated list of values defining the crawl behavior that cooperative crawlers (or "robots") should use with the page.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# standard-metadata-names](https://html.spec.whatwg.org/multipage/semantics.html#standard-metadata-names) |
| [Referrer Policy  <br>\# referrer-policy-delivery-meta](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy-delivery-meta) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name#see_also)

----------------------------------------------------------------------------------------------------

*   [Metadata: the `<meta>` element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Webpage_metadata#metadata_the_meta_element)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meta/name/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meta/name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F04c41175b160dc00b1a1b8e4e13b2183d89fdf1a%0A*+Document+last+modified%3A+2026-07-17T07%3A28%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")