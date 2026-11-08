*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#mdn-search)
    

String.prototype.substring()
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`substring()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values returns the part of this string from the start index up to and excluding the end index, or to the end of the string if no end index is supplied.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#try_it)

-------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#syntax)

-------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#parameters)

[`indexStart`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#indexstart)

The index of the first character to include in the returned substring.

[`indexEnd` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#indexend)

The index of the first character to exclude from the returned substring.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#return_value)

A new string containing the specified part of the given string.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#description)

-----------------------------------------------------------------------------------------------------------------------------

`substring()` extracts characters from `indexStart` up to _but not including_ `indexEnd`. In particular:

*   If `indexEnd` is omitted or `undefined`, `substring()` extracts characters to the end of the string.
*   If `indexStart` is equal to `indexEnd`, `substring()` returns an empty string.
*   If `indexStart` is greater than `indexEnd`, then the effect of `substring()` is as if the two arguments were swapped; see example below.

Any argument value that is less than `0` or greater than `str.length` is treated as if it were `0` and `str.length`, respectively.

Any argument value that is [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 is treated as if it were `0`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Using substring()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#using_substring)

The following example uses `substring()` to display characters from the string `"Mozilla"`:

### [Using substring() with length property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#using_substring_with_length_property)

The following example uses the `substring()` method and [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
 property to extract the last characters of a particular string. This method may be easier to remember, given that you don't need to know the starting and ending indices as you would in the above examples.

### [The difference between substring() and substr()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#the_difference_between_substring_and_substr)

There are subtle differences between the `substring()` and [`substr()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)
 methods, so you should be careful not to get them confused.

*   The two parameters of `substr()` are `start` and `length`, while for `substring()`, they are `start` and `end`.
*   `substr()`'s `start` index will wrap to the end of the string if it is negative, while `substring()` will clamp it to `0`.
*   Negative lengths in `substr()` are treated as zero, while `substring()` will swap the two indexes if `end` is less than `start`.

Furthermore, `substr()` is considered a _legacy feature in ECMAScript_, so it is best to avoid using it if possible.

### [Differences between substring() and slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#differences_between_substring_and_slice)

The `substring()` and [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
 methods are almost identical, but there are a couple of subtle differences between the two, especially in the way negative arguments are dealt with.

The `substring()` method swaps its two arguments if `indexStart` is greater than `indexEnd`, meaning that a string is still returned. The [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
 method returns an empty string if this is the case.

If either or both of the arguments are negative or `NaN`, the `substring()` method treats them as if they were `0`.

`slice()` also treats `NaN` arguments as `0`, but when it is given negative values it counts backwards from the end of the string to find the indexes.

See the [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
 page for more examples with negative numbers.

### [Replacing a substring within a string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#replacing_a_substring_within_a_string)

The following example replaces a substring within a string. It will replace both individual characters and substrings. The function call at the end of the example creates a string `Brave New Web` from the original string `Brave New World`.

Note that this can result in an infinite loop if `oldS` is itself a substring of `newS` — for example, if you attempted to replace `"World"` with `"OtherWorld"` here.

A better method for replacing strings is as follows:

The code above serves as an example for substring operations. If you need to replace substrings, most of the time you will want to use [`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.substring](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.substring) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [`String.prototype.substr()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)
    
*   [`String.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/substring/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/substring (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fsubstring&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fsubstring%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fsubstring%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fsubstring%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")