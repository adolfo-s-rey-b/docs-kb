*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#mdn-search)
    

Promise.try()
=============

Baseline 2025

Newly available

Since January 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Promise.try()`** static method takes a callback of any kind (returns or throws, synchronously or asynchronously) and [resolves](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
 its result to a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#syntax)

--------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#parameters)

[`func`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#func)

A function that is called synchronously with the arguments provided (`arg1`, `arg2`, …, `argN`). It can do anything—either return a value, throw an error, or return a promise.

[`arg1`, `arg2`, …, `argN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#arg1)

Arguments to pass to `func`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#return_value)

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 that is:

*   Already fulfilled, if `func` synchronously returns a value.
*   Already rejected, if `func` synchronously throws an error.
*   Asynchronously fulfilled or rejected, if `func` returns a promise. The returned value is [resolved](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
     to a promise, which means built-in [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
     objects are returned as-is.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#description)

------------------------------------------------------------------------------------------------------------------------

You may have an API that takes a callback. The callback may be synchronous or asynchronous. You want to handle everything uniformly by wrapping the result in a promise. The most straightforward way might be [`Promise.resolve(func())`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
. The problem is that if `func()` synchronously throws an error, this error would not be caught and turned into a rejected promise.

You can wrap this expression in `try...catch`:

The problem is that `try...catch` is not an expression, so you can't directly use it in expression positions like passing it to other functions.

Therefore, when lifting a function call result into a promise, fulfilled or rejected, people more commonly do this:

For the built-in `Promise()` constructor, errors thrown from the executor are automatically caught and turned into rejections, so this also prevents synchronous errors. The problem is that it unconditionally creates a new `Promise` object, which is unnecessary if `func()` already returns a `Promise`. `Promise.resolve()`, on the other hand, is smart enough to prevent that extra promise wrapping.

`Promise.try()` is almost exactly equivalent to the `try...catch` approach, except that it's shorter and can be used as an expression:

Note that `Promise.try()` is _not_ equivalent to this, despite being highly similar:

The difference is that the callback passed to [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
 is always called asynchronously, while the executor of the `Promise()` constructor is called synchronously. `Promise.try` also calls the function synchronously, and resolves the promise immediately if possible.

`Promise.try()`, combined with [`catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
 and [`finally()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally)
, can be used to handle both synchronous and asynchronous errors in a single chain, and make promise error handling appear almost like synchronous error handling.

Like [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
, `Promise.try()` accepts extra arguments that are passed to the callback. This means instead of doing this:

You can do this:

Which are equivalent, but the latter avoids creating an extra closure and is more efficient.

`Promise.try()` is generic and supports subclassing, which means it can be called on subclasses of `Promise`, and the result will contain a promise of the subclass type. To do so, the subclass's constructor must implement the same signature as the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor — accepting a single `executor` function that can be called with the `resolve` and `reject` callbacks as parameters.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#examples)

------------------------------------------------------------------------------------------------------------------

### [Using Promise.try()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#using_promise.try)

The following example takes a callback, "lifts" it into a promise, handles the result, and does some error handling:

In async/await, the same code would look like this:

### [Calling try() on a non-Promise constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#calling_try_on_a_non-promise_constructor)

`Promise.try()` is a generic method. It can be called on any constructor that implements the same signature as the `Promise()` constructor.

The following is a slightly more faithful approximation of the actual `Promise.try()` (although it should still not be used as a polyfill):

`Promise.try()` delegates to [`Promise.resolve()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
 and [`Promise.reject()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject)
 to create the return value, and both of these functions are generic.

For example, we can call it on a constructor that passes `console.log` as the `resolve` and `reject` functions to `executor`:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-promise.try](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-promise.try) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Promise.try` in `core-js`](https://core-js.io/docs/features/ecmascript/promise "External link (opens in new tab)")
    
*   [es-shims polyfill of `Promise.try`](https://www.npmjs.com/package/promise.try "External link (opens in new tab)")
    
*   [Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
     guide
*   [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    
*   [`Promise()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/try/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise/try (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Ftry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Ftry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Ftry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Ftry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")