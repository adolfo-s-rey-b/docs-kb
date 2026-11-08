*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#mdn-search)
    

Promise
=======

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Promise`** object represents the eventual completion (or failure) of an asynchronous operation and its resulting value.

To learn about the way promises work and how you can use them, we advise you to read [Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
 first.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#description)

--------------------------------------------------------------------------------------------------------------------

A `Promise` is a proxy for a value not necessarily known when the promise is created. It allows you to associate handlers with an asynchronous action's eventual success value or failure reason. This lets asynchronous methods return values like synchronous methods: instead of immediately returning the final value, the asynchronous method returns a _promise_ to supply the value at some point in the future.

A `Promise` is in one of these states:

*   _pending_: initial state, neither fulfilled nor rejected.
*   _fulfilled_: meaning that the operation was completed successfully.
*   _rejected_: meaning that the operation failed.

The _eventual state_ of a pending promise can either be _fulfilled_ with a value or _rejected_ with a reason (error). When either of these options occurs, the associated handlers queued up by a promise's `then` method are called. If the promise has already been fulfilled or rejected when a corresponding handler is attached, the handler will be called, so there is no race condition between an asynchronous operation completing and its handlers being attached.

A promise is said to be _settled_ if it is either fulfilled or rejected, but not pending.

![Flowchart showing how the Promise state transitions between pending, fulfilled, and rejected via then/catch handlers. A pending promise can become either fulfilled or rejected. If fulfilled, the "on fulfillment" handler, or first parameter of the then() method, is executed and carries out further asynchronous actions. If rejected, the error handler, either passed as the second parameter of the then() method or as the sole parameter of the catch() method, gets executed.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/promises.png)

You will also hear the term _resolved_ used with promises — this means that the promise is settled or "locked-in" to match the eventual state of another promise, and further resolving or rejecting it has no effect. The [States and fates](https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md "External link (opens in new tab)")
 document from the original Promise proposal contains more details about promise terminology. Colloquially, "resolved" promises are often equivalent to "fulfilled" promises, but as illustrated in "States and fates", resolved promises can be pending or rejected as well. For example:

This promise is already _resolved_ at the time when it's created (because the `resolveOuter` is called synchronously), but it is resolved with another promise, and therefore won't be _fulfilled_ until 1 second later, when the inner promise fulfills. In practice, the "resolution" is often done behind the scenes and not observable, and only its fulfillment or rejection are.

**Note:** Several other languages have mechanisms for lazy evaluation and deferring a computation, which they also call "promises", e.g., Scheme. Promises in JavaScript represent processes that are already happening, which can be chained with callback functions. If you are looking to lazily evaluate an expression, consider using a function with no arguments e.g., `f = () => expression` to create the lazily-evaluated expression, and `f()` to evaluate the expression immediately.

`Promise` itself has no first-class protocol for cancellation, but you may be able to directly cancel the underlying asynchronous operation, typically using [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
.

### [Chained Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#chained_promises)

The promise methods [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
, [`catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
, and [`finally()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally)
 are used to associate further action with a promise that becomes settled. The `then()` method takes up to two arguments; the first argument is a callback function for the fulfilled case of the promise, and the second argument is a callback function for the rejected case. The `catch()` and `finally()` methods call `then()` internally and make error handling less verbose. For example, a `catch()` is really just a `then()` without passing the fulfillment handler. As these methods return promises, they can be chained. For example:

We will use the following terminology: _initial promise_ is the promise on which `then` is called; _new promise_ is the promise returned by `then`. The two callbacks passed to `then` are called _fulfillment handler_ and _rejection handler_, respectively.

The settled state of the initial promise determines which handler to execute.

*   If the initial promise is fulfilled, the fulfillment handler is called with the fulfillment value.
*   If the initial promise is rejected, the rejection handler is called with the rejection reason.

The completion of the handler determines the settled state of the new promise.

*   If the handler returns a [thenable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
     value, the new promise settles in the same state as the returned value.
*   If the handler returns a non-thenable value, the new promise is fulfilled with the returned value.
*   If the handler throws an error, the new promise is rejected with the thrown error.
*   If the initial promise has no corresponding handler attached, the new promise will settle to the same state as the initial promise — that is, without a rejection handler, a rejected promise stays rejected with the same reason.

For example, in the code above, if `myPromise` rejects, `handleRejectedA` will be called, and if `handleRejectedA` completes normally (without throwing or returning a rejected promise), the promise returned by the first `then` will be fulfilled instead of staying rejected. Therefore, if an error must be handled immediately, but we want to maintain the error state down the chain, we must throw an error of some type in the rejection handler. On the other hand, in the absence of an immediate need, we can leave out error handling until the final `catch()` handler.

Using [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 for the callback functions, implementation of the promise chain might look something like this:

**Note:** For faster execution, all synchronous actions should preferably be done within one handler, otherwise it would take several ticks to execute all handlers in sequence.

JavaScript maintains a [job queue](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model)
. Each time, JavaScript picks a job from the queue and executes it to completion. The jobs are defined by the executor of the `Promise()` constructor, the handlers passed to `then`, or any platform API that returns a promise. The promises in a chain represent the dependency relationship between these jobs. When a promise settles, the respective handlers associated with it are added to the back of the job queue.

A promise can participate in more than one chain. For the following code, the fulfillment of `promiseA` will cause both `handleFulfilled1` and `handleFulfilled2` to be added to the job queue. Because `handleFulfilled1` is registered first, it will be invoked first.

An action can be assigned to an already settled promise. In this case, the action is added immediately to the back of the job queue and will be performed when all existing jobs are completed. Therefore, an action for an already "settled" promise will occur only after the current synchronous code completes and at least one loop-tick has passed. This guarantees that promise actions are asynchronous.

### [Thenables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)

The JavaScript ecosystem had made multiple Promise implementations long before it became part of the language. Despite being represented differently internally, at the minimum, all Promise-like objects implement the _Thenable_ interface. A thenable implements the [`.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
 method, which is called with two callbacks: one for when the promise is fulfilled, one for when it's rejected. Promises are thenables as well.

To interoperate with the existing Promise implementations, the language allows using thenables in place of promises. For example, [`Promise.resolve`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
 will not only resolve promises, but also trace thenables.

The `then()` method is responsible for scheduling the execution of the provided `onFulfilled` and `onRejected` callbacks. Its semantics, including error handling and asynchronicity, are precisely defined in the [Promises/A+ specification](https://promisesaplus.com/ "External link (opens in new tab)")
, and we shall not repeat them here. It's very rare that you need to implement a thenable yourself; even if you are not using native promises, you would probably be using a Promise library such as [Bluebird](https://www.npmjs.com/package/bluebird "External link (opens in new tab)")
.

### [Promise concurrency](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#promise_concurrency)

The `Promise` class offers four main static methods to facilitate async task [concurrency](https://en.wikipedia.org/wiki/Concurrent_computing "External link (opens in new tab)")
:

[`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

Fulfills when **all** of the promises fulfill; rejects when **any** of the promises rejects.

[`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)

Fulfills when **all** promises settle.

[`Promise.any()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any)

Fulfills when **any** of the promises fulfills; rejects when **all** of the promises reject.

[`Promise.race()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)

Settles when **any** of the promises settles. In other words, fulfills when any of the promises fulfills; rejects when any of the promises rejects.

All these methods take an [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 of promises ([thenables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
, to be exact) and return a new promise. They all support subclassing, which means they can be called on subclasses of `Promise`, and the result will be a promise of the subclass type. To do so, the subclass's constructor must implement the same signature as the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor — accepting a single `executor` function that can be called with the `resolve` and `reject` callbacks as parameters. The subclass must also have a `resolve` static method that can be called like [`Promise.resolve()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
 to resolve values to promises.

There are two other convenience static methods: [`Promise.allKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed)
 and [`Promise.allSettledKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed)
, that behave like `Promise.all()` and `Promise.allSettled()`, but take _objects_ of promises and return promises that fulfill with _objects_ of the same shape. By working with objects instead of arrays, you can associate results with semantically meaningful keys, instead of arbitrary array ordering which can be difficult to maintain.

These methods attach handlers to each input promise using [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
. Even when the resulting promise has settled early (such as when one input in `Promise.race()` settles), the other handlers are not removed. Repeatedly passing the same pending promise to concurrency methods can accumulate handlers even when those handlers are never used:

Promises do not provide a way to unsubscribe these handlers; they remain attached while the input promise is pending and reachable. Where possible, cancel the underlying operation by using an [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)
 when the pending promise is no longer useful.

Note that JavaScript is [single-threaded](https://developer.mozilla.org/en-US/docs/Glossary/Thread)
 by nature, so at a given instant, only one task will be executing, although control can shift between different promises, making execution of the promises appear concurrent. [Parallel execution](https://en.wikipedia.org/wiki/Parallel_computing "External link (opens in new tab)")
 in JavaScript can only be achieved through [worker threads](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)
.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#constructor)

--------------------------------------------------------------------------------------------------------------------

[`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)

Creates a new `Promise` object. The constructor is primarily used to wrap functions that do not already support promises.

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#static_properties)

--------------------------------------------------------------------------------------------------------------------------------

[`Promise[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Symbol.species)

Returns the constructor used to construct return values from promise methods.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#static_methods)

--------------------------------------------------------------------------------------------------------------------------

[`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

Takes an iterable of promises as input and returns a single `Promise`. This returned promise fulfills when all of the input's promises fulfill (including when an empty iterable is passed), with an array of the fulfillment values. It rejects when any of the input's promises reject, with this first rejection reason.

[`Promise.allKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allKeyed)

Like `Promise.all()`, except that it takes an object of promises and returns a promise that fulfills with an object of the same shape, allowing you to associate results with semantically meaningful keys.

[`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)

Takes an iterable of promises as input and returns a single `Promise`. This returned promise fulfills when all of the input's promises settle (including when an empty iterable is passed), with an array of objects that describe the outcome of each promise.

[`Promise.allSettledKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettledKeyed)

Like `Promise.allSettled()`, except that it takes an object of promises and returns a promise that fulfills with an object of the same shape, allowing you to associate results with semantically meaningful keys.

[`Promise.any()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any)

Takes an iterable of promises as input and returns a single `Promise`. This returned promise fulfills when any of the input's promises fulfill, with this first fulfillment value. It rejects when all of the input's promises reject (including when an empty iterable is passed), with an [`AggregateError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AggregateError)
 containing an array of rejection reasons.

[`Promise.race()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)

Takes an iterable of promises as input and returns a single `Promise`. This returned promise settles with the eventual state of the first promise that settles.

[`Promise.reject()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject)

Returns a new `Promise` object that is rejected with the given reason.

[`Promise.resolve()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)

Returns a `Promise` object that is resolved with the given value. If the value is a thenable (i.e., has a `then` method), the returned promise will "follow" that thenable, adopting its eventual state; otherwise, the returned promise will be fulfilled with the value.

[`Promise.try()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try)

Takes a callback of any kind (returns or throws, synchronously or asynchronously) and resolves its result to a `Promise`.

[`Promise.withResolvers()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers)

Returns an object containing a new `Promise` object and two functions to resolve or reject it, corresponding to the two parameters passed to the executor of the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#instance_properties)

------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Promise.prototype` and shared by all `Promise` instances.

[`Promise.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Promise` instances, the initial value is the [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor.

[`Promise.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#promise.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Promise"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#instance_methods)

------------------------------------------------------------------------------------------------------------------------------

[`Promise.prototype.catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)

Appends a rejection handler callback to the promise, and returns a new promise resolving to the return value of the callback if it is called, or to its original fulfillment value if the promise is instead fulfilled.

[`Promise.prototype.finally()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally)

Appends a handler to the promise, and returns a new promise that is resolved when the original promise is resolved. The handler is called when the promise is settled, whether fulfilled or rejected.

[`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)

Appends fulfillment and rejection handlers to the promise, and returns a new promise resolving to the return value of the called handler, or to its original settled value if the promise was not handled (i.e., if the relevant handler `onFulfilled` or `onRejected` is not a function).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#examples)

--------------------------------------------------------------------------------------------------------------

### [Basic Example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#basic_example)

In this example, we use `setTimeout(...)` to simulate async code. In reality, you will probably be using something like XHR or an HTML API.

### [Example with diverse situations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#example_with_diverse_situations)

This example shows diverse techniques for using Promise capabilities and diverse situations that can occur. To understand this, start by scrolling to the bottom of the code block, and examine the promise chain. Upon provision of an initial promise, a chain of promises can follow. The chain is composed of `.then()` calls, and typically (but not necessarily) has a single `.catch()` at the end, optionally followed by `.finally()`. In this example, the promise chain is initiated by a custom-written `new Promise()` construct; but in actual practice, promise chains more typically start with an API function (written by someone else) that returns a promise.

The example function `tetheredGetNumber()` shows that a promise generator will utilize `reject()` while setting up an asynchronous call, or within the call-back, or both. The function `promiseGetWord()` illustrates how an API function might generate and return a promise in a self-contained manner.

Note that the function `troubleWithGetNumber()` ends with a `throw`. That is forced because a promise chain goes through all the `.then()` promises, even after an error, and without the `throw`, the error would seem "fixed". This is a hassle, and for this reason, it is common to omit `onRejected` throughout the chain of `.then()` promises, and just have a single `onRejected` in the final `catch()`.

This code can be run under Node.js. Comprehension is enhanced by seeing the errors actually occur. To force more errors, change the `threshold` values.

### [Advanced Example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#advanced_example)

This small example shows the mechanism of a `Promise`. The `testPromise()` method is called each time the [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 is clicked. It creates a promise that will be fulfilled, using [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
, to the promise count (number starting from 1) every 1-3 seconds, at random. The `Promise()` constructor is used to create the promise.

The fulfillment of the promise is logged, via a fulfill callback set using [`p1.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
. A few logs show how the synchronous part of the method is decoupled from the asynchronous completion of the promise.

By clicking the button several times in a short amount of time, you'll even see the different promises being fulfilled one after another.

#### HTML

#### JavaScript

#### Result

### [Loading an image with XHR](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#loading_an_image_with_xhr)

Another example using `Promise` and [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
 to load an image is shown below. Each step is commented on and allows you to follow the Promise and XHR architecture closely.

    <h1>Promise example</h1>
    

js

    function imgLoad(url) {
      // Create new promise with the Promise() constructor;
      // This has as its argument a function with two parameters, resolve and reject
      return new Promise((resolve, reject) => {
        // XHR to load an image
        const request = new XMLHttpRequest();
        request.open("GET", url);
        request.responseType = "blob";
        // When the request loads, check whether it was successful
        request.onload = () => {
          if (request.status === 200) {
            // If successful, resolve the promise by passing back the request response
            resolve(request.response);
          } else {
            // If it fails, reject the promise with an error message
            reject(
              Error(
                `Image didn't load successfully; error code: + ${request.statusText}`,
              ),
            );
          }
        };
        // Handle network errors
        request.onerror = () => reject(new Error("There was a network error."));
        // Send the request
        request.send();
      });
    }
    
    // Get a reference to the body element, and create a new image object
    const body = document.querySelector("body");
    const myImage = new Image();
    const imgUrl =
      "https://mdn.github.io/shared-assets/images/examples/round-balloon.png";
    
    // Call the function with the URL we want to load, then chain the
    // promise then() method with two callbacks
    imgLoad(imgUrl).then(
      (response) => {
        // The first runs when the promise resolves, with the request.response
        // specified within the resolve() method.
        const imageURL = URL.createObjectURL(response);
        myImage.src = imageURL;
        body.appendChild(myImage);
      },
      (error) => {
        // The second runs when the promise
        // is rejected, and logs the Error specified with the reject() method.
        console.log(error);
      },
    );
    

### [Incumbent settings object tracking](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#incumbent_settings_object_tracking)

A settings object is an [environment](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object "External link (opens in new tab)")
 that provides additional information when JavaScript code is running. This includes the realm and module map, as well as HTML specific information such as the origin. The incumbent settings object is tracked in order to ensure that the browser knows which one to use for a given piece of user code.

To better picture this, we can take a closer look at how the realm might be an issue. A **realm** can be roughly thought of as the global object. What is unique about realms is that they hold all of the necessary information to run JavaScript code. This includes objects like [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 and [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
. Each settings object has its own "copy" of these and they are not shared. That can cause some unexpected behavior in relation to promises. In order to get around this, we track something called the **incumbent settings object**. This represents information specific to the context of the user code responsible for a certain function call.

To illustrate this a bit further we can take a look at how an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 embedded in a document communicates with its host. Since all web APIs are aware of the incumbent settings object, the following will work in all browsers:

The same concept applies to promises. If we modify the above example a little bit, we get this:

If we change this so that the `<iframe>` in the document is listening to post messages, we can observe the effect of the incumbent settings object:

In the above example, the inner text of the `<iframe>` will be updated only if the incumbent settings object is tracked. This is because without tracking the incumbent, we may end up using the wrong environment to send the message.

**Note:** Currently, incumbent realm tracking is fully implemented in Firefox, and has partial implementations in Chrome and Safari.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-promise-objects](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-promise-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Promise` in `core-js`](https://core-js.io/docs/features/ecmascript/promise "External link (opens in new tab)")
    
*   [Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
     guide
*   [Promises/A+ specification](https://promisesaplus.com/ "External link (opens in new tab)")
    
*   [JavaScript Promises: an introduction](https://web.dev/articles/promises "External link (opens in new tab)")
     on web.dev (2013)
*   [Callbacks, Promises, and Coroutines: Asynchronous Programming Patterns in JavaScript](https://www.slideshare.net/slideshow/callbacks-promises-and-coroutines-oh-my-the-evolution-of-asynchronicity-in-javascript/9953720 "External link (opens in new tab)")
     slide show by Domenic Denicola (2011)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")