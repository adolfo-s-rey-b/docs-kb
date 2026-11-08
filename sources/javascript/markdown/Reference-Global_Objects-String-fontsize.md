*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#mdn-search)
    

String.prototype.fontsize()
===========================

Deprecated

Avoid using this feature in new projects. HTML wrapper methods exist only for backwards compatibility. Use DOM APIs to create elements instead. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model "The DOM (Document Object Model) API represents HTML and XML documents as trees of nodes. You can use the API to inspect and modify the structure and content of a document.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`fontsize()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values creates a string that embeds this string in a [`<font>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/font)
 element (`<font size="...">str</font>`), which causes this string to be displayed in the specified font size.

**Note:** All [HTML wrapper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#html_wrapper_methods)
 are deprecated and only standardized for compatibility purposes. For the case of `fontsize()`, the `<font>` element itself has been removed from the HTML specification and shouldn't be used anymore. Web developers should use [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 properties instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#syntax)

------------------------------------------------------------------------------------------------------------------

js

    fontsize(size)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#parameters)

[`size`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#size)

An integer between 1 and 7, or a string representing a signed integer between 1 and 7.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#return_value)

A string beginning with a `<font size="size">` start tag (double quotes in `size` are replaced with `&quot;`), then the text `str`, and then a `</font>` end tag.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#description)

----------------------------------------------------------------------------------------------------------------------------

The `fontsize()` method itself simply joins the string parts together without any validation or normalization. However, to create valid [`<font>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/font)
 elements, When you specify size as an integer, you set the font size of `str` to one of the 7 defined sizes. You can specify `size` as a string such as `"-2"` or `"+3"` to adjust the font size of `str` relative to 3, the default value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#examples)

----------------------------------------------------------------------------------------------------------------------

### [Using fontsize()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#using_fontsize)

The code below creates an HTML string and then replaces the document's body with it:

js

    const contentString = "Hello, world";
    
    document.body.innerHTML = contentString.fontsize(7);
    

This will create the following HTML:

html

    <font size="7">Hello, world</font>
    

**Warning:** This markup is invalid, because `font` is no longer a valid element.

Instead of using `fontsize()` and creating HTML text directly, you should use CSS to manipulate fonts. For example, you can manipulate [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 through the [`element.style`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style "element.style")
 attribute:

js

    document.getElementById("yourElemId").style.fontSize = "7pt";
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.fontsize](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html#sec-string.prototype.fontsize) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `String.prototype.fontsize` in `core-js`](https://core-js.io/docs/features/ecmascript/string-regexp "External link (opens in new tab)")
    
*   [es-shims polyfill of `String.prototype.fontsize`](https://www.npmjs.com/package/es-string-html-methods "External link (opens in new tab)")
    
*   [HTML wrapper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#html_wrapper_methods)
    
*   [`<font>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/font)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/fontsize/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/fontsize (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Ffontsize&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Ffontsize%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Ffontsize%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Ffontsize%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")