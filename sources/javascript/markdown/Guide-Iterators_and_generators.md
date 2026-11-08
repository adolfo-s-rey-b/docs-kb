*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#mdn-search)
    

Iterators and generators
========================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management)
    

Iterators and Generators bring the concept of iteration directly into the core language and provide a mechanism for customizing the behavior of [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loops.

For details, see also:

*   [Iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
    
*   [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
    
*   [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
     and [`Generator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)
    
*   [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
     and [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
    

[Iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#iterators)

--------------------------------------------------------------------------------------------------------------

In JavaScript an **iterator** is an object which defines a sequence and potentially a return value upon its termination.

Specifically, an iterator is any object which implements the [Iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol)
 by having a `next()` method that returns an object with two properties:

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#value)

The next value in the iteration sequence.

[`done`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#done)

This is `true` if the last value in the sequence has already been consumed. If `value` is present alongside `done`, it is the iterator's return value.

Once created, an iterator object can be iterated explicitly by repeatedly calling `next()`. Iterating over an iterator is said to consume the iterator, because it is generally only possible to do once. After a terminating value has been yielded additional calls to `next()` should continue to return `{done: true}`.

The most common iterator in JavaScript is the Array iterator, which returns each value in the associated array in sequence.

While it is easy to imagine that all iterators could be expressed as arrays, this is not true. Arrays must be allocated in their entirety, but iterators are consumed only as necessary. Because of this, iterators can express sequences of unlimited size, such as the range of integers between `0` and [`Infinity`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity)
.

Here is an example which can do just that. It allows creation of a range iterator which defines a sequence of integers from `start` (inclusive) to `end` (exclusive) spaced `step` apart. Its final return value is the size of the sequence it created, tracked by the variable `iterationCount`.

Using the iterator then looks like this:

**Note:** It is not possible to know reflectively whether a particular object is an iterator. If you need to do this, use [Iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#iterables)
.

[Generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#generator_functions)

----------------------------------------------------------------------------------------------------------------------------------

While custom iterators are a useful tool, their creation requires careful programming due to the need to explicitly maintain their internal state. **Generator functions** provide a powerful alternative: they allow you to define an iterative algorithm by writing a single function whose execution is not continuous. Generator functions are written using the [`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
 syntax.

When called, generator functions do not initially execute their code. Instead, they return a special type of iterator, called a **Generator**. When a value is consumed by calling the generator's `next` method, the Generator function executes until it encounters the `yield` keyword.

The function can be called as many times as desired, and returns a new Generator each time. Each Generator may only be iterated once.

We can now adapt the example from above. The behavior of this code is identical, but the implementation is much easier to write and read.

[Iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#iterables)

--------------------------------------------------------------------------------------------------------------

An object is **iterable** if it defines its iteration behavior, such as what values are looped over in a [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 construct. Some built-in types, such as [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 or [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
, have a default iteration behavior, while other types (such as [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
) do not.

In order to be **iterable**, an object must implement the `[Symbol.iterator]()` method. This means that the object (or one of the objects up its [prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
) must have a property with a [`Symbol.iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)
 key.

It may be possible to iterate over an iterable more than once, or only once. It is up to the programmer to know which is the case.

Iterables which can iterate only once (such as Generators) customarily return `this` from their `[Symbol.iterator]()` method, whereas iterables which can be iterated many times must return a new iterator on each invocation of `[Symbol.iterator]()`.

### [User-defined iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#user-defined_iterables)

You can make your own iterables like this:

User-defined iterables can be used in `for...of` loops or the spread syntax as usual.

### [Built-in iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#built-in_iterables)

[`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
, [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
, [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
, [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 and [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
 are all built-in iterables, because their prototype objects all have a [`Symbol.iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)
 method.

### [Syntaxes expecting iterables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#syntaxes_expecting_iterables)

Some statements and expressions expect iterables. For example: the [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loops, [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
, [`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)
, and [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
 syntax.

[Advanced generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators#advanced_generators)

----------------------------------------------------------------------------------------------------------------------------------

Generators compute their `yield`ed values _on demand_, which allows them to efficiently represent sequences that are expensive to compute (or even infinite sequences, as demonstrated above).

The [`next()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator/next)
 method also accepts a value, which can be used to modify the internal state of the generator. A value passed to `next()` will be received by `yield`.

**Note:** A value passed to the _first_ invocation of `next()` is always ignored.

Here is the fibonacci generator using `next(x)` to restart the sequence:

You can force a generator to throw an exception by calling its [`throw()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator/throw)
 method and passing the exception value it should throw. This exception will be thrown from the current suspended context of the generator, as if the `yield` that is currently suspended were instead a `throw value` statement.

If the exception is not caught from within the generator, it will propagate up through the call to `throw()`, and subsequent calls to `next()` will result in the `done` property being `true`.

Generators have a [`return()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator/return)
 method that returns the given value and finishes the generator itself.

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/iterators_and_generators/index.md?plain=1 "Folder: en-us/web/javascript/guide/iterators_and_generators (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FIterators_and_generators&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fiterators_and_generators%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FIterators_and_generators%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fiterators_and_generators%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1474534461893381d54c502e655f334b5568e597%0A*+Document+last+modified%3A+2026-08-21T19%3A37%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")