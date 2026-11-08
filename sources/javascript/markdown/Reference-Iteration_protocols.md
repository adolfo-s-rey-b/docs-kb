*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#mdn-search)
    

Iteration protocols
===================

**Iteration protocols** aren't new built-ins or syntax, but _protocols_. These protocols can be implemented by any object by following some conventions.

There are two protocols: The [iterable protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 and the [iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
.

[The iterable protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)

-------------------------------------------------------------------------------------------------------------------------------------

**The iterable protocol** allows JavaScript objects to define or customize their iteration behavior, such as what values are looped over in a [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 construct. Some built-in types are [built-in iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#built-in_iterables)
 with a default iteration behavior, such as [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 or [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
, while other types (such as [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
) are not.

In order to be **iterable**, an object must implement the **`[Symbol.iterator]()`** method, meaning that the object (or one of the objects up its [prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
) must have a property with a `[Symbol.iterator]` key which is available via constant [`Symbol.iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)
:

[`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#symbol.iterator)

A zero-argument function that returns an object, conforming to the [iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
.

Whenever an object needs to be iterated (such as at the beginning of a [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loop), its `[Symbol.iterator]()` method is called with no arguments, and the returned **iterator** is used to obtain the values to be iterated.

Note that when this zero-argument function is called, it is invoked as a method on the iterable object. Therefore inside of the function, the `this` keyword can be used to access the properties of the iterable object, to decide what to provide during the iteration.

This function can be an ordinary function, or it can be a generator function, so that when invoked, an iterator object is returned. Inside of this generator function, each entry can be provided by using `yield`.

[The iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)

-------------------------------------------------------------------------------------------------------------------------------------

**The iterator protocol** defines a standard way to produce a sequence of values (either finite or infinite), and potentially a return value when all values have been generated.

An object is an iterator when it implements a **`next()`** method with the following semantics:

[`next()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#next)

A function that accepts zero or one argument and returns an object conforming to the `IteratorResult` interface (see below). If a non-object value gets returned (such as `false` or `undefined`) when a built-in language feature (such as `for...of`) is using the iterator, a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 (`"iterator.next() returned a non-object value"`) will be thrown.

All iterator protocol methods (`next()`, `return()`, and `throw()`) are expected to return an object implementing the `IteratorResult` interface. It must have the following properties:

[`done` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#done)

A boolean that's `false` if the iterator was able to produce the next value in the sequence. (This is equivalent to not specifying the `done` property altogether.)

Has the value `true` if the iterator has completed its sequence. In this case, `value` optionally specifies the return value of the iterator.

[`value` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#value)

Any JavaScript value returned by the iterator. Can be omitted when `done` is `true`.

In practice, neither property is strictly required; if an object without either property is returned, it's effectively equivalent to `{ done: false, value: undefined }`.

If an iterator returns a result with `done: true`, any subsequent calls to `next()` are expected to return `done: true` as well, although this is not enforced on the language level.

The `next` method can receive a value which will be made available to the method body. The only language feature that passes a value is [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
. The value passed to the `next` method of [generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
 will become the value of the corresponding `yield` expression.

Optionally, the iterator can also implement the **`return(value)`** and **`throw(exception)`** methods, which, when called, tell the iterator that the caller is done with iterating it and can perform any necessary cleanup (such as closing a database connection).

[`return(value)` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#returnvalue)

A function that accepts zero or one argument and returns an object conforming to the `IteratorResult` interface, typically with `value` equal to the `value` passed in and `done` equal to `true`. Calling this method tells the iterator that the caller does not intend to make any more `next()` calls and can perform any cleanup actions. When built-in language features call `return()` for cleanup, `value` is always `undefined`.

[`throw(exception)` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#throwexception)

A function that accepts zero or one argument and returns an object conforming to the `IteratorResult` interface, typically with `done` equal to `true`. Calling this method tells the iterator that the caller detects an error condition, and `exception` is typically an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
 instance. No built-in language feature calls `throw()` for cleanup purposes — it's a special feature of generators for the symmetry of `return`/`throw`.

**Note:** It is not possible to know reflectively (i.e., without actually calling `next()` and validating the returned result) whether a particular object implements the iterator protocol.

It is very easy to make an iterator also iterable: just implement a `[Symbol.iterator]()` method that returns `this`.

Such an object is called an _iterable iterator_. Doing so allows an iterator to be consumed by the various syntaxes expecting iterables — therefore, it is seldom useful to implement the Iterator Protocol without also implementing Iterable. (In fact, almost all syntaxes and APIs expect _iterables_, not _iterators_.) The [generator object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
 is an example:

All built-in iterators inherit from [`Iterator.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
, which implements the `[Symbol.iterator]()` method as returning `this`, so that built-in iterators are also iterable.

However, when possible, it's better for `iterable[Symbol.iterator]()` to return different iterators that always start from the beginning, like [`Set.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Symbol.iterator)
 does.

[The async iterator and async iterable protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There is another pair of protocols used for async iteration, named **async iterator** and **async iterable** protocols. They have very similar interfaces compared to the iterable and iterator protocols, except that each return value from the calls to the iterator methods is wrapped in a promise.

An object implements the async iterable protocol when it implements the following methods:

[`[Symbol.asyncIterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncIterator)

A zero-argument function that returns an object, conforming to the async iterator protocol.

An object implements the async iterator protocol when it implements the following methods:

[`next()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#next_2)

A function that accepts zero or one argument and returns a promise. The promise fulfills to an object conforming to the `IteratorResult` interface, and the properties have the same semantics as those of the sync iterator's.

[`return(value)` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#returnvalue_2)

A function that accepts zero or one argument and returns a promise. The promise fulfills to an object conforming to the `IteratorResult` interface, and the properties have the same semantics as those of the sync iterator's.

[`throw(exception)` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#throwexception_2)

A function that accepts zero or one argument and returns a promise. The promise fulfills to an object conforming to the `IteratorResult` interface, and the properties have the same semantics as those of the sync iterator's.

[Interactions between the language and iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#interactions_between_the_language_and_iteration_protocols)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The language specifies APIs that either produce or consume iterables and iterators.

### [Built-in iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#built-in_iterables)

[`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
, [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
, [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
, [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
, [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
, and [`Segments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments)
 (returned by [`Intl.Segmenter.prototype.segment()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment)
) are all built-in iterables, because each of their `prototype` objects implements a `[Symbol.iterator]()` method. In addition, the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object and some DOM collection types such as [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)
 are also iterables. Other than [`AsyncGenerator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator)
, there is no object in the core JavaScript language that is async iterable. Some web APIs, such as [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream)
, have the `Symbol.asyncIterator` method set by default.

[Generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
 return [generator objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
, which are iterable iterators. [Async generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
 return [async generator objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator)
, which are async iterable iterators.

The iterators returned from built-in iterables actually all inherit from a common class [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
, which implements the aforementioned `[Symbol.iterator]() { return this; }` method, making them all iterable iterators. The `Iterator` class also provides additional [helper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#iterator_helper_methods)
 in addition to the `next()` method required by the iterator protocol. You can inspect an iterator's prototype chain by logging it in a graphical console.

console.log(\[\]\[Symbol.iterator\]());

Array Iterator {}
  \[\[Prototype\]\]: Array Iterator     ==> This is the prototype shared by all array iterators
    next: ƒ next()
    Symbol(Symbol.toStringTag): "Array Iterator"
    \[\[Prototype\]\]: Object           ==> This is the prototype shared by all built-in iterators
      Symbol(Symbol.iterator): ƒ \[Symbol.iterator\]()
      \[\[Prototype\]\]: Object         ==> This is Object.prototype

### [Built-in APIs accepting iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#built-in_apis_accepting_iterables)

There are many APIs that accept iterables. Some examples include:

*   [`Map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Map)
    
*   [`WeakMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap/WeakMap)
    
*   [`Set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Set)
    
*   [`WeakSet()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet/WeakSet)
    
*   [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
    
*   [`Promise.allSettled()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled)
    
*   [`Promise.race()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)
    
*   [`Promise.any()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any)
    
*   [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
    
*   [`Object.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy)
    
*   [`Map.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy)
    

### [Syntaxes expecting iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#syntaxes_expecting_iterables)

Some statements and expressions expect iterables, for example the [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loops, [array and parameter spreading](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
, [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
, and [array destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
:

When built-in syntaxes are iterating an iterator, and the last result's `done` is `false` (i.e., the iterator is able to produce more values) but no more values are needed, the `return` method will get called if present. This can happen, for example, if a `break` or `return` is encountered in a `for...of` loop, or if all identifiers are already bound in an array destructuring.

Using `for...of`, array spreading, etc. on an async iterable that's not also a sync iterable (i.e., it has `[Symbol.asyncIterator]()` but no `[Symbol.iterator]()`) will throw a TypeError: x is not iterable. You must use syntaxes designed for async iterables, including [`for await...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
, [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
 in [async generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
 (but not [sync generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
), and [`Array.fromAsync()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fromAsync)
. On the other hand, these syntaxes can also take sync iterables and implicitly convert the results to promises.

[Error handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#error_handling)

-----------------------------------------------------------------------------------------------------------------------

Because iteration involves transferring control back and forth between the iterator and the consumer, error handling happens in both ways: how the consumer handles errors thrown by the iterator, and how the iterator handles errors thrown by the consumer. When you are using one of the built-in ways of iteration, the language may also throw errors because the iterable breaks certain [invariants](https://developer.mozilla.org/en-US/docs/Glossary/Invariant)
. We will describe how built-in syntaxes generate and handle errors, which can be used as a guideline for your own code if you are manually stepping the iterator.

### [Non-well-formed iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#non-well-formed_iterables)

Errors may happen when acquiring the iterator from the iterable. The language invariant enforced here is that the iterable must produce a valid iterator:

*   It has a callable `[Symbol.iterator]()` method.
*   The `[Symbol.iterator]()` method returns an object.
*   The object returned by `[Symbol.iterator]()` has a callable `next()` method.

When using built-in syntax to initiate iteration on a non-well-formed iterable, a TypeError is thrown.

For async iterables, if its `[Symbol.asyncIterator]()` property has value `undefined` or `null`, JavaScript falls back to using the `[Symbol.iterator]` property instead (and wraps the resulting iterator into an async iterator by [forwarding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#forwarding_errors)
 the methods). Otherwise, the `[Symbol.asyncIterator]` property must conform to the above invariants too.

This type of error can be prevented by first validating the iterable before attempting to iterate it. However, it's fairly rare because usually you know the type of the object you are iterating over. If you are receiving this iterable from some other code, you should just let the error propagate to the caller so they know an invalid input was provided.

### [Errors during iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#errors_during_iteration)

Most errors happen when stepping the iterator (calling `next()`). The language invariant enforced here is that the `next()` method must return an object (for async iterators, an object after awaiting). Otherwise, a TypeError is thrown.

If the invariant is broken or the `next()` method throws an error (for async iterators, it may also return a rejected promise), the error is propagated to the caller. For built-in syntaxes, the iteration in progress is aborted without retrying or cleanup (with the assumption that if the `next()` method threw the error, then it has cleaned up already). If you are manually calling `next()`, you may catch the error and retry calling `next()`, but in general you should assume the iterator is already closed.

If the caller decides to exit iteration for any reason other than the errors in the previous paragraph, such as when it enters an error state in its own code (for example, while handling an invalid value produced by the iterator), it should call the `return()` method on the iterator, if one exists. This allows the iterator to perform any cleanup. The `return()` method is only called for premature exits—if `next()` returns `done: true`, the `return()` method is not called, with the assumption that the iterator has already cleaned up.

The `return()` method might be invalid too! The language also enforces that the `return()` method must return an object and throws a TypeError otherwise. If the `return()` method throws an error, the error is propagated to the caller. However, if the `return()` method is called because the caller encountered an error in its own code, then this error overrides the error thrown by the `return()` method.

Usually, the caller implements error handling like this:

The `catch` will be able to catch errors thrown when `iterable` is not a valid iterable, when `next()` throws an error, when `return()` throws an error (if the `for` loop exits early), and when the `for` loop body throws an error.

Most iterators are implemented with generator functions, so we will demonstrate how generator functions typically handle errors:

The lack of `catch` here causes errors thrown by `doSomething()` or `doSomethingElse()` to propagate to the caller of `gen`. If these errors are caught within the generator function (which is equally advisable), the generator function can decide to continue yielding values or to exit early. However, the `finally` block is necessary for generators that keep open resources. The `finally` block is guaranteed to run, either when the last `next()` is called or when `return()` is called.

### [Forwarding errors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#forwarding_errors)

Some built-in syntaxes wrap an iterator into another iterator. They include the iterator produced by [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
, [iterator helper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#iterator_helper_methods)
 (`map()`, `filter()`, `take()`, `drop()`, and `flatMap()`), [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
, and a hidden wrapper when you use async iteration (`for await...of`, `Array.fromAsync`) on sync iterators. The wrapped iterator is then responsible for forwarding errors between the inner iterator and the caller.

*   Wrapper iterators generally directly forward the `next()` method of the inner iterator, including its return value and thrown errors. The async wrapper of a sync iterator awaits the returned object's `value` property and converts thrown errors into promise rejections. If a yielded promise rejects, the wrapper calls the inner iterator's `return()` method, if one exists, before rejecting its own promise. If the inner iterator's `next()` method itself throws, the wrapper rejects its promise without calling `return()`.
*   Wrapper iterators generally directly forward the `return()` method of the inner iterator. If the `return()` method doesn't exist on the inner iterator, it returns `{ done: true, value: undefined }` instead. In the case of iterator helpers: if the iterator helper's `next()` method has not been called, after trying to call `return()` on the inner iterator, the current iterator always returns `{ done: true, value: undefined }`. This is consistent with generator functions where execution hasn't entered the `yield*` expression yet.
*   `yield*` is the only built-in syntax that forwards the `throw()` method of the inner iterator. For information on how [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
     forwards the `return()` and `throw()` methods, see its own reference.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#examples)

-----------------------------------------------------------------------------------------------------------

### [User-defined iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#user-defined_iterables)

You can make your own iterables like this:

### [Basic iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#basic_iterator)

Iterators are stateful by nature. If you don't define it as a [generator function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
 (as the example above shows), you would likely want to encapsulate the state in a closure.

### [Infinite iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#infinite_iterator)

### [Defining an iterable with a generator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#defining_an_iterable_with_a_generator)

### [Defining an iterable with a class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#defining_an_iterable_with_a_class)

State encapsulation can be done with [private fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 as well.

### [Overriding built-in iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#overriding_built-in_iterables)

For example, a [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 is a built-in iterable object:

`String`'s [default iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Symbol.iterator)
 returns the string's code points one by one:

You can redefine the iteration behavior by supplying your own `[Symbol.iterator]()`:

Notice how redefining `[Symbol.iterator]()` affects the behavior of built-in constructs that use the iteration protocol:

### [Concurrent modifications when iterating](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#concurrent_modifications_when_iterating)

Almost all iterables have the same underlying semantic: they don't copy the data at the time when iteration starts. Rather, they keep a pointer and move it around. Therefore, if you add, delete, or modify elements in the collection while iterating over the collection, you may inadvertently change whether other _unchanged_ elements in the collection are visited. This is very similar to how [iterative array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#mutating_initial_array_in_iterative_methods)
 work.

Consider the following case using a [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)
:

Note how it never logs `key2`. This is because a `URLSearchParams` is underlyingly a list of key-value pairs. When `deleteme1` is visited and deleted, all other entries are shifted to the left by one, so `key2` occupies the position that `deleteme1` used to be in, and when the pointer moves to the next key, it lands on `key3`.

Certain iterable implementations avoid this problem by setting "tombstone" values to avoid shifting the remaining values. Consider the similar code using a `Map`:

Note how it logs all keys. This is because `Map` doesn't shift the remaining keys when one is deleted. If you want to implement something similar, here's how it may look:

**Warning:** Concurrent modifications, in general, are very bug-prone and confusing. Unless you know precisely how the iterable is implemented, it's best to avoid modifying the collection while iterating over it.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-iteration](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-iteration) |

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
     guide
*   [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    
*   [`Symbol.iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)
    
*   [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/iteration_protocols/index.md?plain=1 "Folder: en-us/web/javascript/reference/iteration_protocols (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FIteration_protocols&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fiteration_protocols%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FIteration_protocols%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fiteration_protocols%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")