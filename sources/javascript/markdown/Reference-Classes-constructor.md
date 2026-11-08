*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#mdn-search)
    

constructor
===========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`constructor`** method is a special method of a [class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 for creating and initializing an object instance of that class.

**Note:** This page introduces the `constructor` syntax. For the `constructor` property present on all objects, see [`Object.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#try_it)

-------------------------------------------------------------------------------------------------------

    class Polygon {
      constructor() {
        this.name = "Polygon";
      }
    }
    
    const poly = new Polygon();
    
    console.log(poly.name);
    // Expected output: "Polygon"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#syntax)

-------------------------------------------------------------------------------------------------------

js

    constructor() { /* … */ }
    constructor(argument0) { /* … */ }
    constructor(argument0, argument1) { /* … */ }
    constructor(argument0, argument1, /* …, */ argumentN) { /* … */ }
    

There are some additional syntax restrictions:

*   A non-static class method with the non-computed name `constructor` cannot be a [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
    , [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
    , [async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
    , or [generator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
    .
*   A class cannot have more than one `constructor` method.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#description)

-----------------------------------------------------------------------------------------------------------------

A constructor enables you to provide any custom initialization that must be done before any other methods can be called on an instantiated object.

js

    class Person {
      constructor(name) {
        this.name = name;
      }
    
      introduce() {
        console.log(`Hello, my name is ${this.name}`);
      }
    }
    
    const otto = new Person("Otto");
    
    otto.introduce(); // Hello, my name is Otto
    

If you don't provide your own constructor, then a default constructor will be supplied for you. If your class is a base class, the default constructor is empty:

js

    constructor() {}
    

If your class is a derived class, the default constructor calls the parent constructor, passing along any arguments that were provided:

js

    constructor(...args) {
      super(...args);
    }
    

**Note:** The difference between an explicit constructor like the one above and the default constructor is that the latter doesn't actually invoke [the array iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.iterator)
 through [argument spreading](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
.

That enables code like this to work:

js

    class ValidationError extends Error {
      printCustomerMessage() {
        return `Validation failed :-( (details: ${this.message})`;
      }
    }
    
    try {
      throw new ValidationError("Not a valid phone number");
    } catch (error) {
      if (error instanceof ValidationError) {
        console.log(error.name); // This is Error instead of ValidationError!
        console.log(error.printCustomerMessage());
      } else {
        console.log("Unknown error", error);
        throw error;
      }
    }
    

The `ValidationError` class doesn't need an explicit constructor, because it doesn't need to do any custom initialization. The default constructor then takes care of initializing the parent `Error` from the argument it is given.

However, if you provide your own constructor, and your class derives from some parent class, then you must explicitly call the parent class constructor using [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
. For example:

js

    class ValidationError extends Error {
      constructor(message) {
        super(message); // call parent class constructor
        this.name = "ValidationError";
        this.code = "42";
      }
    
      printCustomerMessage() {
        return `Validation failed :-( (details: ${this.message}, code: ${this.code})`;
      }
    }
    
    try {
      throw new ValidationError("Not a valid phone number");
    } catch (error) {
      if (error instanceof ValidationError) {
        console.log(error.name); // Now this is ValidationError!
        console.log(error.printCustomerMessage());
      } else {
        console.log("Unknown error", error);
        throw error;
      }
    }
    

Using [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 on a class goes through the following steps:

1.  (If it's a derived class) The `constructor` body before the `super()` call is evaluated. This part should not access `this` because it's not yet initialized.
2.  (If it's a derived class) The `super()` call is evaluated, which initializes the parent class through the same process.
3.  The current class's [fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
     are initialized.
4.  The `constructor` body after the `super()` call (or the entire body, if it's a base class) is evaluated.

Within the `constructor` body, you can access the object being created through [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 and access the class that is called with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 through [`new.target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target)
. Note that methods (including [getters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 and [setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
) and the [prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 are already initialized on `this` before the `constructor` is executed, so you can even access methods of the subclass from the constructor of the superclass. However, if those methods use `this`, the `this` will not have been fully initialized yet. This means reading public fields of the derived class will result in `undefined`, while reading private fields will result in a `TypeError`.

js

    new (class C extends class B {
      constructor() {
        console.log(this.foo());
      }
    } {
      #a = 1;
      foo() {
        return this.#a; // TypeError: Cannot read private member #a from an object whose class did not declare it
        // It's not really because the class didn't declare it,
        // but because the private field isn't initialized yet
        // when the superclass constructor is running
      }
    })();
    

The `constructor` method may have a return value. While the base class may return anything from its constructor, the derived class must return an object or `undefined`, or a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 will be thrown.

js

    class ParentClass {
      constructor() {
        return 1;
      }
    }
    
    console.log(new ParentClass()); // ParentClass {}
    // The return value is ignored because it's not an object
    // This is consistent with function constructors
    
    class ChildClass extends ParentClass {
      constructor() {
        return 1;
      }
    }
    
    console.log(new ChildClass()); // TypeError: Derived constructors may only return object or undefined
    

If the parent class constructor returns an object, that object will be used as the `this` value on which [class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
 of the derived class will be defined. This trick is called ["return overriding"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements#returning_overriding_object)
, which allows a derived class's fields (including [private](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 ones) to be defined on unrelated objects.

The `constructor` follows normal [method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
 syntax, so [parameter default values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
, [rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
, etc. can all be used.

js

    class Person {
      constructor(name = "Anonymous") {
        this.name = name;
      }
      introduce() {
        console.log(`Hello, my name is ${this.name}`);
      }
    }
    
    const person = new Person();
    person.introduce(); // Hello, my name is Anonymous
    

The constructor must be a literal name. [Computed properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names)
 cannot become constructors.

js

    class Foo {
      // This is a computed property. It will not be picked up as a constructor.
      ["constructor"]() {
        console.log("called");
        this.a = 1;
      }
    }
    
    const foo = new Foo(); // No log
    console.log(foo); // Foo {}
    foo.constructor(); // Logs "called"
    console.log(foo); // Foo { a: 1 }
    

Non-static async methods, generator methods, and accessors are forbidden from having the non-computed name `constructor`. Static and instance class fields also cannot have the non-computed name `constructor`. Private names cannot be called `#constructor`. Any non-static member with the non-computed name `constructor` must be a plain method.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#examples)

-----------------------------------------------------------------------------------------------------------

### [Using the constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#using_the_constructor)

This code snippet is taken from the [classes sample](https://github.com/GoogleChrome/samples/blob/gh-pages/classes-es6/index.html "External link (opens in new tab)")
 ([live demo](https://googlechrome.github.io/samples/classes-es6/index.html "External link (opens in new tab)")
).

js

    class Square extends Polygon {
      constructor(length) {
        // Here, it calls the parent class' constructor with lengths
        // provided for the Polygon's width and height
        super(length, length);
        // NOTE: In derived classes, `super()` must be called before you
        // can use `this`. Leaving this out will cause a ReferenceError.
        this.name = "Square";
      }
    
      get area() {
        return this.height * this.width;
      }
    
      set area(value) {
        this.height = value ** 0.5;
        this.width = value ** 0.5;
      }
    }
    

### [Calling super in a constructor bound to a different prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#calling_super_in_a_constructor_bound_to_a_different_prototype)

`super()` calls the constructor that's the prototype of the current class. If you change the prototype of the current class itself, `super()` will call the constructor that's the new prototype. Changing the prototype of the current class's `prototype` property doesn't affect which constructor `super()` calls.

js

    class Polygon {
      constructor() {
        this.name = "Polygon";
      }
    }
    
    class Rectangle {
      constructor() {
        this.name = "Rectangle";
      }
    }
    
    class Square extends Polygon {
      constructor() {
        super();
      }
    }
    
    // Make Square extend Rectangle (which is a base class) instead of Polygon
    Object.setPrototypeOf(Square, Rectangle);
    
    const newInstance = new Square();
    
    // newInstance is still an instance of Polygon, because we didn't
    // change the prototype of Square.prototype, so the prototype chain
    // of newInstance is still
    //   newInstance --> Square.prototype --> Polygon.prototype
    console.log(newInstance instanceof Polygon); // true
    console.log(newInstance instanceof Rectangle); // false
    
    // However, because super() calls Rectangle as constructor, the name property
    // of newInstance is initialized with the logic in Rectangle
    console.log(newInstance.name); // Rectangle
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-static-semantics-constructormethod](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-static-semantics-constructormethod) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
     guide
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [Static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
    
*   [`Object.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/classes/constructor/index.md?plain=1 "Folder: en-us/web/javascript/reference/classes/constructor (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2Fconstructor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fconstructor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2Fconstructor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fconstructor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")