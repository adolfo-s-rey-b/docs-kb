*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#mdn-search)
    

Proxy.revocable()
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Proxy.revocable()`** static method creates a revocable [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
 object.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#syntax)

------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#parameters)

[`target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#target)

A target object to wrap with `Proxy`. It can be any sort of object, including a native array, a function, or even another proxy.

[`handler`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#handler)

An object whose properties are functions defining the behavior of `proxy` when an operation is performed on it.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#return_value)

A plain object with the following two properties:

[`proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#proxy)

A Proxy object exactly the same as one created with a [`new Proxy(target, handler)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy)
 call.

[`revoke`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#revoke)

A function with no parameters to revoke (switch off) the `proxy`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#description)

----------------------------------------------------------------------------------------------------------------------------

The `Proxy.revocable()` factory function is the same as the [`Proxy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy)
 constructor, except that in addition to creating a proxy object, it also creates a `revoke` function that can be called to disable the proxy. The proxy object and the `revoke` function are wrapped in a plain object.

The `revoke` function does not take any parameters, nor does it rely on the `this` value. The created `proxy` object is attached to the `revoke` function as a [private field](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 that the `revoke` function accesses on itself when called (the existence of the private field is not observable from the outside, but it has implications on how garbage collection happens). The `proxy` object is _not_ captured within the [closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures)
 of the `revoke` function (which will make garbage collection of `proxy` impossible if `revoke` is still alive).

After the `revoke()` function gets called, the proxy becomes unusable: any trap to a handler throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
. Once a proxy is revoked, it remains revoked, and calling `revoke()` again has no effect — in fact, the call to `revoke()` detaches the `proxy` object from the `revoke` function, so the `revoke` function will not be able to access the proxy again at all. If the proxy is not referenced elsewhere, it will then be eligible for garbage collection. The `revoke` function also detaches `target` and `handler` from the `proxy`, so if `target` is not referenced elsewhere, it will also be eligible for garbage collection, even when its proxy is still alive, since there's no longer a way to meaningfully interact with the target object.

Letting users interact with an object through a revocable proxy allows you to [control the lifetime](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management)
 of the object exposed to the user — you can make the object garbage-collectable even when the user is still holding a reference to its proxy.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#examples)

----------------------------------------------------------------------------------------------------------------------

### [Using Proxy.revocable()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#using_proxy.revocable)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-proxy.revocable](https://tc39.es/ecma262/multipage/reflection.html#sec-proxy.revocable) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/revocable/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/proxy/revocable/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/proxy/revocable (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FProxy%2Frevocable&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fproxy%2Frevocable%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FProxy%2Frevocable%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fproxy%2Frevocable%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")