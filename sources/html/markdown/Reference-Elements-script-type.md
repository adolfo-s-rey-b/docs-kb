*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#mdn-search)
    

`<script type>` HTML attribute
==============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`type`** attribute of the [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 element indicates the _type_ of script represented by the element: a classic script, an import map, a JavaScript module, speculation rules, or a data block.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#value)

------------------------------------------------------------------------------------------------

The value of this attribute indicates the type of data represented by the script, and will be one of the following:

[**Attribute is not set (default), an empty string, or a JavaScript MIME type**](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#attribute_is_not_set_default_an_empty_string_or_a_javascript_mime_type)

Indicates that the script is a "classic script", containing JavaScript code. Authors are encouraged to omit the attribute if the script refers to JavaScript code rather than specify a MIME type. JavaScript MIME types are [listed in the IANA media types specification](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types#textjavascript)
.

[`importmap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap)

This value indicates that the body of the element contains an import map. The import map is a JSON object that developers can use to control how the browser resolves module specifiers when importing [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules_on_the_web#importing_modules_using_import_maps)
.

[`module`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#module)

This value causes the code to be treated as a JavaScript module. The processing of the script contents is deferred. The `charset` and `defer` attributes have no effect. For information on using `module`, see our [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
 guide. Unlike classic scripts, module scripts require the use of the CORS protocol for cross-origin fetching.

[`speculationrules`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules)

This value indicates that the body of the element contains speculation rules. Speculation rules take the form of a JSON object that determine what resources should be prefetched or prerendered by the browser. This is part of the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
.

[**Any other value**](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#any_other_value)

The embedded content is treated as a data block, and won't be processed by the browser. Developers must use a valid MIME type that is not a JavaScript MIME type to denote data blocks. All of the other attributes will be ignored, including the `src` attribute.

**Note:** In earlier browsers, the type identified the scripting language of the embedded or imported (via the `src` attribute) code.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-script-type](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/script/type/index.md?plain=1 "Folder: en-us/web/html/reference/elements/script/type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fscript%2Ftype&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fscript%2Ftype%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fscript%2Ftype%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fscript%2Ftype%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")