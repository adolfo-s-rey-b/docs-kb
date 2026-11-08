*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#mdn-search)
    

String: length
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`length`** data property of a [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 value contains the length of the string in UTF-16 code units.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#try_it)

----------------------------------------------------------------------------------------------------------------

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#value)

--------------------------------------------------------------------------------------------------------------

A non-negative integer.

|     |     |
| --- | --- |
| Writable | no  |
| Enumerable | no  |
| Configurable | no  |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#description)

--------------------------------------------------------------------------------------------------------------------------

This property returns the number of code units in the string. JavaScript uses [UTF-16](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)
 encoding, where each Unicode character may be encoded as one or two code units, so it's possible for the value returned by `length` to not match the actual number of Unicode characters in the string. For common scripts like Latin, Cyrillic, wellknown CJK characters, etc., this should not be an issue, but if you are working with certain scripts, such as emojis, [mathematical symbols](https://en.wikipedia.org/wiki/Mathematical_Alphanumeric_Symbols "External link (opens in new tab)")
, or obscure Chinese characters, you may need to account for the difference between code units and characters.

The language specification requires strings to have a maximum length of 253 - 1 elements, which is the upper limit for [precise integers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
. However, a string with this length needs 16384TiB of storage, which cannot fit in any reasonable device's memory, so implementations tend to lower the threshold, which allows the string's length to be conveniently stored in a 32-bit integer.

*   In V8 (used by Chrome and Node), the maximum length is 229 - 24 (~1GiB). On 32-bit systems, the maximum length is 228 - 16 (~512MiB).
*   In Firefox, the maximum length is 230 - 2 (~2GiB). Before Firefox 65, the maximum length was 228 - 1 (~512MiB).
*   In Safari, the maximum length is 231 - 1 (~4GiB).

**Note:** All memory sizes above assume strings are stored in UTF-16 encoding in memory, which may be an overestimate. The actual space used by a string is subject to JavaScript engine optimizations, and all major engines use a more compact internal representation, such as one-byte storage, for strings containing only Latin-1 characters.

If you are working with large strings in other encodings (such as UTF-8 files or blobs), note that when you load the data into a JS string, the encoding always becomes UTF-16. The size of the string may be different from the size of the source file.

For an empty string, `length` is 0.

The static property `String.length` is unrelated to the length of strings. It's the [arity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
 of the `String` function (loosely, the number of formal parameters it has), which is 1.

Since `length` counts code units instead of characters, if you want to get the number of characters, you can first split the string with its [iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Symbol.iterator)
, which iterates by characters:

If you want to count characters by _grapheme clusters_, use [`Intl.Segmenter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter)
. You can first pass the string you want to split to the [`segment()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment)
 method, and then iterate over the returned `Segments` object to get the length:

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#examples)

--------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#basic_usage)

### [Strings with length not equal to the number of characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#strings_with_length_not_equal_to_the_number_of_characters)

### [Assigning to length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#assigning_to_length)

Because string is a primitive, attempting to assign a value to a string's `length` property has no observable effect, and will throw in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-properties-of-string-instances-length](https://tc39.es/ecma262/multipage/text-processing.html#sec-properties-of-string-instances-length) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [`Array`: `length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/length/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/length (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Flength&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Flength%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Flength%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Flength%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb052ff8270b38fccd3996df52dbe800f9c39f374%0A*+Document+last+modified%3A+2026-09-02T04%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")