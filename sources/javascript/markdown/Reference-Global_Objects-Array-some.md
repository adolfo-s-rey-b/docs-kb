*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#mdn-search)
    

Array.prototype.some()
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`some()`** method of [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 instances returns `true` if it finds an element in the array that satisfies the provided testing function. Otherwise, it returns `false`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#try_it)

-------------------------------------------------------------------------------------------------------------

    const array = [1, 2, 3, 4, 5];
    
    // Checks whether an element is even
    const even = (element) => element % 2 === 0;
    
    console.log(array.some(even));
    // Expected output: true
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#syntax)

-------------------------------------------------------------------------------------------------------------

js

    some(callbackFn)
    some(callbackFn, thisArg)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#parameters)

[`callbackFn`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#callbackfn)

A function to execute for each element in the array. It should return a [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 value to indicate the element passes the test, and a [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 value otherwise. The function is called with the following arguments:

[`element`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#element)

The current element being processed in the array.

[`index`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#index)

The index of the current element being processed in the array.

[`array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#array)

The array `some()` was called upon.

[`thisArg` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#thisarg)

A value to use as `this` when executing `callbackFn`. See [iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#return_value)

`false` unless `callbackFn` returns a [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 value for an array element, in which case `true` is immediately returned.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#description)

-----------------------------------------------------------------------------------------------------------------------

The `some()` method is an [iterative method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
. It calls a provided `callbackFn` function once for each element in an array, until the `callbackFn` returns a [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 value. If such an element is found, `some()` immediately returns `true` and stops iterating through the array. Otherwise, if `callbackFn` returns a [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 value for all elements, `some()` returns `false`. Read the [iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
 section for more information about how these methods work in general.

`some()` acts like the "there exists" quantifier in mathematics. In particular, for an empty array, it returns `false` for any condition.

`callbackFn` is invoked only for array indexes which have assigned values. It is not invoked for empty slots in [sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
.

`some()` does not mutate the array on which it is called, but the function provided as `callbackFn` can. Note, however, that the length of the array is saved _before_ the first invocation of `callbackFn`. Therefore:

*   `callbackFn` will not visit any elements added beyond the array's initial length when the call to `some()` began.
*   Changes to already-visited indexes do not cause `callbackFn` to be invoked on them again.
*   If an existing, yet-unvisited element of the array is changed by `callbackFn`, its value passed to the `callbackFn` will be the value at the time that element gets visited. [Deleted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
     elements are not visited.

**Warning:** Concurrent modifications of the kind described above frequently lead to hard-to-understand code and are generally to be avoided (except in special cases).

The `some()` method is [generic](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#generic_array_methods)
. It only expects the `this` value to have a `length` property and integer-keyed properties.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#examples)

-----------------------------------------------------------------------------------------------------------------

### [Testing value of array elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#testing_value_of_array_elements)

The following example tests whether any element in the array is bigger than 10.

js

    function isBiggerThan10(element, index, array) {
      return element > 10;
    }
    
    [2, 5, 8, 1, 4].some(isBiggerThan10); // false
    [12, 5, 8, 1, 4].some(isBiggerThan10); // true
    

### [Testing array elements using arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#testing_array_elements_using_arrow_functions)

[Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 provide a shorter syntax for the same test.

js

    [2, 5, 8, 1, 4].some((x) => x > 10); // false
    [12, 5, 8, 1, 4].some((x) => x > 10); // true
    

### [Checking whether a value exists in an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#checking_whether_a_value_exists_in_an_array)

To mimic the function of the `includes()` method, this custom function returns `true` if the element exists in the array:

js

    const fruits = ["apple", "banana", "mango", "guava"];
    
    function checkAvailability(arr, val) {
      return arr.some((arrVal) => val === arrVal);
    }
    
    checkAvailability(fruits, "grapefruit"); // false
    checkAvailability(fruits, "banana"); // true
    

### [Converting any value to Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#converting_any_value_to_boolean)

js

    const TRUTHY_VALUES = [true, "true", 1];
    
    function getBoolean(value) {
      if (typeof value === "string") {
        value = value.toLowerCase().trim();
      }
    
      return TRUTHY_VALUES.some((t) => t === value);
    }
    
    getBoolean(false); // false
    getBoolean("false"); // false
    getBoolean(1); // true
    getBoolean("true"); // true
    

### [Using the third argument of callbackFn](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#using_the_third_argument_of_callbackfn)

The `array` argument is useful if you want to access another element in the array, especially when you don't have an existing variable that refers to the array. The following example first uses `filter()` to extract the positive values and then uses `some()` to check whether the array is strictly increasing.

js

    const numbers = [3, -1, 1, 4, 1, 5];
    const isIncreasing = !numbers
      .filter((num) => num > 0)
      .some((num, idx, arr) => {
        // Without the arr argument, there's no way to easily access the
        // intermediate array without saving it to a variable.
        if (idx === 0) return false;
        return num <= arr[idx - 1];
      });
    console.log(isIncreasing); // false
    

### [Using some() on sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#using_some_on_sparse_arrays)

`some()` will not run its predicate on empty slots.

js

    console.log([1, , 3].some((x) => x === undefined)); // false
    console.log([1, , 1].some((x) => x !== 1)); // false
    console.log([1, undefined, 1].some((x) => x !== 1)); // true
    

### [Calling some() on non-array objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#calling_some_on_non-array_objects)

The `some()` method reads the `length` property of `this` and then accesses each property whose key is a nonnegative integer less than `length` until they all have been accessed or `callbackFn` returns `true`.

js

    const arrayLike = {
      length: 3,
      0: "a",
      1: "b",
      2: "c",
      3: 3, // ignored by some() since length is 3
    };
    console.log(Array.prototype.some.call(arrayLike, (x) => typeof x === "number"));
    // false
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-array.prototype.some](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.some) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Array.prototype.some` in `core-js`](https://core-js.io/docs/features/ecmascript/array "External link (opens in new tab)")
    
*   [es-shims polyfill of `Array.prototype.some`](https://www.npmjs.com/package/array.prototype.some "External link (opens in new tab)")
    
*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    
*   [`Array.prototype.every()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
    
*   [`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
    
*   [`Array.prototype.find()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
    
*   [`Array.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
    
*   [`TypedArray.prototype.some()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/some)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/some/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/array/some (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fsome&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fsome%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fsome%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fsome%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")