*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#mdn-search)
    

Reflect.getPrototypeOf()
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Reflect.getPrototypeOf()`** static method is like [`Object.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)
. It returns the prototype of the specified object.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#try_it)

-------------------------------------------------------------------------------------------------------------------------

    const object = {
      foo: 42,
    };
    
    const proto = Reflect.getPrototypeOf(object);
    
    console.log(proto);
    // Expected output: Object {  }
    
    console.log(Reflect.getPrototypeOf(proto));
    // Expected output: null
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#syntax)

-------------------------------------------------------------------------------------------------------------------------

js

    Reflect.getPrototypeOf(target)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#parameters)

[`target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#target)

The target object of which to get the prototype.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#return_value)

The prototype of the given object, which may be an object or `null`.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown if `target` is not an object.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#description)

-----------------------------------------------------------------------------------------------------------------------------------

`Reflect.getPrototypeOf()` provides the reflective semantic of retrieving the prototype of an object. The only difference with [`Object.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)
 is how non-object targets are handled. `Reflect.getPrototypeOf()` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 if the target is not an object, while `Object.getPrototypeOf()` coerces it to an object.

`Reflect.getPrototypeOf()` invokes the `[[GetPrototypeOf]]` [object internal method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy#object_internal_methods)
 of `target`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#examples)

-----------------------------------------------------------------------------------------------------------------------------

### [Using Reflect.getPrototypeOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#using_reflect.getprototypeof)

js

    Reflect.getPrototypeOf({}); // Object.prototype
    Reflect.getPrototypeOf(Object.prototype); // null
    Reflect.getPrototypeOf(Object.create(null)); // null
    

### [Difference with Object.getPrototypeOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#difference_with_object.getprototypeof)

js

    // Same result for Objects
    Object.getPrototypeOf({}); // Object.prototype
    Reflect.getPrototypeOf({}); // Object.prototype
    
    // Both throw in ES5 for non-Objects
    Object.getPrototypeOf("foo"); // Throws TypeError
    Reflect.getPrototypeOf("foo"); // Throws TypeError
    
    // In ES2015 only Reflect throws, Object coerces non-Objects
    Object.getPrototypeOf("foo"); // String.prototype
    Reflect.getPrototypeOf("foo"); // Throws TypeError
    
    // To mimic the Object ES2015 behavior you need to coerce
    Reflect.getPrototypeOf(Object("foo")); // String.prototype
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-reflect.getprototypeof](https://tc39.es/ecma262/multipage/reflection.html#sec-reflect.getprototypeof) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf#see_also)

-----------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Reflect.getPrototypeOf` in `core-js`](https://core-js.io/docs/features/ecmascript/reflect "External link (opens in new tab)")
    
*   [es-shims polyfill of `Reflect.getPrototypeOf`](https://www.npmjs.com/package/reflect.getprototypeof "External link (opens in new tab)")
    
*   [`Reflect`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect)
    
*   [`Object.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)
    
*   [`handler.getPrototypeOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/getPrototypeOf)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/getPrototypeOf/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/reflect/getprototypeof/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/reflect/getprototypeof (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FReflect%2FgetPrototypeOf&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Freflect%2Fgetprototypeof%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FReflect%2FgetPrototypeOf%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Freflect%2Fgetprototypeof%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")