*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#mdn-search)
    

Logical AND (&&)
================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **logical AND (`&&`)** (logical conjunction) operator for a set of boolean operands will be `true` if and only if all the operands are `true`. Otherwise it will be `false`.

More generally, the operator returns the value of the first [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 operand encountered when evaluating from left to right, or the value of the last operand if they are all [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#try_it)

---------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#syntax)

---------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#description)

-------------------------------------------------------------------------------------------------------------------

Logical AND (`&&`) evaluates operands from left to right, returning immediately with the value of the first [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 operand it encounters; if all values are [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
, the value of the last operand is returned.

If a value can be converted to `true`, the value is so-called [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
. If a value can be converted to `false`, the value is so-called [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
.

Examples of expressions that can be converted to false are:

*   `false`;
*   `null`;
*   `NaN`;
*   `0`;
*   empty string (`""` or `''` or ` `` `);
*   `undefined`.

The AND operator preserves non-Boolean values and returns them as they are:

Even though the `&&` operator can be used with non-Boolean operands, it is still considered a boolean operator since its return value can always be converted to a [boolean primitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#boolean_type)
. To explicitly convert its return value (or any expression in general) to the corresponding boolean value, use a double [NOT operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT)
 or the [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/Boolean)
 constructor.

### [Short-circuit evaluation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#short-circuit_evaluation)

The logical AND expression is a short-circuit operator. As each operand is converted to a boolean, if the result of one conversion is found to be `false`, the AND operator stops and returns the original value of that falsy operand; it does **not** evaluate any of the remaining operands.

Consider the pseudocode below.

(some falsy expression) && expr

The `expr` part is **never evaluated** because the first operand `(some falsy expression)` is evaluated as [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
. If `expr` is a function, the function is never called. See the example below:

### [Operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#operator_precedence)

The AND operator has a higher precedence than the OR operator, meaning the `&&` operator is executed before the `||` operator (see [operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#examples)

-------------------------------------------------------------------------------------------------------------

### [Using AND](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#using_and)

The following code shows examples of the `&&` (logical AND) operator.

### [Conversion rules for booleans](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#conversion_rules_for_booleans)

#### Converting AND to OR

The following operation involving **booleans**:

is always equal to:

#### Converting OR to AND

The following operation involving **booleans**:

is always equal to:

### [Removing nested parentheses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#removing_nested_parentheses)

As logical expressions are evaluated left to right, it is always possible to remove parentheses from a complex expression provided that certain rules are followed.

The following composite operation involving **booleans**:

is always equal to:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-LogicalANDExpression](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-LogicalANDExpression) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
    
*   [Truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
    
*   [Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/logical_and/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/logical_and (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLogical_AND&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Flogical_and%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLogical_AND%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Flogical_and%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")