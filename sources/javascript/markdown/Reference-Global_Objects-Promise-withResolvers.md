*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#mdn-search)
    

Promise.withResolvers()
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2024.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Promise.withResolvers()`** static method returns an object containing a new [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 object and two functions to resolve or reject it, corresponding to the two parameters passed to the executor of the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#syntax)

------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#return_value)

A plain object containing the following properties:

[`promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#promise)

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 object.

[`resolve`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#resolve)

A function that resolves the promise. For its semantics, see the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor reference.

[`reject`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#reject)

A function that rejects the promise. For its semantics, see the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor reference.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#description)

----------------------------------------------------------------------------------------------------------------------------------

`Promise.withResolvers()` is exactly equivalent to the following code:

Except that it is more concise and does not require the use of [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
.

The key difference when using `Promise.withResolvers()` is that the resolution and rejection functions now live in the same scope as the promise itself, instead of being created and used once within the executor. This may enable some more advanced use cases, such as when reusing them for recurring events, particularly with streams and queues. This also generally results in less nesting than wrapping a lot of logic within the executor.

`Promise.withResolvers()` is generic and supports subclassing, which means it can be called on subclasses of `Promise`, and the result will contain a promise of the subclass type. To do so, the subclass's constructor must implement the same signature as the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor — accepting a single `executor` function that can be called with the `resolve` and `reject` callbacks as parameters.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#examples)

----------------------------------------------------------------------------------------------------------------------------

### [Transforming a stream to an async iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#transforming_a_stream_to_an_async_iterable)

The use case of `Promise.withResolvers()` is when you have a promise that should be resolved or rejected by some event listener that cannot be wrapped inside the promise executor. The following example transforms a Node.js [readable stream](https://nodejs.org/api/stream.html#class-streamreadable "External link (opens in new tab)")
 to an [async iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
. Each `promise` here represents a single batch of data available, and each time the current batch is read, a new promise is created for the next batch. Note how the event listeners are only attached once, but actually call a different version of the `resolve` and `reject` functions each time.

### [Calling withResolvers() on a non-Promise constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#calling_withresolvers_on_a_non-promise_constructor)

`Promise.withResolvers()` is a generic method. It can be called on any constructor that implements the same signature as the `Promise()` constructor. For example, we can call it on a constructor that passes `console.log` as the `resolve` and `reject` functions to `executor`:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#specifications)

----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-promise.withResolvers](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-promise.withResolvers) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Promise.withResolvers` in `core-js`](https://core-js.io/docs/features/ecmascript/promise "External link (opens in new tab)")
    
*   [es-shims polyfill of `Promise.withResolvers`](https://www.npmjs.com/package/promise.withresolvers "External link (opens in new tab)")
    
*   [Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
     guide
*   [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    
*   [`Promise()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/withresolvers/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise/withresolvers (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2FwithResolvers&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fwithresolvers%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2FwithResolvers%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fwithresolvers%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")