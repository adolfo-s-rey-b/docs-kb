*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#mdn-search)
    

NaN
===

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`NaN`** global property is a value representing Not-A-Number.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#try_it)

------------------------------------------------------------------------------------------------------

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#value)

----------------------------------------------------------------------------------------------------

The same number value as [`Number.NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN)
.

|     |     |
| --- | --- |
| Writable | no  |
| Enumerable | no  |
| Configurable | no  |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#description)

----------------------------------------------------------------------------------------------------------------

`NaN` is a property of the _global object_. In other words, it is a variable in global scope.

In modern browsers, `NaN` is a non-configurable, non-writable property. Even when this is not the case, avoid overriding it.

There are five different types of operations that return `NaN`:

*   Failed number conversion (e.g., explicit ones like `parseInt("blabla")`, `Number(undefined)`, or implicit ones like `Math.abs(undefined)`)
*   Math operation where the result is not a real number (e.g., `Math.sqrt(-1)`)
*   Indeterminate form (e.g., `0 * Infinity`, `1 ** Infinity`, `Infinity / Infinity`, `Infinity - Infinity`)
*   A method or expression whose operand is or gets coerced to `NaN` (e.g., `7 ** NaN`, `7 * "blabla"`) — this means `NaN` is contagious
*   Other cases where an invalid value is to be represented as a number (e.g., an invalid [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
     `new Date("blabla").getTime()`, `"".charCodeAt(1)`)

`NaN` and its behaviors are not invented by JavaScript. Its semantics in floating point arithmetic (including that `NaN !== NaN`) are specified by [IEEE 754](https://en.wikipedia.org/wiki/Double_precision_floating-point_format "External link (opens in new tab)")
. `NaN`'s behaviors include:

*   If `NaN` is involved in a mathematical operation (but not [bitwise operations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#bitwise_shift_operators)
    ), the result is usually also `NaN`. (See [counter-example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#silently_escaping_nan)
     below.)
*   When `NaN` is one of the operands of any relational comparison (`>`, `<`, `>=`, `<=`), the result is always `false`.
*   `NaN` compares unequal (via [`==`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
    , [`!=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality)
    , [`===`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)
    , and [`!==`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality)
    ) to any other value — including to another `NaN` value.

`NaN` is also one of the [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 values in JavaScript.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#examples)

----------------------------------------------------------------------------------------------------------

### [Testing against NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#testing_against_nan)

To tell if a value is `NaN`, use [`Number.isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
 or [`isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN)
 to most clearly determine whether a value is `NaN` — or, since `NaN` is the only value that compares unequal to itself, you can perform a self-comparison like `x !== x`.

However, do note the difference between `isNaN()` and `Number.isNaN()`: the former will return `true` if the value is currently `NaN`, or if it is going to be `NaN` after it is coerced to a number, while the latter will return `true` only if the value is currently `NaN`:

For the same reason, using a BigInt value will throw an error with `isNaN()` and not with `Number.isNaN()`:

Additionally, some array methods cannot find `NaN`, while others can. Namely, the index-finding ones ([`indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)
, [`lastIndexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf)
) cannot find `NaN`, while the value-finding ones ([`includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
) can:

For more information about `NaN` and its comparison, see [Equality comparison and sameness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness)
.

### [Observably distinct NaN values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#observably_distinct_nan_values)

It's possible to produce two floating point numbers with different binary representations but are both `NaN`, because in [IEEE 754 encoding](https://en.wikipedia.org/wiki/NaN#Floating_point "External link (opens in new tab)")
, any floating point number with exponent `0x7ff` and a non-zero mantissa is `NaN`. In JavaScript, you can do bit-level manipulation using [typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
.

### [Silently escaping NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#silently_escaping_nan)

`NaN` propagates through mathematical operations, so it's usually sufficient to test for `NaN` once at the end of calculation to detect error conditions. The only case where `NaN` gets silently escaped is when using [exponentiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
 with an exponent of `0`, which immediately returns `1` without testing the base's value.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-value-properties-of-the-global-object-nan](https://tc39.es/ecma262/multipage/global-object.html#sec-value-properties-of-the-global-object-nan) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN#see_also)

----------------------------------------------------------------------------------------------------------

*   [`Number.NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN)
    
*   [`Number.isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
    
*   [`isNaN()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/nan/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/nan (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FNaN&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fnan%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FNaN%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fnan%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")