*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit#mdn-search)
    

Error.stackTraceLimit
=====================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Note:** This feature is part of the currently non-standard [V8 stack trace API](https://v8.dev/docs/stack-trace-api "External link (opens in new tab)")
. However, for compatibility reasons, it is also implemented by JavaScriptCore.

The **`Error.stackTraceLimit`** static data property indicates the maximum number of stack frames captured by the stack trace of an error. It can be set by user code to change the engine's behavior.

Generally, _reading_ this property is not very useful, but you can _set_ it to a new value. Setting it to a larger value can be useful for debugging, as it allows you to see more of the call stack. Setting it to a smaller value can improve performance as it reduces the amount of stack captured.

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit#value)

----------------------------------------------------------------------------------------------------------------------

An integer representing the maximum number of stack frames captured by the stack trace of an error.

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | yes |
| Configurable | yes |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit#description)

----------------------------------------------------------------------------------------------------------------------------------

Because `stackTraceLimit` is a static property of `Error`, you always use it as `Error.stackTraceLimit`, rather than as a property of an `Error` object you created. If you want to customize the stack trace for a single error only, you may need to set the property, create the error, and then reset the property to its original value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit#examples)

----------------------------------------------------------------------------------------------------------------------------

### [Setting Error.stackTraceLimit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit#setting_error.stacktracelimit)

This code is safe to run even in environments that don't support `Error.stackTraceLimit`, because it doesn't read the property, only sets it, and engines that don't support it will ignore the setting.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit#specifications)

----------------------------------------------------------------------------------------------------------------------------------------

This feature does not appear to be defined in any specification.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [`Error.prototype.stack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack)
    
*   [`Error.captureStackTrace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/captureStackTrace)
    
*   [Stack trace API](https://v8.dev/docs/stack-trace-api "External link (opens in new tab)")
     in the V8 docs

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stackTraceLimit/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/error/stacktracelimit/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/error/stacktracelimit (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FError%2FstackTraceLimit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ferror%2Fstacktracelimit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FError%2FstackTraceLimit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ferror%2Fstacktracelimit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")