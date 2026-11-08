*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid#mdn-search)
    

`itemid` HTML global attribute
==============================

The **`itemid`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 provides microdata in the form of a unique, global identifier of an item.

An `itemid` attribute can only be specified for an element that has both [`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
 and [`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)
 attributes. Also, `itemid` can only be specified on elements that possess an `itemscope` attribute whose corresponding `itemtype` refers to or defines a vocabulary that supports global identifiers.

The exact meaning of an `itemtype`'s global identifier is provided by the definition of that identifier within the specified vocabulary. The vocabulary defines whether several items with the same global identifier can coexist and, if so, how items with the same identifier are handled.

**Note:** The [WHATWG](https://developer.mozilla.org/en-US/docs/Glossary/WHATWG)
 definition specifies that an `itemid` must be a [URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)
. However, the following example correctly illustrates that a [URN](https://developer.mozilla.org/en-US/docs/Glossary/URN)
 may also be used. This inconsistency may reflect the incomplete nature of the Microdata specification.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid#examples)

----------------------------------------------------------------------------------------------------------

### [Representing structured data for a book](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid#representing_structured_data_for_a_book)

This example uses microdata attributes to represent the following structured data:

|     |     |     |
| --- | --- | --- |
| itemscope | itemtype: itemid | https://schema.org/Book: urn:isbn:0-374-22848-5 |     |
| itemprop | title | Owls of the Eastern Ice |
| itemprop | author | Jonathan C Slaght |
| itemprop | datePublished | 2020-08-04 |

#### HTML

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-itemid](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemid) |

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid#see_also)

----------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   Other microdata related global attributes:
    *   [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
        
    *   [`itemref`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref)
        
    *   [`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
        
    *   [`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/itemid/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/itemid (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemid&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemid%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemid%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemid%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")