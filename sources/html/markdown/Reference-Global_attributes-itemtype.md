*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype#mdn-search)
    

`itemtype` HTML global attribute
================================

The [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 **`itemtype`** specifies the URL of the vocabulary that will be used to define `itemprop`'s (item properties) in the data structure.

[`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
 is used to set the scope of where in the data structure the vocabulary set by `itemtype` will be active.

Google and other major search engines support the [schema.org](https://schema.org/ "External link (opens in new tab)")
 vocabulary for structured data. This vocabulary defines a standard set of type names and property names. For example, `MusicEvent` indicates a concert performance, with [`startDate`](https://schema.org/startDate "External link (opens in new tab)")
 and [`location`](https://schema.org/location "External link (opens in new tab)")
 properties specifying the concert's key details. In this case, [`MusicEvent`](https://schema.org/MusicEvent "External link (opens in new tab)")
 would be the URL used by `itemtype`, with `startDate` and location as `itemprop`'s which [`MusicEvent`](https://schema.org/MusicEvent "External link (opens in new tab)")
 defines.

**Note:** More about `itemtype` attributes can be found at [https://schema.org/Thing](https://schema.org/Thing "External link (opens in new tab)")

*   The **itemtype** attribute must have a value that is an unordered set of unique tokens which are case-sensitive, each is a valid and absolute URL, and all defined to use the same vocabulary. The attribute's value must have at least one token.
*   The item types must all be types defined in applicable specifications (such as [schema.org](https://schema.org/ "External link (opens in new tab)")
    ), and must all be defined to use the same vocabulary.
*   The itemtype attribute can only be specified on elements which have an itemscope attribute specified.
*   The itemid attribute can only be specified on elements which have both an itemscope attribute and an itemtype attribute specified. They must only be specified on elements with an itemscope attribute, whose itemtype attribute specifies a vocabulary not supporting global identifiers for items, as defined by that vocabulary's specification.
*   The exact meaning of a global identifier is determined by the vocabulary's specification. It is left to such specifications to define whether multiple items of the same global identifier (whether on the same page or different pages) are allowed to exist, and what processing rules for that vocabulary are, with respect to handling the case of multiple items with the same ID.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype#examples)

------------------------------------------------------------------------------------------------------------

### [Representing structured data for a product](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype#representing_structured_data_for_a_product)

This example uses microdata attributes to represent structured data for a product, as follows:

|     |     |     |     |
| --- | --- | --- | --- |
| itemscope | itemtype | Product (https://schema.org/Product) |     |
| itemprop | name | Executive Anvil |
| itemprop | image | https://pixabay.com/static/uploads/photo/2015/09/05/18/15/suitcase-924605\_960\_720.png |
| itemprop | description | Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height. |
| itemprop | mpn | 925872 |
| itemprop | brand \[Thing\] |     |
| itemprop | name | ACME |
| itemscope | itemprop\[itemtype\] | aggregateRating\[AggregateRating\] |     |
| itemprop | ratingValue | 4.4 |
| itemprop | reviewCount | 89  |
| itemprop | offers \[Offer\] | https://schema.org/Offer |
| itemprop | priceCurrency | USD |
| itemprop | price | 119.99 |
| itemprop | priceValidUntil | 2020-11-05 |
| itemprop | itemCondition | https://schema.org/UsedCondition |
| itemprop | availability | https://schema.org/InStock |
| itemscope | itemprop\[itemtype\] | seller \[Organization\] | https://schema.org/Organization |
| itemprop | name | Executive Objects |

**Note:** A handy tool for extracting microdata structures from HTML is Google's [Structured Data Testing Tool](https://developers.google.com/search/docs/appearance/structured-data "External link (opens in new tab)")
. Try it on the HTML shown here.

#### HTML

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-itemtype](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemtype) |

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype#see_also)

------------------------------------------------------------------------------------------------------------

*   [Other different global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    
*   Other microdata related global attributes:
    *   [`itemid`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid)
        
    *   [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
        
    *   [`itemref`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref)
        
    *   [`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/itemtype/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/itemtype (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemtype&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemtype%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemtype%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemtype%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")