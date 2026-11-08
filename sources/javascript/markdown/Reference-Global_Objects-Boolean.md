*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#mdn-search)
    

Boolean
=======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**`Boolean`** values can be one of two values: `true` or `false`, representing the truth value of a logical proposition.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#description)

--------------------------------------------------------------------------------------------------------------------

Boolean values are typically produced by [relational operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#relational_operators)
, [equality operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#equality_operators)
, and [logical NOT (`!`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT)
. They can also be produced by functions that represent conditions, such as [`Array.isArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)
. Note that [binary logical operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#binary_logical_operators)
 such as `&&` and `||` return the values of the operands, which may or may not be boolean values.

Boolean values are typically used in conditional testing, such as the condition for [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
 and [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 statements, the [conditional operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)
 (`? :`), or the predicate return value of [`Array.prototype.filter()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
.

You would rarely need to explicitly convert something to a boolean value, as JavaScript does this automatically in boolean contexts, so you can use any value as if it's a boolean, based on its [truthiness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#boolean_coercion)
. You are also encouraged to use `if (condition)` and `if (!condition)` instead of `if (condition === true)` or `if (condition === false)` in your own code so you can take advantage of this convention. However, making sure that values representing conditions are always booleans can help clarify the intent of your code.

### [Boolean primitives and Boolean objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#boolean_primitives_and_boolean_objects)

For converting non-boolean values to boolean, use `Boolean` as a function or use the [double NOT](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#double_not_!!)
 operator. Do not use the `Boolean()` constructor with `new`.

This is because _all_ objects, including a `Boolean` object whose wrapped value is `false`, are [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 and evaluate to `true` in places such as conditional statements. (See also the [boolean coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#boolean_coercion)
 section below.)

**Warning:** You should rarely find yourself using `Boolean` as a constructor.

### [Boolean coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#boolean_coercion)

Many built-in operations that expect booleans first coerce their arguments to booleans. [The operation](https://tc39.es/ecma262/multipage/abstract-operations.html#sec-toboolean "External link (opens in new tab)")
 can be summarized as follows:

*   Booleans are returned as-is.
*   [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
     turns into `false`.
*   [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
     turns into `false`.
*   `0`, `-0`, and `NaN` turn into `false`; other numbers turn into `true`.
*   `0n` turns into `false`; other [BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
     turn into `true`.
*   The empty string `""` turns into `false`; other strings turn into `true`.
*   [Symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
     turn into `true`.
*   All objects become `true`.

**Note:** A legacy behavior makes [`document.all`](https://developer.mozilla.org/en-US/docs/Web/API/Document/all)
 return `false` when used as a boolean, despite it being an object. This property is legacy and non-standard and should not be used.

**Note:** Unlike other type conversions like [string coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
 or [number coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
, boolean coercion does not attempt to [convert objects to primitives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
 by calling user methods.

In other words, there are only a handful of values that get coerced to `false` — these are called [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 values. All other values are called [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 values. A value's truthiness is important when used with logical operators, conditional statements, or any boolean context.

There are two ways to achieve the same effect in JavaScript.

*   [Double NOT](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT#double_not_!!)
    : `!!x` negates `x` twice, which converts `x` to a boolean using the same algorithm as above.
*   The [`Boolean()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/Boolean)
     function: `Boolean(x)` uses the same algorithm as above to convert `x`.

Note that truthiness is not the same as being [loosely equal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
 to `true` or `false`.

`[]` is truthy, but it's also loosely equal to `false`. It's truthy, because all objects are truthy. However, when comparing with `false`, which is a primitive, `[]` is also converted to a primitive, which is `""` via [`Array.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toString)
. Comparing strings and booleans results in both being [converted to numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
, and they both become `0`, so `[] == false` is `true`. In general, falsiness and `== false` differ in the following cases:

*   `NaN`, `undefined`, and `null` are falsy but not loosely equal to `false`.
*   `"0"` (and other string literals that are not `""` but [get coerced to 0](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
    ) is truthy but loosely equal to `false`.
*   Objects are always truthy, but their primitive representation may be loosely equal to `false`.

Truthy values are even more unlikely to be loosely equal to `true`. All values are either truthy or falsy, but most values are loosely equal to neither `true` nor `false`.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#constructor)

--------------------------------------------------------------------------------------------------------------------

[`Boolean()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/Boolean)

Creates `Boolean` objects. When called as a function, it returns primitive values of type Boolean.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#instance_properties)

------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Boolean.prototype` and shared by all `Boolean` instances.

[`Boolean.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Boolean` instances, the initial value is the [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/Boolean)
 constructor.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#instance_methods)

------------------------------------------------------------------------------------------------------------------------------

[`Boolean.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/toString)

Returns a string of either `true` or `false` depending upon the value of the object. Overrides the [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 method.

[`Boolean.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/valueOf)

Returns the primitive value of the `Boolean` object. Overrides the [`Object.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
 method.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#examples)

--------------------------------------------------------------------------------------------------------------

### [Creating false values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#creating_false_values)

### [Creating true values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#creating_true_values)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-boolean-objects](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-boolean-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean)
    
*   [Boolean primitives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#boolean_type)
    
*   [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type "External link (opens in new tab)")
     on Wikipedia

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/boolean/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/boolean (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FBoolean&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fboolean%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FBoolean%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fboolean%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")