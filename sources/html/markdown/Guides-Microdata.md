*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#mdn-search)
    

Using microdata in HTML
=======================

Microdata is part of the [WHATWG](https://developer.mozilla.org/en-US/docs/Glossary/WHATWG)
 HTML Standard and is used to nest metadata within existing content on web pages. Search engines and web crawlers can extract and process microdata from a web page and use it to provide a richer browsing experience for users. Search engines benefit greatly from direct access to this structured data because it allows search engines to understand the information on web pages and provide more relevant results to users. Microdata uses a supporting vocabulary to describe an item and name-value pairs to assign values to its properties. Microdata is an attempt to provide a declarative way of annotating HTML elements with machine-readable tags than the similar approaches of using RDFa and classic microformats.

At a high level, microdata consists of a group of name-value pairs. The groups are called items, and each name-value pair is a property. Items and properties are represented by regular elements.

*   To create an item, the `itemscope` attribute is used.
*   To add a property to an item, the `itemprop` attribute is used on one of the item's descendants.

[Vocabularies](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#vocabularies)

------------------------------------------------------------------------------------------------

Google and other major search engines support the [Schema.org](https://schema.org/ "External link (opens in new tab)")
 vocabulary for structured data. This vocabulary defines a standard set of type names and property names, for example, [Schema.org Music Event](https://schema.org/MusicEvent "External link (opens in new tab)")
 indicates a concert performance, with [`startDate`](https://schema.org/startDate "External link (opens in new tab)")
 and [`location`](https://schema.org/location "External link (opens in new tab)")
 properties to specify the concert's key details. In this case, [Schema.org Music Event](https://schema.org/MusicEvent "External link (opens in new tab)")
 would be the URL used by `itemtype` and `startDate` and location would be `itemprop`'s that [Schema.org Music Event](https://schema.org/MusicEvent "External link (opens in new tab)")
 defines.

**Note:** More about itemtype attributes can be found at [https://schema.org/Thing](https://schema.org/Thing "External link (opens in new tab)")
.

Microdata vocabularies provide the semantics or meaning of an _`Item`_. Web developers can design a custom vocabulary or use vocabularies available on the web, such as the widely used [schema.org](https://schema.org/ "External link (opens in new tab)")
 vocabulary. A collection of commonly used markup vocabularies are provided by Schema.org.

Commonly used vocabularies:

*   Creative works: [CreativeWork](https://schema.org/CreativeWork "External link (opens in new tab)")
    , [Book](https://schema.org/Book "External link (opens in new tab)")
    , [Movie](https://schema.org/Movie "External link (opens in new tab)")
    , [MusicRecording](https://schema.org/MusicRecording "External link (opens in new tab)")
    , [Recipe](https://schema.org/Recipe "External link (opens in new tab)")
    , [TVSeries](https://schema.org/TVSeries "External link (opens in new tab)")
    
*   Embedded non-text objects: [AudioObject](https://schema.org/AudioObject "External link (opens in new tab)")
    , [ImageObject](https://schema.org/ImageObject "External link (opens in new tab)")
    , [VideoObject](https://schema.org/VideoObject "External link (opens in new tab)")
    
*   [`Event`](https://schema.org/Event "External link (opens in new tab)")
    
*   [Health and medical types](https://schema.org/docs/meddocs.html "External link (opens in new tab)")
    : Notes on the health and medical types under [MedicalEntity](https://schema.org/MedicalEntity "External link (opens in new tab)")
    
*   [`Organization`](https://schema.org/Organization "External link (opens in new tab)")
    
*   [`Person`](https://schema.org/Person "External link (opens in new tab)")
    
*   [`Place`](https://schema.org/Place "External link (opens in new tab)")
    , [LocalBusiness](https://schema.org/LocalBusiness "External link (opens in new tab)")
    , [Restaurant](https://schema.org/Restaurant "External link (opens in new tab)")
    
*   [`Product`](https://schema.org/Product "External link (opens in new tab)")
    , [Offer](https://schema.org/Offer "External link (opens in new tab)")
    , [AggregateOffer](https://schema.org/AggregateOffer "External link (opens in new tab)")
    
*   [`Review`](https://schema.org/Review "External link (opens in new tab)")
    , [AggregateRating](https://schema.org/AggregateRating "External link (opens in new tab)")
    
*   [`Action`](https://schema.org/Action "External link (opens in new tab)")
    
*   [`Thing`](https://schema.org/Thing "External link (opens in new tab)")
    
*   [`Intangible`](https://schema.org/Intangible "External link (opens in new tab)")
    

Major search engine operators like Google, Microsoft, and Yahoo! rely on the [schema.org](https://schema.org/ "External link (opens in new tab)")
 vocabulary to improve search results. For some purposes, an ad hoc vocabulary is adequate. For others, a vocabulary will need to be designed. Where possible, authors are encouraged to re-use existing vocabularies, as this makes content re-use easier.

[Localization](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#localization)

------------------------------------------------------------------------------------------------

In some cases, search engines covering specific regions may provide locally-specific extensions of microdata. For example, [Yandex](https://yandex.com/ "External link (opens in new tab)")
, a major search engine in Russia, supports microformats such as `hCard` (company contact information), `hRecipe` (food recipe), `hReview` (market reviews) and `hProduct` (product data) and provides its own format for the definition of the terms and encyclopedic articles. This extension was made to solve transliteration problems between the Cyrillic and Latin alphabets. Due to the implementation of additional marking parameters of Schema's vocabulary, the indexation of information in Russian-language web-pages became considerably more successful.

[Global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#global_attributes)

----------------------------------------------------------------------------------------------------------

[`itemid`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid)
 – The unique, global identifier of an item.

[`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
 – Used to add properties to an item. Every HTML element may have an `itemprop` attribute specified, where an `itemprop` consists of a name and value pair.

[`itemref`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref)
 – Properties that are not descendants of an element with the `itemscope` attribute can be associated with the item using an **itemref**. `itemref` provides a list of element ids (not `itemid`s) with additional properties elsewhere in the document.

[`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
 – The `itemscope` attribute (usually) works along with [`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)
 to specify that the HTML contained in a block is about a particular item. The `itemscope` attribute creates the _`Item`_ and defines the scope of the itemtype associated with it. The `itemtype` attribute is a valid URL of a vocabulary (such as [schema.org](https://schema.org/ "External link (opens in new tab)")
) that describes the item and its properties context.

[`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)
 – Specifies the URL of the vocabulary that will be used to define `itemprop`'s (item properties) in the data structure. The [`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
 attribute is used to set the scope of where in the data structure the vocabulary set by `itemtype` will be active.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#example)

--------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#html)

### [Structured data](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#structured_data)

|     |     |     |
| --- | --- | --- |
| itemscope | itemtype | SoftwareApplication (https://schema.org/SoftwareApplication) |     |
| itemprop | name | Angry Birds |
| itemprop | operatingSystem | ANDROID |
| itemprop | applicationCategory | SoftwareApplication (https://schema.org/SoftwareApplication) |
| itemscope | itemprop\[itemtype\] | aggregateRating \[AggregateRating\] |     |
| itemprop | ratingValue | 4.6 |
| itemprop | ratingCount | 8864 |
| itemscope | itemprop\[itemtype\] | offers \[Offer\] |     |
| itemprop | price | 1.00 |
| itemprop | priceCurrency | USD |

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#result)

**Note:** A handy tool for extracting and verifying microdata structures from HTML is the [Schema Markup Validator](https://validator.schema.org/ "External link (opens in new tab)")
. Try it on the HTML shown above.

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata#see_also)

----------------------------------------------------------------------------------------

*   [Global Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 27, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/guides/microdata/index.md?plain=1 "Folder: en-us/web/html/guides/microdata (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FMicrodata&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fguides%2Fmicrodata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FMicrodata%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fguides%2Fmicrodata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F057d13e47e8335a52d3c687cf27231527ef758c1%0A*+Document+last+modified%3A+2025-11-27T08%3A54%3A33.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")