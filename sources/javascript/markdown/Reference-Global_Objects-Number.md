*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#mdn-search)
    

Number
======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**`Number`** values represent floating-point numbers like `37` or `-9.25`.

The `Number` constructor contains constants and methods for working with numbers. Values of other types can be converted to numbers using the `Number()` function.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#description)

-------------------------------------------------------------------------------------------------------------------

Numbers are most commonly expressed in literal forms like `255` or `3.14159`. The [lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#numeric_literals)
 contains a more detailed reference.

A number literal like `37` in JavaScript code is a floating-point value, not an integer. There is no separate integer type in common everyday use. (JavaScript also has a [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 type, but it's not designed to replace Number for everyday uses. `37` is still a number, not a BigInt.)

When used as a function, `Number(value)` converts a string or other value to the Number type. If the value can't be converted, it returns [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
.

### [Number encoding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_encoding)

The JavaScript `Number` type is a [double-precision 64-bit binary format IEEE 754](https://en.wikipedia.org/wiki/Double_precision_floating-point_format "External link (opens in new tab)")
 value, like `double` in Java or C#. This means it can represent fractional values, but there are some limits to the stored number's magnitude and precision. Very briefly, an IEEE 754 double-precision number uses 64 bits to represent 3 parts:

*   1 bit for the _sign_ (positive or negative)
*   11 bits for the _exponent_ (-1022 to 1023)
*   52 bits for the _mantissa_ (representing a number between 0 and 1)

The mantissa (also called _significand_) is the part of the number representing the actual value (significant digits). The exponent is the power of 2 that the mantissa should be multiplied by. Thinking about it as scientific notation:

Number\=(−1)sign⋅(1+mantissa)⋅2exponent\\text{Number} = ({-1})^{\\text{sign}} \\cdot (1 + \\text{mantissa}) \\cdot 2^{\\text{exponent}}

The mantissa is stored with 52 bits, interpreted as digits after `1.…` in a binary fractional number. Therefore, the mantissa's precision is 2\-52 (obtainable via [`Number.EPSILON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON)
), or about 15 to 17 significant decimal digits; arithmetic above that level of precision is subject to [rounding](https://en.wikipedia.org/wiki/Floating-point_arithmetic#Representable_numbers,_conversion_and_rounding "External link (opens in new tab)")
.

The largest value a number can hold is 21023 × (2 - 2\-52) (with the exponent being 1023 and the mantissa being 0.1111… in base 2), which is obtainable via [`Number.MAX_VALUE`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_VALUE)
. Values higher than that are replaced with the special number constant [`Infinity`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity)
.

Integers can only be represented without loss of precision in the range -253 + 1 to 253 - 1, inclusive (obtainable via [`Number.MIN_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_SAFE_INTEGER)
 and [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
), because the mantissa can only hold 53 bits (including the leading 1).

More details on this are described in the [ECMAScript standard](https://tc39.es/ecma262/multipage/ecmascript-data-types-and-values.html#sec-ecmascript-language-types-number-type "External link (opens in new tab)")
.

### [Number coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)

Many built-in operations that expect numbers first coerce their arguments to numbers (which is largely why `Number` objects behave similarly to number primitives). [The operation](https://tc39.es/ecma262/multipage/abstract-operations.html#sec-tonumber "External link (opens in new tab)")
 can be summarized as follows:

*   Numbers are returned as-is.
*   [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
     turns into [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
    .
*   [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
     turns into `0`.
*   `true` turns into `1`; `false` turns into `0`.
*   Strings are converted by parsing them as if they contain a [number literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#numeric_literals)
    . Parsing failure results in `NaN`. There are some minor differences compared to an actual number literal:
    *   Leading and trailing whitespace/line terminators are ignored.
    *   A leading `0` digit does not cause the number to become an octal literal (or get rejected in strict mode).
    *   `+` and `-` are allowed at the start of the string to indicate its sign. (In actual code, they "look like" part of the literal, but are actually separate unary operators.) However, the sign can only appear once, and must not be followed by whitespace.
    *   `Infinity` and `-Infinity` are recognized as literals. In actual code, they are global variables.
    *   Empty or whitespace-only strings are converted to `0`.
    *   [Numeric separators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#numeric_separators)
         are not allowed.
*   [BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
     throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
     to prevent unintended implicit coercion causing loss of precision.
*   [Symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
     throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
    .
*   Objects are first [converted to a primitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
     by calling their [`[Symbol.toPrimitive]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive)
     (with `"number"` as hint), `valueOf()`, and `toString()` methods, in that order. The resulting primitive is then converted to a number.

There are two ways to achieve nearly the same effect in JavaScript.

*   [Unary plus](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
    : `+x` does exactly the number coercion steps explained above to convert `x`.
*   The [`Number()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number)
     function: `Number(x)` uses the same algorithm to convert `x`, except that [BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
     don't throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
    , but return their number value, with possible loss of precision.

[`Number.parseFloat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseFloat)
 and [`Number.parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseInt)
 are similar to `Number()` but only convert strings, and have slightly different parsing rules. For example, `parseInt()` doesn't recognize the decimal point, and `parseFloat()` doesn't recognize the `0x` prefix.

#### Integer conversion

Some operations expect integers, most notably those that work with array/string indices, date/time components, and number radixes. After performing the number coercion steps above, the result is [truncated](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/trunc)
 to an integer (by discarding the fractional part). If the number is ±Infinity, it's returned as-is. If the number is `NaN` or `-0`, it's returned as `0`. The result is therefore always an integer (which is not `-0`) or ±Infinity.

Notably, when converted to integers, both `undefined` and `null` become `0`, because `undefined` is converted to `NaN`, which also becomes `0`.

#### Fixed-width number conversion

JavaScript has some lower-level functions that deal with the binary encoding of integer numbers, most notably [bitwise operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#bitwise_shift_operators)
 and [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
 objects. Bitwise operators always convert the operands to 32-bit integers. In these cases, after converting the value to a number, the number is then normalized to the given width by first [truncating](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/trunc)
 the fractional part and then taking the lowest bits in the integer's two's complement encoding.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#constructor)

-------------------------------------------------------------------------------------------------------------------

[`Number()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number)

Creates `Number` objects. When called as a function, it returns primitive values of type Number.

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#static_properties)

-------------------------------------------------------------------------------------------------------------------------------

[`Number.EPSILON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON)

The smallest interval between two representable numbers.

[`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)

The maximum safe integer in JavaScript (253 - 1).

[`Number.MAX_VALUE`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_VALUE)

The largest positive representable number.

[`Number.MIN_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_SAFE_INTEGER)

The minimum safe integer in JavaScript (-(253 - 1)).

[`Number.MIN_VALUE`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_VALUE)

The smallest positive representable number—that is, the positive number closest to zero (without actually being zero).

[`Number.NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN)

Special "**N**ot **a** **N**umber" value.

[`Number.NEGATIVE_INFINITY`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/NEGATIVE_INFINITY)

Special value representing negative infinity. Returned on overflow.

[`Number.POSITIVE_INFINITY`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/POSITIVE_INFINITY)

Special value representing infinity. Returned on overflow.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#static_methods)

-------------------------------------------------------------------------------------------------------------------------

[`Number.isFinite()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isFinite)

Determine whether the passed value is a finite number.

[`Number.isInteger()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isInteger)

Determine whether the passed value is an integer.

[`Number.isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)

Determine whether the passed value is `NaN`.

[`Number.isSafeInteger()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger)

Determine whether the passed value is a safe integer (number between -(253 - 1) and 253 - 1).

[`Number.parseFloat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseFloat)

This is the same as the global [`parseFloat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)
 function.

[`Number.parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseInt)

This is the same as the global [`parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
 function.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#instance_properties)

-----------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Number.prototype` and shared by all `Number` instances.

[`Number.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Number` instances, the initial value is the [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number)
 constructor.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#instance_methods)

-----------------------------------------------------------------------------------------------------------------------------

[`Number.prototype.toExponential()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toExponential)

Returns a string representing the number in exponential notation.

[`Number.prototype.toFixed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)

Returns a string representing the number in fixed-point notation.

[`Number.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toLocaleString)

Returns a string with a language sensitive representation of this number. Overrides the [`Object.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toLocaleString)
 method.

[`Number.prototype.toPrecision()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toPrecision)

Returns a string representing the number to a specified precision in fixed-point or exponential notation.

[`Number.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString)

Returns a string representing the specified object in the specified _radix_ ("base"). Overrides the [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 method.

[`Number.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/valueOf)

Returns the primitive value of the specified object. Overrides the [`Object.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
 method.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#examples)

-------------------------------------------------------------------------------------------------------------

### [Using the Number object to assign values to numeric variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#using_the_number_object_to_assign_values_to_numeric_variables)

The following example uses the `Number` object's properties to assign values to several numeric variables:

### [Integer range for Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#integer_range_for_number)

The following example shows the minimum and maximum integer values that can be represented as `Number` object.

When parsing data that has been serialized to JSON, integer values falling outside of this range can be expected to become corrupted when JSON parser coerces them to `Number` type.

A possible workaround is to use [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 instead.

Larger numbers can be represented using the [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 type.

### [Using Number() to convert a Date object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#using_number_to_convert_a_date_object)

The following example converts the [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
 object to a numerical value using `Number` as a function:

This logs `819199440000`.

### [Convert numeric strings and null to numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#convert_numeric_strings_and_null_to_numbers)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-number-objects](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-number-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Polyfill of modern `Number` behavior (with support binary and octal literals) in `core-js`](https://core-js.io/docs/features/ecmascript/number "External link (opens in new tab)")
    
*   [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
    
*   [Arithmetic operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#arithmetic_operators)
    
*   [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
    
*   [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/number/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/number (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FNumber&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fnumber%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FNumber%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fnumber%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")