*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#mdn-search)
    

Statements and declarations
===========================

JavaScript code is built from statements and declarations, which can contain expressions. This reference groups the constructs used to control execution and declare bindings. A statement can span multiple lines, and a line can contain multiple statements.

[Statements and declarations by category](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#statements_and_declarations_by_category)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

For an alphabetical listing see the sidebar on the left.

### [Control flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#control_flow)

[`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)

Specifies the value to be returned by a function.

[`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)

Terminates the current loop, switch, or label statement and transfers program control to the statement following the terminated statement.

[`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)

Terminates execution of the statements in the current iteration of the current or labeled loop, and continues execution of the loop with the next iteration.

[`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)

Throws a user-defined exception.

[`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)

Executes a statement if a specified condition is true. If the condition is false, another statement can be executed.

[`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)

Evaluates an expression, matching the expression's value to a case clause, and executes statements associated with that case.

[`try...catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)

Marks a block of statements to try, and specifies a response, should an exception be thrown.

### [Declaring variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#declaring_variables)

[`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)

Declares a variable, optionally initializing it to a value.

[`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

Declares a block-scoped variable, optionally initializing it to a value.

[`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)

Declares a block-scoped variable that cannot be re-assigned, which must be initialized at declaration.

[`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)

Declares a variable like `const` that is _synchronously disposed_.

[`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)

Declares a variable like `const` that is _asynchronously disposed_.

### [Functions and classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#functions_and_classes)

[`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)

Declares a function with the specified parameters.

[`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)

Generator Functions enable writing [iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
 more easily.

[`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

Declares an async function with the specified parameters.

[`async function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)

Asynchronous Generator Functions enable writing async [iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
 more easily.

[`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)

Declares a class.

### [Iterations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#iterations)

[`do...while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)

Creates a loop that executes a specified statement until the test condition evaluates to false. The condition is evaluated after executing the statement, resulting in the specified statement executing at least once.

[`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)

Creates a loop that consists of three optional expressions, enclosed in parentheses and separated by semicolons, followed by a statement executed in the loop.

[`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)

Iterates over the enumerable properties of an object, in arbitrary order. For each distinct property, statements can be executed.

[`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)

Iterates over iterable objects (including [arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
, array-like objects, [iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
), invoking a custom iteration hook with statements to be executed for the value of each distinct property.

[`for await...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)

Iterates over async iterable objects, array-like objects, [iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
, invoking a custom iteration hook with statements to be executed for the value of each distinct property.

[`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)

Creates a loop that executes a specified statement as long as the test condition evaluates to true. The condition is evaluated before executing the statement.

### [Others](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#others)

[Empty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Empty)

An empty statement is used to provide no statement, although the JavaScript syntax would expect one.

[Block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)

A block statement is used to group zero or more statements. The block is delimited by a pair of curly braces.

[Expression statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)

An expression statement evaluates an expression and discards its result. It allows the expression to perform side effects, such as executing a function or updating a variable.

[`debugger`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger)

Invokes any available debugging functionality. If no debugging functionality is available, this statement has no effect.

[`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)

Used to export functions to make them available for imports in external modules, and other scripts.

[`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)

Used to import functions exported from an external module, another script.

[`import defer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/defer)

Loads a module as a namespace, deferring synchronous evaluation until the returned namespace's properties are accessed.

[`import source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/source)

Results in an object representing the module's compiled source, without loading its dependencies, linking it, or evaluating it.

[label](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)

Provides a statement with an identifier that you can refer to using a `break` or `continue` statement.

[`with`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)

Extends the scope chain for a statement.

[What are statements, declarations, and expressions?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#what_are_statements_declarations_and_expressions)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All JavaScript programs are composed of a sequence of top-level constructs, using one of the syntaxes listed above. These are known as [_statements_](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#prod-Statement "External link (opens in new tab)")
 and [_declarations_](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#prod-Declaration "External link (opens in new tab)")
. In MDN docs, we often colloquially refer to both as _statements_, but they are technically two disjoint sets of grammars.

The following are declarations:

*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    
*   [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    
*   [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
    
*   [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
    
*   [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    
*   [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    
*   [`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
    
*   [`async function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
     (Note: it can only appear at the top-level of a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    )
*   [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
     (Note: it can only appear at the top-level of a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    )

Everything else in the [list above](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#statements_and_declarations_by_category)
 is a statement.

The terms "statement" and "declaration" have a precise meaning in the formal syntax of JavaScript that affects where they may be placed in code. For example, in most control-flow structures, the body only accepts statements — such as the two arms of an [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
:

If you use a declaration instead of a statement, it would be a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
. For example, a [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 declaration is not a statement, so you can't use it in its bare form as the body of an `if` statement.

On the other hand, [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
 is a statement, so you can use it on its own as the `if` body.

You can see declarations as "[binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
 identifiers to values", and statements as "carrying out actions". The fact that `var` is a statement instead of a declaration is a special case, because it doesn't follow normal lexical scoping rules and may create side effects — in the form of creating global variables, mutating existing `var`\-defined variables, and defining variables that are visible outside of its block (because `var`\-defined variables aren't block-scoped).

As another example, [labels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
 can only be attached to statements.

**Note:** There's a legacy grammar that allows [function declarations to have labels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label#labeled_function_declarations)
, but it's only standardized for compatibility with web reality.

To get around this, you can wrap the declaration in braces — this makes it part of a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
.

In JavaScript, statements and declarations produce values, but these values are almost never observable (other than [`eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
). Their purpose is to manipulate the surrounding environment and produce side effects—creating variable bindings, outputting things, modifying variable values, etc. The values they use come from evaluating [_expressions_](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-Expression "External link (opens in new tab)")
.

Expressions are not top-level constructs; they can only be used in specific slots inside statements and declarations, such as `if (expression)`, `const x = expression`, etc. The [expression statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
 syntax allows most expressions to be used as statements, but that's just a statement with a single expression slot.

You can map out JavaScript syntax structures using just statements, declarations, and expressions:

*   Statements can contain statements, declarations, and expressions (like `if (expression) statement` and block statements `{ statement; declaration }`)
*   Declarations can contain statements, declarations, and expressions (like `function x() { statement; declaration }` and `const x = expression`)
*   Expressions can contain statements, declarations, and expressions (like `() => { statement; declaration }` and `console.log(expression)`)

In the reference documentation for each piece of syntax, we describe all its "slots" and say whether each slot is a statement, declaration, or expression.

_Operators_ is another important concept in JavaScript grammar, but they do not work like building blocks. See [What are operators?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#what_are_operators)
 for more information.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#see_also)

--------------------------------------------------------------------------------------------------

*   [Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 15, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff693fdeb65be430fdf3b7fc5cdf44a10a13f2bbf%0A*+Document+last+modified%3A+2026-09-15T05%3A12%3A42.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")