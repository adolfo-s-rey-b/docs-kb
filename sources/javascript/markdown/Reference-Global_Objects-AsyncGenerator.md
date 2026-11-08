*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#mdn-search)
    

AsyncGenerator
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`AsyncGenerator`** object is returned by an [async generator function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
 and it conforms to both the [async iterable protocol and the async iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_async_iterator_and_async_iterable_protocols)
.

Async generator methods always yield [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 objects.

`AsyncGenerator` is a subclass of the hidden [`AsyncIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)
 class.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#constructor)

---------------------------------------------------------------------------------------------------------------------------

There's no JavaScript entity that corresponds to the `AsyncGenerator` constructor. Instances of `AsyncGenerator` must be returned from [async generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
:

There's only a hidden object which is the prototype object shared by all objects created by async generator functions. This object is often stylized as `AsyncGenerator.prototype` to make it look like a class, but it should be more appropriately called [`AsyncGeneratorFunction.prototype.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/prototype)
, because `AsyncGeneratorFunction` is an actual JavaScript entity. To understand the prototype chain of `AsyncGenerator` instances, see [`AsyncGeneratorFunction.prototype.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/prototype)
.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#instance_properties)

-------------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `AsyncGenerator.prototype` and shared by all `AsyncGenerator` instances.

[`AsyncGenerator.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `AsyncGenerator` instances, the initial value is [`AsyncGeneratorFunction.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction)
.

**Note:** `AsyncGenerator` objects do not store a reference to the async generator function that created them.

[`AsyncGenerator.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#asyncgenerator.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"AsyncGenerator"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#instance_methods)

-------------------------------------------------------------------------------------------------------------------------------------

_Also inherits instance methods from its parent [`AsyncIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)
_.

[`AsyncGenerator.prototype.next()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator/next)

Returns a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 which will be resolved with the given value yielded by the [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
 expression.

[`AsyncGenerator.prototype.return()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator/return)

Acts as if a `return` statement is inserted in the generator's body at the current suspended position, which finishes the generator and allows the generator to perform any cleanup tasks when combined with a [`try...finally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#the_finally_block)
 block.

[`AsyncGenerator.prototype.throw()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator/throw)

Acts as if a `throw` statement is inserted in the generator's body at the current suspended position, which informs the generator of an error condition and allows it to handle the error, or perform cleanup and close itself.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#examples)

---------------------------------------------------------------------------------------------------------------------

### [Async generator iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#async_generator_iteration)

The following example iterates over an async generator, logging values 1–6 to the console at decreasing time intervals. Notice how each time a Promise is yielded, but it's automatically resolved within the `for await...of` loop.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-asyncgenerator-objects](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-asyncgenerator-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [function\*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    
*   [async function\*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
    
*   [`function*` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function*)
    
*   [Generator Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction)
    
*   [Async Generator Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction)
    
*   [Iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
     guide

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/asyncgenerator/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/asyncgenerator (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAsyncGenerator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fasyncgenerator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAsyncGenerator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fasyncgenerator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")