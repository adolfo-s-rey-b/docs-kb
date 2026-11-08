*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#mdn-search)
    

Iterator.concat()
=================

Baseline 2026

Newly available

Since March 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Iterator.concat()`** static method creates a new [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
 object from a list of iterable objects. The new iterator yields the values from each of the input iterables in sequence.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#syntax)

------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#parameters)

[`it1`, `it2`, …, `itN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#it1)

An object that implements the [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 protocol. [Iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 which are not also iterable cannot be passed directly to this method; they must first be wrapped using [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#return_value)

A new [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
 object that yields the values from each of the input iterables in sequence.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#description)

----------------------------------------------------------------------------------------------------------------------------

The `Iterator.concat()` method is conceptually similar to `Array`'s [`concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
 method, but it operates on any kind of iterable, and returns an iterator instead of an array. This means that the iterables can be lazily iterated, avoiding unnecessary allocation or computation. It also means that, technically, you can [concatenate _infinite iterables_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#concatenating_infinite_iterables)
, but results from iterables after the first infinite iterable will never be reached.

While each iterable can be infinite, the list of iterables must be finite—and quite limited in number because engines impose a very low limit on the number of function arguments. If you need to concatenate a large—even infinite—number of iterables, use [`Iterator.prototype.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/flatMap)
 instead.

The `Iterator.concat()` method is similar in functionality to the following function, which uses the [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
 operator to yield values from each of the input iterables in sequence:

Like `yield*`, `Iterator.concat()` doesn't support arguments that are not iterable (i.e., don't have the `[Symbol.iterator]()` method). This is because `Iterator.concat()` always takes ownership over its iterators and [closes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#returnvalue)
 open iterators when the method exits. With iterable arguments, `Iterator.concat()` acquires iterators one-by-one and just closes the current iterator when the iteration is stopped. With iterator arguments, it's not clear whether the caller or `Iterator.concat()` should be responsible for closing the iterators, especially the ones that `Iterator.concat()` hasn't reached, so the method simply disallows non-iterable arguments.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#examples)

----------------------------------------------------------------------------------------------------------------------

### [Combining maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#combining_maps)

In this example, we create a new [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 that's the union of three other maps. The [`Map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Map)
 constructor accepts an iterable of key-value pairs, while the [Map iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Symbol.iterator)
 yields key-value pairs from the map, so just using `Iterator.concat()` on the maps is sufficient to create the new map.

Note that the value of key `"a"` in the resulting map is `5`. This is because the `Map` constructor uses the last value for each key.

### [Concatenating infinite iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#concatenating_infinite_iterables)

When any of the input iterables is infinite, the resulting iterator will also be infinite. This isn't immediately a problem because iterators can be consumed lazily and closed at any time, but it does mean that iterables after the first infinite iterable will never be reached.

### [Concatenating iterables of different types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#concatenating_iterables_of_different_types)

You can concatenate iterables of different types.

The elements of each iterable can also be of different types, just like arrays.

### [Concatenating non-iterable objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#concatenating_non-iterable_objects)

Non-iterable objects throw a `TypeError` when passed to `Iterator.concat()` because they don't have the `[Symbol.iterator]()` method.

Because all built-in iterators extend the [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
 class, they are all iterable and can be passed to `Iterator.concat()`.

To pass an iterator that isn't also iterable, you can wrap it using [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
.

Another option is to use [`Iterator.prototype.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/flatMap)
 instead, which automatically calls `Iterator.from()`. But be careful: you need to call `flatMap()` on an iterator, not on an array, because [`Array.prototype.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
 only supports array return values.

When implementing your own iterators, consider making them iterable by or [subclassing `Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/Iterator#subclassing_iterator)
 or adding a `[Symbol.iterator]()` method that returns `this`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-iterator.concat](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-iterator.concat) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Iterator.concat` in `core-js`](https://core-js.io/docs/features/ecmascript/iterator "External link (opens in new tab)")
    
*   [es-shims polyfill of `Iterator.concat`](https://www.npmjs.com/package/es-iterator-helpers "External link (opens in new tab)")
    
*   [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
    
*   [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
    
*   [`Array.prototype.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/iterator/concat/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/iterator/concat (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator%2Fconcat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%2Fconcat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator%2Fconcat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%2Fconcat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")