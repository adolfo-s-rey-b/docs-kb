*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#mdn-search)
    

`<meta name="robots">` HTML attribute value
===========================================

The **`robots`** value for the [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
 attribute of the [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 element (often called a "robots tag") defines the crawl and indexing behavior that web [crawlers](https://developer.mozilla.org/en-US/docs/Glossary/Crawler)
 should use with the page. If specified, you define instructions for crawlers in the [`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)
 attribute of the `<meta>` element as a comma-separated list of one or more rules.

For example, to hint to crawlers that a page should be excluded from their search indexes, a `noindex` value can be used:

**Note:** Only cooperative robots follow these rules. A crawler still needs to access the resource to read headers and meta elements (see [X-Robots-Tag: Interaction with robots.txt](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Robots-Tag#interaction_with_robots.txt)
). If you want to prevent bandwidth consumption by crawlers, a restrictive [robots.txt](https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt)
 file is more effective than indexing rules as it blocks resources from being crawled entirely.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#usage_notes)

-----------------------------------------------------------------------------------------------------------------

A `<meta name="robots">` element can have the following additional attributes:

[`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)

The `content` attribute must be defined, and its value sets indexing and crawling behavior for cooperative search engine robots. Accepts one or more of the following keywords as a comma-separated list:

[`index`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#index)

Allows the robot to index the page. This is the default behavior. Used by all major crawlers.

[`noindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#noindex)

Requests the robot not to index the page. Used by all major crawlers.

[`follow`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#follow)

Allows the robot to follow links on the page. This is the default behavior. Used by all major crawlers.

[`nofollow`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#nofollow)

Requests the robot not to follow the links on the page. Used by all major crawlers.

[`all`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#all)

Equivalent to `index, follow`. Used by: [Google](https://developers.google.com/search/docs/crawling-indexing/special-tags?visit_id=637855965067987211-415685194&rd=1 "External link (opens in new tab)")
.

[`none`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#none)

Equivalent to `noindex, nofollow`. Used by: [Google](https://developers.google.com/search/docs/crawling-indexing/special-tags?visit_id=637855965074074862-574753619&rd=1 "External link (opens in new tab)")
.

[`noarchive`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#noarchive)

Requests that the search engine not cache the page content. Used by: [Google](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag "External link (opens in new tab)")
, [Yahoo](https://help.yahoo.com/kb/search-for-desktop/SLN2213.html "External link (opens in new tab)")
, [Bing](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240 "External link (opens in new tab)")
.

[`nosnippet`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#nosnippet)

Prevents displaying any description of the page in search engine results. Used by: [Google](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag "External link (opens in new tab)")
, [Bing](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240 "External link (opens in new tab)")
.

[`noimageindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#noimageindex)

Requests that this page not appear as the referring page of an indexed image. Used by: [Google](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag "External link (opens in new tab)")
.

[`nocache`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#nocache)

Synonym of `noarchive`. Used by: [Bing](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240 "External link (opens in new tab)")
.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#description)

-----------------------------------------------------------------------------------------------------------------

There are several important considerations to note when setting a `robots` meta value:

*   Only cooperative robots follow these rules. They won't prevent malicious actors like email harvesters from ignoring the directives.
*   If defined in a `<meta>` tag, robots still need to access the page to read these rules. To reduce bandwidth, consider using a [robots.txt file](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/Robots_txt)
     instead.
*   The `<meta name="robots">` tag and `robots.txt` serve different roles: `robots.txt` controls crawling, while the `robots` meta tag influences indexing and other behavior.
*   A page blocked by `robots.txt` may still be indexed if linked from other sources.
*   The `noindex` directive will only take effect after the robot revisits the page, so ensure `robots.txt` doesn't prevent this.
*   Some values, such as `index` vs. `noindex` or `follow` vs. `nofollow`, are mutually exclusive. Behavior is undefined when conflicting values are used.
*   Robots like Google, Yahoo, and Bing also support these directives in the HTTP header [`X-Robots-Tag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Robots-Tag)
    , which is useful for non-HTML content such as PDFs or images.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#examples)

-----------------------------------------------------------------------------------------------------------

### [Using a robots keyword](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#using_a_robots_keyword)

The following example uses `nofollow` to request that a crawler doesn't follow links on a page and `noindex` to request that the page is excluded from indexing:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#specifications)

-----------------------------------------------------------------------------------------------------------------------

While not part of any specification, it is a de-facto standard method for communicating with search bots, web crawlers, and similar user agents.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

This feature is intended for crawlers to observe, so "browser" compatibility doesn't apply.

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`X-Robots-Tag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Robots-Tag)
     HTTP header
*   [robots.txt configuration](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/Robots_txt)
     guide
*   [robots.txt](https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt)
     glossary entry
*   [Search engine](https://developer.mozilla.org/en-US/docs/Glossary/Search_engine)
     glossary entry
*   [RFC 9309: Robots Exclusion Protocol](https://datatracker.ietf.org/doc/html/rfc9309 "External link (opens in new tab)")
    
*   [WHATWG Wiki MetaExtensions page](https://wiki.whatwg.org/wiki/MetaExtensions "External link (opens in new tab)")
    
*   [Using the robots meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#robotsmeta "External link (opens in new tab)")
     on developers.google.com

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/robots/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meta/name/robots/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meta/name/robots (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Frobots&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Frobots%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Frobots%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Frobots%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc53bfa01f3bf436d486f4032c16f592855a2af2c%0A*+Document+last+modified%3A+2026-05-04T02%3A41%3A10.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")