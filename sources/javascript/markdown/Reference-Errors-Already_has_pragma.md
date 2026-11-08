*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Already_has_pragma#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Already_has_pragma#mdn-search)
    

Warning: -file- is being assigned a //# sourceMappingURL, but already has one
=============================================================================

The JavaScript warning "-file- is being assigned a //# sourceMappingURL, but already has one." occurs when a source map has been specified more than once for a given JavaScript source.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Already_has_pragma#message)

---------------------------------------------------------------------------------------------------------------

Warning: -file- is being assigned a //# sourceMappingURL, but already has one.

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Already_has_pragma#error_type)

---------------------------------------------------------------------------------------------------------------------

A warning. JavaScript execution won't be halted.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Already_has_pragma#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------------

A source map has been specified more than once for a given JavaScript source.

JavaScript sources are often combined and minified to make delivering them from the server more efficient. With [source maps](https://developer.chrome.com/blog/sourcemaps/ "External link (opens in new tab)")
, the debugger can map the code being executed to the original source files. There are two ways to assign a source map, either by using a comment or by setting a header to the JavaScript file.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Already_has_pragma#examples)

-----------------------------------------------------------------------------------------------------------------

### [Setting source maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Already_has_pragma#setting_source_maps)

Setting a source map by using a comment in the file:

js

    //# sourceMappingURL=http://example.com/path/to/your/sourcemap.map
    

Or, alternatively, you can set a header to your JavaScript file:

http

    X-SourceMap: /path/to/file.js.map
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Already_has_pragma#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Use a source map](https://firefox-source-docs.mozilla.org/devtools-user/debugger/how_to/use_a_source_map/index.html "External link (opens in new tab)")
     in the Firefox source docs
*   [Introduction to JavaScript source maps](https://developer.chrome.com/blog/sourcemaps/ "External link (opens in new tab)")
     on developer.chrome.com (2012)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Already_has_pragma/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/already_has_pragma/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/already_has_pragma (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FAlready_has_pragma&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Falready_has_pragma%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FAlready_has_pragma%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Falready_has_pragma%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")