*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#mdn-search)
    

while
=====

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`while`** statement creates a loop that executes a specified statement as long as the test condition evaluates to true. The condition is evaluated before executing the statement.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#syntax)

----------------------------------------------------------------------------------------------------

[`condition`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#condition)

An expression evaluated _before_ each pass through the loop. If this condition [evaluates to true](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
, `statement` is executed. When condition [evaluates to false](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
, execution continues with the statement after the `while` loop.

[`statement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#statement)

A statement that is executed as long as the condition evaluates to true. You can use a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 to execute multiple statements.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#description)

--------------------------------------------------------------------------------------------------------------

Like other looping statements, you can use [control flow statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#control_flow)
 inside `statement`:

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
     stops `statement` execution and goes to the first statement after the loop.
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
     stops `statement` execution and re-evaluates `condition`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#examples)

--------------------------------------------------------------------------------------------------------

### [Using while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#using_while)

The following `while` loop iterates as long as `n` is less than three.

Each iteration, the loop increments `n` and adds it to `x`. Therefore, `x` and `n` take on the following values:

*   After the first pass: `n` = 1 and `x` = 1
*   After the second pass: `n` = 2 and `x` = 3
*   After the third pass: `n` = 3 and `x` = 6

After completing the third pass, the condition `n` < 3 is no longer true, so the loop terminates.

### [Using an assignment as a condition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#using_an_assignment_as_a_condition)

In some cases, it can make sense to use an assignment as a condition. This comes with readability tradeoffs, so there are certain stylistic recommendations that would make the pattern more obvious for everyone.

Consider the following example, which iterates over a document's comments, logging them to the console.

That's not completely a good-practice example, due to the following line specifically:

The _effect_ of that line is fine — in that, each time a comment node is found:

1.  `iterator.nextNode()` returns that comment node, which gets assigned to `currentNode`.
2.  The value of `currentNode = iterator.nextNode()` is therefore [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
    .
3.  So the `console.log()` call executes and the loop continues.

…and then, when there are no more comment nodes in the document:

1.  `iterator.nextNode()` returns [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
    .
2.  The value of `currentNode = iterator.nextNode()` is therefore also `null`, which is [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
    .
3.  So the loop ends.

The problem with this line is: conditions typically use [comparison operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#comparison_operators)
 such as `===`, but the `=` in that line isn't a comparison operator — instead, it's an [assignment operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#assignment_operators)
. So that `=` _looks like_ it's a typo for `===` — even though it's _not_ actually a typo.

Therefore, in cases like that one, some [code-linting tools](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_tools/Introducing_complete_toolchain#code_linting_tools)
 such as ESLint's [`no-cond-assign`](https://eslint.org/docs/latest/rules/no-cond-assign "External link (opens in new tab)")
 rule — in order to help you catch a possible typo so that you can fix it — will report a warning such as the following:

> Expected a conditional expression and instead saw an assignment.

Many style guides recommend more explicitly indicating the intention for the condition to be an assignment. You can do that minimally by putting additional parentheses as a [grouping operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping)
 around the assignment:

In fact, this is the style enforced by ESLint's `no-cond-assign`'s default configuration, as well as [Prettier](https://prettier.io/ "External link (opens in new tab)")
, so you'll likely see this pattern a lot in the wild.

Some people may further recommend adding a comparison operator to turn the condition into an explicit comparison:

There are other ways to write this pattern, such as:

Or, forgoing the idea of using a `while` loop altogether:

If the reader is sufficiently familiar with the assignment as condition pattern, all these variations should have equivalent readability. Otherwise, the last form is probably the most readable, albeit the most verbose.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-while-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-while-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#see_also)

--------------------------------------------------------------------------------------------------------

*   [`do...while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
    
*   [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
    
*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
    
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/while/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/while (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fwhile&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fwhile%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fwhile%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fwhile%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")