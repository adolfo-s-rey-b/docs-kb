*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#mdn-search)
    

for...of
========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`for...of`** statement executes a loop that operates on a sequence of values sourced from an [iterable object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
. Iterable objects include instances of built-ins such as [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
, [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
, [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
, [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
, [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
, [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)
 (and other DOM collections), as well as the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object, [generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
 produced by [generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
, and user-defined iterables.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#try_it)

-------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#syntax)

-------------------------------------------------------------------------------------------------------

[`variable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#variable)

Receives a value from the sequence on each iteration. May be either a declaration with [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
, [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
, [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
, [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
, or an [assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)
 target (e.g., a previously declared variable, an object property, or a [destructuring pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
). Variables declared with `var` are not local to the loop, i.e., they are in the same scope the `for...of` loop is in.

[`iterable`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterable)

An iterable object. The source of the sequence of values on which the loop operates.

[`statement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#statement)

A statement to be executed on every iteration. May reference `variable`. You can use a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 to execute multiple statements.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#description)

-----------------------------------------------------------------------------------------------------------------

A `for...of` loop operates on the values sourced from an iterable one by one in sequential order. Each operation of the loop on a value is called an _iteration_, and the loop is said to _iterate over the iterable_. Each iteration executes statements that may refer to the current sequence value.

When a `for...of` loop iterates over an iterable, it first calls the iterable's [`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)
 method, which returns an [iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
, and then repeatedly calls the resulting iterator's [`next()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 method to produce the sequence of values to be assigned to `variable`.

A `for...of` loop exits when the iterator has completed (the `next()` result is an object with `done: true`). Like other looping statements, you can use [control flow statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#control_flow)
 inside `statement`:

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
     stops `statement` execution and goes to the first statement after the loop.
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
     stops `statement` execution and goes to the next iteration of the loop.

If the `for...of` loop exited early (e.g., a `break` statement is encountered or an error is thrown), the [`return()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 method of the iterator is called to perform any cleanup.

The `variable` part of `for...of` accepts anything that can come before the `=` operator. You can use [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
 to declare the variable as long as it's not reassigned within the loop body (it can change between iterations, because those are two separate variables). Otherwise, you can use [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
.

**Note:** Each iteration creates a new variable. Reassigning the variable inside the loop body does not affect the original value in the iterable (an array, in this case).

Variables declared using the [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 or [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
 declaration are disposed every time a loop iteration is done (and `await using` causes an implicit `await` at the end of the iteration). However, if the loop early-exits, any values left in the iterator that haven't been visited are not disposed (although the current value is).

You can use [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 to assign multiple local variables, or use a property accessor like `for (x.y of iterable)` to assign the value to an object property.

However, a special rule forbids using `async` as the variable name. This is invalid syntax:

This is to avoid syntax ambiguity with the valid code `for (async of => {};;)`, which is a [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
 loop.

Similarly, if you use the `using` declaration, then the variable cannot be called `of`:

This is to avoid syntax ambiguity with the valid code `for (using of [])`, before `using` was introduced.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#examples)

-----------------------------------------------------------------------------------------------------------

### [Iterating over an Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterating_over_an_array)

### [Iterating over a string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterating_over_a_string)

Strings are [iterated by Unicode code points](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Symbol.iterator)
.

### [Iterating over a TypedArray](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterating_over_a_typedarray)

### [Iterating over a Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterating_over_a_map)

### [Iterating over a Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterating_over_a_set)

### [Iterating over the arguments object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterating_over_the_arguments_object)

You can iterate over the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object to examine all parameters passed into a function.

### [Iterating over a NodeList](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterating_over_a_nodelist)

The following example adds a `read` class to paragraphs that are direct descendants of the [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 element by iterating over a [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)
 DOM collection.

### [Iterating over a user-defined iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterating_over_a_user-defined_iterable)

Iterating over an object with a `[Symbol.iterator]()` method that returns a custom iterator:

Iterating over an object with a `[Symbol.iterator]()` generator method:

_Iterable iterators_ (iterators with a `[Symbol.iterator]()` method that returns `this`) are a fairly common technique to make iterators usable in syntaxes expecting iterables, such as `for...of`.

### [Iterating over a generator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#iterating_over_a_generator)

### [Early exiting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#early_exiting)

Execution of the `break` statement in the first loop causes it to exit early. The iterator is not finished yet, so the second loop will continue from where the first one stopped at.

Generators implement the [`return()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator/return)
 method, which causes the generator function to early return when the loop exits. This makes generators not reusable between loops.

### [Difference between for...of and for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#difference_between_for...of_and_for...in)

Both `for...in` and `for...of` statements iterate over something. The main difference between them is in what they iterate over.

The [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 statement iterates over the [enumerable string properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
 of an object, while the `for...of` statement iterates over values that the [iterable object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)
 defines to be iterated over.

The following example shows the difference between a `for...of` loop and a `for...in` loop when used with an [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
.

The object `iterable` inherits the properties `objCustom` and `arrCustom` because it contains both `Object.prototype` and `Array.prototype` in its [prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
.

The `for...in` loop logs only [enumerable properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
 of the `iterable` object. It doesn't log array _elements_ `3`, `5`, `7` or `"hello"` because those are not _properties_ — they are _values_. It logs array _indexes_ as well as `arrCustom` and `objCustom`, which are actual properties. If you're not sure why these properties are iterated over, there's a more thorough explanation of how [array iteration and `for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in#array_iteration_and_for...in)
 work.

The second loop is similar to the first one, but it uses [`Object.hasOwn()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
 to check if the found enumerable property is the object's own, i.e., not inherited. If it is, the property is logged. Properties `0`, `1`, `2` and `foo` are logged because they are own properties. Properties `arrCustom` and `objCustom` are not logged because they are inherited.

The `for...of` loop iterates and logs _values_ that `iterable`, as an array (which is [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.iterator)
), defines to be iterated over. The object's _elements_ `3`, `5`, `7` are shown, but none of the object's _properties_ are.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-for-in-and-for-of-statements](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-for-in-and-for-of-statements) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
    
*   [`Map.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach)
    
*   [`Object.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 30, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/for...of/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/for...of (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor...of&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffor...of%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor...of%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Ffor...of%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")