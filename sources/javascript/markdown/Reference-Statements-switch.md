*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#mdn-search)
    

switch
======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`switch`** statement evaluates an [expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
, matching the expression's value against a series of `case` clauses, and executes [statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
 after the first `case` clause with a matching value, until a `break` statement is encountered. The `default` clause of a `switch` statement will be jumped to if no `case` matches the expression's value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#try_it)

-----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#syntax)

-----------------------------------------------------------------------------------------------------

[`expression`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#expression)

An expression whose result is matched against each `case` clause.

[`caseExpressionN` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#caseexpressionn)

A `case` clause used to match against `expression`. If the value of `expression` matches the value of any `caseExpressionN`, execution starts from the first statement after that `case` clause until either the end of the `switch` statement or the first encountered `break`.

[`default` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#default)

A `default` clause; if provided, this clause is executed if the value of `expression` doesn't match any of the `case` clauses. A `switch` statement can only have one `default` clause.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#description)

---------------------------------------------------------------------------------------------------------------

A `switch` statement first evaluates its expression. It then looks for the first `case` clause whose expression evaluates to the same value as the result of the input expression (using the [strict equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)
 comparison) and transfers control to that clause, executing all statements following that clause.

The clause expressions are only evaluated when necessary — if a match is already found, subsequent `case` clause expressions will not be evaluated, even when they will be visited by [fall-through](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#breaking_and_fall-through)
.

If no matching `case` clause is found, the program looks for the optional `default` clause, and if found, transfers control to that clause, executing statements following that clause. If no `default` clause is found, the program continues execution at the statement following the end of `switch`. By convention, the `default` clause is the last clause, but it does not need to be so. A `switch` statement may only have one `default` clause; multiple `default` clauses will result in a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.

### [Breaking and fall-through](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#breaking_and_fall-through)

You can use the [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
 statement within a `switch` statement's body to break out early, often when all statements between two `case` clauses have been executed. Execution will continue at the first statement following `switch`.

If `break` is omitted, execution will proceed to the next `case` clause, even to the `default` clause, regardless of whether the value of that clause's expression matches. This behavior is called "fall-through".

In the appropriate context, other control-flow statements also have the effect of breaking out of the `switch` statement. For example, if the `switch` statement is contained in a function, then a [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
 statement terminates the execution of the function body and therefore the `switch` statement. If the `switch` statement is contained in a loop, then a [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
 statement stops the `switch` statement and jumps to the next iteration of the loop.

### [Lexical scoping](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#lexical_scoping)

The `case` and `default` clauses are like [labels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
: they indicate possible places that control flow may jump to. However, they don't create lexical [scopes](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
 themselves (neither do they automatically break out — as demonstrated above). For example:

This example will output the error "Uncaught SyntaxError: Identifier 'message' has already been declared", because the first `const message = 'hello';` conflicts with the second `const message = 'hi';` declaration, even when they're within their own separate case clauses. Ultimately, this is due to both `const` declarations being within the same block scope created by the `switch` body.

To fix this, whenever you need to use `let` or `const` declarations in a `case` clause, wrap it in a block.

This code will now output `hello` in the console as it should, without any errors.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#examples)

---------------------------------------------------------------------------------------------------------

### [Using switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#using_switch)

In the following example, if `expr` evaluates to `Bananas`, the program matches the value with case `case 'Bananas'` and executes the associated statement. When `break` is encountered, the program breaks out of `switch` and executes the statement following `switch`. If `break` were omitted, the statement for the `case 'Cherries'` would also be executed.

### [Putting the default clause between two case clauses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#putting_the_default_clause_between_two_case_clauses)

If no match is found, execution will start from the `default` clause, and execute all statements after that.

It also works when you put `default` before all other `case` clauses.

### [Taking advantage of fall-through](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#taking_advantage_of_fall-through)

This method takes advantage of the fact that if there is no `break` below a `case` clause, execution will continue to the next `case` clause regardless if that `case` meets the criteria.

The following is an example of a single operation sequential `case` statement, where four different values perform exactly the same.

The following is an example of a multiple-operation sequential `case` clause, where, depending on the provided integer, you can receive different output. This shows you that it will traverse in the order that you put the `case` clauses, and it does not have to be numerically sequential. In JavaScript, you can even mix in definitions of strings into these `case` statements as well.

The output from this example:

| Value | Log text |
| --- | --- |
| `foo` is `NaN` or not `1`, `2`, `3`, `4`, `5`, or `0` | Please pick a number from 0 to 5! |
| `0` | Output: So What Is Your Name? |
| `1` | Output: What Is Your Name? |
| `2` | Output: Your Name? |
| `3` | Output: Name? |
| `4` | Output: ? |
| `5` | Output: ! |

### [An alternative to if...else chains](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#an_alternative_to_if...else_chains)

You may often find yourself doing a series of [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
 matches.

This pattern is not doing a sequence of `===` comparisons, but you can still convert it to a `switch` construct.

The `switch (true)` pattern as an alternative to `if...else` is especially useful if you want to utilize the fall-through behavior.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-switch-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-switch-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch#see_also)

---------------------------------------------------------------------------------------------------------

*   [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/switch/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/switch (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fswitch&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fswitch%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fswitch%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fswitch%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")