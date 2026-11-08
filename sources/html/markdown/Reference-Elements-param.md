*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#mdn-search)
    

`<param>` HTML object parameter element
=======================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<param>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element defines parameters for an [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
 element.

**Note:** Use the [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
 element with a [`data`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#data)
 attribute to set the URL of an external resource.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#attributes)

----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#name)

Name of the parameter.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#value)

Specifies the value of the parameter.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#type)

Only used if the `valuetype` is set to `ref`. Specifies the MIME type of values found at the URI specified by value.

[`valuetype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#valuetype)

Specifies the type of the `value` attribute. Possible values are:

*   `data`: Default value. The value is passed to the object's implementation as a string.
*   `ref`: The value is a URI to a resource where run-time values are stored.
*   `object`: An ID of another [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
     in the same document.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | An [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)<br> before any [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLParamElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLParamElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# non-conforming-features](https://html.spec.whatwg.org/multipage/obsolete.html#non-conforming-features) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param#see_also)

------------------------------------------------------------------------------------------------

*   [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/param/index.md?plain=1 "Folder: en-us/web/html/reference/elements/param (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fparam&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fparam%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fparam%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fparam%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")