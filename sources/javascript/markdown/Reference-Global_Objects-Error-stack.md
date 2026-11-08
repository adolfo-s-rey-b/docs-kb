*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack#mdn-search)
    

Error.prototype.stack
=====================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Note:** The `stack` property is de facto implemented by all major JavaScript engines, and [the JavaScript standards committee is looking to standardize it](https://github.com/tc39/proposal-error-stacks "External link (opens in new tab)")
. You cannot rely on the precise content of the stack string due to implementation inconsistencies, but you can generally assume it exists and use it for debugging purposes.

The non-standard **`stack`** property of an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
 instance offers a trace of which functions were called, in what order, from which line and file, and with what arguments. The stack string proceeds from the most recent calls to earlier ones, leading back to the original global scope call.

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack#value)

------------------------------------------------------------------------------------------------------------

A string.

Because the `stack` property is non-standard, implementations differ about where it's installed.

*   In Firefox, it's an accessor property on `Error.prototype`.
*   In Chrome and Safari, it's a data property on each `Error` instance, with the descriptor:

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | no  |
| Configurable | yes |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack#description)

------------------------------------------------------------------------------------------------------------------------

Each JavaScript engine uses its own format for stack traces, but they are fairly consistent in their high-level structure. Every implementation uses a separate line in the stack to represent each function call. The call that directly caused the error is placed at the top, and the call that started the whole call chain is placed at the bottom. Below are some examples of stack traces:

\#### JavaScriptCore
baz@filename.js:10:24
bar@filename.js:6:6
foo@filename.js:2:6
global code@filename.js:13:4

#### SpiderMonkey
baz@filename.js:10:15
bar@filename.js:6:3
foo@filename.js:2:3
@filename.js:13:1

#### V8
Error
    at baz (filename.js:10:15)
    at bar (filename.js:6:3)
    at foo (filename.js:2:3)
    at filename.js:13:1

V8 provides the non-standard [stack trace API](https://v8.dev/docs/stack-trace-api "External link (opens in new tab)")
 for customizing the stack trace, including [`Error.captureStackTrace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace)
, [`Error.stackTraceLimit`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit)
, and `Error.prepareStackTrace()`. Other engines support this API to varying extents.

Different engines set this value at different times. Most modern engines set it when the [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
 object is created. This means you can get the full call stack information within a function using the following:

Without having to throw an error and then catch it.

Stack frames can be things other than explicit function calls, too. For example, event listeners, timeout jobs, and promise handlers all begin their own call chain. Source code within [`eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
 and [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 constructor calls also appear in the stack:

\#### JavaScriptCore
anonymous@
global code@filename.js:1:65
====
eval code@
eval@\[native code\]
global code@filename.js:3:17

#### SpiderMonkey
anonymous@filename.js line 1 > Function:1:8
@filename.js:1:65

====
@filename.js line 3 > eval:1:1
@filename.js:3:13

#### V8
Error: Function failed
    at eval (eval at <anonymous> (filename.js:1:13), <anonymous>:1:8)
    at filename.js:1:65
====
Error: eval failed
    at eval (eval at <anonymous> (filename.js:3:13), <anonymous>:1:1)
    at filename.js:3:13

In Firefox, you can use the `//# sourceURL` directive to name an eval source. See the Firefox [Debug eval sources](https://firefox-source-docs.mozilla.org/devtools-user/debugger/how_to/debug_eval_sources/index.html "External link (opens in new tab)")
 docs.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack#examples)

------------------------------------------------------------------------------------------------------------------

### [Using the stack property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack#using_the_stack_property)

The following script demonstrates how to use the `stack` property to output a stack trace into your browser window. You can use this to check what your browser's stack structure looks like.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack#specifications)

------------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack#see_also)

------------------------------------------------------------------------------------------------------------------

*   [TraceKit](https://github.com/csnover/TraceKit/ "External link (opens in new tab)")
     on GitHub
*   [stacktrace.js](https://github.com/stacktracejs/stacktrace.js "External link (opens in new tab)")
     on GitHub
*   [Stack trace API](https://v8.dev/docs/stack-trace-api "External link (opens in new tab)")
     in the V8 docs

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 19, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/error/stack/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/error/stack (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FError%2Fstack&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ferror%2Fstack%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FError%2Fstack%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ferror%2Fstack%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F30c9f71e6a6cac4d894688cabf7e4b50af87cfe5%0A*+Document+last+modified%3A+2025-07-19T12%3A19%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")