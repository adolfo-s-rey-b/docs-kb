*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*#mdn-search)
    

`data-*` HTML global attributes
===============================

The **`data-*`** [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 form a class of attributes called **custom data attributes**, that allow proprietary information to be exchanged between the [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 and its [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
 representation by scripts.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*#try_it)

------------------------------------------------------------------------------------------------------

All such custom data are available via the [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
 interface of the element the attribute is set on. The [`HTMLElement.dataset`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset)
 property gives access to them. The `*` may be replaced by any name following [the production rule of XML names](https://www.w3.org/TR/xml/#NT-Name "External link (opens in new tab)")
 which includes the following recommendations:

*   The name should not start with `xml` (case-insensitive), as it's reserved for future XML specifications.
*   The name should not contain any colon characters (`:`), as XML assigns meaning to such names.
*   The name should not contain any capital letters, as XML is all lowercase.

These are recommendations. If these naming recommendations are not followed, no errors will occur. The attributes will still be matched using CSS [attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
, with the attribute being case insensitive and any attribute value being case-sensitive. Attributes not conforming to these three recommendations will also still be recognized by the JavaScript [`HTMLElement.dataset`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset)
 property and user-agents will include the attribute in the [`DOMStringMap`](https://developer.mozilla.org/en-US/docs/Web/API/DOMStringMap)
 containing all the custom data attributes for an [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
.

If you plan to use [`HTMLElement.dataset`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset)
, the portion of the attribute name following the `data-` can only include characters allowed in JavaScript property names (and hyphens, which will be removed). The `dataset` version of the attribute name removes the "data-" prefix and converts the rest of the name from [kebab-case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case)
 to camelCase. For example, `element.getAttribute("data-test")` is equivalent to `element.dataset.test` and `data-test-abc` will be accessible as `HTMLElement.dataset.testAbc` (or by `HTMLElement.dataset["testAbc"]`). Avoid non-alphabetic characters following a hyphen, such as `data-test-1` or `data--test`, as they will not be recognized by [`HTMLElement.dataset`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*#usage_notes)

----------------------------------------------------------------------------------------------------------------

By adding `data-*` attributes, even ordinary HTML elements can become rather complex and powerful program-objects. For example, a space-ship "[sprite](https://en.wikipedia.org/wiki/Sprite_(computer_graphics) "External link (opens in new tab)")
_"_ in a game could just be an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element with a [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)
 attribute and several `data-*` attributes:

For a more in-depth tutorial about using HTML data attributes, see [Using data attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Use_data_attributes)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-data-\*](https://html.spec.whatwg.org/multipage/dom.html#attr-data-*) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*#see_also)

----------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   The [`HTMLElement.dataset`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset)
     property that allows you to access and modify these values.
*   [Using data attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Use_data_attributes)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/data-_star_/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/data-_star_ (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fdata-*&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fdata-_star_%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fdata-*%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fdata-_star_%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F56f3d7018159127dbe92842413fb45d0aa7e8193%0A*+Document+last+modified%3A+2026-08-27T13%3A16%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")