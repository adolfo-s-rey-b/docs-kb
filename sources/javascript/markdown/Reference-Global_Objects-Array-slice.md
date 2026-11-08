*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#mdn-search)
    

Array.prototype.slice()
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`slice()`** method of [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 instances returns a [shallow copy](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)
 of a portion of an array into a new array object selected from `start` to `end` (`end` not included) where `start` and `end` represent the index of items in that array. The original array will not be modified.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#try_it)

--------------------------------------------------------------------------------------------------------------

    const animals = ["ant", "bison", "camel", "duck", "elephant"];
    
    console.log(animals.slice(2));
    // Expected output: Array ["camel", "duck", "elephant"]
    
    console.log(animals.slice(2, 4));
    // Expected output: Array ["camel", "duck"]
    
    console.log(animals.slice(1, 5));
    // Expected output: Array ["bison", "camel", "duck", "elephant"]
    
    console.log(animals.slice(-2));
    // Expected output: Array ["duck", "elephant"]
    
    console.log(animals.slice(2, -1));
    // Expected output: Array ["camel", "duck"]
    
    console.log(animals.slice());
    // Expected output: Array ["ant", "bison", "camel", "duck", "elephant"]
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#syntax)

--------------------------------------------------------------------------------------------------------------

js

    slice()
    slice(start)
    slice(start, end)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#parameters)

[`start` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#start)

Zero-based index at which to start extraction, [converted to an integer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#integer_conversion)
.

*   Negative index counts back from the end of the array — if `-array.length <= start < 0`, `start + array.length` is used.
*   If `start < -array.length` or `start` is omitted, `0` is used.
*   If `start >= array.length`, an empty array is returned.

[`end` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#end)

Zero-based index at which to end extraction, [converted to an integer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#integer_conversion)
. `slice()` extracts up to but not including `end`.

*   Negative index counts back from the end of the array — if `-array.length <= end < 0`, `end + array.length` is used.
*   If `end < -array.length`, `0` is used.
*   If `end >= array.length` or `end` is omitted or `undefined`, `array.length` is used, causing all elements until the end to be extracted.
*   If `end` implies a position before or at the position that `start` implies, an empty array is returned.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#return_value)

A new array containing the extracted elements.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#description)

------------------------------------------------------------------------------------------------------------------------

The `slice()` method is a [copying method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#copying_methods_and_mutating_methods)
. It does not alter `this` but instead returns a [shallow copy](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)
 that contains some of the same elements as the ones from the original array.

The `slice()` method preserves empty slots. If the sliced portion is [sparse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
, the returned array is sparse as well.

The `slice()` method is [generic](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#generic_array_methods)
. It only expects the `this` value to have a `length` property and integer-keyed properties.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#examples)

------------------------------------------------------------------------------------------------------------------

### [Return a portion of an existing array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#return_a_portion_of_an_existing_array)

js

    const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
    const citrus = fruits.slice(1, 3);
    
    // fruits contains ['Banana', 'Orange', 'Lemon', 'Apple', 'Mango']
    // citrus contains ['Orange','Lemon']
    

In this example, `slice(1, 3)` extracts elements from index `1` up to, but not including, index `3`, resulting in a new array `['Orange', 'Lemon']`.

### [Omitting the end parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#omitting_the_end_parameter)

js

    const fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];
    
    const tropical = fruits.slice(2);
    console.log(tropical); // ['Orange', 'Mango', 'Pineapple']
    

In this example, `slice(2)` extracts elements from index `2` to the end of the array.

### [Using negative indices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#using_negative_indices)

js

    const fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];
    
    const lastTwo = fruits.slice(-2);
    console.log(lastTwo); // ['Mango', 'Pineapple']
    

In this example, `slice(-2)` extracts the last two elements of the array. When using a negative index with the `slice` method, negative indices are counted from the end of the array, starting at `-1` for the last element, `-2` for the second-to-last element, and so on. The negative index `-2` itself is included because it is the starting point of the extraction.

|     |     |     |     |     |
|  S  |  L  |  I  |  C  |  E  |
|     |     |     |     |     |
  -5    -4    -3    -2    -1

<--- read from reverse

### [Using a positive start index and a negative end index](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#using_a_positive_start_index_and_a_negative_end_index)

js

    const fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];
    
    // Using positive start index and negative end index
    const sliceExample = fruits.slice(1, -1);
    console.log(sliceExample); // ['Banana', 'Orange', 'Mango']
    

In this example, `slice(1, -1)` starts extracting from index `1` and goes up to, but does not include, the element at index `-1` (which is the last element). This results in a new array with `['Banana', 'Orange', 'Mango']`. The `slice` method always excludes the element at the final index specified, regardless of whether it is positive or negative.

read from start --->

   0     1     2     3     4
|     |     |     |     |     |
|  S  |  L  |  I  |  C  |  E  |
|     |     |     |     |     |
  -5    -4    -3    -2    -1

<--- read from reverse

### [Using slice with arrays of objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#using_slice_with_arrays_of_objects)

In the following example, `slice` creates a new array, `newCar`, from `myCar`. Both include a reference to the object `myHonda`. When the color of `myHonda` is changed to purple, both arrays reflect the change.

js

    // Using slice, create newCar from myCar.
    const myHonda = {
      color: "red",
      wheels: 4,
      engine: { cylinders: 4, size: 2.2 },
    };
    const myCar = [myHonda, 2, "cherry condition", "purchased 1997"];
    const newCar = myCar.slice(0, 2);
    
    console.log("myCar =", myCar);
    console.log("newCar =", newCar);
    console.log("myCar[0].color =", myCar[0].color);
    console.log("newCar[0].color =", newCar[0].color);
    
    // Change the color of myHonda.
    myHonda.color = "purple";
    console.log("The new color of my Honda is", myHonda.color);
    
    console.log("myCar[0].color =", myCar[0].color);
    console.log("newCar[0].color =", newCar[0].color);
    

This script writes:

myCar = \[\
  { color: 'red', wheels: 4, engine: { cylinders: 4, size: 2.2 } },\
  2,\
  'cherry condition',\
  'purchased 1997'\
\]
newCar = \[ { color: 'red', wheels: 4, engine: { cylinders: 4, size: 2.2 } }, 2 \]
myCar\[0\].color = red
newCar\[0\].color = red
The new color of my Honda is purple
myCar\[0\].color = purple
newCar\[0\].color = purple

### [Calling slice() on non-array objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#calling_slice_on_non-array_objects)

The `slice()` method reads the `length` property of `this`. It then reads the integer-keyed properties from `start` to `end` and defines them on a newly created array.

js

    const arrayLike = {
      length: 3,
      0: 2,
      1: 3,
      2: 4,
      3: 33, // ignored by slice() since length is 3
    };
    console.log(Array.prototype.slice.call(arrayLike, 1, 3));
    // [ 3, 4 ]
    

### [Using slice() to convert array-like objects to arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#using_slice_to_convert_array-like_objects_to_arrays)

The `slice()` method is often used with [`bind()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
 and [`call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
 to create a utility method that converts an array-like object into an array.

js

    // slice() is called with `this` passed as the first argument
    const slice = Function.prototype.call.bind(Array.prototype.slice);
    
    function list() {
      return slice(arguments);
    }
    
    const listResult = list(1, 2, 3); // [1, 2, 3]
    

### [Using slice() on sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#using_slice_on_sparse_arrays)

The array returned from `slice()` may be sparse if the source is sparse.

js

    console.log([1, 2, , 4, 5].slice(1, 4)); // [2, empty, 4]
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-array.prototype.slice](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.slice) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Array.prototype.slice` in `core-js`](https://core-js.io/docs/features/ecmascript/array "External link (opens in new tab)")
    
*   [es-shims polyfill of `Array.prototype.slice`](https://www.npmjs.com/package/array.prototype.slice "External link (opens in new tab)")
    
*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    
*   [`Array.prototype.pop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
    
*   [`Array.prototype.shift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift)
    
*   [`Array.prototype.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
    
*   [`Array.prototype.splice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
    
*   [`TypedArray.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/slice)
    
*   [`String.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/slice/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/array/slice (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fslice&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fslice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fslice%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fslice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")