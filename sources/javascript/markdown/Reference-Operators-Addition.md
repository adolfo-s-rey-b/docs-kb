*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#mdn-search)
    

Addition (+)
============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **addition (`+`)** operator produces the sum of numeric operands or string concatenation.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#try_it)

------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#syntax)

------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#description)

----------------------------------------------------------------------------------------------------------------

The `+` operator is overloaded for two distinct operations: numeric addition and string concatenation. When evaluating, it first [coerces both operands to primitives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
. Then, the two operands' types are tested:

*   If one side is a string, the other operand is also [converted to a string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
     and they are concatenated.
*   If they are both [BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
    , BigInt addition is performed. If one side is a BigInt but the other is not, a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
     is thrown.
*   Otherwise, both sides are [converted to numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
    , and numeric addition is performed.

String concatenation is often thought to be equivalent with [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
 or [`String.prototype.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/concat)
, but they are not. Addition coerces the expression to a _primitive_, which calls [`valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
 in priority; on the other hand, template literals and `concat()` coerce the expression to a _string_, which calls [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 in priority. If the expression has a [`[Symbol.toPrimitive]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive)
 method, string concatenation calls it with `"default"` as hint, while template literals use `"string"`. This is important for objects that have different string and primitive representations — such as [`Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)
, whose objects' `valueOf()` methods all throw.

You are advised to not use `"" + x` to perform [string coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#examples)

----------------------------------------------------------------------------------------------------------

### [Addition using numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#addition_using_numbers)

Other non-string, non-BigInt values are coerced to numbers:

### [Addition using BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#addition_using_bigints)

You cannot mix BigInt and number operands in addition. `null`, `undefined`, and boolean values are coerced to numbers and are forbidden as well.

Strings have priority over other types, so adding a string to a BigInt produces string concatenation rather than a `TypeError`.

To do addition with a BigInt and a non-BigInt, convert either operand:

### [Addition using strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#addition_using_strings)

If one of the operands is a string, the other is converted to a string and they are concatenated:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-addition-operator-plus](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-addition-operator-plus) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition#see_also)

----------------------------------------------------------------------------------------------------------

*   [Subtraction (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction)
    
*   [Division (`/`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division)
    
*   [Multiplication (`*`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)
    
*   [Remainder (`%`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)
    
*   [Exponentiation (`**`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
    
*   [Increment (`++`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
    
*   [Decrement (`--`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)
    
*   [Unary negation (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)
    
*   [Unary plus (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/addition/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/addition (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FAddition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Faddition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FAddition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Faddition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1133f9e054bad2340b98a608b7894fd7daa62af6%0A*+Document+last+modified%3A+2026-05-11T22%3A00%3A03.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")