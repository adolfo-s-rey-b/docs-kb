*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#mdn-search)
    

Labeled statement
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **labeled statement** is any [statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
 that is prefixed with an identifier. You can jump to this label using a [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
 or [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
 statement nested within the labeled statement.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#syntax)

----------------------------------------------------------------------------------------------------

[`label`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#label)

Any JavaScript [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
 that is not a [reserved word](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words)
.

[`statement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#statement)

A JavaScript statement. `break` can be used within any labeled statement, and `continue` can be used within labeled looping statements.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#description)

--------------------------------------------------------------------------------------------------------------

You can use a label to identify a statement, and later refer to it using a `break` or `continue` statement. Note that JavaScript has _no_ `goto` statement; you can only use labels with `break` or `continue`.

Any `break` or `continue` that references `label` must be contained within the `statement` that's labeled by `label`. Think about `label` as a variable that's only available in the scope of `statement`.

If a `break label;` statement is encountered when executing `statement`, execution of `statement` terminates, and execution continues at the statement immediately following the labeled statement.

`continue label;` can only be used if `statement` is one of the [looping statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#iterations)
. If a `continue label;` statement is encountered when executing `statement`, execution of `statement` continues at the next iteration of the loop. `continue;` without a label can only continue the innermost loop, while `continue label;` allows continuing any given loop even when the statement is nested within other loops.

A statement can have multiple labels. In this case, the labels are all functionally equivalent.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#examples)

--------------------------------------------------------------------------------------------------------

### [Using a labeled continue with for loops](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#using_a_labeled_continue_with_for_loops)

Notice how it skips both "i = 1, j = 1" and "i = 1, j = 2".

### [Using a labeled break with for loops](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#using_a_labeled_break_with_for_loops)

Notice the difference with the previous `continue` example: when `break loop1` is encountered, the execution of the outer loop is terminated, so there are no further logs beyond "i = 1, j = 0"; when `continue loop1` is encountered, the execution of the outer loop continues at the next iteration, so only "i = 1, j = 1" and "i = 1, j = 2" are skipped.

### [Using a labeled continue statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#using_a_labeled_continue_statement)

Given an array of items and an array of tests, this example counts the number of items that pass all the tests.

Note how the `continue itemIteration;` statement skips the rest of the tests for the current item as well as the statement that updates the `itemsPassed` counter, and continues with the next item. If you don't use a label, you would need to use a boolean flag instead.

### [Using a labeled break statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#using_a_labeled_break_statement)

Given an array of items and an array of tests, this example determines whether all items pass all tests.

Again, if you don't use a label, you would need to use a boolean flag instead.

### [Using a labeled block with break](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#using_a_labeled_block_with_break)

You can label statements other than loops, such as simple blocks, but only `break` statements can reference non-loop labels.

### [Labeled function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#labeled_function_declarations)

Labels can only be applied to [statements, not declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#what_are_statements_declarations_and_expressions)
. There is a legacy grammar that allows function declarations to be labeled in non-strict code:

In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 code, however, this will throw a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
:

Non-plain functions, such as [generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
 and [async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
 can neither be labeled in strict code, nor in non-strict code:

The labeled function declaration syntax is [deprecated](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features)
 and you should not use it, even in non-strict code. You cannot actually jump to this label within the function body.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-labelled-statements](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-labelled-statements) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#see_also)

--------------------------------------------------------------------------------------------------------

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
    
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/label/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/label (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Flabel&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Flabel%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Flabel%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Flabel%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5c8d0ac21db572edebbd4ad428efca0af3ec1734%0A*+Document+last+modified%3A+2026-09-04T17%3A06%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")