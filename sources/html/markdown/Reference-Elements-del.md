*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#mdn-search)
    

`<del>` HTML deleted text element
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<del>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)
 element can be used for the opposite purpose: to indicate text that has been added to the document.

This element is often (but need not be) rendered by applying a strike-through style to the text.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#try_it)

------------------------------------------------------------------------------------------

    <blockquote>
      There is <del>nothing</del> <ins>no code</ins> either good or bad, but
      <del>thinking</del> <ins>running it</ins> makes it so.
    </blockquote>
    

    del {
      text-decoration: line-through;
      background-color: #ffbbbb;
      color: #555555;
    }
    
    ins {
      text-decoration: none;
      background-color: #d4fcbc;
    }
    
    blockquote {
      padding-left: 15px;
      border-left: 3px solid #d7d7db;
      font-size: 1rem;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#attributes)

--------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`cite`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#cite)

A URI for a resource that explains the change (for example, meeting minutes).

[`datetime`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#datetime)

This attribute indicates the time and date of the change and must be a valid date string with an optional time. If the value cannot be parsed as a date with an optional time string, the element does not have an associated timestamp. For the format of the string without a time, see [Date strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#date_strings)
. The format of the string if it includes both date and time is covered in [Local date and time strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#local_date_and_time_strings)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#examples)

----------------------------------------------------------------------------------------------

html

    <p><del>This text has been deleted</del>, here is the rest of the paragraph.</p>
    <del><p>This paragraph has been deleted.</p></del>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Permitted content | [Transparent](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#transparent_content_model)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[deletion](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles#structural_roles_with_html_equivalents) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLModElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLModElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-del-element](https://html.spec.whatwg.org/multipage/edits.html#the-del-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del#see_also)

----------------------------------------------------------------------------------------------

*   [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)
     element for insertions into a text
*   [`<s>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/s)
     element for strikethrough separate from representing deletion of text

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/del/index.md?plain=1 "Folder: en-us/web/html/reference/elements/del (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdel&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdel%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdel%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdel%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32eceacf42b6bff41d9605298eba143cb7e199a1%0A*+Document+last+modified%3A+2026-10-17T20%3A27%3A33.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")