*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#mdn-search)
    

TypedArray
==========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **_TypedArray_** object describes an array-like view of an underlying [binary data buffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
. There is no global property named `TypedArray`, nor is there a directly visible `TypedArray` constructor. Instead, there are a number of different global properties, whose values are typed array constructors for specific element types, listed below. On the following pages you will find common properties and methods that can be used with any typed array containing elements of any type.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#description)

-----------------------------------------------------------------------------------------------------------------------

The `TypedArray` constructor (often referred to as `%TypedArray%` to indicate its "intrinsicness", since it does not correspond to any global exposed to a JavaScript program) serves as the common superclass of all `TypedArray` subclasses. Think about `%TypedArray%` as an "abstract class" providing a common interface of utility methods for all typed array subclasses. This constructor is not directly exposed: there is no global `TypedArray` property. It is only accessible through `Object.getPrototypeOf(Int8Array)` and similar.

When creating an instance of a `TypedArray` subclass (e.g., `Int8Array`), an array buffer is created internally in memory or, if an `ArrayBuffer` object is given as constructor argument, that `ArrayBuffer` is used instead. The buffer address is saved as an internal property of the instance and all the methods of `%TypedArray%.prototype` will set and get values based on that array buffer address.

### [TypedArray objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#typedarray_objects)

| Type | Value Range | Size in bytes | Web IDL type |
| --- | --- | --- | --- |
| [`Int8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array) | \-128 to 127 | 1   | `byte` |
| [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) | 0 to 255 | 1   | `octet` |
| [`Uint8ClampedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray) | 0 to 255 | 1   | `octet` |
| [`Int16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array) | \-32768 to 32767 | 2   | `short` |
| [`Uint16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array) | 0 to 65535 | 2   | `unsigned short` |
| [`Int32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array) | \-2147483648 to 2147483647 | 4   | `long` |
| [`Uint32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array) | 0 to 4294967295 | 4   | `unsigned long` |
| [`Float16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float16Array) | `-65504` to `65504` | 2   | N/A |
| [`Float32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) | `-3.4e38` to `3.4e38` | 4   | `unrestricted float` |
| [`Float64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) | `-1.8e308` to `1.8e308` | 8   | `unrestricted double` |
| [`BigInt64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array) | \-263 to 263 - 1 | 8   | `bigint` |
| [`BigUint64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array) | 0 to 264 - 1 | 8   | `bigint` |

### [Value encoding and normalization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#value_encoding_and_normalization)

All typed arrays operate on `ArrayBuffer`s, where you can observe the exact byte representation of each element, so how the numbers are encoded in binary format is significant.

*   Unsigned integer arrays (`Uint8Array`, `Uint16Array`, `Uint32Array`, and `BigUint64Array`) store the number directly in binary.
*   Signed integer arrays (`Int8Array`, `Int16Array`, `Int32Array`, and `BigInt64Array`) store the number using [two's complement](https://en.wikipedia.org/wiki/Two's_complement "External link (opens in new tab)")
    .
*   Floating-point arrays (`Float16Array`, `Float32Array`, and `Float64Array`) store the number using [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754 "External link (opens in new tab)")
     floating-point format. The [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_encoding)
     reference has more information about the exact format. JavaScript numbers use double precision floating point format by default, which is the same as `Float64Array`. `Float32Array` uses 23 (instead of 52) bits for the mantissa and 8 (instead of 11) bits for the exponent. `Float16Array` uses 10 bits for the mantissa and 5 bits for the exponent. Note that the spec requires all [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
     values to use the same bit encoding, but the exact bit pattern is implementation-dependent.
*   `Uint8ClampedArray` is a special case. It stores the number in binary like `Uint8Array` does, but when you store a number outside the range, it _clamps_ the number to the range 0 to 255 by mathematical value, instead of truncating the most significant bits.

All typed arrays except `Int8Array`, `Uint8Array`, and `Uint8ClampedArray` store each element using multiple bytes. These bytes can either be ordered from most significant to least significant (big-endian) or from least significant to most significant (little-endian). See [Endianness](https://developer.mozilla.org/en-US/docs/Glossary/Endianness)
 for more explanation. Typed arrays always use the platform's native byte order. If you want to specify the endianness when writing and reading from buffers, you should use a [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)
 instead.

When writing to these typed arrays, values that are outside the representable range are normalized.

*   All integer arrays (except `Uint8ClampedArray`) use [fixed-width number conversion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#fixed-width_number_conversion)
    , which first truncates the decimal part of the number and then takes the lowest bits.
*   `Uint8ClampedArray` first clamps the number to the range 0 to 255 (values greater than 255 become 255 and values less than 0 become 0). It then _rounds_ (instead of flooring) the result to the nearest integer, with half-to-even; meaning if the number is exactly between two integers, it rounds to the nearest even integer. For example, `0.5` becomes `0`, `1.5` becomes `2`, and `2.5` becomes `2`.
*   `Float16Array` and `Float32Array` perform a "round to even" to convert 64-bit floating point numbers to 32-bit and 16-bit. This is the same algorithm as provided by [`Math.fround()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/fround)
     and [`Math.f16round()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/f16round)
    .

### [Behavior when viewing a resizable buffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#behavior_when_viewing_a_resizable_buffer)

When a `TypedArray` is created as a view of a [resizable buffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer#resizing_arraybuffers)
, resizing the underlying buffer will have different effects on the size of the `TypedArray` depending on whether the `TypedArray` is constructed as length-tracking.

If a typed array is created without a specific size by omitting the third parameter or passing `undefined`, the typed array will become _length-tracking_, and will automatically resize to fit the underlying `buffer` as the latter is resized:

If a typed array is created with a specific size using the third `length` parameter, it won't resize to contain the `buffer` as the latter is grown:

When a `buffer` is shrunk, the viewing typed array may become out of bounds, in which case the typed array's observed size will decrease to 0. This is the only case where a non-length-tracking typed array's length may change.

If you then grow the `buffer` again to bring the typed array back in bounds, the typed array's size will be restored to its original value.

The same can happen for length-tracking typed arrays as well, if the buffer is shrunk beyond the `byteOffset`.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#constructor)

-----------------------------------------------------------------------------------------------------------------------

This object cannot be instantiated directly — attempting to construct it with `new` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

Instead, you create an instance of a typed array of a particular type, such as an [`Int8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array)
 or a [`BigInt64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array)
. These objects all have a common syntax for their constructors:

Where `TypedArray` is a constructor for one of the concrete types.

**Note:** All `TypedArray` subclasses' constructors can only be constructed with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. Attempting to call one without `new` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#parameters)

[`typedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#typedarray)

When called with an instance of a `TypedArray` subclass, the `typedArray` gets copied into a new typed array. For a non-[bigint](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 `TypedArray` constructor, the `typedArray` parameter can only be of one of the non-[bigint](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 types (such as [`Int32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array)
). Similarly, for a [bigint](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 `TypedArray` constructor ([`BigInt64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array)
 or [`BigUint64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array)
), the `typedArray` parameter can only be of one of the [bigint](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 types. Each value in `typedArray` is converted to the corresponding type of the constructor before being copied into the new array. The length of the new typed array will be same as the length of the `typedArray` argument.

[`object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#object)

When called with an object that's not a `TypedArray` instance, a new typed array is created in the same way as the [`TypedArray.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from)
 method.

[`length` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#length)

When called with a non-object, the parameter will be treated as a number specifying the length of the typed array. An internal array buffer is created in memory, of size `length` multiplied by [`BYTES_PER_ELEMENT`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/BYTES_PER_ELEMENT)
 bytes, filled with zeros. Omitting all parameters is equivalent to using `0` as `length`.

[`buffer`, `byteOffset` Optional, `length` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#buffer)

When called with an [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
 or [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)
 instance, and optionally a `byteOffset` and a `length` argument, a new typed array view is created that views the specified buffer. The `byteOffset` (in bytes) and `length` (in number of elements, each occupying [`BYTES_PER_ELEMENT`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/BYTES_PER_ELEMENT)
 bytes) parameters specify the memory range that will be exposed by the typed array view. If both are omitted, all of `buffer` is viewed; if only `length` is omitted, the remainder of `buffer` starting from `byteOffset` is viewed. If `length` is omitted, the typed array becomes [length-tracking](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#behavior_when_viewing_a_resizable_buffer)
.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#exceptions)

All `TypeArray` subclass constructors operate in the same way. They would all throw the following exceptions:

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown in one of the following cases:

*   A `typedArray` is passed but it is a [bigint](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
     type while the current constructor is not, or vice versa.
*   A `typedArray` is passed but the buffer it's viewing is detached, or a detached `buffer` is directly passed.

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown in one of the following cases:

*   The new typed array's length is too large.
*   The length of `buffer` (if the `length` parameter is not specified) or `byteOffset` is not an integral multiple of the new typed array's element size.
*   `byteOffset` is not a valid array index (an integer between 0 and 253 - 1).
*   When creating a view from a buffer, the bounds are outside the buffer. In other words, `byteOffset + length * TypedArray.BYTES_PER_ELEMENT > buffer.byteLength`.

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#static_properties)

-----------------------------------------------------------------------------------------------------------------------------------

These properties are defined on the `TypedArray` constructor object and are thus shared by all `TypedArray` subclass constructors.

[`TypedArray[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/Symbol.species)

The constructor function used to create derived objects.

All `TypedArray` subclasses also have the following static properties:

[`TypedArray.BYTES_PER_ELEMENT`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/BYTES_PER_ELEMENT)

Returns a number value of the element size for the different `TypedArray` objects.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#static_methods)

-----------------------------------------------------------------------------------------------------------------------------

These methods are defined on the `TypedArray` constructor object and are thus shared by all `TypedArray` subclass constructors.

[`TypedArray.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from)

Creates a new `TypedArray` from an array-like or iterable object. See also [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
.

[`TypedArray.of()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/of)

Creates a new `TypedArray` with a variable number of arguments. See also [`Array.of()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of)
.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#instance_properties)

---------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `TypedArray.prototype` and shared by all `TypedArray` subclass instances.

[`TypedArray.prototype.buffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/buffer)

Returns the [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
 referenced by the typed array.

[`TypedArray.prototype.byteLength`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/byteLength)

Returns the length (in bytes) of the typed array.

[`TypedArray.prototype.byteOffset`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/byteOffset)

Returns the offset (in bytes) of the typed array from the start of its [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
.

[`TypedArray.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. `TypedArray.prototype.constructor` is the hidden `TypedArray` constructor function, but each typed array subclass also defines its own `constructor` property.

[`TypedArray.prototype.length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/length)

Returns the number of elements held in the typed array.

[`TypedArray.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#typedarray.prototypesymbol.tostringtag)

The initial value of the [`TypedArray.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is a getter that returns the same string as the typed array constructor's name. It returns `undefined` if the `this` value is not one of the typed array subclasses. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
. However, because `TypedArray` also has its own [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/toString)
 method, this property is not used unless you call [`Object.prototype.toString.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
 with a typed array as `thisArg`.

All `TypedArray` subclasses also have the following instance properties:

[`TypedArray.prototype.BYTES_PER_ELEMENT`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/BYTES_PER_ELEMENT)

Returns a number value of the element size for the different `TypedArray` objects.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#instance_methods)

---------------------------------------------------------------------------------------------------------------------------------

These methods are defined on the `TypedArray` prototype object and are thus shared by all `TypedArray` subclass instances.

[`TypedArray.prototype.at()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/at)

Takes an integer value and returns the item at that index. This method allows for negative integers, which count back from the last item.

[`TypedArray.prototype.copyWithin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/copyWithin)

Copies a sequence of array elements within the array. See also [`Array.prototype.copyWithin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin)
.

[`TypedArray.prototype.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/entries)

Returns a new _array iterator_ object that contains the key/value pairs for each index in the array. See also [`Array.prototype.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/entries)
.

[`TypedArray.prototype.every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/every)

Returns `false` if it finds an element in the array that does not satisfy the provided testing function. Otherwise, it returns `true`. See also [`Array.prototype.every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
.

[`TypedArray.prototype.fill()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/fill)

Fills all the elements of an array from a start index to an end index with a static value. See also [`Array.prototype.fill()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill)
.

[`TypedArray.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/filter)

Creates a new array with all of the elements of this array for which the provided filtering function returns `true`. See also [`Array.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
.

[`TypedArray.prototype.find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/find)

Returns the first `element` in the array that satisfies a provided testing function, or `undefined` if no appropriate element is found. See also [`Array.prototype.find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
.

[`TypedArray.prototype.findIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/findIndex)

Returns the first index value in the array that has an element that satisfies a provided testing function, or `-1` if no appropriate element was found. See also [`Array.prototype.findIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)
.

[`TypedArray.prototype.findLast()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/findLast)

Returns the value of the last element in the array that satisfies a provided testing function, or `undefined` if no appropriate element is found. See also [`Array.prototype.findLast()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLast)
.

[`TypedArray.prototype.findLastIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/findLastIndex)

Returns the index of the last element in the array that satisfies a provided testing function, or `-1` if no appropriate element was found. See also [`Array.prototype.findLastIndex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findLastIndex)
.

[`TypedArray.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/forEach)

Calls a function for each element in the array. See also [`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
.

[`TypedArray.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/includes)

Determines whether a typed array includes a certain element, returning `true` or `false` as appropriate. See also [`Array.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
.

[`TypedArray.prototype.indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/indexOf)

Returns the first (least) index of an element within the array equal to the specified value, or `-1` if none is found. See also [`Array.prototype.indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)
.

[`TypedArray.prototype.join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/join)

Returns a new string that is the concatenation of all elements in this typed array, separated by commas or a specified separator string. See also [`Array.prototype.join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
.

[`TypedArray.prototype.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/keys)

Returns a new array iterator that contains the keys for each index in the array. See also [`Array.prototype.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/keys)
.

[`TypedArray.prototype.lastIndexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/lastIndexOf)

Returns the last (greatest) index of an element within the array equal to the specified value, or `-1` if none is found. See also [`Array.prototype.lastIndexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf)
.

[`TypedArray.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/map)

Creates a new array with the results of calling a provided function on every element in this array. See also [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
.

[`TypedArray.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/reduce)

Apply a function against an accumulator and each value of the array (from left-to-right) as to reduce it to a single value. See also [`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
.

[`TypedArray.prototype.reduceRight()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/reduceRight)

Apply a function against an accumulator and each value of the array (from right-to-left) as to reduce it to a single value. See also [`Array.prototype.reduceRight()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight)
.

[`TypedArray.prototype.reverse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/reverse)

Reverses the order of the elements of an array — the first becomes the last, and the last becomes the first. See also [`Array.prototype.reverse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)
.

[`TypedArray.prototype.set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/set)

Stores multiple values in the typed array, reading input values from a specified array.

[`TypedArray.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/slice)

Extracts a section of an array and returns a new array. See also [`Array.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
.

[`TypedArray.prototype.some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/some)

Returns `true` if it finds an element in the array that satisfies the provided testing function. Otherwise, it returns `false`. See also [`Array.prototype.some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
.

[`TypedArray.prototype.sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/sort)

Sorts the elements of an array in place and returns the array. See also [`Array.prototype.sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
.

[`TypedArray.prototype.subarray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/subarray)

Returns a new `TypedArray` from the given start and end element index.

[`TypedArray.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/toLocaleString)

Returns a localized string representing the array and its elements. See also [`Array.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toLocaleString)
.

[`TypedArray.prototype.toReversed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/toReversed)

Returns a new array with the elements in reversed order, without modifying the original array.

[`TypedArray.prototype.toSorted()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/toSorted)

Returns a new array with the elements sorted in ascending order, without modifying the original array.

[`TypedArray.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/toString)

Returns a string representing the array and its elements. See also [`Array.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toString)
.

[`TypedArray.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/values)

Returns a new _array iterator_ object that contains the values for each index in the array. See also [`Array.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/values)
.

[`TypedArray.prototype.with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/with)

Returns a new array with the element at the given index replaced with the given value, without modifying the original array.

[`TypedArray.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/Symbol.iterator)

Returns a new _array iterator_ object that contains the values for each index in the array.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#examples)

-----------------------------------------------------------------------------------------------------------------

### [Property access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#property_access)

You can reference elements in the array using standard array index syntax (that is, using bracket notation). However, getting or setting indexed properties on typed arrays will not search in the prototype chain for this property, even when the indices are out of bound. Indexed properties will consult the [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
 and will never look at object properties. You can still use named properties, just like with all objects.

### [Cannot be frozen](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#cannot_be_frozen)

`TypedArray`s that aren't empty cannot be frozen, as their underlying `ArrayBuffer` could be mutated through another `TypedArray` view of the buffer. This would mean that the object would never genuinely be frozen.

### [ByteOffset must be aligned](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#byteoffset_must_be_aligned)

When constructing a `TypedArray` as a view onto an `ArrayBuffer`, the `byteOffset` argument must be aligned to its element size; in other words, the offset must be a multiple of `BYTES_PER_ELEMENT`.

### [ByteLength must be aligned](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#bytelength_must_be_aligned)

Like the `byteOffset` parameter, the `byteLength` property of an `ArrayBuffer` passed to a `TypedArray`'s constructor must be a multiple of the constructor's `BYTES_PER_ELEMENT`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-typedarray-objects](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-typedarray-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Polyfill of typed arrays in `core-js`](https://core-js.io/docs/features/ecmascript/typed-arrays "External link (opens in new tab)")
    
*   [JavaScript typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
     guide
*   [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
    
*   [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)
    
*   [`TextDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/typedarray/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/typedarray (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTypedArray&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftypedarray%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTypedArray%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftypedarray%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")