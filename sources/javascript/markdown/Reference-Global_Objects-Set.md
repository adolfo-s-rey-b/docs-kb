*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#mdn-search)
    

Set
===

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Set`** object lets you store unique values of any type, whether [primitive values](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 or object references.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#description)

----------------------------------------------------------------------------------------------------------------

`Set` objects are collections of values. A value in the set **may only occur once**; it is unique in the set's collection. You can iterate through the elements of a set in insertion order. The _insertion order_ corresponds to the order in which each element was inserted into the set by the [`add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/add)
 method successfully (that is, there wasn't an identical element already in the set when `add()` was called).

The specification requires sets to be implemented "that, on average, provide access times that are sublinear on the number of elements in the collection". Therefore, it could be represented internally as a hash table (with O(1) lookup), a search tree (with O(log(N)) lookup), or any other data structure, as long as the complexity is better than O(N).

### [Value equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#value_equality)

Value equality is based on the [SameValueZero](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness#same-value-zero_equality)
 algorithm. (It used to use [SameValue](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness#same-value_equality_using_object.is)
, which treated `0` and `-0` as different. Check [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#browser_compatibility)
.) This means [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 is considered the same as `NaN` (even though `NaN !== NaN`) and all other values are considered equal according to the semantics of the `===` operator. Also, for object keys, equality is based on object identity. They are compared by reference, not by value. See [Using the Set object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#using_the_set_object)
 for examples.

### [Performance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#performance)

The [`has`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)
 method checks if a value is in the set, using an approach that is, on average, quicker than testing most of the elements that have previously been added to the set. In particular, it is, on average, faster than the [`Array.prototype.includes`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
 method when an array has a `length` equal to a set's `size`.

### [Set composition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set_composition)

The `Set` object provides some methods that allow you to compose sets like you would with mathematical operations. These methods include:

| Method | Return type | Mathematical equivalent | Venn diagram |
| --- | --- | --- | --- |
| [`A.difference(B)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/difference) | `Set` | A∖BA\\setminus B | ![A Venn diagram where two circles overlap. The difference of A and B is the part of A that is not overlapping B.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/difference/diagram.svg) |
| [`A.intersection(B)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/intersection) | `Set` | A∩BA\\cap B | ![A Venn diagram where two circles overlap. The intersection of A and B is the part where they overlap.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/intersection/diagram.svg) |
| [`A.symmetricDifference(B)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/symmetricDifference) | `Set` | (A∖B)∪(B∖A)(A\\setminus B)\\cup(B\\setminus A) | ![A Venn diagram where two circles overlap. The symmetric difference of A and B is the region contained by either circle but not both.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/symmetricdifference/diagram.svg) |
| [`A.union(B)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/union) | `Set` | A∪BA\\cup B | ![A Venn diagram where two circles overlap. The union of A and B is the region contained by either or both circles.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/union/diagram.svg) |
| [`A.isDisjointFrom(B)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isDisjointFrom) | `Boolean` | A∩B\=∅A\\cap B = \\empty | ![A Venn diagram with two circles. A and B are disjoint because the circles have no region of overlap.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isdisjointfrom/diagram.svg) |
| [`A.isSubsetOf(B)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isSubsetOf) | `Boolean` | A⊆BA\\subseteq B | ![A Venn diagram with two circles. A is a subset of B because A is completely contained in B.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/issubsetof/diagram.svg) |
| [`A.isSupersetOf(B)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isSupersetOf) | `Boolean` | A⊇BA\\supseteq B | ![A Venn diagram with two circles. A is a superset of B because B is completely contained in A.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/issupersetof/diagram.svg) |

To make them more generalizable, these methods don't just accept `Set` objects, but anything that's [set-like](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_objects)
.

### [Set-like objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_objects)

All [set composition methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set_composition)
 require [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 to be an actual `Set` instance, but their arguments just need to be set-like. A _set-like object_ is an object that provides the following:

*   A [`size`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/size)
     property that contains a number.
*   A [`has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)
     method that takes an element and returns a boolean.
*   A [`keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/keys)
     method that returns an [iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
     of the elements in the set.

For example, [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 objects are set-like because they also have [`size`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/size)
, [`has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/has)
, and [`keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/keys)
, so they behave just like sets of keys when used in set methods:

**Note:** The set-like protocol invokes the `keys()` method instead of [`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Symbol.iterator)
 to produce elements. This is to make maps valid set-like objects, because for maps, the iterator produces _entries_ but the `has()` method takes _keys_.

[Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 are not set-like because they don't have a `has()` method or the `size` property, and their `keys()` method produces indices instead of elements. [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
 objects are also not set-like because they don't have a `keys()` method.

### [Set-like browser APIs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis)

Browser **`Set`\-like objects** (or "setlike objects") are [Web API](https://developer.mozilla.org/en-US/docs/Web/API)
 interfaces that behave in many ways like a `Set`.

Just like `Set`, elements can be iterated in the same order that they were added to the object. `Set`\-like objects and `Set` also have properties and methods that share the same name and behavior. However unlike `Set` they only allow a specific predefined type for each entry.

The allowed types are set in the specification IDL definition. For example, [`GPUSupportedFeatures`](https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedFeatures)
 is a `Set`\-like object that must use strings as the key/value. This is defined in the specification IDL below:

`Set`\-like objects are either read-only or read-writable (see the `readonly` keyword in the IDL above).

*   Read-only `Set`\-like objects have the property [`size`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/size)
    , and the methods: [`entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/entries)
    , [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/forEach)
    , [`has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)
    , [`keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/keys)
    , [`values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values)
    , and [`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Symbol.iterator)
    .
*   Writeable `Set`\-like objects additionally have the methods: [`clear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/clear)
    , [`delete()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete)
    , and [`add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/add)
    .

The methods and properties have the same behavior as the equivalent entities in `Set`, except for the restriction on the types of the entry.

The following are examples of read-only `Set`\-like browser objects:

*   [`GPUSupportedFeatures`](https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedFeatures)
    
*   [`XRAnchorSet`](https://developer.mozilla.org/en-US/docs/Web/API/XRAnchorSet)
    

The following are examples of writable `Set`\-like browser objects:

*   [`CustomStateSet`](https://developer.mozilla.org/en-US/docs/Web/API/CustomStateSet)
    
*   [`FontFaceSet`](https://developer.mozilla.org/en-US/docs/Web/API/FontFaceSet)
    
*   [`Highlight`](https://developer.mozilla.org/en-US/docs/Web/API/Highlight)
    
*   [`ViewTransitionTypeSet`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransitionTypeSet)
    

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#constructor)

----------------------------------------------------------------------------------------------------------------

[`Set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Set)

Creates a new `Set` object.

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#static_properties)

----------------------------------------------------------------------------------------------------------------------------

[`Set[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Symbol.species)

The constructor function that is used to create derived objects.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#instance_properties)

--------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Set.prototype` and shared by all `Set` instances.

[`Set.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Set` instances, the initial value is the [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Set)
 constructor.

[`Set.prototype.size`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/size)

Returns the number of values in the `Set` object.

[`Set.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Set"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#instance_methods)

--------------------------------------------------------------------------------------------------------------------------

[`Set.prototype.add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/add)

Inserts the specified value into this set, if it is not already present.

[`Set.prototype.clear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/clear)

Removes all elements from the `Set` object.

[`Set.prototype.delete()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete)

Removes the specified value from this set, if it is in the set.

[`Set.prototype.difference()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/difference)

Takes a set and returns a new set containing elements in this set but not in the given set.

[`Set.prototype.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/entries)

Returns a new iterator object that contains **an array of `[value, value]`** for each element in the `Set` object, in insertion order. This is similar to the [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 object, so that each entry's _key_ is the same as its _value_ for a `Set`.

[`Set.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/forEach)

Calls `callbackFn` once for each value present in the `Set` object, in insertion order. If a `thisArg` parameter is provided, it will be used as the `this` value for each invocation of `callbackFn`.

[`Set.prototype.has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)

Returns a boolean indicating whether the specified value exists in this `Set` or not.

[`Set.prototype.intersection()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/intersection)

Takes a set and returns a new set containing elements in both this set and the given set.

[`Set.prototype.isDisjointFrom()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isDisjointFrom)

Takes a set and returns a boolean indicating if this set has no elements in common with the given set.

[`Set.prototype.isSubsetOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isSubsetOf)

Takes a set and returns a boolean indicating if all elements of this set are in the given set.

[`Set.prototype.isSupersetOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/isSupersetOf)

Takes a set and returns a boolean indicating if all elements of the given set are in this set.

[`Set.prototype.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/keys)

An alias for [`Set.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values)
.

[`Set.prototype.symmetricDifference()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/symmetricDifference)

Takes a set and returns a new set containing elements which are in either this set or the given set, but not in both.

[`Set.prototype.union()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/union)

Takes a set and returns a new set containing elements which are in either or both of this set and the given set.

[`Set.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values)

Returns a new iterator object that yields the **values** for each element in the `Set` object in insertion order.

[`Set.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/Symbol.iterator)

Returns a new iterator object that yields the **values** for each element in the `Set` object in insertion order.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#examples)

----------------------------------------------------------------------------------------------------------

### [Using the Set object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#using_the_set_object)

### [Iterating sets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#iterating_sets)

The iteration over a set visits elements in insertion order.

### [Implementing basic set operations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#implementing_basic_set_operations)

### [Relation to arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#relation_to_arrays)

### [Remove duplicate elements from an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#remove_duplicate_elements_from_an_array)

### [Relation to strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#relation_to_strings)

### [Use a set to ensure the uniqueness of a list of values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#use_a_set_to_ensure_the_uniqueness_of_a_list_of_values)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-set-objects](https://tc39.es/ecma262/multipage/keyed-collections.html#sec-set-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#see_also)

----------------------------------------------------------------------------------------------------------

*   [Polyfill of `Set` in `core-js`](https://core-js.io/docs/features/ecmascript/collections#h-set "External link (opens in new tab)")
    
*   [es-shims polyfill of `Set`](https://www.npmjs.com/package/es-set "External link (opens in new tab)")
    
*   [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
    
*   [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
    
*   [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/set/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/set (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FSet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FSet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")