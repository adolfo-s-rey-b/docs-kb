*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break#mdn-search)
    

SyntaxError: unlabeled break must be inside loop or switch
==========================================================

The JavaScript exception "unlabeled break must be inside loop or switch" occurs when a [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
 statement is not inside a loop or a [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
 statement.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break#message)

------------------------------------------------------------------------------------------------------

SyntaxError: Illegal break statement (V8-based)
SyntaxError: unlabeled break must be inside loop or switch (Firefox)
SyntaxError: 'break' is only valid inside a switch or loop statement. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break#error_type)

------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------

[`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
 statements can be used to exit a loop or a `switch` statement, and using them elsewhere is a syntax error. Alternatively, you can provide a [label](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
 to the `break` statement to break out of any statement with that label — however, if the label does not reference a containing statement, another error [SyntaxError: label not found](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found)
 will be thrown.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break#examples)

--------------------------------------------------------------------------------------------------------

### [Unsyntactic break](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break#unsyntactic_break)

`break` cannot be used outside `switch` or loops.

Maybe instead of `break`, you intend to use [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
 to early-terminate a function.

### [Using break in callbacks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break#using_break_in_callbacks)

`break` cannot be used in callbacks, even if the callback is called from a loop.

Instead, refactor the code so the `break` is used outside the callback.

There's no way to early-terminate a [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
 loop. You can use [`some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
 instead, or convert it to a [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loop.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break#see_also)

--------------------------------------------------------------------------------------------------------

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_break/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/bad_break/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/bad_break (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_break&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_break%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_break%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_break%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")