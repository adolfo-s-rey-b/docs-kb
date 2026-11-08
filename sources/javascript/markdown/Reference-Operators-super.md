*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#mdn-search)
    

super
=====

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`super`** keyword is used to access properties on an object literal or class's \[\[Prototype\]\], or invoke a superclass's constructor.

The `super.prop` and `super[expr]` expressions are valid in any [method definition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
 in both [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 and [object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
. The `super(...args)` expression is valid in class constructors.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#try_it)

---------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#syntax)

---------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#description)

-------------------------------------------------------------------------------------------------------------

The `super` keyword can be used in two ways: as a "function call" (`super(...args)`), or as a "property lookup" (`super.prop` and `super[expr]`).

**Note:** `super` is a keyword and these are special syntactic constructs. `super` is not a variable that points to the prototype object. Attempting to read `super` itself is a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.

In the [constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
 body of a derived class (with `extends`), the `super` keyword may appear as a "function call" (`super(...args)`), which must be called before the `this` keyword is used, and before the constructor returns. It calls the parent class's constructor and binds the parent class's public fields, after which the derived class's constructor can further access and modify `this`.

The "property lookup" form can be used to access methods and properties of an object literal's or class's \[\[Prototype\]\]. Within a class's body, the reference of `super` can be either the superclass's constructor itself, or the constructor's `prototype`, depending on whether the execution context is instance creation or class initialization. See the Examples section for more details.

Note that the reference of `super` is determined by the class or object literal `super` was declared in, not the object the method is called on. Therefore, unbinding or re-binding a method doesn't change the reference of `super` in it (although they do change the reference of [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
). You can see `super` as a variable in the class or object literal scope, which the methods create a closure over. (But also beware that it's not actually a variable, as explained above.)

When setting properties through `super`, the property is set on `this` instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#examples)

-------------------------------------------------------------------------------------------------------

### [Using super in classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#using_super_in_classes)

This code snippet is taken from the [classes sample](https://github.com/GoogleChrome/samples/blob/gh-pages/classes-es6/index.html "External link (opens in new tab)")
 ([live demo](https://googlechrome.github.io/samples/classes-es6/index.html "External link (opens in new tab)")
). Here `super()` is called to avoid duplicating the constructor parts' that are common between `Rectangle` and `Square`.

### [Super-calling static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#super-calling_static_methods)

You are also able to call super on [static](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 methods.

### [Accessing super in class field declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#accessing_super_in_class_field_declaration)

`super` can also be accessed during class field initialization. The reference of `super` depends on whether the current field is an instance field or a static field.

Note that instance fields are set on the instance instead of the constructor's `prototype`, so you can't use `super` to access the instance field of a superclass.

Here, `extendedField` is `undefined` instead of 10, because `baseField` is defined as an own property of the `Base` instance, instead of `Base.prototype`. `super`, in this context, only looks up properties on `Base.prototype`, because that's the \[\[Prototype\]\] of `Extended.prototype`.

### [Deleting super properties will throw an error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#deleting_super_properties_will_throw_an_error)

You cannot use the [`delete` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
 and `super.prop` or `super[expr]` to delete a parent class' property — it will throw a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
.

### [Using super.prop in object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#using_super.prop_in_object_literals)

Super can also be used in the [object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 notation. In this example, two objects define a method. In the second object, `super` calls the first object's method. This works with the help of [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
 with which we are able to set the prototype of `obj2` to `obj1`, so that `super` is able to find `method1` on `obj1`.

### [Methods that read super.prop do not behave differently when bound to other objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#methods_that_read_super.prop_do_not_behave_differently_when_bound_to_other_objects)

Accessing `super.x` behaves like `Reflect.get(Object.getPrototypeOf(objectLiteral), "x", this)`, which means the property is always sought on the object literal/class declaration's prototype, and unbinding and re-binding a method won't change the reference of `super`.

The same happens in object literals.

Only resetting the entire inheritance chain will change the reference of `super`.

### [Calling methods from super](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#calling_methods_from_super)

When calling `super.prop` as a function, the `this` value inside the `prop` function is the current `this`, not the object that `super` points to. For example, the `super.getName()` call logs `"Extended"`, despite the code looking like it's equivalent to `Base.getName()`.

This is especially important when interacting with [static private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#private_static_fields)
.

### [Setting super.prop sets the property on this instead](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#setting_super.prop_sets_the_property_on_this_instead)

Setting properties of `super`, such as `super.x = 1`, behaves like `Reflect.set(Object.getPrototypeOf(objectLiteral), "x", 1, this)`. This is one of the cases where understanding `super` as simply "reference of the prototype object" falls short, because it actually sets the property on `this` instead.

`super.x = 1` will look for the property descriptor of `x` on `A.prototype` (and invoke the setters defined there), but the `this` value will be set to `this`, which is `b` in this context. You can read [`Reflect.set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/set)
 for more details on the case when `target` and `receiver` differ.

This means that while methods that _get_ `super.prop` are usually not susceptible to changes in the `this` context, those that _set_ `super.prop` are.

However, `super.x = 1` still consults the property descriptor of the prototype object, which means you cannot rewrite non-writable properties, and setters will be invoked.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-super-keyword](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-super-keyword) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super#see_also)

-------------------------------------------------------------------------------------------------------

*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/super/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/super (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fsuper&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fsuper%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fsuper%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fsuper%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")