*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#mdn-search)
    

`rel="prefetch"` HTML attribute value
=====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/306)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`prefetch`** keyword for the [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#rel)
 attribute of the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 element provides a hint to browsers that the user is likely to need the target resource for future navigations, and therefore the browser can likely improve the user experience by preemptively fetching and caching the resource. `<link rel="prefetch">` is used for same-site navigation resources, or for subresources used by same-site pages.

The result is kept in the HTTP cache on disk. Because of this it is useful for prefetching subresources, even if they are not used by the current page. You could also use it to prefetch the next document the user will likely visit on the site. However, as a result you need to be careful with headers — for example certain [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control)
 headers could block prefetching (for example `no-cache` or `no-store`).

**Note:** Because of such limitations, you are advised to use the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
 for document prefetches instead, where it is supported.

`<link rel="prefetch">` is functionally equivalent to a [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch "fetch()")
 call with a `priority: "low"` option set on it, except that the former will generally have an even lower priority, and it will have a [`Sec-Purpose: prefetch`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Purpose)
 header set on the request. Note that in general browsers will give prefetch resources a lower priority than preload ones (e.g., requested via [`<link rel="preload">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)
) — the current page is more important than the next.

The fetch request for a `prefetch` operation results in an HTTP request that includes the HTTP header [`Sec-Purpose: prefetch`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Purpose)
. A server might use this header to change the cache timeouts for the resources, or perform other special handling. The request will also include the [`Sec-Fetch-Dest`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Dest)
 header with the value set to `empty`.

The [`Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept)
 header in the request will match the value used for normal navigation requests. This allows the browser to find the matching cached resources following navigation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#examples)

---------------------------------------------------------------------------------------------------------

### [Basic prefetch](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#basic_prefetch)

### [Navigation and subresource prefetches](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#navigation_and_subresource_prefetches)

Prefetching can be used to fetch both HTML and sub-resources for a possible next navigation. A common use case is to have a website landing page that fetches more "heavy-weight" resources used by the rest of the site.

### [The effects of cache partitioning](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#the_effects_of_cache_partitioning)

Many browsers now implement some form of [cache partitioning](https://developer.chrome.com/blog/http-cache-partitioning "External link (opens in new tab)")
, which makes `<link rel="prefetch">` useless for resources intended for use by different top-level sites. This includes the main document when navigating cross-site. So, for example, the following prefetch:

Would not be accessible from `https://aggregator.example/`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# link-type-prefetch](https://html.spec.whatwg.org/multipage/links.html#link-type-prefetch) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch#see_also)

---------------------------------------------------------------------------------------------------------

*   [Speculative loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Speculative_loading)
     for a comparison of `<link rel="prefetch">` and other similar performance improvement features.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/rel/prefetch/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/rel/prefetch (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fprefetch&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fprefetch%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fprefetch%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fprefetch%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf5017c389132af39b50106cf1763fa7106e87b4%0A*+Document+last+modified%3A+2026-04-22T15%3A05%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")