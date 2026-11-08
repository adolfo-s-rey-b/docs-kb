*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#mdn-search)
    

Array.prototype.copyWithin()
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`copyWithin()`** method of [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 instances shallow copies part of this array to another location in the same array and returns this array without modifying its length.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#try_it)

-------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#syntax)

-------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#parameters)

[`target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#target)

Zero-based index at which to copy the sequence to, [converted to an integer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#integer_conversion)
. This corresponds to where the element at `start` will be copied to, and all elements between `start` and `end` are copied to succeeding indices.

*   Negative index counts back from the end of the array — if `-array.length <= target < 0`, `target + array.length` is used.
*   If `target < -array.length`, `0` is used.
*   If `target >= array.length`, nothing is copied.
*   If `target` is positioned after `start` after normalization, copying only happens until the end of `array.length` (in other words, `copyWithin()` never extends the array).

[`start`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#start)

Zero-based index at which to start copying elements from, [converted to an integer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#integer_conversion)
.

*   Negative index counts back from the end of the array — if `-array.length <= start < 0`, `start + array.length` is used.
*   If `start < -array.length`, `0` is used.
*   If `start >= array.length`, nothing is copied.

[`end` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#end)

Zero-based index at which to end copying elements from, [converted to an integer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#integer_conversion)
. `copyWithin()` copies up to but not including `end`.

*   Negative index counts back from the end of the array — if `-array.length <= end < 0`, `end + array.length` is used.
*   If `end < -array.length`, `0` is used.
*   If `end >= array.length` or `end` is omitted or `undefined`, `array.length` is used, causing all elements until the end to be copied.
*   If `end` implies a position before or at the position that `start` implies, nothing is copied.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#return_value)

The modified array.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#description)

-----------------------------------------------------------------------------------------------------------------------------

The `copyWithin()` method works like C and C++'s `memmove`, and is a high-performance method to shift the data of an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
. This especially applies to the [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/copyWithin)
 method of the same name. The sequence is copied and pasted as one operation; the pasted sequence will have the copied values even when the copy and paste region overlap.

Because `undefined` becomes `0` when converted to an integer, omitting the `start` parameter has the same effect as passing `0`, which copies the entire array to the target position, equivalent to a right shift where the right boundary is clipped off and the left boundary is duplicated. This behavior may confuse readers of your code, so you should explicitly pass `0` as `start` instead.

The `copyWithin()` method is a [mutating method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#copying_methods_and_mutating_methods)
. It does not alter the length of `this`, but it will change the content of `this` and create new properties or delete existing properties, if necessary.

The `copyWithin()` method preserves empty slots. If the region to be copied from is [sparse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
, the empty slots' corresponding new indices are [deleted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
 and also become empty slots.

The `copyWithin()` method is [generic](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#generic_array_methods)
. It only expects the `this` value to have a `length` property and integer-keyed properties. Although strings are also array-like, this method is not suitable to be applied on them, as strings are immutable.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Using copyWithin()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#using_copywithin)

### [Using copyWithin() on sparse arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#using_copywithin_on_sparse_arrays)

`copyWithin()` will propagate empty slots.

### [Calling copyWithin() on non-array objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#calling_copywithin_on_non-array_objects)

The `copyWithin()` method reads the `length` property of `this` and then manipulates the integer indices involved.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-array.prototype.copywithin](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.copywithin) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Array.prototype.copyWithin` in `core-js`](https://core-js.io/docs/features/ecmascript/array "External link (opens in new tab)")
    
*   [es-shims polyfill of `Array.prototype.copyWithin`](https://www.npmjs.com/package/array.prototype.copywithin "External link (opens in new tab)")
    
*   [Indexed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
     guide
*   [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    
*   [`TypedArray.prototype.copyWithin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/copyWithin)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/array/copywithin/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/array/copywithin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FcopyWithin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fcopywithin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FcopyWithin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Farray%2Fcopywithin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")