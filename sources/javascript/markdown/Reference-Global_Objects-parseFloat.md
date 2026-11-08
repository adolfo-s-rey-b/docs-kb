*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#mdn-search)
    

parseFloat()
============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`parseFloat()`** function parses a string argument and returns a floating point number.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#try_it)

-------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#syntax)

-------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#parameters)

[`string`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#string)

The value to parse, [coerced to a string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
. Leading [whitespace](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
 in this argument is ignored.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#return_value)

A floating point number parsed from the given `string`, or [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 when the first non-whitespace character cannot be converted to a number.

**Note:** JavaScript does not have the distinction of "floating point numbers" and "integers" on the language level. [`parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
 and `parseFloat()` only differ in their parsing behavior, but not necessarily their return values. For example, `parseInt("42")` and `parseFloat("42")` would return the same value: a [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
 42.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#description)

-----------------------------------------------------------------------------------------------------------------------

The `parseFloat` function converts its first argument to a string, parses that string as a decimal number literal, then returns a number or `NaN`. The number syntax it accepts can be summarized as:

*   The characters accepted by `parseFloat()` are plus sign (`+`), minus sign (`-` U+002D HYPHEN-MINUS), decimal digits (`0` – `9`), decimal point (`.`), exponent indicator (`e` or `E`), and the `"Infinity"` literal.
*   The `+`/`-` signs can only appear strictly at the beginning of the string, or immediately following the `e`/`E` character. The decimal point can only appear once, and only before the `e`/`E` character. The `e`/`E` character can only appear once, and only if there is at least one digit before it.
*   Leading spaces in the argument are trimmed and ignored.
*   `parseFloat()` can also parse and return [`Infinity`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity)
     or `-Infinity` if the string starts with `"Infinity"` or `"-Infinity"` preceded by none or more white spaces.
*   `parseFloat()` picks the longest substring starting from the beginning that generates a valid number literal. If it encounters an invalid character, it returns the number represented up to that point, ignoring the invalid character and all characters following it.
*   If the argument's first character can't start a legal number literal per the syntax above, `parseFloat` returns [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
    .

Syntax-wise, `parseFloat()` parses a subset of the syntax that the [`Number()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number)
 function accepts. Namely, `parseFloat()` does not support non-decimal literals with `0x`, `0b`, or `0o` prefixes but supports everything else. However, `parseFloat()` is more lenient than `Number()` because it ignores trailing invalid characters, which would cause `Number()` to return `NaN`.

Similar to number literals and `Number()`, the number returned from `parseFloat()` may not be exactly equal to the number represented by the string, due to floating point range and inaccuracy. For numbers outside the `-1.7976931348623158e+308` – `1.7976931348623158e+308` range (see [`Number.MAX_VALUE`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_VALUE)
), `-Infinity` or `Infinity` is returned.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using parseFloat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#using_parsefloat)

The following examples all return `3.14`:

### [parseFloat() returning NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#parsefloat_returning_nan)

The following example returns `NaN`:

Anecdotally, because the string `NaN` itself is invalid syntax as accepted by `parseFloat()`, passing `"NaN"` returns `NaN` as well.

### [Returning Infinity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#returning_infinity)

Infinity values are returned when the number is outside the double-precision 64-bit IEEE 754-2019 format range:

Infinity is also returned when the string starts with `"Infinity"` or `"-Infinity"`:

### [Interaction with BigInt values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#interaction_with_bigint_values)

`parseFloat()` does not handle [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 values. It stops at the `n` character, and treats the preceding string as a normal integer, with possible loss of precision. If a BigInt value is passed to `parseFloat()`, it will be converted to a string, and the string will be parsed as a floating-point number, which may result in loss of precision as well.

You should pass the string to the [`BigInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
 function instead, without the trailing `n` character.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-parsefloat-string](https://tc39.es/ecma262/multipage/global-object.html#sec-parsefloat-string) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
    
*   [`Number.parseFloat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseFloat)
    
*   [`Number.parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseInt)
    
*   [`Number.prototype.toFixed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/parsefloat/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/parsefloat (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FparseFloat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fparsefloat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FparseFloat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fparsefloat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")