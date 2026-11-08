*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#mdn-search)
    

`<frame>` HTML frame element
============================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<frame>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element defines a particular area in which another HTML document can be displayed. A frame should be used within a [`<frameset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset)
.

Using the `<frame>` element is not encouraged because of certain disadvantages such as performance problems and lack of accessibility for users with screen readers. Instead of the `<frame>` element, [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 may be preferred.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#attributes)

----------------------------------------------------------------------------------------------------

Like all other HTML elements, this element supports the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#src)

This attribute specifies the document that will be displayed by the frame.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#name)

This attribute is used for labeling frames. Without labeling, every link will open in the frame that it's in – the closest parent frame. See the [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#target)
 attribute for more information.

[`noresize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#noresize)

This attribute prevents resizing of frames by users.

[`scrolling`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#scrolling)

This attribute defines the existence of a scrollbar. If this attribute is not used, the browser adds a scrollbar when necessary. There are two choices: "yes" for forcing a scrollbar even when it is not necessary and "no" for forcing no scrollbar even when it _is_ necessary.

[`marginheight`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#marginheight)

This attribute defines the height of the margin between frames.

[`marginwidth`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#marginwidth)

This attribute defines the width of the margin between frames.

[`frameborder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#frameborder)

This attribute allows you to specify a frame's border.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#example)

----------------------------------------------------------------------------------------------

### [A frameset document](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#a_frameset_document)

A frameset document has a [`<frameset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset)
 element instead of a [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element. The `<frame>` elements are placed within the `<frameset>`.

If you want to embed another HTML page into the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 of a document, use an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 element.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# frame](https://html.spec.whatwg.org/multipage/obsolete.html#frame) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame#see_also)

------------------------------------------------------------------------------------------------

*   [`<frameset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset)
    
*   [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/frame/index.md?plain=1 "Folder: en-us/web/html/reference/elements/frame (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fframe&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fframe%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fframe%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fframe%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")