*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#mdn-search)
    

Object.freeze()
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Object.freeze()`** static method _freezes_ an object. Freezing an object [prevents extensions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/preventExtensions)
 and makes existing properties non-writable and non-configurable. A frozen object can no longer be changed: new properties cannot be added, existing properties cannot be removed, their enumerability, configurability, writability, or value cannot be changed, and the object's prototype cannot be re-assigned. `freeze()` returns the same object that was passed in.

Freezing an object is the highest integrity level that JavaScript provides.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#try_it)

----------------------------------------------------------------------------------------------------------------

    const obj = {
      prop: 42,
    };
    
    Object.freeze(obj);
    
    obj.prop = 33;
    // Throws an error in strict mode
    
    console.log(obj.prop);
    // Expected output: 42
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#syntax)

----------------------------------------------------------------------------------------------------------------

js

    Object.freeze(obj)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#parameters)

[`obj`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#obj)

The object to freeze.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#return_value)

The object that was passed to the function.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#description)

--------------------------------------------------------------------------------------------------------------------------

Freezing an object is equivalent to [preventing extensions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/preventExtensions)
 and then changing all existing [properties' descriptors'](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty#description)
 `configurable` to `false` — and for data properties, `writable` to `false` as well. Nothing can be added to or removed from the properties set of a frozen object. Any attempt to do so will fail, either silently or by throwing a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 exception (most commonly, but not exclusively, when in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
).

For data properties of a frozen object, their values cannot be changed since the `writable` and `configurable` attributes are set to `false`. Accessor properties (getters and setters) work the same — the property value returned by the getter may still change, and the setter can still be called without throwing errors when setting the property. Note that values that are objects can still be modified, unless they are also frozen. As an object, an array can be frozen; after doing so, its elements cannot be altered and no elements can be added to or removed from the array.

[Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 are not properties and do not have the concept of property descriptors. Freezing an object with private elements does not prevent the values of these private elements from being changed. (Freezing objects is usually meant as a security measure against external code, but external code cannot access private elements anyway.) Private elements cannot be added or removed from the object, whether the object is frozen or not.

`freeze()` returns the same object that was passed into the function. It _does not_ create a frozen copy.

A [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
 or a [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)
 with elements will cause a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
, as they are views over memory and will definitely cause other possible issues:

js

    Object.freeze(new Uint8Array(0)); // No elements
    // Uint8Array []
    
    Object.freeze(new Uint8Array(1)); // Has elements
    // TypeError: Cannot freeze array buffer views with elements
    
    Object.freeze(new DataView(new ArrayBuffer(32))); // No elements
    // DataView {}
    
    Object.freeze(new Float64Array(new ArrayBuffer(64), 32, 0)); // No elements
    // Float64Array []
    
    Object.freeze(new Float64Array(new ArrayBuffer(64), 32, 2)); // Has elements
    // TypeError: Cannot freeze array buffer views with elements
    

Note that as the standard three properties (`buf.byteLength`, `buf.byteOffset` and `buf.buffer`) are read-only (as are those of an [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
 or [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)
), there is no reason for attempting to freeze these properties.

Unlike [`Object.seal()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal)
, existing properties in objects frozen with `Object.freeze()` are made immutable and data properties cannot be re-assigned.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#examples)

--------------------------------------------------------------------------------------------------------------------

### [Freezing objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#freezing_objects)

js

    const obj = {
      prop() {},
      foo: "bar",
    };
    
    // Before freezing: new properties may be added,
    // and existing properties may be changed or removed
    obj.foo = "baz";
    obj.lumpy = "woof";
    delete obj.prop;
    
    // Freeze.
    const o = Object.freeze(obj);
    
    // The return value is just the same object we passed in.
    o === obj; // true
    
    // The object has become frozen.
    Object.isFrozen(obj); // === true
    
    // Now any changes will fail
    obj.foo = "quux"; // silently does nothing
    // silently doesn't add the property
    obj.quaxxor = "the friendly duck";
    
    // In strict mode such attempts will throw TypeErrors
    function fail() {
      "use strict";
      obj.foo = "sparky"; // throws a TypeError
      delete obj.foo; // throws a TypeError
      delete obj.quaxxor; // returns true since attribute 'quaxxor' was never added
      obj.sparky = "arf"; // throws a TypeError
    }
    
    fail();
    
    // Attempted changes through Object.defineProperty;
    // both statements below throw a TypeError.
    Object.defineProperty(obj, "ohai", { value: 17 });
    Object.defineProperty(obj, "foo", { value: "eit" });
    
    // It's also impossible to change the prototype
    // both statements below will throw a TypeError.
    Object.setPrototypeOf(obj, { x: 20 });
    obj.__proto__ = { x: 20 };
    

