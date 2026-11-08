*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref#mdn-search)
    

`itemref` HTML global attribute
===============================

Properties that are not descendants of an element with the [`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
 attribute can be associated with an item using the [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 **`itemref`**.

`itemref` provides a list of element IDs (not `itemid`s) elsewhere in the document, with additional properties

The `itemref` attribute can only be specified on elements that have an `itemscope` attribute specified.

**Note:** The `itemref` attribute is not part of the microdata data model. It is merely a syntactic construct to aid authors in adding annotations to pages where the data to be annotated does not follow a convenient tree structure. For example, it allows authors to mark up data in a table so that each column defines a separate item while keeping the properties in the cells.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref#examples)

-----------------------------------------------------------------------------------------------------------

### [Representing structured data for a band](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref#representing_structured_data_for_a_band)

This example uses microdata attributes to represent the following structured data (in [JSON-LD](https://json-ld.org/ "External link (opens in new tab)")
 format):

#### HTML

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-itemref](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemref) |

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Other different global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    
*   Other microdata related global attributes:
    *   [`itemid`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid)
        
    *   [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
        
    *   [`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
        
    *   [`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/itemref/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/itemref (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemref&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemref%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemref%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemref%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")