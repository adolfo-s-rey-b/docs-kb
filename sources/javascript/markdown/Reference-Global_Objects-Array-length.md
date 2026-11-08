*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#mdn-search)
    

Array: length
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`length`** data property of an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 instance represents the number of slots in that array. The value is an unsigned, 32-bit integer that is always numerically greater than the highest index in the array. It may be greater than the number of elements if the array is [sparse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_methods_and_empty_slots)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#try_it)

---------------------------------------------------------------------------------------------------------------

    const clothing = ["shoes", "shirts", "socks", "sweaters"];
    
    console.log(clothing.length);
    // Expected output: 4
    

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#value)

-------------------------------------------------------------------------------------------------------------

A nonnegative integer less than 232.

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | no  |
| Configurable | no  |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#description)

-------------------------------------------------------------------------------------------------------------------------

The value of the `length` property is a nonnegative integer with a value less than 232.

js

    const listA = [1, 2, 3];
    const listB = new Array(6);
    
    console.log(listA.length);
    // 3
    
    console.log(listB.length);
    // 6
    
    listB.length = 2 ** 32; // 4294967296
    // RangeError: Invalid array length
    
    const listC = new Array(-100); // Negative numbers are not allowed
    // RangeError: Invalid array length
    

The array object observes the `length` property, and automatically syncs the `length` value with the array's content. This means:

*   Setting `length` to a value smaller than the current length truncates the array — elements beyond the new `length` are deleted.
*   Setting any array index (a nonnegative integer smaller than 232) beyond the current `length` extends the array — the `length` property is increased to reflect the new highest index.
*   Setting `length` to an invalid value (e.g., a negative number or a non-integer) throws a `RangeError` exception.

When `length` is set to a bigger value than the current length, the array is extended by adding [empty slots](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
, not actual `undefined` values. Empty slots have some special interactions with array methods; see [array methods and empty slots](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#array_methods_and_empty_slots)
.

js

    const arr = [1, 2];
    console.log(arr);
    // [ 1, 2 ]
    
    arr.length = 5; // set array length to 5 while currently 2.
    console.log(arr);
    // [ 1, 2, <3 empty items> ]
    
    arr.forEach((element) => console.log(element));
    // 1
    // 2
    

See also [Relationship between `length` and numerical properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#relationship_between_length_and_numerical_properties)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#examples)

-------------------------------------------------------------------------------------------------------------------

### [Iterating over an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#iterating_over_an_array)

In the following example, the array `numbers` is iterated through by looking at the `length` property. The value in each element is then doubled.

js

    const numbers = [1, 2, 3, 4, 5];
    const length = numbers.length;
    for (let i = 0; i < length; i++) {
      numbers[i] *= 2;
    }
    // numbers is now [2, 4, 6, 8, 10]
    

### [Shortening an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#shortening_an_array)

The following example shortens the array `numbers` to a length of 3 if the current length is greater than 3.

js

    const numbers = [1, 2, 3, 4, 5];
    
    if (numbers.length > 3) {
      numbers.length = 3;
    }
    
    console.log(numbers); // [1, 2, 3]
    console.log(numbers.length); // 3
    console.log(numbers[3]); // undefined; the extra elements are deleted
    

### [Create empty array of fixed length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#create_empty_array_of_fixed_length)

Setting `length` to a value greater than the current length creates a [sparse array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
.

js

    const numbers = [];
    numbers.length = 3;
    console.log(numbers); // [empty x 3]
    

### [Array with non-writable length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#array_with_non-writable_length)

The `length` property is automatically updated by the array when elements are added beyond the current length. If the `length` property is made non-writable, the array will not be able to update it. This causes an error in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
.

js

    "use strict";
    
    const numbers = [1, 2, 3, 4, 5];
    Object.defineProperty(numbers, "length", { writable: false });
    numbers[5] = 6; // TypeError: Cannot assign to read only property 'length' of object '[object Array]'
    numbers.push(5); // // TypeError: Cannot assign to read only property 'length' of object '[object Array]'
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-properties-of-array-instances-length](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-properties-of-array-instances-length) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    
*   [`TypedArray.prototype.length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/length)
    
*   [`String`: `length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
    
*   [RangeError: invalid array length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_array_length)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/length/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/array/length (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Flength&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Flength%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Flength%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Flength%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5a745d55a26933ffd9e71f3b2246deba3f9e6f82%0A*+Document+last+modified%3A+2026-05-02T02%3A38%3A03.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")