### [Freezing arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#freezing_arrays)

js

    const a = [0];
    Object.freeze(a); // The array cannot be modified now.
    
    a[0] = 1; // fails silently
    
    // In strict mode such attempt will throw a TypeError
    function fail() {
      "use strict";
      a[0] = 1;
    }
    
    fail();
    
    // Attempted to push
    a.push(2); // throws a TypeError
    

The object being frozen is _immutable_. However, it is not necessarily _constant_. The following example shows that a frozen object is not constant (freeze is shallow).

js

    const obj1 = {
      internal: {},
    };
    
    Object.freeze(obj1);
    obj1.internal.a = "value";
    
    obj1.internal.a; // 'value'
    

To be a constant object, the entire reference graph (direct and indirect references to other objects) must reference only immutable frozen objects. The object being frozen is said to be immutable because the entire object _state_ (values and references to other objects) within the whole object is fixed. Note that strings, numbers, and booleans are always immutable and that Functions and Arrays are objects.

### [Deep freezing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#deep_freezing)

The result of calling `Object.freeze(object)` only applies to the immediate properties of `object` itself and will prevent future property addition, removal or value re-assignment operations _only_ on `object`. If the value of those properties are objects themselves, those objects are not frozen and may be the target of property addition, removal or value re-assignment operations.

js

    const employee = {
      name: "Mayank",
      designation: "Developer",
      address: {
        street: "Rohini",
        city: "Delhi",
      },
    };
    
    Object.freeze(employee);
    
    employee.name = "Dummy"; // fails silently in non-strict mode
    employee.address.city = "Noida"; // attributes of child object can be modified
    
    console.log(employee.address.city); // "Noida"
    

To make an object immutable, recursively freeze each non-primitive property (deep freeze). Use the pattern on a case-by-case basis based on your design when you know the object contains no [cycles](https://en.wikipedia.org/wiki/Cycle_(graph_theory) "External link (opens in new tab)")
 in the reference graph, otherwise an endless loop will be triggered. For example, functions created with the [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
 syntax have a [`prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)
 property with a `constructor` property that points to the function itself, so they have cycles by default. Other functions, such as [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
, can still be frozen.

An enhancement to `deepFreeze()` would be to store the objects it has already visited, so you can suppress calling `deepFreeze()` recursively when an object is in the process of being made immutable. For one example, see [using `WeakSet` to detect circular references](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet#detecting_circular_references)
. You still run a risk of freezing an object that shouldn't be frozen, such as [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
.

js

    function deepFreeze(object) {
      // Retrieve the property names defined on object
      const propNames = Reflect.ownKeys(object);
    
      // Freeze properties before freezing self
      for (const name of propNames) {
        const value = object[name];
    
        if ((value && typeof value === "object") || typeof value === "function") {
          deepFreeze(value);
        }
      }
    
      return Object.freeze(object);
    }
    
    const obj2 = {
      internal: {
        a: null,
      },
    };
    
    deepFreeze(obj2);
    
    obj2.internal.a = "anotherValue"; // fails silently in non-strict mode
    obj2.internal.a; // null
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-object.freeze](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-object.freeze) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [`Object.isFrozen()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isFrozen)
    
*   [`Object.preventExtensions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/preventExtensions)
    
*   [`Object.isExtensible()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isExtensible)
    
*   [`Object.seal()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal)
    
*   [`Object.isSealed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isSealed)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/object/freeze/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/object/freeze (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Ffreeze&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Ffreeze%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Ffreeze%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Ffreeze%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7aba7d7cba898fe4d4a88df73183bb05f71a19a2%0A*+Document+last+modified%3A+2026-05-02T02%3A35%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")