*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#mdn-search)
    

Promise.all()
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Promise.all()`** static method takes an iterable of promises as input and returns a single [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
. This returned promise fulfills when all of the input's promises fulfill (including when an empty iterable is passed), with an array of the fulfillment values. It rejects when any of the input's promises rejects, with this first rejection reason.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#try_it)

--------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#syntax)

--------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#parameters)

[`iterable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#iterable)

An [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 (such as an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
) of promises. These values are [awaited](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
, so other [thenables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
 are also resolved, while non-thenables are returned as-is.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#return_value)

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 that is:

*   **Already fulfilled**, if the `iterable` passed is empty.
*   **Asynchronously fulfilled**, when all the promises in the given `iterable` fulfill. The fulfillment value is an array of fulfillment values, in the order of the promises passed, regardless of completion order. If the `iterable` passed is non-empty but contains no pending promises, the returned promise is still asynchronously (instead of synchronously) fulfilled.
*   **Asynchronously rejected**, when any of the promises in the given `iterable` rejects. The rejection reason is the rejection reason of the first promise that was rejected.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#description)

------------------------------------------------------------------------------------------------------------------------

The `Promise.all()` method is one of the [promise concurrency](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#promise_concurrency)
 methods. It can be useful for aggregating the results of multiple promises. It is typically used when there are multiple related asynchronous tasks that the overall code relies on to work successfully — all of whom we want to fulfill before the code execution continues.

`Promise.all()` will reject immediately upon **any** of the input promises rejecting. In comparison, the promise returned by [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
 will wait for all input promises to complete, regardless of whether or not one rejects. Use `allSettled()` if you need the final result of every promise in the input iterable.

Like other promise combinators, `Promise.all()` immediately marks all promises as "handled" when it is called (by calling their `.then()` methods). Subsequent rejections after the first rejection will be ignored, and will not trigger any `unhandledrejection` events.

Rejecting the returned promise does not cancel the remaining operations or unsubscribe the handlers attached to their promises. Repeatedly passing a long-lived pending promise to `Promise.all()` can accumulate handlers on that promise even when another input rejects each time.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#examples)

------------------------------------------------------------------------------------------------------------------

### [Using Promise.all()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#using_promise.all)

`Promise.all` waits for all fulfillments (or the first rejection).

If the `iterable` contains non-promise values, they will be ignored, but still counted in the returned promise array value (if the promise is fulfilled):

### [Destructuring the result](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#destructuring_the_result)

You will find [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 very useful if you are batching together a known number of tasks.

Be careful: if the original promises and the result variables' order don't match, you may run into subtle bugs. The [`Promise.allKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed)
 method solves exactly this problem.

### [Asynchronicity or synchronicity of Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#asynchronicity_or_synchronicity_of_promise.all)

This following example demonstrates the asynchronicity of `Promise.all` when a non-empty `iterable` is passed:

The same thing happens if `Promise.all` rejects:

`Promise.all` resolves synchronously if and only if the `iterable` passed is empty:

### [Using Promise.all() with async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#using_promise.all_with_async_functions)

Within [async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
, it's very common to "over-await" your code. For example, given the following functions:

You may write a function like this:

However, note that the execution of `promptForDishChoice` and `fetchPrices` don't depend on the result of each other. While the user is choosing their dish, it's fine for the prices to be fetched in the background, but in the code above, the [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 operator causes the async function to pause until the choice is made, and then again until the prices are fetched. We can use `Promise.all` to run them concurrently, so that the user doesn't have to wait for the prices to be fetched before the result is given:

`Promise.all` is the best choice of [concurrency method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#promise_concurrency)
 here, because error handling is intuitive — if any of the promises reject, the result is no longer available, so the whole `await` expression throws.

`Promise.all` accepts an iterable of promises, so if you are using it to run several async functions concurrently, you need to call the async functions and use the returned promises. Directly passing the functions to `Promise.all` does not work, since they are not promises.

Note that the following, despite other undesirable aspects (like creating more variables and bug-prone error handling), also achieves concurrency:

### [Promise.all fail-fast behavior](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#promise.all_fail-fast_behavior)

`Promise.all` is rejected if any of the elements are rejected. For example, if you pass in four promises that resolve after a timeout and one promise that rejects immediately, then `Promise.all` will reject immediately.

It is possible to change this behavior by handling possible rejections:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-promise.all](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-promise.all) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    
*   [`Promise.allKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed)
    
*   [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
    
*   [`Promise.any()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any)
    
*   [`Promise.race()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/all/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise/all (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fall&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fall%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fall%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fall%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9bda33365e40b6c609fa5190a0af9b5dc6438cf0%0A*+Document+last+modified%3A+2026-09-01T23%3A23%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")