*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#mdn-search)
    

for await...of
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`for await...of`** statement creates a loop iterating over [async iterable objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols)
 as well as [sync iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
. This statement can only be used in contexts where [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 can be used, which includes inside an [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
 body and in a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#try_it)

-------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#syntax)

-------------------------------------------------------------------------------------------------------------

[`variable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#variable)

Receives a value from the sequence on each iteration. May be either a declaration with [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
, or [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
, or an [assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
 target (e.g., a previously declared variable, an object property, or a [destructuring pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
). Variables declared with `var` are not local to the loop, i.e., they are in the same scope the `for await...of` loop is in.

[`iterable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#iterable)

An async iterable or sync iterable. The source of the sequence of values on which the loop operates.

[`statement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#statement)

A statement to be executed on every iteration. May reference `variable`. You can use a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 to execute multiple statements.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#description)

-----------------------------------------------------------------------------------------------------------------------

When a `for await...of` loop iterates over an iterable, it first gets the iterable's [`[Symbol.asyncIterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncIterator)
 method and calls it, which returns an [async iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols)
. If the `@asyncIterator` method does not exist, it then looks for a [`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)
 method, which returns a [sync iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
. The sync iterator returned is then wrapped into an async iterator by wrapping every object returned from the `next()`, `return()`, and `throw()` methods into a resolved or rejected promise, with the `value` property resolved if it's also a promise. The loop then repeatedly calls the final async iterator's [`next()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 method and [awaits](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 the returned promise, producing the sequence of values to be assigned to `variable`.

A `for await...of` loop exits when the iterator has completed (the awaited `next()` result is an object with `done: true`). Like other looping statements, you can use [control flow statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#control_flow)
 inside `statement`:

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
     stops `statement` execution and goes to the first statement after the loop.
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
     stops `statement` execution and goes to the next iteration of the loop.

If the `for await...of` loop exited early (e.g., a `break` statement is encountered or an error is thrown), the [`return()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 method of the iterator is called to perform any cleanup. The returned promise is awaited before the loop exits.

`for await...of` generally functions the same as the [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loop and shares many of the same syntax and semantics. There are a few differences:

*   `for await...of` works on both sync and async iterables, while `for...of` only works on sync iterables.
*   `for await...of` can only be used in contexts where [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
     can be used, which includes inside an [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
     body and in a [module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    . Even when the iterable is sync, the loop still awaits the return value for every iteration, leading to slower execution due to repeated promise unwrapping.
*   If the `iterable` is a sync iterable that yields promises, `for await...of` would produce a sequence of resolved values, while `for...of` would produce a sequence of promises.
*   For `for await...of`, the `variable` can be the identifier `async` (e.g., `for await (async of foo)`); `for...of` forbids this case.

Like `for...of`, if you use a `using` declaration, then the variable cannot be called `of`:

This is to avoid syntax ambiguity with the valid code `for await (using of [])`, before `using` was introduced.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#examples)

-----------------------------------------------------------------------------------------------------------------

### [Iterating over async iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#iterating_over_async_iterables)

You can also iterate over an object that explicitly implements async iterable protocol:

### [Iterating over async generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#iterating_over_async_generators)

Since the return values of async generator functions conform to the async iterable protocol, they can be looped using `for await...of`.

For a more concrete example of iterating over an async generator using `for await...of`, consider iterating over data from an API.

This example first creates an async iterable for a stream of data, then uses it to find the size of the response from the API.

### [Iterating over sync iterables and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#iterating_over_sync_iterables_and_generators)

`for await...of` loop also consumes sync iterables and generators. In that case it internally awaits emitted values before assign them to the loop control variable.

If a sync generator yields a rejected promise, `for await...of` calls the generator's [`return()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator/return)
 method before throwing the rejection reason, allowing `finally` blocks within that generator to run.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-for-in-and-for-of-statements](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-for-in-and-for-of-statements) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`Symbol.asyncIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncIterator)
    
*   [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/for-await...of/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/for-await...of (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor-await...of&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffor-await...of%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor-await...of%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffor-await...of%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff34bebcf0fec2d69b96bb313c37f7e67b0355830%0A*+Document+last+modified%3A+2026-09-03T07%3A41%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")