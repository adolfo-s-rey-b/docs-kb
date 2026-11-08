*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#mdn-search)
    

Promise.allSettledKeyed()
=========================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#browser_compatibility)
 carefully before using this in production.

The **`Promise.allSettledKeyed()`** static method is like [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
, except that instead of using arrays/iterables as input/output, it uses objects. It takes an object where each own key is associated with a promise, and returns a single [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
. This returned promise fulfills when all of the input's promises settle, with an object of the same keys mapped to objects that describe the outcome of the corresponding promise.

Compared to [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
, `Promise.allSettledKeyed()` allows you to associate results with semantically meaningful keys, instead of arbitrary array ordering which can be difficult to maintain.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#syntax)

--------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#parameters)

[`object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#object)

An object. All of its [own enumerable properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
, whether the key is a string or a symbol, should have [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 values. These values are [awaited](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
, so other [thenables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
 are also resolved, while non-thenables are returned as-is.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#return_value)

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 that is:

*   **Already fulfilled**, if the `object` passed has no own enumerable properties.
    
*   **Asynchronously fulfilled**, when all promises in the given `object` have settled (either fulfilled or rejected). The fulfillment value is an object, with the same keys in the same order as the given `object`, and each property's value being an object describing the outcome of the corresponding promise in `object`, regardless of completion order. Each outcome object has the following properties:
    
    [`status`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#status)
    
    A string, either `"fulfilled"` or `"rejected"`, indicating the eventual state of the promise.
    
    [`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#value)
    
    Only present if `status` is `"fulfilled"`. The value that the promise was fulfilled with.
    
    [`reason`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#reason)
    
    Only present if `status` is `"rejected"`. The reason that the promise was rejected with.
    
    If the `object` passed is non-empty but contains no pending promises, the returned promise is still asynchronously (instead of synchronously) fulfilled.
    

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#description)

------------------------------------------------------------------------------------------------------------------------------------

The `Promise.allSettledKeyed()` method is one of the [promise concurrency](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#promise_concurrency)
 methods. It performs the same kind of task as [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
. `Promise.allSettledKeyed()` is preferred when you don't already have an array of promises and/or you are immediately destructuring the results; see [`Promise.allKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed)
 for more description.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#examples)

------------------------------------------------------------------------------------------------------------------------------

### [Using Promise.allSettledKeyed()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#using_promise.allsettledkeyed)

The `Promise.allSettledKeyed()` method takes an object and processes all of its own enumerable properties.

For more examples related to concurrency behavior common to `Promise.allSettled()` and `Promise.allSettledKeyed()`, see [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#specifications)

------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Await Dictionary  <br>\# sec-promise.allsettledkeyed](https://tc39.es/proposal-await-dictionary/#sec-promise.allsettledkeyed) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed#see_also)

------------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Promise.allSettledKeyed` in `core-js`](https://core-js.io/docs/features/proposals/await-dictionary "External link (opens in new tab)")
    
*   [es-shims polyfill of `Promise.allSettledKeyed`](https://www.npmjs.com/package/promise.allsettledkeyed "External link (opens in new tab)")
    
*   [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    
*   [`Promise.allKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed)
    
*   [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/allsettledkeyed/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise/allsettledkeyed (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2FallSettledKeyed&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fallsettledkeyed%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2FallSettledKeyed%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fallsettledkeyed%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9fac65196ac2b9a26afabbcb7f14fd58621916ae%0A*+Document+last+modified%3A+2026-09-18T01%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")