*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#mdn-search)
    

typeof
======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`typeof`** operator returns a string indicating the type of the operand's value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#syntax)

----------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#parameters)

[`operand`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#operand)

An expression representing the object or [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 whose type is to be returned.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#description)

--------------------------------------------------------------------------------------------------------------

The following table summarizes the possible return values of `typeof`. For more information about types and primitives, see also the [JavaScript data structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)
 page.

| Type | Result |
| --- | --- |
| [Undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined) | `"undefined"` |
| [Null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null) | `"object"` ([reason](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#typeof_null)<br>) |
| [Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) | `"boolean"` |
| [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) | `"number"` |
| [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt) | `"bigint"` |
| [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) | `"string"` |
| [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) | `"symbol"` |
| [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)<br> (implements \[\[Call\]\] in ECMA-262 terms; [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)<br> are functions as well) | `"function"` |
| Any other object | `"object"` |

This list of values is exhaustive. No spec-compliant engines are reported to produce (or had historically produced) values other than those listed.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#examples)

--------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#basic_usage)

### [typeof null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#typeof_null)

In the first implementation of JavaScript, JavaScript values were represented as a type tag and a value. The type tag for objects was `0`. `null` was represented as the NULL pointer (`0x00` in most platforms). Consequently, `null` had `0` as type tag, hence the `typeof` return value `"object"`. ([reference](https://2ality.com/2013/10/typeof-null.html "External link (opens in new tab)")
)

A fix was proposed for ECMAScript (via an opt-in), but [was rejected](https://web.archive.org/web/20160331031419/http://wiki.ecmascript.org:80/doku.php?id=harmony:typeof_null "External link (opens in new tab)")
. It would have resulted in `typeof null === "null"`.

### [Using new operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#using_new_operator)

All constructor functions called with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 will return non-primitives (`"object"` or `"function"`). Most return objects, with the notable exception being [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
, which returns a function.

### [Need for parentheses in syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#need_for_parentheses_in_syntax)

The `typeof` operator has higher [precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
 than binary operators like addition (`+`). Therefore, parentheses are needed to evaluate the type of an addition result.

### [Interaction with undeclared and uninitialized variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#interaction_with_undeclared_and_uninitialized_variables)

`typeof` works with undeclared identifiers, returning `"undefined"` instead of throwing an error.

However, using `typeof` on lexical declarations ([`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
, and [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
) in the same block before the place of declaration will throw a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
. Block scoped variables are in a _[temporal dead zone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
_ from the start of the block until the initialization is processed, during which it will throw an error if accessed.

See [`typeof` operator and `undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined#typeof_operator_and_undefined)
 for more details.

### [Exceptional behavior of document.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#exceptional_behavior_of_document.all)

All current browsers expose a non-standard host object [`document.all`](https://developer.mozilla.org/en-US/docs/Web/API/Document/all)
 with type `undefined`.

Although `document.all` is also [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 and [loosely equal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
 to `undefined`, it is not [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
. The case of `document.all` having type `"undefined"` is classified in the web standards as a "willful violation" of the original ECMAScript standard for web compatibility.

### [Custom method that gets a more specific type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#custom_method_that_gets_a_more_specific_type)

`typeof` is very useful, but it's not as versatile as might be required. For example, `typeof []` is `"object"`, as well as `typeof new Date()`, `typeof /abc/`, etc.

For greater specificity in checking types, here we present a custom `type(value)` function, which mostly mimics the behavior of `typeof`, but for non-primitives (i.e., objects and functions), it returns a more granular type name where possible.

For checking potentially non-existent variables that would otherwise throw a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
, use `typeof nonExistentVar === "undefined"` because this behavior cannot be mimicked with custom code.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-typeof-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-typeof-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#see_also)

--------------------------------------------------------------------------------------------------------

*   [`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
    
*   [`document.all` willful violation of the standard](https://github.com/tc39/ecma262/issues/668 "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/typeof/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/typeof (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Ftypeof&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Ftypeof%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Ftypeof%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Ftypeof%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1ddd95504b4507beeda0f08bd772eb167922b86a%0A*+Document+last+modified%3A+2026-05-22T15%3A48%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")