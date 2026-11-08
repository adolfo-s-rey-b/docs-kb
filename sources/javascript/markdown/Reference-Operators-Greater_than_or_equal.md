*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#mdn-search)
    

Greater than or equal (>=)
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **greater than or equal (`>=`)** operator returns `true` if the left operand is greater than or equal to the right operand, and `false` otherwise.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#try_it)

-------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#syntax)

-------------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#description)

-----------------------------------------------------------------------------------------------------------------------------

The operands are compared using the same algorithm as the [Less than](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than)
 operator, with the result negated. `x >= y` is generally equivalent to `!(x < y)`, except for two cases where `x >= y` and `x < y` are both `false`:

*   If one of the operands gets converted to a BigInt, while the other gets converted to a string that cannot be converted to a BigInt value (it throws a [syntax error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_BigInt_syntax)
     when passed to [`BigInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
    ).
*   If one of the operands gets converted to `NaN`. (For example, strings that cannot be converted to numbers, or `undefined`.)

`x >= y` is generally equivalent to `x > y || x == y`, except for a few cases:

*   When one of `x` or `y` is `null`, and the other is something that's not `null` and becomes 0 when [coerced to numeric](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#numeric_coercion)
     (including `0`, `0n`, `false`, `""`, `"0"`, `new Date(0)`, etc.): `x >= y` is `true`, while `x > y || x == y` is `false`.
*   When one of `x` or `y` is `undefined`, and the other is one of `null` or `undefined`: `x >= y` is `false`, while `x == y` is `true`.
*   When `x` and `y` are the same object that becomes `NaN` after the first step of [Less than](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than)
     (such as `new Date(NaN)`): `x >= y` is `false`, while `x == y` is `true`.
*   When `x` and `y` are different objects that become the same value after the first step of [Less than](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than)
    : `x >= y` is `true`, while `x > y || x == y` is `false`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#examples)

-----------------------------------------------------------------------------------------------------------------------

### [String to string comparison](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#string_to_string_comparison)

### [String to number comparison](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#string_to_number_comparison)

### [Number to Number comparison](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#number_to_number_comparison)

### [Number to BigInt comparison](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#number_to_bigint_comparison)

### [Comparing Boolean, null, undefined, NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#comparing_boolean_null_undefined_nan)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-relational-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-relational-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [Greater than (`>`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than)
    
*   [Less than (`<`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than)
    
*   [Less than or equal (`<=`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than_or_equal)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/greater_than_or_equal/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/greater_than_or_equal (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FGreater_than_or_equal&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fgreater_than_or_equal%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FGreater_than_or_equal%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fgreater_than_or_equal%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")