*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#mdn-search)
    

Promise.allKeyed()
==================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#browser_compatibility)
 carefully before using this in production.

The **`Promise.allKeyed()`** static method is like [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
, except that instead of using arrays/iterables as input/output, it uses objects. It takes an object where each own key is associated with a promise, and returns a single [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
. This returned promise fulfills when all of the input's promises fulfill, with an object of the same keys mapped to the corresponding fulfillment values. It rejects when any of the input's promises rejects, with this first rejection reason.

Compared to [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
, `Promise.allKeyed()` allows you to associate results with semantically meaningful keys, instead of arbitrary array ordering which can be difficult to maintain.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#syntax)

-------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#parameters)

[`object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#object)

An object. All of its [own enumerable properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
, whether the key is a string or a symbol, should have [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 values. These values are [awaited](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
, so other [thenables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
 are also resolved, while non-thenables are returned as-is.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#return_value)

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 that is:

*   **Already fulfilled**, if the `object` passed has no own enumerable properties.
*   **Asynchronously fulfilled**, when all the promises in the given `object` fulfill. The fulfillment value is an object of fulfillment values, with the same keys in the same order as the given `object`, regardless of completion order. If the `object` passed is non-empty but contains no pending promises, the returned promise is still asynchronously (instead of synchronously) fulfilled.
*   **Asynchronously rejected**, when any of the promises in the given `object` rejects. The rejection reason is the rejection reason of the first promise that was rejected.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#description)

-----------------------------------------------------------------------------------------------------------------------------

The `Promise.allKeyed()` method is one of the [promise concurrency](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#promise_concurrency)
 methods. It performs the same kind of task as [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
. However, a lot of the times, you don't already have an array of promises and instead just have a few ad-hoc operations to batch up, so you put them in an array and then immediately destructure:

The problem with this is that you need to maintain the consistency of ordering on both sides: if you accidentally write `[resultA, resultC, resultB]`, your code will break.

The keyed method mitigates the problem by associating each async operation with a semantic key:

This way, the ordering no longer matters, and any name mismatch is local: accidentally writing `b: resultC` is now much easier to catch!

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Using Promise.allKeyed()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#using_promise.allkeyed)

The `Promise.allKeyed()` method takes an object and processes all of its own enumerable properties.

For more examples related to concurrency behavior common to `Promise.all()` and `Promise.allKeyed()`, see [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Await Dictionary  <br>\# sec-promise.allkeyed](https://tc39.es/proposal-await-dictionary/#sec-promise.allkeyed) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Promise.allKeyed` in `core-js`](https://core-js.io/docs/features/proposals/await-dictionary "External link (opens in new tab)")
    
*   [es-shims polyfill of `Promise.allKeyed`](https://www.npmjs.com/package/promise.allkeyed "External link (opens in new tab)")
    
*   [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    
*   [`Promise.allSettledKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed)
    
*   [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/allkeyed/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise/allkeyed (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2FallKeyed&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fallkeyed%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2FallKeyed%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fallkeyed%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9fac65196ac2b9a26afabbcb7f14fd58621916ae%0A*+Document+last+modified%3A+2026-09-18T01%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")