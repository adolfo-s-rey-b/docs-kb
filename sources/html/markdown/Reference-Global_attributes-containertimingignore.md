*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore#mdn-search)
    

`containertimingignore` HTML global attribute
=============================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/918)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore#browser_compatibility)
 carefully before using this in production.

The **`containertimingignore`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is a boolean attribute that excludes an element and its descendants from contributing to the timing of any ancestor element marked with [`containertiming`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming)
. For more details, see the [`PerformanceContainerTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceContainerTiming)
 interface.

In the DOM, this attribute is reflected as [`HTMLElement.containerTimingIgnore`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/containerTimingIgnore)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore#examples)

-------------------------------------------------------------------------------------------------------------------------

### [Excluding a subtree from a container's timing](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore#excluding_a_subtree_from_a_containers_timing)

In this example, the [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 and its contents are excluded from the `"hero"` container's timing, while the image still contributes to it.

For examples of how to use the Container Timing API to get timing information, see [`PerformanceContainerTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceContainerTiming)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore#specifications)

-------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Container Timing API  <br>\# dom-htmlelement-containertimingignore](https://w3c.github.io/container-timing/#dom-htmlelement-containertimingignore) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [`containertiming`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming)
    
*   [`PerformanceContainerTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceContainerTiming)
    
*   [`HTMLElement.containerTimingIgnore`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/containerTimingIgnore)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/containertimingignore/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/containertimingignore (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fcontainertimingignore&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fcontainertimingignore%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fcontainertimingignore%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fcontainertimingignore%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F076ee5b53d5e933e7fc2fd5eff68304f9691148e%0A*+Document+last+modified%3A+2026-11-06T19%3A44%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")