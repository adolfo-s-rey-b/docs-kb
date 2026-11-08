*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#mdn-search)
    

Promise.race()
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Promise.race()`** static method takes an iterable of promises as input and returns a single [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
. This returned promise settles with the eventual state of the first promise that settles.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#try_it)

---------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#syntax)

---------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#parameters)

[`iterable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#iterable)

An [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 (such as an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
) of promises. These values are [awaited](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
, so other [thenables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
 are also resolved, while non-thenables are returned as-is.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#return_value)

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 that **asynchronously settles** with the eventual state of the first promise in the `iterable` to settle. In other words, it fulfills if the first promise to settle is fulfilled, and rejects if the first promise to settle is rejected. The returned promise remains pending forever if the `iterable` passed is empty. If the `iterable` passed is non-empty but contains no pending promises, the returned promise is still asynchronously (instead of synchronously) settled.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#description)

-------------------------------------------------------------------------------------------------------------------------

The `Promise.race()` method is one of the [promise concurrency](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#promise_concurrency)
 methods. It's useful when you want the first async task to complete, but do not care about its eventual state (i.e., it can either succeed or fail).

If the iterable contains one or more non-promise values and/or an already settled promise, then `Promise.race()` will settle to the first of these values found in the iterable.

Like other promise combinators, `Promise.race()` immediately marks all promises as "handled" when it is called (by calling their `.then()` methods). Subsequent rejections after the first settlement will be ignored, and will not trigger any `unhandledrejection` events.

Settling the returned promise does not cancel the losing operations or unsubscribe the handlers attached to their promises. If you repeatedly race a long-lived pending promise against short-lived promises, handlers can accumulate on the pending promise even after each race settles.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#examples)

-------------------------------------------------------------------------------------------------------------------

### [Using Promise.race()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#using_promise.race)

This example shows how `Promise.race()` can be used to race several timers implemented with [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
. The timer with the shortest time always wins the race and becomes the resulting promise's state.

### [Asynchronicity of Promise.race](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#asynchronicity_of_promise.race)

This following example demonstrates the asynchronicity of `Promise.race`. Unlike other promise concurrency methods, `Promise.race` is always asynchronous: it never settles synchronously, even when the `iterable` is empty.

An empty iterable causes the returned promise to be forever pending:

If the iterable contains one or more non-promise value and/or an already settled promise, then `Promise.race` will settle to the first of these values found in the array:

### [Using Promise.race() to implement request timeout](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#using_promise.race_to_implement_request_timeout)

You can race a potentially long-lasting request with a timer that rejects, so that when the time limit has elapsed, the resulting promise automatically rejects.

If the `data` promise fulfills, it will contain the data fetched from `/api`. `Promise.race` will capture and discard the settlement results of the losing promises, so the `"Request timed out"` rejection will not bubble up as unhandled. Otherwise, if `fetch` remains pending for 5 seconds and loses the race with the `setTimeout` timer, the final promise will reject.

One promise finishing does not automatically cancel the other; the other's result is simply ignored. This does not pose problems in this small example, but it keeps resources such as network connections and timers alive for longer than necessary. To release resources early, abort the fetch if the timeout wins, or clear the timeout if the fetch wins. Whenever possible—including fetch—prefer using the [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
 API instead.

### [Using Promise.race() to detect the status of a promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#using_promise.race_to_detect_the_status_of_a_promise)

Because `Promise.race()` resolves to the first non-pending promise in the iterable, we can check a promise's state, including if it's pending. This example is adapted from [`promise-status-async`](https://github.com/kudla/promise-status-async/blob/master/lib/promiseState.js "External link (opens in new tab)")
.

In this function, if `promise` is pending, the second value, `pendingState`, which is a non-promise, becomes the result of the race; otherwise, if `promise` is already settled, we may know its state through the `onFulfilled` and `onRejected` handlers. For example:

**Note:** The `promiseState` function still runs asynchronously, because there is no way to synchronously get a promise's value (i.e., without `then()` or `await`), even when it is already settled. However, `promiseState()` always fulfills within one tick and never actually waits for any promise's settlement.

### [Comparison with Promise.any()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#comparison_with_promise.any)

`Promise.race` takes the first settled [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
.

[`Promise.any`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any)
 takes the first fulfilled [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-promise.race](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-promise.race) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    
*   [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
    
*   [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
    
*   [`Promise.any()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/race/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise/race (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Frace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Frace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Frace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Frace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9bda33365e40b6c609fa5190a0af9b5dc6438cf0%0A*+Document+last+modified%3A+2026-09-01T23%3A23%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")