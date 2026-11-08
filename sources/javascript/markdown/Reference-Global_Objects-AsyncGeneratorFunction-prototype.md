*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/prototype#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/prototype#mdn-search)
    

AsyncGeneratorFunction.prototype.prototype
==========================================

The **`prototype`** property of `AsyncGeneratorFunction.prototype` is shared by all async generator functions. Its value is [`AsyncGenerator.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator)
. Each async generator function created with the `async function*` syntax or the `AsyncGeneratorFunction()` constructor also has its own `prototype` property, whose prototype is `AsyncGeneratorFunction.prototype.prototype`. When the async generator function is called, its `prototype` property becomes the prototype of the returned async generator object.

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/prototype#value)

---------------------------------------------------------------------------------------------------------------------------------

The same object as [`AsyncGenerator.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator)
. `AsyncGeneratorFunction.prototype.prototype` is the technically more accurate name, but `AsyncGenerator.prototype` appeals to the intuition that it's the prototype of async generator objects.

|     |     |
| --- | --- |
| Writable | no  |
| Enumerable | no  |
| Configurable | yes |

The `prototype` property of each `AsyncGeneratorFunction` instance is an empty object with no properties, whose prototype is `AsyncGeneratorFunction.prototype.prototype`. It has the following property attributes:

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | no  |
| Configurable | no  |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/prototype#description)

---------------------------------------------------------------------------------------------------------------------------------------------

An async generator function instance has two `prototype` properties. The first one is its own `prototype` property. The second one is the `prototype` property on its prototype, which is `AsyncGeneratorFunction.prototype`. (Remember that every async generator function is an instance of `AsyncGeneratorFunction`, so it has `AsyncGeneratorFunction.prototype` as its prototype.)

When an async generator function is called, the async generator function's `prototype` property becomes the prototype of the returned async generator object.

The following diagram illustrates the prototype chain of an async generator function and its instances. Each hollow arrow indicates an inheritance relationship (i.e., a prototype link), and each solid arrow indicates a property relationship. Note that there's no way to access `genFunc` from `gen` — they only have an `instanceof` relationship.

![The inheritance diagram of async generators and async generator functions](https://mdn.github.io/shared-assets/images/diagrams/javascript/asyncgeneratorfunction/prototype-chain.svg)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/prototype#specifications)

---------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-asyncgeneratorfunction-prototype-prototype](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-asyncgeneratorfunction-prototype-prototype) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-asyncgeneratorfunction-instances-prototype](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-asyncgeneratorfunction-instances-prototype) |

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/prototype#see_also)

---------------------------------------------------------------------------------------------------------------------------------------

*   [`async function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
    
*   [`async function*` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function*)
    
*   [`AsyncGeneratorFunction`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction)
    
*   [`GeneratorFunction`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction)
    
*   [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
    
*   [Iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGeneratorFunction/prototype/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/asyncgeneratorfunction/prototype/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/asyncgeneratorfunction/prototype (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAsyncGeneratorFunction%2Fprototype&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fasyncgeneratorfunction%2Fprototype%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FAsyncGeneratorFunction%2Fprototype%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fasyncgeneratorfunction%2Fprototype%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")