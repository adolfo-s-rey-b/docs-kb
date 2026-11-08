*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#mdn-search)
    

`<ins>` HTML inserted text element
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<ins>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a range of text that has been added to a document. You can use the [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)
 element to similarly represent a range of text that has been deleted from the document.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#try_it)

------------------------------------------------------------------------------------------

    <p>&ldquo;You're late!&rdquo;</p>
    <del>
      <p>&ldquo;I apologize for the delay.&rdquo;</p>
    </del>
    <ins cite="../how-to-be-a-wizard.html" datetime="2018-05">
      <p>&ldquo;A wizard is never late &hellip;&rdquo;</p>
    </ins>
    

    del,
    ins {
      display: block;
      text-decoration: none;
      position: relative;
    }
    
    del {
      background-color: #ffbbbb;
    }
    
    ins {
      background-color: #d4fcbc;
    }
    
    del::before,
    ins::before {
      position: absolute;
      left: 0.5rem;
      font-family: monospace;
    }
    
    del::before {
      content: "−";
    }
    
    ins::before {
      content: "+";
    }
    
    p {
      margin: 0 1.8rem;
      font-family: "Georgia", serif;
      font-size: 1rem;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#attributes)

--------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`cite`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#cite)

This attribute defines the URI of a resource that explains the change, such as a link to meeting minutes or a ticket in a troubleshooting system.

[`datetime`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#datetime)

This attribute indicates the time and date of the change and must be a valid date with an optional time string. If the value cannot be parsed as a date with an optional time string, the element does not have an associated timestamp. For the format of the string without a time, see [Format of a valid date string](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#date_strings)
. The format of the string if it includes both date and time is covered in [Format of a valid local date and time string](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#local_date_and_time_strings)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#examples)

----------------------------------------------------------------------------------------------

html

    <ins>This text has been inserted</ins>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Permitted content | [Transparent](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#transparent_content_model)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[insertion](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles#structural_roles_with_html_equivalents) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLModElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLModElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-ins-element](https://html.spec.whatwg.org/multipage/edits.html#the-ins-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#see_also)

----------------------------------------------------------------------------------------------

*   [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)
     element for marking deletion into a document

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/ins/index.md?plain=1 "Folder: en-us/web/html/reference/elements/ins (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fins&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fins%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fins%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fins%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32eceacf42b6bff41d9605298eba143cb7e199a1%0A*+Document+last+modified%3A+2026-10-17T20%3A27%3A33.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")