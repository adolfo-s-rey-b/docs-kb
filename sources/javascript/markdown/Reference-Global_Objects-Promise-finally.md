*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#mdn-search)
    

Promise.prototype.finally()
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`finally()`** method of [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 instances schedules a function to be called when the promise is settled (either fulfilled or rejected). It immediately returns another [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 object, allowing you to [chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#chaining)
 calls to other promise methods.

Like the [`finally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#the_finally_block)
 block, this method is usually intended for cleanup actions, regardless of the promise's outcome. It lets you avoid duplicating code in both the promise's [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
 and [`catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
 handlers.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#try_it)

------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#syntax)

------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#parameters)

[`onFinally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#onfinally)

A function to asynchronously execute when this promise becomes settled. If the function returns a promise, the resulting promise will wait for that promise to settle before continuing. If the returned promise is rejected, the resulting promise is rejected with the same reason. Any other returned value, or the fulfilled value of the returned promise, is ignored.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#return_value)

Returns a new [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 immediately. This new promise is always pending when returned, regardless of the current promise's status. If `onFinally` throws an error or returns a rejected promise, the new promise will reject with that value. Otherwise, the new promise will settle with the same state as the current promise.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#description)

----------------------------------------------------------------------------------------------------------------------------

The `finally()` method can be useful if you want to do some processing or cleanup once the promise is settled, regardless of its outcome.

The `finally()` method is very similar to calling [`then(onFinally, onFinally)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
. However, there are a couple of differences:

*   When creating a function inline, you can pass it once, instead of being forced to either declare it twice, or create a variable for it.
*   The `onFinally` callback does not receive any argument. This use case is for precisely when you _do not care_ about the rejection reason or the fulfillment value, and so there's no need to provide it.
*   A `finally()` call is usually transparent and reflects the eventual state of the original promise. So for example:
    *   Unlike `Promise.resolve(2).then(() => 77, () => 77)`, which returns a promise eventually fulfilled with the value `77`, `Promise.resolve(2).finally(() => 77)` returns a promise eventually fulfilled with the value `2`.
    *   Similarly, unlike `Promise.reject(3).then(() => 88, () => 88)`, which returns a promise eventually fulfilled with the value `88`, `Promise.reject(3).finally(() => 88)` returns a promise eventually rejected with the reason `3`.

**Note:** A `throw` (or returning a rejected promise) in the `finally` callback still rejects the returned promise. For example, both `Promise.reject(3).finally(() => { throw 99; })` and `Promise.reject(3).finally(() => Promise.reject(99))` reject the returned promise with the reason `99`.

Like [`catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
, `finally()` internally calls the `then` method on the object upon which it was called. If `onFinally` is not a function, `then()` is called with `onFinally` as both arguments — which, for [`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
, means that no useful handler is attached. Otherwise, `then()` is called with two internally created functions, which behave like the following:

**Warning:** This is only for demonstration purposes and is not a polyfill.

Because `finally()` calls `then()`, it supports subclassing. Moreover, notice the [`Promise.resolve()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
 call above — in reality, `onFinally()`'s return value is resolved using the same algorithm as `Promise.resolve()`, but the actual constructor used to construct the resolved promise will be the subclass. `finally()` gets this constructor through [`promise.constructor[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Symbol.species)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#examples)

----------------------------------------------------------------------------------------------------------------------

### [Using finally()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#using_finally)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-promise.prototype.finally](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-promise.prototype.finally) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Promise.prototype.finally` in `core-js`](https://core-js.io/docs/features/ecmascript/promise "External link (opens in new tab)")
    
*   [es-shims polyfill of `Promise.prototype.finally`](https://www.npmjs.com/package/promise.prototype.finally "External link (opens in new tab)")
    
*   [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    
*   [`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
    
*   [`Promise.prototype.catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/finally/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise/finally (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Ffinally&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Ffinally%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Ffinally%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Ffinally%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")