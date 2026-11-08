*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript#mdn-search)
    

JavaScript
==========

**JavaScript** (**JS**) is a lightweight interpreted (or [just-in-time compiled](https://developer.mozilla.org/en-US/docs/Glossary/Just_In_Time_Compilation)
) programming language with [first-class functions](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function)
. While it is most well-known as the scripting language for Web pages, [many non-browser environments](https://en.wikipedia.org/wiki/JavaScript#Other_usage "External link (opens in new tab)")
 also use it, such as [Node.js](https://developer.mozilla.org/en-US/docs/Glossary/Node.js)
, [Apache CouchDB](https://couchdb.apache.org/ "External link (opens in new tab)")
 and [Adobe Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/ "External link (opens in new tab)")
. JavaScript is a [prototype-based](https://developer.mozilla.org/en-US/docs/Glossary/Prototype-based_programming)
, [garbage-collected](https://developer.mozilla.org/en-US/docs/Glossary/Garbage_collection)
, [dynamic](https://developer.mozilla.org/en-US/docs/Glossary/Dynamic_typing)
 language, supporting multiple paradigms such as imperative, functional, and object-oriented.

JavaScript's dynamic capabilities include runtime object construction, variable parameter lists, function variables, dynamic script creation (via [`eval`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
), object introspection (via [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 and [`Object` utilities](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#static_methods)
), and source-code recovery (JavaScript functions store their source text and can be retrieved through [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/toString)
).

This section is dedicated to the JavaScript language itself, and not the parts that are specific to Web pages or other host environments. For information about [APIs](https://developer.mozilla.org/en-US/docs/Glossary/API)
 that are specific to Web pages, please see [Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
 and [DOM](https://developer.mozilla.org/en-US/docs/Glossary/DOM)
.

The standards for JavaScript are the [ECMAScript Language Specification](https://tc39.es/ecma262/ "External link (opens in new tab)")
 (ECMA-262) and the [ECMAScript Internationalization API specification](https://tc39.es/ecma402/ "External link (opens in new tab)")
 (ECMA-402). As soon as one browser implements a feature, we try to document it. This means that cases where some [proposals for new ECMAScript features](https://github.com/tc39/proposals "External link (opens in new tab)")
 have already been implemented in browsers, documentation and examples in MDN articles may use some of those new features. Most of the time, this happens between the [stages](https://tc39.es/process-document/ "External link (opens in new tab)")
 3 and 4, and is usually before the spec is officially published.

Do not confuse JavaScript with the [Java programming language](https://en.wikipedia.org/wiki/Java_(programming_language) "External link (opens in new tab)")
 — **JavaScript is _not_ "Interpreted Java"**. Both "Java" and "JavaScript" are trademarks or registered trademarks of Oracle in the U.S. and other countries. However, the two programming languages have very different syntax, semantics, and use.

JavaScript documentation of core language features (pure [ECMAScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview)
, for the most part) includes the following:

*   The [JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
    
*   The [JavaScript reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
    

For more information about JavaScript specifications and related technologies, see [JavaScript technologies overview](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview)
.

[Beginner's tutorials](https://developer.mozilla.org/en-US/docs/Web/JavaScript#beginners_tutorials)

----------------------------------------------------------------------------------------------------

Our [learn web development core modules](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core)
 contain modern, up-to-date tutorials covering JavaScript fundamentals.

[Your first website: Adding interactivity](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)

This article provides a brief tour of what JavaScript is and how to use it, aimed at people who are completely new to web development.

[Dynamic scripting with JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting)

This module focuses on the essentials of the core JavaScript language, plus some key surrounding topics — learning these topics will give you a solid basis to work from.

[JavaScript frameworks and libraries](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Frameworks_libraries)

JavaScript frameworks are an essential part of modern front-end web development, providing developers with tried and tested tools for building scalable, interactive web applications. Many modern companies use frameworks as a standard part of their tooling, so many front-end development jobs now require framework experience. This set of articles provides a comfortable starting point to help you begin learning frameworks.

[JavaScript guides](https://developer.mozilla.org/en-US/docs/Web/JavaScript#javascript_guides)

-----------------------------------------------------------------------------------------------

### [Fundamental language guides](https://developer.mozilla.org/en-US/docs/Web/JavaScript#fundamental_language_guides)

[JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)

A much more detailed guide to the JavaScript language, aimed at those with previous programming experience either in JavaScript or another language.

### [Intermediate](https://developer.mozilla.org/en-US/docs/Web/JavaScript#intermediate)

[Advanced JavaScript objects](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects)

The object-oriented nature of JavaScript is important to understand if you want to go further with your knowledge of the language and write more efficient code, therefore we've provided this module to help you.

[Asynchronous JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Async_JS)

In this module, we take a look at [asynchronous](https://developer.mozilla.org/en-US/docs/Glossary/Asynchronous)
 JavaScript, why it is important, and how it can be used to effectively handle potential blocking operations, such as fetching resources from a server.

[Client-side web APIs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs)

Explores what APIs are, and how to use some of the most common APIs you'll come across often in your development work.

[JavaScript language overview](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Language_overview)

An overview of the basic syntax and semantics of JavaScript for those coming from other programming languages to get up to speed.

[JavaScript data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)

Overview of available data structures in JavaScript.

[Equality comparisons and sameness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness)

JavaScript provides three different value comparison operations: strict equality using `===`, loose equality using `==`, and the [`Object.is()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is)
 method.

[Enumerability and ownership of properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)

How different methods that visit a group of object properties one-by-one handle the enumerability and ownership of properties.

[Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)

A closure is the combination of a function and the lexical environment within which that function was declared.

### [Advanced](https://developer.mozilla.org/en-US/docs/Web/JavaScript#advanced)

[Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)

Explanation of the widely misunderstood and underestimated prototype-based inheritance.

[Memory Management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management)

Memory life cycle and garbage collection in JavaScript.

[Agent communication and coordination](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Agent_communication_and_coordination)

Sharing memory and coordinating access with `SharedArrayBuffer`, `Atomics`, and `postMessage()`.

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript#reference)

-------------------------------------------------------------------------------

Browse the complete [JavaScript reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
 documentation.

[Standard objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)

Get to know standard built-in objects: [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
, [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
, [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
, [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
, [`JSON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
, [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
, [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
, [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
, [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
, [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
, [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
, [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
, [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
, [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
, and others.

[Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)

Learn more about the behavior of JavaScript's operators [`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
, [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
, [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
, the [operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
, and more.

[Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)

Learn how [`do-while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
, [`for-in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
, [`for-of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
, [`try-catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
, [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
, [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
, [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
, [`if-else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
, [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
, and more JavaScript statements and keywords work.

[Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)

Learn how to work with JavaScript's functions to develop your applications.

[Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)

JavaScript classes are the most appropriate way to do object-oriented programming.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/index.md?plain=1 "Folder: en-us/web/javascript (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9d64ff6c5d0eee1800b0d3b4f9076de65f34f5ce%0A*+Document+last+modified%3A+2026-10-28T18%3A50%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")