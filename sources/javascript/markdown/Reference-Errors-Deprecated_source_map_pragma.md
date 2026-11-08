*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma#mdn-search)
    

SyntaxError: Using //@ to indicate sourceURL pragmas is deprecated. Use //# instead
===================================================================================

The JavaScript warning "Using `//@` to indicate sourceURL pragmas is deprecated. Use `//#` instead" occurs when there is a deprecated source map syntax in a JavaScript source.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma#message)

-------------------------------------------------------------------------------------------------------------------------

Warning: SyntaxError: Using //@ to indicate sourceURL pragmas is deprecated. Use //# instead

Warning: SyntaxError: Using //@ to indicate sourceMappingURL pragmas is deprecated. Use //# instead

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma#error_type)

-------------------------------------------------------------------------------------------------------------------------------

A warning that a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
 occurred. JavaScript execution won't be halted.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------------------

There is a deprecated source map syntax in a JavaScript source.

JavaScript sources are often combined and minified to make delivering them from the server more efficient. With [source maps](https://firefox-source-docs.mozilla.org/devtools-user/debugger/how_to/use_a_source_map/index.html "External link (opens in new tab)")
, the debugger can map the code being executed to the original source files.

The source map specification changed the syntax due to a conflict with IE whenever it was found in the page after `//@cc_on` was interpreted to turn on conditional compilation in the IE JScript engine. The [conditional compilation comment](https://stackoverflow.com/questions/24473882/what-does-this-comment-cc-on-0-do-inside-an-if-statement-in-javascript "External link (opens in new tab)")
 in IE is a little known feature, but it broke source maps with [jQuery](https://bugs.jquery.com/ticket/13274/ "External link (opens in new tab)")
 and other libraries.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Deprecated syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma#deprecated_syntax)

Syntax with the "@" sign is deprecated.

### [Standard syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma#standard_syntax)

Use the "#" sign instead.

Or, alternatively, you can set a [`SourceMap`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/SourceMap)
 header to your JavaScript file to avoid having a comment at all:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [Use a source map](https://firefox-source-docs.mozilla.org/devtools-user/debugger/how_to/use_a_source_map/index.html "External link (opens in new tab)")
     in the Firefox source docs
*   [Introduction to JavaScript source maps](https://developer.chrome.com/blog/sourcemaps/ "External link (opens in new tab)")
     on developer.chrome.com (2012)
*   [`SourceMap`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/SourceMap)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Deprecated_source_map_pragma/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/deprecated_source_map_pragma/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/deprecated_source_map_pragma (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FDeprecated_source_map_pragma&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fdeprecated_source_map_pragma%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FDeprecated_source_map_pragma%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fdeprecated_source_map_pragma%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")