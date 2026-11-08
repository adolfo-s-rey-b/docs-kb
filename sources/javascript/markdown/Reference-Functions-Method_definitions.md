*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#mdn-search)
    

Method definitions
==================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Method definition** is a shorter syntax for defining a function property in an object initializer. It can also be used in [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#try_it)

----------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#syntax)

----------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#description)

--------------------------------------------------------------------------------------------------------------------------

The shorthand syntax is similar to the [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 and [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 syntax.

Given the following code:

You are now able to shorten this to:

Properties defined using this syntax are own properties of the created object, and they are configurable, enumerable, and writable, just like normal properties.

[`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
, [`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
, and [`async function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function*)
 properties all have their respective method syntaxes; see examples below.

However, note that the method syntax is not equivalent to a normal property with a function as its value — there are semantic differences. This makes methods defined in object literals more consistent with methods in [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
.

### [Method definitions are not constructable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#method_definitions_are_not_constructable)

Methods cannot be constructors! They will throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 if you try to instantiate them. On the other hand, a property created as a function can be used as a constructor.

### [Using super in method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#using_super_in_method_definitions)

Only functions defined as methods have access to the [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 keyword. `super.prop` looks up the property on the prototype of the object that the method was initialized on.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#examples)

--------------------------------------------------------------------------------------------------------------------

### [Using method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#using_method_definitions)

### [Method definitions in classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#method_definitions_in_classes)

You can use the exact same syntax to define public instance methods that are available on class instances. In classes, you don't need the comma separator between methods.

Public instance methods are defined on the `prototype` property of the class and are thus shared by all instances of the class. They are writable, non-enumerable, and configurable.

Inside instance methods, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 and [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 work like in normal methods. Usually, `this` refers to the instance itself. In subclasses, `super` lets you access the prototype of the object that the method is attached to, allowing you to call methods from the superclass.

Static methods and private methods use similar syntaxes, which are described in the [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 and [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 pages.

### [Computed property names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#computed_property_names)

The method syntax also supports [computed property names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names)
.

### [Generator methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#generator_methods)

Note that the asterisk (`*`) in the generator method syntax must be _before_ the generator property name. (That is, `* g(){}` will work, but `g *(){}` will not.)

### [Async methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#async_methods)

### [Async generator methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#async_generator_methods)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-method-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-method-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [`get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
    
*   [`set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
    
*   [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/functions/method_definitions/index.md?plain=1 "Folder: en-us/web/javascript/reference/functions/method_definitions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2FMethod_definitions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Fmethod_definitions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2FMethod_definitions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Fmethod_definitions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")