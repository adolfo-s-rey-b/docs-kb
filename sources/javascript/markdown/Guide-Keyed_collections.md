*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#mdn-search)
    

Keyed collections
=================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
    

This chapter introduces collections of data which are indexed by a key; `Map` and `Set` objects contain elements which are iterable in the order of insertion.

[Maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#maps)

---------------------------------------------------------------------------------------------

### [Map object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#map_object)

A [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 object is a key/value map that can iterate its elements in insertion order.

The following code shows some basic operations with a `Map`. See also the [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 reference page for more examples and the complete API. You can use a [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loop to return an array of `[key, value]` for each iteration.

### [Object and Map compared](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#object_and_map_compared)

Traditionally, [objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
 have been used to map strings to values. Objects allow you to set keys to values, retrieve those values, delete keys, and detect whether something is stored at a key. `Map` objects, however, have a few more advantages that make them better maps.

*   The keys of an `Object` are [strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
     or [symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
    , whereas they can be of any value for a `Map`.
*   You can get the `size` of a `Map` easily, while you have to manually keep track of size for an `Object`.
*   The iteration of maps is in insertion order of the elements.
*   An `Object` has a prototype, so there are default keys in the map. (This can be bypassed using `map = Object.create(null)`.)

These three tips can help you to decide whether to use a `Map` or an `Object`:

*   Use maps over objects when keys are unknown until run time, especially if the keys come from external input.
*   Maps support keys and values of any type and do not require keys to be serializable to strings or symbols.
*   Use objects when the shape is known ahead of time and all keys are expressible as strings.

### [WeakMap object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#weakmap_object)

A [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
 is a collection of key/value pairs whose keys must be objects or [non-registered symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry)
, with values of any arbitrary [JavaScript type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)
, and which does not create strong references to its keys. That is, an object's presence as a key in a `WeakMap` does not prevent the object from being garbage collected. Once an object used as a key has been collected, its corresponding values in any `WeakMap` become candidates for garbage collection as well — as long as they aren't strongly referred to elsewhere. The only primitive type that can be used as a `WeakMap` key is symbol — more specifically, [non-registered symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry)
 — because non-registered symbols are guaranteed to be unique and cannot be re-created.

The `WeakMap` API is essentially the same as the `Map` API. However, a `WeakMap` doesn't allow observing the liveness of its keys, which is why it doesn't allow enumeration. So there is no method to obtain a list of the keys in a `WeakMap`. If there were, the list would depend on the state of garbage collection, introducing non-determinism.

For more information and example code, see also "Why WeakMap?" on the [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
 reference page.

One use case of `WeakMap` objects is to store private data for an object, or to hide implementation details. In the following example, the private data and methods belong inside the object and are stored in the `privates` object, which is a `WeakMap`. Everything exposed on the instance and prototype is public; everything else is inaccessible from the outside world because `privates` is not exported from the module.

**Note:** This use case can now be implemented with [classes and private fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
.

[Sets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#sets)

---------------------------------------------------------------------------------------------

### [Set object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#set_object)

[`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
 objects are collections of unique values. You can iterate its elements in insertion order. A value in a `Set` may only occur once; it is unique in the `Set`'s collection.

The following code shows some basic operations with a `Set`. See also the [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
 reference page for more examples and the complete API.

### [Converting between Array and Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#converting_between_array_and_set)

You can create an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 from a Set using [`Array.from`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
 or the [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
. Also, the `Set` constructor accepts an `Array` to convert in the other direction.

**Note:** `Set` objects store _unique values_—so any duplicate elements from an Array are deleted when converting!

### [Array and Set compared](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#array_and_set_compared)

Traditionally, a set of elements has been stored in arrays in JavaScript in a lot of situations. The `Set` object, however, has some advantages:

*   Deleting Array elements by value (`arr.splice(arr.indexOf(val), 1)`) is very slow.
*   `Set` objects let you delete elements by their value. With an array, you would have to `splice` based on an element's index.
*   The value [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
     cannot be found with `indexOf` in an array.
*   `Set` objects store unique values. You don't have to manually keep track of duplicates.

### [WeakSet object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#weakset_object)

[`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
 objects are collections of garbage-collectable values, including objects and [non-registered symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#shared_symbols_in_the_global_symbol_registry)
. A value in the `WeakSet` may only occur once. It is unique in the `WeakSet`'s collection.

The main differences to the [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
 object are:

*   In contrast to `Sets`, `WeakSets` are **collections of _objects or symbols only_**, and not of arbitrary values of any type.
*   The `WeakSet` is _weak_: References to objects in the collection are held weakly. If there is no other reference to an object stored in the `WeakSet`, they can be garbage collected. That also means that there is no list of current objects stored in the collection.
*   `WeakSets` are not enumerable.

The use cases of `WeakSet` objects are limited. They will not leak memory, so it can be safe to use DOM elements as a key and mark them for tracking purposes, for example.

[Key and value equality of Map and Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections#key_and_value_equality_of_map_and_set)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Both the key equality of `Map` objects and the value equality of `Set` objects are based on the [SameValueZero algorithm](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness#same-value-zero_equality)
:

*   Equality works like the identity comparison operator `===`.
*   `-0` and `+0` are considered equal.
*   [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
     is considered equal to itself (contrary to `===`).

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/keyed_collections/index.md?plain=1 "Folder: en-us/web/javascript/guide/keyed_collections (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FKeyed_collections&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fkeyed_collections%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FKeyed_collections%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fkeyed_collections%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1aaf97a83f7db21f5067daa9dcb1f1faa3613aaa%0A*+Document+last+modified%3A+2026-08-11T08%3A22%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")