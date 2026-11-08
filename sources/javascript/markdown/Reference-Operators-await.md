*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#mdn-search)
    

await
=====

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`await`** operator is used to wait for a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 and get its fulfillment value. It can only be used inside an [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
 or at the top level of a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#syntax)

---------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#parameters)

[`expression`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#expression)

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
, a [thenable object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
, or any value to wait for.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#return_value)

The fulfillment value of the promise or thenable object, or, if the expression is not thenable, the expression's own value.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#exceptions)

Throws the rejection reason if the promise or thenable object is rejected.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#description)

-------------------------------------------------------------------------------------------------------------

`await` is usually used to unwrap promises by passing a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 as the `expression`. Using `await` pauses the execution of its surrounding `async` function until the promise is settled (that is, fulfilled or rejected). When execution resumes, the value of the `await` expression becomes that of the fulfilled promise.

If the promise is rejected, the `await` expression throws the rejected value. The function containing the `await` expression will [appear in the stack trace](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#improving_stack_trace)
 of the error. Otherwise, if the rejected promise is not awaited or is immediately returned, the caller function will not appear in the stack trace.

The `expression` is resolved in the same way as [`Promise.resolve()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
: it's always converted to a native `Promise` and then awaited. If the `expression` is a:

*   Native `Promise` (which means `expression` belongs to `Promise` or a subclass, and `expression.constructor === Promise`): The promise is directly used and awaited natively, without calling `then()`.
*   [Thenable object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
     (including non-native promises, polyfill, proxy, child class, etc.): A new promise is constructed with the native [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
     constructor by calling the object's `then()` method and passing in a handler that calls the `resolve` callback.
*   Non-thenable value: An already-fulfilled `Promise` is constructed and used.

Even when the used promise is already fulfilled, the async function's execution still pauses until the next tick. In the meantime, the caller of the async function resumes execution. [See example below.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#control_flow_effects_of_await)

Because `await` is only valid inside async functions and modules, which themselves are asynchronous and return promises, the `await` expression never blocks the main thread and only defers execution of code that actually depends on the result, i.e., anything after the `await` expression.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#examples)

-------------------------------------------------------------------------------------------------------

### [Awaiting a promise to be fulfilled](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#awaiting_a_promise_to_be_fulfilled)

If a `Promise` is passed to an `await` expression, it waits for the `Promise` to be fulfilled and returns the fulfilled value.

### [Thenable objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#thenable_objects)

[Thenable objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
 are resolved just the same as actual `Promise` objects.

They can also be rejected:

### [Conversion to promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#conversion_to_promise)

If the value is not a `Promise`, `await` converts the value to a resolved `Promise`, and waits for it. The awaited value's identity doesn't change as long as it doesn't have a `then` property that's callable.

### [Handling rejected promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#handling_rejected_promises)

If the `Promise` is rejected, the rejected value is thrown.

You can handle rejected promises without a `try` block by chaining a [`catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
 handler before awaiting the promise.

This is built on the assumption that `promisedFunction()` never synchronously throws an error, but always returns a rejected promise. This is the case for most properly-designed promise-based functions, which usually look like:

However, if `promisedFunction()` does throw an error synchronously, the error won't be caught by the `catch()` handler. In this case, the `try...catch` statement is necessary.

### [Top-level await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#top-level_await)

You can use the `await` keyword on its own (outside of an async function) at the top level of a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
. This means that modules with child modules that use `await` will wait for the child modules to execute before they themselves run, all while not blocking sibling modules that don't depend on those child modules from executing.

Here is an example of a module using the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
 and specifying await within the [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
 statement. Any modules that include this will wait for the fetch to resolve before running any code.

Top-level `await` is not free; it has deep implications because it means a part of the [module graph](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph)
 can only be evaluated asynchronously. See the [module graph](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Module_graph#top-level_await_and_asynchronous_evaluation)
 guide for more information.

### [Control flow effects of await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#control_flow_effects_of_await)

When an `await` is encountered in code (either in an async function or in a module), the awaited expression is executed, while all code that depends on the expression's value is paused. Control exits the function and returns to the caller. When the awaited expression's value is resolved, another [microtask](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model)
 that continues the paused code gets scheduled. This happens even if the awaited value is an already-resolved promise or not a promise: execution doesn't return to the current function until all other already-scheduled microtasks are processed. For example, consider the following code:

In this case, the function `foo` is synchronous in effect, because it doesn't contain any `await` expression. The three statements happen in the same tick. Therefore, the two function calls execute all statements in sequence. In promise terms, the function corresponds to:

However, as soon as there's one `await`, the function becomes asynchronous, and execution of following statements is deferred to the next tick.

This corresponds to:

The extra `then()` handler can be merged with the executor passed to the constructor because it's not waiting on any asynchronous operation. However, its existence splits the code into one additional microtask for each call to `foo`. These microtasks are scheduled and executed in an intertwined manner, which can both make your code slower and introduce unnecessary race conditions. Therefore, make sure to use `await` only when necessary (to unwrap promises into their values).

Microtasks are scheduled not only by promise resolution but by other web APIs as well, and they execute with the same priority. This example uses [`queueMicrotask()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/queueMicrotask "queueMicrotask()")
 to demonstrate how the microtask queue is processed when each `await` expression is encountered.

In this example, the `test()` function is always called before the async function resumes, so the microtasks they each schedule are always executed in an intertwined fashion. On the other hand, because both `await` and `queueMicrotask()` schedule microtasks, the order of execution is always based on the order of scheduling. This is why the "queueMicrotask() after calling async function" log happens after the async function resumes for the first time.

### [Improving stack trace](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#improving_stack_trace)

Sometimes, the `await` is omitted when a promise is directly returned from an async function.

However, consider the case where `lastAsyncTask` asynchronously throws an error.

Only `lastAsyncTask` appears in the stack trace, because the promise is rejected after it has already been returned from `noAwait` — in some sense, the promise is unrelated to `noAwait`. To improve the stack trace, you can use `await` to unwrap the promise, so that the exception gets thrown into the current function. The exception will then be immediately wrapped into a new rejected promise, but during error creation, the caller will appear in the stack trace.

Contrary to some popular belief, `return await promise` is at least as fast as `return promise`, due to how the spec and engines optimize the resolution of native promises. There's a proposal to [make `return promise` faster](https://github.com/tc39/proposal-faster-promise-adoption "External link (opens in new tab)")
 and you can also read about [V8's optimization on async functions](https://v8.dev/blog/fast-async "External link (opens in new tab)")
. Therefore, except for stylistic reasons, `return await` is almost always preferable.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-async-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-async-function-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#see_also)

-------------------------------------------------------------------------------------------------------

*   [`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
    
*   [`async function` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function)
    
*   [`AsyncFunction`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncFunction)
    
*   [Top-level await](https://v8.dev/features/top-level-await "External link (opens in new tab)")
     on v8.dev (2019)
*   [typescript-eslint rule: `return-await`](https://typescript-eslint.io/rules/return-await/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/await/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/await (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fawait&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fawait%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fawait%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fawait%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")