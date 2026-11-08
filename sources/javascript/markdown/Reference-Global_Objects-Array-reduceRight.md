*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#mdn-search)
    

Array.prototype.reduceRight()
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`reduceRight()`** method of [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 instances applies a function against an accumulator and each value of the array (from right-to-left) to reduce it to a single value.

See also [`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
 for left-to-right.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#try_it)

--------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#syntax)

--------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#parameters)

[`callbackFn`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#callbackfn)

A function to execute for each element in the array. Its return value becomes the value of the `accumulator` parameter on the next invocation of `callbackFn`. For the last invocation, the return value becomes the return value of `reduceRight()`. The function is called with the following arguments:

[`accumulator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#accumulator)

The value resulting from the previous call to `callbackFn`. On the first call, its value is `initialValue` if the latter is specified; otherwise its value is the last element of the array.

[`currentValue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#currentvalue)

The value of the current element. On the first call, its value is the last element if `initialValue` is specified; otherwise its value is the second-to-last element.

[`currentIndex`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#currentindex)

The index position of `currentValue` in the array. On the first call, its value is `array.length - 1` if `initialValue` is specified, otherwise `array.length - 2`.

[`array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#array)

The array `reduceRight()` was called upon.

[`initialValue` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#initialvalue)

Value to use as accumulator to the first call of the `callbackFn`. If no initial value is supplied, the last element in the array will be used and skipped. Calling `reduceRight()` on an empty array without an initial value creates a `TypeError`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#return_value)

The value that results from the reduction.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#description)

------------------------------------------------------------------------------------------------------------------------------

The `reduceRight()` method is an [iterative method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
. It runs a "reducer" callback function over all elements in the array, in descending-index order, and accumulates them into a single value. Read the [iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
 section for more information about how these methods work in general.

`callbackFn` is invoked only for array indexes which have assigned values. It is not invoked for empty slots in [sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
.

Unlike other [iterative methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)
, `reduceRight()` does not accept a `thisArg` argument. `callbackFn` is always called with `undefined` as `this`, which gets substituted with `globalThis` if `callbackFn` is non-strict.

The `reduceRight()` method is [generic](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#generic_array_methods)
. It only expects the `this` value to have a `length` property and integer-keyed properties.

All caveats about `reduce` discussed in [when to not use reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce#when_to_not_use_reduce)
 apply to `reduceRight` as well. Because JavaScript has no lazy evaluation semantics, there is no performance difference between `reduce` and `reduceRight`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#examples)

------------------------------------------------------------------------------------------------------------------------

### [How reduceRight() works without an initial value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#how_reduceright_works_without_an_initial_value)

The call to the reduceRight `callbackFn` would look something like this:

The first time the function is called, the `accumulator` and `currentValue` can be one of two values. If an `initialValue` was provided in the call to `reduceRight`, then `accumulator` will be equal to `initialValue` and `currentValue` will be equal to the last value in the array. If no `initialValue` was provided, then `accumulator` will be equal to the last value in the array and `currentValue` will be equal to the second-to-last value.

If the array is empty and no `initialValue` was provided, [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 would be thrown. If the array has only one element (regardless of position) and no `initialValue` was provided, or if `initialValue` is provided but the array is empty, the solo value would be returned without calling `callbackFn`.

Some example run-throughs of the function would look like this:

The callback would be invoked four times, with the arguments and return values in each call being as follows:

|     | `accumulator` | `currentValue` | `index` | Return value |
| --- | --- | --- | --- | --- |
| First call | `4` | `3` | `3` | `7` |
| Second call | `7` | `2` | `2` | `9` |
| Third call | `9` | `1` | `1` | `10` |
| Fourth call | `10` | `0` | `0` | `10` |

The `array` parameter never changes through the process — it's always `[0, 1, 2, 3, 4]`. The value returned by `reduceRight` would be that of the last callback invocation (`10`).

### [How reduceRight() works with an initial value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#how_reduceright_works_with_an_initial_value)

Here we reduce the same array using the same algorithm, but with an `initialValue` of `10` passed as the second argument to `reduceRight()`:

|     | `accumulator` | `currentValue` | `index` | Return value |
| --- | --- | --- | --- | --- |
| First call | `10` | `4` | `4` | `14` |
| Second call | `14` | `3` | `3` | `17` |
| Third call | `17` | `2` | `2` | `19` |
| Fourth call | `19` | `1` | `1` | `20` |
| Fifth call | `20` | `0` | `0` | `20` |

The value returned by `reduceRight` this time would be, of course, `20`.

### [Sum up all values within an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#sum_up_all_values_within_an_array)

### [Run a list of asynchronous functions with callbacks in series each passing their results to the next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#run_a_list_of_asynchronous_functions_with_callbacks_in_series_each_passing_their_results_to_the_next)

### [Difference between reduce and reduceRight](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#difference_between_reduce_and_reduceright)

### [Defining composable functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#defining_composable_functions)

Function composition is a mechanism for combining functions, in which the output of each function is passed into the next one, and the output of the last function is the final result. In this example we use `reduceRight()` to implement function composition.

See also [Function composition](https://en.wikipedia.org/wiki/Function_composition_(computer_science) "External link (opens in new tab)")
 on Wikipedia.

### [Using reduceRight() with sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#using_reduceright_with_sparse_arrays)

`reduceRight()` skips missing elements in sparse arrays, but it does not skip `undefined` values.

### [Calling reduceRight() on non-array objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#calling_reduceright_on_non-array_objects)

The `reduceRight()` method reads the `length` property of `this` and then accesses each property whose key is a nonnegative integer less than `length`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#specifications)

------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-array.prototype.reduceright](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.reduceright) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight#see_also)

------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Array.prototype.reduceRight` in `core-js`](https://core-js.io/docs/features/ecmascript/array "External link (opens in new tab)")
    
*   [es-shims polyfill of `Array.prototype.reduceRight`](https://www.npmjs.com/package/array.prototype.reduceright "External link (opens in new tab)")
    
*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    
*   [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
    
*   [`Array.prototype.flat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)
    
*   [`Array.prototype.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)
    
*   [`Array.prototype.reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
    
*   [`TypedArray.prototype.reduceRight()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/reduceRight)
    
*   [`Object.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy)
    
*   [`Map.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/reduceright/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/array/reduceright (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FreduceRight&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Freduceright%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FreduceRight%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Freduceright%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")