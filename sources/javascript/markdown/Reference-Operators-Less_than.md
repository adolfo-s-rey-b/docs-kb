*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#mdn-search)
    

Less than (<)
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **less than (`<`)** operator returns `true` if the left operand is less than the right operand, and `false` otherwise.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#syntax)

-------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#description)

-----------------------------------------------------------------------------------------------------------------

The operands are compared with multiple rounds of coercion, which can be summarized as follows:

*   First, objects are [converted to primitives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
     by calling its [`[Symbol.toPrimitive]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive)
     (with `"number"` as hint), [`valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
    , and [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
     methods, in that order. The left operand is always coerced before the right one. Note that although `[Symbol.toPrimitive]()` is called with the `"number"` hint (meaning there's a slight preference for the object to become a number), the return value is not [converted to a number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
    , since strings are still specially handled.
*   If both values are strings, they are compared as strings, based on the values of the UTF-16 code units (not Unicode code points) they contain.
*   Otherwise JavaScript attempts to convert non-numeric types to numeric values:
    *   Boolean values `true` and `false` are converted to 1 and 0 respectively.
    *   `null` is converted to 0.
    *   `undefined` is converted to `NaN`.
    *   Strings are converted based on the values they contain, and are converted as `NaN` if they do not contain numeric values.
*   If either value is [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
    , the operator returns `false`.
*   Otherwise the values are compared as numeric values. BigInt and number values can be compared together.

Other operators, including [`>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than)
, [`>=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal)
, and [`<=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than_or_equal)
, use the same algorithm as `<`. There are two cases where all four operators return `false`:

*   If one of the operands gets converted to a BigInt, while the other gets converted to a string that cannot be converted to a BigInt value (it throws a [syntax error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_BigInt_syntax)
     when passed to [`BigInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
    ).
*   If one of the operands gets converted to `NaN`. (For example, strings that cannot be converted to numbers, or `undefined`.)

For all other cases, the four operators have the following relationships:

**Note:** One observable difference between `<` and `>` is the order of coercion, especially if the coercion to primitive has side effects. All comparison operators coerce the left operand before the right operand.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#examples)

-----------------------------------------------------------------------------------------------------------

### [String to string comparison](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#string_to_string_comparison)

### [String to number comparison](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#string_to_number_comparison)

### [Number to Number comparison](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#number_to_number_comparison)

### [Number to BigInt comparison](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#number_to_bigint_comparison)

### [Comparing Boolean, null, undefined, NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#comparing_boolean_null_undefined_nan)

### [Comparison with side effects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#comparison_with_side_effects)

Comparisons always coerce their operands to primitives. This means the same object may end up having different values within one comparison expression. For example, you may have two values that are both greater than and less than the other.

**Warning:** This can be a source of confusion. If your objects provide custom primitive conversion logic, make sure it is _idempotent_: multiple coercions should return the same value.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-relational-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-relational-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Greater than (`>`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than)
    
*   [Greater than or equal (`>=`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal)
    
*   [Less than or equal (`<=`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than_or_equal)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/less_than/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/less_than (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLess_than&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fless_than%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLess_than%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fless_than%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")