*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/draggable#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/draggable#mdn-search)
    

`draggable` HTML global attribute
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/draggable#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`draggable`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute that indicates whether the element can be dragged, either with native browser behavior or the [HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
.

The `draggable` attribute may be applied to elements that strictly fall under the [HTML namespace](https://developer.mozilla.org/en-US/docs/Glossary/Namespace)
, which means that it cannot be applied to [SVGs](https://developer.mozilla.org/en-US/docs/Web/SVG)
. For more information about what namespace declarations look like, and what they do, see [Namespace crash course](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Namespaces_crash_course)
.

`draggable` can have the following values:

*   `true`: the element can be dragged.
*   `false`: the element cannot be dragged.

**Warning:** This attribute is _[enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
_ and not _Boolean_. A value of `true` or `false` is mandatory, and shorthand like `<img draggable>` is forbidden. The correct usage is `<img draggable="true">`.

If this attribute is not set, its default value is `auto`, which means drag behavior is the default browser behavior: only text selections, images, and links can be dragged. For other elements, the event [`ondragstart`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragstart_event "ondragstart")
 must be set for drag and drop to work, as shown in this [comprehensive example](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/draggable#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-draggable-attribute](https://html.spec.whatwg.org/multipage/dnd.html#the-draggable-attribute) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/draggable#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/draggable#see_also)

-------------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/draggable/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/draggable/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/draggable (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fdraggable&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fdraggable%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fdraggable%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fdraggable%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")