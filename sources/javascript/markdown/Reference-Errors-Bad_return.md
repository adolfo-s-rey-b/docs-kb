*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_return#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_return#mdn-search)
    

SyntaxError: return not in function
===================================

The JavaScript exception "return not in function" occurs when a [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
 statement is called outside of a [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_return#message)

-------------------------------------------------------------------------------------------------------

SyntaxError: Illegal return statement (V8-based)
SyntaxError: return not in function (Firefox)
SyntaxError: Return statements are only valid inside functions. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_return#error_type)

-------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_return#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------

A [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
 statement is called outside of a [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
. Maybe there are missing curly braces somewhere? The `return` statement must be in a function, because it ends function execution and specifies a value to be returned to the function caller.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_return#examples)

---------------------------------------------------------------------------------------------------------

### [Missing curly braces](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_return#missing_curly_braces)

The curly braces look correct at a first glance, but this code snippet is missing a `{` after the first `if` statement. Correct would be:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_return#see_also)

---------------------------------------------------------------------------------------------------------

*   [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_return/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/bad_return/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/bad_return (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_return&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_return%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_return%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_return%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")