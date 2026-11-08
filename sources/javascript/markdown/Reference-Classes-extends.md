*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#mdn-search)
    

extends
=======

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`extends`** keyword is used in [class declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
 or [class expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class)
 to create a class that is a child of another class.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#try_it)

---------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#syntax)

---------------------------------------------------------------------------------------------------

[`ParentClass`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#parentclass)

An expression that evaluates to a constructor function (including a class) or `null`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#description)

-------------------------------------------------------------------------------------------------------------

The `extends` keyword can be used to subclass custom classes as well as built-in objects.

Any constructor that can be called with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 and has the [`prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)
 property can be the candidate for the parent class. The two conditions must both hold — for example, [bound functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
 and [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
 can be constructed, but they don't have a `prototype` property, so they cannot be subclassed.

The `prototype` property of the `ParentClass` must be an [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
 or [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
, but you would rarely worry about this in practice, because a non-object `prototype` doesn't behave as it should anyway. (It's ignored by the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator.)

`extends` sets the prototype for both `ChildClass` and `ChildClass.prototype`.

|     | Prototype of `ChildClass` | Prototype of `ChildClass.prototype` |
| --- | --- | --- |
| `extends` clause absent | `Function.prototype` | `Object.prototype` |
| [`extends null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#extending_null) | `Function.prototype` | `null` |
| `extends ParentClass` | `ParentClass` | `ParentClass.prototype` |

The right-hand side of `extends` does not have to be an identifier. You can use any expression that evaluates to a constructor. This is often useful to create [mixins](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#mix-ins)
. The `this` value in the `extends` expression is the `this` surrounding the class definition, and referring to the class's name is a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
 because the class is not initialized yet. [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 and [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
 work as expected in this expression.

While the base class may return anything from its constructor, the derived class must return an object or `undefined`, or a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 will be thrown.

If the parent class constructor returns an object, that object will be used as the `this` value for the derived class when further initializing [class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
. This trick is called ["return overriding"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#returning_overriding_object)
, which allows a derived class's fields (including [private](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 ones) to be defined on unrelated objects.

### [Subclassing built-ins](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#subclassing_built-ins)

**Warning:** The standard committee now holds the position that the built-in subclassing mechanism in previous spec versions is over-engineered and causes non-negligible performance and security impacts. New built-in methods consider less about subclasses, and engine implementers are [investigating whether to remove certain subclassing mechanisms](https://github.com/tc39/proposal-rm-builtin-subclassing "External link (opens in new tab)")
. Consider using composition instead of inheritance when enhancing built-ins.

Here are some things you may expect when extending a class:

*   When calling a static factory method (like [`Promise.resolve()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)
     or [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
    ) on a subclass, the returned instance is always an instance of the subclass.
*   When calling an instance method that returns a new instance (like [`Promise.prototype.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
     or [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
    ) on a subclass, the returned instance is always an instance of the subclass.
*   Instance methods try to delegate to a minimal set of primitive methods where possible. For example, for a subclass of [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
    , overriding [`then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
     automatically causes the behavior of [`catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)
     to change; or for a subclass of [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
    , overriding [`set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/set)
     automatically causes the behavior of the [`Map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Map)
     constructor to change.

However, the above expectations take non-trivial efforts to implement properly.

*   The first one requires the static method to read the value of [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
     to get the constructor for constructing the returned instance. This means `[p1, p2, p3].map(Promise.resolve)` throws an error because the `this` inside `Promise.resolve` is `undefined`. A way to fix this is to fall back to the base class if `this` is not a constructor, like [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
     does, but that still means the base class is special-cased.
*   The second one requires the instance method to read [`this.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)
     to get the constructor function. However, `new this.constructor()` may break legacy code, because the `constructor` property is both writable and configurable and is not protected in any way. Therefore, many copying built-in methods use the constructor's [`[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/species)
     property instead (which by default just returns `this`, the constructor itself). However, `[Symbol.species]` allows running arbitrary code and creating instances of arbitrary type, which poses a security concern and greatly complicates subclassing semantics.
*   The third one leads to visible invocations of custom code, which makes a lot of optimizations harder to implement. For example, if the `Map()` constructor is called with an iterable of _x_ elements, then it must visibly invoke the `set()` method _x_ times, instead of just copying the elements into the internal storage.

These problems are not unique to built-in classes. For your own classes, you will likely have to make the same decisions. However, for built-in classes, optimizability and security are a much bigger concern. New built-in methods always construct the base class and call as few custom methods as possible. If you want to subclass built-ins while achieving the above expectations, you need to override all methods that have the default behavior baked into them. Any addition of new methods on the base class may also break the semantics of your subclass because they are inherited by default. Therefore, a better way to extend built-ins is to use [_composition_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#avoiding_inheritance)
.

### [Extending null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#extending_null)

`extends null` was designed to allow easy creation of [objects that do not inherit from `Object.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#null-prototype_objects)
. However, due to unsettled decisions about whether `super()` should be called within the constructor, it's not possible to construct such a class in practice using any constructor implementation that doesn't return an object. [The TC39 committee is working on re-enabling this feature](https://github.com/tc39/ecma262/pull/1321 "External link (opens in new tab)")
.

Instead, you need to explicitly return an instance from the constructor.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#examples)

-------------------------------------------------------------------------------------------------------

### [Using extends](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#using_extends)

The first example creates a class called `Square` from a class called `Polygon`. This example is extracted from this [live demo](https://googlechrome.github.io/samples/classes-es6/index.html "External link (opens in new tab)")
 [(source)](https://github.com/GoogleChrome/samples/blob/gh-pages/classes-es6/index.html "External link (opens in new tab)")
.

### [Extending plain objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#extending_plain_objects)

Classes cannot extend regular (non-constructible) objects. If you want to inherit from a regular object by making all properties of this object available on inherited instances, you can instead use [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
:

### [Extending built-in objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#extending_built-in_objects)

This example extends the built-in [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
 object. This example is extracted from this [live demo](https://googlechrome.github.io/samples/classes-es6/index.html "External link (opens in new tab)")
 [(source)](https://github.com/GoogleChrome/samples/blob/gh-pages/classes-es6/index.html "External link (opens in new tab)")
.

### [Extending `Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#extending_object)

All JavaScript objects inherit from `Object.prototype` by default, so writing `extends Object` at first glance seems redundant. The only difference from not writing `extends` at all is that the constructor itself inherits static methods from `Object`, such as [`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
. However, because no `Object` static method uses the `this` value, there's still no value in inheriting these static methods.

The [`Object()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/Object)
 constructor special-cases the subclassing scenario. If it's implicitly called via [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
, it always initializes a new object with `new.target.prototype` as its prototype. Any value passed to `super()` is ignored.

Compare this behavior with a custom wrapper that does not special-case subclassing:

### [Species](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#species)

You might want to return [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 objects in your derived array class `MyArray`. The species pattern lets you override default constructors.

For example, when using methods such as [`Array.prototype.map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
 that return the default constructor, you want these methods to return a parent `Array` object, instead of the `MyArray` object. The [`Symbol.species`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/species)
 symbol lets you do this:

This behavior is implemented by many built-in copying methods. For caveats of this feature, see the [subclassing built-ins](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#subclassing_built-ins)
 discussion.

### [Mix-ins](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#mix-ins)

Abstract subclasses or _mix-ins_ are templates for classes. A class can only have a single superclass, so multiple inheritance from tooling classes, for example, is not possible. The functionality must be provided by the superclass.

A function with a superclass as input and a subclass extending that superclass as output can be used to implement mix-ins:

A class that uses these mix-ins can then be written like this:

### [Avoiding inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#avoiding_inheritance)

Inheritance is a very strong coupling relationship in object-oriented programming. It means all behaviors of the base class are inherited by the subclass by default, which may not always be what you want. For example, consider the implementation of a `ReadOnlyMap`:

It turns out that `ReadOnlyMap` is not constructible, because the [`Map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Map)
 constructor calls the instance's `set()` method.

We may get around this by using a private flag to indicate whether the instance is being constructed. However, a more significant problem with this design is that it breaks the [Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle "External link (opens in new tab)")
, which states that a subclass should be substitutable for its superclass. If a function expects a `Map` object, it should be able to use a `ReadOnlyMap` object as well, which will break here.

Inheritance often leads to [the circle-ellipse problem](https://en.wikipedia.org/wiki/Circle%E2%80%93ellipse_problem "External link (opens in new tab)")
, because neither type perfectly entails the behavior of the other, although they share a lot of common traits. In general, unless there's a very good reason to use inheritance, it's better to use composition instead. Composition means that a class has a reference to an object of another class, and only uses that object as an implementation detail.

In this case, the `ReadOnlyMap` class is not a subclass of `Map`, but it still implements most of the same methods. This means more code duplication, but it also means that the `ReadOnlyMap` class is not strongly coupled to the `Map` class, and does not easily break if the `Map` class is changed, avoiding the [semantic issues of built-in subclassing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#subclassing_built-ins)
. For example, if the `Map` class adds a new utility method (such as [`getOrInsert()`](https://github.com/tc39/proposal-upsert "External link (opens in new tab)")
) that does not call `set()`, it would cause the `ReadOnlyMap` class to no longer be read-only unless the latter is updated accordingly to override `getOrInsert()` as well. Moreover, `ReadOnlyMap` objects do not have the `set` method at all, which is more accurate than throwing an error at runtime.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-class-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-class-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#see_also)

-------------------------------------------------------------------------------------------------------

*   [Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
     guide
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/classes/extends/index.md?plain=1 "Folder: en-us/web/javascript/reference/classes/extends (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2Fextends&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fextends%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2Fextends%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fextends%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")