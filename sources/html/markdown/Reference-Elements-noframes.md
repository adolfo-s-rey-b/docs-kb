*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes#mdn-search)
    

`<noframes>` HTML frame fallback element
========================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<noframes>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element provides content to be presented in browsers that don't support (or have disabled support for) the [`<frame>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame)
 element. Although most commonly-used browsers support frames, there are exceptions, including certain special-use browsers including some mobile browsers, as well as text-mode browsers.

A `<noframes>` element can contain any HTML elements that are allowed within the body of an HTML document, except for the [`<frameset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset)
 and [`<frame>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame)
 elements, since using frames when they aren't supported doesn't make sense.

`<noframes>` can be used to present a message explaining that the user's browser doesn't support frames, but ideally should be used to present an alternate form of the site that doesn't use frames but still offers the same or similar functionality.

**Note:** This element is obsolete and shouldn't be used, since the [`<frame>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame)
 and [`<frameset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset)
 elements are also obsolete. When frames are needed at all, they should be presented using the [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 element.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes#attributes)

-------------------------------------------------------------------------------------------------------

Like all other HTML elements, this element supports the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
. It has no other attributes available.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes#example)

-------------------------------------------------------------------------------------------------

In this example, we see a frameset with two frames. In addition, `<noframes>` is used to present an explanatory message if the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 doesn't support frames.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# noframes](https://html.spec.whatwg.org/multipage/obsolete.html#noframes) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes#see_also)

---------------------------------------------------------------------------------------------------

*   [`<frameset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset)
    
*   [`<frame>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/noframes/index.md?plain=1 "Folder: en-us/web/html/reference/elements/noframes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fnoframes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fnoframes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fnoframes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fnoframes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")