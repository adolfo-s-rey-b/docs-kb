*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#mdn-search)
    

Using microformats in HTML
==========================

[_Microformats_](https://microformats.org/wiki/Main_Page "External link (opens in new tab)")
 are standards used to embed semantics and structured data in HTML, and provide an API to be used by social web applications, search engines, aggregators, and other tools. These minimal patterns of HTML are used for marking up entities that range from fundamental to domain-specific information, such as people, organizations, events, and locations.

*   To create a microformats object, `h-*` class names are used in the class attribute.
*   To add a property to an object, the `p-*`, `u-*`, `dt-*`, `e-*` class names are used on one of the object's descendants.

Microformats use supporting vocabularies to describe objects and name-value pairs to assign values to their properties. The properties are carried in class attributes that can be added to any HTML element, while the data values re-use HTML element content and semantic attributes.

Microformats2 (sometimes referred to as mf2) is an update to microformats that provides a method of annotating HTML structured syntax and vocabularies than previous approaches of using RDFa and microdata. These previous approaches require learning new attributes.

There are [open source parsing libraries for most languages](https://microformats.org/wiki/microformats2#Parsers "External link (opens in new tab)")
 for microformats2.

[How Microformats Work](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#how_microformats_work)

---------------------------------------------------------------------------------------------------------------------

An author of a webpage can add microformats to their HTML. For example if they wanted to identify themselves they could use an [h-card](https://microformats.org/wiki/h-card "External link (opens in new tab)")
 such as:

### [HTML Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#html_example)

When a parser encounters this data, it will know that this page contains a "card" which describes a person or organization named `Alice Blogger` with a URL of `https://alice.example.com/`. The parser makes this data available via APIs that can be used for different applications. For example, an application could scan a page for a h-card to use as profile information for someone who has signed up to a service.

As in this example, some markup patterns require only a single microformat root class name, which parsers use to find a few generic properties such as `name`, `url`, `photo`.

[Microformats Use Cases](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#microformats_use_cases)

-----------------------------------------------------------------------------------------------------------------------

Microformats have numerous use cases. First, the [Webmention standard](https://webmention.net/draft/ "External link (opens in new tab)")
 uses microformats to provide a way in which messages and comments can be sent from one site to another. The Webmention specification defines specific attributes that sites may publish and consume to create a rich, interoperable way of publishing messages and comments. Microformats can also be used with Webmentions to enable sending social reactions such as likes, reposts, and bookmarks from one site to another.

Microformats also enable easy syndication across sites. An aggregator could parse a page with published microformats to look for information such as a post title, a post body, and the author of a post. This aggregator could then use the semantic information gathered to render a result on their site. For instance, news aggregators and community posting boards could facilitate submissions and use microformats to exact relevant content from a page. Further, a website could use microformats to send crafted requests to third-parties to publish content, such as social networks.

All major search engines support reading and interpreting microformats. Search engines benefit greatly from direct access to this structured data because it allows them to understand the information on web pages. With this information, search engines can provide more relevant results to users. Some search engines may render special snippets such as star ratings on a search result page based on the data provided in microformats.

In addition to being machine-readable, microformats are designed to be easily read by humans. This approach makes it easy for people to understand and maintain microformats data.

[Microformats Prefixes](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#microformats_prefixes)

---------------------------------------------------------------------------------------------------------------------

All microformats consist of a root, and a collection of properties. Properties are all optional and potentially multivalued - applications needing a singular value may use the first instance of a property. Hierarchical data is represented with nested microformats, typically as property values themselves.

All microformats class names use prefixes. Prefixes are **syntax independent of vocabularies**, which are developed separately.

*   **"h-\*" for root class names**, e.g., "h-card", "h-entry", "h-feed", and many more. These top-level root classes usually indicate a type and corresponding expected vocabulary of properties. For example:
    
    *   [h-card](https://microformats.org/wiki/h-card "External link (opens in new tab)")
         describes a person or organization
    *   [h-entry](https://microformats.org/wiki/h-entry "External link (opens in new tab)")
         describes episodic or date stamped online content like a blog post
    *   [h-feed](https://microformats.org/wiki/h-feed "External link (opens in new tab)")
         describes a stream or feed of posts
    *   You can find many more [vocabularies on the microformats2 wiki.](https://microformats.org/wiki/microformats2#v2_vocabularies "External link (opens in new tab)")
        
*   **"p-\*" for plain (text) properties**, e.g., "p-name", "p-summary"
    
    *   Generic plain text parsing, element text in general. On certain HTML elements, use special attributes first, e.g., img/alt, abbr/title.
*   **"u-\*" for URL properties**, e.g., "u-url", "u-photo", "u-logo"
    
    *   Special parsing: element attributes a/href, img/src, object/data etc. attributes over element contents.
*   **"dt-\*" for datetime properties**, e.g., "dt-start", "dt-end", "dt-bday"
    
    *   Special parsing: time element datetime attribute, [value-class-pattern](https://microformats.org/wiki/value-class-pattern "External link (opens in new tab)")
         and separate date time value parsing for readability.
*   **"e-\*" for element tree properties** where the entire contained element hierarchy is the value, e.g., "e-content". The "e-" prefix can also be mnemonically remembered as "element tree", "embedded markup", or "encapsulated markup".
    

[Some microformats examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#some_microformats_examples)

-------------------------------------------------------------------------------------------------------------------------------

### [h-card](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#h-card)

The [h-card](https://microformats.org/wiki/h-card "External link (opens in new tab)")
 microformat represents a person or organization.

The value of each property is defined in HTML using the class property any element can carry

#### Example h-card

| Property | Description |
| --- | --- |
| **`p-name`** | The full/formatted name of the person or organization. |
| **`u-email`** | email address |
| **`u-photo`** | a photo of the person or organization |
| **`u-url`** | home page or other URL representing the person or organization |
| **`u-uid`** | universally unique identifier, preferably canonical URL |
| **`p-street-address`** | street number + name |
| **`p-locality`** | city/town/village |
| **`p-country-name`** | country name |

#### Nested h-card example

Parsed JSON:

In this example, a h-card is specified for both a person and the organization they represent. The person's affiliation with the linked organization is specified using the p-org property.

Note: the nested h-card has implied 'name' and 'url' properties, just like any other root-class-name-only h-card on an `<a href>` would.

### [h-entry](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#h-entry)

The [h-entry](https://microformats.org/wiki/h-entry "External link (opens in new tab)")
 microformat represents episodic or datestamped content on the web. h-entry is often used with content intended to be syndicated, e.g., blog posts and short notes.

Example h-entry as a blog post:

#### Properties

| Property | Description |
| --- | --- |
| **`p-name`** | entry name/title |
| **`p-author`** | who wrote the entry, optionally embedded h-card |
| **`dt-published`** | when the entry was published |
| **`p-summary`** | short entry summary |
| **`e-content`** | full content of the entry |

#### Parsed reply h-entry example

### [h-feed](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#h-feed)

The [h-feed](https://microformats.org/wiki/h-feed "External link (opens in new tab)")
 is a stream or feed of [h-entry](https://microformats.org/wiki/h-entry "External link (opens in new tab)")
 posts, like complete posts on a home page or archive pages, or summaries or other brief lists of posts.

#### Example h-feed

#### Properties

| Property | Description |
| --- | --- |
| **`p-name`** | name of the feed |
| **`p-author`** | author of the feed, optionally embed an h-card |

#### Children

|     |     |
| --- | --- |
| **Nested h-entry** |     |
| objects representing the items of the feed |     |

### [h-event](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#h-event)

The `h-event` is for events on the web. h-event is often used with both event listings and individual event pages.

#### Properties

| Property | Description |
| --- | --- |
| **`p-name`** | event name (or title) |
| **`p-summary`** | short summary of the event |
| **`dt-start`** | datetime the event starts |
| **`dt-end`** | datetime the event ends |
| **`p-location`** | where the event takes place, optionally embedded h-card |

#### Parsed h-event Example

[Microformats rel property examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#microformats_rel_property_examples)

-----------------------------------------------------------------------------------------------------------------------------------------------

There are some microformats that are applied to a page by using a special `rel=` property. These microformats describe a relation between a current document and a linked document. For a full list of these, see the [rel property](https://microformats.org/wiki/rel-values "External link (opens in new tab)")
 on the microformats wiki.

### [rel=author](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#relauthor)

This attribute states that the linked document represents the author of the current page.

### [rel=license](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#rellicense)

This attribute states that the linked document contains the license under which the current page is published.

### [rel=nofollow](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#relnofollow)

This attribute states that the linked document should not be given any weight by search engine ranking algorithms that may derive from the current page. This is useful to prevent link graph algorithms from weighing a page higher than it otherwise would after seeing a link to a document.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------

Supported in all browsers' support for the class attribute and its DOM API.

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats#see_also)

-------------------------------------------------------------------------------------------

*   [class attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)
    
*   [Microformat](https://en.wikipedia.org/wiki/Microformat "External link (opens in new tab)")
     on Wikipedia
*   [Microformats official website](https://microformats.org/wiki/Main_Page "External link (opens in new tab)")
    
*   [Search engines support](https://microformats.org/wiki/search_engines "External link (opens in new tab)")
     on Microformats official website
*   [Microformats on IndieWebCamp](https://indieweb.org/microformats "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 9, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microformats/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/guides/microformats/index.md?plain=1 "Folder: en-us/web/html/guides/microformats (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FMicroformats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fguides%2Fmicroformats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FMicroformats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fguides%2Fmicroformats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0754cd805a8e010d2e3a2a065f634a3bcf358252%0A*+Document+last+modified%3A+2025-07-09T21%3A49%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")