*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#mdn-search)
    

WeakRef
=======

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **`WeakRef`** object lets you hold a weak reference to another object, without preventing that object from getting garbage-collected.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#description)

--------------------------------------------------------------------------------------------------------------------

A `WeakRef` object contains a weak reference to an object, which is called its _target_ or _referent_. A _weak reference_ to an object is a reference that does not prevent the object from being reclaimed by the garbage collector. In contrast, a normal (or _strong_) reference keeps an object in memory. When an object no longer has any strong references to it, the JavaScript engine's garbage collector may destroy the object and reclaim its memory. If that happens, you can't get the object from a weak reference anymore.

Because [non-registered symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry)
 are also garbage collectable, they can also be used as the target of a `WeakRef` object. However, the use case of this is limited.

### [Avoid where possible](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#avoid_where_possible)

Correct use of `WeakRef` takes careful thought, and it's best avoided if possible. It's also important to avoid relying on any specific behaviors not guaranteed by the specification. When, how, and whether garbage collection occurs is down to the implementation of any given JavaScript engine. Any behavior you observe in one engine may be different in another engine, in another version of the same engine, or even in a slightly different situation with the same version of the same engine. Garbage collection is a hard problem that JavaScript engine implementers are constantly refining and improving their solutions to.

Here are some specific points included by the authors in the [proposal](https://github.com/tc39/proposal-weakrefs "External link (opens in new tab)")
 that introduced `WeakRef`:

> [Garbage collectors](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science) "External link (opens in new tab)")
>  are complicated. If an application or library depends on GC cleaning up a WeakRef or calling a finalizer \[cleanup callback\] in a timely, predictable manner, it's likely to be disappointed: the cleanup may happen much later than expected, or not at all. Sources of variability include:
> 
> *   One object might be garbage-collected much sooner than another object, even if they become unreachable at the same time, e.g., due to generational collection.
> *   Garbage collection work can be split up over time using incremental and concurrent techniques.
> *   Various runtime heuristics can be used to balance memory usage, responsiveness.
> *   The JavaScript engine may hold references to things which look like they are unreachable (e.g., in closures, or inline caches).
> *   Different JavaScript engines may do these things differently, or the same engine may change its algorithms across versions.
> *   Complex factors may lead to objects being held alive for unexpected amounts of time, such as use with certain APIs.

### [Notes on WeakRefs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#notes_on_weakrefs)

*   If your code has just created a `WeakRef` for a target object, or has gotten a target object from a `WeakRef`'s `deref` method, that target object will not be reclaimed until the end of the current JavaScript [job](https://tc39.es/ecma262/multipage/executable-code-and-execution-contexts.html#job "External link (opens in new tab)")
     (including any promise reaction jobs that run at the end of a script job). That is, you can only "see" an object get reclaimed between turns of the event loop. This is primarily to avoid making the behavior of any given JavaScript engine's garbage collector apparent in code — because if it were, people would write code relying on that behavior, which would break when the garbage collector's behavior changed. (Garbage collection is a hard problem; JavaScript engine implementers are constantly refining and improving how it works.)
*   If multiple `WeakRef`s have the same target, they're consistent with one another. The result of calling `deref` on one of them will match the result of calling `deref` on another of them (in the same job), you won't get the target object from one of them but `undefined` from another.
*   If the target of a `WeakRef` is also in a [`FinalizationRegistry`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry)
    , the `WeakRef`'s target is cleared at the same time or before any cleanup callback associated with the registry is called; if your cleanup callback calls `deref` on a `WeakRef` for the object, it will receive `undefined`.
*   You cannot change the target of a `WeakRef`, it will always only ever be the original target object or `undefined` when that target has been reclaimed.
*   A `WeakRef` might never return `undefined` from `deref`, even if nothing strongly holds the target, because the garbage collector may never decide to reclaim the object.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#constructor)

--------------------------------------------------------------------------------------------------------------------

[`WeakRef()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef/WeakRef)

Creates a new `WeakRef` object.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#instance_properties)

------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `WeakRef.prototype` and shared by all `WeakRef` instances.

[`WeakRef.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)
 Optional

The constructor function that created the instance object. For `WeakRef` instances, the initial value is the [`WeakRef`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef/WeakRef)
 constructor.

**Note:** This property is marked as "normative optional" in the specification, which means a conforming implementation may not expose the `constructor` property. This prevents arbitrary code from obtaining the `WeakRef` constructor and being able to observe garbage collection. However, all major engines do expose it by default.

[`WeakRef.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#weakref.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"WeakRef"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#instance_methods)

------------------------------------------------------------------------------------------------------------------------------

[`WeakRef.prototype.deref()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef/deref)

Returns the `WeakRef` object's target object, or `undefined` if the target object has been reclaimed.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#examples)

--------------------------------------------------------------------------------------------------------------

### [Using a WeakRef object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#using_a_weakref_object)

This example starts a counter shown in a DOM element, stopping when the element doesn't exist anymore:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-weak-ref-objects](https://tc39.es/ecma262/multipage/managing-memory.html#sec-weak-ref-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`FinalizationRegistry`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry)
    
*   [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
    
*   [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/weakref/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/weakref (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FWeakRef&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fweakref%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FWeakRef%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fweakref%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")