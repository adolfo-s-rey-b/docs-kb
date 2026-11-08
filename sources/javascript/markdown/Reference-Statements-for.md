*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#mdn-search)
    

for
===

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`for`** statement creates a loop that consists of three optional expressions, enclosed in parentheses and separated by semicolons, followed by a statement (usually a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
) to be executed in the loop.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#syntax)

--------------------------------------------------------------------------------------------------

[`initialization` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#initialization)

An expression (including [assignment expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
) or variable declaration evaluated once before the loop begins. Typically used to initialize a counter variable. This expression may optionally declare new variables with `var` or `let` keywords. Variables declared with `var` are not local to the loop, i.e., they are in the same scope the `for` loop is in. Variables declared with `let` are local to the statement.

The result of this expression is discarded.

[`condition` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#condition)

An expression to be evaluated before each loop iteration. If this expression [evaluates to true](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
, `statement` is executed. If the expression [evaluates to false](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
, execution exits the loop and goes to the first statement after the `for` construct.

This conditional test is optional. If omitted, the condition always evaluates to true.

[`afterthought` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#afterthought)

An expression to be evaluated at the end of each loop iteration. This occurs before the next evaluation of `condition`. Generally used to update or increment the counter variable.

[`statement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#statement)

A statement that is executed as long as the condition evaluates to true. You can use a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 to execute multiple statements. To execute no statement within the loop, use an [empty statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Empty)
 (`;`).

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#description)

------------------------------------------------------------------------------------------------------------

Like other looping statements, you can use [control flow statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#control_flow)
 inside `statement`:

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
     stops `statement` execution and goes to the first statement after the loop.
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
     stops `statement` execution and re-evaluates `afterthought` then `condition`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#examples)

------------------------------------------------------------------------------------------------------

### [Using for](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#using_for)

The following `for` statement starts by declaring the variable `i` and initializing it to `0`. It checks that `i` is less than nine, performs the two succeeding statements, and increments `i` by 1 after each pass through the loop.

### [Initialization block syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#initialization_block_syntax)

The initialization block accepts both expressions and variable declarations. However, expressions cannot use the [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 operator unparenthesized, because that is ambiguous with a [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 loop.

### [Optional for expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#optional_for_expressions)

All three expressions in the head of the `for` loop are optional. For example, it is not required to use the `initialization` block to initialize variables:

Like the `initialization` block, the `condition` part is also optional. If you are omitting this expression, you must make sure to break the loop in the body in order to not create an infinite loop.

You can also omit all three expressions. Again, make sure to use a [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
 statement to end the loop and also modify (increase) a variable, so that the condition for the break statement is true at some point.

However, in the case where you are not fully using all three expression positions — especially if you are not declaring variables with the first expression but mutating something in the upper scope — consider using a [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 loop instead, which makes the intention clearer.

### [Lexical declarations in the initialization block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#lexical_declarations_in_the_initialization_block)

Declaring a variable within the initialization block has important differences from declaring it in the upper [scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope)
, especially when creating a [closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)
 within the loop body. For example, for the code below:

It logs `0`, `1`, and `2`, as expected. However, if the variable is defined in the upper scope:

It logs `3`, `3`, and `3`. The reason is that each `setTimeout` creates a new closure that closes over the `i` variable, but if the `i` is not scoped to the loop body, all closures will reference the same variable when they eventually get called — and due to the asynchronous nature of [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
, it will happen after the loop has already exited, causing the value of `i` in all queued callbacks' bodies to have the value of `3`.

This also happens if you use a `var` statement as the initialization, because variables declared with `var` are only function-scoped, but not lexically scoped (i.e., they can't be scoped to the loop body).

The scoping effect of the initialization block can be understood as if the declaration happens within the loop body, but just happens to be accessible within the `condition` and `afterthought` parts. More precisely, `let` declarations are special-cased by `for` loops — if `initialization` is a `let` declaration, then every time, after the loop body is evaluated, the following happens:

1.  A new lexical scope is created with new `let`\-declared variables.
2.  The binding values from the last iteration are used to re-initialize the new variables.
3.  `afterthought` is evaluated in the new scope.

So re-assigning the new variables within `afterthought` does not affect the bindings from the previous iteration.

A new lexical scope is also created after `initialization`, just before `condition` is evaluated for the first time. These details can be observed by creating closures, which allow you to get hold of a binding at any particular point. For example, in this code a closure created within the `initialization` section does not get updated by re-assignments of `i` in the `afterthought`:

This does not log "0, 1, 2", like what would happen if `getI` is declared in the loop body. This is because `getI` is not re-evaluated on each iteration — rather, the function is created once and closes over the `i` variable, which refers to the variable declared when the loop was first initialized. Subsequent updates to the value of `i` actually create new variables called `i`, which `getI` does not see. A way to fix this is to re-compute `getI` every time `i` updates:

The `i` variable inside the `initialization` is distinct from the `i` variable inside every iteration, including the first. So, in this example, `getI` returns 0, even though the value of `i` inside the iteration is incremented beforehand:

In fact, you can capture this initial binding of the `i` variable and re-assign it later, and this updated value will not be visible to the loop body, which sees the next new binding of `i`.

This logs "0, 0, 0", because the `i` variable in each loop evaluation is actually a separate variable, but `getI` and `incrementI` both read and write the _initial_ binding of `i`, not what was subsequently declared.

### [Using for without a body](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#using_for_without_a_body)

The following `for` cycle calculates the offset position of a node in the `afterthought` section, and therefore it does not require the use of a `statement` section, a semicolon is used instead.

Note that the semicolon after the `for` statement is mandatory, because it stands as an [empty statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Empty)
. Otherwise, the `for` statement acquires the following `console.log` line as its `statement` section, which makes the `log` execute multiple times.

### [Using for with two iterating variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#using_for_with_two_iterating_variables)

You can create two counters that are updated simultaneously in a for loop using the [comma operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)
. Multiple `let` and `var` declarations can also be joined with commas.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-for-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-for-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for#see_also)

------------------------------------------------------------------------------------------------------

*   [Empty statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Empty)
    
*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
    
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
    
*   [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
    
*   [`do...while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
    
*   [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
    
*   [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/for/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/for (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F56f3d7018159127dbe92842413fb45d0aa7e8193%0A*+Document+last+modified%3A+2026-08-27T13%3A16%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")