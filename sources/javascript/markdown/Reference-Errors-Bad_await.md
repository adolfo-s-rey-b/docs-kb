*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await#mdn-search)
    

SyntaxError: await is only valid in async functions, async generators and modules
=================================================================================

The JavaScript exception "await is only valid in async functions, async generators and modules" occurs when an [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 expression is used outside of [async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
 or [modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
 or other async contexts.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await#message)

------------------------------------------------------------------------------------------------------

SyntaxError: await is only valid in async functions and the top level bodies of modules (V8-based)
SyntaxError: await is only valid in async functions, async generators and modules (Firefox)
SyntaxError: Unexpected identifier (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await#error_type)

------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------

JavaScript execution is never blocking: an `await` can never block the execution of the program. Instead, it pauses the execution of the surrounding async task, while allowing other tasks to continue running. Therefore, `await` cannot be used in sync tasks, such as functions, generator functions, or top level of scripts. It is not always apparent whether the current file is a script or a module — see the [Modules guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#top-level_await)
 for more information.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await#examples)

--------------------------------------------------------------------------------------------------------

### [Top-level await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await#top-level_await)

You cannot use `await` at the top level of a script:

Instead, make the script a module:

### [Async callbacks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await#async_callbacks)

You cannot use `await` in a sync callback:

Instead, make the callback async. See more explanation in the [Using promises guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#composition)
.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await#see_also)

--------------------------------------------------------------------------------------------------------

*   [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_await/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/bad_await/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/bad_await (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_await&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_await%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBad_await%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbad_await%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")