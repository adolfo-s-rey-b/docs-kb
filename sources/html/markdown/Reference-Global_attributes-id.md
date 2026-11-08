*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id#mdn-search)
    

`id` HTML global attribute
==========================

The **`id`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 defines an identifier (ID) that must be unique within the entire document.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id#syntax)

--------------------------------------------------------------------------------------------------

An ID attribute's value must not contain [ASCII whitespace](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace#in_html)
 characters. Browsers treat non-conforming IDs that contain whitespace as if the whitespace is part of the ID. In contrast to the [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)
 attribute, which allows space-separated values, elements can only have one single ID value.

Technically, the value for an ID attribute may contain any other Unicode character. However, when used in CSS selectors, either from JavaScript using APIs like [`Document.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
 or in CSS stylesheets, ID attribute values must be valid [CSS identifiers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
. This means that if an ID attribute value is not a valid CSS identifier (for example, `my?id` or `1234`) then it must be escaped before being used in a selector, either using the [`CSS.escape()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/escape_static "CSS.escape()")
 method or [manually](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#escaping_characters)
.

For this reason, it's recommended that developers choose values for ID attributes that are valid CSS identifiers that don't require escaping.

Also, not all valid ID attribute values are valid JavaScript identifiers. For example, `1234` is a valid attribute value but not a valid JavaScript identifier. This means that the value is not a valid variable name, so you can't access the element using code like `window.1234`. However, you can access it using `window["1234"]`.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id#description)

------------------------------------------------------------------------------------------------------------

The purpose of the ID attribute is to identify a single element when linking (using a [fragment identifier](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment)
), scripting, or styling (with [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
).

You can access elements with ID attributes as global properties of the `window` object, where the property name is the ID value, and the property value is the corresponding element. For example, given this markup:

You can access this paragraph element in JavaScript using the following code:

**Warning:** Relying on the `window["id-value"]` or `window.idValue` pattern is dangerous and discouraged because it can lead to unexpected conflicts with existing or future APIs in the browser. For example, if a browser introduces a built-in global property named `preamble` in the future, your code may no longer be able to access the HTML element. To avoid such conflicts, always use the [`Document.getElementById()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)
 or [`Document.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
 method to access elements by ID.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-id-attribute](https://html.spec.whatwg.org/multipage/dom.html#the-id-attribute) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id#see_also)

------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   [`Element.id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id)
     that reflects this attribute.
*   The [`Document.getElementById`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)
     method.
*   CSS [ID selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/ID_selectors)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/id/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/id (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fid&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fid%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fid%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fid%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")