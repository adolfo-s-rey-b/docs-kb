*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#mdn-search)
    

Memory management
=================

Low-level languages like C, have manual memory management primitives such as [`malloc()`](https://pubs.opengroup.org/onlinepubs/009695399/functions/malloc.html "External link (opens in new tab)")
 and [`free()`](https://en.wikipedia.org/wiki/C_dynamic_memory_allocation#Overview_of_functions "External link (opens in new tab)")
. In contrast, JavaScript automatically allocates memory when objects are created and frees it when they are not used anymore (_garbage collection_). This automaticity is a potential source of confusion: it can give developers the false impression that they don't need to worry about memory management.

[Memory life cycle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#memory_life_cycle)

-----------------------------------------------------------------------------------------------------------------------

Regardless of the programming language, the memory life cycle is pretty much always the same:

1.  Allocate the memory you need
2.  Use the allocated memory (read, write)
3.  Release the allocated memory when it is not needed anymore

The second part is explicit in all languages. The first and last parts are explicit in low-level languages but are mostly implicit in high-level languages like JavaScript.

### [Allocation in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#allocation_in_javascript)

#### Value initialization

In order to not bother the programmer with allocations, JavaScript will automatically allocate memory when values are initially declared.

#### Allocation via function calls

Some function calls result in object allocation.

Some methods allocate new values or objects:

### [Using values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#using_values)

Using values basically means reading and writing in allocated memory. This can be done by reading or writing the value of a variable or an object property or even passing an argument to a function.

### [Release when the memory is not needed anymore](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#release_when_the_memory_is_not_needed_anymore)

The majority of memory management issues occur at this phase. The most difficult aspect of this stage is determining when the allocated memory is no longer needed.

Low-level languages require the developer to manually determine at which point in the program the allocated memory is no longer needed and to release it.

Some high-level languages, such as JavaScript, utilize a form of automatic memory management known as [garbage collection](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science) "External link (opens in new tab)")
 (GC). The purpose of a garbage collector is to monitor memory allocation and determine when a block of allocated memory is no longer needed and reclaim it. This automatic process is an approximation since the general problem of determining whether or not a specific piece of memory is still needed is [undecidable](https://en.wikipedia.org/wiki/Decidability_%28logic%29 "External link (opens in new tab)")
.

[Garbage collection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#garbage_collection)

-------------------------------------------------------------------------------------------------------------------------

As stated above, the general problem of automatically finding whether some memory "is not needed anymore" is undecidable. As a consequence, garbage collectors implement a restriction of a solution to the general problem. This section will explain the concepts that are necessary for understanding the main garbage collection algorithms and their respective limitations.

### [References](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#references)

The main concept that garbage collection algorithms rely on is the concept of _reference_. Within the context of memory management, an object is said to reference another object if the former has access to the latter (either implicitly or explicitly). For instance, a JavaScript object has a reference to its [prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 (implicit reference) and to its properties values (explicit reference).

In this context, the notion of an "object" is extended to something broader than regular JavaScript objects and also contain function scopes (or the global lexical scope).

### [Reference-counting garbage collection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#reference-counting_garbage_collection)

**Note:** No modern JavaScript engine uses reference-counting for garbage collection anymore.

This is the most naïve garbage collection algorithm. This algorithm reduces the problem from determining whether or not an object is still needed to determining if an object still has any other objects referencing it. An object is said to be "garbage", or collectible if there are zero references pointing to it.

For example:

There is a limitation when it comes to circular references. In the following example, two objects are created with properties that reference one another, thus creating a cycle. They will go out of scope after the function call has completed. At that point they become unneeded and their allocated memory should be reclaimed. However, the reference-counting algorithm will not consider them reclaimable since each of the two objects has at least one reference pointing to them, resulting in neither of them being marked for garbage collection. Circular references are a common cause of memory leaks.

### [Mark-and-sweep algorithm](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#mark-and-sweep_algorithm)

This algorithm reduces the definition of "an object is no longer needed" to "an object is unreachable".

This algorithm assumes the knowledge of a set of objects called _roots._ In JavaScript, the root is the global object. Periodically, the garbage collector will start from these roots, find all objects that are referenced from these roots, then all objects referenced from these, etc. Starting from the roots, the garbage collector will thus find all _reachable_ objects and collect all non-reachable objects.

This algorithm is an improvement over the previous one since an object having zero references is effectively unreachable. The opposite does not hold true as we have seen with circular references.

Currently, all modern engines ship a mark-and-sweep garbage collector. All improvements made in the field of JavaScript garbage collection (generational/incremental/concurrent/parallel garbage collection) over the last few years are implementation improvements of this algorithm, but not improvements over the garbage collection algorithm itself nor its reduction of the definition of when "an object is no longer needed".

The immediate benefit of this approach is that cycles are no longer a problem. In the first example above, after the function call returns, the two objects are no longer referenced by any resource that is reachable from the global object. Consequently, they will be found unreachable by the garbage collector and have their allocated memory reclaimed.

However, the inability to manually control garbage collection remains. There are times when it would be convenient to manually decide when and what memory is released. In order to release the memory of an object, it needs to be made explicitly unreachable. It is also not possible to programmatically trigger garbage collection in JavaScript — and will likely never be within the core language, although engines may expose APIs behind opt-in flags.

[Configuring an engine's memory model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#configuring_an_engines_memory_model)

------------------------------------------------------------------------------------------------------------------------------------------------------------

JavaScript engines typically offer flags that expose the memory model. For example, Node.js offers additional options and tools that expose the underlying V8 mechanisms for configuring and debugging memory issues. This configuration may not be available in browsers, and even less so for web pages (via HTTP headers, etc.).

The max amount of available heap memory can be increased with a flag:

We can also expose the garbage collector for debugging memory issues using a flag and the [Chrome Debugger](https://nodejs.org/learn/getting-started/debugging "External link (opens in new tab)")
:

[Data structures aiding memory management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#data_structures_aiding_memory_management)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Although JavaScript does not directly expose the garbage collector API, the language offers several data structures that indirectly observe garbage collection and can be used to manage memory usage.

### [WeakMaps and WeakSets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#weakmaps_and_weaksets)

[`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
 and [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
 are data structures whose APIs closely mirror their non-weak counterparts: [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 and [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
. `WeakMap` allows you to maintain a collection of key-value pairs, while `WeakSet` allows you to maintain a collection of unique values, both with performant addition, deletion, and querying.

`WeakMap` and `WeakSet` got the name from the concept of _weakly held_ values. If `x` is weakly held by `y`, it means that although you can access the value of `x` via `y`, the mark-and-sweep algorithm won't consider `x` as reachable if nothing else _strongly holds_ to it. Most data structures, except the ones discussed here, strongly hold to the objects passed in so that you can retrieve them at any time. The keys of `WeakMap` and `WeakSet` can be garbage-collected (for `WeakMap` objects, the values would then be eligible for garbage collection as well) as long as nothing else in the program is referencing the key. This is ensured by two characteristics:

*   `WeakMap` and `WeakSet` can only store objects or symbols. This is because only objects are garbage collected — primitive values can always be forged (that is, `1 === 1` but `{} !== {}`), making them stay in the collection forever. [Registered symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry)
     (like `Symbol.for("key")`) can also be forged and thus are not garbage collectable, but symbols created with `Symbol("key")` are garbage collectable. [Well-known symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#well-known_symbols)
     like `Symbol.iterator` come in a fixed set and are unique throughout the lifetime of the program, similar to intrinsic objects such as `Array.prototype`, so they are also allowed as keys.
*   `WeakMap` and `WeakSet` are not iterable. This prevents you from using `Array.from(map.keys()).length` to observe the liveliness of objects, or get hold of an arbitrary key which should otherwise be eligible for garbage collection. (Garbage collection should be as invisible as possible.)

In typical explanations of `WeakMap` and `WeakSet` (such as the one above), it's often implied that the key is garbage-collected first, freeing the value for garbage collection as well. However, consider the case of the value referencing the key:

If `key` is stored as an actual reference, it would create a cyclic reference and make both the key and value ineligible for garbage collection, even when nothing else references `key` — because if `key` is garbage collected, it means that at some particular instant, `value.key` would point to a non-existent address, which is not legal. To fix this, the entries of `WeakMap` and `WeakSet` aren't actual references, but [ephemerons](https://dl.acm.org/doi/pdf/10.1145/263700.263733 "External link (opens in new tab)")
, an enhancement to the mark-and-sweep mechanism. [Barros et al.](https://www.jucs.org/jucs_14_21/eliminating_cycles_in_weak/jucs_14_21_3481_3497_barros.pdf "External link (opens in new tab)")
 offers a good summary of the algorithm (page 4). To quote a paragraph:

> Ephemerons are a refinement of weak pairs where neither the key nor the value can be classified as weak or strong. The connectivity of the key determines the connectivity of the value, but the connectivity of the value does not affect the connectivity of the key. \[…\] when the garbage collection offers support to ephemerons, it occurs in three phases instead of two (mark and sweep).

As a rough mental model, think of a `WeakMap` as the following implementation:

**Warning:** This is not a polyfill, nor is it anywhere close to how it's implemented in the engine (which hooks into the garbage collection mechanism).

As you can see, the `MyWeakMap` never actually holds a collection of keys. It simply adds metadata to each object being passed in. The object is then garbage-collectable via mark-and-sweep. Therefore, it's not possible to iterate over the keys in a `WeakMap`, nor clear the `WeakMap` (as that also relies on the knowledge of the entire key collection).

For more information on their APIs, see the [keyed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections)
 guide.

### [WeakRefs and FinalizationRegistry](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#weakrefs_and_finalizationregistry)

**Note:** `WeakRef` and `FinalizationRegistry` offer direct introspection into the garbage collection machinery. [Avoid using them where possible](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef#avoid_where_possible)
 because the runtime semantics are almost completely unguaranteed.

All variables with an object as value are references to that object. However, such references are _strong_ — their existence would prevent the garbage collector from marking the object as eligible for collection. A [`WeakRef`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef)
 is a _weak reference_ to an object that allows the object to be garbage collected, while still retaining the ability to read the object's content during its lifetime.

One use case for `WeakRef` is a cache system which maps string URLs to large objects. We cannot use a `WeakMap` for this purpose, because `WeakMap` objects have their _keys_ weakly held, but not their _values_ — if you access a key, you would always deterministically get the value (since having access to the key means it's still alive). Here, we are okay to get `undefined` for a key (if the corresponding value is no longer alive) since we can just re-compute it, but we don't want unreachable objects to stay in the cache. In this case, we can use a normal `Map`, but with each value being a `WeakRef` of the object instead of the actual object value.

[`FinalizationRegistry`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry)
 provides an even stronger mechanism to observe garbage collection. It allows you to register objects and be notified when they are garbage collected. For example, for the cache system exemplified above, even when the blobs themselves are free for collection, the `WeakRef` objects that hold them are not — and over time, the `Map` may accumulate a lot of useless entries. Using a `FinalizationRegistry` allows one to perform cleanup in this case.

Due to performance and security concerns, there is no guarantee of when the callback will be called, or if it will be called at all. It should only be used for cleanup — and non-critical cleanup. There are other ways for more deterministic resource management, such as [`try...finally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
, which will always execute the `finally` block. `WeakRef` and `FinalizationRegistry` exist solely for optimization of memory usage in long-running programs.

For more information on the API of [`WeakRef`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef)
 and [`FinalizationRegistry`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry)
, see their reference pages.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 23, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/memory_management/index.md?plain=1 "Folder: en-us/web/javascript/guide/memory_management (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FMemory_management&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fmemory_management%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FMemory_management%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fmemory_management%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd49a4a4b409c60938b544e315358e27068991484%0A*+Document+last+modified%3A+2026-10-23T21%3A16%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")