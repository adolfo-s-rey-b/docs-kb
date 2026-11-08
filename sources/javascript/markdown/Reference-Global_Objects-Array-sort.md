*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#mdn-search)
    

Array.prototype.sort()
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`sort()`** method of [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 instances sorts the elements of an array _[in place](https://en.wikipedia.org/wiki/In-place_algorithm "External link (opens in new tab)")
_ and returns the reference to the same array, now sorted. The default sort order is ascending, built upon converting the elements into strings, then comparing their sequences of UTF-16 code unit values.

The time and space complexity of the sort cannot be guaranteed as it depends on the implementation.

To sort the elements in an array without mutating the original array, use [`toSorted()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#try_it)

-------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#syntax)

-------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#parameters)

[`compareFn` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#comparefn)

A function that determines the order of the elements. The function is called with the following arguments:

[`a`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#a)

The first element for comparison. Will never be `undefined`.

[`b`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#b)

The second element for comparison. Will never be `undefined`.

It should return a number where:

*   A negative value indicates that `a` should come before `b`.
*   A positive value indicates that `a` should come after `b`.
*   Zero or `NaN` indicates that `a` and `b` are considered equal.

To memorize this, remember that `(a, b) => a - b` sorts numbers in ascending order.

If omitted, the array elements are converted to strings, then sorted according to each character's Unicode code point value.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#return_value)

The reference to the original array, now sorted. Note that the array is sorted _[in place](https://en.wikipedia.org/wiki/In-place_algorithm "External link (opens in new tab)")
_, and no copy is made.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#description)

-----------------------------------------------------------------------------------------------------------------------

If `compareFn` is not supplied, all non-`undefined` array elements are sorted by converting them to strings and comparing strings in UTF-16 code units order. For example, "banana" comes before "cherry". In a numeric sort, 9 comes before 80, but because numbers are converted to strings, "80" comes before "9" in the Unicode order. All `undefined` elements are sorted to the end of the array.

The `sort()` method preserves empty slots. If the source array is [sparse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
, the empty slots are moved to the end of the array, and always come after all the `undefined`.

**Note:** In UTF-16, Unicode characters above `\uFFFF` are encoded as two surrogate code units, of the range `\uD800` - `\uDFFF`. The value of each code unit is taken separately into account for the comparison. Thus the character formed by the surrogate pair `\uD855\uDE51` will be sorted before the character `\uFF3A`.

If `compareFn` is supplied, all non-`undefined` array elements are sorted according to the return value of the compare function (all `undefined` elements are sorted to the end of the array, with no call to `compareFn`).

| `compareFn(a, b)` return value | sort order |
| --- | --- |
| \> 0 | sort `a` after `b`, e.g., `[b, a]` |
| < 0 | sort `a` before `b`, e.g., `[a, b]` |
| \=== 0 | keep original order of `a` and `b` |

So, the compare function has the following form:

More formally, the comparator is expected to have the following properties, in order to ensure proper sort behavior:

*   _Pure_: The comparator does not mutate the objects being compared or any external state. (This is important because there's no guarantee _when_ and _how_ the comparator will be called, so any particular call should not produce visible effects to the outside.)
*   _Stable_: The comparator returns the same result with the same pair of input.
*   _Reflexive_: `compareFn(a, a) === 0`.
*   _Anti-symmetric_: `compareFn(a, b)` and `compareFn(b, a)` must both be `0` or have opposite signs.
*   _Transitive_: If `compareFn(a, b)` and `compareFn(b, c)` are both positive, zero, or negative, then `compareFn(a, c)` has the same positivity as the previous two.

A comparator conforming to the constraints above will always be able to return all of `1`, `0`, and `-1`, or consistently return `0`. For example, if a comparator only returns `1` and `0`, or only returns `0` and `-1`, it will not be able to sort reliably because _anti-symmetry_ is broken. A comparator that always returns `0` will cause the array to not be changed at all, but is reliable nonetheless.

The default lexicographic comparator satisfies all constraints above.

To compare numbers instead of strings, the compare function can subtract `b` from `a`. The following function will sort the array in ascending order (if it doesn't contain `NaN`):

The `sort()` method is [generic](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#generic_array_methods)
. It only expects the `this` value to have a `length` property and integer-keyed properties. Although strings are also array-like, this method is not suitable to be applied on them, as strings are immutable.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#examples)

-----------------------------------------------------------------------------------------------------------------

### [Creating, displaying, and sorting an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#creating_displaying_and_sorting_an_array)

The following example creates four arrays and displays the original array, then the sorted arrays. The numeric arrays are sorted without a compare function, then sorted using one.

### [Sorting array of objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#sorting_array_of_objects)

Arrays of objects can be sorted by comparing the value of one of their properties.

### [Sorting non-ASCII characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#sorting_non-ascii_characters)

For sorting strings with non-[ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 characters, i.e., strings with accented characters (e, é, è, a, ä, etc.), strings from languages other than English, use [`String.prototype.localeCompare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)
. This function can compare those characters so they appear in the right order.

### [Sorting with map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#sorting_with_map)

The `compareFn` can be invoked multiple times per element within the array. Depending on the `compareFn`'s nature, this may yield a high overhead. The more work a `compareFn` does and the more elements there are to sort, it may be more efficient to use [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
 for sorting. The idea is to traverse the array once to extract the actual values used for sorting into a temporary array, sort the temporary array, and then traverse the temporary array to achieve the right order.

There is an open source library available called [mapsort](https://github.com/Pimm/mapsort "External link (opens in new tab)")
 which applies this approach.

### [sort() returns the reference to the same array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#sort_returns_the_reference_to_the_same_array)

The `sort()` method returns a reference to the original array, so mutating the returned array will mutate the original array as well.

In case you want `sort()` to not mutate the original array, but return a [shallow-copied](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)
 array like other array methods (e.g., [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
) do, use the [`toSorted()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted)
 method. Alternatively, you can do a shallow copy before calling `sort()`, using the [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
 or [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
.

### [Sort stability](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#sort_stability)

Since version 10 (or ECMAScript 2019), the specification dictates that `Array.prototype.sort` is stable.

For example, say you had a list of students alongside their grades. Note that the list of students is already pre-sorted by name in alphabetical order:

After sorting this array by `grade` in ascending order:

The `students` variable will then have the following value:

It's important to note that students that have the same grade (for example, Alex and Devlin), will remain in the same order as before calling the sort. This is what a stable sorting algorithm guarantees.

Before version 10 (or ECMAScript 2019), sort stability was not guaranteed, meaning that you could end up with the following:

### [Sorting with non-well-formed comparator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#sorting_with_non-well-formed_comparator)

If a comparing function does not satisfy all of purity, stability, reflexivity, anti-symmetry, and transitivity rules, as explained in the [description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#description)
, the program's behavior is not well-defined.

For example, consider this code:

The `compareFn` function here is not well-formed, because it does not satisfy anti-symmetry: if `a > b`, it returns `1`; but by swapping `a` and `b`, it returns `0` instead of a negative value. Therefore, the resulting array will be different across engines. For example, V8 (used by Chrome, Node.js, etc.) and JavaScriptCore (used by Safari) would not sort the array at all and return `[3, 1, 4, 1, 5, 9]`, while SpiderMonkey (used by Firefox) will return the array sorted ascendingly, as `[1, 1, 3, 4, 5, 9]`.

However, if the `compareFn` function is changed slightly so that it returns `-1` or `0`:

Then V8 and JavaScriptCore sorts it descendingly, as `[9, 5, 4, 3, 1, 1]`, while SpiderMonkey returns it as-is: `[3, 1, 4, 1, 5, 9]`.

Due to this implementation inconsistency, you are always advised to make your comparator well-formed by following the five constraints.

### [Using sort() on sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#using_sort_on_sparse_arrays)

Empty slots are moved to the end of the array.

### [Calling sort() on non-array objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#calling_sort_on_non-array_objects)

The `sort()` method reads the `length` property of `this`. It then collects all existing integer-keyed properties in the range of `0` to `length - 1`, sorts them, and writes them back. If there are missing properties in the range, the corresponding trailing properties are [deleted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
, as if the non-existent properties are sorted towards the end.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-array.prototype.sort](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.sort) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Array.prototype.sort` with modern behavior like stable sort in `core-js`](https://core-js.io/docs/features/ecmascript/array "External link (opens in new tab)")
    
*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    
*   [`Array.prototype.reverse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)
    
*   [`Array.prototype.toSorted()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toSorted)
    
*   [`String.prototype.localeCompare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)
    
*   [`TypedArray.prototype.sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/sort)
    
*   [Getting things sorted in V8](https://v8.dev/blog/array-sort "External link (opens in new tab)")
     on v8.dev (2018)
*   [Stable `Array.prototype.sort`](https://v8.dev/features/stable-sort "External link (opens in new tab)")
     on v8.dev (2019)
*   [`Array.prototype.sort` stability](https://mathiasbynens.be/demo/sort-stability "External link (opens in new tab)")
     by Mathias Bynens

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/sort/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/array/sort (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fsort&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fsort%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fsort%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fsort%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")