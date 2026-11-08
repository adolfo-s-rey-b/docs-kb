*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/elementtiming#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/elementtiming#mdn-search)
    

`elementtiming` HTML attribute
==============================

The **`elementtiming`** attribute is used to indicate that an element is flagged for tracking by [`PerformanceObserver`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver)
 objects using the `"element"` type. For more details, see the [`PerformanceElementTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceElementTiming)
 interface.

This attribute may be applied to [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
, [`<image>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/image)
 elements inside an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
, poster images of [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 elements, elements which have a [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
, and elements containing text nodes, such as a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
.

In the DOM, this attribute is reflected as [`Element.elementTiming`](https://developer.mozilla.org/en-US/docs/Web/API/Element/elementTiming)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/elementtiming#usage_notes)

----------------------------------------------------------------------------------------------------------------

The value given for `elementtiming` becomes an identifier for the observed element.

Good contenders for elements you might want to observe are:

*   The main image for an article.
*   A blog post title
*   Images in a carousel for a shopping site.
*   The poster image for the main video on a page.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/elementtiming#examples)

----------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/elementtiming#see_also)

----------------------------------------------------------------------------------------------------------

*   [`PerformanceElementTiming`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceElementTiming)
    
*   [`Element.elementTiming`](https://developer.mozilla.org/en-US/docs/Web/API/Element/elementTiming)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/elementtiming/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/elementtiming/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/elementtiming (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Felementtiming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Felementtiming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Felementtiming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Felementtiming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")