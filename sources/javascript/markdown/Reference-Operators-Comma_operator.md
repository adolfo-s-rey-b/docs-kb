*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#mdn-search)
    

Comma operator (,)
==================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **comma (`,`)** operator evaluates each of its operands (from left to right) and returns the value of the last operand. This is commonly used to provide multiple updaters to a [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
 loop's afterthought.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#try_it)

------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#syntax)

------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#parameters)

[`expr1`, `expr2`, `expr3`, …](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#expr1)

One or more expressions, the last of which is returned as the value of the compound expression.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#description)

----------------------------------------------------------------------------------------------------------------------

You can use the comma operator when you want to include multiple expressions in a location that requires a single expression. The most common usage of this operator is to supply multiple updaters in a `for` loop. For an idiom allowing multiple _statements_ in a location that requires a single expression, you may use an [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
.

Because all expressions except the last are evaluated and then discarded, these expressions must have side effects to be useful. Common expressions that have side effects are assignments, function calls, and [`++`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
 and [`--`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)
 operators. Others may also have side effects if they invoke [getters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 or trigger [type coercions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#type_coercion)
.

The comma operator has the lowest [precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
 of all operators. If you want to incorporate a comma-joined expression into a bigger expression, you must parenthesize it.

The comma operator is completely different from commas used as syntactic separators in other locations, which include:

*   Elements in array initializers (`[1, 2, 3]`)
*   Properties in [object initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
     (`{ a: 1, b: 2 }`)
*   Parameters in [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    /expressions (`function f(a, b) { … }`)
*   Arguments in function calls (`f(1, 2)`)
*   [Binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
     lists in [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    , [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    , or [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
     declarations (`const a = 1, b = 2;`)
*   Import lists in [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
     declarations (`import { a, b } from "c";`)
*   Export lists in [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
     declarations (`export { a, b };`)

In fact, although some of these places accept almost all expressions, they don't accept comma-joined expressions because that would be ambiguous with the syntactic comma separators. In this case, you must parenthesize the comma-joined expression. For example, the following is a `const` declaration that declares two variables, where the comma is not the comma operator:

It is different from the following, where `b = 2` is an [assignment expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
, not a declaration. The value of `a` is `2`, the return value of the assignment, while the value of `1` is discarded:

Comma operators cannot appear as [trailing commas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#examples)

----------------------------------------------------------------------------------------------------------------

### [Using the comma operator in a for loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#using_the_comma_operator_in_a_for_loop)

If `a` is a 2-dimensional array with 10 elements on each side, the following code uses the comma operator to increment `i` and decrement `j` at once, thus printing the values of the diagonal elements in the array:

### [Using the comma operator to join assignments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#using_the_comma_operator_to_join_assignments)

Because commas have the lowest [precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
 — even lower than assignment — commas can be used to join multiple assignment expressions. In the following example, `a` is set to the value of `b = 3` (which is 3). Then, the `c = 4` expression evaluates and its result becomes the return value of the entire comma expression.

### [Processing and then returning](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#processing_and_then_returning)

Another example that one could make with the comma operator is processing before returning. As stated, only the last element will be returned but all others are going to be evaluated as well. So, one could do:

This is especially useful for one-line [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
. The following example uses a single [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
 to get both the sum of an array and the squares of its elements, which would otherwise require two iterations, one with [`reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
 and one with `map()`:

### [Discarding reference binding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#discarding_reference_binding)

The comma operator always returns the last expression as a _value_ instead of a _reference_. This causes some contextual information such as the [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 binding to be lost. For example, a property access returns a reference to the function, which also remembers the object that it's accessed on, so that calling the property works properly. If the method is returned from a comma expression, then the function is called as if it's a new function value, and `this` is `undefined`.

You can enter [indirect eval](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#direct_and_indirect_eval)
 with this technique, because direct eval requires the function call to happen on the reference to the `eval()` function.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-comma-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-comma-operator) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
    
*   [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/comma_operator/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/comma_operator (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FComma_operator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fcomma_operator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FComma_operator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fcomma_operator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")