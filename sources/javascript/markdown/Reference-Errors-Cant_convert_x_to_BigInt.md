*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt#mdn-search)
    

TypeError: can't convert x to BigInt
====================================

The JavaScript exception "x can't be converted to BigInt" occurs when attempting to convert a [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
, [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
, or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 value to a [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
, or if an operation expecting a BigInt parameter receives a number.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt#message)

---------------------------------------------------------------------------------------------------------------------

TypeError: Cannot convert null to a BigInt (V8-based)
TypeError: can't convert null to BigInt (Firefox)
TypeError: Invalid argument type in ToBigInt operation (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt#error_type)

---------------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------------------

When using the [`BigInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
 function to convert a value to a BigInt, the value would first be converted to a primitive. Then, if it's not one of BigInt, string, number, and boolean, the error is thrown.

Some operations, like [`BigInt.asIntN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/asIntN)
, require the parameter to be a BigInt. Passing in a number in this case will also throw this error.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Using BigInt() on invalid values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt#using_bigint_on_invalid_values)

**Note:** Simply coercing the value to a string or number using [`String()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/String)
 or [`Number()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number)
 before passing it to `BigInt()` is usually not sufficient to avoid all errors. If the string is not a valid integer number string, a [SyntaxError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_BigInt_syntax)
 is thrown; if the number is not an integer (most notably, [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
), a [RangeError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_be_converted_to_BigInt_because_it_isnt_an_integer)
 is thrown. If the range of input is unknown, properly validate it before using `BigInt()`.

### [Passing a number to a function expecting a BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt#passing_a_number_to_a_function_expecting_a_bigint)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [`BigInt()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Cant_convert_x_to_BigInt/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/cant_convert_x_to_bigint/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/cant_convert_x_to_bigint (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_convert_x_to_BigInt&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_convert_x_to_bigint%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FCant_convert_x_to_BigInt%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fcant_convert_x_to_bigint%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")