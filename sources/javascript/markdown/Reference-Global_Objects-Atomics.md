*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#mdn-search)
    

Atomics
=======

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2021.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Atomics`** namespace object contains static methods for carrying out atomic operations. They are used with [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)
 and [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
 objects.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#description)

--------------------------------------------------------------------------------------------------------------------

Unlike most global objects, `Atomics` is not a constructor. You cannot use it with the [`new` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 or invoke the `Atomics` object as a function. All properties and methods of `Atomics` are static (just like the [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
 object).

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#static_properties)

--------------------------------------------------------------------------------------------------------------------------------

[`Atomics[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#atomicssymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Atomics"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#static_methods)

--------------------------------------------------------------------------------------------------------------------------

[`Atomics.add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/add)

Adds the provided value to the existing value at the specified index of the array. Returns the old value at that index.

[`Atomics.and()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/and)

Computes a bitwise AND on the value at the specified index of the array with the provided value. Returns the old value at that index.

[`Atomics.compareExchange()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/compareExchange)

Stores a value at the specified index of the array, if it equals a value. Returns the old value.

[`Atomics.exchange()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/exchange)

Stores a value at the specified index of the array. Returns the old value.

[`Atomics.isLockFree()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/isLockFree)

An optimization primitive that can be used to determine whether to use locks or atomic operations. Returns `true` if an atomic operation on arrays of the given element size will be implemented using a hardware atomic operation (as opposed to a lock). Experts only.

[`Atomics.load()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/load)

Returns the value at the specified index of the array.

[`Atomics.notify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/notify)

Notifies agents that are waiting on the specified index of the array. Returns the number of agents that were notified.

[`Atomics.or()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/or)

Computes a bitwise OR on the value at the specified index of the array with the provided value. Returns the old value at that index.

[`Atomics.pause()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/pause)

Provides a micro-wait primitive that hints to the CPU that the caller is spinning while waiting on access to a shared resource. This allows the system to reduce the resources allocated to the core (such as power) or thread, without yielding the current thread.

[`Atomics.store()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/store)

Stores a value at the specified index of the array. Returns the value.

[`Atomics.sub()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/sub)

Subtracts a value at the specified index of the array. Returns the old value at that index.

[`Atomics.wait()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/wait)

Verifies that the specified index of the array still contains a value and sleeps awaiting or times out. Returns either `"ok"`, `"not-equal"`, or `"timed-out"`. If waiting is not allowed in the calling agent then it throws an exception. (Most browsers will not allow `wait()` on the browser's main thread.)

[`Atomics.waitAsync()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/waitAsync)

Waits asynchronously (i.e., without blocking, unlike `Atomics.wait`) on a shared memory location and returns an object representing the result of the operation.

[`Atomics.xor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/xor)

Computes a bitwise XOR on the value at the specified index of the array with the provided value. Returns the old value at that index.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#examples)

--------------------------------------------------------------------------------------------------------------

Note that these examples cannot be run directly from the console or an arbitrary web page, because `SharedArrayBuffer` is not defined unless its [security requirements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer#security_requirements)
 are met.

### [Using Atomics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#using_atomics)

### [Waiting and notifying](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#waiting_and_notifying)

Given a shared `Int32Array`:

A reading thread is sleeping and waiting on location 0 because the provided value matches what is stored at the provided index. The reading thread will not move on until the writing thread has called `Atomics.notify()` on position 0 of the provided typed array. Note that if, after being woken up, the value of location 0 has not been changed by the writing thread, the reading thread will **not** go back to sleep, but will continue on.

A writing thread stores a new value and notifies the waiting thread once it has written:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-atomics-object](https://tc39.es/ecma262/multipage/structured-data.html#sec-atomics-object) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Agent communication and coordination](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Agent_communication_and_coordination)
     guide
*   [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
    
*   [JavaScript typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
     guide
*   [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)
    
*   [Shared Memory – a brief tutorial](https://github.com/tc39/proposal-ecmascript-sharedmem/blob/main/TUTORIAL.md "External link (opens in new tab)")
     in the TC39 ecmascript-sharedmem proposal
*   [A Taste of JavaScript's New Parallel Primitives](https://hacks.mozilla.org/2016/05/a-taste-of-javascripts-new-parallel-primitives/ "External link (opens in new tab)")
     on hacks.mozilla.org (2016)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/atomics/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/atomics (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAtomics&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fatomics%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAtomics%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fatomics%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9d64ff6c5d0eee1800b0d3b4f9076de65f34f5ce%0A*+Document+last+modified%3A+2026-10-28T18%3A50%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")