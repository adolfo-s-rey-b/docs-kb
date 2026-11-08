*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#mdn-search)
    

Numbers and strings
===================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times)
    

This chapter introduces the two most fundamental data types in JavaScript: numbers and strings. We will introduce their underlying representations, and functions used to work with and perform calculations on them.

[Numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#numbers)

-----------------------------------------------------------------------------------------------------

In JavaScript, numbers are implemented in [double-precision 64-bit binary format IEEE 754](https://en.wikipedia.org/wiki/Double-precision_floating-point_format "External link (opens in new tab)")
 (i.e., a number between ±2^−1022 and ±2^+1023, or about ±10^−308 to ±10^+308, with a numeric precision of 53 bits). Integer values up to ±2^53 − 1 can be represented exactly.

In addition to being able to represent floating-point numbers, the number type has three symbolic values: [`Infinity`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity)
, `-Infinity`, and [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 (not-a-number).

See also [JavaScript data types and structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)
 for context with other primitive types in JavaScript.

You can use four types of number literals: decimal, binary, octal, and hexadecimal.

### [Decimal numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#decimal_numbers)

Decimal literals can start with a zero (`0`) followed by another decimal digit, but if all digits after the leading `0` are smaller than 8, the number is interpreted as an octal number. This is considered a legacy syntax, and number literals prefixed with `0`, whether interpreted as octal or decimal, cause a syntax error in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#legacy_octal_literals)
 — so, use the `0o` prefix instead.

### [Binary numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#binary_numbers)

Binary number syntax uses a leading zero followed by a lowercase or uppercase Latin letter "B" (`0b` or `0B`). If the digits after the `0b` are not 0 or 1, the following [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
 is thrown: "Missing binary digits after 0b".

### [Octal numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#octal_numbers)

The standard syntax for octal numbers is to prefix them with `0o`. For example:

There's also a legacy syntax for octal numbers — by prefixing the octal number with a zero: `0644 === 420` and `"\045" === "%"`. If the digits after the `0` are outside the range 0 through 7, the number will be interpreted as a decimal number.

[Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 forbids this octal syntax.

### [Hexadecimal numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#hexadecimal_numbers)

Hexadecimal number syntax uses a leading zero followed by a lowercase or uppercase Latin letter "X" (`0x` or `0X`). If the digits after 0x are outside the range (0123456789ABCDEF), the following [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
 is thrown: "Identifier starts immediately after numeric literal".

### [Exponentiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#exponentiation)

### [Numeric separators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#numeric_separators)

For all literal syntaxes shown above, an underscore (`_`) can be inserted between digits to improve readability.

See the [lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#numeric_literals)
 reference for more details about number literals.

[Number object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#number_object)

-----------------------------------------------------------------------------------------------------------------

The built-in [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
 object has properties for numerical constants, such as maximum value, not-a-number, and infinity. You cannot change the values of these properties and you use them as follows:

You always refer to a property of the predefined `Number` object as shown above, and not as a property of a `Number` object you create yourself.

The following table summarizes the `Number` object's properties.

| Property | Description |
| --- | --- |
| [`Number.MAX_VALUE`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_VALUE) | The largest positive representable number (`1.7976931348623157e+308`) |
| [`Number.MIN_VALUE`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_VALUE) | The smallest positive representable number (`5e-324`) |
| [`Number.NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN) | Special "not a number" value |
| [`Number.NEGATIVE_INFINITY`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/NEGATIVE_INFINITY) | Special negative infinite value; returned on overflow |
| [`Number.POSITIVE_INFINITY`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/POSITIVE_INFINITY) | Special positive infinite value; returned on overflow |
| [`Number.EPSILON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON) | Difference between `1` and the smallest value greater than `1` that can be represented as a [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)<br> (`2.220446049250313e-16`) |
| [`Number.MIN_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_SAFE_INTEGER) | Minimum safe integer in JavaScript (−2^53 + 1, or `−9007199254740991`) |
| [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER) | Maximum safe integer in JavaScript (+2^53 − 1, or `+9007199254740991`) |

| Method | Description |
| --- | --- |
| [`Number.parseFloat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseFloat) | Parses a string argument and returns a floating point number. Same as the global [`parseFloat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)<br> function. |
| [`Number.parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseInt) | Parses a string argument and returns an integer of the specified radix or base. Same as the global [`parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)<br> function. |
| [`Number.isFinite()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isFinite) | Determines whether the passed value is a finite number. |
| [`Number.isInteger()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isInteger) | Determines whether the passed value is an integer. |
| [`Number.isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN) | Determines whether the passed value is [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)<br>. More robust version of the original global [`isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN)<br>. |
| [`Number.isSafeInteger()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger) | Determines whether the provided value is a number that is a _safe integer_. |

The `Number` prototype provides methods for retrieving information from `Number` objects in various formats. The following table summarizes the methods of `Number.prototype`.

| Method | Description |
| --- | --- |
| [`toExponential()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toExponential) | Returns a string representing the number in exponential notation. |
| [`toFixed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed) | Returns a string representing the number in fixed-point notation. |
| [`toPrecision()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toPrecision) | Returns a string representing the number to a specified precision in fixed-point notation. |

[Math object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#math_object)

-------------------------------------------------------------------------------------------------------------

The built-in [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
 object has properties and methods for mathematical constants and functions. For example, the `Math` object's `PI` property has the value of pi (3.141…), which you would use in an application as

Similarly, standard mathematical functions are methods of `Math`. These include trigonometric, logarithmic, exponential, and other functions. For example, if you want to use the trigonometric function sine, you would write

Note that all trigonometric methods of `Math` take arguments in radians.

The following table summarizes the `Math` object's methods.

|     |     |
| --- | --- |Methods of `Math`
| Method | Description |
| --- | --- |
| [`abs()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/abs) | Absolute value |
| [`sin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sin)<br>, [`cos()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cos)<br>, [`tan()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/tan) | Standard trigonometric functions; with the argument in radians. |
| [`asin()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/asin)<br>, [`acos()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/acos)<br>, [`atan()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan)<br>, [`atan2()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2) | Inverse trigonometric functions; return values in radians. |
| [`sinh()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sinh)<br>, [`cosh()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cosh)<br>, [`tanh()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/tanh) | Hyperbolic functions; argument in hyperbolic angle. |
| [`asinh()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/asinh)<br>, [`acosh()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/acosh)<br>, [`atanh()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atanh) | Inverse hyperbolic functions; return values in hyperbolic angle. |
| [`pow()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/pow)<br>, [`exp()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/exp)<br>, [`expm1()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/expm1)<br>, [`log()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log)<br>, [`log10()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log10)<br>, [`log1p()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p)<br>, [`log2()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log2) | Exponential and logarithmic functions. |
| [`floor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor)<br>, [`ceil()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil) | Returns the largest/smallest integer less/greater than or equal to an argument. |
| [`min()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/min)<br>, [`max()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max) | Returns the minimum or maximum (respectively) value of a comma separated list of numbers as arguments. |
| [`random()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random) | Returns a random number between 0 and 1. |
| [`round()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round)<br>, [`fround()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/fround)<br>, [`trunc()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/trunc)<br>, | Rounding and truncation functions. |
| [`sqrt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sqrt)<br>, [`cbrt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cbrt)<br>, [`hypot()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/hypot) | Square root, cube root, Square root of the sum of square arguments. |
| [`sign()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sign) | The sign of a number, indicating whether the number is positive, negative or zero. |
| [`clz32()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/clz32)<br>,  <br>[`imul()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/imul) | Number of leading zero bits in the 32-bit binary representation.  <br>The result of the C-like 32-bit multiplication of the two arguments. |

Unlike many other objects, you never create a `Math` object of your own. You always use the built-in `Math` object.

[BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#bigints)

-----------------------------------------------------------------------------------------------------

One shortcoming of number values is they only have 64 bits. In practice, due to using IEEE 754 encoding, they cannot represent any integer larger than [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
 (which is 253 - 1) accurately. To solve the need of encoding binary data and to interoperate with other languages that offer wide integers like `i64` (64-bit integers) and `i128` (128-bit integers), JavaScript also offers another data type to represent _arbitrarily large integers_: [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
.

A BigInt can be defined as an integer literal suffixed by `n`:

BigInts can also be constructed from number values or string values using the [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
 constructor.

Conceptually, a BigInt is just an arbitrarily long sequence of bits which encodes an integer. You can safely do any arithmetic operations without losing precision or over-/underflowing.

Compared to numbers, BigInt values yield higher precision when representing large _integers_; however, they cannot represent _floating-point numbers_. For example, division would round to zero:

`Math` functions cannot be used on BigInt values; they only work with numbers.

Choosing between BigInt and number depends on your use-case and your input's range. The precision of numbers should be able to accommodate most day-to-day tasks already, and BigInts are most suitable for handling binary data.

Read more about what you can do with BigInt values in the [Expressions and Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#bigint_operators)
 section, or the [BigInt reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
.

[Strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#strings)

-----------------------------------------------------------------------------------------------------

JavaScript's [String](https://developer.mozilla.org/en-US/docs/Glossary/String)
 type is used to represent textual data. It is a set of "elements" of 16-bit unsigned integer values (UTF-16 code units). Each element in the String occupies a position in the String. The first element is at index 0, the next at index 1, and so on. The length of a String is the number of elements in it. You can create strings using string literals or string objects.

### [String literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#string_literals)

You can declare strings in source code using either single or double quotes:

Within a string literal, most characters can be entered literally. The only exceptions are the backslash (`\`, which starts an escape sequence), the quote character being used to enclose the string, which terminates the string, and the newline character, which is a syntax error if not preceded by a backslash.

More advanced strings can be created using escape sequences:

#### Hexadecimal escape sequences

The number after \\x is interpreted as a [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal "External link (opens in new tab)")
 number.

#### Unicode escape sequences

The Unicode escape sequences require at least four hexadecimal digits following `\u`.

#### Unicode code point escapes

With Unicode code point escapes, any character can be escaped using hexadecimal numbers so that it is possible to use Unicode code points up to `0x10FFFF`. With the four-digit Unicode escapes it is often necessary to write the surrogate halves separately to achieve the same result.

See also [`String.fromCodePoint()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCodePoint)
 or [`String.prototype.codePointAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/codePointAt)
.

[String object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#string_object)

-----------------------------------------------------------------------------------------------------------------

You can call methods directly on a string value:

The following methods are available on [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values:

*   Query: get the character or character code at a particular string index. Methods include [`at()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/at)
    , [`charAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)
    , [`charCodeAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt)
    , and [`codePointAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/codePointAt)
    .
*   Search: get information about a substring that conforms to a pattern, or test if a particular substring exists. Methods include [`indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf)
    , [`lastIndexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/lastIndexOf)
    , [`startsWith()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith)
    , [`endsWith()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith)
    , [`includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)
    , [`match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
    , [`matchAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)
    , and [`search()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search)
    
*   Composition: combine strings into a longer string. Methods include [`padStart()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padStart)
    , [`padEnd()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padEnd)
    , [`concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/concat)
    , and [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/repeat)
    .
*   Decomposition: break a string into smaller strings. Methods include [`split()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
    , [`slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
    , [`substring()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring)
    , [`substr()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)
    , [`trim()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim)
    , [`trimStart()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trimStart)
    , and [`trimEnd()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trimEnd)
    .
*   Transformation: return a new string based on the current string's content. Methods include [`toLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
    , [`toUpperCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)
    , [`toLocaleLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleLowerCase)
    , [`toLocaleUpperCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase)
    , [`normalize()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize)
    , and [`toWellFormed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toWellFormed)
    .

When working with strings, there are two other objects that provide important functionality for string manipulation: [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 and [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
. They are introduced in [regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
 and [internationalization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Internationalization)
 respectively.

[Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#template_literals)

-------------------------------------------------------------------------------------------------------------------------

[Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
 are string literals allowing embedded expressions. You can use multi-line strings and string interpolation features with them.

Template literals are enclosed by backtick ([grave accent](https://en.wikipedia.org/wiki/Grave_accent "External link (opens in new tab)")
) characters (`` ` ``) instead of double or single quotes. Template literals can contain placeholders. These are indicated by the dollar sign and curly braces (`${expression}`).

### [Multi-lines](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#multi-lines)

Any new line characters inserted in the source are part of the template literal. Using normal strings, you would have to use the following syntax in order to get multi-line strings:

To get the same effect with multi-line strings, you can now write:

### [Embedded expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings#embedded_expressions)

In order to embed expressions within normal strings, you would use the following syntax:

Now, with template literals, you are able to make use of the syntactic sugar making substitutions like this more readable:

For more information, read about [Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
 in the [JavaScript reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
.

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 26, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/numbers_and_strings/index.md?plain=1 "Folder: en-us/web/javascript/guide/numbers_and_strings (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FNumbers_and_strings&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fnumbers_and_strings%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FNumbers_and_strings%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fnumbers_and_strings%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F82617295992be4d9dc4ca74499ee63f8d2e5984b%0A*+Document+last+modified%3A+2025-08-26T12%3A41%3A57.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")