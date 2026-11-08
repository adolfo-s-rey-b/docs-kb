*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#mdn-search)
    

get
===

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`get`** syntax binds an object property to a function that will be called when that property is looked up. It can also be used in [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#try_it)

-------------------------------------------------------------------------------------------------

    const obj = {
      log: ["a", "b", "c"],
      get latest() {
        return this.log[this.log.length - 1];
      },
    };
    
    console.log(obj.latest);
    // Expected output: "c"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#syntax)

-------------------------------------------------------------------------------------------------

js

    { get prop() { /* … */ } }
    { get [expression]() { /* … */ } }
    

There are some additional syntax restrictions:

*   A getter must have exactly zero parameters.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#parameters)

[`prop`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#prop)

The name of the property to bind to the given function. In the same way as other properties in [object initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
, it can be a string literal, a number literal, or an identifier.

[`expression`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#expression)

You can also use expressions for a computed property name to bind to the given function.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#description)

-----------------------------------------------------------------------------------------------------------

Sometimes, it is desirable to allow access to a property that returns a dynamically computed value, or you may want to reflect the status of an internal variable without requiring the use of explicit method calls. In JavaScript, this can be accomplished with the use of a _getter_.

An object property is either a data property or an accessor property, but it cannot simultaneously be both. Read [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 for more information. The getter syntax allows you to specify the getter function in an object initializer.

js

    const obj = {
      get prop() {
        // getter, the code executed when reading obj.prop
        return someValue;
      },
    };
    

Properties defined using this syntax are own properties of the created object, and they are configurable and enumerable.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#examples)

-----------------------------------------------------------------------------------------------------

### [Defining a getter on new objects in object initializers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#defining_a_getter_on_new_objects_in_object_initializers)

This will create a pseudo-property `latest` for object `obj`, which will return the last array item in `log`.

js

    const obj = {
      log: ["example", "test"],
      get latest() {
        return this.log.at(-1);
      },
    };
    console.log(obj.latest); // "test"
    

Note that attempting to assign a value to `latest` will not change it.

### [Using getters in classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#using_getters_in_classes)

You can use the exact same syntax to define public instance getters that are available on class instances. In classes, you don't need the comma separator between methods.

js

    class ClassWithGetSet {
      #msg = "hello world";
      get msg() {
        return this.#msg;
      }
      set msg(x) {
        this.#msg = `hello ${x}`;
      }
    }
    
    const instance = new ClassWithGetSet();
    console.log(instance.msg); // "hello world"
    
    instance.msg = "cake";
    console.log(instance.msg); // "hello cake"
    

Getter properties are defined on the `prototype` property of the class and are thus shared by all instances of the class. Unlike getter properties in object literals, getter properties in classes are not enumerable.

Static getters and private getters use similar syntaxes, which are described in the [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 and [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 pages.

### [Deleting a getter using the `delete` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#deleting_a_getter_using_the_delete_operator)

If you want to remove the getter, you can just [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
 it:

js

    delete obj.latest;
    

### [Defining a getter on existing objects using `defineProperty`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#defining_a_getter_on_existing_objects_using_defineproperty)

To append a getter to an existing object later at any time, use [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
.

js

    const o = { a: 0 };
    
    Object.defineProperty(o, "b", {
      get() {
        return this.a + 1;
      },
    });
    
    console.log(o.b); // Runs the getter, which yields a + 1 (which is 1)
    

### [Using a computed property name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#using_a_computed_property_name)

js

    const expr = "foo";
    
    const obj = {
      get [expr]() {
        return "bar";
      },
    };
    
    console.log(obj.foo); // "bar"
    

### [Defining static getters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#defining_static_getters)

js

    class MyConstants {
      static get foo() {
        return "foo";
      }
    }
    
    console.log(MyConstants.foo); // 'foo'
    MyConstants.foo = "bar";
    console.log(MyConstants.foo); // 'foo', a static getter's value cannot be changed
    

### [Smart / self-overwriting / lazy getters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#smart_self-overwriting_lazy_getters)

Getters give you a way to _define_ a property of an object, but they do not _calculate_ the property's value until it is accessed. A getter defers the cost of calculating the value until the value is needed. If it is never needed, you never pay the cost.

An additional optimization technique to lazify or delay the calculation of a property value and cache it for later access is _smart_ (or _[memoized](https://developer.mozilla.org/en-US/docs/Glossary/Memoization)
_) getters. The value is calculated the first time the getter is called and is then cached so subsequent accesses return the cached value without recalculating it. This is useful in the following situations:

*   If the calculation of a property value is expensive (takes much RAM or CPU time, spawns worker threads, retrieves remote file, etc.).
*   If the value isn't needed just now. It will be used later, or in some cases, it's not used at all.
*   If it's used, it will be accessed several times, and there is no need to re-calculate that value because it will never be changed or shouldn't be re-calculated.

**Note:** This means that you shouldn't write a lazy getter for a property whose value you expect to change, because if the getter is lazy, then it will not recalculate the value.

Note that getters are not "lazy" or "[memoized](https://developer.mozilla.org/en-US/docs/Glossary/Memoization)
" by nature; you must implement this technique if you desire this behavior.

In the following example, the object has a getter as its own property. On getting the property, the property is removed from the object and re-added, but implicitly as a data property this time. Finally, the value gets returned.

js

    const obj = {
      get notifier() {
        delete this.notifier;
        this.notifier = document.getElementById("bookmarked-notification-anchor");
        return this.notifier;
      },
    };
    

### [Feature detection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#feature_detection)

Many functions accept an object and retrieve individual properties from it as separate parameters (this object parameter is known as an _options bag_). You can detect whether a specific option is supported by using a getter to track if the property has been retrieved. This example checks if the `colorType` option is supported by the [`HTMLCanvasElement.getContext()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext)
 method.

js

    function isColorTypeSupported() {
      let supported = false;
      const obj = {
        get colorType() {
          supported = true;
          return undefined;
        },
      };
      document.createElement("canvas").getContext("2d", obj);
      return supported;
    }
    

### [get vs. defineProperty](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#get_vs._defineproperty)

While using the `get` keyword and [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 have similar results, there is a subtle difference between the two when used on [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
. The `get` syntax defines the property on the instance's prototype, while [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 defines the property on the instance it is applied to.

js

    class Example {
      get hello() {
        return "world";
      }
    }
    
    const obj = new Example();
    console.log(obj.hello);
    // "world"
    
    console.log(Object.getOwnPropertyDescriptor(obj, "hello"));
    // undefined
    
    console.log(
      Object.getOwnPropertyDescriptor(Object.getPrototypeOf(obj), "hello"),
    );
    // { configurable: true, enumerable: false, get: function get hello() { return 'world'; }, set: undefined }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-method-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-method-definitions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get#see_also)

-----------------------------------------------------------------------------------------------------

*   [Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [`set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
    
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

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/functions/get/index.md?plain=1 "Folder: en-us/web/javascript/reference/functions/get (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Fget&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Fget%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Fget%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Fget%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")