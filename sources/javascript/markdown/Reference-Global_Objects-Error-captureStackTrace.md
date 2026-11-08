*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#mdn-search)
    

Error.captureStackTrace()
=========================

The **`Error.captureStackTrace()`** static method installs stack trace information on a provided object as the [`stack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack)
 property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#syntax)

--------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#parameters)

[`object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#object)

The object on which to add the `stack` property.

[`constructor` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#constructor)

A function, typically the constructor where the `object` was created. When collecting the stack trace, all frames above the topmost call to this function, including that call, are left out of the stack trace.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#return_value)

None ([`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
).

The `object` is modified in-place with an extra own property called `stack` defined, whose string value follows the same format as [`Error.prototype.stack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack)
. This property is non-enumerable and configurable. In V8, it is a getter-setter pair. In SpiderMonkey and JavaScriptCore, it is a data property that is writable.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#examples)

------------------------------------------------------------------------------------------------------------------------------

### [Using Error.captureStackTrace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#using_error.capturestacktrace)

The `getStack()` utility function returns the current stack trace at the point it is called, removing itself from the stack. This serves the same debugging purpose as [`console.trace()`](https://developer.mozilla.org/en-US/docs/Web/API/console/trace_static)
, but allows you to output the string elsewhere. Note that it does not construct an `Error` instance for this purpose, but installs `stack` on a plain object, which would be more efficient for our purposes. Normally, you would call `Error.captureStackTrace` on objects intended to be thrown as errors, as shown in the next example.

### [Installing stack trace on a custom error object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#installing_stack_trace_on_a_custom_error_object)

The main use case for `Error.captureStackTrace()` is to install a stack trace on a custom error object. Typically, you define [custom errors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#custom_error_types)
 by extending the `Error` class, which automatically makes the `stack` property available via inheritance. However, the problem with the default stack trace is that it includes the constructor call itself, which leaks implementation details. You can avoid this by using `Error.captureStackTrace()`, which allows the stack trace to be installed even for custom errors that do not inherit from `Error`.

Note that even if you don't call `Error.captureStackTrace()` here, some engines are still smart enough to avoid `MyError` in the stack trace if the constructor inherits from `Error`. Calling `Error.captureStackTrace()` is more important for custom errors that, for some reason, do not inherit from `Error`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#specifications)

------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Unknown specification  <br>\# errorcapturestacktrace-1](https://github.com/tc39/proposal-error-capturestacktrace?tab=readme-ov-file#errorcapturestacktrace-1) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace#see_also)

------------------------------------------------------------------------------------------------------------------------------

*   [`Error.prototype.stack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack)
    
*   [`Error.stackTraceLimit`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit)
    
*   [Stack trace API](https://v8.dev/docs/stack-trace-api "External link (opens in new tab)")
     in the V8 docs

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/error/capturestacktrace/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/error/capturestacktrace (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FError%2FcaptureStackTrace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ferror%2Fcapturestacktrace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FError%2FcaptureStackTrace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ferror%2Fcapturestacktrace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")