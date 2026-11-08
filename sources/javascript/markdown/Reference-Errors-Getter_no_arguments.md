*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments#mdn-search)
    

SyntaxError: getter functions must have no arguments
====================================================

The JavaScript exception "getter functions must have no arguments" occurs when a [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 is declared and the parameter list is non-empty.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments#message)

----------------------------------------------------------------------------------------------------------------

SyntaxError: Getter must not have any formal parameters. (V8-based)
SyntaxError: getter functions must have no arguments (Firefox)
SyntaxError: Unexpected identifier 'x'. getter functions must have no parameters. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments#error_type)

----------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments#what_went_wrong)

---------------------------------------------------------------------------------------------------------------------------------

The [`get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 property syntax looks like a function, but it is stricter and not all function syntax is allowed. A getter is always invoked with no arguments, so defining it with any parameter is likely an error.

Note that this error only applies to property getters using the `get` syntax. If you define the getter using [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
, etc., the getter is defined as a normal function, although it's likely still an error if the getter expects any arguments, as it will be called without any.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments#examples)

------------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments#invalid_cases)

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments#valid_cases)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [`get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Getter_no_arguments/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/getter_no_arguments/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/getter_no_arguments (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FGetter_no_arguments&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fgetter_no_arguments%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FGetter_no_arguments%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fgetter_no_arguments%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")