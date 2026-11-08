*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#mdn-search)
    

String.prototype.italics()
==========================

Deprecated

Avoid using this feature in new projects. HTML wrapper methods exist only for backwards compatibility. Use DOM APIs to create elements instead. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model "The DOM (Document Object Model) API represents HTML and XML documents as trees of nodes. You can use the API to inspect and modify the structure and content of a document.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`italics()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values creates a string that embeds this string in an [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
 element (`<i>str</i>`), which causes this string to be displayed as italic.

**Note:** All [HTML wrapper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#html_wrapper_methods)
 are deprecated and only standardized for compatibility purposes. Use [DOM APIs](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
 such as [`document.createElement()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
 instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#syntax)

-----------------------------------------------------------------------------------------------------------------

js

    italics()
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#return_value)

A string beginning with an `<i>` start tag, then the text `str`, and then an `</i>` end tag.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#examples)

---------------------------------------------------------------------------------------------------------------------

### [Using italics()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#using_italics)

The code below creates an HTML string and then replaces the document's body with it:

js

    const contentString = "Hello, world";
    
    document.body.innerHTML = contentString.italics();
    

This will create the following HTML:

html

    <i>Hello, world</i>
    

Instead of using `italics()` and creating HTML text directly, you should use DOM APIs such as [`document.createElement()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
. For example:

js

    const contentString = "Hello, world";
    const elem = document.createElement("i");
    elem.innerText = contentString;
    document.body.appendChild(elem);
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.italics](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html#sec-string.prototype.italics) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `String.prototype.italics` in `core-js`](https://core-js.io/docs/features/ecmascript/string-regexp "External link (opens in new tab)")
    
*   [es-shims polyfill of `String.prototype.italics`](https://www.npmjs.com/package/es-string-html-methods "External link (opens in new tab)")
    
*   [HTML wrapper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#html_wrapper_methods)
    
*   [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/italics/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/italics (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fitalics&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fitalics%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fitalics%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fitalics%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")