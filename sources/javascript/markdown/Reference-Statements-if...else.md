*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#mdn-search)
    

if...else
=========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`if...else`** statement executes a statement if a specified condition is [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
. If the condition is [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
, another statement in the optional `else` clause will be executed.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#try_it)

--------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#syntax)

--------------------------------------------------------------------------------------------------------

[`condition`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#condition)

An expression that is considered to be either [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 or [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
.

[`statement1`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#statement1)

Statement that is executed if _condition_ is [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
. Can be any statement, including further nested `if` statements. To execute multiple statements, use a [block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 statement (`{ /* ... */ }`) to group those statements. To execute no statements, use an [empty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Empty)
 statement.

[`statement2`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#statement2)

Statement that is executed if `condition` is [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 and the `else` clause exists. Can be any statement, including block statements and further nested `if` statements.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#description)

------------------------------------------------------------------------------------------------------------------

Multiple `if...else` statements can be nested to create an `else if` clause. Note that there is no `elseif` (in one word) keyword in JavaScript.

To see how this works, this is how it would look if the nesting were properly indented:

The conditions are evaluated in order until one evaluates to `true`. At that point, the associated statement is executed and the rest of the `else if` clauses are skipped.

To execute multiple statements within a clause, use a block statement (`{ /* ... */ }`) to group those statements.

Not using blocks may lead to confusing behavior, especially if the code is hand-formatted. For example:

This code looks innocent — however, executing `checkValue(1, 3)` will log "a is not 1". This is because in the case of [dangling else](https://en.wikipedia.org/wiki/Dangling_else "External link (opens in new tab)")
, the `else` clause will be connected to the closest `if` clause. Therefore, the code above, with proper indentation, would look like:

In general, it is a good practice to always use block statements, especially in code involving nested `if` statements.

Do not confuse the primitive Boolean values `true` and `false` with truthiness or falsiness of the [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
 object. Any value that is not `false`, `undefined`, `null`, `0`, `-0`, `NaN`, or the empty string (`""`), and any object, including a Boolean object whose value is `false`, is considered [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 when used as the condition. For example:

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#examples)

------------------------------------------------------------------------------------------------------------

### [Using if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#using_if...else)

### [Using else if](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#using_else_if)

Note that there is no `elseif` syntax in JavaScript. However, you can write it with a space between `else` and `if`:

### [Using an assignment as a condition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#using_an_assignment_as_a_condition)

You should almost never have an `if...else` with an assignment like `x = y` as a condition:

Because unlike [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 loops, the condition is only evaluated once, so the assignment is only performed once. The code above is equivalent to:

Which is much clearer. However, in the rare case you find yourself wanting to do something like that, the [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 documentation has a [Using an assignment as a condition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#using_an_assignment_as_a_condition)
 section with our recommendations.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-if-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-if-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else#see_also)

------------------------------------------------------------------------------------------------------------

*   [`block`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
    
*   [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
    
*   [Conditional (ternary) operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/if...else/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/if...else (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fif...else&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fif...else%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fif...else%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fif...else%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0dff7c501b844de960d5a180c1348a9ce01b82fe%0A*+Document+last+modified%3A+2026-05-04T02%3A42%3A58.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")