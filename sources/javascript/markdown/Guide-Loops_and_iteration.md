*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#mdn-search)
    

Loops and iteration
===================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
    

Loops offer a quick and easy way to do something repeatedly. This chapter of the [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
 introduces the different iteration statements available to JavaScript.

You can think of a loop as a computerized version of the game where you tell someone to take _X_ steps in one direction, then _Y_ steps in another. For example, the idea "Go five steps to the east" could be expressed this way as a loop:

There are many different kinds of loops, but they all essentially do the same thing: they repeat an action some number of times. (Note that it's possible that number could be zero!)

The various loop mechanisms offer different ways to determine the start and end points of the loop. There are various situations that are more easily served by one type of loop over the others.

The statements for loops provided in JavaScript are:

*   [for statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#for_statement)
    
*   [do...while statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#do...while_statement)
    
*   [while statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#while_statement)
    
*   [labeled statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#labeled_statement)
    
*   [break statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#break_statement)
    
*   [continue statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#continue_statement)
    
*   [for...in statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#for...in_statement)
    
*   [for...of statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#for...of_statement)
    

[for statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#for_statement)

-----------------------------------------------------------------------------------------------------------------

A [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
 loop repeats until a specified condition evaluates to false. The JavaScript `for` loop is similar to the Java and C `for` loop.

A `for` statement looks as follows:

When a `for` loop executes, the following occurs:

1.  The initializing expression `initialization`, if any, is executed. This expression usually initializes one or more loop counters, but the syntax allows an expression of any degree of complexity. This expression can also declare variables.
2.  The `condition` expression is evaluated. If the value of `condition` is true, the loop statements execute. Otherwise, the `for` loop terminates. (If the `condition` expression is omitted entirely, the condition is assumed to be true.)
3.  The `statement` executes. To execute multiple statements, use a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
     (`{ }`) to group those statements.
4.  If present, the update expression `afterthought` is executed.
5.  Control returns to Step 2.

### [Example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#example)

In the example below, the function contains a `for` statement that counts the number of selected options in a scrolling list (a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element that allows multiple selections).

#### HTML

#### JavaScript

Here, the `for` statement declares the variable `i` and initializes it to `0`. It checks that `i` is less than the number of options in the `<select>` element, performs the succeeding `if` statement, and increments `i` by 1 after each pass through the loop.

[do...while statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#do...while_statement)

-------------------------------------------------------------------------------------------------------------------------------

The [`do...while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
 statement repeats until a specified condition evaluates to false.

A `do...while` statement looks as follows:

`statement` is always executed once before the condition is checked. (To execute multiple statements, use a block statement (`{ }`) to group those statements.)

If `condition` is `true`, the statement executes again. At the end of every execution, the condition is checked. When the condition is `false`, execution stops, and control passes to the statement following `do...while`.

### [Example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#example_2)

In the following example, the `do` loop iterates at least once and reiterates until `i` is no longer less than `5`.

[while statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#while_statement)

---------------------------------------------------------------------------------------------------------------------

A [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 statement executes its statements as long as a specified condition evaluates to `true`. A `while` statement looks as follows:

If the `condition` becomes `false`, `statement` within the loop stops executing and control passes to the statement following the loop.

The condition test occurs _before_ `statement` in the loop is executed. If the condition returns `true`, `statement` is executed and the `condition` is tested again. If the condition returns `false`, execution stops, and control is passed to the statement following `while`.

To execute multiple statements, use a block statement (`{ }`) to group those statements.

### [Example 1](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#example_1)

The following `while` loop iterates as long as `n` is less than `3`:

With each iteration, the loop increments `n` and adds that value to `x`. Therefore, `x` and `n` take on the following values:

*   After the first pass: `n` = `1` and `x` = `1`
*   After the second pass: `n` = `2` and `x` = `3`
*   After the third pass: `n` = `3` and `x` = `6`

After completing the third pass, the condition `n < 3` is no longer `true`, so the loop terminates.

### [Example 2](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#example_3)

Avoid infinite loops. Make sure the condition in a loop eventually becomes `false`—otherwise, the loop will never terminate! The statements in the following `while` loop execute forever because the condition never becomes `false`:

[labeled statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#labeled_statement)

-------------------------------------------------------------------------------------------------------------------------

A [`label`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
 provides a statement with an identifier that lets you refer to it elsewhere in your program. For example, you can use a label to identify a loop, and then use the `break` or `continue` statements to indicate whether a program should interrupt the loop or continue its execution.

The syntax of the labeled statement looks like the following:

The value of `label` may be any JavaScript identifier that is not a reserved word. The `statement` that you identify with a label may be any statement. For examples of using labeled statements, see the examples of `break` and `continue` below.

[break statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#break_statement)

---------------------------------------------------------------------------------------------------------------------

Use the [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
 statement to terminate a loop, `switch`, or in conjunction with a labeled statement.

*   When you use `break` without a label, it terminates the innermost enclosing `while`, `do-while`, `for`, or `switch` immediately and transfers control to the following statement.
*   When you use `break` with a label, it terminates the specified labeled statement.

The syntax of the `break` statement looks like this:

1.  The first form of the syntax terminates the innermost enclosing loop or `switch`.
2.  The second form of the syntax terminates the specified enclosing labeled statement.

### [Example 1](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#example_4)

The following example iterates through the elements in an array until it finds the index of an element whose value is `theValue`:

### [Example 2: Breaking to a label](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#example_2_breaking_to_a_label)

[continue statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#continue_statement)

---------------------------------------------------------------------------------------------------------------------------

The [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
 statement can be used to restart a `while`, `do-while`, `for`, or `label` statement.

*   When you use `continue` without a label, it terminates the current iteration of the innermost enclosing `while`, `do-while`, or `for` statement and continues execution of the loop with the next iteration. In contrast to the `break` statement, `continue` does not terminate the execution of the loop entirely. In a `while` loop, it jumps back to the condition. In a `for` loop, it jumps to the `increment-expression`.
*   When you use `continue` with a label, it applies to the looping statement identified with that label.

The syntax of the `continue` statement looks like the following:

### [Example 1](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#example_5)

The following example shows a `while` loop with a `continue` statement that executes when the value of `i` is `3`. Thus, `n` takes on the values `1`, `3`, `7`, and `12`.

If you comment out the `continue;`, the loop would run till the end and you would see `1,3,6,10,15`.

### [Example 2](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#example_6)

A statement labeled `checkIandJ` contains a statement labeled `checkJ`. If `continue` is encountered, the program terminates the current iteration of `checkJ` and begins the next iteration. Each time `continue` is encountered, `checkJ` reiterates until its condition returns `false`. When `false` is returned, the remainder of the `checkIandJ` statement is completed, and `checkIandJ` reiterates until its condition returns `false`. When `false` is returned, the program continues at the statement following `checkIandJ`.

If `continue` had a label of `checkIandJ`, the program would continue at the top of the `checkIandJ` statement.

[for...in statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#for...in_statement)

---------------------------------------------------------------------------------------------------------------------------

The [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 statement iterates a specified variable over all the enumerable properties of an object. For each distinct property, JavaScript executes the specified statements. A `for...in` statement looks as follows:

### [Example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#example_7)

The following function takes as its argument an object and the object's name. It then iterates over all the object's properties and returns a string that lists the property names and their values.

For an object `car` with properties `make` and `model`, `result` would be:

car.make = Ford
car.model = Mustang

### [Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#arrays)

Although it may be tempting to use this as a way to iterate over [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 elements, the `for...in` statement will return the name of your user-defined properties in addition to the numeric indexes.

Therefore, it is better to use a traditional [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
 loop with a numeric index when iterating over arrays, because the `for...in` statement iterates over user-defined properties in addition to the array elements, if you modify the Array object (such as adding custom properties or methods).

[for...of statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#for...of_statement)

---------------------------------------------------------------------------------------------------------------------------

The [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 statement creates a loop Iterating over [iterable objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
 (including [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
, [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
, [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
, [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object and so on), invoking a custom iteration hook with statements to be executed for the value of each distinct property.

The following example shows the difference between a `for...of` loop and a [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 loop. While `for...in` iterates over property names, `for...of` iterates over property values:

The `for...of` and `for...in` statements can also be used with [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
. For example, you can simultaneously loop over the keys and values of an object using [`Object.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries)
.

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/loops_and_iteration/index.md?plain=1 "Folder: en-us/web/javascript/guide/loops_and_iteration (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FLoops_and_iteration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Floops_and_iteration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FLoops_and_iteration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Floops_and_iteration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0abb70602b0b3b11a2909c417a03e10eabd607a8%0A*+Document+last+modified%3A+2026-05-21T18%3A54%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")