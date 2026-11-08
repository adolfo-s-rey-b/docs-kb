*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#mdn-search)
    

JavaScript typed arrays
=======================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
    

JavaScript typed arrays are array-like objects that provide a mechanism for reading and writing raw binary data in memory buffers.

Typed arrays are not intended to replace arrays for any kind of functionality. Instead, they provide developers with a familiar interface for manipulating binary data. This is useful when interacting with platform features, such as audio and video manipulation, access to raw data using [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
, and so forth. Each entry in a JavaScript typed array is a raw binary value in one of a number of supported formats, from 8-bit integers to 64-bit floating-point numbers.

Typed array objects share many of the same methods as arrays with similar semantics. However, typed arrays are _not_ to be confused with normal arrays, as calling [`Array.isArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)
 on a typed array returns `false`. Moreover, not all methods available for normal arrays are supported by typed arrays (e.g., push and pop).

To achieve maximum flexibility and efficiency, JavaScript typed arrays split the implementation into _buffers_ and _views_. A buffer is an object representing a chunk of data; it has no format to speak of, and offers no mechanism for accessing its contents. In order to access the memory contained in a buffer, you need to use a [view](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#views)
. A view provides a _context_ — that is, a data type, starting offset, and number of elements.

![A diagram showing how different typed arrays may be views of the same underlying buffer. Each one has a different element number and width.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays/typed_arrays.png)

[Buffers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#buffers)

----------------------------------------------------------------------------------------------

There are two types of buffers: [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
 and [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)
. Both are low-level representations of a memory span. They have "array" in their names, but they don't have much to do with arrays — you cannot read or write to them directly. Instead, buffers are generic objects that just contain raw data. In order to access the memory represented by a buffer, you need to use a view.

Buffers support the following actions:

*   _Allocate_: As soon as a new buffer is created, a new memory span is allocated and initialized to `0`.
*   _Copy_: Using the [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/slice)
     method, you can efficiently copy a portion of the memory without creating views to manually copy each byte.
*   _Transfer_: Using the [`transfer()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/transfer)
     and [`transferToFixedLength()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/transferToFixedLength)
     methods, you can transfer ownership of the memory span to a new buffer object. This is useful when transferring data between different execution contexts without copying. After the transfer, the original buffer is no longer usable. A `SharedArrayBuffer` cannot be transferred (as the buffer is already shared by all execution contexts).
*   _Resize_: Using the [`resize()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/resize)
     method, you can resize the memory span (either claim more memory space, as long as it doesn't pass the pre-set [`maxByteLength`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/maxByteLength)
     limit, or release some memory space). `SharedArrayBuffer` can only be [grown](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer/grow)
     but not shrunk.

The difference between `ArrayBuffer` and `SharedArrayBuffer` is that the former is always owned by a single execution context at a time. If you pass an `ArrayBuffer` to a different execution context, it is _transferred_ and the original `ArrayBuffer` becomes unusable. This ensures that only one execution context can access the memory at a time. A `SharedArrayBuffer` is not transferred when passed to a different execution context, so it can be accessed by multiple execution contexts at the same time. This may introduce race conditions when multiple threads access the same memory span, so operations such as [`Atomics`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics)
 methods become useful.

[Views](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#views)

------------------------------------------------------------------------------------------

There are currently two main kinds of views: typed array views and [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)
. Typed arrays provide [utility methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#instance_methods)
 that allow you to conveniently transform binary data. `DataView` is more low-level and allows granular control of how data is accessed. The ways to read and write data using the two views are very different.

Both kinds of views cause [`ArrayBuffer.isView()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/isView)
 to return `true`. They both have the following properties:

[`buffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#buffer)

The underlying buffer that the view references.

[`byteOffset`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#byteoffset)

The offset, in bytes, of the view from the start of its buffer.

[`byteLength`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#bytelength)

The length, in bytes, of the view.

Both constructors accept the above three as separate arguments, although typed array constructors accept `length` as the number of elements rather than the number of bytes.

### [Typed array views](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#typed_array_views)

Typed array views have self-descriptive names and provide views for all the usual numeric types like `Int8`, `Uint32`, `Float64` and so forth. There is one special typed array view, [`Uint8ClampedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray)
, which clamps the values between `0` and `255`. This is useful for [Canvas data processing](https://developer.mozilla.org/en-US/docs/Web/API/ImageData)
, for example.

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

All typed array views have the same methods and properties, as defined by the [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
 class. They only differ in the underlying data type and the size in bytes. This is discussed in more detail in [Value encoding and normalization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#value_encoding_and_normalization)
.

Typed arrays are, in principle, fixed-length, so array methods that may change the length of an array are not available. This includes `pop`, `push`, `shift`, `splice`, and `unshift`. In addition, `flat` is unavailable because there are no nested typed arrays, and related methods including `concat` and `flatMap` do not have great use cases so are unavailable. As `splice` is unavailable, so too is `toSpliced`. All other array methods are shared between `Array` and `TypedArray`.

On the other hand, `TypedArray` has the extra `set` and `subarray` methods that optimize working with multiple typed arrays that view the same buffer. The `set()` method allows setting multiple typed array indices at once, using data from another array or typed array. If the two typed arrays share the same underlying buffer, the operation may be more efficient as it's a fast memory move. The `subarray()` method creates a new typed array view that references the same buffer as the original typed array, but with a narrower span.

There's no way to directly change the length of a typed array without changing the underlying buffer. However, when the typed array views a resizable buffer and does not have a fixed `byteLength`, it is _length-tracking_, and will automatically resize to fit the underlying buffer as the resizable buffer is resized. See [Behavior when viewing a resizable buffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#behavior_when_viewing_a_resizable_buffer)
 for details.

Similar to regular arrays, you can access typed array elements using [bracket notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#bracket_notation)
. The corresponding bytes in the underlying buffer are retrieved and interpreted as a number. Any property access using a number (or the string representation of a number, since numbers are always converted to strings when accessing properties) will be proxied by the typed array — they never interact with the object itself. This means, for example:

*   Out-of-bounds index access always returns `undefined`, without actually accessing the property on the object.
*   Any attempt to write to such an out-of-bounds property has no effect: it does not throw an error but doesn't change the buffer or typed array either.
*   Typed array indices appear to be configurable and writable, but any attempt to change their attributes will fail.

### [DataView](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#dataview)

The [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)
 is a low-level interface that provides a getter/setter API to read and write arbitrary data to the buffer. This is useful when dealing with different types of data, for example. Typed array views are in the native byte-order (see [Endianness](https://developer.mozilla.org/en-US/docs/Glossary/Endianness)
) of your platform. With a `DataView`, the byte-order can be controlled. By default, it's big-endian—the bytes are ordered from most significant to least significant. This can be reversed, with the bytes ordered from least significant to most significant (little-endian), using getter/setter methods.

`DataView` does not require alignment; multi-byte read and write can be started at any specified offset. The setter methods work the same way.

The following example uses a `DataView` to get the binary representation of any number:

[Web APIs using typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#web_apis_using_typed_arrays)

--------------------------------------------------------------------------------------------------------------------------------------

These are some examples of APIs that make use of typed arrays; there are others, and more are being added all the time.

[`FileReader.prototype.readAsArrayBuffer()`](https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsArrayBuffer)

The `FileReader.prototype.readAsArrayBuffer()` method starts reading the contents of the specified [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob)
 or [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File)
.

[`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch)

The [`body`](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#body)
 option to `fetch()` can be a typed array or [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
, enabling you to send these objects as the payload of a [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST)
 request.

[`ImageData.data`](https://developer.mozilla.org/en-US/docs/Web/API/ImageData)

Is a [`Uint8ClampedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray)
 representing a one-dimensional array containing the data in the RGBA order, with integer values between `0` and `255` inclusive.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#examples)

------------------------------------------------------------------------------------------------

### [Using views with buffers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#using_views_with_buffers)

First of all, we will need to create a buffer, here with a fixed length of 16-bytes:

At this point, we have a chunk of memory whose bytes are all pre-initialized to 0. There's not a lot we can do with it, though. For example, we can confirm that the buffer is the right size:

Before we can really work with this buffer, we need to create a view. Let's create a view that treats the data in the buffer as an array of 32-bit signed integers:

Now we can access the fields in the array just like a normal array:

This fills out the 4 entries in the array (4 entries at 4 bytes each makes 16 total bytes) with the values `0`, `2`, `4`, and `6`.

### [Multiple views on the same data](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#multiple_views_on_the_same_data)

Things start to get really interesting when you consider that you can create multiple views onto the same data. For example, given the code above, we can continue like this:

Here we create a 16-bit integer view that shares the same buffer as the existing 32-bit view and we output all the values in the buffer as 16-bit integers. Now we get the output `0`, `0`, `2`, `0`, `4`, `0`, `6`, `0` (assuming little-endian encoding):

Int16Array  |   0  |  0   |   2  |  0   |   4  |  0   |   6  |  0   |
Int32Array  |      0      |      2      |      4      |      6      |
ArrayBuffer | 00 00 00 00 | 02 00 00 00 | 04 00 00 00 | 06 00 00 00 |

You can go a step farther, though. Consider this:

The output from this is `"Entry 0 in the 32-bit array is now 32"`.

In other words, the two arrays are indeed viewed on the same data buffer, treating it as different formats.

Int16Array  |  32  |  0   |   2  |  0   |   4  |  0   |   6  |  0   |
Int32Array  |     32      |      2      |      4      |      6      |
ArrayBuffer | 20 00 00 00 | 02 00 00 00 | 04 00 00 00 | 06 00 00 00 |

You can do this with any view type, although if you set an integer and then read it as a floating-point number, you will probably get a strange result because the bits are interpreted differently.

### [Reading text from a buffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#reading_text_from_a_buffer)

Buffers don't always represent numbers. For example, reading a file can give you a text data buffer. You can read this data out of the buffer using a typed array.

The following reads UTF-8 text using the [`TextDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder)
 web API:

The following reads UTF-16 text using the [`String.fromCharCode()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode)
 method:

### [Working with complex data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#working_with_complex_data_structures)

By combining a single buffer with multiple views of different types, starting at different offsets into the buffer, you can interact with data objects containing multiple data types. This lets you, for example, interact with complex data structures from [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)
 or data files.

Consider this C structure:

You can access a buffer containing data in this format like this:

Then you can access, for example, the amount due with `amountDueView[0]`.

**Note:** The [data structure alignment](https://en.wikipedia.org/wiki/Data_structure_alignment "External link (opens in new tab)")
 in a C structure is platform-dependent. Take precautions and considerations for these padding differences.

### [Conversion to normal arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#conversion_to_normal_arrays)

After processing a typed array, it is sometimes useful to convert it back to a normal array in order to benefit from the [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 prototype. This can be done using [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
:

as well as the [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays#see_also)

------------------------------------------------------------------------------------------------

*   [Faster Canvas Pixel Manipulation with Typed Arrays](https://hacks.mozilla.org/2011/12/faster-canvas-pixel-manipulation-with-typed-arrays/ "External link (opens in new tab)")
     on hacks.mozilla.org (2011)
*   [Typed arrays - Binary data in the browser](https://web.dev/articles/webgl-typed-arrays "External link (opens in new tab)")
     on web.dev (2012)
*   [Endianness](https://developer.mozilla.org/en-US/docs/Glossary/Endianness)
    
*   [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
    
*   [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)
    
*   [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
    
*   [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)
    

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/typed_arrays/index.md?plain=1 "Folder: en-us/web/javascript/guide/typed_arrays (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FTyped_arrays&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Ftyped_arrays%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FTyped_arrays%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Ftyped_arrays%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")