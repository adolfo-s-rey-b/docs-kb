*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#mdn-search)
    

Block statement
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **block statement** is used to group zero or more statements. The block is delimited by a pair of braces ("curly braces") and contains a list of zero or more statements and declarations.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#syntax)

----------------------------------------------------------------------------------------------------

[`StatementList`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#statementlist)

Statements and declarations grouped within the block statement.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#description)

--------------------------------------------------------------------------------------------------------------

The block statement is often called the _compound statement_ in other languages. It allows you to use multiple statements where JavaScript expects only one statement. Combining statements into blocks is a common practice in JavaScript, especially when used in association with control flow statements like [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
 and [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
. The opposite behavior is possible using an [empty statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Empty)
, where you provide no statement, although one is required.

In addition, combined with block-scoped declarations like [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
, [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, and [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
, blocks can prevent temporary variables from polluting the global namespace, just like [IIFEs](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 do.

### [Block scoping rules with var or function declaration in non-strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#block_scoping_rules_with_var_or_function_declaration_in_non-strict_mode)

Variables declared with `var` or created by [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
 in non-strict mode **do not** have block scope. Variables introduced within a block are scoped to the containing function or script, and the effects of setting them persist beyond the block itself. For example:

This logs 2 because the `var x` statement within the block is in the same scope as the `var x` statement before the block.

In non-strict code, function declarations inside blocks behave strangely. Do not use them.

### [Block scoping rules with let, const, class, or function declaration in strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#block_scoping_rules_with_let_const_class_or_function_declaration_in_strict_mode)

By contrast, identifiers declared with [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
, [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, and [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
 do have block scope:

The `x = 2` is limited in scope to the block in which it was defined.

The same is true of `const`:

Note that the block-scoped `const c = 2` _does not_ throw a `SyntaxError: Identifier 'c' has already been declared` because it can be declared uniquely within the block.

In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, function declarations inside blocks are scoped to that block and are hoisted to the top of the block.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#examples)

--------------------------------------------------------------------------------------------------------

### [Using a block statement as the body of a for loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#using_a_block_statement_as_the_body_of_a_for_loop)

A [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
 loop accepts a single statement as its body.

If you want to use more than one statement in the loop body, you can group them into one block statement:

### [Using a block statement to encapsulate data](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#using_a_block_statement_to_encapsulate_data)

`let` and `const` declarations are scoped to the containing block. This allows you to hide data from the global scope without wrapping it in a function.

### [`using` declarations in a block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#using_declarations_in_a_block)

You can declare variables with [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 or [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
 in a block, which causes the object stored in the variable to be disposed when control exits the block. For more information, see [resource management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-block](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-block) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block#see_also)

--------------------------------------------------------------------------------------------------------

*   [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
    
*   [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
    
*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 29, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/block/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/block (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fblock&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fblock%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fblock%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fblock%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb6a36de3428f4b42c7707c8f190a349db13bf531%0A*+Document+last+modified%3A+2025-07-29T03%3A29%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")