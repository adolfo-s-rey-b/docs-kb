*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#mdn-search)
    

BigInt
======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**`BigInt`** values represent integer values which are [too high](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
 or [too low](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_SAFE_INTEGER)
 to be represented by the `number` [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#description)

-------------------------------------------------------------------------------------------------------------------

A **BigInt value**, also sometimes just called a **BigInt**, is a `bigint` [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
, created by appending `n` to the end of an integer literal, or by calling the [`BigInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
 function (without the `new` operator) and giving it an integer value or string value.

BigInt values are similar to Number values in some ways, but also differ in a few key matters: A BigInt value cannot be used with methods in the built-in [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
 object and cannot be mixed with a Number value in operations; they must be coerced to the same type. Be careful coercing values back and forth, however, as the precision of a BigInt value may be lost when it is coerced to a Number value.

### [Type information](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#type_information)

When tested against `typeof`, a BigInt value (`bigint` primitive) will give `"bigint"`:

A BigInt value can also be wrapped in an `Object`:

### [Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#operators)

Most operators support BigInts, however most do not permit operands to be of mixed types — both operands must be BigInt or neither:

*   [Arithmetic operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#arithmetic_operators)
    : `+`, `-`, `*`, `/`, `%`, `**`
*   [Bitwise operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#bitwise_shift_operators)
    : `>>`, `<<`, `&`, `|`, `^`, `~`
*   [Unary negation (`-`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)
    
*   [Increment/decrement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#increment_and_decrement)
    : `++`, `--`

The boolean-returning operators allow mixing numbers and BigInts as operands:

*   [Relational operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#relational_operators)
     and [equality operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#equality_operators)
    : `>`, `<`, `>=`, `<=`, `==`, `!=`, `===`, `!==`
*   [Logical operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#binary_logical_operators)
     only rely on the [truthiness](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
     of operands

A couple of operators do not support BigInt at all:

*   [Unary plus (`+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)
     cannot be supported due to conflicting usage in asm.js, so it has been left out [in order to not break asm.js](https://github.com/tc39/proposal-bigint/blob/master/ADVANCED.md#dont-break-asmjs "External link (opens in new tab)")
    .
*   [Unsigned right shift (`>>>`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift)
     is the only bitwise operator that's unsupported, as every BigInt value is signed.

Special cases:

*   Addition (`+`) involving a string and a BigInt returns a string.
*   Division (`/`) truncates fractional components towards zero, since BigInt is unable to represent fractional quantities.

### [Comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#comparisons)

A BigInt value is not strictly equal to a Number value, but it _is_ loosely so:

A Number value and a BigInt value may be compared as usual:

BigInt values and Number values may be mixed in arrays and sorted:

Note that comparisons with `Object`\-wrapped BigInt values act as with other objects, only indicating equality when the same object instance is compared:

Because coercing between Number values and BigInt values can lead to loss of precision, the following are recommended:

*   Only use a BigInt value when values greater than 253 are reasonably expected.
*   Don't coerce between BigInt values and Number values.

### [Conditionals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#conditionals)

A BigInt value follows the same conversion rules as Numbers when:

*   it is converted to a [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
    : via the [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
     function;
*   when used with [logical operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)
     `||`, `&&`, and `!`; or
*   within a conditional test like an [`if`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
     statement.

Namely, only `0n` is [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
; everything else is [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
.

### [Cryptography](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#cryptography)

The operations supported on BigInt values are not constant-time and are thus open to [timing attacks](https://en.wikipedia.org/wiki/Timing_attack "External link (opens in new tab)")
. JavaScript BigInts therefore could be dangerous for use in cryptography without mitigating factors. As a very generic example, an attacker could measure the time difference between `101n ** 65537n` and `17n ** 9999n`, and deduce the magnitude of secrets, such as private keys, based on the time elapsed. If you still have to use BigInts, take a look at the [Timing attack FAQ](https://timing.attacks.cr.yp.to/programming.html "External link (opens in new tab)")
 for general advice regarding the issue.

### [Use within JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#use_within_json)

Using [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
 with any BigInt value will raise a `TypeError`, as BigInt values aren't serialized in JSON by default. However, `JSON.stringify()` specifically leaves a backdoor for BigInt values: it would try to call the BigInt's `toJSON()` method. (It doesn't do so for any other primitive values.) Therefore, you can implement your own `toJSON()` method (which is one of the few cases where patching built-in objects is not explicitly discouraged):

Instead of throwing, `JSON.stringify()` now produces a string like this:

If you do not wish to patch `BigInt.prototype`, you can use the [`replacer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#the_replacer_parameter)
 parameter of `JSON.stringify` to serialize BigInt values:

You can then use the [`reviver`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#using_the_reviver_parameter)
 parameter of `JSON.parse` to handle them:

**Note:** While it's possible to make the replacer of `JSON.stringify()` generic and properly serialize BigInt values for all objects as shown above, the reviver of `JSON.parse()` has to be used with caution, because the serialization is _irreversible_: it's not possible to distinguish between an object that happens to have a property called `$bigint` and an actual BigInt.

In addition, the example above creates an entire object during replacing and reviving, which may have performance or storage implications for larger objects containing many BigInts. If you know the shape of the payload, it may be better to just serialize them as strings and revive them based on the property key's name instead.

In fact, JSON allows number literals that are arbitrarily long; they just cannot be parsed to full precision in JavaScript. If you are communicating with another program in a language that supports longer integers (such as 64-bit integers), and you want to transmit the BigInt as a JSON number instead of a JSON string, see [Lossless number serialization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON#using_json_numbers)
.

### [BigInt coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#bigint_coercion)

Many built-in operations that expect BigInts first coerce their arguments to BigInts. [The operation](https://tc39.es/ecma262/multipage/abstract-operations.html#sec-tobigint "External link (opens in new tab)")
 can be summarized as follows:

*   BigInts are returned as-is.
*   [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
     and [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
     throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
    .
*   `true` turns into `1n`; `false` turns into `0n`.
*   Strings are converted by parsing them as if they contain an integer literal. Any parsing failure results in a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
    . The syntax is a subset of [string numeric literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
    , where decimal points or exponent indicators are not allowed.
*   [Numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
     throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
     to prevent unintended implicit coercion causing loss of precision.
*   [Symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
     throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
    .
*   Objects are first [converted to a primitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
     by calling their [`[Symbol.toPrimitive]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive)
     (with `"number"` as hint), `valueOf()`, and `toString()` methods, in that order. The resulting primitive is then converted to a BigInt.

The best way to achieve nearly the same effect in JavaScript is through the [`BigInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
 function: `BigInt(x)` uses the same algorithm to convert `x`, except that [Numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
 don't throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
, but are converted to BigInts if they are integers.

Note that built-in operations expecting BigInts often truncate the BigInt to a fixed width after coercion. This includes [`BigInt.asIntN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/asIntN)
, [`BigInt.asUintN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/asUintN)
, and methods of [`BigInt64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array)
 and [`BigUint64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array)
.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#constructor)

-------------------------------------------------------------------------------------------------------------------

[`BigInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)

Returns primitive values of type BigInt. Throws an error when called with `new`.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#static_methods)

-------------------------------------------------------------------------------------------------------------------------

[`BigInt.asIntN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/asIntN)

Truncates a `BigInt` value to the given number of least significant bits and returns that value as a signed integer.

[`BigInt.asUintN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/asUintN)

Truncates a `BigInt` value to the given number of least significant bits and returns that value as an unsigned integer.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#instance_properties)

-----------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `BigInt.prototype` and shared by all `BigInt` instances.

[`BigInt.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `BigInt` instances, the initial value is the [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt)
 constructor.

[`BigInt.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#bigint.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"BigInt"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
. However, because `BigInt` also has its own [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/toString)
 method, this property is not used unless you call [`Object.prototype.toString.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
 with a BigInt as `thisArg`.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#instance_methods)

-----------------------------------------------------------------------------------------------------------------------------

[`BigInt.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/toLocaleString)

Returns a string with a language-sensitive representation of this BigInt value. Overrides the [`Object.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toLocaleString)
 method.

[`BigInt.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/toString)

Returns a string representing this BigInt value in the specified radix (base). Overrides the [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 method.

[`BigInt.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/valueOf)

Returns this BigInt value. Overrides the [`Object.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
 method.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#examples)

-------------------------------------------------------------------------------------------------------------

### [Calculating Primes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#calculating_primes)

**Note:** The `isPrime()` implementation is for demonstration only. For a real-world application, you would want to use a heavily [memoized](https://developer.mozilla.org/en-US/docs/Glossary/Memoization)
 algorithm such as the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes "External link (opens in new tab)")
 to avoid repeated calculations.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-bigint-objects](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-bigint-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
    
*   [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/bigint/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/bigint (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FBigInt&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fbigint%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FBigInt%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fbigint%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9f46f08d20b21498293cbf6b84f508103272ec6f%0A*+Document+last+modified%3A+2026-09-02T15%3A24%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")