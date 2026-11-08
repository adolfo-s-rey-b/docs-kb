*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#mdn-search)
    

Control flow and error handling
===============================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
    

JavaScript supports a compact set of statements, specifically control flow statements, that you can use to incorporate a great deal of interactivity in your application. This chapter provides an overview of these statements.

The [JavaScript reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
 contains exhaustive details about the statements in this chapter. The semicolon (`;`) character is used to separate statements in JavaScript code.

Any JavaScript expression is also a statement. See [Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
 for complete information about expressions.

[Block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#block_statement)

---------------------------------------------------------------------------------------------------------------------------------

The most basic statement is a _block statement_, which is used to group statements. The block is delimited by a pair of curly braces:

### [Example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#example)

Block statements are commonly used with control flow statements (`if`, `for`, `while`).

Here, `{ x++; }` is the block statement.

**Note:** [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
\-declared variables are not block-scoped, but are scoped to the containing function or script, and the effects of setting them persist beyond the block itself. For example:

This outputs `2` because the `var x` statement within the block is in the same scope as the `var x` statement before the block. (In C or Java, the equivalent code would have output `1`.)

This scoping effect can be mitigated by using [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 or [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
.

[Conditional statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#conditional_statements)

-----------------------------------------------------------------------------------------------------------------------------------------------

A conditional statement is a set of commands that executes if a specified condition is true. JavaScript supports two conditional statements: `if...else` and `switch`.

### [if...else statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#if...else_statement)

Use the `if` statement to execute a statement if a logical condition is `true`. Use the optional `else` clause to execute a statement if the condition is `false`.

An `if` statement looks like this:

Here, the `condition` can be any expression that evaluates to `true` or `false`. (See [Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#description)
 for an explanation of what evaluates to `true` and `false`.)

If `condition` evaluates to `true`, `statement1` is executed. Otherwise, `statement2` is executed. `statement1` and `statement2` can be any statement, including further nested `if` statements.

You can also compound the statements using `else if` to have multiple conditions tested in sequence, as follows:

In the case of multiple conditions, only the first logical condition which evaluates to `true` will be executed. To execute multiple statements, group them within a block statement (`{ /* … */ }`).

#### Best practice

In general, it's good practice to always use block statements—_especially_ when nesting `if` statements:

In general it's good practice to not have an `if...else` with an assignment like `x = y` as a condition:

However, in the rare case you find yourself wanting to do something like that, the [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 documentation has a [Using an assignment as a condition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#using_an_assignment_as_a_condition)
 section with guidance on a general best-practice syntax you should know about and follow.

#### Falsy values

The following values evaluate to `false` (also known as [Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 values):

*   `false`
*   `undefined`
*   `null`
*   `0`
*   `NaN`
*   the empty string (`""`)

All other values—including all objects—evaluate to `true` when passed to a conditional statement.

**Note:** Do not confuse the primitive boolean values `true` and `false` with the true and false values of the [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
 object!

For example:

#### Example

In the following example, the function `checkData` returns `true` if the number of characters in a `Text` object is three. Otherwise, it displays an alert and returns `false`.

### [switch statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#switch_statement)

A `switch` statement allows a program to evaluate an expression and attempt to match the expression's value to a `case` label. If a match is found, the program executes the associated statement.

A `switch` statement looks like this:

JavaScript evaluates the above switch statement as follows:

*   The program first looks for a `case` clause with a label matching the value of expression and then transfers control to that clause, executing the associated statements.
*   If no matching label is found, the program looks for the optional `default` clause:
    *   If a `default` clause is found, the program transfers control to that clause, executing the associated statements.
    *   If no `default` clause is found, the program resumes execution at the statement following the end of `switch`.
    *   (By convention, the `default` clause is written as the last clause, but it does not need to be so.)

#### break statements

The optional `break` statement associated with each `case` clause ensures that the program breaks out of `switch` once the matched statement is executed, and then continues execution at the statement following `switch`. If `break` is omitted, the program continues execution inside the `switch` statement (and will execute statements under the next `case`, and so on).

##### Example

In the following example, if `fruitType` evaluates to `"Bananas"`, the program matches the value with `case "Bananas"` and executes the associated statement. When `break` is encountered, the program exits the `switch` and continues execution from the statement following `switch`. If `break` were omitted, the statement for `case "Cherries"` would also be executed.

[Exception handling statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#exception_handling_statements)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

You can throw exceptions using the `throw` statement and handle them using the `try...catch` statements.

*   [`throw` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#throw_statement)
    
*   [`try...catch` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#try...catch_statement)
    

### [Exception types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#exception_types)

Just about any object can be thrown in JavaScript. Nevertheless, not all thrown objects are created equal. While it is common to throw numbers or strings as errors, it is frequently more effective to use one of the exception types specifically created for this purpose:

*   [ECMAScript exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#error_types)
    
*   [`DOMException`](https://developer.mozilla.org/en-US/docs/Web/API/DOMException)
    

### [throw statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#throw_statement)

Use the `throw` statement to throw an exception. A `throw` statement specifies the value to be thrown:

You may throw any expression, not just expressions of a specific type. The following code throws several exceptions of varying types:

### [try...catch statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#try...catch_statement)

The `try...catch` statement marks a block of statements to try, and specifies one or more responses should an exception be thrown. If an exception is thrown, the `try...catch` statement catches it.

The `try...catch` statement consists of a `try` block, which contains one or more statements, and a `catch` block, containing statements that specify what to do if an exception is thrown in the `try` block.

In other words, you want the `try` block to succeed—but if it does not, you want control to pass to the `catch` block. If any statement within the `try` block (or in a function called from within the `try` block) throws an exception, control _immediately_ shifts to the `catch` block. If no exception is thrown in the `try` block, the `catch` block is skipped. The `finally` block executes after the `try` and `catch` blocks execute but before the statements following the `try...catch` statement.

The following example uses a `try...catch` statement. The example calls a function that retrieves a month name from an array based on the value passed to the function. If the value does not correspond to a month number (`1` – `12`), an exception is thrown with the value `'Invalid month code'` and the statements in the `catch` block set the `monthName` variable to `'unknown'`.

#### The catch block

You can use a `catch` block to handle all exceptions that may be generated in the `try` block.

The `catch` block specifies an identifier (`exception` in the preceding syntax) that holds the value specified by the `throw` statement. You can use this identifier to get information about the exception that was thrown.

JavaScript creates this identifier when the `catch` block is entered. The identifier lasts only for the duration of the `catch` block. Once the `catch` block finishes executing, the identifier no longer exists.

For example, the following code throws an exception. When the exception occurs, control transfers to the `catch` block.

**Note:** When logging errors to the console inside a `catch` block, using `console.error()` rather than `console.log()` is advised for debugging. It formats the message as an error, and adds it to the list of error messages generated by the page.

#### The finally block

The `finally` block contains statements to be executed _after_ the `try` and `catch` blocks execute. Additionally, the `finally` block executes _before_ the code that follows the `try...catch...finally` statement.

It is also important to note that the `finally` block will execute _whether or not_ an exception is thrown. If an exception is thrown, however, the statements in the `finally` block execute even if no `catch` block handles the exception that was thrown.

You can use the `finally` block to make your script fail gracefully when an exception occurs. For example, you may need to release a resource that your script has tied up.

The following example opens a file and then executes statements that use the file. (Server-side JavaScript allows you to access files.) If an exception is thrown while the file is open, the `finally` block closes the file before the script fails. Using `finally` here _ensures_ that the file is never left open, even if an error occurs.

If the `finally` block returns a value, this value becomes the return value of the entire `try...catch...finally` production, regardless of any `return` statements in the `try` and `catch` blocks:

Overwriting of return values by the `finally` block also applies to exceptions thrown or re-thrown inside of the `catch` block:

#### Nesting try...catch statements

You can nest one or more `try...catch` statements.

If an inner `try` block does _not_ have a corresponding `catch` block:

1.  it _must_ contain a `finally` block, and
2.  the enclosing `try...catch` statement's `catch` block is checked for a match.

For more information, see [nested try-blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#nested_try_blocks)
 on the [`try...catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
 reference page.

### [Utilizing Error objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#utilizing_error_objects)

Depending on the type of error, you may be able to use the `name` and `message` properties to get a more refined message.

The `name` property provides the general class of `Error` (such as `DOMException` or `Error`), while `message` generally provides a more succinct message than one would get by converting the error object to a string.

If you are throwing your own exceptions, in order to take advantage of these properties (such as if your `catch` block doesn't discriminate between your own exceptions and system ones), you can use the `Error` constructor.

For example:

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 19, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/control_flow_and_error_handling/index.md?plain=1 "Folder: en-us/web/javascript/guide/control_flow_and_error_handling (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FControl_flow_and_error_handling&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fcontrol_flow_and_error_handling%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FControl_flow_and_error_handling%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fcontrol_flow_and_error_handling%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F08d55156ba73587da8c20d882dea32ccba85dc0d%0A*+Document+last+modified%3A+2025-09-19T23%3A15%3A13.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")