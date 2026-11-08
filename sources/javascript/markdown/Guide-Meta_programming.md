*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#mdn-search)
    

Meta programming
================

The [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
 and [`Reflect`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect)
 objects allow you to intercept and define custom behavior for fundamental language operations (e.g., property lookup, assignment, enumeration, function invocation, etc.). With the help of these two objects you are able to program at the meta level of JavaScript.

[Proxies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#proxies)

--------------------------------------------------------------------------------------------------

[`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
 objects allow you to intercept certain operations and to implement custom behaviors.

For example, getting a property on an object:

The `Proxy` object defines a `target` (an empty object here) and a `handler` object, in which a `get` _trap_ is implemented. Here, an object that is proxied will not return `undefined` when getting undefined properties, but will instead return the number `42`.

Additional examples are available on the [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
 reference page.

### [Terminology](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#terminology)

The following terms are used when talking about the functionality of proxies.

[handler](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy)

Placeholder object which contains traps.

[traps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#traps)

The methods that provide property access. (This is analogous to the concept of _traps_ in operating systems.)

[target](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#target)

Object which the proxy virtualizes. It is often used as storage backend for the proxy. Invariants (semantics that remain unchanged) regarding object non-extensibility or non-configurable properties are verified against the target.

[invariants](https://developer.mozilla.org/en-US/docs/Glossary/Invariant)

Semantics that remain unchanged when implementing custom operations are called _invariants_. If you violate the invariants of a handler, a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 will be thrown.

[Handlers and traps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#handlers_and_traps)

------------------------------------------------------------------------------------------------------------------------

The following table summarizes the available traps available to `Proxy` objects. See the [reference pages](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy)
 for detailed explanations and examples.

| Handler / trap | Interceptions |
| --- | --- |
| [`handler.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/getPrototypeOf) | [`Object.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)<br>  <br>[`Reflect.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf)<br>  <br>[`__proto__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto)<br>  <br>[`Object.prototype.isPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isPrototypeOf)<br>  <br>[`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof) |
| [`handler.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/setPrototypeOf) | [`Object.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)<br>  <br>[`Reflect.setPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/setPrototypeOf) |
| [`handler.isExtensible()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/isExtensible) | [`Object.isExtensible()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isExtensible)<br>  <br>[`Reflect.isExtensible()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/isExtensible) |
| [`handler.preventExtensions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/preventExtensions) | [`Object.preventExtensions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/preventExtensions)<br>  <br>[`Reflect.preventExtensions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/preventExtensions) |
| [`handler.getOwnPropertyDescriptor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/getOwnPropertyDescriptor) | [`Object.getOwnPropertyDescriptor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptor)<br>  <br>[`Reflect.getOwnPropertyDescriptor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getOwnPropertyDescriptor) |
| [`handler.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/defineProperty) | [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)<br>  <br>[`Reflect.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/defineProperty) |
| [`handler.has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/has) | [Property query](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#property_query)<br><br>`foo in proxy`<br><br>[Inherited property query](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#inherited_property_query)<br><br>`foo in Object.create(proxy)`  <br>[`Reflect.has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/has) |
| [`handler.get()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/get) | [Property access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#property_access)<br><br>`proxy[foo]`  <br>`proxy.bar`<br><br>[Inherited property access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#inherited_property_access)<br><br>`Object.create(proxy)[foo]`  <br>[`Reflect.get()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/get) |
| [`handler.set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/set) | [Property assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#property_assignment)<br><br>`proxy[foo] = bar`  <br>`proxy.foo = bar`<br><br>[Inherited property assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#inherited_property_assignment)<br><br>`Object.create(proxy)[foo] = bar`  <br>[`Reflect.set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/set) |
| [`handler.deleteProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/deleteProperty) | [Property deletion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#property_deletion)<br><br>`delete proxy[foo]`  <br>`delete proxy.foo`  <br>[`Reflect.deleteProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/deleteProperty) |
| [`handler.ownKeys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/ownKeys) | [`Object.getOwnPropertyNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames)<br>  <br>[`Object.getOwnPropertySymbols()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols)<br>  <br>[`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)<br>  <br>[`Reflect.ownKeys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/ownKeys) |
| [`handler.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/apply) | `proxy(..args)`  <br>[`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)<br> and [`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)<br>  <br>[`Reflect.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/apply) |
| [`handler.construct()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/construct) | `new proxy(...args)`  <br>[`Reflect.construct()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/construct) |

[Revocable `Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#revocable_proxy)

--------------------------------------------------------------------------------------------------------------------

The [`Proxy.revocable()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable)
 method is used to create a revocable `Proxy` object. This means that the proxy can be revoked via the function `revoke` and switches the proxy off.

Afterwards, any operation on the proxy leads to a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

[Reflection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#reflection)

--------------------------------------------------------------------------------------------------------

[`Reflect`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect)
 is a built-in object that provides methods for interceptable JavaScript operations. The methods are the same as those of the [proxy handler's](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy)
.

`Reflect` is not a function object.

`Reflect` helps with forwarding default operations from the handler to the `target`.

With [`Reflect.has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/has)
 for example, you get the [`in` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 as a function:

### [A better apply() function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#a_better_apply_function)

Before `Reflect`, you typically use the [`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
 method to call a function with a given `this` value and `arguments` provided as an array (or an [array-like object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections#working_with_array-like_objects)
).

With [`Reflect.apply`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/apply)
 this becomes less verbose and easier to understand:

### [Checking if property definition has been successful](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming#checking_if_property_definition_has_been_successful)

With [`Object.defineProperty`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
, which returns an object if successful, or throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 otherwise, you would use a [`try...catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
 block to catch any error that occurred while defining a property. Because [`Reflect.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/defineProperty)
 returns a Boolean success status, you can just use an [`if...else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
 block here:

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/meta_programming/index.md?plain=1 "Folder: en-us/web/javascript/guide/meta_programming (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FMeta_programming&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fmeta_programming%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FMeta_programming%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fmeta_programming%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1ddd95504b4507beeda0f08bd772eb167922b86a%0A*+Document+last+modified%3A+2026-05-22T15%3A48%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")