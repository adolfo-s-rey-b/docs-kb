*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#mdn-search)
    

set
===

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`set`** syntax binds an object property to a function to be called when there is an attempt to set that property. It can also be used in [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#try_it)

-------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#syntax)

-------------------------------------------------------------------------------------------------

There are some additional syntax restrictions:

*   A setter must have exactly one parameter.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#parameters)

[`prop`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#prop)

The name of the property to bind to the given function. In the same way as other properties in [object initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
, it can be a string literal, a number literal, or an identifier.

[`val`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#val)

An alias for the variable that holds the value attempted to be assigned to `prop`.

[`expression`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#expression)

You can also use expressions for a computed property name to bind to the given function.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#description)

-----------------------------------------------------------------------------------------------------------

In JavaScript, a setter can be used to execute a function whenever an attempt is made to change a property's value. Setters are most often used in conjunction with getters.

An object property is either a data property or an accessor property, but it cannot simultaneously be both. Read [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 for more information. The setter syntax allows you to specify the setter function in an object initializer.

Properties defined using this syntax are own properties of the created object, and they are configurable and enumerable.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#examples)

-----------------------------------------------------------------------------------------------------

### [Defining a setter on new objects in object initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#defining_a_setter_on_new_objects_in_object_initializers)

The following example defines a pseudo-property `current` of object `language`. When `current` is assigned a value, it updates `log` with that value:

Note that `current` has no getter, and any attempts to access it will result in `undefined`.

### [Using setters in classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#using_setters_in_classes)

You can use the exact same syntax to define public instance setters that are available on class instances. In classes, you don't need the comma separator between methods.

Setter properties are defined on the `prototype` property of the class and are thus shared by all instances of the class. Unlike setter properties in object literals, setter properties in classes are not enumerable.

Static setters and private setters use similar syntaxes, which are described in the [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 and [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 pages.

### [Removing a setter with the `delete` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#removing_a_setter_with_the_delete_operator)

If you want to remove the setter, you can just [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
 it:

### [Defining a setter on existing objects using `defineProperty`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#defining_a_setter_on_existing_objects_using_defineproperty)

To append a setter to an _existing_ object, use [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
.

### [Using a computed property name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#using_a_computed_property_name)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-method-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-method-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set#see_also)

-----------------------------------------------------------------------------------------------------

*   [Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [`get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
    
*   [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
    
*   [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [Property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
    
*   [Incompatible ES5 change: literal getter and setter functions must now have exactly zero or one arguments](https://whereswalden.com/2010/08/22/incompatible-es5-change-literal-getter-and-setter-functions-must-now-have-exactly-zero-or-one-arguments/ "External link (opens in new tab)")
     by Jeff Walden (2010)
*   [More SpiderMonkey changes: ancient, esoteric, very rarely used syntax for creating getters and setters is being removed](https://whereswalden.com/2010/04/16/more-spidermonkey-changes-ancient-esoteric-very-rarely-used-syntax-for-creating-getters-and-setters-is-being-removed/ "External link (opens in new tab)")
     by Jeff Walden (2010)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/functions/set/index.md?plain=1 "Folder: en-us/web/javascript/reference/functions/set (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Fset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Fset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Fset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Fset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")