*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#mdn-search)
    

Exponentiation (\*\*)
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **exponentiation (`**`)** operator returns the result of raising the first operand to the power of the second operand. It is equivalent to [`Math.pow()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/pow)
, except it also accepts [BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 as operands.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#try_it)

------------------------------------------------------------------------------------------------------------

    console.log(3 ** 4);
    // Expected output: 81
    
    console.log(10 ** -2);
    // Expected output: 0.01
    
    console.log(2 ** (3 ** 2));
    // Expected output: 512
    
    console.log((2 ** 3) ** 2);
    // Expected output: 64
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#syntax)

------------------------------------------------------------------------------------------------------------

js

    x ** y
    

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#description)

----------------------------------------------------------------------------------------------------------------------

The `**` operator is overloaded for two types of operands: number and [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
. It first [coerces both operands to numeric values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#numeric_coercion)
 and tests the types of them. It performs BigInt exponentiation if both operands become BigInts; otherwise, it performs number exponentiation. A [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 is thrown if one operand becomes a BigInt but the other becomes a number.

For both numbers and BigInts, `0` raised to a positive power returns `0`, and `0` raised to a power of `0` returns `1`. For numbers, `0` raised to a negative number returns `Infinity`, while `-0` raised to a negative number returns `-Infinity`.

`NaN ** 0` (and the equivalent `Math.pow(NaN, 0)`) is the only case where [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 doesn't propagate through mathematical operations — it returns `1` despite the operand being `NaN`. In addition, the behavior where `base` is 1 and `exponent` is non-finite (±Infinity or `NaN`) is different from IEEE 754, which specifies that the result should be 1, whereas JavaScript returns `NaN` to preserve backward compatibility with its original behavior.

For BigInt exponentiation, a [`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
 is thrown if the exponent `y` is negative. This is because any negative exponent would likely result in a value between 0 and 1 (unless the base is `1`, `-1`, or `0`), which is rounded to zero, and is likely a developer mistake.

The exponentiation operator is [right-associative](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
: `a ** b ** c` is equal to `a ** (b ** c)`.

In most languages, such as PHP, Python, and others that have an exponentiation operator (`**`), the exponentiation operator is defined to have a higher precedence than unary operators, such as unary `+` and unary `-`, but there are a few exceptions. For example, in Bash, the `**` operator is defined to have a lower precedence than unary operators.

In JavaScript, it is impossible to write an ambiguous exponentiation expression. That is, you cannot put a unary operator (with [precedence 14](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#table)
, including `+`/`-`/`~`/`!`/`++`/`--`/`delete`/`void`/`typeof`/`await`) immediately before the base number; [doing so will cause a SyntaxError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation)
.

For example, `-2 ** 2` is 4 in Bash, but is -4 in other languages (such as Python). This is invalid in JavaScript, as the operation is ambiguous. You have to parenthesize either side — for example, as `-(2 ** 2)` — to make the intention unambiguous.

Note that some programming languages use the caret symbol `^` for exponentiation, but JavaScript uses that symbol for the [bitwise XOR operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#examples)

----------------------------------------------------------------------------------------------------------------

### [Exponentiation using numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#exponentiation_using_numbers)

js

    2 ** 3; // 8
    3 ** 2; // 9
    3 ** 2.5; // 15.588457268119896
    10 ** -1; // 0.1
    2 ** 1024; // Infinity
    NaN ** 2; // NaN
    NaN ** 0; // 1
    1 ** Infinity; // NaN
    

Other non-BigInt values are coerced to numbers:

js

    2 ** "3"; // 8
    2 ** "hello"; // NaN
    

### [Exponentiation using BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#exponentiation_using_bigints)

js

    2n ** 3n; // 8n
    2n ** 1024n; // A very large number, but not Infinity
    

You cannot mix BigInt and number operands in exponentiation.

js

    2n ** 2; // TypeError: Cannot mix BigInt and other types, use explicit conversions
    2 ** 2n; // TypeError: Cannot mix BigInt and other types, use explicit conversions
    

To do exponentiation with a BigInt and a non-BigInt, convert either operand:

js

    2n ** BigInt(2); // 4n
    Number(2n) ** 2; // 4
    

### [Associativity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#associativity)

js

    2 ** 3 ** 2; // 512
    2 ** (3 ** 2); // 512
    (2 ** 3) ** 2; // 64
    

### [Usage with unary operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#usage_with_unary_operators)

To invert the sign of the result of an exponentiation expression:

js

    -(2 ** 2); // -4
    

To force the base of an exponentiation expression to be a negative number:

js

    (-2) ** 2; // 4
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-exp-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-exp-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Addition (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
    
*   [Subtraction (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction)
    
*   [Division (`/`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division)
    
*   [Multiplication (`*`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)
    
*   [Remainder (`%`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)
    
*   [Increment (`++`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
    
*   [Decrement (`--`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)
    
*   [Unary negation (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)
    
*   [Unary plus (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/exponentiation/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/exponentiation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FExponentiation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fexponentiation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FExponentiation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fexponentiation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")