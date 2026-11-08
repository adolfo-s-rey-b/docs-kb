*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class#mdn-search)
    

`class` HTML global attribute
=============================

The **`class`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is a list of the classes of the element, separated by [ASCII whitespace](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace#in_html)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class#try_it)

-----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class#syntax)

-----------------------------------------------------------------------------------------------------

The `class` attribute is a list of class values separated by [ASCII whitespace](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace#in_html)
.

Each class value may contain any Unicode characters (except, of course, ASCII whitespace). However, when used in CSS selectors, either from JavaScript using APIs like [`Document.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
 or in CSS stylesheets, class attribute values must be valid [CSS identifiers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
. This means that if a class attribute value is not a valid CSS identifier (for example, `my?class` or `1234`) then it must be escaped before being used in a selector, either using the [`CSS.escape()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/escape_static "CSS.escape()")
 method or [manually](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#escaping_characters)
.

For this reason, it's recommended that developers choose values for class attributes that are valid CSS identifiers that don't require escaping.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class#description)

---------------------------------------------------------------------------------------------------------------

Classes allow CSS and JavaScript to select and access specific elements via the [class selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors)
 or functions like the [`document.getElementsByClassName()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName)
.

Though the specification doesn't put requirements on the name of classes, web developers are encouraged to use names that describe the semantic purpose of the element, rather than the presentation of the element. For example, _attribute_ to describe an attribute rather than _italics_, although an element of this class may be presented by _italics_. Semantic names remain logical even if the presentation of the page changes.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# classes](https://html.spec.whatwg.org/multipage/dom.html#classes) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class#see_also)

---------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   [`element.className`](https://developer.mozilla.org/en-US/docs/Web/API/Element/className)
    
*   [`element.classList`](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)
    
*   [Introduction to CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/class/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/class (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fclass&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fclass%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fclass%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fclass%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")