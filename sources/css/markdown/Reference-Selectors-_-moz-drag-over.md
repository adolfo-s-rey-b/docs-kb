*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#mdn-search)
    

`:-moz-drag-over` CSS pseudo-class
==================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`:-moz-drag-over`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 is a [Mozilla extension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
 that matches an element when a [`dragover`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragover_event "dragover")
 event is called on it.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#syntax)

------------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#examples)

----------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#html)

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#javascript)

Most elements are not valid places to drop data, so in order to allow a drop, you must prevent default behavior by canceling [`dragenter`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragenter_event)
 or [`dragover`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragover_event)
 (or both) events. In this example, we only need to cancel the `dragenter` event, which is the first event fired when the browser evaluates if an element can be a drop target. For more information, see [Drag operations: Specifying drop targets](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations#dragging_over_elements_and_specifying_drop_targets)
.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#css)

The following CSS changes the drop target color to red when the draggable element overlays the drop area.

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#specifications)

----------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over#see_also)

----------------------------------------------------------------------------------------------------------

*   [Mozilla CSS extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
    
*   [HTML drag and drop](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_-moz-drag-over/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_-moz-drag-over (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-drag-over&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-drag-over%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-drag-over%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-drag-over%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F77ea71add6054857698eb7ac1bfec8c7afe9ad4f%0A*+Document+last+modified%3A+2026-08-27T08%3A10%3A48.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")