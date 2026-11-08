*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#mdn-search)
    

TypedArray.from()
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`TypedArray.from()`** static method creates a new [typed array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#typedarray_objects)
 from an array-like or iterable object. This method is nearly the same as [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#try_it)

------------------------------------------------------------------------------------------------------------------

    const uint16 = Int16Array.from("12345");
    
    console.log(uint16);
    // Expected output: Int16Array [1, 2, 3, 4, 5]
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#syntax)

------------------------------------------------------------------------------------------------------------------

js

    TypedArray.from(arrayLike, mapFn)
    TypedArray.from(arrayLike, mapFn, thisArg)
    

Where `TypedArray` is one of:

*   [`Int8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array)
    
*   [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
    
*   [`Uint8ClampedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray)
    
*   [`Int16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array)
    
*   [`Uint16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array)
    
*   [`Int32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array)
    
*   [`Uint32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array)
    
*   [`Float16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float16Array)
    
*   [`Float32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array)
    
*   [`Float64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array)
    
*   [`BigInt64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array)
    
*   [`BigUint64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#parameters)

[`arrayLike`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#arraylike)

An iterable or array-like object to convert to a typed array.

[`mapFn` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#mapfn)

A function to call on every element of the typed array. If provided, every value to be added to the array is first passed through this function, and `mapFn`'s return value is added to the typed array instead. The function is called with the following arguments:

[`element`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#element)

The current element being processed in the typed array.

[`index`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#index)

The index of the current element being processed in the typed array.

[`thisArg` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#thisarg)

Value to use as `this` when executing `mapFn`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#return_value)

A new [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
 instance.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#description)

----------------------------------------------------------------------------------------------------------------------------

See [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
 for more details.

There are some subtle distinctions between [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
 and `TypedArray.from()` (note: the `this` value mentioned below is the `this` value that `TypedArray.from()` was called with, not the `thisArg` argument used to invoke `mapFn`):

*   If the `this` value of `TypedArray.from()` is not a constructor, `TypedArray.from()` will throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
    , while `Array.from()` defaults to creating a new [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    .
*   The object constructed by `this` must be a `TypedArray` instance, while `Array.from()` allows its `this` value to be constructed to any object.
*   When the `source` parameter is an iterator, `TypedArray.from()` first collects all the values from the iterator, then creates an instance of `this` using the count, and finally sets the values on the instance. `Array.from()` sets each value as it receives them from the iterator, then sets its `length` at the end.
*   `TypedArray.from()` uses `[[Set]]` while `Array.from()` uses `[[DefineOwnProperty]]`. Hence, when working with [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
     objects, it calls [`handler.set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set)
     to create new elements rather than [`handler.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/defineProperty)
    .
*   When `Array.from()` gets an array-like which isn't an iterator, it respects holes. `TypedArray.from()` will ensure the result is dense.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#examples)

----------------------------------------------------------------------------------------------------------------------

### [From an iterable object (Set)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#from_an_iterable_object_set)

js

    const s = new Set([1, 2, 3]);
    Uint8Array.from(s);
    // Uint8Array [ 1, 2, 3 ]
    

### [From a string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#from_a_string)

js

    Int16Array.from("123");
    // Int16Array [ 1, 2, 3 ]
    

### [Use with arrow function and map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#use_with_arrow_function_and_map)

Using an arrow function as the map function to manipulate the elements

js

    Float32Array.from([1, 2, 3], (x) => x + x);
    // Float32Array [ 2, 4, 6 ]
    

### [Generate a sequence of numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#generate_a_sequence_of_numbers)

js

    Uint8Array.from({ length: 5 }, (v, k) => k);
    // Uint8Array [ 0, 1, 2, 3, 4 ]
    

### [Calling from() on non-TypedArray constructors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#calling_from_on_non-typedarray_constructors)

The `this` value of `from()` must be a constructor that returns a `TypedArray` instance.

js

    function NotArray(len) {
      console.log("NotArray called with length", len);
    }
    
    Int8Array.from.call({}, []); // TypeError: #<Object> is not a constructor
    Int8Array.from.call(NotArray, []);
    // NotArray called with length 0
    // TypeError: Method %TypedArray%.from called on incompatible receiver #<NotArray>
    

js

    function NotArray2(len) {
      console.log("NotArray2 called with length", len);
      return new Uint8Array(len);
    }
    console.log(Int8Array.from.call(NotArray2, [1, 2, 3]));
    // NotArray2 called with length 3
    // Uint8Array(3) [ 1, 2, 3 ]
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-%typedarray%.from](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-%typedarray%.from) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `TypedArray.from` in `core-js`](https://core-js.io/docs/features/ecmascript/typed-arrays "External link (opens in new tab)")
    
*   [JavaScript typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
     guide
*   [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
    
*   [`TypedArray.of()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/of)
    
*   [`TypedArray.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/map)
    
*   [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/from/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/typedarray/from/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/typedarray/from (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTypedArray%2Ffrom&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftypedarray%2Ffrom%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTypedArray%2Ffrom%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftypedarray%2Ffrom%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")