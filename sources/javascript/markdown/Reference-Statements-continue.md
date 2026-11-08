*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#mdn-search)
    

continue
========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`continue`** statement terminates execution of the statements in the current iteration of the current or labeled loop, and continues execution of the loop with the next iteration.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#syntax)

-------------------------------------------------------------------------------------------------------

[`label` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#label)

Identifier associated with the label of the statement.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#description)

-----------------------------------------------------------------------------------------------------------------

In contrast to the [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
 statement, `continue` does not terminate the execution of the loop entirely, but instead:

*   In a [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
     or [`do...while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
     loop, it jumps back to the condition.
*   In a [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
     loop, it jumps to the update expression.
*   In a [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
    , [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
    , or [`for await...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)
     loop, it jumps to the next iteration.

The `continue` statement can include an optional label that allows the program to jump to the next iteration of a labeled loop statement instead of the innermost loop. In this case, the `continue` statement needs to be nested within this labeled statement.

A `continue` statement, with or without a following label, cannot be used at the top level of a script, module, function's body, or [static initialization block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
, even when the function or class is further contained within a loop.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#examples)

-----------------------------------------------------------------------------------------------------------

### [Using continue with while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#using_continue_with_while)

The following example shows a [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 loop that has a `continue` statement that executes when the value of `i` is 3. Thus, `n` takes on the values 1, 3, 7, and 12.

### [Using continue with a label](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#using_continue_with_a_label)

In the following example, a statement labeled `checkIAndJ` contains a statement labeled `checkJ`. If `continue` is encountered, the program continues at the top of the `checkJ` statement. Each time `continue` is encountered, `checkJ` reiterates until its condition returns false. When false is returned, the remainder of the `checkIAndJ` statement is completed.

If `continue` had a label of `checkIAndJ`, the program would continue at the top of the `checkIAndJ` statement.

Output:

i: 0

// start checkJ
j: 8
7 is odd.
j: 7
j: 6
5 is odd.
j: 5
// end checkJ

i = 1
j = 4

i: 1
i = 2
j = 4

i: 2
i = 3
j = 4

i: 3
i = 4
j = 4

### [Unsyntactic continue statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#unsyntactic_continue_statements)

`continue` cannot be used within loops across function boundaries.

When referencing a label, the labeled statement must contain the `continue` statement.

The labeled statement must be a loop.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-continue-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-continue-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
    
*   [label](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/continue/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/continue (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fcontinue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fcontinue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fcontinue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fcontinue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")