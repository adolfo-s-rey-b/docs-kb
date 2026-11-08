*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#mdn-search)
    

Using promises
==============

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
    

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 is an object representing the eventual completion or failure of an asynchronous operation. Since most people are consumers of already-created promises, this guide will explain consumption of returned promises before explaining how to create them.

Essentially, a promise is a returned object to which you attach callbacks, instead of passing callbacks into a function. Imagine a function, `createAudioFileAsync()`, which asynchronously generates a sound file given a configuration record and two callback functions: one called if the audio file is successfully created, and the other called if an error occurs.

Here's some code that uses `createAudioFileAsync()`:

If `createAudioFileAsync()` were rewritten to return a promise, you would attach your callbacks to it instead:

This convention has several advantages. We will explore each one.

[Chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#chaining)

--------------------------------------------------------------------------------------------------

A common need is to execute two or more asynchronous operations back to back, where each subsequent operation starts when the previous operation succeeds, with the result from the previous step. In the old days, doing several asynchronous operations in a row would lead to the classic [callback hell](https://medium.com/@raihan_tazdid/callback-hell-in-javascript-all-you-need-to-know-296f7f5d3c1 "External link (opens in new tab)")
:

With promises, we accomplish this by creating a promise chain. The API design of promises makes this great, because callbacks are attached to the returned promise object, instead of being passed into a function.

Here's the magic: the `then()` function returns a **new promise**, different from the original:

This second promise (`promise2`) represents the completion not just of `doSomething()`, but also of the `successCallback` or `failureCallback` you passed in — which can be other asynchronous functions returning a promise. When that's the case, any callbacks added to `promise2` get queued behind the promise returned by either `successCallback` or `failureCallback`.

**Note:** If you want a working example to play with, you can use the following template to create any function returning a promise:

The implementation is discussed in the [Creating a Promise around an old callback API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#creating_a_promise_around_an_old_callback_api)
 section below.

With this pattern, you can create longer chains of processing, where each promise represents the completion of one asynchronous step in the chain. In addition, the arguments to `then` are optional, and `catch(failureCallback)` is short for `then(null, failureCallback)` — so if your error handling code is the same for all steps, you can attach it to the end of the chain:

You might see this expressed with [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 instead:

**Note:** Arrow function expressions can have an [implicit return](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#function_body)
; so, `() => x` is short for `() => { return x; }`.

`doSomethingElse` and `doThirdThing` can return any value — if they return promises, that promise is first waited until it settles, and the next callback receives the fulfillment value, not the promise itself. It is important to always return promises from `then` callbacks, even if the promise always resolves to `undefined`. If the previous handler started a promise but did not return it, there's no way to track its settlement anymore, and the promise is said to be "floating".

By returning the result of the `fetch` call (which is a promise), we can both track its completion and receive its value when it completes.

Floating promises could be worse if you have race conditions — if the promise from the last handler is not returned, the next `then` handler will be called early, and any value it reads may be incomplete.

Therefore, as a rule of thumb, whenever your operation encounters a promise, return it and defer its handling to the next `then` handler.

Even better, you can flatten the nested chain into a single chain, which is simpler and makes error handling easier. The details are discussed in the [Nesting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#nesting)
 section below.

Using [`async`/`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
 can help you write code that's more intuitive and resembles synchronous code. Below is the same example using `async`/`await`:

Note how the code looks exactly like synchronous code, except for the `await` keywords in front of promises. One of the only tradeoffs is that it may be easy to forget the [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
 keyword, which can only be fixed when there's a type mismatch (e.g., trying to use a promise as a value).

`async`/`await` builds on promises — for example, `doSomething()` is the same function as before, so there's minimal refactoring needed to change from promises to `async`/`await`. You can read more about the `async`/`await` syntax in the [async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
 and [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 references.

**Note:** `async`/`await` has the same concurrency semantics as normal promise chains. `await` within one async function does not stop the entire program, only the parts that depend on its value, so other async jobs can still run while the `await` is pending.

[Error handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#error_handling)

--------------------------------------------------------------------------------------------------------------

You might recall seeing `failureCallback` three times in the pyramid of doom earlier, compared to only once at the end of the promise chain:

If there's an exception, the browser will look down the chain for `.catch()` handlers or `onRejected`. This is very much modeled after how synchronous code works:

This symmetry with asynchronous code culminates in the `async`/`await` syntax:

Promises solve a fundamental flaw with the callback pyramid of doom, by catching all errors, even thrown exceptions and programming errors. This is essential for functional composition of asynchronous operations. All errors are now handled by the [`catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
 method at the end of the chain, and you should almost never need to use `try`/`catch` without using `async`/`await`.

### [Nesting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#nesting)

In the examples above involving `listOfIngredients`, the first one has one promise chain nested in the return value of another `then()` handler, while the second one uses an entirely flat chain. Simple promise chains are best kept flat without nesting, as nesting can be a result of careless composition.

Nesting is a control structure to limit the scope of `catch` statements. Specifically, a nested `catch` only catches failures in its scope and below, not errors higher up in the chain outside the nested scope. When used correctly, this gives greater precision in error recovery:

Note that the optional steps here are nested — with the nesting caused not by the indentation, but by the placement of the outer `(` and `)` parentheses around the steps.

The inner error-silencing `catch` handler only catches failures from `doSomethingOptional()` and `doSomethingExtraNice()`, after which the code resumes with `moreCriticalStuff()`. Importantly, if `doSomethingCritical()` fails, its error is caught by the final (outer) `catch` only, and does not get swallowed by the inner `catch` handler.

In `async`/`await`, this code looks like:

**Note:** If you don't have sophisticated error handling, you very likely don't need nested `then` handlers. Instead, use a flat chain and put the error handling logic at the end.

### [Chaining after a catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#chaining_after_a_catch)

It's possible to chain _after_ a failure, i.e., a `catch`, which is useful to accomplish new actions even after an action failed in the chain. Read the following example:

This will output the following text:

Do that
Do this, no matter what happened before

**Note:** The text "Do this" is not displayed because the "Something failed" error caused a rejection.

In `async`/`await`, this code looks like:

### [Promise rejection events](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#promise_rejection_events)

If a promise rejection event is not handled by any handler, it bubbles to the top of the call stack, and the host needs to surface it. On the web, whenever a promise is rejected, one of two events is sent to the global scope (generally, this is either the [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 or, if being used in a web worker, it's the [`Worker`](https://developer.mozilla.org/en-US/docs/Web/API/Worker)
 or other worker-based interface). The two events are:

[`unhandledrejection`](https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event)

Sent when a promise is rejected but there is no rejection handler available.

[`rejectionhandled`](https://developer.mozilla.org/en-US/docs/Web/API/Window/rejectionhandled_event)

Sent when a handler is attached to a rejected promise that has already caused an `unhandledrejection` event.

In both cases, the event (of type [`PromiseRejectionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/PromiseRejectionEvent)
) has as members a [`promise`](https://developer.mozilla.org/en-US/docs/Web/API/PromiseRejectionEvent/promise)
 property indicating the promise that was rejected, and a [`reason`](https://developer.mozilla.org/en-US/docs/Web/API/PromiseRejectionEvent/reason)
 property that provides the reason given for the promise to be rejected.

These make it possible to offer fallback error handling for promises, as well as to help debug issues with your promise management. These handlers are global per context, so all errors will go to the same event handlers, regardless of source.

In [Node.js](https://developer.mozilla.org/en-US/docs/Glossary/Node.js)
, handling promise rejection is slightly different. You capture unhandled rejections by adding a handler for the Node.js `unhandledRejection` event (notice the difference in capitalization of the name), like this:

For Node.js, to prevent the error from being logged to the console (the default action that would otherwise occur), adding that `process.on()` listener is all that's necessary; there's no need for an equivalent of the browser runtime's [`preventDefault()`](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)
 method.

However, if you add that `process.on` listener but don't also have code within it to handle rejected promises, they will just be dropped on the floor and silently ignored. So ideally, you should add code within that listener to examine each rejected promise and make sure it was not caused by an actual code bug.

[Composition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#composition)

--------------------------------------------------------------------------------------------------------

There are four [composition tools](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#promise_concurrency)
 for running asynchronous operations concurrently: [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
, [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
, [`Promise.any()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any)
, and [`Promise.race()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)
.

We can start operations at the same time and wait for them all to finish like this:

If one of the promises in the array rejects, `Promise.all()` immediately rejects the returned promise. The other operations continue to run, but their outcomes are not available via the return value of `Promise.all()`. This may cause unexpected state or behavior. [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
 is another composition tool that ensures all operations are complete before resolving.

These methods all run promises concurrently — a sequence of promises are started simultaneously and do not wait for each other. Sequential composition is possible using some clever JavaScript:

In this example, we [reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
 an array of asynchronous functions down to a promise chain. The code above is equivalent to:

This can be made into a reusable compose function, which is common in functional programming:

The `composeAsync()` function accepts any number of functions as arguments and returns a new function that accepts an initial value to be passed through the composition pipeline:

Sequential composition can also be done more succinctly with async/await:

However, before you compose promises sequentially, consider if it's really necessary — it's always better to run promises concurrently so that they don't unnecessarily block each other unless one promise's execution depends on another's result.

[Cancellation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#cancellation)

----------------------------------------------------------------------------------------------------------

`Promise` itself has no first-class protocol for cancellation, but you may be able to directly cancel the underlying asynchronous operation, typically using [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
.

[Creating a Promise around an old callback API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#creating_a_promise_around_an_old_callback_api)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 can be created from scratch using its [constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
. This should be needed only to wrap old APIs.

In an ideal world, all asynchronous functions would already return promises. Unfortunately, some APIs still expect success and/or failure callbacks to be passed in the old way. The most obvious example is the [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
 function:

Mixing old-style callbacks and promises is problematic. If `saySomething()` fails or contains a programming error, nothing catches it. This is intrinsic to the design of `setTimeout()`.

Luckily we can wrap `setTimeout()` in a promise. The best practice is to wrap the callback-accepting functions at the lowest possible level, and then never call them directly again:

The promise constructor takes an executor function that lets us resolve or reject a promise manually. Since `setTimeout()` doesn't really fail, we left out reject in this case. For more information on how the executor function works, see the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 reference.

[Timing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#timing)

----------------------------------------------------------------------------------------------

Lastly, we will look into the more technical details, about when the registered callbacks get called.

### [Guarantees](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#guarantees)

In the callback-based API, when and how the callback gets called depends on the API implementor. For example, the callback may be called synchronously or asynchronously:

The above design is strongly discouraged because it leads to the so-called "state of Zalgo". In the context of designing asynchronous APIs, this means a callback is called synchronously in some cases but asynchronously in other cases, creating ambiguity for the caller. For further background, see the article [Designing APIs for Asynchrony](https://blog.izs.me/2013/08/designing-apis-for-asynchrony/ "External link (opens in new tab)")
, where the term was first formally presented. This API design makes side effects hard to analyze:

On the other hand, promises are a form of [inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control "External link (opens in new tab)")
 — the API implementor does not control when the callback gets called. Instead, the job of maintaining the callback queue and deciding when to call the callbacks is delegated to the promise implementation, and both the API user and API developer automatically get strong semantic guarantees, including:

*   Callbacks added with [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
     will never be invoked before the [completion of the current run](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model#run-to-completion)
     of the JavaScript event loop.
*   These callbacks will be invoked even if they were added _after_ the success or failure of the asynchronous operation that the promise represents.
*   Multiple callbacks may be added by calling [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
     several times. They will be invoked one after another, in the order in which they were inserted.

To avoid surprises, functions passed to [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
 will never be called synchronously, even with an already-resolved promise:

Instead of running immediately, the passed-in function is put on a microtask queue, which means it runs later (only after the function which created it exits, and when the JavaScript execution stack is empty), just before control is returned to the event loop; i.e., pretty soon:

### [Task queues vs. microtasks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#task_queues_vs._microtasks)

Promise callbacks are handled as a [microtask](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide)
 whereas [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
 callbacks are handled as task queues.

The code above will output:

Promise callback
Promise (pending) Promise {<pending>}
Promise callback (.then)
event-loop cycle: Promise (fulfilled) Promise {<fulfilled>}

For more details, refer to [Tasks vs. microtasks](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide/In_depth#tasks_vs._microtasks)
.

### [When promises and tasks collide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#when_promises_and_tasks_collide)

If you run into situations in which you have promises and tasks (such as events or callbacks) which are firing in unpredictable orders, it's possible you may benefit from using a microtask to check status or balance out your promises when promises are created conditionally.

If you think microtasks may help solve this problem, see the [microtask guide](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide)
 to learn more about how to use [`queueMicrotask()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/queueMicrotask "queueMicrotask()")
 to enqueue a function as a microtask.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#see_also)

--------------------------------------------------------------------------------------------------

*   [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    
*   [`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
    
*   [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
    
*   [Promises/A+ specification](https://promisesaplus.com/ "External link (opens in new tab)")
    
*   [We have a problem with promises](https://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html "External link (opens in new tab)")
     on pouchdb.com (2015)

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/using_promises/index.md?plain=1 "Folder: en-us/web/javascript/guide/using_promises (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FUsing_promises&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fusing_promises%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FUsing_promises%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fusing_promises%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F298079b550c76f20de6611c4ecdde4c30dc68b2b%0A*+Document+last+modified%3A+2026-09-22T10%3A09%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")