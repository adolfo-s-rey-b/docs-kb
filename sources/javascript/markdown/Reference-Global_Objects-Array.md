*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#mdn-search)
    

Array
=====

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Array`** object, as with arrays in other programming languages, enables [storing a collection of multiple items under a single variable name](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Arrays)
, and has members for [performing common array operations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#examples)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#description)

------------------------------------------------------------------------------------------------------------------

In JavaScript, arrays aren't [primitives](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 but are instead `Array` objects with the following core characteristics:

*   **JavaScript arrays are resizable** and **can contain a mix of different [data types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)
    **. (When those characteristics are undesirable, use [typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
     instead.)
*   **JavaScript arrays are not associative arrays** and so, array elements cannot be accessed using arbitrary strings as indexes, but must be accessed using nonnegative integers (or their respective string form) as indexes.
*   **JavaScript arrays are [zero-indexed](https://en.wikipedia.org/wiki/Zero-based_numbering "External link (opens in new tab)")
    **: the first element of an array is at index `0`, the second is at index `1`, and so on — and the last element is at the value of the array's [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
     property minus `1`.
*   **JavaScript [array-copy operations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#copy_an_array)
     create [shallow copies](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)
    **. (All standard built-in copy operations with _any_ JavaScript objects create shallow copies, rather than [deep copies](https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy)
    ).

### [Array indices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_indices)

`Array` objects cannot use arbitrary strings as element indexes (as in an [associative array](https://en.wikipedia.org/wiki/Associative_array "External link (opens in new tab)")
) but must use nonnegative integers (or their respective string form). Setting or accessing via non-integers will not set or retrieve an element from the array list itself, but will set or access a variable associated with that array's [object property collection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#properties)
. The array's object properties and list of array elements are separate, and the array's [traversal and mutation operations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#array_methods)
 cannot be applied to these named properties.

Array elements are object properties in the same way that `toString` is a property (to be specific, however, `toString()` is a method). Nevertheless, trying to access an element of an array as follows throws a syntax error because the property name is not valid:

JavaScript syntax requires properties beginning with a digit to be accessed using [bracket notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects#objects_and_properties)
 instead of [dot notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
. It's also possible to quote the array indices (e.g., `years['2']` instead of `years[2]`), although usually not necessary.

The `2` in `years[2]` is coerced into a string by the JavaScript engine through an implicit `toString` conversion. As a result, `'2'` and `'02'` would refer to two different slots on the `years` object, and the following example could be `true`:

Only `years['2']` is an actual array index. `years['02']` is an arbitrary string property that will not be visited in array iteration.

### [Relationship between length and numerical properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#relationship_between_length_and_numerical_properties)

A JavaScript array's [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 property and numerical properties are connected.

Several of the built-in array methods (e.g., [`join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
, [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
, [`indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)
, etc.) take into account the value of an array's [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 property when they're called.

Other methods (e.g., [`push()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)
, [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
, etc.) also result in updates to an array's [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 property.

When setting a property on a JavaScript array when the property is a valid array index and that index is outside the current bounds of the array, the engine will update the array's [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 property accordingly:

Increasing the [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 extends the array by adding empty slots without creating any new elements — not even `undefined`.

Decreasing the [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 property does, however, delete elements.

This is explained further on the [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 page.

### [Array methods and empty slots](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_methods_and_empty_slots)

Array methods have different behaviors when encountering empty slots in [sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
. In general, older methods (e.g., `forEach`) treat empty slots differently from indices that contain `undefined`.

Methods that have special treatment for empty slots include the following: [`concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
, [`copyWithin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin)
, [`every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
, [`filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
, [`flat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)
, [`flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
, [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
, [`indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)
, [`lastIndexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf)
, [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
, [`reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
, [`reduceRight()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight)
, [`reverse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)
, [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
, [`some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
, [`sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
, and [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
. Iteration methods such as `forEach` don't visit empty slots at all. Other methods, such as `concat`, `copyWithin`, etc., preserve empty slots when doing the copying, so in the end the array is still sparse.

Newer methods (e.g., `keys`) do not treat empty slots specially and treat them as if they contain `undefined`. Methods that conflate empty slots with `undefined` elements include the following: [`entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/entries)
, [`fill()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill)
, [`find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
, [`findIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)
, [`findLast()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLast)
, [`findLastIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLastIndex)
, [`includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
, [`join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
, [`keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/keys)
, [`toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toLocaleString)
, [`toReversed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toReversed)
, [`toSorted()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted)
, [`toSpliced()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSpliced)
, [`values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/values)
, and [`with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/with)
.

### [Copying methods and mutating methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#copying_methods_and_mutating_methods)

Some methods do not mutate the existing array that the method was called on, but instead return a new array. They do so by first constructing a new array and then populating it with elements. The copy always happens [_shallowly_](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)
 — the method never copies anything beyond the initially created array. Elements of the original array(s) are copied into the new array as follows:

*   Objects: the object reference is copied into the new array. Both the original and new array refer to the same object. That is, if a referenced object is modified, the changes are visible to both the new and original arrays.
*   Primitive types such as strings, numbers and booleans (not [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
    , [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
    , and [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
     objects): their values are copied into the new array.

Other methods mutate the array that the method was called on, in which case their return value differs depending on the method: sometimes a reference to the same array, sometimes the length of the new array.

The following methods create new arrays by accessing [`this.constructor[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.species)
 to determine the constructor to use: [`concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
, [`filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
, [`flat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)
, [`flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
, [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
, [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
, and [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
 (to construct the array of removed elements that's returned).

The following methods always create new arrays with the `Array` base constructor: [`toReversed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toReversed)
, [`toSorted()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted)
, [`toSpliced()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSpliced)
, and [`with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/with)
.

The following table lists the methods that mutate the original array, and the corresponding non-mutating alternative:

| Mutating method | Non-mutating alternative |
| --- | --- |
| [`copyWithin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin) | No one-method alternative |
| [`fill()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill) | No one-method alternative |
| [`pop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop) | [`slice(0, -1)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) |
| [`push(v1, v2)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push) | [`concat([v1, v2])`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat) |
| [`reverse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse) | [`toReversed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toReversed) |
| [`shift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift) | [`slice(1)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) |
| [`sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) | [`toSorted()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted) |
| [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice) | [`toSpliced()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSpliced) |
| [`unshift(v1, v2)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift) | [`toSpliced(0, 0, v1, v2)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSpliced) |

An easy way to change a mutating method into a non-mutating alternative is to use the [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
 or [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
 to create a copy first:

### [Iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)

Many array methods take a callback function as an argument. The callback function is called sequentially and at most once for each element in the array, and the return value of the callback function is used to determine the return value of the method. They all share the same signature:

Where `callbackFn` takes three arguments:

[`element`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#element)

The current element being processed in the array.

[`index`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#index)

The index of the current element being processed in the array.

[`array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array)

The array that the method was called upon.

What `callbackFn` is expected to return depends on the array method that was called.

The `thisArg` argument (defaults to `undefined`) will be used as the `this` value when calling `callbackFn`. The `this` value ultimately observable by `callbackFn` is determined according to [the usual rules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
: if `callbackFn` is [non-strict](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#no_this_substitution)
, primitive `this` values are wrapped into objects, and `undefined`/`null` is substituted with [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
. The `thisArg` argument is irrelevant for any `callbackFn` defined with an [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
, as arrow functions don't have their own `this` [binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
.

The `array` argument passed to `callbackFn` is most useful if you want to read another index during iteration, because you may not always have an existing variable that refers to the current array. You should generally not mutate the array during iteration (see [mutating initial array in iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#mutating_initial_array_in_iterative_methods)
), but you can also use this argument to do so. The `array` argument is _not_ the array that is being built, in the case of methods like `map()`, `filter()`, and `flatMap()` — there is no way to access the array being built from the callback function.

All iterative methods are [copying](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#copying_methods_and_mutating_methods)
 and [generic](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#generic_array_methods)
, although they behave differently with [empty slots](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_methods_and_empty_slots)
.

The following methods are iterative: [`every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
, [`filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
, [`find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
, [`findIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)
, [`findLast()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLast)
, [`findLastIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLastIndex)
, [`flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
, [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
, [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
, and [`some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
.

In particular, [`every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
, [`find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
, [`findIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)
, [`findLast()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLast)
, [`findLastIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLastIndex)
, and [`some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
 do not always invoke `callbackFn` on every element — they stop iteration as soon as the return value is determined.

The [`reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
 and [`reduceRight()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight)
 methods also take a callback function and run it at most once for each element in the array, but they have slightly different signatures from typical iterative methods (for example, they don't accept `thisArg`).

The [`sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
 method also takes a callback function, but it is not an iterative method. It mutates the array in-place, doesn't accept `thisArg`, and may invoke the callback multiple times on an index.

Iterative methods iterate the array like the following (with a lot of technical details omitted):

Note the following:

1.  Not all methods do the `i in this` test. The `find`, `findIndex`, `findLast`, and `findLastIndex` methods do not, but other methods do.
2.  The `length` is memorized before the loop starts. This affects how insertions and deletions during iteration are handled (see [mutating initial array in iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#mutating_initial_array_in_iterative_methods)
    ).
3.  The method doesn't memorize the array contents, so if any index is modified during iteration, the new value might be observed.
4.  The code above iterates the array in ascending order of index. Some methods iterate in descending order of index (`for (let i = length - 1; i >= 0; i--)`): `reduceRight()`, `findLast()`, and `findLastIndex()`.
5.  `reduce` and `reduceRight` have slightly different signatures and do not always start at the first/last element.

### [Generic array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#generic_array_methods)

Array methods are always generic — they don't access any internal data of the array object. They only access the array elements through the `length` property and the indexed elements. This means that they can be called on array-like objects as well.

#### Normalization of the length property

The `length` property is [converted to an integer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#integer_conversion)
 and then clamped to the range between 0 and 253 - 1. `NaN` becomes `0`, so even when `length` is not present or is `undefined`, it behaves as if it has value `0`.

The language avoids setting `length` to an [unsafe integer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
. All built-in methods will throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 if `length` will be set to a number greater than 253 - 1. However, because the [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
 property of arrays throws an error if it's set to greater than 232 - 1, the safe integer threshold is usually not reached unless the method is called on a non-array object.

Some array methods set the `length` property of the array object. They always set the value after normalization, so `length` always ends as an integer.

#### Array-like objects

The term [_array-like object_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#working_with_array-like_objects)
 refers to any object that doesn't throw during the `length` conversion process described above. In practice, such object is expected to actually have a `length` property and to have indexed elements in the range `0` to `length - 1`. (If it doesn't have all indices, it will be functionally equivalent to a [sparse array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_methods_and_empty_slots)
.) Any integer index less than zero or greater than `length - 1` is ignored when an array method operates on an array-like object.

Many DOM objects are array-like — for example, [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)
 and [`HTMLCollection`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection)
. The [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object is also array-like. You can call array methods on them even if they don't have these methods themselves.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#constructor)

------------------------------------------------------------------------------------------------------------------

[`Array()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Array)

Creates a new `Array` object.

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#static_properties)

------------------------------------------------------------------------------------------------------------------------------

[`Array[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.species)

Returns the `Array` constructor.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#static_methods)

------------------------------------------------------------------------------------------------------------------------

[`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)

Creates a new `Array` instance from an iterable or array-like object.

[`Array.fromAsync()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fromAsync)

Creates a new `Array` instance from an async iterable, iterable, or array-like object.

[`Array.isArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)

Returns `true` if the argument is an array, or `false` otherwise.

[`Array.of()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of)

Creates a new `Array` instance with a variable number of arguments, regardless of number or type of the arguments.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_properties)

----------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Array.prototype` and shared by all `Array` instances.

[`Array.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Array` instances, the initial value is the [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Array)
 constructor.

[`Array.prototype[Symbol.unscopables]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.unscopables)

Contains property names that were not included in the ECMAScript standard prior to the ES2015 version and that are ignored for [`with`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)
 statement-binding purposes.

These properties are own properties of each `Array` instance.

[`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)

Reflects the number of elements in an array.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods)

----------------------------------------------------------------------------------------------------------------------------

[`Array.prototype.at()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at)

Returns the array item at the given index. Accepts negative integers, which count back from the last item.

[`Array.prototype.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)

Returns a new array that is the calling array joined with other array(s) and/or value(s).

[`Array.prototype.copyWithin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin)

Copies a sequence of array elements within an array.

[`Array.prototype.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/entries)

Returns a new [_array iterator_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
 object that contains the key/value pairs for each index in an array.

[`Array.prototype.every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)

Returns `false` if it finds an element in the array that does not satisfy the provided testing function. Otherwise, it returns `true`.

[`Array.prototype.fill()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill)

Fills all the elements of an array from a start index to an end index with a static value.

[`Array.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

Returns a new array containing all elements of the calling array for which the provided filtering function returns `true`.

[`Array.prototype.find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)

Returns the value of the first element in the array that satisfies the provided testing function, or `undefined` if no appropriate element is found.

[`Array.prototype.findIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)

Returns the index of the first element in the array that satisfies the provided testing function, or `-1` if no appropriate element was found.

[`Array.prototype.findLast()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLast)

Returns the value of the last element in the array that satisfies the provided testing function, or `undefined` if no appropriate element is found.

[`Array.prototype.findLastIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLastIndex)

Returns the index of the last element in the array that satisfies the provided testing function, or `-1` if no appropriate element was found.

[`Array.prototype.flat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)

Returns a new array with all sub-array elements concatenated into it recursively up to the specified depth.

[`Array.prototype.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)

Returns a new array formed by applying a given callback function to each element of the calling array, and then flattening the result by one level.

[`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)

Calls a function for each element in the calling array.

[`Array.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)

Determines whether the calling array contains a value, returning `true` or `false` as appropriate.

[`Array.prototype.indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)

Returns the first (least) index at which a given element can be found in the calling array.

[`Array.prototype.join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)

Returns a new string that is the concatenation of all elements in this array, separated by commas or a specified separator string.

[`Array.prototype.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/keys)

Returns a new [_array iterator_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
 that contains the keys for each index in the calling array.

[`Array.prototype.lastIndexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf)

Returns the last (greatest) index at which a given element can be found in the calling array, or `-1` if none is found.

[`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

Returns a new array containing the results of invoking a function on every element in the calling array.

[`Array.prototype.pop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)

Removes the last element from an array and returns that element.

[`Array.prototype.push()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)

Adds one or more elements to the end of an array, and returns the new `length` of the array.

[`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

Executes a user-supplied "reducer" callback function on each element of the array (from left to right), to reduce it to a single value.

[`Array.prototype.reduceRight()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight)

Executes a user-supplied "reducer" callback function on each element of the array (from right to left), to reduce it to a single value.

[`Array.prototype.reverse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)

Reverses the order of the elements of an array _in place_. (First becomes the last, last becomes first.)

[`Array.prototype.shift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift)

Removes the first element from an array and returns that element.

[`Array.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

Extracts a section of the calling array and returns a new array.

[`Array.prototype.some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)

Returns `true` if it finds an element in the array that satisfies the provided testing function. Otherwise, it returns `false`.

[`Array.prototype.sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

Sorts the elements of an array in place and returns the array.

[`Array.prototype.splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

Adds and/or removes elements from an array.

[`Array.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toLocaleString)

Returns a localized string representing the calling array and its elements. Overrides the [`Object.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toLocaleString)
 method.

[`Array.prototype.toReversed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toReversed)

Returns a new array with the elements in reversed order, without modifying the original array.

[`Array.prototype.toSorted()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted)

Returns a new array with the elements sorted in ascending order, without modifying the original array.

[`Array.prototype.toSpliced()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSpliced)

Returns a new array with some elements removed and/or replaced at a given index, without modifying the original array.

[`Array.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toString)

Returns a string representing the calling array and its elements. Overrides the [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 method.

[`Array.prototype.unshift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift)

Adds one or more elements to the front of an array, and returns the new `length` of the array.

[`Array.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/values)

Returns a new [_array iterator_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
 object that contains the values for each index in the array.

[`Array.prototype.with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/with)

Returns a new array with the element at the given index replaced with the given value, without modifying the original array.

[`Array.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.iterator)

An alias for the [`values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/values)
 method by default.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#examples)

------------------------------------------------------------------------------------------------------------

This section provides some examples of common array operations in JavaScript.

**Note:** If you're not yet familiar with array basics, consider first reading [JavaScript First Steps: Arrays](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Arrays)
, which [explains what arrays are](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Arrays#what_is_an_array)
, and includes other examples of common array operations.

### [Create an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#create_an_array)

This example shows three ways to create new array: first using [array literal notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Array#array_literal_notation)
, then using the [`Array()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Array)
 constructor, and finally using [`String.prototype.split()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
 to build the array from a string.

### [Create a string from an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#create_a_string_from_an_array)

This example uses the [`join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
 method to create a string from the `fruits` array.

### [Access an array item by its index](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#access_an_array_item_by_its_index)

This example shows how to access items in the `fruits` array by specifying the index number of their position in the array.

### [Find the index of an item in an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#find_the_index_of_an_item_in_an_array)

This example uses the [`indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)
 method to find the position (index) of the string `"Banana"` in the `fruits` array.

### [Check if an array contains a certain item](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#check_if_an_array_contains_a_certain_item)

This example shows two ways to check if the `fruits` array contains `"Banana"` and `"Cherry"`: first with the [`includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
 method, and then with the [`indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)
 method to test for an index value that's not `-1`.

### [Append an item to an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#append_an_item_to_an_array)

This example uses the [`push()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)
 method to append a new string to the `fruits` array.

### [Remove the last item from an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#remove_the_last_item_from_an_array)

This example uses the [`pop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
 method to remove the last item from the `fruits` array.

**Note:** `pop()` can only be used to remove the last item from an array. To remove multiple items from the end of an array, see the next example.

### [Remove multiple items from the end of an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#remove_multiple_items_from_the_end_of_an_array)

This example uses the [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
 method to remove the last 3 items from the `fruits` array.

### [Truncate an array down to just its first N items](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#truncate_an_array_down_to_just_its_first_n_items)

This example uses the [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
 method to truncate the `fruits` array down to just its first 2 items.

### [Remove the first item from an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#remove_the_first_item_from_an_array)

This example uses the [`shift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift)
 method to remove the first item from the `fruits` array.

**Note:** `shift()` can only be used to remove the first item from an array. To remove multiple items from the beginning of an array, see the next example.

### [Remove multiple items from the beginning of an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#remove_multiple_items_from_the_beginning_of_an_array)

This example uses the [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
 method to remove the first 3 items from the `fruits` array.

### [Add a new first item to an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#add_a_new_first_item_to_an_array)

This example uses the [`unshift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift)
 method to add, at index `0`, a new item to the `fruits` array — making it the new first item in the array.

### [Remove a single item by index](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#remove_a_single_item_by_index)

This example uses the [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
 method to remove the string `"Banana"` from the `fruits` array — by specifying the index position of `"Banana"`.

### [Remove multiple items by index](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#remove_multiple_items_by_index)

This example uses the [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
 method to remove the strings `"Banana"` and `"Strawberry"` from the `fruits` array — by specifying the index position of `"Banana"`, along with a count of the number of total items to remove.

### [Replace multiple items in an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#replace_multiple_items_in_an_array)

This example uses the [`splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
 method to replace the last 2 items in the `fruits` array with new items.

### [Iterate over an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterate_over_an_array)

This example uses a [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loop to iterate over the `fruits` array, logging each item to the console.

But `for...of` is just one of many ways to iterate over any array; for more ways, see [Loops and iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
, and see the documentation for the [`every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
, [`filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
, [`flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
, [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
, [`reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
, and [`reduceRight()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight)
 methods — and see the next example, which uses the [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
 method.

### [Call a function on each element in an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#call_a_function_on_each_element_in_an_array)

This example uses the [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
 method to call a function on each element in the `fruits` array; the function causes each item to be logged to the console, along with the item's index number.

### [Merge multiple arrays together](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#merge_multiple_arrays_together)

This example uses the [`concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
 method to merge the `fruits` array with a `moreFruits` array, to produce a new `combinedFruits` array. Notice that `fruits` and `moreFruits` remain unchanged.

### [Copy an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#copy_an_array)

This example shows three ways to create a new array from the existing `fruits` array: first by using [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
, then by using the [`from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
 method, and then by using the [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
 method.

All built-in array-copy operations ([spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
, [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
, [`Array.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
, and [`Array.prototype.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
) create [shallow copies](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)
. If you instead want a [deep copy](https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy)
 of an array, you can use [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
 to convert the array to a JSON string, and then [`JSON.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)
 to convert the string back into a new array that's completely independent from the original array.

You can also create deep copies using the [`structuredClone()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone "structuredClone()")
 method, which has the advantage of allowing [transferable objects](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Transferable_objects)
 in the source to be _transferred_ to the new copy, rather than just cloned.

Finally, it's important to understand that assigning an existing array to a new variable doesn't create a copy of either the array or its elements. Instead the new variable is just a reference, or alias, to the original array; that is, the original array's name and the new variable name are just two names for the exact same object (and so will always evaluate as [strictly equivalent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness#strict_equality_using)
). Therefore, if you make any changes at all either to the value of the original array or to the value of the new variable, the other will change, too:

### [Creating a two-dimensional array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#creating_a_two-dimensional_array)

The following creates a chessboard as a two-dimensional array of strings. The first move is made by copying the `'p'` in `board[6][4]` to `board[4][4]`. The old position at `[6][4]` is made blank.

Here is the output:

R,N,B,Q,K,B,N,R
P,P,P,P,P,P,P,P
 , , , , , , ,
 , , , , , , ,
 , , , , , , ,
 , , , , , , ,
p,p,p,p,p,p,p,p
r,n,b,q,k,b,n,r

R,N,B,Q,K,B,N,R
P,P,P,P,P,P,P,P
 , , , , , , ,
 , , , , , , ,
 , , , ,p, , ,
 , , , , , , ,
p,p,p,p, ,p,p,p
r,n,b,q,k,b,n,r

### [Using an array to tabulate a set of values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#using_an_array_to_tabulate_a_set_of_values)

Results in

// The first column is the index
0  1    0
1  2    2
2  4    8
3  8    18
4  16   32
5  32   50
6  64   72
7  128  98
8  256  128
9  512  162

### [Creating an array using the result of a match](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#creating_an_array_using_the_result_of_a_match)

The result of a match between a [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 and a string can create a JavaScript array that has properties and elements which provide information about the match. Such an array is returned by [`RegExp.prototype.exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
 and [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
.

For example:

For more information about the result of a match, see the [`RegExp.prototype.exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
 and [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
 pages.

### [Mutating initial array in iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#mutating_initial_array_in_iterative_methods)

[Iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
 do not mutate the array on which it is called, but the function provided as `callbackFn` can. The key principle to remember is that only indexes between 0 and `arrayLength - 1` are visited, where `arrayLength` is the length of the array at the time the array method was first called, but the element passed to the callback is the value at the time the index is visited. Therefore:

*   `callbackFn` will not visit any elements added beyond the array's initial length when the call to the iterative method began.
*   Changes to already-visited indexes do not cause `callbackFn` to be invoked on them again.
*   If an existing, yet-unvisited element of the array is changed by `callbackFn`, its value passed to the `callbackFn` will be the value at the time that element gets visited. Removed elements are not visited.

**Warning:** Concurrent modifications of the kind described above frequently lead to hard-to-understand code and are generally to be avoided (except in special cases).

The following examples use the `forEach` method as an example, but other methods that visit indexes in ascending order work in the same way. We will first define a helper function:

Modification to indexes not visited yet will be visible once the index is reached:

Modification to already visited indexes does not change iteration behavior, although the array will be different afterwards:

Inserting _n_ elements at unvisited indexes that are less than the initial array length will make them be visited. The last _n_ elements in the original array that now have index greater than the initial array length will not be visited:

Inserting _n_ elements with index greater than the initial array length will not make them be visited:

Inserting _n_ elements at already visited indexes will not make them be visited, but it shifts remaining elements back by _n_, so the current index and the _n - 1_ elements before it are visited again:

Deleting _n_ elements at unvisited indexes will make them not be visited anymore. Because the array has shrunk, the last _n_ iterations will visit out-of-bounds indexes. If the method ignores non-existent indexes (see [array methods and empty slots](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_methods_and_empty_slots)
), the last _n_ iterations will be skipped; otherwise, they will receive `undefined`:

Deleting _n_ elements at already visited indexes does not change the fact that they were visited before they get deleted. Because the array has shrunk, the next _n_ elements after the current index are skipped. If the method ignores non-existent indexes, the last _n_ iterations will be skipped; otherwise, they will receive `undefined`:

For methods that iterate in descending order of index, insertion causes elements to be skipped, and deletion causes elements to be visited multiple times. Adjust the code above yourself to see the effects.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-array-objects](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#see_also)

------------------------------------------------------------------------------------------------------------

*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
    
*   [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/array (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7c2fdcaace1ab622a1055b7cc710297c452ce9ee%0A*+Document+last+modified%3A+2026-07-28T09%3A28%3A22.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")