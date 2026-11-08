*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#mdn-search)
    

Private elements
================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Private elements** are counterparts of the regular class elements which are public, including [class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
, class methods, etc. Private elements get created by using a hash `#` prefix and cannot be legally referenced outside of the class. The privacy encapsulation of these class elements is enforced by JavaScript itself. The only way to access a private element is via [dot notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#dot_notation)
, and you can only do so within the class that defines the private element.

Private elements were not native to the language before this syntax existed. In prototypal inheritance, its behavior may be emulated with [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap#emulating_private_members)
 objects or [closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures#emulating_private_methods_with_closures)
, but they can't compare to the `#` syntax in terms of ergonomics.

**Note:** On MDN, we avoid using the term "private property". A [property](https://developer.mozilla.org/en-US/docs/Glossary/Property/JavaScript)
 in JavaScript has a string or symbol key, and has attributes like `writable`, `enumerable`, and `configurable`, but private elements have none. While private elements are accessed with the familiar dot notation, they cannot be [proxied](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
, enumerated, deleted, or interacted with using any [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
 method.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#syntax)

------------------------------------------------------------------------------------------------------------

There are some additional syntax restrictions:

*   All private identifiers declared within a class must be unique. The namespace is shared between static and instance elements. The only exception is when the two declarations define a getter-setter pair.
*   The private identifier cannot be `#constructor`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#description)

----------------------------------------------------------------------------------------------------------------------

Most class elements have their private counterparts:

*   Private fields
*   Private methods
*   Private static fields
*   Private static methods
*   Private getters
*   Private setters
*   Private static getters
*   Private static setters

These features are collectively called _private elements_. However, [constructors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
 cannot be private in JavaScript. To prevent classes from being constructed outside of the class, you have to [use a private flag](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#simulating_private_constructors)
.

Private elements are declared with **\# names** (pronounced "hash names"), which are identifiers prefixed with `#`. The hash prefix is an inherent part of the property name — you can draw relationship with the old underscore prefix convention `_privateField` — but it's not an ordinary string property, so you can't dynamically access it with the [bracket notation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#bracket_notation)
.

It is a syntax error to refer to `#` names from outside of the class. It is also a syntax error to refer to private elements that were not declared in the class body, or to attempt to remove declared elements with [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
.

JavaScript, being a dynamic language, is able to perform this compile-time check because of the special hash identifier syntax, making it different from normal properties on the syntax level.

**Note:** Code run in the Chrome console can access private elements outside the class. This is a DevTools-only relaxation of the JavaScript syntax restriction.

If you access a private element from an object that doesn't have the element, a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 is thrown, instead of returning `undefined` as normal properties do.

This example also illustrates that you can access private elements within static functions too, and on externally defined instances of the class.

You can use the [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 operator to check whether an externally defined object possesses a private element. This will return `true` if the private field or method exists, and `false` otherwise.

Note a corollary of private names being always pre-declared and non-deletable: if you found that an object possesses one private element of the current class (either from a `try...catch` or an `in` check), it must possess all other private elements. An object possessing the private elements of a class generally means it was constructed by that class (although [not always](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#returning_overriding_object)
).

Private elements are not part of the [prototypical inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 model since they can only be accessed within the current class's body and aren't inherited by subclasses. Private elements with the same name within different classes are entirely different and do not interoperate with each other. See them as external metadata attached to each instance, managed by the class. For this reason, [`structuredClone()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone "structuredClone()")
 does not clone private elements, and [`Object.freeze()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
 and [`Object.seal()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal)
 have no effect on private elements.

For more information on how and when private fields are initialized, see [public class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#examples)

----------------------------------------------------------------------------------------------------------------

### [Private fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#private_fields)

Private fields include private instance fields and private static fields. Private fields are only accessible from inside the class declaration.

#### Private instance fields

Like their public counterparts, private instance fields:

*   are added before the constructor runs in a base class, or immediately after [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
     is invoked in a subclass, and
*   are only available on instances of the class.

**Note:** `#privateField` from the `ClassWithPrivateField` base class is private to `ClassWithPrivateField` and is not accessible from the derived `Subclass`.

#### Returning overriding object

A class's constructor can return a different object, which will be used as the new `this` for the derived class constructor. The derived class may then define private fields on that returned object — meaning it is possible to "stamp" private fields onto unrelated objects.

**Warning:** This is a potentially very confusing thing to do. You are generally advised to avoid returning anything from the constructor — especially something unrelated to `this`.

#### Private static fields

Like their public counterparts, private static fields:

*   are added to the class constructor at class evaluation time, and
*   are only available on the class itself.

There is a restriction on private static fields: only the class which defines the private static field can access the field. This can lead to unexpected behavior when using [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
. In the following example, `this` refers to the `Subclass` class (not the `ClassWithPrivateStaticField` class) when we try to call `Subclass.publicStaticMethod()`, and so causes a `TypeError`.

This is the same if you call the method with `super`, because [`super` methods are not called with the super class as `this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#calling_methods_from_super)
.

You are advised to always access private static fields through the class name, not through `this`, so inheritance doesn't break the method.

### [Private methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#private_methods)

Private methods include private instance methods and private static methods. Private methods are only accessible from inside the class declaration.

#### Private instance methods

Unlike their public counterparts, private instance methods:

*   are installed immediately before the instance fields are installed, and
*   are only available on instances of the class, not on its `.prototype` property.

Private instance methods may be generator, async, or async generator functions. Private getters and setters are also possible, and follow the same syntax requirements as their public [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 and [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 counterparts.

Unlike public methods, private methods are not accessible on the `.prototype` property of their class.

#### Private static methods

Like their public counterparts, private static methods:

*   are added to the class constructor at class evaluation time, and
*   are only available on the class itself.

Private static methods may be generator, async, and async generator functions.

The same restriction previously mentioned for private static fields holds for private static methods, and similarly can lead to unexpected behavior when using `this`. In the following example, when we try to call `Subclass.publicStaticMethod()`, `this` refers to the `Subclass` class (not the `ClassWithPrivateStaticMethod` class) and so causes a `TypeError`.

### [Simulating private constructors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#simulating_private_constructors)

Many other languages include the capability to mark a constructor as private, which prevents the class from being instantiated outside of the class itself — you can only use static factory methods that create instances, or not be able to create instances at all. JavaScript does not have a native way to do this, but it can be accomplished by using a private static flag.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-PrivateIdentifier](https://tc39.es/ecma262/multipage/ecmascript-language-lexical-grammar.html#prod-PrivateIdentifier) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

### [javascript.classes.private\_class\_fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#javascript.classes.private_class_fields)

### [javascript.classes.private\_class\_fields\_in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#javascript.classes.private_class_fields_in)

### [javascript.classes.private\_class\_methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#javascript.classes.private_class_methods)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
     guide
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [Public class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [Private Syntax FAQ](https://github.com/tc39/proposal-class-fields/blob/main/PRIVATE_SYNTAX_FAQ.md "External link (opens in new tab)")
     in the TC39 class-fields proposal
*   [The semantics of all JS class elements](https://rfrn.org/~shu/2018/05/02/the-semantics-of-all-js-class-elements.html "External link (opens in new tab)")
     by Shu-yu Guo (2018)
*   [Public and private class fields](https://v8.dev/features/class-fields "External link (opens in new tab)")
     on v8.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/classes/private_elements/index.md?plain=1 "Folder: en-us/web/javascript/reference/classes/private_elements (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2FPrivate_elements&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fprivate_elements%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2FPrivate_elements%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fprivate_elements%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")