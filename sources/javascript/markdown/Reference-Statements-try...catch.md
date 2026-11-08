*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#mdn-search)
    

try...catch
===========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`try...catch`** statement is comprised of a `try` block and either a `catch` block, a `finally` block, or both. The code in the `try` block is executed first, and if it throws an exception, the code in the `catch` block will be executed. The code in the `finally` block will always be executed before control flow exits the entire construct.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#try_it)

----------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#syntax)

----------------------------------------------------------------------------------------------------------

[`tryStatements`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#trystatements)

The statements to be executed.

[`catchStatements`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#catchstatements)

Statement that is executed if an exception is thrown in the `try` block.

[`exceptionVar` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#exceptionvar)

An optional [identifier or pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#catch_binding)
 to hold the caught exception for the associated `catch` block. If the `catch` block does not use the exception's value, you can omit the `exceptionVar` and its surrounding parentheses.

[`finallyStatements`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#finallystatements)

Statements that are executed before control flow exits the `try...catch...finally` construct. These statements execute regardless of whether an exception was thrown or caught.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#description)

--------------------------------------------------------------------------------------------------------------------

The `try` statement always starts with a `try` block. Then, a `catch` block or a `finally` block must be present. It's also possible to have both `catch` and `finally` blocks. This gives us three forms for the `try` statement:

*   `try...catch`
*   `try...finally`
*   `try...catch...finally`

Unlike other constructs such as [`if`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
 or [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
, the `try`, `catch`, and `finally` blocks must be _blocks_, instead of single statements.

A `catch` block contains statements that specify what to do if an exception is thrown in the `try` block. If any statement within the `try` block (or in a function called from within the `try` block) throws an exception, control is immediately shifted to the `catch` block. If no exception is thrown in the `try` block, the `catch` block is skipped.

The `finally` block will always execute before control flow exits the `try...catch...finally` construct. It always executes, regardless of whether an exception was thrown or caught.

You can nest one or more `try` statements. If an inner `try` statement does not have a `catch` block, the enclosing `try` statement's `catch` block is used instead.

You can also use the `try` statement to handle JavaScript exceptions. See the [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#exception_handling_statements)
 for more information on JavaScript exceptions.

### [Catch binding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#catch_binding)

When an exception is thrown in the `try` block, `exceptionVar` (i.e., the `e` in `catch (e)`) holds the exception value. You can use this [binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
 to get information about the exception that was thrown. This [binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
 is only available in the `catch` block's [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
.

It doesn't need to be a single identifier. You can use a [destructuring pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 to assign multiple identifiers at once.

The bindings created by the `catch` clause live in the same scope as the `catch` block, so any variables declared in the `catch` block cannot have the same name as the bindings created by the `catch` clause. (There's [one exception to this rule](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#statements)
, but it's a deprecated syntax.)

The exception binding is writable. For example, you may want to normalize the exception value to make sure it's an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
 object.

If you don't need the exception value, you can omit it along with the enclosing parentheses.

### [The finally block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#the_finally_block)

The `finally` block contains statements to execute after the `try` block and `catch` block(s) execute, but before the statements following the `try...catch...finally` block. Control flow will always enter the `finally` block, which can proceed in one of the following ways:

*   Immediately after the control flow exits the `try` block in a `try...finally` construct (either after the last statement or a `throw`, `return`, `break`, or `continue` statement);
*   Immediately after the control flow exits the `catch` block in a `try...catch...finally` construct;
*   Immediately after the control flow exits the `try` block in a `try...catch...finally` construct, unless it exits via a `throw` statement (in which case control flow enters the `catch` block first).

If the `finally` block is entered after a control flow statement (`return`, `throw`, `break`, `continue`) in the `try` or `catch` block, the effect of this statement is deferred until after the last statement executed in the `finally` block. For example, if an exception is thrown from the `try` block, even when there's no `catch` block to handle the exception, the `finally` block still executes, and the exception is thrown immediately after the `finally` block finishes executing.

However, there is one exception to this rule: if the last statement executed in the `finally` block is itself a control flow statement, that statement will override the effect of the previous one (no deferral); see [returning from a `finally` block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#returning_from_a_finally_block)
 for examples. It is generally a bad idea to use control flow statements (`return`, `throw`, `break`, `continue`) in the `finally` block because they can override the effect of previously executed control flow statements, which is rarely intended. Most of the time, the `finally` block should be reserved for cleanup code that does not modify the main logic.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#examples)

--------------------------------------------------------------------------------------------------------------

### [Unconditional catch block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#unconditional_catch_block)

When a `catch` block is used, the `catch` block is executed when any exception is thrown from within the `try` block. For example, when the exception occurs in the following code, control transfers to the `catch` block.

The `catch` block specifies an identifier (`e` in the example above) that holds the value of the exception; this value is only available in the [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
 of the `catch` block.

### [Conditional catch blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#conditional_catch_blocks)

You can create "Conditional `catch` blocks" by combining `try...catch` blocks with `if...else if...else` structures, like this:

A common use case for this is to only catch (and silence) a small subset of expected errors, and then re-throw the error in other cases:

This may mimic the syntax from other languages, like Java:

### [Nested try blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#nested_try_blocks)

First, let's see what happens with this:

Now, if we already caught the exception in the inner `try` block by adding a `catch` block:

And now, let's rethrow the error.

Any given exception will be caught only once by the nearest enclosing `catch` block unless it is rethrown. Of course, any new exceptions raised in the "inner" block (because the code in `catch` block may do something that throws), will be caught by the "outer" block.

### [Resource cleanup using finally](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#resource_cleanup_using_finally)

The following example shows one use case for the `finally` block. The code opens a file and then executes statements that use the file; the `finally` block makes sure the file always closes after it is used even if an exception was thrown.

In the same way, the effect of any `return` statement in the `try` block is deferred at the end of the `finally` block, although the return value expression is evaluated before entering the `finally` block.

### [Returning from a finally block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#returning_from_a_finally_block)

The following example illustrates how control flow statements in the `finally` block behave. When control flow exits the `try` block via the first `return` statement, the return value expression (`order.sort()`) is evaluated before entering the `finally` block, and the function is planned to return that value after the `finally` block finishes executing. However, the `return` statement in the `finally` block overrides the effect of the previous `return` statement, including its return value.

The same logic applies to other control flow statements. Here, the function is first planned to throw the value `"catch"`, but instead returns the value `"finally"`.

Again, control flow statements are discouraged in the `finally` block because this effect is likely not intended.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-try-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-try-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
    
*   [`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Mar 9, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/try...catch/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/try...catch (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ftry...catch&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ftry...catch%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ftry...catch%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ftry...catch%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F203acfabc8a27b2a64757df33586b3c29abb730f%0A*+Document+last+modified%3A+2026-03-09T16%3A45%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")