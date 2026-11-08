*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#mdn-search)
    

`rel` HTML attribute
====================

The **`rel`** attribute defines the relationship between a linked resource and the current document. Valid on [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, and [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, the supported values depend on the element on which the attribute is found.

The type of relationships is given by the value of the `rel` attribute, which, if present, must have a value that is an unordered set of unique space-separated keywords. Differently from a `class` name, which does not express semantics, the `rel` attribute must express tokens that are semantically valid for both machines and humans. The current registries for the possible values of the `rel` attribute are the [IANA link relation registry](https://www.iana.org/assignments/link-relations "External link (opens in new tab)")
, the [HTML Living Standard](https://html.spec.whatwg.org/multipage/links.html#linkTypes "External link (opens in new tab)")
, and the freely-editable [existing-rel-values page](https://microformats.org/wiki/existing-rel-values "External link (opens in new tab)")
 in the microformats wiki, [as suggested](https://html.spec.whatwg.org/multipage/links.html#other-link-types "External link (opens in new tab)")
 by the Living Standard. If a `rel` attribute not present in one of the three sources above is used some HTML validators (such as the [W3C Markup Validation Service](https://validator.w3.org/ "External link (opens in new tab)")
) will generate a warning.

The following table lists some of the most important existing keywords. Every keyword within a space-separated value should be unique within that value.

| `rel` value | Description | [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link) | [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)<br> and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area) | [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form) |
| --- | --- | --- | --- | --- |
| [`alternate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#alternate) | Alternate representations of the current document. | Link | Link | Not allowed |
| [`author`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#author) | Author of the current document or article. | Link | Link | Not allowed |
| [`bookmark`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#bookmark) | Permalink for the nearest ancestor section. | Not allowed | Link | Not allowed |
| [`canonical`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#canonical) | Preferred URL for the current document. | Link | Not allowed | Not allowed |
| [`compression-dictionary`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/compression-dictionary) | Link to a [compression dictionary](https://developer.mozilla.org/en-US/docs/Glossary/Compression_dictionary_transport)<br> that can be used to compress future downloads for resources on this site. | Link | Not allowed | Not allowed |
| [`dns-prefetch`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/dns-prefetch) | Tells the browser to preemptively perform DNS resolution for the target resource's origin. | External Resource | Not allowed | Not allowed |
| [`external`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#external) | The referenced document is not part of the same site as the current document. | Not allowed | Annotation | Annotation |
| [`expect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#expect) | When used with [`blocking="render"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#blocking)<br>, allows the page to be [render-blocked](https://developer.mozilla.org/en-US/docs/Glossary/Render_blocking)<br> until the essential parts of the document are parsed so it will render consistently. | Link | Not allowed | Not allowed |
| [`help`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#help) | Link to context-sensitive help. | Link | Link | Link |
| [`icon`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#icon) | An icon representing the current document. | External Resource | Not allowed | Not allowed |
| [`license`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#license) | Indicates that the main content of the current document is covered by the copyright license described by the referenced document. | Link | Link | Link |
| [`manifest`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/manifest) | Web app manifest. | Link | Not allowed | Not allowed |
| [`me`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/me) | Indicates that the current document represents the person who owns the linked content. | Link | Link | Not allowed |
| [`modulepreload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload) | Tells to browser to preemptively fetch the script and store it in the document's module map for later evaluation. Optionally, the module's dependencies can be fetched as well. | External Resource | Not allowed | Not allowed |
| [`next`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#next) | Indicates that the current document is a part of a series and that the next document in the series is the referenced document. | Link | Link | Link |
| [`nofollow`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#nofollow) | Indicates that the current document's original author or publisher does not endorse the referenced document. | Not allowed | Annotation | Annotation |
| [`noopener`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener) | Creates a top-level browsing context that is not an auxiliary browsing context if the hyperlink would create either of those, to begin with (i.e., has an appropriate `target` attribute value). | Not allowed | Annotation | Annotation |
| [`noreferrer`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noreferrer) | No `Referer` header will be included. Additionally, has the same effect as `noopener`. | Not allowed | Annotation | Annotation |
| [`opener`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#opener) | Creates an auxiliary browsing context if the hyperlink would otherwise create a top-level browsing context that is not an auxiliary browsing context (i.e., has `"_blank"` as `target` attribute value). | Not allowed | Annotation | Annotation |
| [`pingback`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#pingback) | Gives the address of the pingback server that handles pingbacks to the current document. | External Resource | Not allowed | Not allowed |
| [`preconnect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preconnect) | Specifies that the user agent should preemptively connect to the target resource's origin. | External Resource | Not allowed | Not allowed |
| [`prefetch`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch) | Specifies that the user agent should preemptively fetch and cache the target resource as it is likely to be required for a followup navigation. | External Resource | Not allowed | Not allowed |
| [`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload) | Specifies that the user agent must preemptively fetch and cache the target resource for current navigation according to the potential destination given by the [`as`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#as)<br> attribute (and the priority associated with the corresponding destination). | External Resource | Not allowed | Not allowed |
| [`prerender`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prerender) | Specifies that the user agent should preemptively fetch the target resource and process it in a way that helps deliver a faster response in the future. This feature is superseded by the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)<br>. | External Resource | Not allowed | Not allowed |
| [`prev`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#prev) | Indicates that the current document is a part of a series and that the previous document in the series is the referenced document. | Link | Link | Link |
| [`privacy-policy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#privacy-policy) | Gives a link to information about the data collection and usage practices that apply to the current document. | Link | Link | Not allowed |
| [`search`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#search) | Gives a link to a resource that can be used to search through the current document and its related pages. | Link | Link | Link |
| [`stylesheet`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#stylesheet) | Imports a style sheet. | External Resource | Not allowed | Not allowed |
| [`tag`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#tag) | Gives a tag (identified by the given address) that applies to the current document. | Not allowed | Link | Not allowed |
| [`terms-of-service`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#terms-of-service) | Link to the agreement, or terms of service, between the document's provider and users who wish to use the document. | Link | Link | Not allowed |

The `rel` attribute is relevant to the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, and [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 elements, but some values only relevant to a subset of those elements. Like all HTML keyword attribute values, these values are case-insensitive.

The `rel` attribute has no default value. If the attribute is omitted or if none of the values in the attribute are supported, then the document has no particular relationship with the destination resource other than there being a hyperlink between the two. In this case, on [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 and [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, if the `rel` attribute is absent, has no keywords, or if not one or more of the space-separated keywords above, then the element does not create any links. [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 will still create links, but without a defined relationship.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#value)

------------------------------------------------------------------------------------------

[`alternate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#alternate)

Indicates an alternate representation of the current document. Valid for [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, the meaning depends on the values of the other attributes.

*   With the [`stylesheet`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#stylesheet)
     keyword on a `<link>`, it creates an [alternate stylesheet](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet)
    .
    
*   With an [`hreflang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#hreflang)
     attribute that differs from the document language, it indicates a translation.
    
*   With the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#type)
     attribute value of `"application/rss+xml"` or `"application/atom+xml"`, it creates a hyperlink referencing a syndication feed.
    
*   Otherwise, it creates a hyperlink referencing an alternate representation of the current document, whose nature is given by the [`hreflang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#hreflang)
     and [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#type)
     attributes.
    
    *   If `hreflang` is given alongside `alternate`, and the value of `hreflang` is different from the current document's language, it indicates that the referenced document is a translation.
    *   If `type` is given alongside `alternate`, it indicates that the referenced document is an alternative format (such as a PDF).
    *   The `hreflang` and `type` attributes may both be given alongside `alternate`.
    

[`author`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#author)

Indicates the referenced document provides further information about the author of the current document or article. Relevant for [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 elements.

With [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, it indicates the linked document (or `mailto:`) provides information about the author of the nearest [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 ancestor if there is one, otherwise the entire document.

With [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, it represents the author of the entire document.

**Note:** For historical reasons, the obsolete attribute value `rev="made"` is treated as `rel="author"`.

[`bookmark`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#bookmark)

Relevant as the `rel` attribute value for the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 elements. Gives a permalink for the nearest ancestor [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 element, if there is one. If there is no ancestor `<article>` element, gives a permalink for the section the linking element is most closely associated with.

[`canonical`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#canonical)

Valid for [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, it defines the preferred URL for the current document, which helps search engines reduce duplicate content.

[`compression-dictionary`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#compression-dictionary)

Valid for [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, it defines a [compression dictionary](https://developer.mozilla.org/en-US/docs/Glossary/Compression_dictionary_transport)
 that can be used to compress future downloads for resources on this site so the download sizes of those resources are smaller than standard compression.

[`dns-prefetch`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#dns-prefetch)

Relevant for the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 element both in the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 and [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
, it tells the browser to preemptively perform DNS resolution for the target resource's origin. Useful for resources the user will likely need, it helps reduce latency and thereby improves performance when the user does access the resources as the browser preemptively performed DNS resolution for the origin of the specified resource. See [dns-prefetch](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/dns-prefetch)
 described in [resource hints](https://w3c.github.io/resource-hints/ "External link (opens in new tab)")
.

[`external`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#external)

Relevant to [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, it indicates the referenced document is not part of the current site. This can be used with attribute selectors to style external links in a way that indicates to the user that they will be leaving the current site.

[`expect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#expect)

Allows the page to be [render-blocked](https://developer.mozilla.org/en-US/docs/Glossary/Render_blocking)
 until the essential parts of the document are parsed so it will render consistently. Note that render-blocking occurs only when supplemented with the [`blocking="render"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#blocking)
 attribute.

**Note:** See [Stabilizing page state to make cross-document transitions consistent](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#stabilizing_page_state_to_make_cross-document_transitions_consistent)
 for more information on its use.

[`help`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#help)

Relevant to [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, the `help` keyword indicates that the linked to content provides context-sensitive help, providing information for the parent of the element defining the hyperlink, and its children. When used within `<link>`, the help is for the whole document. When included with [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 and supported, the default [`cursor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)
 will be `help` instead of `pointer`.

[`icon`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#icon)

Valid with [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, the linked resource represents the icon, a resource for representing the page in the user interface, for the current document.

The most common use for the `icon` value is the favicon:

If there are multiple `<link rel="icon">`s, the browser uses their [`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#media)
, [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#type)
, and [`sizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#sizes)
 attributes to select the most appropriate icon. If several icons are equally appropriate, the last one is used. If the most appropriate icon is later found to be inappropriate, for example because it uses an unsupported format, the browser proceeds to the next-most appropriate, and so on.

**Note:** The [`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)
 attribute is not supported for `rel="icon"` in Chromium-based browsers. See the [open Chromium issue](https://crbug.com/1121645 "External link (opens in new tab)")
.

**Note:** Apple's iOS does not use this link type, nor the [`sizes`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#sizes)
 attribute, like others mobile browsers do, to select a webpage icon for Web Clip or a start-up placeholder. Instead it uses the non-standard [`apple-touch-icon`](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html#//apple_ref/doc/uid/TP40002051-CH3-SW4 "External link (opens in new tab)")
 and [`apple-touch-startup-image`](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html#//apple_ref/doc/uid/TP40002051-CH3-SW6 "External link (opens in new tab)")
 respectively.

**Note:** The `shortcut` link type is often seen before `icon`, but this link type is non-conforming, ignored and **web authors must not use it anymore**.

[`license`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#license)

Valid on the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 elements, the `license` value indicates that the hyperlink leads to a document describing the licensing information; that the main content of the current document is covered by the copyright license described by the referenced document. If not inside the [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
 element, the standard doesn't distinguish between a hyperlink applying to a specific part of the document or to the document as a whole. Only the data on the page can indicate this.

**Note:** Although recognized, the synonym `copyright` is incorrect and must be avoided.

[`manifest`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#manifest)

[Web app manifest](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest)
. Requires the use of the CORS protocol for cross-origin fetching.

[`modulepreload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#modulepreload)

Useful for improved performance, and relevant to the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 anywhere in the document, setting `rel="modulepreload"` tells the browser to preemptively fetch the script (and dependencies) and store it in the document's module map for later evaluation. `modulepreload` links can ensure network fetching is done with the module ready (but not evaluated) in the module map before it is necessarily needed. See also [`modulepreload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload)
.

[`next`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#next)

Relevant to [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, the `next` values indicates that the current document is a part of a series, and that the next document in the series is the referenced document. When included in a `<link>`, browsers may assume that document will be fetched next, and treat it as a resource hint.

[`nofollow`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#nofollow)

Relevant to [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, the `nofollow` keyword tells search engine spiders to ignore the link relationship. The nofollow relationship may indicate the current document's owner does not endorse the referenced document. It is often included by Search Engine Optimizers pretending their link farms are not spam pages.

[`noopener`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#noopener)

Relevant to [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, creates a top-level browsing context that is not an auxiliary browsing context if the hyperlink would create either of those to begin with (i.e., has an appropriate `target` attribute value). In other words, it makes the link behave as if [`window.opener`](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)
 were null and `target="_parent"` were set.

This is the opposite of [`opener`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#opener)
.

[`noreferrer`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#noreferrer)

Relevant to [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, including this value makes the referrer unknown (no `Referer` header will be included), and creates a top-level browsing context as if `noopener` were also set.

[`opener`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#opener)

Creates an auxiliary browsing context if the hyperlink would otherwise create a top-level browsing context that is not an auxiliary browsing context (i.e., has `"_blank"` as `target` attribute value). Effectively, the opposite of [noopener](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#noopener)
.

[`pingback`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#pingback)

Gives the address of the pingback server that handles pingbacks to the current document. See the [Pingback specification](https://www.hixie.ch/specs/pingback/pingback "External link (opens in new tab)")
.

[`preconnect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#preconnect)

Provides a hint to the browser suggesting that it open a connection to the linked website in advance, without disclosing any private information or downloading any content, so that when the link is followed the linked content can be fetched more quickly.

[`prefetch`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#prefetch)

Specifies that the user agent should preemptively fetch and cache the target resource as it is likely to be required for a followup navigation. See [prefetch](https://developer.mozilla.org/en-US/docs/Glossary/Prefetch)
 for more information.

[`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#preload)

Specifies that the user agent must preemptively fetch and cache the target resource for current navigation according to the potential destination given by the [`as`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#as)
 attribute (and the priority associated with the corresponding destination). See the page for the [`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)
 value.

[`prerender`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#prerender)

Specifies that the user agent should preemptively fetch the target resource and process it in a way that helps deliver a faster response in the future, for example by fetching its subresources or performing some rendering. This feature is superseded by the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
.

[`prev`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#prev)

Similar to the [`next`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#next)
 keyword, relevant to [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, the `prev` values indicates that the current document is a part of a series, and that the link references a previous document in the series is the referenced document.

Note: The synonym `previous` is incorrect and should not be used.

[`privacy-policy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#privacy-policy)

Valid for [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, and [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 elements, the `privacy-policy` value indicates that the referenced document is the Privacy Policy which describes the data collection and usage practices of the current document.

[`search`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#search)

Relevant to [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 elements, the `search` keywords indicates that the hyperlink references a document whose interface is specially designed for searching in the current document, site, and related resources, providing a link to a resource that can be used to search.

If the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#type)
 attribute is set to `application/opensearchdescription+xml` the resource is an [OpenSearch](https://developer.mozilla.org/en-US/docs/Web/XML/Guides/OpenSearch)
 plugin that can be easily added to the interface of Firefox.

[`stylesheet`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#stylesheet)

Valid for the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 element, it imports an external resource to be used as a stylesheet. The [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#type)
 attribute is not needed if it's a `text/css` stylesheet, as that is the default value. If it's not a stylesheet of type `text/css` it is best to declare the type.

While this attribute defines the link as being a stylesheet, the interaction with other attributes and other key terms within the rel value impact whether the stylesheet is downloaded and/or used.

When used with the [`alternate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#alternate)
 keyword, it defines an alternative style sheet. In this case, include a non-empty [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#title)
.

The external stylesheet will not be used or even downloaded if the media does not match the value of the [`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#media)
 attribute.

Requires the use of the CORS protocol for cross-origin fetching.

[`tag`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#tag)

Valid for the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 elements, it gives a tag (identified by the given address) that applies to the current document. The tag value denotes that the link refers to a document describing a tag applying to the document on which it is located. This link type is not meant for tags within a tag cloud, as those tags apply to a group of pages, whereas the `tag` value of the `rel` attribute is for a single document.

[`terms-of-service`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#terms-of-service)

Valid for [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, and [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 elements, the `terms-of-service` value indicates that the referenced document is the Terms of Service that describes the agreements between the current document's provider and users who wish to use the document provided.

### [Non-standard values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#non-standard_values)

[`apple-touch-icon`](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html#//apple_ref/doc/uid/TP40002051-CH3-SW4 "External link (opens in new tab)")

Specifies the icon for a web application on an iOS device.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# linkTypes](https://html.spec.whatwg.org/multipage/links.html#linkTypes) |
| [HTML  <br>\# attr-hyperlink-rel](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-rel) |
| [HTML  <br>\# attr-form-rel](https://html.spec.whatwg.org/multipage/forms.html#attr-form-rel) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

### [html.elements.link.rel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#html.elements.link.rel)

### [html.elements.a.rel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#html.elements.a.rel)

### [html.elements.area.rel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#html.elements.area.rel)

### [html.elements.form.rel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#html.elements.form.rel)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#see_also)

------------------------------------------------------------------------------------------------

*   [`HTMLLinkElement.relList`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLinkElement/relList)
    
*   [`HTMLAnchorElement.relList`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement/relList)
    
*   [`HTMLAreaElement.relList`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAreaElement/relList)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/rel/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/rel (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf7ff749b987d530e9a6c07f23ac66f94d968e57%0A*+Document+last+modified%3A+2026-10-07T02%3A00%3A05.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")