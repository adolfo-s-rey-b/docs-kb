*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#mdn-search)
    

handler.set()
=============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`handler.set()`** method is a trap for the `[[Set]]` [object internal method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy#object_internal_methods)
, which is used by operations such as using [property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
 to set a property's value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#try_it)

------------------------------------------------------------------------------------------------------------------

    const monster = { eyeCount: 4 };
    
    const handler = {
      set(obj, prop, value) {
        if (prop === "eyeCount" && value % 2 !== 0) {
          console.log("Monsters must have an even number of eyes");
        } else {
          return Reflect.set(...arguments);
        }
      },
    };
    
    const proxy = new Proxy(monster, handler);
    
    proxy.eyeCount = 1;
    // Expected output: "Monsters must have an even number of eyes"
    
    console.log(proxy.eyeCount);
    // Expected output: 4
    
    proxy.eyeCount = 2;
    console.log(proxy.eyeCount);
    // Expected output: 2
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#syntax)

------------------------------------------------------------------------------------------------------------------

js

    new Proxy(target, {
      set(target, property, value, receiver) {
      }
    })
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#parameters)

The following parameters are passed to the `set()` method. `this` is bound to the handler.

[`target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#target)

The target object.

[`property`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#property)

A string or [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
 representing the property name.

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#value)

The new value of the property to set.

[`receiver`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#receiver)

The `this` value for setters; see [`Reflect.set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/set)
. This is usually either the proxy itself or an object that inherits from the proxy.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#return_value)

The `set()` method must return a [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
 indicating whether or not the assignment succeeded. Other values are [coerced to booleans](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean#boolean_coercion)
.

Many operations, including using property accessors in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 if the `[[Set]]` internal method returns `false`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#description)

----------------------------------------------------------------------------------------------------------------------------

### [Interceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#interceptions)

This trap can intercept these operations:

*   Property assignment: `proxy[foo] = bar` and `proxy.foo = bar`
*   [`Reflect.set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/set)
    

Or any other operation that invokes the `[[Set]]` [internal method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy#object_internal_methods)
.

### [Invariants](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#invariants)

The proxy's `[[Set]]` internal method throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 if the handler definition violates one of the following invariants:

*   Cannot change the value of a property to be different from the value of the corresponding target object property, if the corresponding target object property is a non-writable, non-configurable own data property. That is, if [`Reflect.getOwnPropertyDescriptor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getOwnPropertyDescriptor)
     returns `configurable: false, writable: false` for the property on `target`, and `value` is different from the `value` attribute in the `target`'s property descriptor, then the trap must return a falsy value.
*   Cannot set the value of a property if the corresponding target object property is a non-configurable own accessor property that has an undefined setter. That is, if [`Reflect.getOwnPropertyDescriptor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getOwnPropertyDescriptor)
     returns `configurable: false, set: undefined` for the property on `target`, then the trap must return a falsy value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#examples)

----------------------------------------------------------------------------------------------------------------------

### [Trap setting of a property value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#trap_setting_of_a_property_value)

The following code traps setting a property value.

js

    const p = new Proxy(
      {},
      {
        set(target, prop, value, receiver) {
          target[prop] = value;
          console.log(`property set: ${prop} = ${value}`);
          return true;
        },
      },
    );
    
    console.log("a" in p); // false
    
    p.a = 10; // "property set: a = 10"
    console.log("a" in p); // true
    console.log(p.a); // 10
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-proxy-object-internal-methods-and-internal-slots-set-p-v-receiver](https://tc39.es/ecma262/multipage/ordinary-and-exotic-objects-behaviours.html#sec-proxy-object-internal-methods-and-internal-slots-set-p-v-receiver) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
    
*   [`Proxy()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy)
    
*   [`Reflect.set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/set)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 20, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/proxy/proxy/set/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/proxy/proxy/set (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FProxy%2FProxy%2Fset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fproxy%2Fproxy%2Fset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FProxy%2FProxy%2Fset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fproxy%2Fproxy%2Fset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd22b9f18cf2450c0cc488379b8b780f0f343397%0A*+Document+last+modified%3A+2025-07-20T13%3A51%3A13.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")