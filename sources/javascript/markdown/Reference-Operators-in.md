*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#mdn-search)
    

in
==

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`in`** operator returns `true` if the specified property is in the specified object or its prototype chain.

The `in` operator cannot be used to search for values in other collections. To test if a certain value exists in an array, use [`Array.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
. For sets, use [`Set.prototype.has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#try_it)

------------------------------------------------------------------------------------------------

    const car = { make: "Honda", model: "Accord", year: 1998 };
    
    console.log("make" in car);
    // Expected output: true
    
    delete car.make;
    if ("make" in car === false) {
      car.make = "Suzuki";
    }
    
    console.log(car.make);
    // Expected output: "Suzuki"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#syntax)

------------------------------------------------------------------------------------------------

js

    prop in object
    #prop in object
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#parameters)

[`prop`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#prop)

A string or symbol representing a property name (non-symbols will be [coerced to strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
). Can also be a [private element identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
.

[`object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#object)

Object to check if it (or its prototype chain) contains the property with specified name (`prop`).

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown if `object` is not an object (i.e., a primitive).

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#description)

----------------------------------------------------------------------------------------------------------

The `in` operator tests if a string or symbol property is present in an object or its prototype chain. If you want to check for only _non-inherited_ properties, use [`Object.hasOwn()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
 instead.

A property may be present in an object but have value `undefined`. Therefore, `"x" in obj` is not the same as `obj.x !== undefined`. To make `in` return `false` after a property is added, use the [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
 operator instead of setting that property's value to `undefined`.

You can also use the `in` operator to check whether a particular [private class field or method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 has been defined in an object. The operator returns `true` if the property is defined, and `false` otherwise. This is known as a _branded check_, because it returns `true` if and only if the object was created with that class constructor, after which you can safely access other private elements as well.

This is a special syntax — the left-hand side of the `in` operator is a property identifier instead of an expression, but unquoted (because otherwise it's a string property, not a private element).

Because accessing private elements on objects unrelated to the current class throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 instead of returning `undefined`, this syntax allows you to shorten:

js

    class C {
      #x;
      static isC(obj) {
        try {
          obj.#x;
          return true;
        } catch {
          return false;
        }
      }
    }
    

To:

js

    class C {
      #x;
      static isC(obj) {
        return #x in obj;
      }
    }
    

It also generally avoids the need for dealing with error handling just to access a private element that may be nonexistent.

However, the `in` operator still requires the private element to be declared beforehand in the enclosing class — otherwise, it would throw a [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
 ("Private field '#x' must be declared in an enclosing class"), the same one as when you try to access an undeclared private element.

js

    class C {
      foo() {
        #x in this;
      }
    }
    
    new C().foo(); // SyntaxError: Private field '#x' must be declared in an enclosing class
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#examples)

----------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#basic_usage)

The following examples show some uses of the `in` operator.

js

    // Arrays
    const trees = ["redwood", "bay", "cedar", "oak", "maple"];
    0 in trees; // returns true
    3 in trees; // returns true
    6 in trees; // returns false
    "bay" in trees; // returns false (you must specify the index number, not the value at that index)
    "length" in trees; // returns true (length is an Array property)
    Symbol.iterator in trees; // returns true
    
    // Predefined objects
    "PI" in Math; // returns true
    
    // Custom objects
    const myCar = { make: "Honda", model: "Accord", year: 1998 };
    "make" in myCar; // returns true
    "model" in myCar; // returns true
    

You must specify an object on the right side of the `in` operator. For example, you can specify a string created with the `String` constructor, but you cannot specify a string literal.

js

    const color1 = new String("green");
    "length" in color1; // returns true
    
    const color2 = "coral";
    // generates an error (color2 is not a String object)
    "length" in color2;
    

### [Using the in operator with deleted or undefined properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#using_the_in_operator_with_deleted_or_undefined_properties)

If you delete a property with the [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
 operator, the `in` operator returns `false` for that property.

js

    const myCar = { make: "Honda", model: "Accord", year: 1998 };
    delete myCar.make;
    "make" in myCar; // returns false
    
    const trees = ["redwood", "bay", "cedar", "oak", "maple"];
    delete trees[3];
    3 in trees; // returns false
    

If you set a property to [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 but do not delete it, the `in` operator returns true for that property.

js

    const myCar = { make: "Honda", model: "Accord", year: 1998 };
    myCar.make = undefined;
    "make" in myCar; // returns true
    

js

    const trees = ["redwood", "bay", "cedar", "oak", "maple"];
    trees[3] = undefined;
    3 in trees; // returns true
    

The `in` operator will return `false` for [empty array slots](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#sparse_arrays)
, even if accessing it directly returns `undefined`.

js

    const empties = new Array(3);
    empties[2]; // returns undefined
    2 in empties; // returns false
    

To avoid this, make sure a new array is always filled with non-empty values or not write to indexes past the end of array.

js

    const empties = new Array(3).fill(undefined);
    2 in empties; // returns true
    

### [Inherited properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#inherited_properties)

The `in` operator returns `true` for properties in the prototype chain. This may be undesirable if you are using objects to store arbitrary key-value pairs.

js

    const ages = { alice: 18, bob: 27 };
    
    function hasPerson(name) {
      return name in ages;
    }
    
    hasPerson("hasOwnProperty"); // true
    

You can use [`Object.hasOwn()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
 to check if the object has the key.

js

    const ages = { alice: 18, bob: 27 };
    
    function hasPerson(name) {
      return Object.hasOwn(ages, name);
    }
    
    hasPerson("hasOwnProperty"); // false
    

Alternatively, you should consider using a [null prototype object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#null-prototype_objects)
 or a [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
 for storing `ages`, to avoid other bugs.

js

    const ages = new Map([\
      ["alice", 18],\
      ["bob", 27],\
    ]);
    
    function hasPerson(name) {
      return ages.has(name);
    }
    
    hasPerson("hasOwnProperty"); // false
    

### [Using the in operator to implement branded checks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#using_the_in_operator_to_implement_branded_checks)

The code fragment below demonstrates a static function that tells if an object was created with the `Person` constructor and therefore can perform other methods safely.

js

    class Person {
      #age;
      constructor(age) {
        this.#age = age;
      }
      static isPerson(o) {
        return #age in o;
      }
      ageDifference(other) {
        return this.#age - other.#age;
      }
    }
    
    const p1 = new Person(20);
    const p2 = new Person(30);
    console.log(p1.ageDifference(p2)); // -10
    console.log(Person.isPerson(p1)); // true
    
    if (Person.isPerson(p1) && Person.isPerson(p2)) {
      console.log(p1.ageDifference(p2)); // -10
    }
    

It helps to prevent the following case:

js

    const p2 = {};
    
    p1.ageDifference(p2); // TypeError: Cannot read private member #age from an object whose class did not declare it
    

Without the `in` operator, you would have to use a `try...catch` block to check if the object has the private element.

You can also implement this as a [`[Symbol.hasInstance]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/hasInstance)
 method of the class, so that you can use the [`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
 operator to perform the same check (which, by default, only checks for the existence of `Person.prototype` in the object's prototype chain).

js

    class Person {
      #age;
      constructor(age) {
        this.#age = age;
      }
      static [Symbol.hasInstance](o) {
        // Testing `this` to prevent false-positives when
        // calling `instanceof SubclassOfPerson`
        return this === Person && #age in o;
      }
      ageDifference(other) {
        return this.#age - other.#age;
      }
    }
    
    const p1 = new Person(20);
    const p2 = new Person(30);
    
    if (p1 instanceof Person && p2 instanceof Person) {
      console.log(p1.ageDifference(p2)); // -10
    }
    

For more examples, see [Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 and the [class guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes#private_fields)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-relational-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-relational-operators) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in#see_also)

----------------------------------------------------------------------------------------------------

*   [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
    
*   [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
    
*   [`Object.hasOwn()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
    
*   [`Reflect.has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/has)
    
*   [Enumerability and ownership of properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/in/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/in (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")