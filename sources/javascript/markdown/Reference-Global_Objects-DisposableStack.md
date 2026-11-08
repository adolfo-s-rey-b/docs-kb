*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#mdn-search)
    

DisposableStack
===============

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/366)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`DisposableStack`** object represents a stack of [disposers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
 to run when the stack itself is disposed. Disposer functions are executed in reverse order of registration, with strong error handling guarantees. Calling its `move()` method will transfer responsibility for calling the current registered disposers to a new `DisposableStack` and prevent registering any additional disposers.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#description)

----------------------------------------------------------------------------------------------------------------------------

A `DisposableStack` is not exactly a "stack" in terms of its interface. It has several methods for pushing disposers to it, but it has no way to pop one disposer off. Rather, _all_ disposers are popped and executed one-by-one when the stack is disposed.

You register [disposable resources](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management)
 to the `DisposableStack` using its [`use()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/use)
, [`adopt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/adopt)
, or [`defer()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/defer)
 methods.

js

    using disposer = new DisposableStack();
    const reader = disposer.use(stream.getReader());
    

Then, when the `disposer` goes out of scope, all resources registered to it are disposed in reverse order of registration, unless they have been moved out with `move()`.

It is good practice to _not_ extract the resource acquisition expression to a separate statement, no matter how long the expression is. You should always wrap the `use()` or `adopt()` call around the resource acquisition expression to ensure that the resource is registered to the stack immediately.

js

    using disposer = new DisposableStack();
    const reader = stream.getReader();
    disposer.use(reader);
    

Functionally, these two code snippets are equivalent. However, the first one is less error-prone because the resource is declared and registered in a single line. If someone puts more code between the second and third lines of the second snippet, an error could occur, causing the resource to leak.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#constructor)

----------------------------------------------------------------------------------------------------------------------------

[`DisposableStack()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/DisposableStack)

Creates a new `DisposableStack` object.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#instance_properties)

--------------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `DisposableStack.prototype` and shared by all `DisposableStack` instances.

[`DisposableStack.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `DisposableStack` instances, the initial value is the [`DisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/DisposableStack)
 constructor.

[`DisposableStack.prototype.disposed`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/disposed)

Read-only. Returns `true` if the `DisposableStack` has been disposed, or `false` if not.

[`DisposableStack.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#disposablestack.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"DisposableStack"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#instance_methods)

--------------------------------------------------------------------------------------------------------------------------------------

[`DisposableStack.prototype.adopt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/adopt)

Registers a value that doesn't implement the disposable protocol to the stack by providing a custom disposer function.

[`DisposableStack.prototype.defer()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/defer)

Takes a callback function to be called when the stack is disposed.

[`DisposableStack.prototype.dispose()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/dispose)

Disposes this stack by calling all disposers registered to it in reverse order of registration.

[`DisposableStack.prototype.move()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/move)

Creates a new `DisposableStack` instance that contains the same disposers as this stack, and then marks this stack as disposed, without calling any disposers.

[`DisposableStack.prototype.use()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/use)

Registers a value that implements the disposable protocol to the stack.

[`DisposableStack.prototype[Symbol.dispose]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/Symbol.dispose)

An alias for the `dispose()` method.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript Async Explicit Resource Management  <br>\# sec-disposablestack-objects](https://tc39.es/proposal-async-explicit-resource-management/#sec-disposablestack-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `DisposableStack` in `core-js`](https://core-js.io/docs/features/ecmascript/explicit-resource-management "External link (opens in new tab)")
    
*   [JavaScript resource management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Resource_management)
    
*   [`Symbol.dispose`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/dispose)
    
*   [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
    
*   [`AsyncDisposableStack`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncDisposableStack)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DisposableStack/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/disposablestack/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/disposablestack (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDisposableStack&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdisposablestack%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDisposableStack%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdisposablestack%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")