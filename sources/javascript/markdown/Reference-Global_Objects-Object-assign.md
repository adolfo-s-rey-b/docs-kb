*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#mdn-search)
    

Object.assign()
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Object.assign()`** static method copies all [enumerable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/propertyIsEnumerable)
 [own properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn)
 from one or more _source objects_ to a _target object_. It returns the modified target object.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#try_it)

----------------------------------------------------------------------------------------------------------------

    const target = { a: 1, b: 2 };
    const source = { b: 4, c: 5 };
    
    const returnedTarget = Object.assign(target, source);
    
    console.log(target);
    // Expected output: Object { a: 1, b: 4, c: 5 }
    
    console.log(returnedTarget === target);
    // Expected output: true
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#syntax)

----------------------------------------------------------------------------------------------------------------

js

    Object.assign(target)
    Object.assign(target, source1)
    Object.assign(target, source1, source2)
    Object.assign(target, source1, source2, /* …, */ sourceN)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#parameters)

[`target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#target)

The target object — what to apply the sources' properties to, which is returned after it is modified. If a primitive value is provided as the target, it will be converted to an object.

[`source1`, …, `sourceN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#source1)

The source object(s) — objects containing the properties you want to apply.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#return_value)

The target object.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown in one of the following cases:

*   The `target` parameter is [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
     or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
    .
*   Assignment of a property on the target object fails; for example, because the property is non-writable on the target object, or because its setter throws an error.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#description)

--------------------------------------------------------------------------------------------------------------------------

Properties in the target object are overwritten by properties in the sources if they have the same [key](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
. Later sources' properties overwrite earlier ones.

The `Object.assign()` method only copies _enumerable_ and _own_ properties from a source object to a target object. It uses `[[Get]]` on the source and `[[Set]]` on the target, so it will invoke [getters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 and [setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
. Therefore it _assigns_ properties, versus copying or defining new properties. This may make it unsuitable for merging new properties into a prototype if the merge sources contain getters.

For copying property definitions (including their enumerability) into prototypes, use [`Object.getOwnPropertyDescriptor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptor)
 and [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 instead.

Both [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 and [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
 properties are copied.

In case of an error, for example if a property is non-writable, a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 is raised, and the `target` object is changed if any properties are added before the error is raised.

**Note:** `Object.assign()` does not throw on [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 sources.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#examples)

--------------------------------------------------------------------------------------------------------------------

### [Cloning an object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#cloning_an_object)

js

    const obj = { a: 1 };
    const copy = Object.assign({}, obj);
    console.log(copy); // { a: 1 }
    

### [Warning for deep clone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#warning_for_deep_clone)

For [deep cloning](https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy)
, we need to use alternatives like [`structuredClone()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone "structuredClone()")
, because `Object.assign()` copies property values.

If the source value is a reference to an object, it only copies the reference value.

js

    const obj1 = { a: 0, b: { c: 0 } };
    const obj2 = Object.assign({}, obj1);
    console.log(obj2); // { a: 0, b: { c: 0 } }
    
    obj1.a = 1;
    console.log(obj1); // { a: 1, b: { c: 0 } }
    console.log(obj2); // { a: 0, b: { c: 0 } }
    
    obj2.a = 2;
    console.log(obj1); // { a: 1, b: { c: 0 } }
    console.log(obj2); // { a: 2, b: { c: 0 } }
    
    obj2.b.c = 3;
    console.log(obj1); // { a: 1, b: { c: 3 } }
    console.log(obj2); // { a: 2, b: { c: 3 } }
    
    // Deep Clone
    const obj3 = { a: 0, b: { c: 0 } };
    const obj4 = structuredClone(obj3);
    obj3.a = 4;
    obj3.b.c = 4;
    console.log(obj4); // { a: 0, b: { c: 0 } }
    

### [Merging objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#merging_objects)

js

    const o1 = { a: 1 };
    const o2 = { b: 2 };
    const o3 = { c: 3 };
    
    const obj = Object.assign(o1, o2, o3);
    console.log(obj); // { a: 1, b: 2, c: 3 }
    console.log(o1); // { a: 1, b: 2, c: 3 }, target object itself is changed.
    

### [Merging objects with same properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#merging_objects_with_same_properties)

js

    const o1 = { a: 1, b: 1, c: 1 };
    const o2 = { b: 2, c: 2 };
    const o3 = { c: 3 };
    
    const obj = Object.assign({}, o1, o2, o3);
    console.log(obj); // { a: 1, b: 2, c: 3 }
    

The properties are overwritten by other objects that have the same properties later in the parameters order.

### [Copying symbol-typed properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#copying_symbol-typed_properties)

js

    const o1 = { a: 1 };
    const o2 = { [Symbol("foo")]: 2 };
    
    const obj = Object.assign({}, o1, o2);
    console.log(obj); // { a : 1, [Symbol("foo")]: 2 } (cf. bug 1207182 on Firefox)
    Object.getOwnPropertySymbols(obj); // [Symbol(foo)]
    

### [Properties on the prototype chain and non-enumerable properties cannot be copied](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#properties_on_the_prototype_chain_and_non-enumerable_properties_cannot_be_copied)

js

    const obj = Object.create(
      // foo is on obj's prototype chain.
      { foo: 1 },
      {
        bar: {
          value: 2, // bar is a non-enumerable property.
        },
        baz: {
          value: 3,
          enumerable: true, // baz is an own enumerable property.
        },
      },
    );
    
    const copy = Object.assign({}, obj);
    console.log(copy); // { baz: 3 }
    

### [Primitives will be wrapped to objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#primitives_will_be_wrapped_to_objects)

js

    const v1 = "abc";
    const v2 = true;
    const v3 = 10;
    const v4 = Symbol("foo");
    
    const obj = Object.assign({}, v1, null, v2, undefined, v3, v4);
    // Primitives will be wrapped, null and undefined will be ignored.
    // Note, only string wrappers can have own enumerable properties.
    console.log(obj); // { "0": "a", "1": "b", "2": "c" }
    
    // Primitives as the target are also wrapped to objects
    const number = Object.assign(3, { a: 1 });
    console.log(number); // Number {3, a: 1}
    console.log(typeof number); // object
    console.log(number.a); // 1
    
    // null and undefined as targets throw TypeError
    try {
      Object.assign(null, { a: 1 });
    } catch (e) {
      console.log(e.message); // "Cannot convert undefined or null to object"
    }
    

### [Exceptions will interrupt the ongoing copying task](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#exceptions_will_interrupt_the_ongoing_copying_task)

js

    const target = Object.defineProperty({}, "foo", {
      value: 1,
      writable: false,
    }); // target.foo is a read-only property
    
    Object.assign(target, { bar: 2 }, { foo2: 3, foo: 3, foo3: 3 }, { baz: 4 });
    // TypeError: "foo" is read-only
    // The Exception is thrown when assigning target.foo
    
    console.log(target.bar); // 2, the first source was copied successfully.
    console.log(target.foo2); // 3, the first property of the second source was copied successfully.
    console.log(target.foo); // 1, exception is thrown here.
    console.log(target.foo3); // undefined, assign method has finished, foo3 will not be copied.
    console.log(target.baz); // undefined, the third source will not be copied either.
    

### [Copying accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#copying_accessors)

js

    const obj = {
      foo: 1,
      get bar() {
        return 2;
      },
    };
    
    let copy = Object.assign({}, obj);
    console.log(copy);
    // { foo: 1, bar: 2 }
    // The value of copy.bar is obj.bar's getter's return value.
    
    // This is an assign function that copies full descriptors
    function completeAssign(target, ...sources) {
      sources.forEach((source) => {
        const descriptors = Object.keys(source).reduce((descriptors, key) => {
          descriptors[key] = Object.getOwnPropertyDescriptor(source, key);
          return descriptors;
        }, {});
    
        // By default, Object.assign copies enumerable Symbols, too
        Object.getOwnPropertySymbols(source).forEach((sym) => {
          const descriptor = Object.getOwnPropertyDescriptor(source, sym);
          if (descriptor.enumerable) {
            descriptors[sym] = descriptor;
          }
        });
        Object.defineProperties(target, descriptors);
      });
      return target;
    }
    
    copy = completeAssign({}, obj);
    console.log(copy);
    // { foo:1, get bar() { return 2 } }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-object.assign](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-object.assign) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Object.assign` in `core-js`](https://core-js.io/docs/features/ecmascript/object "External link (opens in new tab)")
    
*   [es-shims polyfill of `Object.assign`](https://www.npmjs.com/package/object.assign "External link (opens in new tab)")
    
*   [`Object.defineProperties()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperties)
    
*   [Enumerability and ownership of properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
    
*   [Spread in object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/object/assign/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/object/assign (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fassign&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Fassign%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fassign%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Fassign%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")