*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#mdn-search)
    

Logical OR (||)
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **logical OR (`||`)** (logical disjunction) operator for a set of operands is true if and only if one or more of its operands is true. It is typically used with boolean (logical) values. When it is, it returns a Boolean value. However, the `||` operator actually returns the value of one of the specified operands, so if this operator is used with non-Boolean values, it will return a non-Boolean value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#try_it)

--------------------------------------------------------------------------------------------------------

    const a = 3;
    const b = -2;
    
    console.log(a > 0 || b > 0);
    // Expected output: true
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#syntax)

--------------------------------------------------------------------------------------------------------

js

    x || y
    

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#description)

------------------------------------------------------------------------------------------------------------------

If `x` can be converted to `true`, returns `x`; else, returns `y`.

If a value can be converted to `true`, the value is so-called [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
. If a value can be converted to `false`, the value is so-called [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
.

Examples of expressions that can be converted to false are:

*   `null`;
*   `NaN`;
*   `0`;
*   empty string (`""` or `''` or ` `` `);
*   `undefined`.

Even though the `||` operator can be used with operands that are not Boolean values, it can still be considered a boolean operator since its return value can always be converted to a [boolean primitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#boolean_type)
. To explicitly convert its return value (or any expression in general) to the corresponding boolean value, use a double [NOT operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT)
 or the [`Boolean()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/Boolean)
 constructor.

### [Short-circuit evaluation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#short-circuit_evaluation)

The logical OR expression is evaluated left to right, it is tested for possible "short-circuit" evaluation using the following rule:

`(some truthy expression) || expr` is short-circuit evaluated to the truthy expression.

Short circuit means that the `expr` part above is **not evaluated**, hence any side effects of doing so do not take effect (e.g., if `expr` is a function call, the calling never takes place). This happens because the value of the operator is already determined after the evaluation of the first operand. See example:

js

    function A() {
      console.log("called A");
      return false;
    }
    function B() {
      console.log("called B");
      return true;
    }
    
    console.log(B() || A());
    // Logs "called B" due to the function call,
    // then logs true (which is the resulting value of the operator)
    

### [Operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#operator_precedence)

The following expressions might seem equivalent, but they are not, because the `&&` operator is executed before the `||` operator (see [operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
).

js

    true || false && false; // returns true, because && is executed first
    (true || false) && false; // returns false, because grouping has the highest precedence
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#examples)

------------------------------------------------------------------------------------------------------------

### [Using OR](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#using_or)

The following code shows examples of the `||` (logical OR) operator.

js

    true || true; // t || t returns true
    false || true; // f || t returns true
    true || false; // t || f returns true
    false || 3 === 4; // f || f returns false
    "Cat" || "Dog"; // t || t returns "Cat"
    false || "Cat"; // f || t returns "Cat"
    "Cat" || false; // t || f returns "Cat"
    "" || false; // f || f returns false
    false || ""; // f || f returns ""
    false || varObject; // f || object returns varObject
    

**Note:** If you use this operator to provide a default value to some variable, be aware that any _falsy_ value will not be used. If you only need to filter out [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
, consider using [the nullish coalescing operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
.

### [Conversion rules for booleans](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#conversion_rules_for_booleans)

#### Converting AND to OR

The following operation involving **booleans**:

js

    bCondition1 && bCondition2
    

is always equal to:

js

    !(!bCondition1 || !bCondition2)
    

#### Converting OR to AND

The following operation involving **booleans**:

js

    bCondition1 || bCondition2
    

is always equal to:

js

    !(!bCondition1 && !bCondition2)
    

### [Removing nested parentheses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#removing_nested_parentheses)

As logical expressions are evaluated left to right, it is always possible to remove parentheses from a complex expression following some rules.

The following composite operation involving **booleans**:

js

    bCondition1 && (bCondition2 || bCondition3)
    

is always equal to:

js

    !(!bCondition1 || !bCondition2 && !bCondition3)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-LogicalORExpression](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-LogicalORExpression) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR#see_also)

------------------------------------------------------------------------------------------------------------

*   [Nullish coalescing operator (`??`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
    
*   [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
    
*   [Truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
    
*   [Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/logical_or/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/logical_or (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLogical_OR&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Flogical_or%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FLogical_OR%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Flogical_or%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")