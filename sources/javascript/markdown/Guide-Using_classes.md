*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#mdn-search)
    

Using classes
=============

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
    

JavaScript is a prototype-based language — an object's behaviors are specified by its own properties and its prototype's properties. However, with the addition of [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
, the creation of hierarchies of objects and the inheritance of properties and their values are much more in line with other object-oriented languages such as Java. In this section, we will demonstrate how objects can be created from classes.

In many other languages, _classes_, or constructors, are clearly distinguished from _objects_, or instances. In JavaScript, classes are mainly an abstraction over the existing prototypical inheritance mechanism — all patterns are convertible to prototype-based inheritance. Classes themselves are normal JavaScript values as well, and have their own prototype chains. In fact, most plain JavaScript functions can be used as constructors — you use the `new` operator with a constructor function to create a new object.

We will be playing with the well-abstracted class model in this tutorial, and discuss what semantics classes offer. If you want to dive deep into the underlying prototype system, you can read the [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 guide.

This chapter assumes that you are already somewhat familiar with JavaScript and that you have used ordinary objects.

[Overview of classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#overview_of_classes)

-----------------------------------------------------------------------------------------------------------------------

If you have some hands-on experience with JavaScript, or have followed along with the guide, you probably have already used classes, even if you haven't created one. For example, this [may seem familiar to you](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times)
:

On the first line, we created an instance of the class [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
, and called it `bigDay`. On the second line, we called a [method](https://developer.mozilla.org/en-US/docs/Glossary/Method)
 [`toLocaleDateString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString)
 on the `bigDay` instance, which returns a string. Then, we compared two numbers: one returned from the [`getTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTime)
 method, the other directly called from the `Date` class _itself_, as [`Date.now()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)
.

`Date` is a built-in class of JavaScript. From this example, we can get some basic ideas of what classes do:

*   Classes create objects through the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
     operator.
*   Each object has some properties (data or method) added by the class.
*   The class stores some properties (data or method) itself, which are usually used to interact with instances.

These correspond to the three key features of classes:

*   Constructor;
*   Instance methods and instance fields;
*   Static methods and static fields.

[Declaring a class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#declaring_a_class)

-------------------------------------------------------------------------------------------------------------------

Classes are usually created with _class declarations_.

Within a class body, there are a range of features available.

If you came from a pre-ES6 world, you may be more familiar with using functions as constructors. The pattern above would roughly translate to the following with function constructors:

**Note:** Private fields and methods are new features in classes with no trivial equivalent in function constructors.

### [Constructing a class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#constructing_a_class)

After a class has been declared, you can create instances of it using the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator.

Typical function constructors can both be constructed with `new` and called without `new`. However, attempting to "call" a class without `new` will result in an error.

### [Class declaration hoisting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#class_declaration_hoisting)

Unlike function declarations, class declarations are not [hoisted](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
 (or, in some interpretations, hoisted but with the temporal dead zone restriction), which means you cannot use a class before it is declared.

This behavior is similar to variables declared with [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 and [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
.

### [Class expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#class_expressions)

Similar to functions, class declarations also have their expression counterparts.

Class expressions can have names as well. The expression's name is only visible to the class's body.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#constructor)

-------------------------------------------------------------------------------------------------------

Perhaps the most important job of a class is to act as a "factory" for objects. For example, when we use the `Date` constructor, we expect it to give a new object which represents the date data we passed in — which we can then manipulate with other methods the instance exposes. In classes, the instance creation is done by the [constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
.

As an example, we would create a class called `Color`, which represents a specific color. Users create colors through passing in an [RGB](https://developer.mozilla.org/en-US/docs/Glossary/RGB)
 triplet.

Open your browser's devtools, paste the above code into the console, and then create an instance:

You should see some output like this:

Object { values: (3) \[…\] }
  values: Array(3) \[ 255, 0, 0 \]

You have successfully created a `Color` instance, and the instance has a `values` property, which is an array of the RGB values you passed in. That is pretty much equivalent to the following:

The constructor's syntax is exactly the same as a normal function — which means you can use other syntaxes, like [rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
:

Each time you call `new`, a different instance is created.

Within a class constructor, the value of `this` points to the newly created instance. You can assign properties to it, or read existing properties (especially methods — which we will cover next).

The `this` value will be automatically returned as the result of `new`. You are advised to not return any value from the constructor — because if you return a non-primitive value, it will become the value of the `new` expression, and the value of `this` is dropped. (You can read more about what `new` does in [its description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new#description)
.)

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#instance_methods)

-----------------------------------------------------------------------------------------------------------------

If a class only has a constructor, it is not much different from a `createX` factory function which just creates plain objects. However, the power of classes is that they can be used as "templates" which automatically assign methods to instances.

For example, for `Date` instances, you can use a range of methods to get different information from a single date value, such as the [year](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)
, [month](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMonth)
, [day of the week](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay)
, etc. You can also set those values through the `setX` counterparts like [`setFullYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear)
.

For our own `Color` class, we can add a method called `getRed` which returns the red value of the color.

Without methods, you may be tempted to define the function within the constructor:

This also works. However, a problem is that this creates a new function every time a `Color` instance is created, even when they all do the same thing!

In contrast, if you use a method, it will be shared between all instances. A function can be shared between all instances, but still have its behavior differ when different instances call it, because the value of `this` is different. If you are curious _where_ this method is stored in — it's defined on the prototype of all instances, or `Color.prototype`, which is explained in more detail in [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
.

Similarly, we can create a new method called `setRed`, which sets the red value of the color.

[Private fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#private_fields)

-------------------------------------------------------------------------------------------------------------

You might be wondering: why do we want to go to the trouble of using `getRed` and `setRed` methods, when we can directly access the `values` array on the instance?

There is a philosophy in object-oriented programming called "encapsulation". This means you should not access the underlying implementation of an object, but instead use well-abstracted methods to interact with it. For example, if we suddenly decided to represent colors as [HSL](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
 instead:

The user assumption that `values` means the RGB value suddenly collapses, and it may cause their logic to break. So, if you are an implementor of a class, you would want to hide the internal data structure of your instance from your user, both to keep the API clean and to prevent the user's code from breaking when you do some "harmless refactors". In classes, this is done through [_private fields_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
.

A private field is an identifier prefixed with `#` (the hash symbol). The hash is an integral part of the field's name, which means a private field can never clash names with a public field or method. In order to refer to a private field anywhere in the class, you must _declare_ it in the class body (you can't create a private element on the fly). Apart from this, a private field is pretty much equivalent to a normal property.

Accessing private fields outside the class is an early syntax error. The language can guard against this because `#privateField` is a special syntax, so it can do some static analysis and find all usage of private fields before even evaluating the code.

**Note:** Code run in the Chrome console can access private elements outside the class. This is a DevTools-only relaxation of the JavaScript syntax restriction.

Private fields in JavaScript are _hard private_: if the class does not implement methods that expose these private fields, there's absolutely no mechanism to retrieve them from outside the class. This means you are safe to do any refactors to your class's private fields, as long as the behavior of exposed methods stay the same.

After we've made the `values` field private, we can add some more logic in the `getRed` and `setRed` methods, instead of making them simple pass-through methods. For example, we can add a check in `setRed` to see if it's a valid R value:

If we leave the `values` property exposed, our users can easily circumvent that check by assigning to `values[0]` directly, and create invalid colors. But with a well-encapsulated API, we can make our code more robust and prevent logic errors downstream.

A class method can read the private fields of other instances, as long as they belong to the same class.

However, if `anotherColor` is not a Color instance, `#values` won't exist. (Even if another class has an identically named `#values` private field, it's not referring to the same thing and cannot be accessed here.) Accessing a nonexistent private element throws an error instead of returning `undefined` like normal properties do. If you don't know if a private field exists on an object and you wish to access it without using `try`/`catch` to handle the error, you can use the [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 operator.

**Note:** Keep in mind that the `#` is a special identifier syntax, and you can't use the field name as if it's a string. `"#values" in anotherColor` would look for a property name literally called `"#values"`, instead of a private field.

There are some limitations in using private elements: the same name can't be declared twice in a single class, and they can't be deleted. Both lead to early syntax errors.

Methods, [getters, and setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#accessor_fields)
 can be private as well. They're useful when you have something complex that the class needs to do internally but no other part of the code should be allowed to call.

For example, imagine creating [HTML custom elements](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements)
 that should do something somewhat complicated when clicked/tapped/otherwise activated. Furthermore, the somewhat complicated things that happen when the element is clicked should be restricted to this class, because no other part of the JavaScript will (or should) ever access it.

In this case, pretty much every field and method is private to the class. Thus, it presents an interface to the rest of the code that's essentially just like a built-in HTML element. No other part of the program has the power to affect any of the internals of `Counter`.

[Accessor fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#accessor_fields)

---------------------------------------------------------------------------------------------------------------

`color.getRed()` and `color.setRed()` allow us to read and write to the red value of a color. If you come from languages like Java, you will be very familiar with this pattern. However, using methods to simply access a property is still somewhat unergonomic in JavaScript. _Accessor fields_ allow us to manipulate something as if it is an "actual property".

It looks as if the object has a property called `red` — but actually, no such property exists on the instance! There are only two methods, but they are prefixed with `get` and `set`, which allows them to be manipulated as if they were properties.

If a field only has a getter but no setter, it will be effectively read-only.

In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, the `red.red = 0` line will throw a type error: "Cannot set property red of #<Color> which has only a getter". In non-strict mode, the assignment is silently ignored.

[Public fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#public_fields)

-----------------------------------------------------------------------------------------------------------

Private fields also have their public counterparts, which allow every instance to have a property. Fields are usually designed to be independent of the constructor's parameters.

Public fields are almost equivalent to assigning a property to `this`. For example, the above example can also be converted to:

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#static_properties)

-------------------------------------------------------------------------------------------------------------------

With the `Date` example, we have also encountered the [`Date.now()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)
 method, which returns the current date. This method does not belong to any date instance — it belongs to the class itself. However, it's put on the `Date` class instead of being exposed as a global `DateNow()` function, because it's mostly useful when dealing with date instances.

**Note:** Prefixing utility methods with what they deal with is called "namespacing" and is considered a good practice. For example, in addition to the older, unprefixed [`parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
 method, JavaScript also later added the prefixed [`Number.parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/parseInt)
 method to indicate that it's for dealing with numbers.

[_Static properties_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 are a group of class features that are defined on the class itself, rather than on individual instances of the class. These features include:

*   Static methods
*   Static fields
*   Static getters and setters

Everything also has private counterparts. For example, for our `Color` class, we can create a static method that checks whether a given triplet is a valid RGB value:

Static properties are very similar to their instance counterparts, except that:

*   They are all prefixed with `static`, and
*   They are not accessible from instances.

There is also a special construct called a [_static initialization block_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
, which is a block of code that runs when the class is first loaded.

Static initialization blocks are almost equivalent to immediately executing some code after a class has been declared. The only difference is that they have access to static private elements.

[Extends and inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#extends_and_inheritance)

-------------------------------------------------------------------------------------------------------------------------------

A key feature that classes bring about (in addition to ergonomic encapsulation with private fields) is _inheritance_, which means one object can "borrow" a large part of another object's behaviors, while overriding or enhancing certain parts with its own logic.

For example, suppose our `Color` class now needs to support transparency. We may be tempted to add a new field that indicates its transparency:

However, this means every instance — even the vast majority which aren't transparent (those with an alpha value of 1) — will have to have the extra alpha value, which is not very elegant. Plus, if the features keep growing, our `Color` class will become very bloated and hard to maintain.

Instead, in object-oriented programming, we would create a _derived class_. The derived class has access to all public properties of the parent class. In JavaScript, derived classes are declared with an [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
 clause, which indicates the class it extends from.

There are a few things that have immediately come to attention. First is that in the constructor, we are calling `super(r, g, b)`. It is a language requirement to call [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 before accessing `this`. The `super()` call calls the parent class's constructor to initialize `this` — here it's roughly equivalent to `this = new Color(r, g, b)`. You can have code before `super()`, but you cannot access `this` before `super()` — the language prevents you from accessing the uninitialized `this`.

After the parent class is done with modifying `this`, the derived class can do its own logic. Here we added a private field called `#alpha`, and also provided a pair of getter/setters to interact with them.

A derived class inherits all methods from its parent. For example, consider the `get red()` accessor we added to the `Color` in the [Accessor fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#accessor_fields)
 section—even though we haven't declared one in `ColorWithAlpha`, we can still access `red` because this behavior is specified by the parent class:

Derived classes can also override methods from the parent class. For example, all classes implicitly inherit the [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
 class, which defines some basic methods like [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
. However, the base `toString()` method is notoriously useless, because it prints `[object Object]` in most cases:

Instead, our class can override it to print the color's RGB values:

Within derived classes, you can access the parent class's methods by using `super`. This allows you to build enhancement methods and avoid code duplication.

When you use `extends`, the static methods inherit from each other as well, so you can also override or enhance them.

Derived classes don't have access to the parent class's private fields — this is another key aspect to JavaScript private fields being "hard private". Private fields are scoped to the class body itself and do not grant access to _any_ outside code.

A class can only extend from one class. This prevents problems in multiple inheritance like the [diamond problem](https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem "External link (opens in new tab)")
. However, due to the dynamic nature of JavaScript, it's still possible to achieve the effect of multiple inheritance through class composition and [mixins](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends#mix-ins)
.

Instances of derived classes are also [instances of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
 the base class.

[Why classes?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#why_classes)

--------------------------------------------------------------------------------------------------------

The guide has been pragmatic so far: we are focusing on _how_ classes can be used, but there's one question unanswered: _why_ would one use a class? The answer is: it depends.

Classes introduce a _paradigm_, or a way to organize your code. Classes are the foundations of object-oriented programming, which is built on concepts like [inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming) "External link (opens in new tab)")
 and [polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science) "External link (opens in new tab)")
 (especially _subtype polymorphism_). However, many people are philosophically against certain OOP practices and don't use classes as a result.

For example, one thing that makes `Date` objects infamous is that they're _mutable_.

Mutability and internal state are important aspects of object-oriented programming, but often make code hard to reason with — because any seemingly innocent operation may have unexpected side effects and change the behavior in other parts of the program.

In order to reuse code, we usually resort to extending classes, which can create big hierarchies of inheritance patterns.

![A typical OOP inheritance tree, with five classes and three levels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes/figure8.1.png)

However, it is often hard to describe inheritance cleanly when one class can only extend one other class. Often, we want the behavior of multiple classes. In Java, this is done through interfaces; in JavaScript, it can be done through mixins. But at the end of the day, it's still not very convenient.

On the brighter side, classes are a very powerful way to organize our code on a higher level. For example, without the `Color` class, we may need to create a dozen of utility functions:

But with classes, we can congregate them all under the `Color` namespace, which improves readability. In addition, the introduction of private fields allows us to hide certain data from downstream users, creating a clean API.

In general, you should consider using classes when you want to create objects that store their own internal data and expose a lot of behavior. Take built-in JavaScript classes as examples:

*   The [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
     and [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
     classes store a collection of elements and allow you to access them by key using `get()`, `set()`, `has()`, etc.
*   The [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
     class stores a date as a Unix timestamp (a number) and allows you to format, update, and read individual date components.
*   The [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
     class stores information about a particular exception, including the error message, stack trace, cause, etc. It's one of the few classes that come with a rich inheritance structure: there are multiple built-in classes like [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
     and [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
     that extend `Error`. In the case of errors, this inheritance allows refining the semantics of errors: each error class represents a specific type of error, which can be easily checked with [`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
    .

JavaScript offers the mechanism to organize your code in a canonical object-oriented way, but whether and how to use it is entirely up to the programmer's discretion.

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/using_classes/index.md?plain=1 "Folder: en-us/web/javascript/guide/using_classes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FUsing_classes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fusing_classes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FUsing_classes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fusing_classes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F44b7cee840c2c4b4f9fa164d45bb4f397e5af5da%0A*+Document+last+modified%3A+2026-10-03T17%3A54%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")