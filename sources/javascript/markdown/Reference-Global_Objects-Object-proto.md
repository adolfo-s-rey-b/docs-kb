*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#mdn-search)
    

Object.prototype.\_\_proto\_\_
==============================

Deprecated

Avoid using this feature in new projects. Changing `__proto__` is slow and can cause surprising bugs. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Warning:** Changing the `[[Prototype]]` of an object is, by the nature of how modern JavaScript engines optimize property accesses, currently a very slow operation in every browser and JavaScript engine. In addition, the effects of altering inheritance are subtle and far-flung, and are not limited to the time spent in the `obj.__proto__ = ...` statement, but may extend to **_any_** code that has access to any object whose `[[Prototype]]` has been altered. You can read more in [JavaScript engine fundamentals: optimizing prototypes](https://mathiasbynens.be/notes/prototypes "External link (opens in new tab)")
.

**Note:** The use of `__proto__` is controversial and discouraged. Its existence and exact behavior have only been standardized as a legacy feature to ensure web compatibility, while it presents several [security issues](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Prototype_pollution)
 and footguns. For better support, prefer [`Object.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)
/[`Reflect.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf)
 and [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
/[`Reflect.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/setPrototypeOf)
 instead.

The **`__proto__`** accessor property of [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
 instances exposes the [`[[Prototype]]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 (either an object or [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
) of this object.

The `__proto__` property can also be used in an object literal definition to set the object `[[Prototype]]` on creation, as an alternative to [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
. See: [object initializer / literal syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
. That syntax is standard and optimized for in implementations, and quite different from `Object.prototype.__proto__`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#syntax)

---------------------------------------------------------------------------------------------------------------

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#return_value)

If used as a getter, returns the object's `[[Prototype]]`.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown if attempting to set the prototype of a [non-extensible](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isExtensible)
 object or an [immutable prototype exotic object](https://tc39.es/ecma262/multipage/ordinary-and-exotic-objects-behaviours.html#sec-immutable-prototype-exotic-objects "External link (opens in new tab)")
, such as `Object.prototype` or [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#description)

-------------------------------------------------------------------------------------------------------------------------

The `__proto__` getter function exposes the value of the internal `[[Prototype]]` of an object. For objects created using an object literal (unless you use the [prototype setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#prototype_setter)
 syntax), this value is `Object.prototype`. For objects created using array literals, this value is [`Array.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
. For functions, this value is [`Function.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)
. You can read more about the prototype chain in [Inheritance and the prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
.

The `__proto__` setter allows the `[[Prototype]]` of an object to be mutated. The value provided must be an object or [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
. Providing any other value will do nothing.

Unlike [`Object.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)
 and [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
, which are always available on `Object` as static properties and always reflect the `[[Prototype]]` internal property, the `__proto__` property doesn't always exist as a property on all objects, and as a result doesn't reflect `[[Prototype]]` reliably.

The `__proto__` property is just an accessor property on `Object.prototype` consisting of a getter and setter function. A property access for `__proto__` that eventually consults `Object.prototype` will find this property, but an access that does not consult `Object.prototype` will not. If some other `__proto__` property is found before `Object.prototype` is consulted, that property will hide the one found on `Object.prototype`.

[`null`\-prototype objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#null-prototype_objects)
 don't inherit any property from `Object.prototype`, including the `__proto__` accessor property, so if you try to read `__proto__` on such an object, the value is always `undefined` regardless of the object's actual `[[Prototype]]`, and any assignment to `__proto__` would create a new property called `__proto__` instead of setting the object's prototype. Furthermore, `__proto__` can be redefined as an own property on any object instance through [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 without triggering the setter. In this case, `__proto__` will no longer be an accessor for `[[Prototype]]`. Therefore, always prefer [`Object.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)
 and [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
 for setting and getting the `[[Prototype]]` of an object.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#examples)

-------------------------------------------------------------------------------------------------------------------

### [Using \_\_proto\_\_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#using___proto__)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-object.prototype.\_\_proto\_\_](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-object.prototype.__proto__) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`Object.prototype.isPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isPrototypeOf)
    
*   [`Object.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)
    
*   [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
    
*   [Prototype pollution attack](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Prototype_pollution)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/object/proto/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/object/proto (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fproto&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Fproto%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fproto%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Fproto%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")