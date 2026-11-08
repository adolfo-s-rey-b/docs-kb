*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#mdn-search)
    

Iterator.zip()
==============

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/950)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Iterator.zip()`** static method creates a new [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
 object that aggregates elements from multiple iterable objects by yielding arrays containing elements at the same position. It essentially "zips" the input iterables together, allowing simultaneous iteration over them.

The [`Iterator.zipKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed)
 method is similar, but yields objects instead of arrays with keys you can specify.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#syntax)

---------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#parameters)

[`iterables`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#iterables)

An iterable of iterables whose elements are aggregated. It must be [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 and cannot be an [iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
. It should be finite, although its elements can be infinite iterables. Each element must implement either the [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 protocol or, failing that, the [iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 protocol. Strings are rejected: to zip strings, convert them to iterators explicitly using [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
.

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#options)

An object specifying behavior in case of inconsistent input lengths. It may have the following properties:

[`mode` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#mode)

One of the following:

*   `"shortest"` (default): The resulting iterator stops when one input iterable is exhausted.
*   `"longest"`: The resulting iterator stops when all input iterables are exhausted. Missing values from shorter iterables are filled according to the `padding` option.
*   `"strict"`: A [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
     is thrown if not all input iterables finish at the same time.

[`padding` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#padding)

An iterable object (not iterator). Only retrieved and validated when `mode` is `"longest"`. If `undefined` or absent, missing values from shorter iterables are filled with `undefined` (which is equivalent to passing an empty iterable). If an iterable is provided, it is iterated for the number of times equal to the number of elements in `iterables` _as soon as `Iterator.zip()` is called_. `padding[i]` is used for missing values for `iterables[i]` (assuming `padding` and `iterables` are provided as arrays; they don't have to be). If `padding` is shorter than `iterables`, `undefined` is used for the remaining iterables.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#return_value)

A new [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
 object. Each of its elements is an array with length equal to the number of input iterables, containing the elements from each input iterable at the corresponding position. If the `iterables` object is empty, the resulting iterator is created as completed.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#description)

-------------------------------------------------------------------------------------------------------------------------

The `Iterator.zip()` function behaves like a [transpose](https://en.wikipedia.org/wiki/Transpose "External link (opens in new tab)")
 operation, yielding arrays containing the elements at matching positions in each of the inputs. If we represent iterables as arrays, the input may looks like this:

The resulting iterator, regardless of the options, will start by yielding the following arrays:

After the first three arrays are yielded, the input iterable `b` is exhausted on the fourth `next()` call—it returns `{ done: true }`. What happens next depends on the `mode` option. If `mode` is `"shortest"` (the default), the resulting iterator stops here: the other two input iterators are [closed](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#errors_during_iteration)
. If `mode` is `"strict"`, an error is thrown because the other two iterables are _not_ finished when the second one yields the result `{ done: true }`. If `mode` is `"longest"`, the resulting iterator continues yielding arrays, filling missing values. For example, if `padding` is not provided, it defaults to `undefined`:

If `padding` is provided as an iterable, because there are three input iterables, the first three values from the `padding` iterable are used to fill missing values. Let's suppose that `padding` is an array with values `[p1, p2, p3]`. Then `p2` is used to fill the missing value from the input iterable `b`, and `p1` is used to fill the missing value from the input iterable `a`:

If the `padding` iterable has fewer than three values, the remaining missing values are filled with `undefined`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#examples)

-------------------------------------------------------------------------------------------------------------------

### [Iteration over a map with indices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#iteration_over_a_map_with_indices)

Using `Iterator.zip()`, you can iterate over any iterable object (strings aren't supported by default) while also having access to an incrementing counter:

`numbers` is an infinite iterator that generates incrementing numbers starting from `0`. Because `Iterator.zip()` stops by default when the shortest input iterable is exhausted, the loop iterates exactly three times. The `numbers` iterator is properly closed after the loop ends; it doesn't cause an infinite loop.

### [Creating a Map from lists of keys and values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#creating_a_map_from_lists_of_keys_and_values)

Suppose you have two arrays: one with keys and another with values. You can use `Iterator.zip()` to combine them into a [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
:

### [Joint iteration over multiple data sources](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#joint_iteration_over_multiple_data_sources)

Suppose you have data coming from multiple sources, such as multiple microservices or databases. You know that each source provides related data in the same order, and you want to process them together. You can use `Iterator.zip()` to achieve this:

### [Providing padding for uneven iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#providing_padding_for_uneven_iterables)

When zipping iterables of different lengths with `mode` set to `"longest"`, you can provide a `padding` iterable to specify the values used to fill in missing entries:

### [Zipping strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#zipping_strings)

Strings are not accepted as input iterables to `Iterator.zip()`, because it is now considered a mistake to make strings implicitly iterable. To zip strings, convert them to iterators explicitly using [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
:

In some cases, you may wish to split by [grapheme clusters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)
 instead of code units. In that case, you can use the [`Intl.Segmenter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter)
 API:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-iterator.zip](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-iterator.zip) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Iterator.zip` in `core-js`](https://core-js.io/docs/features/ecmascript/iterator "External link (opens in new tab)")
    
*   [es-shims polyfill of `Iterator.zip`](https://www.npmjs.com/package/es-iterator-helpers "External link (opens in new tab)")
    
*   [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)
    
*   [`Iterator.zipKeyed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zipKeyed)
    
*   [`Iterator.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/from)
    
*   [`Iterator.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/zip/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/iterator/zip/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/iterator/zip (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator%2Fzip&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%2Fzip%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIterator%2Fzip%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fiterator%2Fzip%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")