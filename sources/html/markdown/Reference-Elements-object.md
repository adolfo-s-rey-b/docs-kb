*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#mdn-search)
    

`<object>` HTML external object element
=======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<object>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#try_it)

---------------------------------------------------------------------------------------------

    <object
      type="video/mp4"
      data="/shared-assets/videos/flower.mp4"
      width="250"
      height="200"></object>
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#attributes)

-----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`archive`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#archive)

A space-separated list of URIs for archives of resources for the object.

[`border`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#border)

The width of a border around the control, in pixels.

[`classid`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#classid)

The URI of the object's implementation. It can be used together with, or in place of, the **data** attribute.

[`codebase`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#codebase)

The base path used to resolve relative URIs specified by **classid**, **data**, or **archive**. If not specified, the default is the base URI of the current document.

[`codetype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#codetype)

The content type of the data specified by **classid**.

[`data`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#data)

The address of the resource as a valid URL. At least one of **data** and **type** must be defined.

[`declare`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#declare)

The presence of this Boolean attribute makes this element a declaration only. The object must be instantiated by a subsequent `<object>` element. Repeat the `<object>` element completely each time the resource is reused.

[`form`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form)

The form element, if any, that the object element is associated with (its _form owner_). The value of the attribute must be an ID of a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element in the same document.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#height)

The height of the displayed resource, as in [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 in [CSS pixels](https://developer.mozilla.org/en-US/docs/Glossary/CSS_pixel)
.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#name)

The name of valid browsing context (HTML5), or the name of the control (HTML 4). The name becomes a property of the [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 and [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document)
 objects, containing a reference to the embedded window or the element itself.

[`standby`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#standby)

A message that the browser can show while loading the object's implementation and data.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#type)

The [content type](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type)
 of the resource specified by **data**. At least one of **data** and **type** must be defined.

[`usemap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#usemap)

A hash-name reference to a [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
 element; that is a '#' followed by the value of a [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#name)
 of a map element.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#width)

The width of the display resource, as in [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 in [CSS pixels](https://developer.mozilla.org/en-US/docs/Glossary/CSS_pixel)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#usage_notes)

-------------------------------------------------------------------------------------------------------

The `<object>` element can display PDFs using the browser's built-in PDF viewer. Its children provide fallback content when the resource cannot be displayed. You can use this to provide a link to the PDF, but also provide a link outside the element so it remains available if the viewer loads but fails to display the PDF.

Unlike [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
, `<object>` has no attributes that control loading. The embedding page's Content Security Policy controls its sources through [`object-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/object-src)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#examples)

-------------------------------------------------------------------------------------------------

### [Embed a video](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#embed_a_video)

#### HTML

html

    <object
      type="video/webm"
      data="/shared-assets/videos/flower.webm"
      width="600"
      height="140">
      <img
        src="/shared-assets/images/examples/flowers.jpg"
        alt="Some beautiful flowers" />
    </object>
    

#### Result

If the video in the example fails to load, the user will be provided with an image as fallback content. The [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 tag is used to display an image. We include the `src` attribute set to the path to the image we want to embed. We also include the `alt` attribute, which provides the image with an accessible name. If the image also fails to load, the content of the `alt` attribute will be displayed.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>; [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>; [embedded content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#embedded_content)<br>, palpable content; if the element has a [`usemap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#usemap)<br> attribute, [interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)<br>; [listed](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#listed)<br>, [submittable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#submittable)<br> [form-associated](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#form-associated_content)<br> element. |
| Permitted content | zero or more [`<param>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param)<br> elements, then [transparent](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#transparent_content_model)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [embedded content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#embedded_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | [`application`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role)<br>, [`document`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/document_role)<br>, [`img`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/img_role) |
| DOM interface | [`HTMLObjectElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-object-element](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-object-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#see_also)

-------------------------------------------------------------------------------------------------

*   [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
    
*   [`<param>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/object/index.md?plain=1 "Folder: en-us/web/html/reference/elements/object (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fobject&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fobject%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fobject%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fobject%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F456c370394c0cd8869feb60c4e9926f35422beaf%0A*+Document+last+modified%3A+2026-09-16T03%3A52%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")