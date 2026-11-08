*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#mdn-search)
    

FinalizationRegistry
====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **`FinalizationRegistry`** object lets you request a callback when a value is garbage-collected.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#description)

---------------------------------------------------------------------------------------------------------------------------------

`FinalizationRegistry` provides a way to request that a _cleanup callback_ get called at some point when a value registered with the registry has been _reclaimed_ (garbage-collected). (Cleanup callbacks are sometimes called _finalizers_.)

**Note:** Cleanup callbacks should not be used for essential program logic. See [Notes on cleanup callbacks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#notes_on_cleanup_callbacks)
 for details.

You create the registry passing in the callback:

Then you register any value you want a cleanup callback for by calling the `register` method, passing in the value and a _held value_ for it:

The registry does not keep a strong reference to the value, as that would defeat the purpose (if the registry held it strongly, the value would never be reclaimed). In JavaScript, objects and [non-registered symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry)
 are garbage collectable, so they can be registered in a `FinalizationRegistry` object as the target or the token.

If `target` is reclaimed, your cleanup callback may be called at some point with the _held value_ you provided for it (`"some value"` in the above). The held value can be any value you like: a primitive or an object, even `undefined`. If the held value is an object, the registry keeps a _strong_ reference to it (so it can pass it to your cleanup callback later).

If you might want to unregister a registered target value later, you pass a third value, which is the _unregistration token_ you'll use later when calling the registry's `unregister` function to unregister the value. The registry only keeps a weak reference to the unregister token.

It's common to use the target value itself as the unregister token, which is just fine:

It doesn't have to be the same value, though; it can be a different one:

### [Avoid where possible](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#avoid_where_possible)

Correct use of `FinalizationRegistry` takes careful thought, and it's best avoided if possible. It's also important to avoid relying on any specific behaviors not guaranteed by the specification. When, how, and whether garbage collection occurs is down to the implementation of any given JavaScript engine. Any behavior you observe in one engine may be different in another engine, in another version of the same engine, or even in a slightly different situation with the same version of the same engine. Garbage collection is a hard problem that JavaScript engine implementers are constantly refining and improving their solutions to.

Here are some specific points included by the authors in the [proposal](https://github.com/tc39/proposal-weakrefs "External link (opens in new tab)")
 that introduced `FinalizationRegistry`:

> [Garbage collectors](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science) "External link (opens in new tab)")
>  are complicated. If an application or library depends on GC cleaning up a WeakRef or calling a finalizer \[cleanup callback\] in a timely, predictable manner, it's likely to be disappointed: the cleanup may happen much later than expected, or not at all. Sources of variability include:
> 
> *   One object might be garbage-collected much sooner than another object, even if they become unreachable at the same time, e.g., due to generational collection.
> *   Garbage collection work can be split up over time using incremental and concurrent techniques.
> *   Various runtime heuristics can be used to balance memory usage, responsiveness.
> *   The JavaScript engine may hold references to things which look like they are unreachable (e.g., in closures, or inline caches).
> *   Different JavaScript engines may do these things differently, or the same engine may change its algorithms across versions.
> *   Complex factors may lead to objects being held alive for unexpected amounts of time, such as use with certain APIs.

### [Notes on cleanup callbacks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#notes_on_cleanup_callbacks)

*   Developers shouldn't rely on cleanup callbacks for essential program logic. Cleanup callbacks may be useful for reducing memory usage across the course of a program, but are unlikely to be useful otherwise.
*   If your code has just registered a value to the registry, that target will not be reclaimed until the end of the current JavaScript [job](https://tc39.es/ecma262/multipage/executable-code-and-execution-contexts.html#job "External link (opens in new tab)")
    . See [notes on WeakRefs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#notes_on_weakrefs)
     for details.
*   A conforming JavaScript implementation, even one that does garbage collection, is not required to call cleanup callbacks. When and whether it does so is entirely down to the implementation of the JavaScript engine. When a registered object is reclaimed, any cleanup callbacks for it may be called then, or some time later, or not at all.
*   It's likely that major implementations will call cleanup callbacks at some point during execution, but those calls may be substantially after the related object was reclaimed. Furthermore, if there is an object registered in two registries, there is no guarantee that the two callbacks are called next to each other — one may be called and the other never called, or the other may be called much later.
*   There are also situations where even implementations that normally call cleanup callbacks are unlikely to call them:
    *   When the JavaScript program shuts down entirely (for instance, closing a tab in a browser).
    *   When the `FinalizationRegistry` instance itself is no longer reachable by JavaScript code.
*   If the target of a `WeakRef` is also in a `FinalizationRegistry`, the `WeakRef`'s target is cleared at the same time or before any cleanup callback associated with the registry is called; if your cleanup callback calls `deref` on a `WeakRef` for the object, it will receive `undefined`.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#constructor)

---------------------------------------------------------------------------------------------------------------------------------

[`FinalizationRegistry()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry/FinalizationRegistry)

Creates a new `FinalizationRegistry` object.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#instance_properties)

-------------------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `FinalizationRegistry.prototype` and shared by all `FinalizationRegistry` instances.

[`FinalizationRegistry.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `FinalizationRegistry` instances, the initial value is the [`FinalizationRegistry`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry/FinalizationRegistry)
 constructor.

[`FinalizationRegistry.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#finalizationregistry.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"FinalizationRegistry"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#instance_methods)

-------------------------------------------------------------------------------------------------------------------------------------------

[`FinalizationRegistry.prototype.register()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry/register)

Registers an object with the registry in order to get a cleanup callback when/if the object is garbage-collected.

[`FinalizationRegistry.prototype.unregister()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry/unregister)

Unregisters an object from the registry.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Creating a new registry](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#creating_a_new_registry)

You create the registry passing in the callback:

### [Registering objects for cleanup](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#registering_objects_for_cleanup)

Then you register any objects you want a cleanup callback for by calling the `register` method, passing in the object and a _held value_ for it:

### [Callbacks never called synchronously](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#callbacks_never_called_synchronously)

No matter how much pressure you put on the garbage collector, the cleanup callback will never be called synchronously. The object may be reclaimed synchronously, but the callback will always be called sometime after the current job finishes:

However, if you allow a little break between each allocation, the callback may be called sooner:

There's no guarantee that the callback will be called sooner or if it will be called at all, but there's a possibility that the logged message has a counter value smaller than 5000.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-finalization-registry-objects](https://tc39.es/ecma262/multipage/managing-memory.html#sec-finalization-registry-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [`WeakRef`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef)
    
*   [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
    
*   [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/finalizationregistry/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/finalizationregistry (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFinalizationRegistry&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffinalizationregistry%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFinalizationRegistry%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffinalizationregistry%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")