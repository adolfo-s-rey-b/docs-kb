*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#mdn-search)
    

`<embed>` HTML embed external content element
=============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<embed>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element embeds external content at the specified point in the document. This content is handled by the browser or an external application.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#try_it)

--------------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#attributes)

----------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#height)

The displayed height of the resource, in [CSS pixels](https://drafts.csswg.org/css-values/#px "External link (opens in new tab)")
. This must be an absolute value; percentages are _not_ allowed.

[`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#src)

The URL of the resource being embedded.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#type)

The [MIME type](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type)
 of the embedded resource.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#width)

The displayed width of the resource, in [CSS pixels](https://drafts.csswg.org/css-values/#px "External link (opens in new tab)")
. This must be an absolute value; percentages are _not_ allowed.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#usage_notes)

------------------------------------------------------------------------------------------------------

Modern browsers no longer support browser plug-ins such as Flash, but `<embed>` can still display content handled by the browser itself, such as PDFs in a built-in PDF viewer.

For PDF previews, consider [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
 or [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
. Unlike `<object>`, `<embed>` cannot contain fallback content. Unlike `<iframe>`, it has no attributes that control loading.

You can use the [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
 property to adjust the positioning of the embedded object within the element's frame.

**Note:** The [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 property has no effect on `<embed>` elements.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#accessibility)

----------------------------------------------------------------------------------------------------------

Use the [`title` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 on an `embed` element to label its content so that people navigating with assistive technology such as a screen reader can understand what it contains. The title's value should concisely describe the embedded content. Without a title, they may not be able to determine what its embedded content is. This context shift can be confusing and time-consuming, especially if the `embed` element contains interactive content like video or audio.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#examples)

------------------------------------------------------------------------------------------------

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, embedded content, interactive content, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | Any element that accepts embedded content. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | [`application`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role)<br>, [`document`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/document_role)<br>, [`img`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/img_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role) |
| DOM interface | [`HTMLEmbedElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLEmbedElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-embed-element](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-embed-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed#see_also)

------------------------------------------------------------------------------------------------

*   Other elements that are used for embedding content of various types include [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
    , [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
    , [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
    , [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    , [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math "<math>")
    , [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
    , [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
    , and [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
    .
*   Positioning and sizing the embedded content within its frame: [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
     and [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/embed/index.md?plain=1 "Folder: en-us/web/html/reference/elements/embed (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fembed&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fembed%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fembed%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fembed%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F456c370394c0cd8869feb60c4e9926f35422beaf%0A*+Document+last+modified%3A+2026-09-16T03%3A52%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")