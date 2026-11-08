*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#mdn-search)
    

String.prototype.anchor()
=========================

Deprecated

Avoid using this feature in new projects. HTML wrapper methods exist only for backwards compatibility. Use DOM APIs to create elements instead. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model "The DOM (Document Object Model) API represents HTML and XML documents as trees of nodes. You can use the API to inspect and modify the structure and content of a document.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`anchor()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values creates a string that embeds this string in an [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 element with a name (`<a name="...">str</a>`).

**Note:** All [HTML wrapper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#html_wrapper_methods)
 are deprecated and only standardized for compatibility purposes. Use [DOM APIs](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
 such as [`document.createElement()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
 instead.

The HTML specification no longer allows the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 element to have a `name` attribute, so this method doesn't even create valid markup.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#syntax)

----------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#parameters)

[`name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#name)

A string representing a `name` value to put into the generated `<a name="...">` start tag.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#return_value)

A string beginning with an `<a name="name">` start tag (double quotes in `name` are replaced with `&quot;`), then the text `str`, and then an `</a>` end tag.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#examples)

--------------------------------------------------------------------------------------------------------------------

### [Using anchor()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#using_anchor)

The code below creates an HTML string and then replaces the document's body with it:

This will create the following HTML:

**Warning:** This markup is invalid, because `name` is no longer a valid attribute of the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 element.

Instead of using `anchor()` and creating HTML text directly, you should use DOM APIs such as [`document.createElement()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
. For example:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.anchor](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html#sec-string.prototype.anchor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `String.prototype.anchor` in `core-js`](https://core-js.io/docs/features/ecmascript/string-regexp "External link (opens in new tab)")
    
*   [es-shims polyfill of `String.prototype.anchor`](https://www.npmjs.com/package/es-string-html-methods "External link (opens in new tab)")
    
*   [HTML wrapper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#html_wrapper_methods)
    
*   [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/anchor/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/anchor (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fanchor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fanchor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fanchor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fanchor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")