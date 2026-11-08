*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#mdn-search)
    

String.prototype.split()
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`split()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values takes a pattern and divides this string into an ordered list of substrings by searching for the pattern, puts these substrings into an array, and returns the array.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#try_it)

---------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#syntax)

---------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#parameters)

[`separator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#separator)

The pattern describing where each split should occur. Can be `undefined`, a string, or an object with a [`Symbol.split`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/split)
 method — the typical example being a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
. Omitting `separator` or passing `undefined` causes `split()` to return an array with the calling string as a single element. All values that are not `undefined` or objects with a `[Symbol.split]()` method are [coerced to strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
.

[`limit` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#limit)

A non-negative integer specifying a limit on the number of substrings to be included in the array. If provided, splits the string at each occurrence of the specified `separator`, but stops when `limit` entries have been placed in the array. Any leftover text is not included in the array at all.

*   The array may contain fewer entries than `limit` if the end of the string is reached before the limit is reached.
*   If `limit` is `0`, `[]` is returned.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#return_value)

If `separator` is a string, an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 of strings is returned, split at each point where the `separator` occurs in the given string.

If `separator` is a regex, the returned [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 also contains the [captured groups](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group)
 for each separator match; see below for details. The capturing groups may be unmatched, in which case they are `undefined` in the array.

If `separator` has a custom `[Symbol.split]()` method, its return value is directly returned.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#description)

-------------------------------------------------------------------------------------------------------------------------

If `separator` is a non-empty string, the target string is split by all matches of the `separator` without including `separator` in the results. For example, a string containing tab separated values (TSV) could be parsed by passing a tab character as the separator, like `myString.split("\t")`. If `separator` contains multiple characters, that entire character sequence must be found in order to split. If `separator` appears at the beginning (or end) of the string, it still has the effect of splitting, resulting in an empty (i.e., zero length) string appearing at the first (or last) position of the returned array. If `separator` does not occur in `str`, the returned array contains one element consisting of the entire string.

If `separator` is an empty string (`""`), `str` is converted to an array of each of its UTF-16 "characters", without empty strings on either ends of the resulting string.

**Note:** `"".split("")` is therefore the only way to produce an empty array when a string is passed as `separator` and `limit` is not `0`.

**Warning:** When the empty string (`""`) is used as a separator, the string is **not** split by _user-perceived characters_ ([grapheme clusters](https://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries "External link (opens in new tab)")
) or unicode characters (code points), but by UTF-16 code units. This destroys [surrogate pairs](https://unicode.org/faq/utf_bom.html#utf16-2 "External link (opens in new tab)")
. See ["How do you get a string to a character array in JavaScript?" on Stack Overflow](https://stackoverflow.com/questions/4547609/how-to-get-character-array-from-a-string/34717402#34717402 "External link (opens in new tab)")
.

If `separator` is a regexp that matches empty strings, whether the match is split by UTF-16 code units or Unicode code points depends on if the regex is [Unicode-aware](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
.

If `separator` is a regular expression with capturing groups, then each time `separator` matches, the captured groups (including any `undefined` results) are spliced into the output array. This behavior is specified by the regexp's [`Symbol.split`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/split)
 method.

If `separator` is an object with a [`Symbol.split`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/split)
 method, that method is called with the target string and `limit` as arguments, and `this` set to the object. Its return value becomes the return value of `split`.

Any other value will be coerced to a string before being used as separator.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#examples)

-------------------------------------------------------------------------------------------------------------------

### [Using split()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#using_split)

When the string is empty and a non-empty separator is specified, `split()` returns `[""]`. If the string and separator are both empty strings, an empty array is returned.

The following example defines a function that splits a string into an array of strings using `separator`. After splitting the string, the function logs messages indicating the original string (before the split), the separator used, the number of elements in the array, and the individual array elements.

This example produces the following output:

The original string is: "Oh brave new world that has such people in it."
The separator is: " "
The array has 10 elements: Oh / brave / new / world / that / has / such / people / in / it.

The original string is: "Oh brave new world that has such people in it."
The separator is: "undefined"
The array has 1 elements: Oh brave new world that has such people in it.

The original string is: "Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec"
The separator is: ","
The array has 12 elements: Jan / Feb / Mar / Apr / May / Jun / Jul / Aug / Sep / Oct / Nov / Dec

### [Removing spaces from a string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#removing_spaces_from_a_string)

In the following example, `split()` looks for zero or more spaces, followed by a semicolon, followed by zero or more spaces—and, when found, removes the spaces and the semicolon from the string. `nameList` is the array returned as a result of `split()`.

This logs two lines; the first line logs the original string, and the second line logs the resulting array.

Harry Trump ;Fred Barney; Helen Rigby ; Bill Abel ;Chris Hand
\[ "Harry Trump", "Fred Barney", "Helen Rigby", "Bill Abel", "Chris Hand", "" \]

### [Returning a limited number of splits](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#returning_a_limited_number_of_splits)

In the following example, `split()` looks for spaces in a string and returns the first 3 splits that it finds.

### [Splitting with a `RegExp` to include parts of the separator in the result](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#splitting_with_a_regexp_to_include_parts_of_the_separator_in_the_result)

If `separator` is a regular expression that contains capturing parentheses `( )`, matched results are included in the array.

**Note:** `\d` matches the [character class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
 for digits between 0 and 9.

### [Using a custom splitter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#using_a_custom_splitter)

An object with a `Symbol.split` method can be used as a splitter with custom behavior.

The following example splits a string using an internal state consisting of an incrementing number:

The following example uses an internal state to enforce certain behavior, and to ensure a "valid" result is produced.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.split](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.split) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `String.prototype.split` in `core-js` with fixes and implementation of modern behavior like `Symbol.split` support](https://core-js.io/docs/features/ecmascript/string-regexp "External link (opens in new tab)")
    
*   [es-shims polyfill of `String.prototype.split`](https://www.npmjs.com/package/string.prototype.split "External link (opens in new tab)")
    
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
     guide
*   [`String.prototype.charAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)
    
*   [`String.prototype.indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf)
    
*   [`String.prototype.lastIndexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/lastIndexOf)
    
*   [`Array.prototype.join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/split/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/split (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fsplit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fsplit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fsplit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fsplit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")