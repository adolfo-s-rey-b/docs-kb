*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#mdn-search)
    

Object.setPrototypeOf()
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Object.setPrototypeOf()`** static method sets the prototype (i.e., the internal `[[Prototype]]` property) of a specified object to another object or [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
.

**Warning:** Changing the `[[Prototype]]` of an object is, by the nature of how modern JavaScript engines optimize property accesses, currently a very slow operation in every browser and JavaScript engine. In addition, the effects of altering inheritance are subtle and far-flung, and are not limited to the time spent in the `Object.setPrototypeOf(...)` statement, but may extend to **_any_** code that has access to any object whose `[[Prototype]]` has been altered. You can read more in [JavaScript engine fundamentals: optimizing prototypes](https://mathiasbynens.be/notes/prototypes "External link (opens in new tab)")
.

Because this feature is a part of the language, it is still the burden on engine developers to implement that feature performantly (ideally). Until engine developers address this issue, if you are concerned about performance, you should avoid setting the `[[Prototype]]` of an object. Instead, create a new object with the desired `[[Prototype]]` using [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#try_it)

------------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#syntax)

------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#parameters)

[`obj`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#obj)

The object which is to have its prototype set.

[`prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#prototype)

The object's new prototype (an object or [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
).

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#return_value)

The specified object.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown in one of the following cases:

*   The `obj` parameter is `undefined` or `null`.
*   The `obj` parameter is [non-extensible](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isExtensible)
    , or it's an [immutable prototype exotic object](https://tc39.es/ecma262/multipage/ordinary-and-exotic-objects-behaviours.html#sec-immutable-prototype-exotic-objects "External link (opens in new tab)")
    , such as `Object.prototype` or [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
    . However, the error is not thrown if the new prototype is the same value as the original prototype of `obj`.
*   The `prototype` parameter is not an object or [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
    .

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#description)

----------------------------------------------------------------------------------------------------------------------------------

`Object.setPrototypeOf()` is generally considered the proper way to set the prototype of an object. You should always use it in favor of the deprecated [`Object.prototype.__proto__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto)
 accessor.

If the `obj` parameter is not an object (e.g., number, string, etc.), this method does nothing — without coercing it to an object or attempting to set its prototype — and directly returns `obj` as a primitive value. If `prototype` is the same value as the prototype of `obj`, then `obj` is directly returned, without causing a `TypeError` even when `obj` has immutable prototype.

For security concerns, there are certain built-in objects that are designed to have an _immutable prototype_. This prevents [prototype pollution attacks](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Prototype_pollution)
, especially [proxy-related ones](https://github.com/tc39/ecma262/issues/272 "External link (opens in new tab)")
. The core language only specifies `Object.prototype` as an immutable prototype exotic object, whose prototype is always `null`. In browsers, [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 and [`location`](https://developer.mozilla.org/en-US/docs/Web/API/Window/location)
 are two other very common examples.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#examples)

----------------------------------------------------------------------------------------------------------------------------

### [Pseudoclassical inheritance using Object.setPrototypeOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#pseudoclassical_inheritance_using_object.setprototypeof)

Inheritance in JS using classes.

However, if we want to implement subclasses without using `class`, we can do the following:

The similarity between classical inheritance (with classes) and pseudoclassical inheritance (with constructors' `prototype` property) as done above is mentioned in [Inheritance chains](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain#building_longer_inheritance_chains)
.

Since function constructors' [`prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)
 property is writable, you can reassign it to a new object created with [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create#classical_inheritance_with_object.create)
 to achieve the same inheritance chain as well. There are caveats to watch out when using `create()`, such as remembering to re-add the [`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)
 property.

In the example below, which also uses classes, `SuperHero` is made to inherit from `Human` without using `extends` by using `setPrototypeOf()` instead.

**Warning:** It is not advisable to use `setPrototypeOf()` instead of `extends` due to performance and readability reasons.

Subclassing without `extends` is mentioned in [ES-6 subclassing](https://hacks.mozilla.org/2015/08/es6-in-depth-subclassing/ "External link (opens in new tab)")
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#specifications)

----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-object.setprototypeof](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-object.setprototypeof) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Object.setPrototypeOf` in `core-js`](https://core-js.io/docs/features/ecmascript/object "External link (opens in new tab)")
    
*   [`Reflect.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/setPrototypeOf)
    
*   [`Object.prototype.isPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isPrototypeOf)
    
*   [`Object.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)
    
*   [`Object.prototype.__proto__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto)
    
*   [Inheritance chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain#building_longer_inheritance_chains)
    
*   [ES6 In Depth: Subclassing](https://hacks.mozilla.org/2015/08/es6-in-depth-subclassing/ "External link (opens in new tab)")
     on hacks.mozilla.org (2015)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/object/setprototypeof/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/object/setprototypeof (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FsetPrototypeOf&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Fsetprototypeof%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2FsetPrototypeOf%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fobject%2Fsetprototypeof%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")