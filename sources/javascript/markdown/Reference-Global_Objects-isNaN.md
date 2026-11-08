*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#mdn-search)
    

isNaN()
=======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`isNaN()`** function determines whether a value is [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
, first converting the value to a number if necessary. Because coercion inside the `isNaN()` function can be [surprising](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#description)
, you may prefer to use [`Number.isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#try_it)

--------------------------------------------------------------------------------------------------------

    function milliseconds(x) {
      if (isNaN(x)) {
        return "Not a Number!";
      }
      return x * 1000;
    }
    
    console.log(milliseconds("100F"));
    // Expected output: "Not a Number!"
    
    console.log(milliseconds("0.0314E+2"));
    // Expected output: 3140
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#syntax)

--------------------------------------------------------------------------------------------------------

js

    isNaN(value)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#parameters)

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#value)

The value to be tested.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#return_value)

`true` if the given value is [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 after being [coerced to a number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#description)

------------------------------------------------------------------------------------------------------------------

`isNaN()` is a function property of the global object.

For number values, `isNaN()` tests if the number is the value [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
. When the argument to the `isNaN()` function is not of type [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#number_type)
, the value is first [coerced to a number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
, and the resulting value is then compared against [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
.

This behavior of `isNaN()` for non-numeric arguments can be confusing! For example:

*   [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#null_type)
     is coerced to 0
*   an empty string is coerced to 0
*   a boolean is coerced to 0 or 1

These values are intuitively "not numbers", but they don't evaluate to `NaN`, so `isNaN()` returns `false`. Therefore, `isNaN()` answers neither the question "is the input the floating point [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 value" nor the question "is the input not a number".

[`Number.isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
 is a more reliable way to test whether a value is the number value `NaN` or not. Alternatively, the expression `x !== x` can be used, and neither of the solutions is subject to the false positives that make the global `isNaN()` unreliable. To test if a value is a number, use [`typeof x === "number"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
.

The `isNaN()` function answers the question "is the input functionally equivalent to [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 when used in a number context". If `isNaN(x)` returns `false`, you can use `x` in an arithmetic expression as if it's a valid number that's not `NaN`. If `isNaN(x)` returns `true`, `x` will get coerced to `NaN` and make most arithmetic expressions return `NaN` (because `NaN` propagates). You can use this, for example, to test whether an argument to a function is arithmetically processable (usable "like" a number), and handle values that are not number-like by throwing an error, providing a default value, etc. This way, you can have a function that makes use of the full versatility JavaScript provides by implicitly converting values depending on context.

**Note:** The [`+` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
 performs both number addition and string concatenation. Therefore, even if `isNaN()` returns `false` for both operands, the `+` operator may still return a string, because it's not used as an arithmetic operator. For example, `isNaN("1")` returns `false`, but `"1" + 1` returns `"11"`. To be sure that you are working with numbers, [coerce the value to a number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
 and use [`Number.isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
 to test the result.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#examples)

------------------------------------------------------------------------------------------------------------

Note how `isNaN()` returns `true` for values that are not the value `NaN` but are not numbers either:

js

    isNaN(NaN); // true
    isNaN(undefined); // true
    isNaN({}); // true
    
    isNaN(true); // false
    isNaN(null); // false
    isNaN(37); // false
    
    // Strings
    isNaN("37"); // false: "37" is converted to the number 37 which is not NaN
    isNaN("37.37"); // false: "37.37" is converted to the number 37.37 which is not NaN
    isNaN("37,5"); // true
    isNaN("123ABC"); // true: Number("123ABC") is NaN
    isNaN(""); // false: the empty string is converted to 0 which is not NaN
    isNaN(" "); // false: a string with spaces is converted to 0 which is not NaN
    
    // Dates
    isNaN(new Date()); // false; Date objects can be converted to a number (timestamp)
    isNaN(new Date().toString()); // true; the string representation of a Date object cannot be parsed as a number
    
    // Arrays
    isNaN([]); // false; the primitive representation is "", which converts to the number 0
    isNaN([1]); // false; the primitive representation is "1"
    isNaN([1, 2]); // true; the primitive representation is "1,2", which cannot be parsed as number
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-isnan-number](https://tc39.es/ecma262/multipage/global-object.html#sec-isnan-number) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#see_also)

------------------------------------------------------------------------------------------------------------

*   [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
    
*   [`Number.isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/isnan/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/isnan (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FisNaN&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fisnan%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FisNaN%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fisnan%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F52aca3c51ce0ff04036a13d4db471c9844d07b00%0A*+Document+last+modified%3A+2026-10-27T22%3A06%3A33.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")