*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#mdn-search)
    

`<data>` HTML data element
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<data>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element links a given piece of content with a machine-readable translation. If the content is time- or date-related, the [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time)
 element must be used.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#try_it)

-------------------------------------------------------------------------------------------

    <p>New Products:</p>
    <ul>
      <li><data value="398">Mini Ketchup</data></li>
      <li><data value="399">Jumbo Ketchup</data></li>
      <li><data value="400">Mega Jumbo Ketchup</data></li>
    </ul>
    

    data:hover::after {
      content: " (ID " attr(value) ")";
      font-size: 0.7em;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#attributes)

---------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#value)

This attribute specifies the machine-readable translation of the content of the element.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#examples)

-----------------------------------------------------------------------------------------------

The following example displays product names but also associates each name with a product number.

html

    <p>New Products</p>
    <ul>
      <li><data value="398">Mini Ketchup</data></li>
      <li><data value="399">Jumbo Ketchup</data></li>
      <li><data value="400">Mega Jumbo Ketchup</data></li>
    </ul>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLDataElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDataElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-data-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-data-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data#see_also)

-----------------------------------------------------------------------------------------------

*   The HTML [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time)
     element.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/data/index.md?plain=1 "Folder: en-us/web/html/reference/elements/data (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdata&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdata%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")