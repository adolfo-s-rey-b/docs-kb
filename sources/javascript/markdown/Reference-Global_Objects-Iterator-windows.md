*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#mdn-search)
    

Iterator.prototype.windows()
============================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#browser_compatibility)
 carefully before using this in production.

The **`windows()`** method of [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
 instances returns a new [iterator helper object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#iterator_helper_objects)
 that yields a sliding window of elements. Each time the helper is iterated, it yields an array removing the first element from the previous iteration and adding the next element from the original iterator.

To yield distinct chunks, see [`Iterator.prototype.chunks()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/chunks)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#syntax)

-------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#parameters)

[`windowSize`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#windowsize)

The number of elements in the sliding window. Must be a positive integer less than 232 (the maximum array length).

[`underSized` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#undersized)

A string specifying what to do when the number of elements in the iterator is less than `windowSize` but greater than 0. It can be one of the following:

[`"only-full"` (default)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#only-full)

Ignore the partial window. The returned iterator immediately completes as if the input is empty.

[`"allow-partial"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#allow-partial)

Yield all elements in the partial window as an array (with length less than `windowSize`).

Note that when the input is empty, the returned iterator always immediately completes without yielding an empty array.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#return_value)

A new [iterator helper object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator#iterator_helper_objects)
. The first time the returned iterator helper's `next()` method is called, the current iterator is immediately advanced by `windowSize` elements. If that many elements are available, they are yielded together as an array. Otherwise, the behavior depends on the `underSized` argument: the iterator either immediately completes without yielding anything (with `"only-full"` or with a fully empty input), or an array of length less than `windowSize` is yielded.

Afterwards, each time, the yielded array consists of the previous array, the leftmost element removed, a new element retrieved from the input iterable appended. When the input iterable is exhausted, the iterator helper also completes.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown if `limit` is not an integer, or if `underSized` is not one of the allowed values.

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown if `limit` is less than 1 or greater than 232－1.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Moving average](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#moving_average)

The following example creates an iterator that yields terms in the Fibonacci sequence. Then, a new iterator is created, each time yielding the average of two adjacent elements.

This process, known as a moving average, is very useful in signal processing.

### [Enumerating substrings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#enumerating_substrings)

The following example enumerates all substrings of a given length in a string. The `windows()` method is used to create a sliding window of characters, which are then joined together to form substrings.

**Note:** This is probably much less efficient than manually iterating a number index and calling the [`String.prototype.substring()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring)
 method.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Iterator Chunking  <br>\# sec-iterator.prototype.windows](https://tc39.es/proposal-iterator-chunking/#sec-iterator.prototype.windows) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Iterator.prototype.windows` in `core-js`](https://core-js.io/docs/features/ecmascript/iterator "External link (opens in new tab)")
    
*   [es-shims polyfill of `Iterator.prototype.windows`](https://www.npmjs.com/package/es-iterator-helpers "External link (opens in new tab)")
    
*   [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
    
*   [`Iterator.prototype.chunks()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/chunks)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/windows/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/iterator/windows/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/iterator/windows (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator%2Fwindows&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%2Fwindows%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator%2Fwindows%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%2Fwindows%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")