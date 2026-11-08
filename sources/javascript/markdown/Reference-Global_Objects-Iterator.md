*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#mdn-search)
    

Iterator
========

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

An **`Iterator`** object is an object that conforms to the [iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 by providing a `next()` method that returns an iterator result object. All built-in iterators inherit from the `Iterator` class. The `Iterator` class provides a [`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/Symbol.iterator)
 method that returns the iterator object itself, making the iterator also [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
. It also provides some helper methods for working with iterators.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#description)

---------------------------------------------------------------------------------------------------------------------

The following are all built-in JavaScript iterators:

*   The _Array Iterator_ returned by [`Array.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/values)
    , [`Array.prototype.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/keys)
    , [`Array.prototype.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/entries)
    , [`Array.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.iterator)
    , [`TypedArray.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/values)
    , [`TypedArray.prototype.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/keys)
    , [`TypedArray.prototype.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/entries)
    , [`TypedArray.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/Symbol.iterator)
    , and [`arguments[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/Symbol.iterator)
    .
*   The _String Iterator_ returned by [`String.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Symbol.iterator)
    .
*   The _Map Iterator_ returned by [`Map.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/values)
    , [`Map.prototype.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/keys)
    , [`Map.prototype.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/entries)
    , and [`Map.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Symbol.iterator)
    .
*   The _Set Iterator_ returned by [`Set.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values)
    , [`Set.prototype.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/keys)
    , [`Set.prototype.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/entries)
    , and [`Set.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Symbol.iterator)
    .
*   The _RegExp String Iterator_ returned by [`RegExp.prototype[Symbol.matchAll]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.matchAll)
     and [`String.prototype.matchAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)
    .
*   The [`Generator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
     object returned by [generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    .
*   The _Segments Iterator_ returned by the [`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/Symbol.iterator)
     method of the [`Segments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments)
     object returned by [`Intl.Segmenter.prototype.segment()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment)
    .
*   The _Iterator Helper_ returned by iterator helper methods such as [`Iterator.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/filter)
     and [`Iterator.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/map)
    .

Web APIs may return iterators too. Some reuse core JavaScript iterators while others define their own iterators. For example:

*   [Array-Like](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array-like_objects)
     objects such as [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)
     return an _Array Iterator_ from their respective methods `keys()`, `values()`, `entries()`, and `[Symbol.iterator]()`.
*   [Map-Like](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map-like_browser_apis)
     objects from Web APIs such as [`Headers`](https://developer.mozilla.org/en-US/docs/Web/API/Headers)
     return their own iterator type like _Headers Iterator_ from their respective methods `keys()`, `values()`, `entries()`, and `[Symbol.iterator]()`.
*   [Set-Like](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis)
     objects from Web APIs such as [`FontFaceSet`](https://developer.mozilla.org/en-US/docs/Web/API/FontFaceSet)
     return their own iterator type like _FontFaceSet Iterator_ from their respective methods `keys()`, `values()`, `entries()`, and `[Symbol.iterator]()`.

**Note:** [`NodeIterator`](https://developer.mozilla.org/en-US/docs/Web/API/NodeIterator)
 and other old interfaces are named as such but do not conform to the [iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 or [iterable protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
.

Each of these iterators have a distinct prototype object, which defines the `next()` method used by the particular iterator. For example, all string iterator objects inherit from a hidden object `StringIteratorPrototype`, which has a `next()` method that iterates this string by code points. `StringIteratorPrototype` also has a [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property whose initial value is the string `"String Iterator"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
. Similarly, other iterator prototypes also have their own `[Symbol.toStringTag]` values, which are the same as the names given above.

All of these prototype objects inherit from `Iterator.prototype`, which provides a [`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)
 method that returns the iterator object itself, making the iterator also [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
.

### [Iterator helper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#iterator_helper_methods)

**Note:** These methods are _iterator_ helpers, not _iterable_ helpers, because the only requirement for an object to be iterable is just the presence of a `[Symbol.iterator]()` method. There is no shared prototype to install these methods on.

The `Iterator` class itself provides some helper methods for working with iterators. For example, you may be tempted to do the following:

This first converts the iterator returned by [`Map.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/values)
 to an array, then uses the [`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
 method to calculate the sum. However, this both creates an intermediate array and iterates the array twice. Instead, you can use the `reduce()` method of the iterator itself:

This method may be more efficient, especially memory-wise, because it only iterates the iterator once, without memorizing any intermediate values. Iterator helper methods are necessary to work with infinite iterators:

You cannot convert `seq` to an array, because it is infinite. Instead, you can use the `find()` method of the iterator itself, which only iterates `seq` as far as necessary to find the first value that satisfies the condition.

You will find many iterator methods analogous to array methods, such as:

| Iterator method | Array method |
| --- | --- |
| [`Iterator.prototype.every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/every) | [`Array.prototype.every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every) |
| [`Iterator.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/filter) | [`Array.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) |
| [`Iterator.prototype.find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/find) | [`Array.prototype.find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find) |
| [`Iterator.prototype.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/flatMap) | [`Array.prototype.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap) |
| [`Iterator.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/forEach) | [`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) |
| [`Iterator.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/includes) | [`Array.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes) |
| [`Iterator.prototype.join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/join) | [`Array.prototype.join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join) |
| [`Iterator.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/map) | [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) |
| [`Iterator.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/reduce) | [`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) |
| [`Iterator.prototype.some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/some) | [`Array.prototype.some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some) |

[`Iterator.prototype.drop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/drop)
 and [`Iterator.prototype.take()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/take)
 combined are somewhat analogous to [`Array.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
.

### [Iterator helper objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#iterator_helper_objects)

**Note:** _Iterator helper objects_ and _iterator helper methods_ are two different concepts. An Iterator helper object is detectable at runtime, while "iterator helper method" is just a name for a set of methods for comprehension. _Iterator helper_ may refer to either the object or the method, depending on the context.

Among the iterator helper methods, [`filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/filter)
, [`flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/flatMap)
, [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/map)
, [`drop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/drop)
, and [`take()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/take)
 return a new _Iterator Helper_ object. The iterator helper is also an `Iterator` instance, making these helper methods chainable. All iterator helper objects inherit from a common prototype object, which implements the iterator protocol:

[`next()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#next)

Calls the `next()` method of the underlying iterator, applies the helper method to the result, and returns the result.

[`return()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#return)

Calls the `return()` method of the underlying iterator, and returns the result.

The iterator helper shares the same data source as the underlying iterator, so iterating the iterator helper causes the underlying iterator to be iterated as well. There is no way to "fork" an iterator to allow it to be iterated multiple times.

### [Proper iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#proper_iterators)

There are two kinds of "iterators": objects that conform to the [iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 (which, at its minimum, only requires the presence of a `next()` method), and objects that inherit from the `Iterator` class, which enjoy the helper methods. They do not entail each other — objects that inherit from `Iterator` do not automatically become iterators, because the `Iterator` class does not define a `next()` method. Instead, the object needs to define a `next()` method itself. A _proper iterator_ is one that both conforms to the iterator protocol and inherits from `Iterator`, and most code expect iterators to be proper iterators and iterables to return proper iterators. To create proper iterators, define a class that extends [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/Iterator)
, or use the [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
 method.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#constructor)

---------------------------------------------------------------------------------------------------------------------

[`Iterator()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/Iterator)

Intended to be [extended](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
 by other classes that create iterators. Throws an error when constructed by itself.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#static_methods)

---------------------------------------------------------------------------------------------------------------------------

[`Iterator.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat)

Creates a new `Iterator` object from a list of iterable objects. The new iterator yields the values from each of the input iterables in sequence.

[`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)

Creates a new `Iterator` object from an iterator or iterable object.

[`Iterator.zip()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip)

Creates a new `Iterator` object that aggregates elements from multiple iterable objects by yielding arrays containing elements at the same position.

[`Iterator.zipKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed)

Creates a new `Iterator` object that aggregates elements from multiple iterable objects by yielding objects containing elements at the same position, with keys specified by the input.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#instance_properties)

-------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Iterator.prototype` and shared by all `Iterator` instances.

[`Iterator.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Iterator` instances, the initial value is the [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/Iterator)
 constructor.

[`Iterator.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#iterator.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Iterator"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

**Note:** Unlike the `[Symbol.toStringTag]` on most built-in classes, `Iterator.prototype[Symbol.toStringTag]` is writable for web compatibility reasons.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#instance_methods)

-------------------------------------------------------------------------------------------------------------------------------

[`Iterator.prototype.chunks()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/chunks)

Returns a new iterator helper object that splits the elements from the original iterator into consecutive array chunks. Each time the helper is iterated, it gets the specified number of elements from the underlying iterator and yields them together.

[`Iterator.prototype.drop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/drop)

Returns a new iterator helper object that skips the given number of elements at the start of this iterator.

[`Iterator.prototype.every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/every)

Returns `false` if it finds an element that does not satisfy the provided testing function. Otherwise, if the iterator is exhausted without finding such an element, it returns `true`.

[`Iterator.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/filter)

Returns a new iterator helper object that yields only those elements of the iterator for which the provided callback function returns `true`.

[`Iterator.prototype.find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/find)

Returns the first element produced by the iterator that satisfies the provided testing function. If no values satisfy the testing function, [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 is returned.

[`Iterator.prototype.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/flatMap)

Returns a new iterator helper object that takes each element in the original iterator, runs it through a mapping function, and yields elements returned by the mapping function (which are contained in another iterator or iterable).

[`Iterator.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/forEach)

Executes a provided function once for each element produced by the iterator.

[`Iterator.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/includes)

Returns `true` if an element produced by the iterator is equal to the given value. Otherwise, if the iterator is exhausted without finding such an element, it returns `false`.

[`Iterator.prototype.join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/join)

Returns a string that is the concatenation of all elements produced by the iterator, separated by commas or a specified separator string.

[`Iterator.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/map)

Returns a new iterator helper object that yields elements of the iterator, each transformed by a mapping function.

[`Iterator.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/reduce)

Executes a user-supplied "reducer" callback function on each element produced by the iterator, passing in the return value from the calculation on the preceding element. The final result of running the reducer across all elements is a single value.

[`Iterator.prototype.some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/some)

Returns `true` if it finds an element that satisfies the provided testing function. Otherwise, if the iterator is exhausted without finding such an element, it returns `false`.

[`Iterator.prototype.take()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/take)

Returns a new iterator helper object that yields the given number of elements in this iterator and then terminates.

[`Iterator.prototype.toArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/toArray)

Creates a new [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 instance populated with the elements yielded from the iterator.

[`Iterator.prototype.windows()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows)

Returns a new iterator helper object that yields a sliding window of elements. Each time the helper is iterated, it yields an array removing the first element from the previous iteration and adding the next element from the original iterator.

[`Iterator.prototype[Symbol.dispose]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/Symbol.dispose)

Calls the `return()` method of `this`, if it exists. This implements the _disposable protocol_ and allows it to be disposed when used with [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 or [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
.

[`Iterator.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/Symbol.iterator)

Returns the iterator object itself. This allows iterator objects to also be iterable.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#examples)

---------------------------------------------------------------------------------------------------------------

### [Using an iterator as an iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#using_an_iterator_as_an_iterable)

All built-in iterators are also iterable, so you can use them in a `for...of` loop:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-iterator-objects](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-iterator-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Iterator` in `core-js`](https://core-js.io/docs/features/ecmascript/iterator "External link (opens in new tab)")
    
*   [es-shims polyfill of `Iterator` and associated helpers](https://www.npmjs.com/package/es-iterator-helpers "External link (opens in new tab)")
    
*   [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    
*   [Iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/iterator/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/iterator (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")