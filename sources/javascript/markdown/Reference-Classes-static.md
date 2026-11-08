*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#mdn-search)
    

static
======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`static`** keyword defines a [static method or field](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#static_methods_and_fields)
 for a class, or a [static initialization block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
 (see the link for more information about this usage). Static properties cannot be directly accessed on instances of the class. Instead, they're accessed on the class itself.

Static methods are often utility functions, such as functions to create or clone objects, whereas static properties are useful for caches, fixed-configuration, or any other data you don't need to be replicated across instances.

**Note:** In the context of classes, MDN Web Docs content uses the terms properties and [fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
 interchangeably.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#syntax)

--------------------------------------------------------------------------------------------------

There are some additional syntax restrictions:

*   The name of a static property (field or method) cannot be `prototype`.
*   The name of a class field (static or instance) cannot be `constructor`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#description)

------------------------------------------------------------------------------------------------------------

This page introduces public static properties of classes, which include static methods, static accessors, and static fields.

*   For private static features, see [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
    .
*   For instance features, see [method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
    , [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
    , [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
    , and [public class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
    .

Public static features are declared using the `static` keyword. They are added to the class constructor at the time of [class evaluation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#evaluation_order)
 using the [`[[DefineOwnProperty]]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/defineProperty)
 semantic (which is essentially [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
). They are accessed again from the class constructor.

Static methods are often utility functions, such as functions to create or clone instances. Public static fields are useful when you want a field to exist only once per class, not on every class instance you create. This is useful for caches, fixed-configuration, or any other data you don't need to be replicated across instances.

Static field names can be [computed](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names)
. The `this` value in the computed expression is the `this` surrounding the class definition, and referring to the class's name is a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
 because the class is not initialized yet. [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 and [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
 work as expected in this expression.

Static fields can have an initializer. Static fields without initializers are initialized to `undefined`. Public static fields are not reinitialized on subclasses, but can be accessed via the prototype chain.

In the field initializer, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 refers to the current class (which you can also access through its name), and [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 refers to the base class constructor.

The expression is evaluated synchronously. You cannot use [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 or [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
 in the initializer expression. (Think of the initializer expression as being implicitly wrapped in a function.)

Static field initializers and [static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
 are evaluated one-by-one. Field initializers can refer to field values above them, but not below them. All static methods are added beforehand and can be accessed, although calling them may not behave as expected if they refer to fields below the one being initialized.

**Note:** This is more important with [private static fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
, because accessing a non-initialized private field throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
, even if the private field is declared below. (If the private field is not declared, it would be an early [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.)

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#examples)

------------------------------------------------------------------------------------------------------

### [Using static members in classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#using_static_members_in_classes)

The following example demonstrates several things:

1.  How a static member (method or property) is defined on a class.
2.  That a class with a static member can be sub-classed.
3.  How a static member can and cannot be called.

### [Calling static members from another static method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#calling_static_members_from_another_static_method)

In order to call a static method or property within another static method of the same class, you can use the [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 keyword.

### [Calling static members from a class constructor and other methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#calling_static_members_from_a_class_constructor_and_other_methods)

Static members are not directly accessible using the [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 keyword from non-static methods. You need to call them using the class name: `CLASSNAME.STATIC_METHOD_NAME()` / `CLASSNAME.STATIC_PROPERTY_NAME` or by calling the method as a property of the `constructor`: `this.constructor.STATIC_METHOD_NAME()` / `this.constructor.STATIC_PROPERTY_NAME`

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-class-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-class-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static#see_also)

------------------------------------------------------------------------------------------------------

*   [Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
     guide
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [Static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/classes/static/index.md?plain=1 "Folder: en-us/web/javascript/reference/classes/static (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2Fstatic&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fstatic%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2Fstatic%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fstatic%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")