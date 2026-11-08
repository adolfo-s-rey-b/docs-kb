*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#mdn-search)
    

Equality (==)
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **equality (`==`)** operator checks whether its two operands are equal, returning a Boolean result. Unlike the [strict equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)
 operator, it attempts to convert and compare operands that are of different types.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#try_it)

------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#syntax)

------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#description)

----------------------------------------------------------------------------------------------------------------

The equality operators (`==` and `!=`) provide the [IsLooselyEqual](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness#loose_equality_using)
 semantic. This can be roughly summarized as follows:

1.  If the operands have the same type, they are compared as follows:
    *   Object: return `true` only if both operands reference the same object.
    *   String: return `true` only if both operands have the same characters in the same order.
    *   Number: return `true` only if both operands have the same value. `+0` and `-0` are treated as the same value. If either operand is `NaN`, return `false`; so, `NaN` is never equal to `NaN`.
    *   Boolean: return `true` only if operands are both `true` or both `false`.
    *   BigInt: return `true` only if both operands have the same value.
    *   Symbol: return `true` only if both operands reference the same symbol.
2.  If one of the operands is `null` or `undefined`, the other must also be `null` or `undefined` to return `true`. Otherwise return `false`.
3.  If one of the operands is an object and the other is a primitive, [convert the object to a primitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
    .
4.  At this step, both operands are converted to primitives (one of String, Number, Boolean, Symbol, and BigInt). The rest of the conversion is done case-by-case.
    *   If they are of the same type, compare them using step 1.
    *   If one of the operands is a Symbol but the other is not, return `false`.
    *   If one of the operands is a Boolean but the other is not, [convert the boolean to a number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
        : `true` is converted to 1, and `false` is converted to 0. Then compare the two operands loosely again.
    *   Number to String: [convert the string to a number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
        . Conversion failure results in `NaN`, which will guarantee the equality to be `false`.
    *   Number to BigInt: compare by their mathematical value. If the number is ±Infinity or `NaN`, return `false`.
    *   String to BigInt: convert the string to a BigInt using the same algorithm as the [`BigInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
         constructor. If conversion fails, return `false`.

Loose equality is _symmetric_: `A == B` always has identical semantics to `B == A` for any values of `A` and `B` (except for the order of applied conversions).

The most notable difference between this operator and the [strict equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)
 (`===`) operator is that the strict equality operator does not attempt type conversion. Instead, the strict equality operator always considers operands of different types to be different. The strict equality operator essentially carries out only step 1, and then returns `false` for all other cases.

There's a "willful violation" of the above algorithm: if one of the operands is [`document.all`](https://developer.mozilla.org/en-US/docs/Web/API/Document/all)
, it is treated as if it's `undefined`. This means that `document.all == null` is `true`, but `document.all === undefined || document.all === null` is `false`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#examples)

----------------------------------------------------------------------------------------------------------

### [Comparison with no type conversion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#comparison_with_no_type_conversion)

### [Comparison with type conversion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#comparison_with_type_conversion)

### [Comparison of objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#comparison_of_objects)

### [Comparing strings and String objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#comparing_strings_and_string_objects)

Note that strings constructed using `new String()` are objects. If you compare one of these with a string literal, the `String` object will be converted to a string literal and the contents will be compared. However, if both operands are `String` objects, then they are compared as objects and must reference the same object for comparison to succeed:

### [Comparing Dates and strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#comparing_dates_and_strings)

### [Comparing arrays and strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#comparing_arrays_and_strings)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-equality-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-equality-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#see_also)

----------------------------------------------------------------------------------------------------------

*   [Inequality (`!=`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality)
    
*   [Strict equality (`===`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)
    
*   [Strict inequality (`!==`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/equality/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/equality (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FEquality&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fequality%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FEquality%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fequality%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1133f9e054bad2340b98a608b7894fd7daa62af6%0A*+Document+last+modified%3A+2026-05-11T22%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")