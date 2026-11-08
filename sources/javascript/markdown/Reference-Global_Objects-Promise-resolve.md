*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#mdn-search)
    

Promise.resolve()
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Promise.resolve()`** static method "resolves" a given value to a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
. If the value is a promise, that promise is returned; if the value is a [thenable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
, `Promise.resolve()` will call the `then()` method with two callbacks it prepared; otherwise the returned promise will be fulfilled with the value.

This function flattens nested layers of promise-like objects (e.g., a promise that fulfills to a promise that fulfills to something) into a single layer — a promise that fulfills to a non-thenable value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#try_it)

------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#syntax)

------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#parameters)

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#value)

Argument to be resolved by this `Promise`. Can also be a `Promise` or a thenable to resolve.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#return_value)

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 that is resolved with the given value, or the promise passed as value, if the value was a promise object. A resolved promise can be in any of the states — fulfilled, rejected, or pending. For example, resolving a rejected promise will still result in a rejected promise.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#description)

----------------------------------------------------------------------------------------------------------------------------

`Promise.resolve()` _resolves_ a promise, which is not the same as fulfilling or rejecting the promise. See [Promise description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#description)
 for definitions of the terminology. In brief, `Promise.resolve()` returns a promise whose eventual state depends on another promise, thenable object, or other value.

**Note:** If evaluating the `value` expression may synchronously throw an error, this error won't be caught and wrapped in a rejected promise by `Promise.resolve()`. Consider using [`Promise.try(() => value)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/try)
 in this case.

`Promise.resolve()` is generic and supports subclassing, which means it can be called on subclasses of `Promise`, and the result will be a promise of the subclass type. To do so, the subclass's constructor must implement the same signature as the [`Promise()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise)
 constructor — accepting a single `executor` function that can be called with the `resolve` and `reject` callbacks as parameters.

`Promise.resolve()` special-cases native `Promise` instances. If `value` belongs to `Promise` or a subclass, and `value.constructor === Promise`, then `value` is directly returned by `Promise.resolve()`, without creating a new `Promise` instance. Otherwise, `Promise.resolve()` is essentially a shorthand for `new Promise((resolve) => resolve(value))`.

The bulk of the resolving logic is actually implemented by [the `resolve` function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise#the_resolve_function)
 passed by the `Promise()` constructor. In summary:

*   If a non-[thenable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables)
     value is passed, the returned promise is already fulfilled with that value.
*   If a thenable is passed, the returned promise will adopt the state of that thenable by calling the `then` method and passing a pair of resolving functions as arguments. (But because native promises directly pass through `Promise.resolve()` without creating a wrapper, the `then` method is not called on native promises.) If the `resolve` function receives another thenable object, it will be resolved again, so that the eventual fulfillment value of the promise will never be thenable.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#examples)

----------------------------------------------------------------------------------------------------------------------

### [Using the static Promise.resolve method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#using_the_static_promise.resolve_method)

### [Resolving an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#resolving_an_array)

### [Resolving another Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#resolving_another_promise)

`Promise.resolve()` reuses existing `Promise` instances. If it's resolving a native promise, it returns the same promise instance without creating a wrapper.

The inverted order of the logs is due to the fact that the `then` handlers are called asynchronously. See the [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
 reference for more information.

### [Resolving thenables and throwing Errors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#resolving_thenables_and_throwing_errors)

Nested thenables will be "deeply flattened" to a single promise.

**Warning:** Do not call `Promise.resolve()` on a thenable that resolves to itself. That leads to infinite recursion, because it attempts to flatten an infinitely-nested promise.

### [Calling resolve() on a non-Promise constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#calling_resolve_on_a_non-promise_constructor)

`Promise.resolve()` is a generic method. It can be called on any constructor that implements the same signature as the `Promise()` constructor. For example, we can call it on a constructor that passes it `console.log` as `resolve`:

The ability to flatten nested thenables is implemented by the `resolve` function of the `Promise()` constructor, so if you call it on another constructor, nested thenables may not be flattened, depending on how that constructor implements its `resolve` function.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-promise.resolve](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-promise.resolve) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/promise/resolve/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/promise/resolve (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fresolve&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fresolve%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fresolve%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fpromise%2Fresolve%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa6a2daec3965d85ef6dfc06cfd3507c1b2f886e2%0A*+Document+last+modified%3A+2026-09-14T07%3A31%3A42.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")