*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#mdn-search)
    

String.prototype.strike()
=========================

Deprecated

Avoid using this feature in new projects. HTML wrapper methods exist only for backwards compatibility. Use DOM APIs to create elements instead. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model "The DOM (Document Object Model) API represents HTML and XML documents as trees of nodes. You can use the API to inspect and modify the structure and content of a document.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`strike()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values creates a string that embeds this string in a [`<strike>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strike)
 element (`<strike>str</strike>`), which causes this string to be displayed as struck-out text.

**Note:** All [HTML wrapper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#html_wrapper_methods)
 are deprecated and only standardized for compatibility purposes. For the case of `strike()`, the `<strike>` element itself has been removed from the HTML specification and shouldn't be used anymore. Web developers should use the [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)
 for deleted content or the [`<s>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/s)
 for content that is no longer accurate or no longer relevant instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#syntax)

----------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#return_value)

A string beginning with a `<strike>` start tag, then the text `str`, and then a `</strike>` end tag.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#examples)

--------------------------------------------------------------------------------------------------------------------

### [Using strike()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#using_strike)

The code below creates an HTML string and then replaces the document's body with it:

This will create the following HTML:

**Warning:** This markup is invalid, because `strike` is no longer a valid element.

Instead of using `strike()` and creating HTML text directly, you should use DOM APIs such as [`document.createElement()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
. For example:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.strike](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html#sec-string.prototype.strike) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `String.prototype.strike` in `core-js`](https://core-js.io/docs/features/ecmascript/string-regexp "External link (opens in new tab)")
    
*   [es-shims polyfill of `String.prototype.strike`](https://www.npmjs.com/package/es-string-html-methods "External link (opens in new tab)")
    
*   [HTML wrapper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#html_wrapper_methods)
    
*   [`<strike>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strike)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/strike/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/strike (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fstrike&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fstrike%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fstrike%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fstrike%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")