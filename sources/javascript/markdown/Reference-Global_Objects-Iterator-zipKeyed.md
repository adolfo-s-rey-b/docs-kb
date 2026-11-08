*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#mdn-search)
    

Iterator.zipKeyed()
===================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/950)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Iterator.zipKeyed()`** static method creates a new [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
 object that aggregates elements from multiple iterable objects by yielding objects containing elements at the same position, with keys specified by the input. It essentially "zips" the input iterables together, allowing simultaneous iteration over them.

The [`Iterator.zip()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip)
 method is similar, but yields arrays instead of objects.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#syntax)

--------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#parameters)

[`iterables`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#iterables)

An object. Each property's key is used as the key in the resulting objects. The property's value must implement either the [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 protocol or, failing that, the [iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 protocol. These iterables may be infinite. Strings are rejected: to zip strings, convert them to iterators explicitly using [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
.

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#options)

An object specifying behavior in case of inconsistent input lengths. It may have the following properties:

[`mode` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#mode)

One of the following:

*   `"shortest"` (default): The resulting iterator stops when one input iterable is exhausted.
*   `"longest"`: The resulting iterator stops when all input iterables are exhausted. Missing values from shorter iterables are filled according to the `padding` option.
*   `"strict"`: A [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
     is thrown if not all input iterables finish at the same time.

[`padding` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#padding)

An object. Only retrieved and validated when `mode` is `"longest"`. If `undefined` or absent, missing values from shorter iterables are filled with `undefined` (which is equivalent to passing an empty object). If an object is provided, each key of the `iterables` argument is retrieved _as soon as `Iterator.zipKeyed()` is called_. `padding[key]` is used for missing values for `iterables[key]`. If the `padding` object is missing some keys, those keys are filled with `undefined`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#return_value)

A new [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
 object. Each of its elements is an object with the same keys as the `iterables` argument, containing the elements from each input iterable at the corresponding position.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#description)

------------------------------------------------------------------------------------------------------------------------------

The `Iterator.zipKeyed()` function behaves like [`Iterator.zip()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip)
; the only difference is that you can specify the keys used in the resulting objects, while `Iterator.zip()` always uses numeric indices (by yielding arrays).

If we represent iterables as arrays, the input may looks like this:

The resulting iterator, regardless of the options, will start by yielding the following arrays:

After the first three objects are yielded, the input iterable `b` is exhausted on the fourth `next()` call—it returns `{ done: true }`. What happens next depends on the `mode` option. If `mode` is `"shortest"` (the default), the resulting iterator stops here: the other two input iterators are [closed](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#errors_during_iteration)
. If `mode` is `"strict"`, an error is thrown because the other two iterables are _not_ finished when the second one yields the result `{ done: true }`. If `mode` is `"longest"`, the resulting iterator continues yielding objects, filling missing values. For example, if `padding` is not provided, it defaults to `undefined`:

If `padding` is provided as an object, it may look like `{ a: p1, b: p2, c: p3 }`. Then `p2` is used to fill the missing value from the input iterable `b`, and `p1` is used to fill the missing value from the input iterable `a`:

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#examples)

------------------------------------------------------------------------------------------------------------------------

### [Transposing tabular data](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#transposing_tabular_data)

There are two common ways to represent tabular data: as an object where each property is a column, or as an array of objects where each object is a row. This example shows how you can iterate the column-based representation by rows using `Iterator.zipKeyed()`.

Most use cases of `Iterator.zipKeyed()` are identical to those of [`Iterator.zip()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip)
. Which one to use depends on whether you already have an object of iterables (use `zipKeyed()`) or an array of iterables (use `zip()`). We recommend using `zipKeyed()` when possible, because specifying explicit keys makes it harder to accidentally mix up the order of iterables.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#specifications)

------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-iterator.zipkeyed](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-iterator.zipkeyed) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed#see_also)

------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Iterator.zipKeyed` in `core-js`](https://core-js.io/docs/features/ecmascript/iterator "External link (opens in new tab)")
    
*   [es-shims polyfill of `Iterator.zipKeyed`](https://www.npmjs.com/package/es-iterator-helpers "External link (opens in new tab)")
    
*   [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
    
*   [`Iterator.zip()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip)
    
*   [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
    
*   [`Iterator.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/iterator/zipkeyed/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/iterator/zipkeyed (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator%2FzipKeyed&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%2Fzipkeyed%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator%2FzipKeyed%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%2Fzipkeyed%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")