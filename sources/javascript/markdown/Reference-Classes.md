*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#mdn-search)
    

Classes
=======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

Classes are a template for creating objects. They encapsulate data with code to work on that data. Classes in JS are built on [prototypes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 but also have some syntax and semantics that are unique to classes.

For more examples and explanations, see the [Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
 guide.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#description)

-----------------------------------------------------------------------------------------------------

### [Defining classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#defining_classes)

Classes are in fact "special [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
", and just as you can define [function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
 and [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
, a class can be defined in two ways: a [class expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class)
 or a [class declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
.

Like function expressions, class expressions may be anonymous, or have a name that's different from the variable that it's assigned to. However, unlike function declarations, class declarations have the same [temporal dead zone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz)
 restrictions as `let` or `const` and behave as if they are [not hoisted](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#class_declaration_hoisting)
.

### [Class body](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#class_body)

The body of a class is the part that is in curly braces `{}`. This is where you define class members, such as methods or constructor.

The body of a class is executed in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 even without the `"use strict"` directive.

A class element can be characterized by three aspects:

*   Kind: Getter, setter, method, or field
*   Location: Static or instance
*   Visibility: Public or private

Together, they add up to 16 possible combinations. To divide the reference more logically and avoid overlapping content, the different elements are introduced in detail in different pages:

[Method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)

Public instance method

[getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)

Public instance getter

[setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)

Public instance setter

[Public class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)

Public instance field

[`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)

Public static method, getter, setter, and field

[Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)

Everything that's private

**Note:** Private elements have the restriction that all private names declared in the same class must be unique, except for a getter/setter pair where both are static or both are instance. All other public properties do not have this restriction — you can have multiple public properties with the same name, and the last one overwrites the others. This is the same behavior as in [object initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#duplicate_property_names)
.

In addition, there are two special class element syntaxes: [`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#constructor)
 and [static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#static_initialization_blocks)
, with their own references.

#### Constructor

The [`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
 method is a special method for creating and initializing an object created with a class. There can only be one special method with the name "constructor" in a class — a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
 is thrown if the class contains more than one occurrence of a `constructor` method.

A constructor can use the [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 keyword to call the constructor of the super class.

You can create instance properties inside the constructor:

Alternatively, if your instance properties' values do not depend on the constructor's arguments, you can define them as [class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#field_declarations)
.

#### Static initialization blocks

[Static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
 allow flexible initialization of [static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#static_methods_and_fields)
, including the evaluation of statements during initialization, while granting access to the private scope.

Multiple static blocks can be declared, and these can be interleaved with the declaration of static fields and methods (all static items are evaluated in declaration order).

#### Methods

Methods are defined on the prototype of each class instance and are shared by all instances. Methods can be plain functions, async functions, generator functions, or async generator functions. For more information, see [method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
.

#### Static methods and fields

The [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 keyword defines a static method or field for a class. Static properties (fields and methods) are defined on the class itself instead of each instance. Static methods are often used to create utility functions for an application, whereas static fields are useful for caches, fixed-configuration, or any other data that doesn't need to be replicated across instances.

#### Field declarations

With the class field declaration syntax, the [constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#constructor)
 example can be written as:

Class fields are similar to object properties, not variables, so we don't use keywords such as `const` to declare them. In JavaScript, [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#private_elements)
 use a special identifier syntax, so modifier keywords like `public` and `private` should not be used either.

As seen above, the fields can be declared with or without a default value. Fields without default values default to `undefined`. By declaring fields up-front, class definitions become more self-documenting, and the fields are always present, which help with optimizations.

See [public class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
 for more information.

#### Private elements

Using private fields, the definition can be refined as below.

It's an error to reference private fields from outside of the class; they can only be read or written within the class body. By defining things that are not visible outside of the class, you ensure that your classes' users can't depend on internals, which may change from version to version.

Private fields can only be declared up-front in a field declaration. They cannot be created later through assigning to them, the way that normal properties can.

Private methods and accessors can also be defined using the same syntax as their public counterparts, but with the identifier starting with `#`.

For more information, see [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
.

### [Inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#inheritance)

The [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
 keyword is used in _class declarations_ or _class expressions_ to create a class as a child of another constructor (either a class or a function).

If there is a constructor present in the subclass, it needs to first call `super()` before using `this`. The [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 keyword can also be used to call corresponding methods of super class.

### [Evaluation order](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#evaluation_order)

When a [`class` declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
 or [`class` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class)
 is evaluated, its various components are evaluated in the following order:

1.  The [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
     clause, if present, is first evaluated. It must evaluate to a valid constructor function or `null`, or a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
     is thrown.
2.  The [`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
     method is extracted, substituted with a default implementation if `constructor` is not present. However, because the `constructor` definition is only a method definition, this step is not observable.
3.  The class elements' property keys are evaluated in the order of declaration. If the property key is computed, the computed expression is evaluated, with the `this` value set to the `this` value surrounding the class (not the class itself). None of the property values are evaluated yet.
4.  Methods and accessors are installed in the order of declaration. Instance methods and accessors are installed on the `prototype` property of the current class, and static methods and accessors are installed on the class itself. Private instance methods and accessors are saved to be installed on the instance directly later. This step is not observable.
5.  The class is now initialized with the prototype specified by `extends` and implementation specified by `constructor`. For all steps above, if an evaluated expression tries to access the name of the class, a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
     is thrown because the class is not initialized yet.
6.  The class elements' values are evaluated in the order of declaration:
    *   For each [instance field](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
         (public or private), its initializer expression is saved. The initializer is evaluated during instance creation, at the start of the constructor (for base classes) or immediately before the `super()` call returns (for derived classes).
    *   For each [static field](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
         (public or private), its initializer is evaluated with `this` set to the class itself, and the property is created on the class.
    *   [Static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
         are evaluated with `this` set to the class itself.
7.  The class is now fully initialized and can be used as a constructor function.

For how instances are created, see the [`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
 reference.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#examples)

-----------------------------------------------------------------------------------------------

### [Binding this with instance and static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#binding_this_with_instance_and_static_methods)

When a static or instance method is called without a value for [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
, such as by assigning the method to a variable and then calling it, the `this` value will be `undefined` inside the method. This behavior is the same even if the [`"use strict"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 directive isn't present, because code within the `class` body is always executed in strict mode.

If we rewrite the above using traditional function-based syntax in non–strict mode, then `this` method calls are automatically bound to [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
. In strict mode, the value of `this` remains as `undefined`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-class-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-class-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#see_also)

-----------------------------------------------------------------------------------------------

*   [Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
     guide
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [`class` expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class)
    
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [ES6 In Depth: Classes](https://hacks.mozilla.org/2015/07/es6-in-depth-classes/ "External link (opens in new tab)")
     on hacks.mozilla.org (2015)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/classes/index.md?plain=1 "Folder: en-us/web/javascript/reference/classes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fclasses%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")