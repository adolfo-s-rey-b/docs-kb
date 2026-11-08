*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#mdn-search)
    

`containertiming` HTML global attribute
=======================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/918)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#browser_compatibility)
 carefully before using this in production.

The **`containertiming`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 marks an element as a _container root_, for which [`PerformanceContainerTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceContainerTiming)
 entries can be observed by [`PerformanceObserver`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver)
 objects using the `"container"` type.

Any paints to new areas inside the container root's subtree contribute to the container's timing (content painted inside the container root itself is excluded, as are repaints to already painted areas). Timing entries are reported only until the user scrolls or interacts with the page. Descendant subtrees can be excluded from a container's timing using the [`containertimingignore`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore)
 attribute. For more details, see the [`PerformanceContainerTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceContainerTiming)
 interface.

In the DOM, this attribute is reflected as [`HTMLElement.containerTiming`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/containerTiming)
.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#value)

-------------------------------------------------------------------------------------------------------------

A string that identifies the container. This is returned in [`PerformanceContainerTiming.identifier`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceContainerTiming/identifier)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#examples)

-------------------------------------------------------------------------------------------------------------------

### [Marking a container root](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#marking_a_container_root)

This example marks two elements as container roots, identified as `"hero"` and `"product-list"`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Container Timing API  <br>\# dom-htmlelement-containertiming](https://w3c.github.io/container-timing/#dom-htmlelement-containertiming) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`containertimingignore`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore)
    
*   [`PerformanceContainerTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceContainerTiming)
    
*   [`HTMLElement.containerTiming`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/containerTiming)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/containertiming/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/containertiming (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fcontainertiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fcontainertiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fcontainertiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fcontainertiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F076ee5b53d5e933e7fc2fd5eff68304f9691148e%0A*+Document+last+modified%3A+2026-11-06T19%3A44%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")