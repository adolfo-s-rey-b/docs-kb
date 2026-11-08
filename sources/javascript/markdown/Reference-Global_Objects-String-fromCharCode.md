*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#mdn-search)
    

String.fromCharCode()
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`String.fromCharCode()`** static method returns a string created from the specified sequence of UTF-16 code units.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#try_it)

----------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#syntax)

----------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#parameters)

[`num1`, …, `numN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#num1)

A number between `0` and `65535` (`0xFFFF`) representing a UTF-16 code unit. Numbers greater than `0xFFFF` are truncated to the last 16 bits. No validity checks are performed.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#return_value)

A string of length `N` consisting of the `N` specified UTF-16 code units.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#description)

--------------------------------------------------------------------------------------------------------------------------------

Because `fromCharCode()` is a static method of `String`, you always use it as `String.fromCharCode()`, rather than as a method of a `String` value you created.

Unicode code points range from `0` to `1114111` (`0x10FFFF`). `charCodeAt()` always returns a value that is less than `65536`, because the higher code points are represented by _a pair_ of 16-bit surrogate pseudo-characters. Therefore, in order to produce a full character with value greater than `65535`, it is necessary to provide two code units (as if manipulating a string with two characters). For information on Unicode, see [UTF-16 characters, Unicode code points, and grapheme clusters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)
.

Because `fromCharCode()` only works with 16-bit values (same as the `\u` escape sequence), a surrogate pair is required in order to return a supplementary character. For example, both `String.fromCharCode(0xd83c, 0xdf03)` and `"\ud83c\udf03"` return code point `U+1F303` "Night with Stars". While there is a mathematical relationship between the supplementary code point value (e.g., `0x1f303`) and both surrogate values that represent it (e.g., `0xd83c` and `0xdf03`), it does require an extra step to either calculate or look up the surrogate pair values every time a supplementary code point is to be used. For this reason, it's more convenient to use [`String.fromCodePoint()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCodePoint)
, which allows for returning supplementary characters based on their actual code point value. For example, `String.fromCodePoint(0x1f303)` returns code point `U+1F303` "Night with Stars".

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#examples)

--------------------------------------------------------------------------------------------------------------------------

### [Using fromCharCode()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#using_fromcharcode)

BMP characters, in UTF-16, use a single code unit:

Supplementary characters, in UTF-16, require two code units (i.e., a surrogate pair):

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#specifications)

--------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.fromcharcode](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.fromcharcode) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode#see_also)

--------------------------------------------------------------------------------------------------------------------------

*   [`String.fromCodePoint()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCodePoint)
    
*   [`String.prototype.charAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)
    
*   [`String.prototype.charCodeAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt)
    
*   [`String.prototype.codePointAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/codePointAt)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/fromcharcode/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/fromcharcode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2FfromCharCode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Ffromcharcode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2FfromCharCode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Ffromcharcode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")