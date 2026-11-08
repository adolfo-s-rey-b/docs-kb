*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#mdn-search)
    

Promise() constructor
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Promise()`** constructor creates [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 objects. It is primarily used to wrap callback-based APIs that do not already support promises.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#try_it)

------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#syntax)

------------------------------------------------------------------------------------------------------------------

**Note:** `Promise()` can only be constructed with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. Attempting to call it without `new` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#parameters)

[`executor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#executor)

A [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 to be executed by the constructor. It receives two functions as parameters: `resolveFunc` and `rejectFunc`. Any errors thrown in the `executor` will cause the promise to be rejected, and the return value will be neglected. The semantics of `executor` are detailed below.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#return_value)

When called via `new`, the `Promise` constructor returns a promise object. The promise object will become _resolved_ when either of the functions `resolveFunc` or `rejectFunc` are invoked. Note that if you call `resolveFunc` and pass another promise object as an argument, the initial promise can be said to be "resolved", but still not "settled". See the [Promise description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#description)
 for more explanation.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#description)

----------------------------------------------------------------------------------------------------------------------------

Traditionally (before promises), asynchronous tasks were designed as callbacks.

To take advantage of the readability improvement and language features offered by promises, the `Promise()` constructor allows one to transform the callback-based API to a promise-based one.

**Note:** If your task is already promise-based, you likely do not need the `Promise()` constructor.

The `executor` is custom code that ties an outcome in a callback to a promise. You, the programmer, write the `executor`. Its signature is expected to be:

`resolveFunc` and `rejectFunc` are also functions, and you can give them whatever actual names you want. Their signatures are simple: they accept a single parameter of any type.

The `value` parameter passed to `resolveFunc` can be another promise object, in which case the newly constructed promise's state will be "locked in" to the promise passed (as part of the [resolution](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#the_resolve_function)
 promise). The `rejectFunc` has semantics close to the [`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
 statement, so `reason` is typically an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
 instance. If either `value` or `reason` is omitted, the promise is fulfilled/rejected with `undefined`.

The `executor`'s completion state has limited effect on the promise's state:

*   The `executor` return value is ignored. `return` statements within the `executor` merely impact control flow and alter whether a part of the function is executed, but do not have any impact on the promise's fulfillment value. If `executor` exits and it's impossible for `resolveFunc` or `rejectFunc` to be called in the future (for example, there are no async tasks scheduled), then the promise remains pending forever.
*   If an error is thrown in the `executor`, the promise is rejected, unless `resolveFunc` or `rejectFunc` has already been called.

**Note:** The existence of pending promises does not prevent the program from exiting. If the event loop is empty, the program exits despite any pending promises (because those are necessarily forever-pending).

Here's a summary of the typical flow:

1.  At the time when the constructor generates the new `Promise` object, it also generates a corresponding pair of functions for `resolveFunc` and `rejectFunc`; these are "tethered" to the `Promise` object.
2.  `executor` typically wraps some asynchronous operation which provides a callback-based API. The callback (the one passed to the original callback-based API) is defined within the `executor` code, so it has access to the `resolveFunc` and `rejectFunc`.
3.  The `executor` is called synchronously (as soon as the `Promise` is constructed) with the `resolveFunc` and `rejectFunc` functions as arguments.
4.  The code within the `executor` has the opportunity to perform some operation. The eventual completion of the asynchronous task is communicated with the promise instance via the side effect caused by `resolveFunc` or `rejectFunc`. The side effect is that the `Promise` object becomes "resolved".
    *   If `resolveFunc` is called first, the value passed will be [resolved](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#the_resolve_function)
        . The promise may stay pending (in case another [thenable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
         is passed), become fulfilled (in most cases where a non-thenable value is passed), or become rejected (in case of an invalid resolution value).
    *   If `rejectFunc` is called first, the promise instantly becomes rejected.
    *   Once one of the resolving functions (`resolveFunc` or `rejectFunc`) is called, the promise stays resolved. Only the first call to `resolveFunc` or `rejectFunc` affects the promise's eventual state, and subsequent calls to either function can neither change the fulfillment value/rejection reason nor toggle its eventual state from "fulfilled" to "rejected" or opposite.
    *   If `executor` exits by throwing an error, then the promise is rejected. However, the error is ignored if one of the resolving functions has already been called (so that the promise is already resolved).
    *   Resolving the promise does not necessarily cause the promise to become fulfilled or rejected (i.e., settled). The promise may still be pending because it's resolved with another thenable, but its eventual state will match that of the resolved thenable.
5.  Once the promise settles, it (asynchronously) invokes any further handlers associated through [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
    , [`catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
    , or [`finally()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally)
    . The eventual fulfillment value or rejection reason is passed to the invocation of fulfillment and rejection handlers as an input parameter (see [Chained Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#chained_promises)
    ).

For example, the callback-based `readFile` API above can be transformed into a promise-based one.

The `resolve` and `reject` callbacks are only available within the scope of the executor function, which means you can't access them after the promise is constructed. If you want to construct the promise before deciding how to resolve it, you can use the [`Promise.withResolvers()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers)
 method instead, which exposes the `resolve` and `reject` functions.

### [The resolve function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#the_resolve_function)

The `resolve` function has the following behaviors:

*   If it's called with the same value as the newly created promise (the promise it's "tethered to"), the promise is rejected with a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
    .
*   If it's called with a non-[thenable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
     value (a primitive, or an object whose `then` property is not callable, including when the property is not present), the promise is immediately fulfilled with that value.
*   If it's called with a thenable value (including another `Promise` instance), then the thenable's `then` method is saved and called in the future (it's always called asynchronously). The `then` method will be called with two callbacks, which are two new functions with the exact same behaviors as the `resolveFunc` and `rejectFunc` passed to the `executor` function. If calling the `then` method throws, then the current promise is rejected with the thrown error.

In the last case, it means code like:

Is roughly equivalent to:

Except that in the `resolve(thenable)` case:

1.  `resolve` is called synchronously, so that calling `resolve` or `reject` again has no effect, even when the handlers attached through `anotherPromise.then()` are not called yet.
2.  The `then` method is called asynchronously, so that the promise will never be instantly resolved if a thenable is passed.

Because `resolve` is called again with whatever `thenable.then()` passes to it as `value`, the resolver function is able to flatten nested thenables, where a thenable calls its `onFulfilled` handler with another thenable. The effect is that the fulfillment handler of a real promise will never receive a thenable as its fulfillment value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#examples)

----------------------------------------------------------------------------------------------------------------------

### [Turning a callback-based API into a promise-based one](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#turning_a_callback-based_api_into_a_promise-based_one)

To provide a function with promise functionality, have it return a promise by calling the `resolve` and `reject` functions at the correct times.

### [Effect of calling resolveFunc](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#effect_of_calling_resolvefunc)

Calling `resolveFunc` causes the promise to become resolved, so that calling `resolveFunc` or `rejectFunc` again has no effect. However, the promise may be in any of the states: pending, fulfilled, or rejected.

This `pendingResolved` promise is resolved the time it's created, because it has already been "locked in" to match the eventual state of the inner promise, and calling `resolveOuter` or `rejectOuter` or throwing an error later in the executor has no effect on its eventual state. However, the inner promise is still pending until 100ms later, so the outer promise is also pending:

This `fulfilledResolved` promise becomes fulfilled the moment it's resolved, because it's resolved with a non-thenable value. However, when it's created, it's unresolved, because neither `resolve` nor `reject` has been called yet. An unresolved promise is necessarily pending:

Calling `rejectFunc` obviously causes the promise to reject. However, there are also two ways to cause the promise to instantly become rejected even when the `resolveFunc` callback is called.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-promise-constructor](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-promise-constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Promise` in `core-js`](https://core-js.io/docs/features/ecmascript/promise "External link (opens in new tab)")
    
*   [Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
     guide
*   [`Promise.withResolvers()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/promise/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise/promise (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2FPromise&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fpromise%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2FPromise%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fpromise%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")