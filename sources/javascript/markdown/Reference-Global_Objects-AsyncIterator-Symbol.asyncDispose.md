*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#mdn-search)
    

AsyncIterator.prototype\[Symbol.asyncDispose\]()
================================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/366)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`[Symbol.asyncDispose]()`** method of [`AsyncIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)
 instances implements the _async disposable protocol_ and allows it to be disposed when used with [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
. It calls and awaits the `return()` method of `this`, if it exists.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#syntax)

------------------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#return_value)

None ([`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#examples)

----------------------------------------------------------------------------------------------------------------------------------------

### [Declaring an async iterator with `await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#declaring_an_async_iterator_with_await_using)

The `Symbol.asyncDispose` method is intended to be automatically called in an `await using` declaration. This is useful if you have an async iterator that you manually iterate over by calling its `next()` method; if you iterate it with [`for await...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
 or something similar, then error handling and cleanup is done automatically.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#specifications)

----------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript Async Explicit Resource Management  <br>\# sec-asyncdisposablestack.prototype-@@asyncDispose](https://tc39.es/proposal-async-explicit-resource-management/#sec-asyncdisposablestack.prototype-@@asyncDispose) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose#see_also)

----------------------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `AsyncIterator.prototype[Symbol.asyncDispose]` in `core-js`](https://core-js.io/docs/features/ecmascript/explicit-resource-management "External link (opens in new tab)")
    
*   [JavaScript resource management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management)
    
*   [`Symbol.asyncDispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncDispose)
    
*   [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator/Symbol.asyncDispose/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/asynciterator/symbol.asyncdispose/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/asynciterator/symbol.asyncdispose (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAsyncIterator%2FSymbol.asyncDispose&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fasynciterator%2Fsymbol.asyncdispose%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAsyncIterator%2FSymbol.asyncDispose%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fasynciterator%2Fsymbol.asyncdispose%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")